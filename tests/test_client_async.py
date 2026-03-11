"""Async client request behavior tests."""

from __future__ import annotations

import asyncio
from typing import Any

import httpx
import pytest
import respx

from incident_py_q.client import AsyncClient
from incident_py_q.schema.registry import SchemaRegistry


def _build_client(tiny_registry: SchemaRegistry, **kwargs: Any) -> AsyncClient:
    return AsyncClient(
        base_url="https://tenant.example/api/v1",
        api_token="token-123",
        max_retries=1,
        backoff_base=0.0,
        registry=tiny_registry,
        **kwargs,
    )


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
