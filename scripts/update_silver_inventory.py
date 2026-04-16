#!/usr/bin/env python3
"""Regenerate HAR-derived Silver inventory artifacts."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def main() -> int:
    project_root = Path(__file__).resolve().parents[1]
    src_root = project_root / "src"
    if str(src_root) not in sys.path:
        sys.path.insert(0, str(src_root))

    from incident_py_q import Client
    from incident_py_q.schema.loader import load_stoplight_documents
    from incident_py_q.schema.registry import build_schema_registry
    from incident_py_q.silver import (
        extract_silver_inventory,
        legacy_app_inventory_records,
        silver_inventory_payload,
        silver_inventory_records,
    )

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("har_files", nargs="+", help="HAR files to scan for undocumented routes.")
    args = parser.parse_args()

    registry = build_schema_registry(load_stoplight_documents())
    silver_metadata = extract_silver_inventory(har_files=args.har_files, registry=registry)

    package_destination = project_root / "src/incident_py_q/data/silver_inventory.json"
    silver_destination = project_root / "tests/contract/silver_sdk_inventory.json"
    merged_destination = project_root / "tests/contract/merged_sdk_inventory.json"
    legacy_app_destination = project_root / "tests/fixtures/har_app_inventory.json"

    client = Client(
        base_url="https://example.incidentiq.com",
        api_token="placeholder-token",
        validate_responses=True,
        registry=registry,
    )
    golden_inventory = [
        {**entry, "provenance": "golden"}
        for entry in client.sdk_inventory()
    ]
    client.close()

    package_destination.write_text(
        json.dumps(silver_inventory_payload(silver_metadata), indent=2, sort_keys=True),
        encoding="utf-8",
    )
    silver_destination.write_text(
        json.dumps(silver_inventory_records(silver_metadata), indent=2, sort_keys=True),
        encoding="utf-8",
    )
    merged_destination.write_text(
        json.dumps([*golden_inventory, *silver_inventory_records(silver_metadata)], indent=2, sort_keys=True),
        encoding="utf-8",
    )
    legacy_app_destination.write_text(
        json.dumps(legacy_app_inventory_records(silver_metadata), indent=2, sort_keys=True),
        encoding="utf-8",
    )
    print(
        "Wrote Silver inventory artifacts to "
        f"{package_destination}, {silver_destination}, {merged_destination}, and {legacy_app_destination}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
