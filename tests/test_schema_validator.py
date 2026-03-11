"""Tests for runtime JSON-schema response validation behavior."""

from __future__ import annotations

import pytest

from incident_py_q.exceptions import SchemaValidationError
from incident_py_q.schema.registry import OperationSpec, SchemaRegistry
from incident_py_q.schema.validator import ResponseSchemaValidator


def test_response_validation_passes_for_valid_payload(tiny_registry: SchemaRegistry) -> None:
    operation = tiny_registry.match_operation("GET", "/things/abc")
    assert operation is not None

    validator = ResponseSchemaValidator(tiny_registry)
    validator.validate(operation, status_code=200, payload={"id": "abc", "name": "Desk"})


def test_response_validation_raises_on_schema_mismatch(tiny_registry: SchemaRegistry) -> None:
    operation = tiny_registry.match_operation("GET", "/things/abc")
    assert operation is not None

    validator = ResponseSchemaValidator(tiny_registry)
    with pytest.raises(SchemaValidationError):
        validator.validate(operation, status_code=200, payload={"id": "abc"})


def test_response_validation_uses_status_class_fallback(tiny_registry: SchemaRegistry) -> None:
    operation = tiny_registry.match_operation("GET", "/maybe")
    assert operation is not None
    assert "2XX" in operation.response_schemas

    validator = ResponseSchemaValidator(tiny_registry)
    validator.validate(operation, status_code=204, payload={"ok": True})


def test_response_validation_uses_default_fallback(tiny_registry: SchemaRegistry) -> None:
    operation = OperationSpec(
        operation_id="Fallback_GetDefault",
        method="GET",
        path_template="/default",
        namespace="default",
        parameters=(),
        response_schemas={
            "default": {
                "type": "object",
                "required": ["status"],
                "properties": {"status": {"type": "string"}},
            }
        },
        source_controller="test",
    )
    validator = ResponseSchemaValidator(tiny_registry)
    validator.validate(operation, status_code=418, payload={"status": "ok"})
