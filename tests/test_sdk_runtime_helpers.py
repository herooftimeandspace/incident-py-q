"""Targeted tests for SDK runtime helper branches."""

from __future__ import annotations

import asyncio
from typing import Any

import pytest
from pydantic import BaseModel

from incident_py_q.schema.registry import OperationSpec, ParameterSpec, build_schema_registry
from incident_py_q.sdk.model_factory import SwaggerModelFactory
from incident_py_q.sdk.runtime import (
    AsyncOperationMethod,
    Namespace,
    OperationMethod,
    _Binding,
    _annotation_for_parameter,
    _attach_aliases,
    _build_request_model,
    _build_response_model,
    _build_signature,
    _extract_items,
    _find_page_binding,
    _find_page_size_binding,
    _operation_bindings,
    _suggest_alias,
    _to_request_components,
)


class _SyncDispatcher:
    def __init__(self, payload: Any) -> None:
        self.payload = payload
        self.calls: list[dict[str, Any]] = []

    def _request_from_operation(
        self,
        operation: OperationSpec,
        *,
        path_params: dict[str, Any] | None,
        params: dict[str, Any] | None,
        json_body: Any | None,
        headers: dict[str, str] | None,
        timeout: float | None,
    ) -> Any:
        self.calls.append(
            {
                "operation": operation.operation_id,
                "path_params": path_params,
                "params": params,
                "json_body": json_body,
                "headers": headers,
                "timeout": timeout,
            }
        )
        return self.payload


class _AsyncDispatcher:
    def __init__(self, payload: Any) -> None:
        self.payload = payload
        self.calls: list[dict[str, Any]] = []

    async def _request_from_operation(
        self,
        operation: OperationSpec,
        *,
        path_params: dict[str, Any] | None,
        params: dict[str, Any] | None,
        json_body: Any | None,
        headers: dict[str, str] | None,
        timeout: float | None,
    ) -> Any:
        self.calls.append(
            {
                "operation": operation.operation_id,
                "path_params": path_params,
                "params": params,
                "json_body": json_body,
                "headers": headers,
                "timeout": timeout,
            }
        )
        return self.payload


def _operation(*, path: str = "/things/{ThingId}", method: str = "GET") -> OperationSpec:
    return OperationSpec(
        operation_id="Things_GetThing",
        method=method,
        path_template=path,
        namespace="things",
        parameters=(
            ParameterSpec(
                name="ThingId",
                location="path",
                required=True,
                schema=None,
                primitive_type="string",
                description=None,
            ),
        ),
        response_schemas={"200": {"type": "object", "properties": {"id": {"type": "string"}}}},
        source_controller="Things",
        description="Fetch thing",
    )


def test_build_signature_marks_required_and_optional_params() -> None:
    signature = _build_signature(
        [
            _Binding("thing_id", "ThingId", "path", True, str),
            _Binding("site_id", "SiteId", "header", False, str),
        ]
    )

    assert signature.parameters["thing_id"].default is signature.empty
    assert signature.parameters["site_id"].default is None
    assert "timeout" in signature.parameters


def test_operation_bindings_skip_reserved_headers_and_dedupe_names() -> None:
    factory = SwaggerModelFactory({})
    operation = OperationSpec(
        operation_id="Things_GetThing",
        method="GET",
        path_template="/things/{ThingId}",
        namespace="things",
        parameters=(
            ParameterSpec("Authorization", "header", False, None, "string", None),
            ParameterSpec("Content-Type", "header", False, None, "string", None),
            ParameterSpec("ThingId", "path", True, None, "string", None),
            ParameterSpec("ThingId", "query", False, None, "string", None),
            ParameterSpec("", "query", False, None, "string", None),
        ),
        response_schemas={},
        source_controller="Things",
    )

    bindings = _operation_bindings(operation, factory)

    assert [binding.field_name for binding in bindings] == ["thing_id", "thing_id_arg"]


def test_annotation_for_parameter_prefers_body_schema_and_known_primitives() -> None:
    factory = SwaggerModelFactory({"Thing": {"type": "object", "properties": {"id": {"type": "string"}}}})

    body = ParameterSpec("payload", "body", True, {"$ref": "#/definitions/Thing"}, None, None)
    query = ParameterSpec("count", "query", False, None, "integer", None)
    unsupported = ParameterSpec("mystery", "query", False, None, "mystery", None)

    body_type = _annotation_for_parameter(body, factory)

    assert isinstance(body_type, type)
    assert issubclass(body_type, BaseModel)
    assert _annotation_for_parameter(query, factory) is int
    assert _annotation_for_parameter(unsupported, factory) is Any


def test_build_request_and_response_models_cover_fallbacks() -> None:
    factory = SwaggerModelFactory({"Thing": {"type": "object", "properties": {"id": {"type": "string"}}}})
    operation = _operation()
    bindings = [_Binding("thing_id", "ThingId", "path", True, str)]

    request_model = _build_request_model(operation, bindings)
    assert request_model.model_validate({"thing_id": "abc"}).thing_id == "abc"

    preferred = _build_response_model(
        OperationSpec(
            operation_id="Things_CreateThing",
            method="POST",
            path_template="/things",
            namespace="things",
            parameters=(),
            response_schemas={"201": {"$ref": "#/definitions/Thing"}},
            source_controller="Things",
        ),
        factory,
    )
    primitive = _build_response_model(
        OperationSpec(
            operation_id="Things_Count",
            method="GET",
            path_template="/count",
            namespace="things",
            parameters=(),
            response_schemas={"200": {"type": "integer"}},
            source_controller="Things",
        ),
        factory,
    )

    assert preferred is not None
    assert primitive is None


def test_to_request_components_splits_fields_by_location() -> None:
    class Payload(BaseModel):
        name: str
        optional: str | None = None

    request_model = _build_request_model(
        _operation(),
        [
            _Binding("thing_id", "ThingId", "path", True, str),
            _Binding("page", "page", "query", False, int),
            _Binding("site_id", "SiteId", "header", False, str),
            _Binding("payload", "payload", "body", False, Payload),
        ],
    )
    validated = request_model.model_validate(
        {
            "thing_id": "abc",
            "page": 2,
            "site_id": "site-42",
            "payload": {"name": "Desk"},
        }
    )

    components = _to_request_components(
        validated=validated,
        bindings=[
            _Binding("thing_id", "ThingId", "path", True, str),
            _Binding("page", "page", "query", False, int),
            _Binding("site_id", "SiteId", "header", False, str),
            _Binding("payload", "payload", "body", False, Payload),
        ],
    )

    assert components["path_params"] == {"ThingId": "abc"}
    assert components["params"] == {"page": 2}
    assert components["headers"] == {"SiteId": "site-42"}
    assert components["json_body"] == {"name": "Desk"}


def test_pagination_helpers_cover_alternate_names_and_extract_items() -> None:
    bindings = [
        _Binding("page_number", "PageNumber", "query", False, int),
        _Binding("page_size", "PageSize", "query", False, int),
    ]

    assert _find_page_binding(bindings) == "page_number"
    assert _find_page_size_binding(bindings) == "page_size"
    assert _extract_items([1, 2]) == [1, 2]
    assert _extract_items({"Results": [3]}) == [3]
    assert _extract_items({"unknown": "value"}) == []


def test_attach_aliases_registers_only_unique_aliases() -> None:
    namespace = Namespace("things")
    operation = _operation()
    namespace._register("get_thing", object())
    _attach_aliases(namespace, {"get_thing": operation})

    assert "get" in namespace.list_methods()
    assert _suggest_alias(operation) == "get"
    assert _suggest_alias(_operation(path="/things", method="GET")) == "list"
    assert _suggest_alias(_operation(path="/things", method="POST")) == "create"
    assert _suggest_alias(_operation(path="/things/{ThingId}", method="DELETE")) == "delete"


def test_operation_method_and_async_operation_method_dispatch_requests() -> None:
    factory = SwaggerModelFactory({"Thing": {"type": "object", "properties": {"id": {"type": "string"}}}})
    operation = OperationSpec(
        operation_id="Things_UpdateThing",
        method="PUT",
        path_template="/things/{ThingId}",
        namespace="things",
        parameters=(
            ParameterSpec("ThingId", "path", True, None, "string", None),
            ParameterSpec("SiteId", "header", False, None, "string", None),
            ParameterSpec("payload", "body", True, {"$ref": "#/definitions/Thing"}, None, None),
        ),
        response_schemas={"200": {"$ref": "#/definitions/Thing"}},
        source_controller="Things",
    )
    bindings = _operation_bindings(operation, factory)
    request_model = _build_request_model(operation, bindings)
    response_model = _build_response_model(operation, factory)
    sync_dispatcher = _SyncDispatcher({"id": "abc"})
    sync_method = OperationMethod(
        client=sync_dispatcher,
        operation=operation,
        bindings=bindings,
        request_model=request_model,
        response_model=response_model,
    )

    payload = sync_method(thing_id="abc", site_id="site-42", payload={"id": "abc"}, timeout=3.5)

    assert payload.model_dump() == {"id": "abc"}
    assert sync_dispatcher.calls[0]["path_params"] == {"ThingId": "abc"}
    assert sync_dispatcher.calls[0]["headers"] == {"SiteId": "site-42"}
    assert sync_dispatcher.calls[0]["json_body"] == {"id": "abc"}
    assert sync_dispatcher.calls[0]["timeout"] == 3.5

    async_dispatcher = _AsyncDispatcher({"id": "xyz"})
    async_method = AsyncOperationMethod(
        client=async_dispatcher,
        operation=operation,
        bindings=bindings,
        request_model=request_model,
        response_model=response_model,
    )

    async def run() -> dict[str, Any]:
        typed = await async_method(thing_id="xyz", payload={"id": "xyz"})
        raw = await async_method.raw(thing_id="xyz", payload={"id": "xyz"})
        assert typed.model_dump() == {"id": "xyz"}
        return raw

    raw_payload = asyncio.run(run())
    assert raw_payload == {"id": "xyz"}


def test_operation_method_iter_pages_without_page_binding_calls_once() -> None:
    dispatcher = _SyncDispatcher({"id": "abc"})
    operation = _operation()
    method = OperationMethod(
        client=dispatcher,
        operation=operation,
        bindings=[_Binding("thing_id", "ThingId", "path", True, str)],
        request_model=_build_request_model(operation, [_Binding("thing_id", "ThingId", "path", True, str)]),
        response_model=None,
    )

    pages = method.iter_pages(thing_id="abc")

    assert pages == [{"id": "abc"}]
    assert len(dispatcher.calls) == 1


def test_operation_method_validation_rejects_extra_fields() -> None:
    dispatcher = _SyncDispatcher({"id": "abc"})
    operation = _operation()
    method = OperationMethod(
        client=dispatcher,
        operation=operation,
        bindings=[_Binding("thing_id", "ThingId", "path", True, str)],
        request_model=_build_request_model(operation, [_Binding("thing_id", "ThingId", "path", True, str)]),
        response_model=None,
    )

    with pytest.raises(Exception):
        method.raw(thing_id="abc", unexpected=True)


def test_build_sdk_dedupes_names_when_operation_ids_collide() -> None:
    registry = build_schema_registry(
        [
            {
                "swagger": "2.0",
                "info": {"title": "Things Controller", "version": "1.0.0"},
                "paths": {
                    "/things/{ThingId}": {
                        "get": {"operationId": "Things_Get", "responses": {"200": {"schema": {"type": "object"}}}},
                        "post": {"operationId": "Things_Get", "responses": {"200": {"schema": {"type": "object"}}}},
                    }
                },
            }
        ]
    )

    from incident_py_q.sdk.runtime import build_sdk

    artifacts = build_sdk(client=object(), registry=registry, async_mode=False)
    methods = artifacts.namespaces["things"].list_methods()

    assert "get" in methods
    assert "get_1" in methods
