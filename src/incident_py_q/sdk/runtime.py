"""Dynamic SDK namespace and operation method runtime."""

from __future__ import annotations

import inspect
from dataclasses import dataclass
from typing import Any, Protocol, cast

from pydantic import BaseModel, ConfigDict, Field, ValidationError, create_model

from incident_py_q._utils import to_snake_case
from incident_py_q.schema.registry import OperationSpec, ParameterSpec, SchemaRegistry

from .model_factory import SwaggerModelFactory


class _SupportsSyncOperationDispatch(Protocol):
    def _request_from_operation(
        self,
        operation: OperationSpec,
        *,
        path_params: dict[str, Any] | None,
        params: dict[str, Any] | None,
        json_body: Any | None,
        headers: dict[str, str] | None,
        timeout: float | None,
    ) -> dict[str, Any] | list[Any] | None: ...


class _SupportsAsyncOperationDispatch(Protocol):
    async def _request_from_operation(
        self,
        operation: OperationSpec,
        *,
        path_params: dict[str, Any] | None,
        params: dict[str, Any] | None,
        json_body: Any | None,
        headers: dict[str, str] | None,
        timeout: float | None,
    ) -> dict[str, Any] | list[Any] | None: ...


@dataclass(slots=True, frozen=True)
class _Binding:
    field_name: str
    original_name: str
    location: str
    required: bool
    annotation: Any


@dataclass(slots=True, frozen=True)
class SDKArtifacts:
    """Generated SDK namespaces and serialized inventory."""

    namespaces: dict[str, NamespaceBase]
    inventory: list[dict[str, str]]


class NamespaceBase:
    """Base class for sync and async namespace objects."""

    def __init__(self, name: str) -> None:
        self._name = name
        self._methods: dict[str, Any] = {}

    def _register(self, name: str, method: Any) -> None:
        self._methods[name] = method
        setattr(self, name, method)

    def list_methods(self) -> list[str]:
        """Return available method names for this namespace."""
        return sorted(self._methods.keys())

    def __dir__(self) -> list[str]:
        return sorted(set(list(super().__dir__()) + list(self._methods.keys())))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, methods={len(self._methods)})"


class Namespace(NamespaceBase):
    """Sync SDK namespace."""


class AsyncNamespace(NamespaceBase):
    """Async SDK namespace."""


class OperationMethod:
    """Sync callable method object for one generated operation."""

    def __init__(
        self,
        *,
        client: _SupportsSyncOperationDispatch,
        operation: OperationSpec,
        bindings: list[_Binding],
        request_model: type[BaseModel],
        response_model: type[BaseModel] | None,
    ) -> None:
        self._client = client
        self.operation = operation
        self.bindings = bindings
        self.request_model = request_model
        self.response_model = response_model
        self.__signature__ = _build_signature(bindings)
        self.__name__ = operation.python_method_name
        self.__doc__ = operation.description or operation.summary or ""

    def __call__(self, **kwargs: Any) -> Any:
        payload = self.raw(**kwargs)
        return _coerce_response(payload, self.response_model)

    def raw(self, **kwargs: Any) -> dict[str, Any] | list[Any] | None:
        bound = self.__signature__.bind(**kwargs)
        request_arguments = {
            key: value for key, value in bound.arguments.items() if key != "timeout"
        }
        validated = self.request_model.model_validate(request_arguments)
        request = _to_request_components(validated=validated, bindings=self.bindings)
        timeout = bound.arguments.get("timeout")
        return self._client._request_from_operation(self.operation, timeout=timeout, **request)

    def iter_pages(
        self,
        *,
        start_page: int = 1,
        page_size: int = 100,
        max_pages: int | None = None,
        **kwargs: Any,
    ) -> list[dict[str, Any] | list[Any] | None]:
        """Return successive raw page responses when paging params are present."""
        page_field = _find_page_binding(self.bindings)
        page_size_field = _find_page_size_binding(self.bindings)
        if page_field is None:
            return [self.raw(**kwargs)]

        pages: list[dict[str, Any] | list[Any] | None] = []
        page_number = start_page
        while True:
            call_kwargs = dict(kwargs)
            call_kwargs[page_field] = page_number
            if page_size_field:
                call_kwargs[page_size_field] = page_size

            page_payload = self.raw(**call_kwargs)
            pages.append(page_payload)
            items = _extract_items(page_payload)
            if not items:
                break
            page_number += 1
            if max_pages is not None and len(pages) >= max_pages:
                break
        return pages


class AsyncOperationMethod:
    """Async callable method object for one generated operation."""

    def __init__(
        self,
        *,
        client: _SupportsAsyncOperationDispatch,
        operation: OperationSpec,
        bindings: list[_Binding],
        request_model: type[BaseModel],
        response_model: type[BaseModel] | None,
    ) -> None:
        self._client = client
        self.operation = operation
        self.bindings = bindings
        self.request_model = request_model
        self.response_model = response_model
        self.__signature__ = _build_signature(bindings)
        self.__name__ = operation.python_method_name
        self.__doc__ = operation.description or operation.summary or ""

    async def __call__(self, **kwargs: Any) -> Any:
        payload = await self.raw(**kwargs)
        return _coerce_response(payload, self.response_model)

    async def raw(self, **kwargs: Any) -> dict[str, Any] | list[Any] | None:
        bound = self.__signature__.bind(**kwargs)
        request_arguments = {
            key: value for key, value in bound.arguments.items() if key != "timeout"
        }
        validated = self.request_model.model_validate(request_arguments)
        request = _to_request_components(validated=validated, bindings=self.bindings)
        timeout = bound.arguments.get("timeout")
        return await self._client._request_from_operation(self.operation, timeout=timeout, **request)


def build_sdk(
    *,
    client: Any,
    registry: SchemaRegistry,
    async_mode: bool,
) -> SDKArtifacts:
    """Create namespace objects and operation callables from a registry."""
    raw_definitions = registry.merged_document.get("definitions", {})
    definitions = raw_definitions if isinstance(raw_definitions, dict) else {}
    model_factory = SwaggerModelFactory(cast(dict[str, dict[str, Any]], definitions))
    namespaces: dict[str, NamespaceBase] = {}
    inventory: list[dict[str, str]] = []

    namespace_operations: dict[str, list[tuple[str, OperationSpec]]] = {}
    for operation in registry.operations:
        namespace_operations.setdefault(operation.namespace, []).append(
            (operation.python_method_name, operation)
        )

    for namespace_name, operations in sorted(namespace_operations.items()):
        namespace_obj: NamespaceBase = AsyncNamespace(namespace_name) if async_mode else Namespace(
            namespace_name
        )
        name_counts: dict[str, int] = {}
        method_names_for_aliasing: dict[str, OperationSpec] = {}

        for base_name, operation in operations:
            deduped_name = base_name
            if deduped_name in name_counts:
                name_counts[deduped_name] += 1
                deduped_name = f"{deduped_name}_{name_counts[deduped_name]}"
            else:
                name_counts[deduped_name] = 0

            bindings = _operation_bindings(operation, model_factory)
            request_model = _build_request_model(operation, bindings)
            response_model = _build_response_model(operation, model_factory)
            method_obj: Any

            if async_mode:
                method_obj = AsyncOperationMethod(
                    client=client,
                    operation=operation,
                    bindings=bindings,
                    request_model=request_model,
                    response_model=response_model,
                )
            else:
                method_obj = OperationMethod(
                    client=client,
                    operation=operation,
                    bindings=bindings,
                    request_model=request_model,
                    response_model=response_model,
                )

            namespace_obj._register(deduped_name, method_obj)
            method_names_for_aliasing[deduped_name] = operation
            inventory.append(
                {
                    "namespace": namespace_name,
                    "name": deduped_name,
                    "operation_id": operation.operation_id,
                    "method": operation.method,
                    "path": operation.path_template,
                }
            )

        _attach_aliases(namespace_obj, method_names_for_aliasing)
        namespaces[namespace_name] = namespace_obj

    return SDKArtifacts(namespaces=namespaces, inventory=sorted(inventory, key=str))


def _build_signature(bindings: list[_Binding]) -> inspect.Signature:
    parameters: list[inspect.Parameter] = []
    for binding in bindings:
        default = inspect._empty if binding.required else None
        parameters.append(
            inspect.Parameter(
                binding.field_name,
                kind=inspect.Parameter.KEYWORD_ONLY,
                default=default,
                annotation=binding.annotation,
            )
        )

    parameters.append(
        inspect.Parameter(
            "timeout",
            kind=inspect.Parameter.KEYWORD_ONLY,
            default=None,
            annotation=float | None,
        )
    )
    return inspect.Signature(parameters=parameters)


def _operation_bindings(
    operation: OperationSpec,
    model_factory: SwaggerModelFactory,
) -> list[_Binding]:
    bindings: list[_Binding] = []
    used: set[str] = set()
    for parameter in operation.parameters:
        if parameter.location == "header" and parameter.name.lower() in {"authorization", "content-type"}:
            continue
        if not parameter.name:
            continue
        field_name = to_snake_case(parameter.name)
        while field_name in used:
            field_name = f"{field_name}_arg"
        used.add(field_name)

        annotation = _annotation_for_parameter(parameter, model_factory)
        bindings.append(
            _Binding(
                field_name=field_name,
                original_name=parameter.name,
                location=parameter.location,
                required=parameter.required,
                annotation=annotation,
            )
        )

    return bindings


def _annotation_for_parameter(parameter: ParameterSpec, model_factory: SwaggerModelFactory) -> Any:
    if parameter.location == "body":
        return model_factory.type_from_schema(parameter.schema)
    if parameter.primitive_type:
        primitive = {
            "string": str,
            "integer": int,
            "number": float,
            "boolean": bool,
        }.get(parameter.primitive_type, Any)
        return primitive
    return Any


def _build_request_model(operation: OperationSpec, bindings: list[_Binding]) -> type[BaseModel]:
    fields: dict[str, tuple[Any, Any]] = {}
    for binding in bindings:
        default = ... if binding.required else None
        fields[binding.field_name] = (binding.annotation, Field(default=default))
    model = create_model(
        f"{operation.operation_id}Request",
        __config__=ConfigDict(extra="forbid"),
        **cast(Any, fields),
    )
    return cast(type[BaseModel], model)


def _build_response_model(
    operation: OperationSpec,
    model_factory: SwaggerModelFactory,
) -> type[BaseModel] | None:
    if not operation.response_schemas:
        return None

    schema = operation.response_schemas.get("200")
    if schema is None:
        schema = operation.response_schemas.get(next(iter(operation.response_schemas)))
    if schema is None:
        return None
    annotation = model_factory.type_from_schema(schema)
    if isinstance(annotation, type) and issubclass(annotation, BaseModel):
        return annotation
    return None


def _to_request_components(
    *,
    validated: BaseModel,
    bindings: list[_Binding],
) -> dict[str, dict[str, Any] | Any | None]:
    path_params: dict[str, Any] = {}
    query_params: dict[str, Any] = {}
    headers: dict[str, str] = {}
    json_body: Any | None = None

    for binding in bindings:
        value = getattr(validated, binding.field_name)
        if value is None:
            continue

        if isinstance(value, BaseModel):
            serializable_value: Any = value.model_dump(by_alias=True, exclude_none=True)
        else:
            serializable_value = value

        if binding.location == "path":
            path_params[binding.original_name] = serializable_value
        elif binding.location == "query":
            query_params[binding.original_name] = serializable_value
        elif binding.location == "header":
            headers[binding.original_name] = str(serializable_value)
        elif binding.location == "body":
            json_body = serializable_value

    return {
        "path_params": path_params or None,
        "params": query_params or None,
        "headers": headers or None,
        "json_body": json_body,
    }


def _coerce_response(payload: Any, response_model: type[BaseModel] | None) -> Any:
    if payload is None or response_model is None:
        return payload
    try:
        return response_model.model_validate(payload)
    except ValidationError as exc:
        raise ValueError(f"Response payload failed pydantic validation: {exc}") from exc


def _find_page_binding(bindings: list[_Binding]) -> str | None:
    candidates = {"page", "page_number", "p"}
    for binding in bindings:
        if binding.location != "query":
            continue
        if binding.field_name in candidates:
            return binding.field_name
        if binding.original_name in {"$p", "Page", "PageNumber", "page"}:
            return binding.field_name
    return None


def _find_page_size_binding(bindings: list[_Binding]) -> str | None:
    candidates = {"page_size", "s", "limit"}
    for binding in bindings:
        if binding.location != "query":
            continue
        if binding.field_name in candidates:
            return binding.field_name
        if binding.original_name in {"$s", "PageSize", "pageSize", "limit"}:
            return binding.field_name
    return None


def _extract_items(payload: Any) -> list[Any]:
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        for key in ("Data", "Items", "Results", "data", "items", "results"):
            maybe_list = payload.get(key)
            if isinstance(maybe_list, list):
                return maybe_list
    return []


def _attach_aliases(namespace: NamespaceBase, methods: dict[str, OperationSpec]) -> None:
    alias_candidates: dict[str, list[str]] = {"list": [], "get": [], "create": [], "update": [], "delete": []}
    for method_name, operation in methods.items():
        alias = _suggest_alias(operation)
        if alias:
            alias_candidates[alias].append(method_name)

    for alias_name, names in alias_candidates.items():
        if len(names) != 1:
            continue
        if alias_name in namespace.list_methods():
            continue
        namespace._register(alias_name, getattr(namespace, names[0]))


def _suggest_alias(operation: OperationSpec) -> str | None:
    path = operation.path_template
    method = operation.method
    if method == "GET" and "{" not in path and path.count("/") == 1:
        return "list"
    if method == "GET" and _is_simple_item_path(path):
        return "get"
    if method == "POST" and ("{" not in path) and (path.count("/") == 1 or path.endswith("/new")):
        return "create"
    if method in {"PUT", "POST"} and _is_simple_item_path(path):
        return "update"
    if method == "DELETE" and _is_simple_item_path(path):
        return "delete"
    return None


def _is_simple_item_path(path: str) -> bool:
    parts = [part for part in path.split("/") if part]
    return len(parts) == 2 and parts[1].startswith("{") and parts[1].endswith("}")
