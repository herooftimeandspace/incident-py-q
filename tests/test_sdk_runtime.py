"""Tests for dynamic SDK namespace and method generation."""

from __future__ import annotations

import asyncio
import inspect

import httpx
import pytest
import respx
from pydantic import BaseModel, ValidationError

from incident_py_q import AsyncClient, Client
from incident_py_q.schema.registry import SchemaRegistry
from incident_py_q.sdk.runtime import _coerce_response


def _build_sync_client(tiny_registry: SchemaRegistry) -> Client:
    return Client(
        base_url="https://tenant.example/api/v1",
        api_token="token-123",
        registry=tiny_registry,
        max_retries=0,
    )


def _build_async_client(tiny_registry: SchemaRegistry) -> AsyncClient:
    return AsyncClient(
        base_url="https://tenant.example/api/v1",
        api_token="token-123",
        registry=tiny_registry,
        max_retries=0,
    )


def test_sdk_namespace_methods_and_aliases(tiny_registry: SchemaRegistry) -> None:
    client = _build_sync_client(tiny_registry)
    methods = client.things.list_methods()
    client.close()

    assert "get_thing" in methods
    assert "get_things" in methods
    assert "create_thing" in methods
    assert "get" in methods
    assert "list" in methods
    assert "create" in methods


def test_sdk_signature_uses_snake_case_parameters(tiny_registry: SchemaRegistry) -> None:
    client = _build_sync_client(tiny_registry)
    signature = inspect.signature(client.things.get_thing)
    client.close()

    assert "thing_id" in signature.parameters
    assert signature.parameters["thing_id"].kind is inspect.Parameter.KEYWORD_ONLY


@respx.mock
def test_sdk_returns_typed_models_by_default(tiny_registry: SchemaRegistry) -> None:
    respx.get("https://tenant.example/api/v1/things/abc").mock(
        return_value=httpx.Response(200, json={"id": "abc", "name": "Desk"})
    )
    client = _build_sync_client(tiny_registry)
    payload = client.things.get_thing(thing_id="abc")
    raw_payload = client.things.get_thing.raw(thing_id="abc")
    client.close()

    assert isinstance(payload, BaseModel)
    assert payload.model_dump() == {"id": "abc", "name": "Desk"}
    assert raw_payload == {"id": "abc", "name": "Desk"}


@respx.mock
def test_sdk_iter_pages_fetches_until_empty_page(tiny_registry: SchemaRegistry) -> None:
    route = respx.get("https://tenant.example/api/v1/things").mock(
        side_effect=[
            httpx.Response(200, json={"Items": [{"id": "1", "name": "One"}]}),
            httpx.Response(200, json={"Items": []}),
        ]
    )
    client = _build_sync_client(tiny_registry)
    pages = client.things.get_things.iter_pages(start_page=1, page_size=10, max_pages=4)
    client.close()

    assert route.call_count == 2
    assert len(pages) == 2
    first_query = route.calls[0].request.url.params
    assert first_query["page"] == "1"
    assert first_query["pageSize"] == "10"


def test_sync_async_sdk_surface_parity(tiny_registry: SchemaRegistry) -> None:
    sync_client = _build_sync_client(tiny_registry)
    async_client = _build_async_client(tiny_registry)

    sync_namespaces = sorted(name for name in dir(sync_client) if not name.startswith("_"))
    async_namespaces = sorted(name for name in dir(async_client) if not name.startswith("_"))

    sync_client.close()
    asyncio.run(async_client.close())

    assert "things" in sync_namespaces
    assert "things" in async_namespaces
    assert sync_client.sdk_inventory() == async_client.sdk_inventory()


def test_sdk_request_model_rejects_invalid_param_type(tiny_registry: SchemaRegistry) -> None:
    client = _build_sync_client(tiny_registry)
    with respx.mock, pytest.raises(ValidationError):
        client.things.get_things(page="invalid")
    client.close()


def test_typed_response_rejection_raises_value_error() -> None:
    class StrictModel(BaseModel):
        count: int

    try:
        _coerce_response({"count": "not-int"}, StrictModel)
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError when response model validation fails.")
