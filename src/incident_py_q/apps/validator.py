"""Schema validation utilities for undocumented app-path endpoints."""

from __future__ import annotations

from typing import Any

from jsonschema import ValidationError as JSONSchemaValidationError
from jsonschema import validate

from incident_py_q.exceptions import SchemaValidationError
from incident_py_q.schema.loader import load_app_schemas


class AppSchemaValidator:
    """Validate app-path request/response payloads against bundled JSON schemas."""

    def __init__(self) -> None:
        loaded = load_app_schemas()
        if not isinstance(loaded, dict):
            raise ValueError("App schema bundle must be a JSON object.")
        self._schemas: dict[str, dict[str, Any]] = {}
        for key, schema in loaded.items():
            if isinstance(key, str) and isinstance(schema, dict):
                self._schemas[key] = schema

    def validate(self, schema_name: str, payload: Any) -> None:
        schema = self._schemas.get(schema_name)
        if schema is None:
            raise ValueError(f"Unknown app schema '{schema_name}'.")
        try:
            validate(instance=payload, schema=schema)
        except JSONSchemaValidationError as exc:
            raise SchemaValidationError(
                f"App schema validation failed for '{schema_name}': {exc.message}"
            ) from exc
