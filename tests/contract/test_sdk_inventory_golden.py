"""Golden tests for semver-sensitive generated SDK public surface."""

from __future__ import annotations

import json
from pathlib import Path

from incident_py_q import Client
from incident_py_q.schema.loader import load_stoplight_documents
from incident_py_q.schema.registry import build_schema_registry


def test_sdk_inventory_matches_golden_snapshot() -> None:
    golden_path = Path("tests/contract/golden_sdk_inventory.json")
    expected_inventory = json.loads(golden_path.read_text(encoding="utf-8"))

    registry = build_schema_registry(load_stoplight_documents())
    client = Client(
        base_url="https://example.incidentiq.com/api/v1",
        api_token="placeholder-token",
        registry=registry,
    )
    actual_inventory = client.sdk_inventory()
    client.close()

    assert actual_inventory == expected_inventory
