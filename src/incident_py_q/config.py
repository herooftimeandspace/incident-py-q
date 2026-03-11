"""Configuration loading and normalization for Incident IQ clients."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Literal, cast

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


@dataclass(slots=True, frozen=True)
class ClientConfig:
    """Normalized runtime configuration for sync and async Incident IQ clients."""

    base_url: str
    api_token: str
    site_id: str | None = None
    client_header: str = "ApiClient"
    auth_mode: AuthMode = "bearer"
    timeout: float = 30.0
    validate_responses: bool = True
    max_retries: int = 2
    backoff_base: float = 0.25

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

        return cls(
            base_url=base_url.rstrip("/"),
            api_token=api_token,
            site_id=site_id,
            client_header=client_header,
            auth_mode=resolved_auth_mode,
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
