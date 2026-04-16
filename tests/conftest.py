"""Shared fixtures for unit and contract tests."""

from __future__ import annotations

from typing import Any

import pytest

from incident_py_q.config import ClientConfig
from incident_py_q.schema.registry import SchemaRegistry, build_schema_registry


@pytest.fixture()
def tiny_swagger_document() -> dict[str, Any]:
    """Small Swagger contract used for deterministic unit tests."""
    return {
        "swagger": "2.0",
        "info": {"title": "Tiny Controller", "version": "1.0.0"},
        "paths": {
            "/things": {
                "get": {
                    "operationId": "Things_GetThings",
                    "parameters": [
                        {"name": "page", "in": "query", "type": "integer"},
                        {"name": "pageSize", "in": "query", "type": "integer"},
                    ],
                    "responses": {"200": {"schema": {"$ref": "#/definitions/ThingList"}}},
                },
                "post": {
                    "operationId": "Things_CreateThing",
                    "parameters": [
                        {"name": "payload", "in": "body", "required": True, "schema": {"$ref": "#/definitions/Thing"}}
                    ],
                    "responses": {"201": {"schema": {"$ref": "#/definitions/Thing"}}},
                },
            },
            "/things/{ThingId}": {
                "get": {
                    "operationId": "Things_GetThing",
                    "parameters": [
                        {"name": "ThingId", "in": "path", "required": True, "type": "string"}
                    ],
                    "responses": {"200": {"schema": {"$ref": "#/definitions/Thing"}}},
                }
            },
            "/maybe": {
                "get": {
                    "operationId": "Things_GetMaybe",
                    "responses": {"2XX": {"schema": {"type": "object", "required": ["ok"], "properties": {"ok": {"type": "boolean"}}}}},
                }
            },
        },
        "definitions": {
            "Thing": {
                "type": "object",
                "required": ["id", "name"],
                "properties": {"id": {"type": "string"}, "name": {"type": "string"}},
            },
            "ThingList": {
                "type": "object",
                "required": ["Items"],
                "properties": {
                    "Items": {"type": "array", "items": {"$ref": "#/definitions/Thing"}},
                },
            },
        },
    }


@pytest.fixture()
def tiny_registry(tiny_swagger_document: dict[str, Any]) -> SchemaRegistry:
    """Registry built from the tiny Swagger fixture."""
    return build_schema_registry([tiny_swagger_document])


@pytest.fixture()
def tiny_config() -> ClientConfig:
    """Common client config used by request/SDK tests."""
    return ClientConfig(
        base_url="https://tenant.example/api/v1",
        api_token="token-123",
        site_id="site-42",
        client_header="ApiClient",
        auth_mode="bearer",
        timeout=10.0,
        validate_responses=True,
        max_retries=1,
        backoff_base=0.01,
    )
