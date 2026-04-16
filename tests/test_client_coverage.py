"""Additional coverage tests for sync/async client helper branches."""

from __future__ import annotations

import asyncio
from collections.abc import Mapping
from typing import Any, cast

import httpx
import pytest
import respx

from incident_py_q.client import (
    AsyncClient,
    Client,
    _build_url,
    _decode_payload,
    _merge_headers,
    _normalize_app_headers,
)
from incident_py_q.config import ClientConfig
from incident_py_q.exceptions import ConfigurationError
from incident_py_q.schema.registry import OperationSpec, SchemaRegistry


def _sync_client(tiny_registry: SchemaRegistry, **kwargs: Any) -> Client:
    return Client(
        base_url="https://tenant.example/api/v1",
        api_token="token-123",
        max_retries=1,
        backoff_base=0.01,
        registry=tiny_registry,
        **kwargs,
    )


def _async_client(tiny_registry: SchemaRegistry, **kwargs: Any) -> AsyncClient:
    return AsyncClient(
        base_url="https://tenant.example/api/v1",
        api_token="token-123",
        max_retries=1,
        backoff_base=0.01,
        registry=tiny_registry,
        **kwargs,
    )


def test_client_env_constructors_and_missing_configuration(monkeypatch: pytest.MonkeyPatch) -> None:
    for key in ("INCIDENTIQ_BASE_URL", "INCIDENTIQ_API_TOKEN", "INCIDENTIQ_TEST_BASE_URL", "INCIDENTIQ_TEST_API_TOKEN"):
        monkeypatch.delenv(key, raising=False)

    with pytest.raises(ConfigurationError):
        Client()
    with pytest.raises(ConfigurationError):
        AsyncClient()

    monkeypatch.setenv("INCIDENTIQ_BASE_URL", "https://tenant.example/api/v1")
    monkeypatch.setenv("INCIDENTIQ_API_TOKEN", "token-123")
    client = Client.from_env()
    assert client.config.base_url == "https://tenant.example/api/v1"
    client.close()

    async_client = AsyncClient.from_env()
    asyncio.run(async_client.close())

    monkeypatch.setenv("INCIDENTIQ_TEST_BASE_URL", "https://tenant.example/api/v1")
    monkeypatch.setenv("INCIDENTIQ_TEST_API_TOKEN", "token-123")
    test_client = Client.from_test_env()
    assert test_client.config.base_url == "https://tenant.example/api/v1"
    test_client.close()

    test_async_client = AsyncClient.from_test_env()
    asyncio.run(test_async_client.close())


def test_client_context_and_getattr_helpers(tiny_registry: SchemaRegistry) -> None:
    with _sync_client(tiny_registry) as client:
        assert isinstance(client.sdk_inventory(), list)
        with pytest.raises(AttributeError):
            _ = client.not_a_namespace

    async def run() -> None:
        async with _async_client(tiny_registry) as client:
            assert isinstance(client.sdk_inventory(), list)
            with pytest.raises(AttributeError):
                _ = client.not_a_namespace

    asyncio.run(run())


@respx.mock
def test_request_without_matching_operation_skips_schema_validation(tiny_registry: SchemaRegistry) -> None:
    respx.get("https://tenant.example/api/v1/unmodeled").mock(return_value=httpx.Response(200, json={"ok": True}))
    client = _sync_client(tiny_registry)
    payload = client.request("GET", "/unmodeled")
    client.close()
    assert payload == {"ok": True}


class _SyncHTTPStub:
    def __init__(self, events: list[httpx.Response | Exception]) -> None:
        self.events = events
        self.calls: list[dict[str, Any]] = []

    def request(self, method: str, url: str, **kwargs: Any) -> httpx.Response:
        self.calls.append({"method": method, "url": url, **kwargs})
        event = self.events.pop(0)
        if isinstance(event, Exception):
            raise event
        return event

    def close(self) -> None:
        return None


class _AsyncHTTPStub:
    def __init__(self, events: list[httpx.Response | Exception]) -> None:
        self.events = events
        self.calls: list[dict[str, Any]] = []

    async def request(self, method: str, url: str, **kwargs: Any) -> httpx.Response:
        self.calls.append({"method": method, "url": url, **kwargs})
        event = self.events.pop(0)
        if isinstance(event, Exception):
            raise event
        return event

    async def aclose(self) -> None:
        return None


def _status_error(method: str, url: str, status_code: int) -> httpx.HTTPStatusError:
    request = httpx.Request(method, url)
    response = httpx.Response(status_code, request=request)
    return httpx.HTTPStatusError("boom", request=request, response=response)


def test_sync_retry_paths_for_raised_http_status_and_transport_errors(
    tiny_registry: SchemaRegistry, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr("incident_py_q.client.time.sleep", lambda _: None)
    op = tiny_registry.match_operation("GET", "/things/abc")
    assert op is not None

    url = "https://tenant.example/api/v1/things/abc"
    http_stub = _SyncHTTPStub(
        events=[
            _status_error("GET", url, 503),
            httpx.Response(200, json={"id": "abc", "name": "Desk"}, request=httpx.Request("GET", url)),
        ]
    )
    client = _sync_client(tiny_registry, http_client=http_stub)
    assert client.request("GET", "/things/{ThingId}", path_params={"ThingId": "abc"}) == {"id": "abc", "name": "Desk"}
    assert len(http_stub.calls) == 2
    assert http_stub.calls[0]["timeout"] == client.config.timeout
    client.close()

    transport_stub = _SyncHTTPStub(events=[httpx.ConnectError("down"), httpx.ConnectError("down again")])
    post_client = _sync_client(tiny_registry, http_client=transport_stub)
    with pytest.raises(httpx.RequestError):
        post_client.request("POST", "/things", json={"id": "x"}, timeout=3.5)
    assert len(transport_stub.calls) == 1
    assert transport_stub.calls[0]["timeout"] == 3.5
    post_client.close()

    bypass_validation_client = _sync_client(
        tiny_registry,
        http_client=_SyncHTTPStub(
            events=[httpx.Response(200, json={"id": "only"}, request=httpx.Request("GET", url))]
        ),
        validate_responses=False,
    )
    assert bypass_validation_client.request("GET", "/things/{ThingId}", path_params={"ThingId": "abc"}) == {"id": "only"}
    bypass_validation_client.close()

    explicit = _sync_client(
        tiny_registry,
        http_client=_SyncHTTPStub(
            events=[httpx.Response(200, json={"id": "abc", "name": "Desk"}, request=httpx.Request("GET", url))]
        ),
    )
    assert explicit._request_from_operation(
        op,
        path_params={"ThingId": "abc"},
        params=None,
        json_body=None,
        headers=None,
        timeout=None,
    ) == {"id": "abc", "name": "Desk"}
    explicit.close()


def test_async_retry_paths_for_raised_http_status_and_transport_errors(
    tiny_registry: SchemaRegistry, monkeypatch: pytest.MonkeyPatch
) -> None:
    async def run() -> None:
        async def no_sleep(_: float) -> None:
            return None

        monkeypatch.setattr("incident_py_q.client.asyncio.sleep", no_sleep)
        url = "https://tenant.example/api/v1/things/abc"
        http_stub = _AsyncHTTPStub(
            events=[
                _status_error("GET", url, 503),
                httpx.Response(200, json={"id": "abc", "name": "Desk"}, request=httpx.Request("GET", url)),
            ]
        )
        client = _async_client(tiny_registry, http_client=http_stub)
        payload = await client.request("GET", "/things/{ThingId}", path_params={"ThingId": "abc"})
        assert payload == {"id": "abc", "name": "Desk"}
        assert len(http_stub.calls) == 2
        assert http_stub.calls[0]["timeout"] == client.config.timeout
        await client.close()

        post_stub = _AsyncHTTPStub(events=[httpx.ConnectError("down"), httpx.ConnectError("still down")])
        post_client = _async_client(tiny_registry, http_client=post_stub)
        with pytest.raises(httpx.RequestError):
            await post_client.request("POST", "/things", json={"id": "x"}, timeout=4.0)
        assert len(post_stub.calls) == 1
        assert post_stub.calls[0]["timeout"] == 4.0
        await post_client.close()

        op = tiny_registry.match_operation("GET", "/things/abc")
        assert op is not None
        explicit = _async_client(
            tiny_registry,
            http_client=_AsyncHTTPStub(
                events=[httpx.Response(200, json={"id": "abc", "name": "Desk"}, request=httpx.Request("GET", url))]
            ),
        )
        payload2 = await explicit._request_from_operation(
            op,
            path_params={"ThingId": "abc"},
            params=None,
            json_body=None,
            headers=None,
            timeout=None,
        )
        assert payload2 == {"id": "abc", "name": "Desk"}
        await explicit.close()

    asyncio.run(run())


def test_client_low_level_helpers() -> None:
    config = ClientConfig(
        base_url="https://tenant.example/api/v1",
        api_token="token-123",
        site_id="site-42",
        client_header="ApiClient",
        auth_mode="bearer",
        timeout=10.0,
        validate_responses=True,
        max_retries=1,
        backoff_base=0.01,
    )
    assert _build_url(config.base_url, "/things/1") == "https://tenant.example/api/v1/things/1"
    assert _build_url(config.base_url, "things/1") == "https://tenant.example/api/v1/things/1"
    assert _build_url(config.base_url, "https://override.example/x") == "https://override.example/x"

    merged = _merge_headers(config, {"Extra": "1"})
    assert merged["Authorization"] == "Bearer token-123"
    assert merged["Client"] == "ApiClient"
    assert merged["SiteId"] == "site-42"
    assert merged["Extra"] == "1"

    assert _normalize_app_headers(None) is None
    assert _normalize_app_headers({}) is None
    assert _normalize_app_headers({"x": "y"}) == {"x": "y"}
    bad_headers: Mapping[str, str] = cast(Mapping[str, str], {"x": cast(Any, 1)})
    with pytest.raises(ConfigurationError):
        _normalize_app_headers(bad_headers)

    response_204 = httpx.Response(204, request=httpx.Request("GET", "https://tenant.example"))
    assert _decode_payload(response_204) is None

    no_content = httpx.Response(200, content=b"", request=httpx.Request("GET", "https://tenant.example"))
    assert _decode_payload(no_content) is None

    json_dict = httpx.Response(
        200,
        json={"ok": True},
        headers={"content-type": "application/json"},
        request=httpx.Request("GET", "https://tenant.example"),
    )
    assert _decode_payload(json_dict) == {"ok": True}

    json_scalar = httpx.Response(
        200,
        content=b'"x"',
        headers={"content-type": "application/json"},
        request=httpx.Request("GET", "https://tenant.example"),
    )
    assert _decode_payload(json_scalar) is None

    non_json_parseable = httpx.Response(
        200,
        content=b'{"ok": true}',
        headers={"content-type": "text/plain"},
        request=httpx.Request("GET", "https://tenant.example"),
    )
    assert _decode_payload(non_json_parseable) == {"ok": True}

    non_json_unparseable = httpx.Response(
        200,
        content=b"not json",
        headers={"content-type": "text/plain"},
        request=httpx.Request("GET", "https://tenant.example"),
    )
    assert _decode_payload(non_json_unparseable) is None


def test_operation_spec_python_method_name_property() -> None:
    op = OperationSpec(
        operation_id="Prefix_DoThing",
        method="GET",
        path_template="/x",
        namespace="x",
        parameters=(),
        response_schemas={},
        source_controller="test",
    )
    assert op.python_method_name == "do_thing"
