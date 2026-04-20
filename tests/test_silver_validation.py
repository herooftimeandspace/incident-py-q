"""Tests for Silver-only validation overrides."""

from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path
from typing import Any

import pytest

from incident_py_q.exceptions import SchemaValidationError
from incident_py_q.schema.registry import SchemaRegistry
from incident_py_q.silver.validation import SilverResponseSchemaValidator


def _load_asset_serial_payload() -> dict[str, Any]:
    fixture_path = Path(__file__).parent / "fixtures" / "asset_serial_live_response.json"
    return json.loads(fixture_path.read_text(encoding="utf-8"))


def test_asset_serial_override_accepts_live_payload(bundled_registry: SchemaRegistry) -> None:
    validator = SilverResponseSchemaValidator(bundled_registry)

    handled = validator.validate_if_override(
        method="GET",
        route="/assets/serial/{serial}",
        status_code=200,
        payload=_load_asset_serial_payload(),
    )

    assert handled is True


def test_asset_serial_override_does_not_relax_unrelated_required_fields(
    bundled_registry: SchemaRegistry,
) -> None:
    payload: dict[str, Any] = deepcopy(_load_asset_serial_payload())
    payload["Items"][0].pop("AssetId")

    validator = SilverResponseSchemaValidator(bundled_registry)

    with pytest.raises(SchemaValidationError, match="AssetId"):
        validator.validate_if_override(
            method="GET",
            route="/assets/serial/{serial}",
            status_code=200,
            payload=payload,
        )


def test_asset_serial_override_is_route_scoped(bundled_registry: SchemaRegistry) -> None:
    validator = SilverResponseSchemaValidator(bundled_registry)

    handled = validator.validate_if_override(
        method="GET",
        route="/assets/not-the-serial-route/{serial}",
        status_code=200,
        payload={"ok": True},
    )

    assert handled is False
