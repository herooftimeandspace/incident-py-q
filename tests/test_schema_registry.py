"""Tests for operation registry construction and matching."""

from __future__ import annotations

from typing import Any

import pytest

from incident_py_q.schema.registry import build_schema_registry


def test_registry_builds_operations_and_matches_paths(tiny_swagger_document: dict[str, Any]) -> None:
    registry = build_schema_registry([tiny_swagger_document])

    assert len(registry.operations) == 4
    operation = registry.match_operation("GET", "/things/abc123")
    assert operation is not None
    assert operation.operation_id == "Things_GetThing"
    assert operation.namespace == "things"


def test_registry_detects_path_method_collisions(tiny_swagger_document: dict[str, Any]) -> None:
    other_document = {
        "swagger": "2.0",
        "info": {"title": "Other Controller", "version": "1.0.0"},
        "paths": {
            "/things": {
                "get": {
                    "operationId": "Other_GetThings",
                    "responses": {"200": {"schema": {"type": "object"}}},
                }
            }
        },
        "definitions": {},
    }

    with pytest.raises(ValueError):
        build_schema_registry([tiny_swagger_document, other_document])


def test_registry_detects_definition_collisions(tiny_swagger_document: dict[str, Any]) -> None:
    other_document = {
        "swagger": "2.0",
        "info": {"title": "Other Controller", "version": "1.0.0"},
        "paths": {},
        "definitions": {
            "Thing": {
                "type": "object",
                "required": ["id"],
                "properties": {"id": {"type": "integer"}},
            }
        },
    }

    with pytest.raises(ValueError):
        build_schema_registry([tiny_swagger_document, other_document])


def test_registry_inventory_match_miss_and_generated_operation_ids() -> None:
    registry = build_schema_registry(
        [
            {
                "swagger": "2.0",
                "info": {"title": "Root Controller", "version": "1.0.0"},
                "paths": {
                    "/": {
                        "parameters": [{"name": "ignored", "in": "cookie", "type": "string"}],
                        "get": {
                            "responses": {"200": {"schema": {"type": "object"}}},
                        },
                    }
                },
                "definitions": {},
            }
        ]
    )

    assert registry.match_operation("POST", "/") is None
    inventory = registry.inventory()
    assert inventory[0]["namespace"] == "root"
    assert inventory[0]["operation_id"].startswith("Root Controller_get_")
    assert inventory[0]["python_method"] == "get"
