#!/usr/bin/env python3
"""Drop bundled Silver routes that the Golden contract now documents.

Silver is the HAR-derived view of routes the published contract omits. When a
Golden sync starts documenting a route Silver had inferred, the documented
contract wins and the Silver entry is removed from the bundled inventory.

This runs without HAR files, so it can be used after any Golden sync;
`scripts/update_silver_inventory.py` is still the tool for re-deriving Silver
from fresh HAR captures.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def main() -> int:
    project_root = Path(__file__).resolve().parents[1]
    src_root = project_root / "src"
    if str(src_root) not in sys.path:
        sys.path.insert(0, str(src_root))

    from incident_py_q.schema.loader import load_contract_documents
    from incident_py_q.schema.registry import build_schema_registry
    from incident_py_q.silver.inventory import _matches_golden_contract

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--inventory",
        default="src/incident_py_q/data/silver_inventory.json",
        help="Path to the bundled Silver inventory JSON.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report superseded routes without rewriting the inventory.",
    )
    args = parser.parse_args()

    inventory_path = Path(args.inventory).resolve()
    payload: dict[str, Any] = json.loads(inventory_path.read_text(encoding="utf-8"))
    endpoints = payload.get("endpoints")
    if not isinstance(endpoints, list):
        raise SystemExit(f"{inventory_path} must contain an 'endpoints' list.")

    registry = build_schema_registry(load_contract_documents())

    kept: list[Any] = []
    superseded: list[tuple[str, str]] = []
    for endpoint in endpoints:
        if not isinstance(endpoint, dict):
            kept.append(endpoint)
            continue
        http_method = str(endpoint.get("http_method", ""))
        route = str(endpoint.get("route", endpoint.get("path", "")))
        if http_method and route and _matches_golden_contract(registry, http_method, route):
            superseded.append((http_method, route))
            continue
        kept.append(endpoint)

    for http_method, route in sorted(superseded):
        print(f"superseded by Golden: {http_method} {route}")

    print(
        f"\n{len(superseded)} superseded, {len(kept)} Silver routes remain "
        f"({len(endpoints)} before reconciliation)."
    )

    if args.dry_run:
        print("Dry run: inventory not modified.")
        return 0

    if superseded:
        payload["endpoints"] = kept
        inventory_path.write_text(
            json.dumps(payload, indent=2, sort_keys=True),
            encoding="utf-8",
        )
        print(f"Rewrote {inventory_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
