#!/usr/bin/env python3
"""Regenerate the SDK inventory snapshots from the bundled Golden contract.

Run this after `scripts/sync_schemas.py` pulls a new Golden OpenAPI snapshot.
The Golden inventory is derived from the published contract; the Silver
inventory covers only the HAR-derived routes the contract still does not
document, because Golden always wins a route-level conflict.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    project_root = Path(__file__).resolve().parents[1]
    src_root = project_root / "src"
    if str(src_root) not in sys.path:
        sys.path.insert(0, str(src_root))

    from incident_py_q import Client
    from incident_py_q.silver import silver_inventory_records
    from incident_py_q.silver.runtime import build_silver_metadata, superseded_by_golden

    contract_dir = project_root / "tests/contract"
    contract_dir.mkdir(parents=True, exist_ok=True)

    client = Client(
        base_url="https://example.incidentiq.com",
        api_token="placeholder-token",
        validate_responses=True,
    )
    golden_inventory = client.sdk_inventory()

    silver_metadata = build_silver_metadata()
    superseded = set(superseded_by_golden(silver_metadata, client._registry))
    retained_metadata = tuple(
        method for method in silver_metadata if method not in superseded
    )
    client.close()

    silver_records = silver_inventory_records(retained_metadata)
    merged_records = [
        *({**entry, "provenance": "golden"} for entry in golden_inventory),
        *silver_records,
    ]

    targets = {
        contract_dir / "golden_sdk_inventory.json": golden_inventory,
        contract_dir / "silver_sdk_inventory.json": silver_records,
        contract_dir / "merged_sdk_inventory.json": merged_records,
    }
    for destination, payload in targets.items():
        destination.write_text(
            json.dumps(payload, indent=2, sort_keys=True),
            encoding="utf-8",
        )
        print(f"Wrote {len(payload)} entries to {destination.relative_to(project_root)}")

    if superseded:
        print(
            f"\n{len(superseded)} Silver route(s) are superseded by the Golden contract "
            "and were excluded. Run scripts/reconcile_silver_inventory.py to prune them "
            "from the bundled Silver inventory."
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
