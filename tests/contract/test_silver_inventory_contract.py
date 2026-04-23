"""Contract tests for checked-in Silver and merged SDK inventories."""

from __future__ import annotations

import json
from pathlib import Path


def _normalize_path(path: str) -> str:
    if path.startswith("/api/v1.0"):
        return path[len("/api/v1.0") :] or "/"
    return path


def test_silver_inventory_has_required_route_and_no_golden_overlap() -> None:
    silver_inventory = json.loads(
        Path("tests/contract/silver_sdk_inventory.json").read_text(encoding="utf-8")
    )
    golden_inventory = json.loads(
        Path("tests/contract/golden_sdk_inventory.json").read_text(encoding="utf-8")
    )

    silver_pairs = {
        (entry["http_method"], _normalize_path(entry["path"])) for entry in silver_inventory
    }
    golden_pairs = {(entry["method"], entry["path"]) for entry in golden_inventory}

    assert ("GET", "/assets/serial/{serial}") in silver_pairs
    assert ("POST", "/profiles/{user_id}/picture") in silver_pairs
    assert ("POST", "/profiles/my/picture") not in silver_pairs
    assert silver_pairs.isdisjoint(golden_pairs)


def test_merged_inventory_contains_golden_and_silver_surfaces() -> None:
    merged_inventory = json.loads(
        Path("tests/contract/merged_sdk_inventory.json").read_text(encoding="utf-8")
    )
    provenances = {
        entry.get("provenance", "golden")
        for entry in merged_inventory
    }

    assert "golden" in provenances
    assert "silver" in provenances
