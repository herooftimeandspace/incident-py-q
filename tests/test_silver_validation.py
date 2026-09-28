"""Tests for Silver-only response-schema overrides."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, cast
from unittest import mock

import pytest

from incident_py_q.exceptions import SchemaValidationError
from incident_py_q.schema.loader import load_legacy_contract_document
from incident_py_q.schema.registry import SchemaRegistry
from incident_py_q.silver.validation import (
    SilverResponseSchemaValidator,
    _build_overrides,
    _pick_response_schema,
)


def _load_asset_serial_payload() -> dict[str, Any]:
    fixture_path = Path(__file__).parent / "fixtures" / "asset_serial_live_response.json"
    return cast(dict[str, Any], json.loads(fixture_path.read_text(encoding="utf-8")))


def _part_payload(*, include_site_id: bool = True) -> dict[str, Any]:
    identifier = "11111111-1111-1111-1111-111111111111"
    part: dict[str, Any] = {
        "PartId": identifier,
        "ProductId": identifier,
        "CreatedDate": "2026-09-28T00:00:00Z",
        "ModifiedDate": "2026-09-28T00:00:00Z",
        "StandardCostEach": 12.5,
        "StandardSupplierId": identifier,
        "Name": "Screen",
    }
    if include_site_id:
        part["SiteId"] = identifier
    return {
        "UserToken": identifier,
        "RequestDate": "2026-09-28T00:00:00Z",
        "ExecutionTime": 0.01,
        "StatusCode": 200,
        "ProcessId": 1,
        "Item": part,
    }


def test_overrides_cover_every_migrated_legacy_route(bundled_registry: SchemaRegistry) -> None:
    """Routes migrated off Golden keep strict validation from the legacy contract."""
    validator = SilverResponseSchemaValidator(bundled_registry)
    legacy_document = load_legacy_contract_document()

    expected = {
        (method.upper(), route)
        for route, path_item in legacy_document["paths"].items()
        for method in path_item
        if method.lower() in {"get", "post", "put", "delete", "patch"}
    }

    assert expected
    assert set(validator._overrides) == expected


def test_migrated_route_accepts_contract_shaped_payload(
    bundled_registry: SchemaRegistry,
) -> None:
    validator = SilverResponseSchemaValidator(bundled_registry)

    handled = validator.validate_if_override(
        method="GET",
        route="/api/v1.0/parts/{part_id}",
        status_code=200,
        payload=_part_payload(),
    )

    assert handled is True


def test_migrated_route_still_rejects_missing_required_fields(
    bundled_registry: SchemaRegistry,
) -> None:
    validator = SilverResponseSchemaValidator(bundled_registry)

    with pytest.raises(SchemaValidationError, match="SiteId"):
        validator.validate_if_override(
            method="GET",
            route="/api/v1.0/parts/{part_id}",
            status_code=200,
            payload=_part_payload(include_site_id=False),
        )


def test_validator_declines_routes_without_an_override(
    bundled_registry: SchemaRegistry,
) -> None:
    """Golden-documented routes are validated by Golden, not by a Silver override."""
    validator = SilverResponseSchemaValidator(bundled_registry)

    handled = validator.validate_if_override(
        method="GET",
        route="/assets/serial/{serial}",
        status_code=200,
        payload=_load_asset_serial_payload(),
    )

    assert handled is False


def test_override_lookup_is_route_scoped(bundled_registry: SchemaRegistry) -> None:
    validator = SilverResponseSchemaValidator(bundled_registry)

    handled = validator.validate_if_override(
        method="GET",
        route="/assets/not-the-serial-route/{serial}",
        status_code=200,
        payload={"ok": True},
    )

    assert handled is False


def test_status_code_falls_back_to_class_then_default(
    bundled_registry: SchemaRegistry,
) -> None:
    """Response lookup prefers the exact status, then `2xx`, then `default`."""
    validator = SilverResponseSchemaValidator(bundled_registry)
    schemas = {
        "200": {"type": "object"},
        "2xx": {"type": "array"},
        "default": {"type": "string"},
    }

    assert _pick_response_schema(response_schemas=schemas, status_code=200) == {"type": "object"}
    assert _pick_response_schema(response_schemas=schemas, status_code=201) == {"type": "array"}
    assert _pick_response_schema(response_schemas=schemas, status_code=404) == {"type": "string"}
    assert _pick_response_schema(response_schemas={}, status_code=200) is None
    assert validator is not None


def test_override_without_a_matching_schema_is_treated_as_handled(
    bundled_registry: SchemaRegistry,
) -> None:
    """A migrated route with no schema for the status still counts as Silver-validated.

    Otherwise the caller would fall through to Golden validation for a route the
    Golden contract deliberately does not document.
    """
    validator = SilverResponseSchemaValidator(bundled_registry)

    handled = validator.validate_if_override(
        method="GET",
        route="/api/v1.0/parts/{part_id}",
        status_code=599,
        payload={"anything": True},
    )

    assert handled is True


def test_overrides_ignore_malformed_contract_entries() -> None:
    """Non-operation keys and malformed path items never become overrides."""
    document = {
        "swagger": "2.0",
        "definitions": {},
        "paths": {
            "/api/v1.0/ok": {
                "get": {"operationId": "ok", "responses": {"200": {"description": "no schema"}}},
                "parameters": [{"name": "x", "in": "query"}],
                "x-extension": {"ignored": True},
            },
            "/api/v1.0/bad": "not-a-path-item",
        },
    }

    with mock.patch(
        "incident_py_q.silver.validation.load_legacy_contract_document",
        return_value=document,
    ):
        overrides = _build_overrides(cast(SchemaRegistry, None))

    assert set(overrides) == {("GET", "/api/v1.0/ok")}
    assert overrides[("GET", "/api/v1.0/ok")].response_schemas == {}


def test_overrides_are_empty_when_the_contract_has_no_paths() -> None:
    with mock.patch(
        "incident_py_q.silver.validation.load_legacy_contract_document",
        return_value={"swagger": "2.0", "definitions": {}},
    ):
        assert _build_overrides(cast(SchemaRegistry, None)) == {}


def test_override_operation_id_falls_back_to_method_and_route() -> None:
    document = {
        "swagger": "2.0",
        "definitions": {},
        "paths": {"/api/v1.0/anon": {"post": {"responses": {}}}},
    }

    with mock.patch(
        "incident_py_q.silver.validation.load_legacy_contract_document",
        return_value=document,
    ):
        overrides = _build_overrides(cast(SchemaRegistry, None))

    assert overrides[("POST", "/api/v1.0/anon")].operation_id == "POST /api/v1.0/anon"
