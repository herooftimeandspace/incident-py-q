"""Tests for configuration parsing and auth header normalization."""

from __future__ import annotations

from pathlib import Path
from typing import Any, cast

import pytest

from incident_py_q.config import ClientConfig, build_authorization_value
from incident_py_q.exceptions import ConfigurationError


def test_from_env_runtime_values() -> None:
    config = ClientConfig.from_env(
        env={
            "INCIDENTIQ_BASE_URL": "https://tenant.example/api/v1",
            "INCIDENTIQ_API_TOKEN": "abc123",
            "INCIDENTIQ_SITE_ID": "site-1",
            "INCIDENTIQ_CLIENT_HEADER": "CustomClient",
            "INCIDENTIQ_AUTH_MODE": "raw",
            "INCIDENTIQ_APP_HEADERS_JSON": "{\"apptoken\":\"app-token\"}",
        }
    )

    assert config.base_url == "https://tenant.example/api/v1"
    assert config.api_token == "abc123"
    assert config.site_id == "site-1"
    assert config.client_header == "CustomClient"
    assert config.auth_mode == "raw"
    assert config.app_headers == {"apptoken": "app-token"}


def test_from_env_test_prefix() -> None:
    config = ClientConfig.from_env(
        env={
            "INCIDENTIQ_TEST_BASE_URL": "https://tenant.example/api/v1",
            "INCIDENTIQ_TEST_API_TOKEN": "test-token",
        },
        test_mode=True,
    )
    assert config.base_url == "https://tenant.example/api/v1"
    assert config.api_token == "test-token"
    assert config.auth_mode == "bearer"
    assert config.client_header == "ApiClient"


def test_from_env_reads_dotenv(tmp_path: Path) -> None:
    dotenv = tmp_path / ".env"
    dotenv.write_text(
        "\n".join(
            [
                "INCIDENTIQ_BASE_URL=https://tenant.example/api/v1",
                "INCIDENTIQ_API_TOKEN=dotenv-token",
            ]
        ),
        encoding="utf-8",
    )
    config = ClientConfig.from_env(env={}, dotenv_path=dotenv)
    assert config.base_url == "https://tenant.example/api/v1"
    assert config.api_token == "dotenv-token"


def test_from_env_missing_required_value_raises() -> None:
    with pytest.raises(ConfigurationError):
        ClientConfig.from_env(
            env={"INCIDENTIQ_API_TOKEN": "missing-base"},
            dotenv_path=Path("missing.env"),
        )

    with pytest.raises(ConfigurationError):
        ClientConfig.from_env(
            env={"INCIDENTIQ_BASE_URL": "https://tenant.example"},
            dotenv_path=Path("missing.env"),
        )


def test_from_env_rejects_unknown_auth_mode() -> None:
    with pytest.raises(ConfigurationError):
        ClientConfig.from_env(
            env={
                "INCIDENTIQ_BASE_URL": "https://tenant.example",
                "INCIDENTIQ_API_TOKEN": "token",
                "INCIDENTIQ_AUTH_MODE": "basic",
            }
        )


def test_from_env_rejects_invalid_app_headers_json() -> None:
    with pytest.raises(ConfigurationError):
        ClientConfig.from_env(
            env={
                "INCIDENTIQ_BASE_URL": "https://tenant.example",
                "INCIDENTIQ_API_TOKEN": "token",
                "INCIDENTIQ_APP_HEADERS_JSON": "not-json",
            }
        )


def test_build_authorization_value() -> None:
    assert build_authorization_value("abc", "bearer") == "Bearer abc"
    assert build_authorization_value("Bearer abc", "bearer") == "Bearer abc"
    assert build_authorization_value("Raw token", "raw") == "Raw token"


def _build_valid_config(**overrides: Any) -> ClientConfig:
    base_url = cast(str, overrides.get("base_url", "https://tenant.example/api/v1"))
    api_token = cast(str, overrides.get("api_token", "token-123"))
    client_header = cast(str, overrides.get("client_header", "ApiClient"))
    site_id = cast(str | None, overrides.get("site_id"))
    auth_mode = cast(str, overrides.get("auth_mode", "bearer"))
    app_headers = cast(dict[str, str] | None, overrides.get("app_headers"))
    timeout = cast(float, overrides.get("timeout", 30.0))
    validate_responses = cast(bool, overrides.get("validate_responses", True))
    max_retries = cast(int, overrides.get("max_retries", 2))
    backoff_base = cast(float, overrides.get("backoff_base", 0.25))
    return ClientConfig(
        base_url=base_url,
        api_token=api_token,
        site_id=site_id,
        client_header=client_header,
        auth_mode=cast(Any, auth_mode),
        app_headers=app_headers,
        timeout=timeout,
        validate_responses=validate_responses,
        max_retries=max_retries,
        backoff_base=backoff_base,
    )


@pytest.mark.parametrize(
    "value",
    [
        "http://tenant.example/api/v1",
        "https://tenant.example/api/v1?query=value",
        "https://tenant.example/api/v1#section",
        "https://user:pass@tenant.example/api/v1",
    ],
)
def test_client_config_rejects_insecure_base_url(value: str) -> None:
    with pytest.raises(ConfigurationError):
        _build_valid_config(base_url=value)


def test_client_config_normalizes_trailing_slash() -> None:
    config = _build_valid_config(base_url="https://tenant.example/api/v1/")
    assert config.base_url == "https://tenant.example/api/v1"


def test_client_config_rejects_invalid_timeouts_and_backoff() -> None:
    with pytest.raises(ConfigurationError):
        _build_valid_config(timeout=0)
    with pytest.raises(ConfigurationError):
        _build_valid_config(max_retries=-1)
    with pytest.raises(ConfigurationError):
        _build_valid_config(backoff_base=0)


def test_client_config_rejects_header_control_characters() -> None:
    with pytest.raises(ConfigurationError):
        _build_valid_config(client_header="Api\nClient")
    with pytest.raises(ConfigurationError):
        _build_valid_config(site_id="site\r\n42")


def test_client_config_rejects_invalid_app_header_values() -> None:
    with pytest.raises(ConfigurationError):
        _build_valid_config(app_headers={"apptoken": "bad\nvalue"})
