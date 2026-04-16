"""Coverage tests for app schema validator error branches."""

from __future__ import annotations

import pytest

import incident_py_q.apps.validator as validator_module
from incident_py_q.apps.validator import AppSchemaValidator
from incident_py_q.exceptions import SchemaValidationError


def test_validator_rejects_non_object_bundle(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(validator_module, "load_app_schemas", lambda: [])
    with pytest.raises(ValueError, match="JSON object"):
        AppSchemaValidator()


def test_validator_unknown_schema_name_raises_value_error() -> None:
    validator = AppSchemaValidator()
    with pytest.raises(ValueError, match="Unknown app schema"):
        validator.validate("missing_schema", {})


def test_validator_wraps_jsonschema_failures() -> None:
    validator = AppSchemaValidator()
    with pytest.raises(SchemaValidationError, match="App schema validation failed"):
        validator.validate("registry_response", {"ItemCount": "bad-type"})
