"""Tests for Swagger normalization helpers."""

from __future__ import annotations

from typing import Any, cast

from incident_py_q.schema.normalize import normalize_swagger_document


def test_normalize_swagger_document_converts_nullable_string_fields() -> None:
    source: dict[str, Any] = {
        "definitions": {
            "Thing": {
                "type": "object",
                "properties": {"name": {"type": "string", "x-nullable": True}},
            }
        }
    }

    normalized = normalize_swagger_document(source)

    assert source["definitions"]["Thing"]["properties"]["name"]["type"] == "string"
    assert normalized["definitions"]["Thing"]["properties"]["name"]["type"] == ["string", "null"]


def test_normalize_swagger_document_rewrites_nullable_refs_and_preserves_description() -> None:
    source: dict[str, Any] = {
        "paths": {
            "/things": {
                "get": {
                    "responses": {
                        "200": {
                            "schema": {
                                "$ref": "#/definitions/Thing",
                                "x-nullable": True,
                                "description": "nullable thing",
                            }
                        }
                    }
                }
            }
        }
    }

    normalized = normalize_swagger_document(source)

    schema = cast(
        dict[str, Any],
        normalized["paths"]["/things"]["get"]["responses"]["200"]["schema"],
    )
    assert schema["anyOf"] == [{"$ref": "#/definitions/Thing"}, {"type": "null"}]
    assert schema["description"] == "nullable thing"


def test_normalize_swagger_document_leaves_non_nullable_values_unchanged() -> None:
    source: dict[str, Any] = {
        "definitions": {"Thing": {"type": "object", "properties": {"count": {"type": "integer"}}}}
    }

    normalized = normalize_swagger_document(source)

    assert normalized == source


def test_normalize_swagger_document_relaxes_live_ticket_status_workflow_id_drift() -> None:
    source: dict[str, Any] = {
        "definitions": {
            "TicketStatus": {
                "type": "object",
                "required": [
                    "TicketStatusTypeId",
                    "WorkflowId",
                    "WorkflowStepId",
                    "IsClosed",
                ],
                "properties": {
                    "TicketStatusTypeId": {"type": "string"},
                    "WorkflowId": {"type": "string"},
                    "WorkflowStepId": {"type": "string"},
                    "IsClosed": {"type": "boolean"},
                },
            }
        }
    }

    normalized = normalize_swagger_document(source)

    assert source["definitions"]["TicketStatus"]["required"] == [
        "TicketStatusTypeId",
        "WorkflowId",
        "WorkflowStepId",
        "IsClosed",
    ]
    assert normalized["definitions"]["TicketStatus"]["required"] == [
        "TicketStatusTypeId",
        "WorkflowStepId",
        "IsClosed",
    ]
