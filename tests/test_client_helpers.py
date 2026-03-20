"""Tests for client helper branches and constructor convenience paths."""

from __future__ import annotations

import asyncio

import httpx
import pytest

from incident_py_q.client import (
    AsyncClient,
    Client,
    _build_url,
    _decode_payload,
    _merge_headers,
)
from incident_py_q.config import ClientConfig
from incident_py_q.schema.registry import SchemaRegistry


def _make_config(**overrides: object) -> ClientConfig:
    values: dict[str, object] = {
        "base_url": "https://tenant.example/api/v1",
        "api_token": "token-123",
        "client_header": "ApiClient",
        "site_id": "site-42",
        "max_retries": 1,
        "backoff_base": 0.01,
    }
    values.update(overrides)
    return ClientConfig(**values)


def test_build_url_joins_relative_paths() -> None:
    assert _build_url("https://tenant.example/api/v1", "things/abc") == (
        "https://tenant.example/api/v1/things/abc"
    )


def test_build_url_preserves_absolute_paths() -> None:
    absolute = "https://api.example/override"
    assert _build_url("https://tenant.example/api/v1", absolute) == absolute


def test_merge_headers_builds_default_auth_and_optional_headers() -> None:
    config = _make_config()
    headers = _merge_headers(config, {"X-Test": "value"})

    assert headers["Authorization"] == "Bearer token-123"
    assert headers["Client"] == "ApiClient"
    assert headers["SiteId"] == "site-42"
    assert headers["X-Test"] == "value"


def test_merge_headers_supports_raw_auth_and_missing_site_id() -> None:
    config = _make_config(auth_mode="raw", site_id=None)
    headers = _merge_headers(config, None)

    assert headers["Authorization"] == "token-123"
    assert headers["Client"] == "ApiClient"
    assert "SiteId" not in headers


def test_decode_payload_handles_no_content_and_empty_body() -> None:
    no_content = httpx.Response(204, request=httpx.Request("GET", "https://tenant.example/no-content"))
    empty = httpx.Response(200, content=b"", request=httpx.Request("GET", "https://tenant.example/empty"))

    assert _decode_payload(no_content) is None
    assert _decode_payload(empty) is None


def test_decode_payload_handles_json_scalars_and_invalid_json() -> None:
    scalar = httpx.Response(
        200,
        json="ok",
        headers={"content-type": "application/json"},
        request=httpx.Request("GET", "https://tenant.example/scalar"),
    )
    invalid = httpx.Response(
        200,
        content=b"not-json",
        headers={"content-type": "text/plain"},
        request=httpx.Request("GET", "https://tenant.example/plain"),
    )

    assert _decode_payload(scalar) is None
    assert _decode_payload(invalid) is None


def test_client_from_env_builds_normalized_config(
    tiny_registry: SchemaRegistry, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("INCIDENTIQ_BASE_URL", "https://tenant.example/api/v1/")
    monkeypatch.setenv("INCIDENTIQ_API_TOKEN", "env-token")
    monkeypatch.setenv("INCIDENTIQ_SITE_ID", "site-env")
    monkeypatch.setenv("INCIDENTIQ_CLIENT_HEADER", "EnvClient")

    client = Client.from_env()
    try:
        assert client.config.base_url == "https://tenant.example/api/v1"
        assert client.config.api_token == "env-token"
        assert client.config.site_id == "site-env"
        assert client.config.client_header == "EnvClient"
        assert isinstance(client._registry, SchemaRegistry)
    finally:
        client.close()


def test_client_from_test_env_uses_test_prefix(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("INCIDENTIQ_TEST_BASE_URL", "https://tenant.example/api/v1")
    monkeypatch.setenv("INCIDENTIQ_TEST_API_TOKEN", "test-token")

    client = Client.from_test_env()
    try:
        assert client.config.api_token == "test-token"
        assert client.config.base_url == "https://tenant.example/api/v1"
    finally:
        client.close()


def test_client_context_manager_closes_http_client(tiny_registry: SchemaRegistry) -> None:
    http_client = httpx.Client()
    with Client(
        base_url="https://tenant.example/api/v1",
        api_token="token-123",
        registry=tiny_registry,
        http_client=http_client,
    ) as client:
        assert client is not None

    assert http_client.is_closed


def test_client_getattr_raises_for_unknown_namespace(tiny_registry: SchemaRegistry) -> None:
    client = Client(
        base_url="https://tenant.example/api/v1",
        api_token="token-123",
        registry=tiny_registry,
    )

    try:
        with pytest.raises(AttributeError):
            _ = client.unknown_namespace
    finally:
        client.close()


def test_client_requires_credentials_when_no_config_is_provided() -> None:
    with pytest.raises(Exception):
        Client(base_url=None, api_token=None)


def test_async_client_from_env_and_context_manager(
    tiny_registry: SchemaRegistry, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("INCIDENTIQ_BASE_URL", "https://tenant.example/api/v1")
    monkeypatch.setenv("INCIDENTIQ_API_TOKEN", "env-token")

    async def run() -> None:
        client = AsyncClient.from_env()
        try:
            assert client.config.api_token == "env-token"
        finally:
            await client.close()

        http_client = httpx.AsyncClient()
        async with AsyncClient(
            base_url="https://tenant.example/api/v1",
            api_token="token-123",
            registry=tiny_registry,
            http_client=http_client,
        ) as context_client:
            assert context_client is not None

        assert http_client.is_closed

    asyncio.run(run())


def test_async_client_from_test_env_and_missing_namespace(
    tiny_registry: SchemaRegistry, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("INCIDENTIQ_TEST_BASE_URL", "https://tenant.example/api/v1")
    monkeypatch.setenv("INCIDENTIQ_TEST_API_TOKEN", "test-token")

    async def run() -> None:
        client = AsyncClient.from_test_env()
        try:
            assert client.config.api_token == "test-token"
            with pytest.raises(AttributeError):
                _ = client.unknown_namespace
        finally:
            await client.close()

    asyncio.run(run())


def test_decode_payload_handles_non_json_content_with_json_body() -> None:
    response = httpx.Response(
        200,
        content=b"{\"ok\": true}",
        headers={"content-type": "text/plain"},
        request=httpx.Request("GET", "https://tenant.example/plain-json"),
    )

    assert _decode_payload(response) == {"ok": True}
