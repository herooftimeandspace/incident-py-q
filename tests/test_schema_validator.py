"""Tests for runtime JSON-schema response validation behavior."""

from __future__ import annotations

import pytest

from incident_py_q.exceptions import SchemaValidationError
from incident_py_q.schema.registry import OperationSpec, SchemaRegistry, build_schema_registry
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


def test_response_validation_accepts_integer_enum_flag_composites() -> None:
    registry = build_schema_registry(
        [
            {
                "swagger": "2.0",
                "info": {"title": "Flag Controller", "version": "1.0.0"},
                "paths": {
                    "/roles": {
                        "get": {
                            "operationId": "Roles_GetRoles",
                            "responses": {
                                "200": {
                                    "schema": {
                                        "type": "object",
                                        "required": ["Visibility"],
                                        "properties": {
                                            "Visibility": {"$ref": "#/definitions/VisibilityTypes"}
                                        },
                                    }
                                }
                            },
                        }
                    }
                },
                "definitions": {
                    "VisibilityTypes": {
                        "enum": [0, 1, 4, 16, 64],
                        "type": "integer",
                        "x-enumFlags": True,
                    }
                },
            }
        ]
    )
    operation = registry.match_operation("GET", "/roles")
    assert operation is not None

    validator = ResponseSchemaValidator(registry)
    validator.validate(operation, status_code=200, payload={"Visibility": 127})

    with pytest.raises(SchemaValidationError):
        validator.validate(operation, status_code=200, payload={"Visibility": 128})


def test_response_validation_accepts_user_site_missing_known_live_optional_fields() -> None:
    registry = build_schema_registry(
        [
            {
                "swagger": "2.0",
                "info": {"title": "User Controller", "version": "1.0.0"},
                "paths": {
                    "/users": {
                        "get": {
                            "operationId": "User_GetUsersLegacy",
                            "responses": {
                                "200": {
                                    "schema": {"$ref": "#/definitions/ListGetResponseOfUser"}
                                }
                            },
                        }
                    }
                },
                "definitions": {
                    "ListGetResponseOfUser": {
                        "type": "object",
                        "required": ["Items"],
                        "properties": {
                            "Items": {
                                "type": "array",
                                "items": {"$ref": "#/definitions/User"},
                            }
                        },
                    },
                    "User": {
                        "type": "object",
                        "required": ["UserId", "Site"],
                        "properties": {
                            "UserId": {"type": "string"},
                            "Site": {"$ref": "#/definitions/Site"},
                        },
                    },
                    "Site": {
                        "type": "object",
                        "required": [
                            "SiteId",
                            "ProductId",
                            "DefaultWorkflowId",
                            "DefaultWorkflowInitialStepId",
                            "EnableAnalytics",
                            "EnableUsersnap",
                            "SystemUserId",
                        ],
                        "properties": {
                            "SiteId": {"type": "string"},
                            "ProductId": {"type": "string"},
                            "DefaultWorkflowId": {"type": "string"},
                            "DefaultWorkflowInitialStepId": {"type": "string"},
                            "EnableAnalytics": {"type": "boolean"},
                            "EnableUsersnap": {"type": "boolean"},
                            "SystemUserId": {"type": "string"},
                        },
                    },
                },
            }
        ]
    )
    operation = registry.match_operation("GET", "/users")
    assert operation is not None

    validator = ResponseSchemaValidator(registry)
    validator.validate(
        operation,
        status_code=200,
        payload={
            "Items": [
                {
                    "UserId": "user-1",
                    "Site": {
                        "SiteId": "site-1",
                        "ProductId": "product-1",
                        "SystemUserId": "system-user-1",
                    },
                }
            ]
        },
    )

    with pytest.raises(SchemaValidationError):
        validator.validate(
            operation,
            status_code=200,
            payload={
                "Items": [
                    {
                        "UserId": "user-1",
                        "Site": {
                            "SiteId": "site-1",
                            "ProductId": "product-1",
                        },
                    }
                ]
            },
        )


def test_response_validation_accepts_user_missing_training_percent_complete() -> None:
    registry = build_schema_registry(
        [
            {
                "swagger": "2.0",
                "info": {"title": "User Controller", "version": "1.0.0"},
                "paths": {
                    "/users": {
                        "get": {
                            "operationId": "User_GetUsersLegacy",
                            "responses": {
                                "200": {
                                    "schema": {"$ref": "#/definitions/ListGetResponseOfUser"}
                                }
                            },
                        }
                    }
                },
                "definitions": {
                    "ListGetResponseOfUser": {
                        "type": "object",
                        "required": ["Items"],
                        "properties": {
                            "Items": {
                                "type": "array",
                                "items": {"$ref": "#/definitions/User"},
                            }
                        },
                    },
                    "User": {
                        "type": "object",
                        "required": [
                            "UserId",
                            "IsDeleted",
                            "TrainingPercentComplete",
                            "Portal",
                        ],
                        "properties": {
                            "UserId": {"type": "string"},
                            "IsDeleted": {"type": "boolean"},
                            "TrainingPercentComplete": {"type": "integer"},
                            "Portal": {"type": "integer"},
                        },
                    },
                },
            }
        ]
    )
    operation = registry.match_operation("GET", "/users")
    assert operation is not None

    validator = ResponseSchemaValidator(registry)
    validator.validate(
        operation,
        status_code=200,
        payload={
            "Items": [
                {
                    "UserId": "user-1",
                    "IsDeleted": False,
                    "Portal": 2,
                }
            ]
        },
    )

    with pytest.raises(SchemaValidationError):
        validator.validate(
            operation,
            status_code=200,
            payload={
                "Items": [
                    {
                        "UserId": "user-1",
                        "IsDeleted": False,
                    }
                ]
            },
        )
