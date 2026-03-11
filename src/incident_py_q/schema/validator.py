"""JSON-schema response validation against bundled Incident IQ contracts."""

from __future__ import annotations

from typing import Any

from jsonschema import RefResolver, validators
from jsonschema import ValidationError as JSONSchemaValidationError

from incident_py_q.exceptions import SchemaValidationError

from .registry import OperationSpec, SchemaRegistry


class ResponseSchemaValidator:
    """Validate HTTP payloads against operation response schemas."""

    def __init__(self, registry: SchemaRegistry) -> None:
        self._registry = registry
        self._validator_cls = validators.validator_for(registry.merged_document)
        self._resolver = RefResolver.from_schema(registry.merged_document)

    def validate(
        self,
        operation: OperationSpec,
        *,
        status_code: int,
        payload: Any,
    ) -> None:
        """Validate a payload against the operation's matched response schema.

        Raises:
            SchemaValidationError: if payload fails schema validation.
        """
        response_schema = _pick_response_schema(
            response_schemas=operation.response_schemas,
            status_code=status_code,
        )
        if response_schema is None:
            return

        validator = self._validator_cls(
            response_schema,
            resolver=self._resolver,
        )

        try:
            validator.validate(payload)
        except JSONSchemaValidationError as exc:
            raise SchemaValidationError(
                f"Response schema validation failed for {operation.method} "
                f"{operation.path_template} ({operation.operation_id}): {exc.message}"
            ) from exc


def _pick_response_schema(
    *,
    response_schemas: dict[str, dict[str, Any]],
    status_code: int,
) -> dict[str, Any] | None:
    """Pick the most specific response schema for a status code.

    Fallback order:
    1. Exact status code (`200`, `404`, ...)
    2. Status-class wildcard (`2xx`, `2XX`, ...)
    3. `default`
    """
    exact = response_schemas.get(str(status_code))
    if exact is not None:
        return exact

    class_prefix = f"{str(status_code)[0]}xx"
    for candidate in response_schemas:
        if candidate.lower() == class_prefix:
            return response_schemas[candidate]

    return response_schemas.get("default")
