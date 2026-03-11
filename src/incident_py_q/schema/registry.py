"""Operation registry built from bundled Swagger controller documents."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any, Literal

from incident_py_q._utils import to_snake_case

from .normalize import normalize_swagger_document

ParameterLocation = Literal["path", "query", "header", "body"]
HTTP_METHODS = ("get", "post", "put", "delete", "patch", "head", "options")


@dataclass(frozen=True, slots=True)
class ParameterSpec:
    """A normalized request parameter specification for one operation."""

    name: str
    location: ParameterLocation
    required: bool
    schema: dict[str, Any] | None
    primitive_type: str | None
    description: str | None


@dataclass(frozen=True, slots=True)
class OperationSpec:
    """A normalized API operation contract derived from Swagger paths."""

    operation_id: str
    method: str
    path_template: str
    namespace: str
    parameters: tuple[ParameterSpec, ...]
    response_schemas: dict[str, dict[str, Any]]
    source_controller: str
    summary: str | None = None
    description: str | None = None

    @property
    def python_method_name(self) -> str:
        """Generate a stable snake_case method name from operationId."""
        if "_" in self.operation_id:
            _, suffix = self.operation_id.split("_", 1)
        else:
            suffix = self.operation_id
        return to_snake_case(suffix)


@dataclass(slots=True)
class _CompiledOperation:
    operation: OperationSpec
    regex: re.Pattern[str]


class SchemaRegistry:
    """Registry of operations and merged schema definitions."""

    def __init__(
        self,
        *,
        operations: list[OperationSpec],
        merged_document: dict[str, Any],
        controllers: dict[str, dict[str, Any]],
    ) -> None:
        self.operations = operations
        self.merged_document = merged_document
        self.controllers = controllers
        self._compiled = [_compile_operation(op) for op in operations]

        namespace_map: dict[str, list[OperationSpec]] = {}
        for operation in operations:
            namespace_map.setdefault(operation.namespace, []).append(operation)
        self.operations_by_namespace = {
            key: tuple(sorted(value, key=lambda item: (item.path_template, item.method)))
            for key, value in namespace_map.items()
        }

    def match_operation(self, method: str, path: str) -> OperationSpec | None:
        """Find an operation by method and rendered request path."""
        method_upper = method.upper()
        for compiled in self._compiled:
            if compiled.operation.method != method_upper:
                continue
            if compiled.regex.fullmatch(path):
                return compiled.operation
        return None

    def inventory(self) -> list[dict[str, str]]:
        """Return a stable public SDK inventory payload for golden tests."""
        return [
            {
                "namespace": op.namespace,
                "method": op.method,
                "path": op.path_template,
                "operation_id": op.operation_id,
                "python_method": op.python_method_name,
            }
            for op in sorted(
                self.operations, key=lambda item: (item.namespace, item.python_method_name)
            )
        ]


def build_schema_registry(swagger_documents: list[dict[str, Any]]) -> SchemaRegistry:
    """Build a full operation registry and merged definitions from controller specs."""
    normalized_docs = [normalize_swagger_document(document) for document in swagger_documents]

    merged_definitions: dict[str, dict[str, Any]] = {}
    merged_paths: dict[str, dict[str, Any]] = {}
    operations: list[OperationSpec] = []
    controllers: dict[str, dict[str, Any]] = {}

    for document in normalized_docs:
        controller_name = str(document.get("info", {}).get("title", "unknown"))
        controllers[controller_name] = document

        for definition_name, definition_schema in document.get("definitions", {}).items():
            existing = merged_definitions.get(definition_name)
            if existing is None:
                merged_definitions[definition_name] = definition_schema
            elif existing != definition_schema:
                raise ValueError(
                    f"Definition collision for '{definition_name}' in controller '{controller_name}'"
                )

        for raw_path, path_item in document.get("paths", {}).items():
            if raw_path in merged_paths:
                overlap = set(merged_paths[raw_path]).intersection(set(path_item))
                if overlap:
                    overlap_repr = ", ".join(sorted(overlap))
                    raise ValueError(
                        f"Path/method collision at '{raw_path}' ({overlap_repr}) "
                        f"while merging controller '{controller_name}'"
                    )
                merged_paths[raw_path] = {**merged_paths[raw_path], **path_item}
            else:
                merged_paths[raw_path] = dict(path_item)

            shared_parameters = tuple(_parse_parameters(path_item.get("parameters", [])))

            for method_name, operation_payload in path_item.items():
                if method_name not in HTTP_METHODS:
                    continue

                operation_id = operation_payload.get("operationId")
                if not operation_id:
                    operation_id = f"{controller_name}_{method_name}_{raw_path}".replace("/", "_")

                namespace = _namespace_from_path(raw_path)
                op_parameters = list(shared_parameters)
                op_parameters.extend(_parse_parameters(operation_payload.get("parameters", [])))
                response_schemas = _extract_response_schemas(operation_payload.get("responses", {}))

                operations.append(
                    OperationSpec(
                        operation_id=str(operation_id),
                        method=method_name.upper(),
                        path_template=raw_path,
                        namespace=namespace,
                        parameters=tuple(op_parameters),
                        response_schemas=response_schemas,
                        source_controller=controller_name,
                        summary=operation_payload.get("summary"),
                        description=operation_payload.get("description"),
                    )
                )

    merged_document: dict[str, Any] = {
        "swagger": "2.0",
        "info": {"title": "Incident IQ (Merged Controller Contract)", "version": "1.0.0"},
        "paths": merged_paths,
        "definitions": merged_definitions,
    }

    return SchemaRegistry(
        operations=sorted(operations, key=lambda op: (op.namespace, op.path_template, op.method)),
        merged_document=merged_document,
        controllers=controllers,
    )


def _parse_parameters(parameters: list[dict[str, Any]]) -> list[ParameterSpec]:
    parsed: list[ParameterSpec] = []
    for parameter in parameters:
        location = parameter.get("in")
        if location not in {"path", "query", "header", "body"}:
            continue

        schema_value: dict[str, Any] | None
        raw_schema = parameter.get("schema")
        schema_value = raw_schema if isinstance(raw_schema, dict) else None

        parsed.append(
            ParameterSpec(
                name=str(parameter.get("name", "")),
                location=location,
                required=bool(parameter.get("required", False)),
                schema=schema_value,
                primitive_type=parameter.get("type")
                if isinstance(parameter.get("type"), str)
                else None,
                description=parameter.get("description"),
            )
        )
    return parsed


def _extract_response_schemas(responses: dict[str, Any]) -> dict[str, dict[str, Any]]:
    extracted: dict[str, dict[str, Any]] = {}
    for status_code, response_payload in responses.items():
        schema = response_payload.get("schema")
        if isinstance(schema, dict):
            extracted[str(status_code)] = schema
    return extracted


def _namespace_from_path(path: str) -> str:
    stripped = path.strip("/")
    if not stripped:
        return "root"
    first = stripped.split("/", 1)[0]
    return to_snake_case(first)


def _compile_operation(operation: OperationSpec) -> _CompiledOperation:
    pattern = re.sub(r"\{[^}]+\}", "[^/]+", operation.path_template)
    regex = re.compile(f"^{pattern}$")
    return _CompiledOperation(operation=operation, regex=regex)
