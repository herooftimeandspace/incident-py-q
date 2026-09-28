"""Tests for Silver-only response-schema overrides."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, cast

import pytest

from incident_py_q.exceptions import SchemaValidationError
from incident_py_q.schema.loader import load_legacy_contract_document
from incident_py_q.schema.registry import SchemaRegistry
from incident_py_q.silver.validation import SilverResponseSchemaValidator


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
