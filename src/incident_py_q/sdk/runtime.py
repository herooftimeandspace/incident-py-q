"""Dynamic SDK namespace, metadata, and operation method runtime."""

from __future__ import annotations

import inspect
import types
from dataclasses import dataclass
from typing import Any, Protocol, Union, cast, get_args, get_origin

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
class SDKParameterMetadata:
    """Documentation and typing metadata for one generated method parameter."""

    python_name: str
    api_name: str
    location: str
    required: bool
    annotation: Any
    annotation_display: str
    description: str | None
    schema_ref: str | None
    model_name: str | None
    primitive_type: str | None


@dataclass(slots=True, frozen=True)
class SDKMethodMetadata:
    """Canonical metadata for one generated SDK method."""

    namespace: str
    name: str
    aliases: tuple[str, ...]
    operation: OperationSpec
    bindings: tuple[_Binding, ...]
    parameters: tuple[SDKParameterMetadata, ...]
    request_model: type[BaseModel]
    response_model: type[BaseModel] | None
    signature: inspect.Signature
    request_model_name: str
    response_model_name: str | None
    response_schema_ref: str | None
    response_type_display: str
    raw_return_type_display: str
    supports_pagination: bool


@dataclass(slots=True, frozen=True)
class SDKArtifacts:
    """Generated SDK namespaces and serialized inventory."""

    namespaces: dict[str, NamespaceBase]
    inventory: list[dict[str, str]]
    metadata: tuple[SDKMethodMetadata, ...]


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
        metadata: SDKMethodMetadata | None = None,
        operation: OperationSpec | None = None,
        bindings: list[_Binding] | None = None,
        request_model: type[BaseModel] | None = None,
        response_model: type[BaseModel] | None = None,
    ) -> None:
        if metadata is None:
            metadata = _metadata_from_method_parts(
                operation=operation,
                bindings=bindings,
                request_model=request_model,
                response_model=response_model,
            )
        self._client = client
        self.metadata = metadata
        self.operation = metadata.operation
        self.bindings = list(metadata.bindings)
        self.request_model = metadata.request_model
        self.response_model = metadata.response_model
        self.__signature__ = metadata.signature
        self.__name__ = metadata.name
        self.__doc__ = format_operation_docstring(metadata, async_mode=False)

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
        metadata: SDKMethodMetadata | None = None,
        operation: OperationSpec | None = None,
        bindings: list[_Binding] | None = None,
        request_model: type[BaseModel] | None = None,
        response_model: type[BaseModel] | None = None,
    ) -> None:
        if metadata is None:
            metadata = _metadata_from_method_parts(
                operation=operation,
                bindings=bindings,
                request_model=request_model,
                response_model=response_model,
            )
        self._client = client
        self.metadata = metadata
        self.operation = metadata.operation
        self.bindings = list(metadata.bindings)
        self.request_model = metadata.request_model
        self.response_model = metadata.response_model
        self.__signature__ = metadata.signature
        self.__name__ = metadata.name
        self.__doc__ = format_operation_docstring(metadata, async_mode=True)

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
    metadata = build_sdk_metadata(registry)
    namespaces: dict[str, NamespaceBase] = {}
    inventory: list[dict[str, str]] = []
    metadata_by_namespace: dict[str, list[SDKMethodMetadata]] = {}
    for method_metadata in metadata:
        metadata_by_namespace.setdefault(method_metadata.namespace, []).append(method_metadata)

    for namespace_name, methods in sorted(metadata_by_namespace.items()):
        namespace_obj: NamespaceBase = AsyncNamespace(namespace_name) if async_mode else Namespace(
            namespace_name
        )
        for method_metadata in methods:
            method_obj: Any

            if async_mode:
                method_obj = AsyncOperationMethod(
                    client=client,
                    metadata=method_metadata,
                )
            else:
                method_obj = OperationMethod(
                    client=client,
                    metadata=method_metadata,
                )

            namespace_obj._register(method_metadata.name, method_obj)
            inventory.append(
                {
                    "namespace": namespace_name,
                    "name": method_metadata.name,
                    "operation_id": method_metadata.operation.operation_id,
                    "method": method_metadata.operation.method,
                    "path": method_metadata.operation.path_template,
                }
            )

        for method_metadata in methods:
            method_obj = getattr(namespace_obj, method_metadata.name)
            for alias_name in method_metadata.aliases:
                namespace_obj._register(alias_name, method_obj)
        namespaces[namespace_name] = namespace_obj

    return SDKArtifacts(
        namespaces=namespaces,
        inventory=sorted(inventory, key=str),
        metadata=metadata,
    )


def build_sdk_metadata(registry: SchemaRegistry) -> tuple[SDKMethodMetadata, ...]:
    """Return canonical generated SDK metadata for docs and typing artifacts."""
    raw_definitions = registry.merged_document.get("definitions", {})
    definitions = raw_definitions if isinstance(raw_definitions, dict) else {}
    model_factory = SwaggerModelFactory(cast(dict[str, dict[str, Any]], definitions))
    metadata: list[SDKMethodMetadata] = []

    namespace_operations: dict[str, list[tuple[str, OperationSpec]]] = {}
    for operation in registry.operations:
        namespace_operations.setdefault(operation.namespace, []).append(
            (operation.python_method_name, operation)
        )

    for namespace_name, operations in sorted(namespace_operations.items()):
        name_counts: dict[str, int] = {}
        method_names_for_aliasing: dict[str, OperationSpec] = {}
        namespace_metadata: list[SDKMethodMetadata] = []

        for base_name, operation in operations:
            deduped_name = base_name
            if deduped_name in name_counts:
                name_counts[deduped_name] += 1
                deduped_name = f"{deduped_name}_{name_counts[deduped_name]}"
            else:
                name_counts[deduped_name] = 0

            namespace_metadata.append(
                _build_method_metadata(
                    namespace=namespace_name,
                    name=deduped_name,
                    operation=operation,
                    model_factory=model_factory,
                )
            )
            method_names_for_aliasing[deduped_name] = operation

        alias_map = _build_alias_map(method_names_for_aliasing)
        alias_lookup: dict[str, list[str]] = {name: [] for name in method_names_for_aliasing}
        for alias_name, canonical_name in alias_map.items():
            alias_lookup.setdefault(canonical_name, []).append(alias_name)

        for method_metadata in namespace_metadata:
            metadata.append(
                SDKMethodMetadata(
                    namespace=method_metadata.namespace,
                    name=method_metadata.name,
                    aliases=tuple(sorted(alias_lookup.get(method_metadata.name, []))),
                    operation=method_metadata.operation,
                    bindings=method_metadata.bindings,
                    parameters=method_metadata.parameters,
                    request_model=method_metadata.request_model,
                    response_model=method_metadata.response_model,
                    signature=method_metadata.signature,
                    request_model_name=method_metadata.request_model_name,
                    response_model_name=method_metadata.response_model_name,
                    response_schema_ref=method_metadata.response_schema_ref,
                    response_type_display=method_metadata.response_type_display,
                    raw_return_type_display=method_metadata.raw_return_type_display,
                    supports_pagination=method_metadata.supports_pagination,
                )
            )

    return tuple(sorted(metadata, key=lambda item: (item.namespace, item.name)))


def format_annotation(annotation: Any) -> str:
    """Return a stable, readable Python type representation."""
    if annotation is Any:
        return "Any"
    if annotation is None or annotation is type(None):
        return "None"
    if isinstance(annotation, type):
        if issubclass(annotation, BaseModel):
            return annotation.__name__
        if annotation.__module__ == "builtins":
            return annotation.__name__
        return f"{annotation.__module__}.{annotation.__name__}"

    origin = get_origin(annotation)
    if origin in {list, tuple, dict, set}:
        args = get_args(annotation)
        if origin is list:
            return f"list[{format_annotation(args[0])}]" if args else "list[Any]"
        if origin is tuple:
            if not args:
                return "tuple[Any, ...]"
            if len(args) == 2 and args[1] is Ellipsis:
                return f"tuple[{format_annotation(args[0])}, ...]"
            return f"tuple[{', '.join(format_annotation(arg) for arg in args)}]"
        if origin is dict:
            if len(args) == 2:
                return f"dict[{format_annotation(args[0])}, {format_annotation(args[1])}]"
            return "dict[str, Any]"
        if origin is set:
            return f"set[{format_annotation(args[0])}]" if args else "set[Any]"

    if origin in {Union, types.UnionType}:
        return " | ".join(format_annotation(arg) for arg in get_args(annotation))

    return inspect.formatannotation(annotation)


def format_operation_docstring(metadata: SDKMethodMetadata, *, async_mode: bool) -> str:
    """Build a structured docstring for one generated SDK method."""
    summary = metadata.operation.summary or "No contract summary provided."
    description = metadata.operation.description
    lines = [summary]
    if description and description != summary:
        lines.extend(["", description])

    lines.extend(
        [
            "",
            f"HTTP route: {metadata.operation.method} {metadata.operation.path_template}",
            f"Source controller: {metadata.operation.source_controller}",
        ]
    )

    if metadata.aliases:
        lines.append(f"Aliases: {', '.join(metadata.aliases)}")

    lines.extend(["", "Parameters:"])
    if metadata.parameters:
        for parameter in metadata.parameters:
            required = "required" if parameter.required else "optional"
            description_suffix = f" {parameter.description}" if parameter.description else ""
            lines.append(
                f"- `{parameter.python_name}` ({parameter.annotation_display}, {required}, "
                f"{parameter.location} -> `{parameter.api_name}`).{description_suffix}"
            )
    else:
        lines.append("- This operation does not define request parameters.")

    call_prefix = "await " if async_mode else ""
    lines.extend(
        [
            "",
            "Returns:",
            f"- `{call_prefix}client.{metadata.namespace}.{metadata.name}(...)` returns "
            f"`{metadata.response_type_display}`.",
            f"- `{call_prefix}client.{metadata.namespace}.{metadata.name}.raw(...)` returns "
            f"`{metadata.raw_return_type_display}`.",
        ]
    )

    if not async_mode:
        if metadata.supports_pagination:
            lines.append(
                f"- `client.{metadata.namespace}.{metadata.name}.iter_pages(...)` fetches "
                "successive raw page responses."
            )
        else:
            lines.append(
                f"- `client.{metadata.namespace}.{metadata.name}.iter_pages(...)` returns a "
                "single raw response when no paging parameters are present."
            )

    return "\n".join(lines)


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


def _build_method_metadata(
    *,
    namespace: str,
    name: str,
    operation: OperationSpec,
    model_factory: SwaggerModelFactory,
) -> SDKMethodMetadata:
    bindings = tuple(_operation_bindings(operation, model_factory))
    request_model = _build_request_model(operation, list(bindings))
    response_model = _build_response_model(operation, model_factory)
    response_schema = _preferred_response_schema(operation)
    response_annotation = model_factory.type_from_schema(response_schema) if response_schema else Any
    parameters = tuple(_build_parameter_metadata(operation, bindings))
    return SDKMethodMetadata(
        namespace=namespace,
        name=name,
        aliases=(),
        operation=operation,
        bindings=bindings,
        parameters=parameters,
        request_model=request_model,
        response_model=response_model,
        signature=_build_signature(list(bindings)),
        request_model_name=request_model.__name__,
        response_model_name=response_model.__name__ if response_model is not None else None,
        response_schema_ref=_schema_ref_name(response_schema),
        response_type_display=(
            response_model.__name__ if response_model is not None else format_annotation(response_annotation)
        ),
        raw_return_type_display="dict[str, Any] | list[Any] | None",
        supports_pagination=_find_page_binding(list(bindings)) is not None,
    )


def _metadata_from_method_parts(
    *,
    operation: OperationSpec | None,
    bindings: list[_Binding] | None,
    request_model: type[BaseModel] | None,
    response_model: type[BaseModel] | None,
) -> SDKMethodMetadata:
    if operation is None or bindings is None or request_model is None:
        raise TypeError(
            "metadata or operation/bindings/request_model must be provided to construct "
            "an operation method."
        )

    binding_tuple = tuple(bindings)
    parameters = tuple(_build_parameter_metadata(operation, binding_tuple))
    return SDKMethodMetadata(
        namespace=operation.namespace,
        name=operation.python_method_name,
        aliases=(),
        operation=operation,
        bindings=binding_tuple,
        parameters=parameters,
        request_model=request_model,
        response_model=response_model,
        signature=_build_signature(bindings),
        request_model_name=request_model.__name__,
        response_model_name=response_model.__name__ if response_model is not None else None,
        response_schema_ref=_schema_ref_name(_preferred_response_schema(operation)),
        response_type_display=(
            response_model.__name__
            if response_model is not None
            else "dict[str, Any] | list[Any] | None"
        ),
        raw_return_type_display="dict[str, Any] | list[Any] | None",
        supports_pagination=_find_page_binding(bindings) is not None,
    )


def _build_parameter_metadata(
    operation: OperationSpec,
    bindings: tuple[_Binding, ...],
) -> list[SDKParameterMetadata]:
    metadata: list[SDKParameterMetadata] = []
    for binding in bindings:
        source_parameter = next(
            (
                parameter
                for parameter in operation.parameters
                if parameter.name == binding.original_name and parameter.location == binding.location
            ),
            None,
        )
        metadata.append(
            SDKParameterMetadata(
                python_name=binding.field_name,
                api_name=binding.original_name,
                location=binding.location,
                required=binding.required,
                annotation=binding.annotation,
                annotation_display=format_annotation(binding.annotation),
                description=source_parameter.description if source_parameter is not None else None,
                schema_ref=(
                    _schema_ref_name(source_parameter.schema) if source_parameter is not None else None
                ),
                model_name=_model_name_for_annotation(binding.annotation),
                primitive_type=source_parameter.primitive_type if source_parameter is not None else None,
            )
        )
    return metadata


def _model_name_for_annotation(annotation: Any) -> str | None:
    if isinstance(annotation, type) and issubclass(annotation, BaseModel):
        return annotation.__name__
    return None


def _schema_ref_name(schema: dict[str, Any] | None) -> str | None:
    if not schema:
        return None
    ref_value = schema.get("$ref")
    if isinstance(ref_value, str):
        return ref_value.rsplit("/", 1)[-1]
    return None


def _preferred_response_schema(operation: OperationSpec) -> dict[str, Any] | None:
    if not operation.response_schemas:
        return None
    schema = operation.response_schemas.get("200")
    if schema is not None:
        return schema
    return operation.response_schemas.get(next(iter(operation.response_schemas)))


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


def _build_alias_map(methods: dict[str, OperationSpec]) -> dict[str, str]:
    alias_candidates: dict[str, list[str]] = {"list": [], "get": [], "create": [], "update": [], "delete": []}
    for method_name, operation in methods.items():
        alias = _suggest_alias(operation)
        if alias:
            alias_candidates[alias].append(method_name)

    alias_map: dict[str, str] = {}
    for alias_name, names in alias_candidates.items():
        if len(names) != 1:
            continue
        alias_map[alias_name] = names[0]
    return alias_map


def _attach_aliases(namespace: NamespaceBase, methods: dict[str, OperationSpec]) -> None:
    for alias_name, canonical_name in _build_alias_map(methods).items():
        if alias_name in namespace.list_methods():
            continue
        namespace._register(alias_name, getattr(namespace, canonical_name))


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
