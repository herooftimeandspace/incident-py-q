"""Schema normalization for known Incident IQ/Swagger irregularities."""

from __future__ import annotations

from copy import deepcopy
from typing import Any

_LIVE_OPTIONAL_SITE_FIELDS = {
    "DefaultWorkflowId",
    "DefaultWorkflowInitialStepId",
    "EnableAnalytics",
    "EnableUsersnap",
}

_LIVE_OPTIONAL_USER_FIELDS = {
    "TrainingPercentComplete",
}

_LIVE_OPTIONAL_USER_CUSTOM_FIELD_VALUE_FIELDS = {
    "UserId",
}

_LIVE_OPTIONAL_TICKET_STATUS_FIELDS = {
    "DisplayOrder",
    "WorkflowId",
    "WorkflowStepId",
}

_LIVE_OPTIONAL_TICKET_DETAIL_FIELDS = {
    "IsTraining",
    "SiteId",
    "TicketId",
}

_LIVE_OPTIONAL_TICKET_CUSTOM_FIELD_VALUE_FIELDS = {
    "TicketId",
}

_LIVE_OPTIONAL_TAG_FIELDS = {
    "ProductId",
    "SiteId",
}

_LIVE_PORTALS_ENUM_VALUES = {
    0,
}


def normalize_swagger_document(document: dict[str, Any]) -> dict[str, Any]:
    """Return a normalized copy of a Swagger 2.0 document.

    Normalization is intentionally narrow:
    - Convert `x-nullable: true` schemas into JSON Schema nullable forms.
    - Relax known live-contract drift that is documented by regression tests.
    - Preserve all unknown extension fields to avoid contract drift.
    """
    normalized: dict[str, Any] = deepcopy(document)
    _walk_and_normalize(normalized)
    _normalize_ticket_status_required_field_drift(normalized)
    _normalize_ticket_detail_required_field_drift(normalized)
    _normalize_ticket_custom_field_value_required_field_drift(normalized)
    _normalize_tag_required_field_drift(normalized)
    _normalize_site_required_field_drift(normalized)
    _normalize_user_required_field_drift(normalized)
    _normalize_user_custom_field_value_required_field_drift(normalized)
    _normalize_portals_enum_drift(normalized)
    return normalized


def _walk_and_normalize(node: Any) -> Any:
    if isinstance(node, dict):
        _normalize_nullable(node)
        _normalize_integer_enum_flags(node)
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


def _normalize_integer_enum_flags(schema: dict[str, Any]) -> None:
    """Relax OpenAPI enum constraints for integer bitmask extension schemas.

    Swagger/OpenAPI's standard `enum` keyword describes a closed list of exact
    values. Incident IQ also emits `x-enumFlags: true` for some integer enums,
    which means the listed values are named bit flags rather than the full set of
    accepted values. Runtime response validation must therefore accept composite
    bitmasks such as `127` for a schema whose largest documented flag is `64`.

    The normalized contract keeps the schema integer-shaped, preserves extension
    metadata such as `x-enumNames`, removes the exact-value enum, and bounds the
    value to the non-negative mask range covered by the highest documented flag.
    This keeps ordinary integer validation useful without rejecting unnamed or
    composite flag combinations that are valid live API behavior.
    """
    if schema.get("x-enumFlags") is not True:
        return
    if schema.get("type") != "integer":
        return

    enum_values = schema.get("enum")
    if not isinstance(enum_values, list):
        return

    integer_values = [value for value in enum_values if type(value) is int]
    if len(integer_values) != len(enum_values) or not integer_values:
        return

    highest_flag = max(integer_values)
    if highest_flag < 0:
        return

    schema.pop("enum", None)
    schema.setdefault("minimum", 0)
    schema.setdefault("maximum", _highest_bitmask_value(highest_flag))


def _highest_bitmask_value(highest_flag: int) -> int:
    """Return the largest bitmask value covered by a documented flag value."""
    if highest_flag == 0:
        return 0
    return (1 << highest_flag.bit_length()) - 1


def _normalize_ticket_status_required_field_drift(document: dict[str, Any]) -> None:
    """Treat known live-optional `TicketStatus` workflow fields as optional.

    Incident IQ's bundled Stoplight controller marks `DisplayOrder`,
    `WorkflowId`, and `WorkflowStepId` as required on `TicketStatus`, but live
    `GET /tickets/statuses` responses can omit ordering and workflow metadata
    while still carrying the stable ticket status type identifier and
    human-readable status metadata used by callers. The SDK keeps those upstream
    properties in the schema so callers can read them when tenants provide them,
    but removes only those fields from the normalized required list so read-only
    status lookup does not fail solely because of this known upstream drift.
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
    ticket_status["required"] = [
        field for field in required if field not in _LIVE_OPTIONAL_TICKET_STATUS_FIELDS
    ]


def _normalize_ticket_detail_required_field_drift(document: dict[str, Any]) -> None:
    """Treat known live-optional `Ticket` detail fields as optional.

    Incident IQ's bundled Stoplight controller marks `TicketId`, `SiteId`, and
    `IsTraining` as required on the `Ticket` response model. Live
    `GET /tickets/{TicketId}` detail responses can omit any one of those fields
    while still returning the response wrapper, ticket number, status flags,
    timestamps, ownership identifiers, and workflow metadata needed for
    read-only detail hydration. The path parameter continues to carry the ticket
    identity for callers that requested a specific ticket.

    The fields remain available in the schema for tenants that return them. Only
    the normalized required list is relaxed, and only for the `Ticket` response
    definition. Request models such as `UpdateTicketRequest` keep their upstream
    requirements unchanged.
    """
    definitions = document.get("definitions")
    if not isinstance(definitions, dict):
        return
    ticket = definitions.get("Ticket")
    if not isinstance(ticket, dict):
        return
    required = ticket.get("required")
    if not isinstance(required, list):
        return
    ticket["required"] = [
        field for field in required if field not in _LIVE_OPTIONAL_TICKET_DETAIL_FIELDS
    ]


def _normalize_ticket_custom_field_value_required_field_drift(
    document: dict[str, Any],
) -> None:
    """Treat parent ticket IDs as optional on nested ticket custom field values.

    Live `GET /tickets/{TicketId}` detail responses can embed
    `TicketCustomFieldValue` records without repeating the parent `TicketId`.
    The custom field type and value metadata still describe the field value, and
    the containing ticket detail response already identifies the requested ticket
    through the route and response wrapper. This mirrors the existing
    `UserCustomFieldValue` relaxation for nested user list payloads.
    """
    definitions = document.get("definitions")
    if not isinstance(definitions, dict):
        return
    ticket_custom_field_value = definitions.get("TicketCustomFieldValue")
    if not isinstance(ticket_custom_field_value, dict):
        return
    required = ticket_custom_field_value.get("required")
    if not isinstance(required, list):
        return
    ticket_custom_field_value["required"] = [
        field
        for field in required
        if field not in _LIVE_OPTIONAL_TICKET_CUSTOM_FIELD_VALUE_FIELDS
    ]


def _normalize_tag_required_field_drift(document: dict[str, Any]) -> None:
    """Treat site/product identifiers as optional on compact nested tags.

    Live ticket detail responses can include compact `Tag` entries that identify
    the tag itself but omit tenant-scoped `SiteId` and `ProductId` values. The
    SDK keeps those properties available when returned, but does not reject a
    read-only ticket detail solely because nested tags use the compact shape.
    """
    definitions = document.get("definitions")
    if not isinstance(definitions, dict):
        return
    tag = definitions.get("Tag")
    if not isinstance(tag, dict):
        return
    required = tag.get("required")
    if not isinstance(required, list):
        return
    tag["required"] = [
        field for field in required if field not in _LIVE_OPTIONAL_TAG_FIELDS
    ]


def _normalize_site_required_field_drift(document: dict[str, Any]) -> None:
    """Treat known live-optional `Site` fields as optional in runtime contracts.

    Incident IQ's published Stoplight controllers mark several `Site` fields as
    required even though live responses can omit them in nested payloads. This is
    currently visible in `GET /users`, where user list items can include a
    compact `Site` object without default workflow or analytics flags. Silver's
    asset serial validation already accepts the same drift for `Site`; Golden
    response validation needs the same narrow relaxation so documented read-only
    routes do not fail solely because a nested site is compact.

    The properties remain in the schema for tenants that return them. Only the
    `required` list is relaxed, and only for the four fields observed or already
    captured by Silver's production-shape override.
    """
    definitions = document.get("definitions")
    if not isinstance(definitions, dict):
        return
    site = definitions.get("Site")
    if not isinstance(site, dict):
        return
    required = site.get("required")
    if not isinstance(required, list):
        return
    site["required"] = [
        field for field in required if field not in _LIVE_OPTIONAL_SITE_FIELDS
    ]


def _normalize_user_required_field_drift(document: dict[str, Any]) -> None:
    """Treat known live-optional `User` fields as optional in runtime contracts.

    Incident IQ's published Stoplight controller marks `TrainingPercentComplete`
    as required on `User`, but live `GET /users` list responses can omit it while
    still carrying the stable identifiers, timestamps, role, status, and portal
    fields needed by callers. The SDK keeps the property in the schema for
    tenants that return it, but removes it from the normalized required list so
    read-only user list calls do not fail solely because this progress metadata
    is absent.
    """
    definitions = document.get("definitions")
    if not isinstance(definitions, dict):
        return
    user = definitions.get("User")
    if not isinstance(user, dict):
        return
    required = user.get("required")
    if not isinstance(required, list):
        return
    user["required"] = [
        field for field in required if field not in _LIVE_OPTIONAL_USER_FIELDS
    ]


def _normalize_user_custom_field_value_required_field_drift(
    document: dict[str, Any],
) -> None:
    """Treat known live-optional `UserCustomFieldValue` fields as optional.

    Incident IQ's published schema marks `UserId` as required on
    `UserCustomFieldValue`, but live `GET /users` list responses can embed custom
    field values without repeating the parent user identifier. The field remains
    available in the schema for routes that return it; normalization only relaxes
    the required list so nested custom field values can validate when they still
    carry their custom field type and value metadata.
    """
    definitions = document.get("definitions")
    if not isinstance(definitions, dict):
        return
    user_custom_field_value = definitions.get("UserCustomFieldValue")
    if not isinstance(user_custom_field_value, dict):
        return
    required = user_custom_field_value.get("required")
    if not isinstance(required, list):
        return
    user_custom_field_value["required"] = [
        field
        for field in required
        if field not in _LIVE_OPTIONAL_USER_CUSTOM_FIELD_VALUE_FIELDS
    ]


def _normalize_portals_enum_drift(document: dict[str, Any]) -> None:
    """Allow the live `Portals` sentinel value returned by user list payloads.

    The published `Portals` enum documents the named portal values `1`, `2`, and
    `3`, but live `GET /users` list responses can use `0` as an unset or unknown
    sentinel. The SDK preserves the named enum values and appends only this
    observed sentinel so ordinary enum validation still rejects unrelated values.
    """
    definitions = document.get("definitions")
    if not isinstance(definitions, dict):
        return
    portals = definitions.get("Portals")
    if not isinstance(portals, dict):
        return
    enum_values = portals.get("enum")
    if not isinstance(enum_values, list):
        return
    for value in sorted(_LIVE_PORTALS_ENUM_VALUES):
        if value not in enum_values:
            enum_values.insert(0, value)
