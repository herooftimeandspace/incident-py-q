"""Coverage-oriented tests for SDK runtime helper branches."""

from __future__ import annotations

import asyncio
import inspect
from typing import Any

from pydantic import BaseModel

from incident_py_q.schema.registry import OperationSpec, ParameterSpec, build_schema_registry
from incident_py_q.sdk.model_factory import SwaggerModelFactory
from incident_py_q.sdk.runtime import (
    AsyncNamespace,
    AsyncOperationMethod,
    Namespace,
    OperationMethod,
    _annotation_for_parameter,
    _attach_aliases,
    _Binding,
    _build_request_model,
    _build_response_model,
    _build_signature,
    _extract_items,
    _find_page_binding,
    _find_page_size_binding,
    _is_simple_item_path,
    _operation_bindings,
    _suggest_alias,
    _to_request_components,
    build_sdk,
)


class _SyncDispatch:
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
    ) -> dict[str, Any] | list[Any] | None:
        self.calls.append(
            {
                "operation_id": operation.operation_id,
                "path_params": path_params,
                "params": params,
                "json_body": json_body,
                "headers": headers,
                "timeout": timeout,
            }
        )
        payload = self.payload
        if payload is None or isinstance(payload, (dict, list)):
            return payload
        raise AssertionError(f"Unsupported payload type: {type(payload)!r}")


class _AsyncDispatch:
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
    ) -> dict[str, Any] | list[Any] | None:
        self.calls.append(
            {
                "operation_id": operation.operation_id,
                "path_params": path_params,
                "params": params,
                "json_body": json_body,
                "headers": headers,
                "timeout": timeout,
            }
        )
        payload = self.payload
        if payload is None or isinstance(payload, (dict, list)):
            return payload
        raise AssertionError(f"Unsupported payload type: {type(payload)!r}")


def _fixture_operation() -> OperationSpec:
    return OperationSpec(
        operation_id="Things_GetThing",
        method="GET",
        path_template="/things/{ThingId}",
        namespace="things",
        parameters=(
            ParameterSpec(name="ThingId", location="path", required=True, schema=None, primitive_type="string", description=None),
            ParameterSpec(name="page", location="query", required=False, schema=None, primitive_type="integer", description=None),
            ParameterSpec(name="X-Test", location="header", required=False, schema=None, primitive_type="string", description=None),
        ),
        response_schemas={"200": {"type": "object", "required": ["id"], "properties": {"id": {"type": "string"}}}},
        source_controller="test",
    )


def test_namespace_base_helpers_and_alias_attachment() -> None:
    namespace = Namespace("things")
    namespace._register("existing", object())
    namespace._register("get_thing", object())
    namespace._register("get_things_a", object())
    namespace._register("get_things_b", object())
    assert "existing" in namespace.list_methods()
    assert "existing" in dir(namespace)
    assert "methods=4" in repr(namespace)

    methods = {
        "get_things_a": OperationSpec(
            operation_id="Things_GetThingsA",
            method="GET",
            path_template="/things",
            namespace="things",
            parameters=(),
            response_schemas={},
            source_controller="test",
        ),
        "get_things_b": OperationSpec(
            operation_id="Things_GetThingsB",
            method="GET",
            path_template="/things",
            namespace="things",
            parameters=(),
            response_schemas={},
            source_controller="test",
        ),
        "get_thing": _fixture_operation(),
    }
    _attach_aliases(namespace, methods)
    assert "get" in namespace.list_methods()
    assert "list" not in namespace.list_methods()


def test_operation_bindings_and_signature_helpers() -> None:
    factory = SwaggerModelFactory(definitions={})
    op = OperationSpec(
        operation_id="Things_Search",
        method="POST",
        path_template="/things/search",
        namespace="things",
        parameters=(
            ParameterSpec(name="Authorization", location="header", required=False, schema=None, primitive_type="string", description=None),
            ParameterSpec(name="Content-Type", location="header", required=False, schema=None, primitive_type="string", description=None),
            ParameterSpec(name="", location="query", required=False, schema=None, primitive_type="string", description=None),
            ParameterSpec(name="Page", location="query", required=False, schema=None, primitive_type="integer", description=None),
            ParameterSpec(name="page", location="query", required=False, schema=None, primitive_type="integer", description=None),
            ParameterSpec(name="Payload", location="body", required=False, schema={"type": "object"}, primitive_type=None, description=None),
        ),
        response_schemas={},
        source_controller="test",
    )
    bindings = _operation_bindings(op, factory)
    assert [b.field_name for b in bindings] == ["page", "page_arg", "payload"]
    signature = _build_signature(bindings)
    assert "timeout" in signature.parameters
    assert signature.parameters["page"].default is None


def test_request_component_and_paging_helpers() -> None:
    class BodyModel(BaseModel):
        model_config = {"extra": "forbid"}
        id: str

    bindings = [
        _Binding("thing_id", "ThingId", "path", True, str),
        _Binding("page", "page", "query", False, int),
        _Binding("x_test", "X-Test", "header", False, str),
        _Binding("payload", "payload", "body", False, BodyModel),
        _Binding("ignored", "Ignored", "formData", False, str),
    ]
    model = _build_request_model(
        OperationSpec(
            operation_id="Things_UpdateThing",
            method="PUT",
            path_template="/things/{ThingId}",
            namespace="things",
            parameters=(),
            response_schemas={},
            source_controller="test",
        ),
        bindings,
    )
    validated = model.model_validate(
        {"thing_id": "abc", "page": 2, "x_test": "ok", "payload": BodyModel(id="abc")}
    )
    components = _to_request_components(validated=validated, bindings=bindings)
    assert components["path_params"] == {"ThingId": "abc"}
    assert components["params"] == {"page": 2}
    assert components["headers"] == {"X-Test": "ok"}
    assert components["json_body"] == {"id": "abc"}

    assert _find_page_binding(bindings) == "page"
    size_bindings = [_Binding("size", "$s", "query", False, int)]
    assert _find_page_size_binding(size_bindings) == "size"
    assert _find_page_binding([_Binding("id", "ThingId", "path", True, str)]) is None
    assert _find_page_size_binding([_Binding("id", "ThingId", "path", True, str)]) is None

    assert _extract_items([1, 2]) == [1, 2]
    assert _extract_items({"Data": [1]}) == [1]
    assert _extract_items({"Items": [1]}) == [1]
    assert _extract_items({"Results": [1]}) == [1]
    assert _extract_items({"data": [1]}) == [1]
    assert _extract_items({"items": [1]}) == [1]
    assert _extract_items({"results": [1]}) == [1]
    assert _extract_items({"none": "here"}) == []


def test_operation_method_and_async_operation_method_paths() -> None:
    op = _fixture_operation()
    bindings = [
        _Binding("thing_id", "ThingId", "path", True, str),
        _Binding("page", "page", "query", False, int),
    ]
    request_model = _build_request_model(op, bindings)
    response_model = _build_response_model(
        op,
        SwaggerModelFactory(definitions={"Thing": {"type": "object", "properties": {"id": {"type": "string"}}}}),
    )
    sync_dispatch = _SyncDispatch(payload={"id": "abc"})
    method = OperationMethod(
        client=sync_dispatch,
        operation=op,
        bindings=bindings,
        request_model=request_model,
        response_model=response_model,
    )
    result = method(thing_id="abc", page=1)
    assert isinstance(result, BaseModel)
    assert sync_dispatch.calls[0]["params"] == {"page": 1}
    pages = method.iter_pages(start_page=1, page_size=50, max_pages=1, thing_id="abc")
    assert len(pages) == 1

    no_page_method = OperationMethod(
        client=_SyncDispatch(payload={"id": "abc"}),
        operation=op,
        bindings=[_Binding("thing_id", "ThingId", "path", True, str)],
        request_model=_build_request_model(op, [_Binding("thing_id", "ThingId", "path", True, str)]),
        response_model=None,
    )
    assert len(no_page_method.iter_pages(thing_id="abc")) == 1

    async def run() -> None:
        async_dispatch = _AsyncDispatch(payload={"id": "abc"})
        async_method = AsyncOperationMethod(
            client=async_dispatch,
            operation=op,
            bindings=bindings,
            request_model=request_model,
            response_model=response_model,
        )
        payload = await async_method.raw(thing_id="abc", page=3)
        assert payload == {"id": "abc"}
        typed = await async_method(thing_id="abc", page=3)
        assert isinstance(typed, BaseModel)

    asyncio.run(run())


def test_alias_suggestion_annotation_and_path_helpers() -> None:
    body_param = ParameterSpec(name="payload", location="body", required=False, schema={"type": "object"}, primitive_type=None, description=None)
    primitive_param = ParameterSpec(name="count", location="query", required=False, schema=None, primitive_type="integer", description=None)
    unknown_param = ParameterSpec(name="mystery", location="query", required=False, schema=None, primitive_type=None, description=None)
    factory = SwaggerModelFactory(definitions={})
    assert _annotation_for_parameter(body_param, factory) is not None
    assert _annotation_for_parameter(primitive_param, factory) is int
    assert _annotation_for_parameter(unknown_param, factory) is Any

    op_list = OperationSpec("A_List", "GET", "/things", "things", (), {}, "test")
    op_get = OperationSpec("A_Get", "GET", "/things/{ThingId}", "things", (), {}, "test")
    op_create = OperationSpec("A_Create", "POST", "/things/new", "things", (), {}, "test")
    op_update = OperationSpec("A_Update", "PUT", "/things/{ThingId}", "things", (), {}, "test")
    op_delete = OperationSpec("A_Delete", "DELETE", "/things/{ThingId}", "things", (), {}, "test")
    op_none = OperationSpec("A_None", "PATCH", "/things/{ThingId}/nested", "things", (), {}, "test")
    assert _suggest_alias(op_list) == "list"
    assert _suggest_alias(op_get) == "get"
    assert _suggest_alias(op_create) == "create"
    assert _suggest_alias(op_update) == "update"
    assert _suggest_alias(op_delete) == "delete"
    assert _suggest_alias(op_none) is None
    assert _is_simple_item_path("/things/{ThingId}") is True
    assert _is_simple_item_path("/things/{ThingId}/nested") is False


def test_build_sdk_with_deduped_method_names() -> None:
    doc = {
        "swagger": "2.0",
        "info": {"title": "Dup Controller", "version": "1.0.0"},
        "paths": {
            "/widgets/{WidgetId}": {
                "get": {
                    "operationId": "Widgets_GetThing",
                    "parameters": [{"name": "WidgetId", "in": "path", "required": True, "type": "string"}],
                    "responses": {"200": {"schema": {"type": "object", "properties": {"id": {"type": "string"}}}}},
                }
            },
            "/widgets/{WidgetId}/details": {
                "get": {
                    "operationId": "Widgets_GetThing",
                    "parameters": [{"name": "WidgetId", "in": "path", "required": True, "type": "string"}],
                    "responses": {"200": {"schema": {"type": "object", "properties": {"id": {"type": "string"}}}}},
                }
            },
            "/widgets": {
                "post": {
                    "operationId": "Widgets_CreateWidget",
                    "responses": {"200": {"schema": {"type": "object", "properties": {"id": {"type": "string"}}}}},
                }
            },
        },
        "definitions": {},
    }
    registry = build_schema_registry([doc])
    artifacts = build_sdk(client=_SyncDispatch(payload={"id": "x"}), registry=registry, async_mode=False)
    widgets = artifacts.namespaces["widgets"]
    assert "get_thing" in widgets.list_methods()
    assert "get_thing_1" in widgets.list_methods()

    async_artifacts = build_sdk(client=_AsyncDispatch(payload={"id": "x"}), registry=registry, async_mode=True)
    assert isinstance(async_artifacts.namespaces["widgets"], AsyncNamespace)

    namespace = Namespace("x")
    namespace._register("list", object())
    _attach_aliases(namespace, {"list_widgets": OperationSpec("W_List", "GET", "/widgets", "widgets", (), {}, "test")})
    assert inspect.isroutine(getattr(namespace, "list", None)) is False
