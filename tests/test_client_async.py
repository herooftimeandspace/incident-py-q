"""Async client request behavior tests."""

from __future__ import annotations

import asyncio
from typing import Any, cast

import httpx
import pytest
import respx

from incident_py_q.client import AsyncClient
from incident_py_q.schema.registry import SchemaRegistry


def _build_client(tiny_registry: SchemaRegistry, **kwargs: Any) -> AsyncClient:
    config: dict[str, Any] = {
        "base_url": "https://tenant.example/api/v1",
        "api_token": "token-123",
        "max_retries": 1,
        "backoff_base": 0.01,
        "registry": tiny_registry,
    }
    config.update(kwargs)
    return AsyncClient(**config)


@respx.mock
def test_async_request_success(tiny_registry: SchemaRegistry) -> None:
    respx.get("https://tenant.example/api/v1/things/abc").mock(
        return_value=httpx.Response(200, json={"id": "abc", "name": "Desk"})
    )
    client = _build_client(tiny_registry)

    async def run() -> dict[str, Any] | list[Any] | None:
        result = await client.request("GET", "/things/{ThingId}", path_params={"ThingId": "abc"})
        await client.close()
        return result

    payload = asyncio.run(run())
    assert payload == {"id": "abc", "name": "Desk"}


@respx.mock
def test_async_request_retries_on_transport_error(
    tiny_registry: SchemaRegistry, monkeypatch: pytest.MonkeyPatch
) -> None:
    async def no_sleep(_: float) -> None:
        return None

    monkeypatch.setattr("incident_py_q.client.asyncio.sleep", no_sleep)
    route = respx.get("https://tenant.example/api/v1/things/abc").mock(
        side_effect=[
            httpx.ConnectError("temporary failure"),
            httpx.Response(200, json={"id": "abc", "name": "Desk"}),
        ]
    )
    client = _build_client(tiny_registry)

    async def run() -> dict[str, Any] | list[Any] | None:
        result = await client.request("GET", "/things/{ThingId}", path_params={"ThingId": "abc"})
        await client.close()
        return result

    payload = asyncio.run(run())
    assert payload == {"id": "abc", "name": "Desk"}
    assert route.call_count == 2


@respx.mock
def test_async_request_raises_for_http_errors(tiny_registry: SchemaRegistry) -> None:
    respx.get("https://tenant.example/api/v1/things/abc").mock(return_value=httpx.Response(404))
    client = _build_client(tiny_registry)

    async def run() -> None:
        with pytest.raises(httpx.HTTPStatusError):
            await client.request("GET", "/things/{ThingId}", path_params={"ThingId": "abc"})
        await client.close()

    asyncio.run(run())


def test_async_request_raises_transport_error_after_retry_exhaustion(
    tiny_registry: SchemaRegistry, monkeypatch: pytest.MonkeyPatch
) -> None:
    client = _build_client(tiny_registry, max_retries=0)

    async def no_sleep(_: float) -> None:
        return None

    async def fake_request(*args: Any, **kwargs: Any) -> httpx.Response:
        raise httpx.ConnectError("network down")

    monkeypatch.setattr("incident_py_q.client.asyncio.sleep", no_sleep)
    monkeypatch.setattr(client._http, "request", fake_request)

    async def run() -> None:
        with pytest.raises(httpx.ConnectError):
            await client.request("GET", "/things/{ThingId}", path_params={"ThingId": "abc"})
        await client.close()

    asyncio.run(run())


def test_async_request_from_operation_uses_rendered_path(tiny_registry: SchemaRegistry) -> None:
    operation = tiny_registry.match_operation("GET", "/things/abc")
    assert operation is not None
    client = _build_client(tiny_registry)

    async def fake_request(*args: Any, **kwargs: Any) -> httpx.Response:
        request = httpx.Request("GET", "https://tenant.example/api/v1/things/abc")
        return httpx.Response(200, json={"id": "abc", "name": "Desk"}, request=request)

    async def run() -> dict[str, Any] | list[Any] | None:
        client._http.request = fake_request
        payload = await client._request_from_operation(
            operation,
            path_params={"ThingId": "abc"},
            params=None,
            json_body=None,
            headers=None,
            timeout=None,
        )
        await client.close()
        return cast(dict[str, Any] | list[Any] | None, payload)

    payload = asyncio.run(run())
    assert payload == {"id": "abc", "name": "Desk"}
