"""Schema normalization for known Incident IQ/Swagger irregularities."""

from __future__ import annotations

from copy import deepcopy
from typing import Any


def normalize_swagger_document(document: dict[str, Any]) -> dict[str, Any]:
    """Return a normalized copy of a Swagger 2.0 document.

    Normalization is intentionally narrow:
    - Convert `x-nullable: true` schemas into JSON Schema nullable forms.
    - Preserve all unknown extension fields to avoid contract drift.
    """
    normalized: dict[str, Any] = deepcopy(document)
    _walk_and_normalize(normalized)
    return normalized


def _walk_and_normalize(node: Any) -> Any:
    if isinstance(node, dict):
        _normalize_nullable(node)
        for value in node.values():
            _walk_and_normalize(value)
    elif isinstance(node, list):
        for item in node:
            _walk_and_normalize(item)
    return node


def _normalize_nullable(schema: dict[str, Any]) -> None:
    if not schema.get("x-nullable", False):
        return

    schema_type = schema.get("type")
    if isinstance(schema_type, str):
        schema["type"] = [schema_type, "null"]
        return

    if "$ref" in schema:
        ref = schema["$ref"]
        description = schema.get("description")
        any_of: list[dict[str, Any]] = [{"$ref": ref}, {"type": "null"}]
        schema.clear()
        schema["anyOf"] = any_of
        if description:
            schema["description"] = description

