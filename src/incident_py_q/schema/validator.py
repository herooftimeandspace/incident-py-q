"""JSON-schema response validation against bundled Incident IQ contracts."""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from jsonschema import RefResolver, validators
from jsonschema import ValidationError as JSONSchemaValidationError

from incident_py_q.exceptions import SchemaValidationError

from .registry import OperationSpec, SchemaRegistry

_LIVE_OPTIONAL_TICKET_DETAIL_FIELDS = frozenset({"IsTraining", "SiteId", "TicketId"})
_LIVE_OPTIONAL_TICKET_CUSTOM_FIELD_VALUE_FIELDS = frozenset({"TicketId"})
_LIVE_OPTIONAL_TAG_FIELDS = frozenset({"ProductId", "SiteId"})


class ResponseSchemaValidator:
    """Validate HTTP payloads against operation response schemas."""

    def __init__(self, registry: SchemaRegistry) -> None:
        self._registry = registry
        self._validator_cls = validators.validator_for(registry.merged_document)
        self._resolver = RefResolver.from_schema(registry.merged_document)
        ticket_detail_document = _ticket_detail_response_document(registry.merged_document)
        self._ticket_detail_validator_cls = validators.validator_for(ticket_detail_document)
        self._ticket_detail_resolver = RefResolver.from_schema(ticket_detail_document)

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

        validator_cls = self._validator_cls
        resolver = self._resolver
        if _is_ticket_detail_response(operation):
            validator_cls = self._ticket_detail_validator_cls
            resolver = self._ticket_detail_resolver

        validator = validator_cls(response_schema, resolver=resolver)

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


def _is_ticket_detail_response(operation: OperationSpec) -> bool:
    """Return whether an operation validates a single ticket-detail response."""
    return (
        operation.method == "GET"
        and operation.path_template == "/tickets/{TicketId}"
        and operation.operation_id == "Ticket_GetTicket"
    )


def _ticket_detail_response_document(document: dict[str, Any]) -> dict[str, Any]:
    """Return a validation document relaxed only for ticket detail responses.

    Incident IQ live ``GET /tickets/{TicketId}`` payloads can omit a few fields
    from the top-level ticket detail item and its nested custom-field/tag rows.
    Those same shared definitions are also used by list, create, and update
    contracts, where relaxing them globally would weaken request and non-detail
    response validation. The copied document created here is therefore used only
    while validating the matched ticket-detail operation.
    """
    detail_document = deepcopy(document)
    definitions = detail_document.get("definitions")
    if not isinstance(definitions, dict):
        return detail_document

    _remove_required_fields(
        definitions,
        "Ticket",
        _LIVE_OPTIONAL_TICKET_DETAIL_FIELDS,
    )
    _remove_required_fields(
        definitions,
        "TicketCustomFieldValue",
        _LIVE_OPTIONAL_TICKET_CUSTOM_FIELD_VALUE_FIELDS,
    )
    _remove_required_fields(
        definitions,
        "Tag",
        _LIVE_OPTIONAL_TAG_FIELDS,
    )
    return detail_document


def _remove_required_fields(
    definitions: dict[str, Any],
    definition_name: str,
    optional_fields: frozenset[str],
) -> None:
    schema = definitions.get(definition_name)
    if not isinstance(schema, dict):
        return
    required = schema.get("required")
    if not isinstance(required, list):
        return
    schema["required"] = [field for field in required if field not in optional_fields]
