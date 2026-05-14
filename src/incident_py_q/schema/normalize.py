"""Schema normalization for known Incident IQ/Swagger irregularities."""

from __future__ import annotations

from copy import deepcopy
from typing import Any


def normalize_swagger_document(document: dict[str, Any]) -> dict[str, Any]:
    """Return a normalized copy of a Swagger 2.0 document.

    Normalization is intentionally narrow:
    - Convert `x-nullable: true` schemas into JSON Schema nullable forms.
    - Relax known live-contract drift that is documented by regression tests.
    - Preserve all unknown extension fields to avoid contract drift.
    """
    normalized: dict[str, Any] = deepcopy(document)
    _walk_and_normalize(normalized)
    _normalize_ticket_status_workflow_id_drift(normalized)
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


def _normalize_ticket_status_workflow_id_drift(document: dict[str, Any]) -> None:
    """Treat `TicketStatus.WorkflowId` as optional for live ticket status payloads.

    Incident IQ's bundled Stoplight controller marks `WorkflowId` as required on
    `TicketStatus`, but live `GET /tickets/statuses` responses have been observed
    without that field while still carrying stable status identifiers, workflow
    step identifiers, and status metadata. The SDK keeps the upstream property in
    the schema so callers can read it when tenants provide it, but removes it from
    the required list in the normalized runtime contract so read-only status
    lookup does not fail solely because of this known upstream drift.
    """
    definitions = document.get("definitions")
    if not isinstance(definitions, dict):
        return
    ticket_status = definitions.get("TicketStatus")
    if not isinstance(ticket_status, dict):
        return
    required = ticket_status.get("required")
    if not isinstance(required, list):
        return
    ticket_status["required"] = [field for field in required if field != "WorkflowId"]
