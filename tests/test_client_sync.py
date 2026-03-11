"""Sync client request behavior tests."""

from __future__ import annotations

from typing import Any

import httpx
import pytest
import respx

from incident_py_q.client import Client
from incident_py_q.exceptions import ConfigurationError, SchemaValidationError
from incident_py_q.schema.registry import SchemaRegistry


def _build_client(tiny_registry: SchemaRegistry, **kwargs: Any) -> Client:
    return Client(
        base_url="https://tenant.example/api/v1",
        api_token="token-123",
        site_id="site-42",
        client_header="ApiClient",
        max_retries=1,
        backoff_base=0.0,
        registry=tiny_registry,
        **kwargs,
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
