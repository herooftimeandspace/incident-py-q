"""Configuration loading and normalization for Incident IQ clients."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Literal, cast
from urllib.parse import ParseResult, urlparse, urlunparse

from .exceptions import ConfigurationError

AuthMode = Literal["bearer", "raw"]


def _parse_dotenv(path: Path) -> dict[str, str]:
    """Parse a simple `.env` file using only the standard library.

    This intentionally supports a conservative subset of dotenv behavior:
    `KEY=value`, optional surrounding quotes, comments, and blank lines.
    """
    if not path.exists():
        return {}

    values: dict[str, str] = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip("'").strip('"')
        if key:
            values[key] = value
    return values


def _env_get(env: dict[str, str], key: str) -> str | None:
    value = env.get(key)
    if value is None:
        return None
    stripped = value.strip()
    return stripped if stripped else None


def _normalize_base_url(base_url: str) -> str:
    parsed = urlparse(base_url)
    if parsed.scheme.lower() != "https":
        raise ConfigurationError("base_url must use https.")
    if not parsed.netloc:
        raise ConfigurationError("base_url must include a network location.")
    if parsed.username or parsed.password:
        raise ConfigurationError("base_url must not contain credentials.")
    if parsed.query or parsed.fragment:
        raise ConfigurationError("base_url must not include query parameters or fragments.")
    normalized_path = parsed.path.rstrip("/")
    sanitized: ParseResult = parsed._replace(path=normalized_path)
    return urlunparse(sanitized)


def _validate_timeout(timeout: float) -> None:
    if timeout <= 0:
        raise ConfigurationError("timeout must be greater than zero.")


def _validate_max_retries(max_retries: int) -> None:
    if max_retries < 0:
        raise ConfigurationError("max_retries must be zero or positive.")


def _validate_backoff_base(backoff_base: float) -> None:
    if backoff_base <= 0:
        raise ConfigurationError("backoff_base must be greater than zero.")


def _validate_header_value(value: str | None, field_name: str) -> None:
    if value is None:
        return
    if "\r" in value or "\n" in value:
        raise ConfigurationError(f"{field_name} must not contain CR or LF characters.")


@dataclass(slots=True, frozen=True)
class ClientConfig:
    """Normalized runtime configuration for sync and async Incident IQ clients."""

    base_url: str
    api_token: str
    site_id: str | None = None
    client_header: str = "ApiClient"
    auth_mode: AuthMode = "bearer"
    app_headers: dict[str, str] | None = None
    timeout: float = 30.0
    validate_responses: bool = True
    max_retries: int = 2
    backoff_base: float = 0.25

    def __post_init__(self) -> None:
        normalized = _normalize_base_url(self.base_url)
        object.__setattr__(self, "base_url", normalized)
        _validate_timeout(self.timeout)
        _validate_max_retries(self.max_retries)
        _validate_backoff_base(self.backoff_base)
        _validate_header_value(self.client_header, "client_header")
        _validate_header_value(self.site_id, "site_id")
        if self.app_headers is not None:
            for key, value in self.app_headers.items():
                _validate_header_value(key, "app_headers key")
                _validate_header_value(value, f"app_headers[{key!r}]")

    @classmethod
    def from_env(
        cls,
        *,
        env: dict[str, str] | None = None,
        dotenv_path: str | Path | None = None,
        test_mode: bool = False,
    ) -> ClientConfig:
        """Create a config from environment variables and optional `.env` file.

        Environment names:
        - Runtime: `INCIDENTIQ_BASE_URL`, `INCIDENTIQ_API_TOKEN`, ...
        - Integration test mode: `INCIDENTIQ_TEST_BASE_URL`, `INCIDENTIQ_TEST_API_TOKEN`, ...
        """
        merged: dict[str, str] = {}
        if dotenv_path is not None:
            merged.update(_parse_dotenv(Path(dotenv_path)))
        else:
            merged.update(_parse_dotenv(Path.cwd() / ".env"))
        merged.update(env or {})

        prefix = "INCIDENTIQ_TEST_" if test_mode else "INCIDENTIQ_"
        base_url = _env_get(merged, f"{prefix}BASE_URL")
        api_token = _env_get(merged, f"{prefix}API_TOKEN")
        site_id = _env_get(merged, f"{prefix}SITE_ID")
        client_header = _env_get(merged, f"{prefix}CLIENT_HEADER") or "ApiClient"
        auth_mode = (_env_get(merged, f"{prefix}AUTH_MODE") or "bearer").lower()
        raw_app_headers = _env_get(merged, f"{prefix}APP_HEADERS_JSON")

        if not base_url:
            raise ConfigurationError(
                f"Missing required environment variable: {prefix}BASE_URL"
            )
        if not api_token:
            raise ConfigurationError(
                f"Missing required environment variable: {prefix}API_TOKEN"
            )
        if auth_mode not in {"bearer", "raw"}:
            raise ConfigurationError(
                f"Unsupported auth mode '{auth_mode}'. Expected 'bearer' or 'raw'."
            )
        resolved_auth_mode = cast(AuthMode, auth_mode)
        resolved_app_headers = _parse_app_headers_json(raw_app_headers)

        return cls(
            base_url=base_url,
            api_token=api_token,
            site_id=site_id,
            client_header=client_header,
            auth_mode=resolved_auth_mode,
            app_headers=resolved_app_headers,
        )


def build_authorization_value(token: str, auth_mode: AuthMode) -> str:
    """Return the outbound `Authorization` header value.

    - `bearer`: normalize to `Bearer <token>` while preserving pre-prefixed values.
    - `raw`: use token exactly as provided.
    """
    if auth_mode == "raw":
        return token
    if token.lower().startswith("bearer "):
        return token
    return f"Bearer {token}"


def _parse_app_headers_json(raw_value: str | None) -> dict[str, str] | None:
    if raw_value is None:
        return None

    try:
        parsed = json.loads(raw_value)
    except json.JSONDecodeError as exc:
        raise ConfigurationError(
            "INCIDENTIQ_APP_HEADERS_JSON must contain valid JSON object text."
        ) from exc

    if not isinstance(parsed, dict):
        raise ConfigurationError("INCIDENTIQ_APP_HEADERS_JSON must be a JSON object.")

    normalized: dict[str, str] = {}
    for key, value in parsed.items():
        if not isinstance(key, str):
            raise ConfigurationError("INCIDENTIQ_APP_HEADERS_JSON keys must be strings.")
        if not isinstance(value, str):
            raise ConfigurationError("INCIDENTIQ_APP_HEADERS_JSON values must be strings.")
        normalized[key] = value
    return normalized or None
