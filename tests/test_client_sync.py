"""Sync client request behavior tests."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import httpx
import pytest
import respx

from incident_py_q.client import Client
from incident_py_q.exceptions import ConfigurationError, SchemaValidationError
from incident_py_q.schema.registry import SchemaRegistry


def _load_asset_serial_payload() -> dict[str, Any]:
    fixture_path = Path(__file__).parent / "fixtures" / "asset_serial_live_response.json"
    return json.loads(fixture_path.read_text(encoding="utf-8"))


def _build_client(tiny_registry: SchemaRegistry, **kwargs: Any) -> Client:
    config: dict[str, Any] = {
        "base_url": "https://tenant.example/api/v1",
        "api_token": "token-123",
        "site_id": "site-42",
        "client_header": "ApiClient",
        "max_retries": 1,
        "backoff_base": 0.01,
        "registry": tiny_registry,
    }
    config.update(kwargs)
    return Client(
        **config,
    )


@respx.mock
def test_request_builds_headers_and_validates_payload(tiny_registry: SchemaRegistry) -> None:
    route = respx.get("https://tenant.example/api/v1/things/abc").mock(
        return_value=httpx.Response(200, json={"id": "abc", "name": "Desk"})
    )
    client = _build_client(tiny_registry)
    payload = client.request("GET", "/things/{ThingId}", path_params={"ThingId": "abc"})
    client.close()

    assert payload == {"id": "abc", "name": "Desk"}
    assert route.call_count == 1
    sent_headers = route.calls[0].request.headers
    assert sent_headers["Authorization"] == "Bearer token-123"
    assert sent_headers["Client"] == "ApiClient"
    assert sent_headers["SiteId"] == "site-42"


@respx.mock
def test_request_raises_for_http_errors(tiny_registry: SchemaRegistry) -> None:
    respx.get("https://tenant.example/api/v1/things/abc").mock(return_value=httpx.Response(404))
    client = _build_client(tiny_registry)
    with pytest.raises(httpx.HTTPStatusError):
        client.request("GET", "/things/{ThingId}", path_params={"ThingId": "abc"})
    client.close()


@respx.mock
def test_request_retries_on_idempotent_retryable_status(
    tiny_registry: SchemaRegistry, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr("incident_py_q.client.time.sleep", lambda _: None)
    route = respx.get("https://tenant.example/api/v1/things/abc").mock(
        side_effect=[
            httpx.Response(503),
            httpx.Response(200, json={"id": "abc", "name": "Desk"}),
        ]
    )
    client = _build_client(tiny_registry)
    payload = client.request("GET", "/things/{ThingId}", path_params={"ThingId": "abc"})
    client.close()

    assert payload == {"id": "abc", "name": "Desk"}
    assert route.call_count == 2


@respx.mock
def test_request_does_not_retry_post_by_default(
    tiny_registry: SchemaRegistry, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr("incident_py_q.client.time.sleep", lambda _: None)
    route = respx.post("https://tenant.example/api/v1/things").mock(
        side_effect=[httpx.Response(503), httpx.Response(201, json={"id": "abc", "name": "Desk"})]
    )
    client = _build_client(tiny_registry)
    with pytest.raises(httpx.HTTPStatusError):
        client.request("POST", "/things", json={"id": "abc", "name": "Desk"})
    client.close()
    assert route.call_count == 1


@respx.mock
def test_request_raises_on_schema_validation_failure(tiny_registry: SchemaRegistry) -> None:
    respx.get("https://tenant.example/api/v1/things/abc").mock(
        return_value=httpx.Response(200, json={"id": "abc"})
    )
    client = _build_client(tiny_registry)
    with pytest.raises(SchemaValidationError):
        client.request("GET", "/things/{ThingId}", path_params={"ThingId": "abc"})
    client.close()


def test_request_retries_on_transport_error(
    tiny_registry: SchemaRegistry, monkeypatch: pytest.MonkeyPatch
) -> None:
    client = _build_client(tiny_registry)
    monkeypatch.setattr("incident_py_q.client.time.sleep", lambda _: None)
    request = httpx.Request("GET", "https://tenant.example/api/v1/things/abc")

    attempts: list[Exception | httpx.Response] = [
        httpx.ConnectTimeout("network"),
        httpx.Response(200, json={"id": "abc", "name": "Desk"}, request=request),
    ]

    def fake_request(*args: Any, **kwargs: Any) -> httpx.Response:
        result = attempts.pop(0)
        if isinstance(result, Exception):
            raise result
        return result

    monkeypatch.setattr(client._http, "request", fake_request)
    payload = client.request("GET", "/things/{ThingId}", path_params={"ThingId": "abc"})
    client.close()

    assert payload == {"id": "abc", "name": "Desk"}
    assert not attempts


def test_request_raises_for_missing_path_params(tiny_registry: SchemaRegistry) -> None:
    client = _build_client(tiny_registry)
    with pytest.raises(ValueError):
        client.request("GET", "/things/{ThingId}")
    client.close()


def test_invalid_auth_mode_raises_configuration_error(tiny_registry: SchemaRegistry) -> None:
    with pytest.raises(ConfigurationError):
        Client(
            base_url="https://tenant.example/api/v1",
            api_token="token-123",
            auth_mode="basic",
            registry=tiny_registry,
        )


def test_request_raises_transport_error_after_retry_exhaustion(
    tiny_registry: SchemaRegistry, monkeypatch: pytest.MonkeyPatch
) -> None:
    client = _build_client(tiny_registry, max_retries=0)
    monkeypatch.setattr("incident_py_q.client.time.sleep", lambda _: None)

    def fake_request(*args: Any, **kwargs: Any) -> httpx.Response:
        raise httpx.ConnectError("network down")

    monkeypatch.setattr(client._http, "request", fake_request)

    with pytest.raises(httpx.ConnectError):
        client.request("GET", "/things/{ThingId}", path_params={"ThingId": "abc"})

    client.close()


@respx.mock
def test_golden_asset_serial_lookup_stays_strict(
    bundled_registry: SchemaRegistry,
) -> None:
    payload = _load_asset_serial_payload()
    respx.get("https://tenant.example/api/v1/assets/serial/4825670226C6").mock(
        return_value=httpx.Response(200, json=payload)
    )

    client = Client(
        base_url="https://tenant.example/api/v1",
        api_token="token-123",
        registry=bundled_registry,
    )
    try:
        with pytest.raises(SchemaValidationError):
            client.assets.get_assets_by_serial(serial="4825670226C6")
    finally:
        client.close()


@respx.mock
def test_silver_asset_serial_lookup_accepts_relaxed_live_payload(
    bundled_registry: SchemaRegistry,
) -> None:
    payload = _load_asset_serial_payload()
    respx.get("https://tenant.example/api/v1/assets/serial/4825670226C6").mock(
        return_value=httpx.Response(200, json=payload)
    )

    client = Client(
        base_url="https://tenant.example/api/v1",
        api_token="token-123",
        registry=bundled_registry,
    )
    try:
        assert client.silver.assets.get_asset_by_serial(serial="4825670226C6") == payload
    finally:
        client.close()
