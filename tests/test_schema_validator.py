"""Tests for runtime JSON-schema response validation behavior."""

from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path
from typing import Any, cast

import pytest

from incident_py_q.exceptions import SchemaValidationError
from incident_py_q.schema.registry import OperationSpec, SchemaRegistry, build_schema_registry
from incident_py_q.schema.validator import ResponseSchemaValidator


def _load_ticket_detail_live_shape_fixtures() -> list[dict[str, Any]]:
    """Load sanitized ticket detail payloads shaped like observed live drift."""
    fixture_path = Path(__file__).parent / "fixtures" / "ticket_detail_live_shape_drift.json"
    return cast(list[dict[str, Any]], json.loads(fixture_path.read_text(encoding="utf-8")))


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


def test_response_validation_accepts_user_portal_zero_sentinel() -> None:
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
                        "required": ["UserId", "Portal"],
                        "properties": {
                            "UserId": {"type": "string"},
                            "Portal": {"$ref": "#/definitions/Portals"},
                        },
                    },
                    "Portals": {
                        "enum": [1, 2, 3],
                        "type": "integer",
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
        payload={"Items": [{"UserId": "user-1", "Portal": 0}]},
    )

    with pytest.raises(SchemaValidationError):
        validator.validate(
            operation,
            status_code=200,
            payload={"Items": [{"UserId": "user-1", "Portal": 4}]},
        )


def test_response_validation_accepts_user_custom_field_value_missing_user_id() -> None:
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
                        "required": ["UserId", "CustomFieldValues"],
                        "properties": {
                            "UserId": {"type": "string"},
                            "CustomFieldValues": {
                                "type": "array",
                                "items": {"$ref": "#/definitions/UserCustomFieldValue"},
                            },
                        },
                    },
                    "UserCustomFieldValue": {
                        "type": "object",
                        "required": ["CustomFieldTypeId", "UserId"],
                        "properties": {
                            "CustomFieldTypeId": {"type": "string"},
                            "UserId": {"type": "string"},
                            "Value": {"type": "string"},
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
                    "CustomFieldValues": [
                        {
                            "CustomFieldTypeId": "field-1",
                            "Value": "[]",
                        }
                    ],
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
                        "CustomFieldValues": [{"Value": "[]"}],
                    }
                ]
            },
        )


@pytest.mark.parametrize(
    "fixture",
    _load_ticket_detail_live_shape_fixtures(),
    ids=lambda fixture: str(fixture["name"]),
)
def test_response_validation_accepts_ticket_detail_missing_known_live_optional_fields(
    bundled_registry: SchemaRegistry,
    fixture: dict[str, Any],
) -> None:
    operation = bundled_registry.match_operation(
        "GET",
        "/tickets/11111111-1111-1111-1111-111111111111",
    )
    assert operation is not None

    validator = ResponseSchemaValidator(bundled_registry)
    validator.validate(
        operation,
        status_code=200,
        payload=fixture["payload"],
    )


def test_response_validation_still_rejects_ticket_detail_missing_core_status_fields(
    bundled_registry: SchemaRegistry,
) -> None:
    operation = bundled_registry.match_operation(
        "GET",
        "/tickets/11111111-1111-1111-1111-111111111111",
    )
    assert operation is not None
    fixture = _load_ticket_detail_live_shape_fixtures()[0]
    payload = deepcopy(fixture["payload"])
    del payload["Item"]["ProductId"]

    validator = ResponseSchemaValidator(bundled_registry)
    with pytest.raises(SchemaValidationError):
        validator.validate(operation, status_code=200, payload=payload)
