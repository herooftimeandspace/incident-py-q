#!/usr/bin/env python3
"""Write the legacy app-path HAR inventory subset from the broader Silver extractor."""

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

    from incident_py_q.schema.loader import load_stoplight_documents
    from incident_py_q.schema.registry import build_schema_registry
    from incident_py_q.silver import extract_silver_inventory, legacy_app_inventory_records

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("har_files", nargs="+", help="Input HAR files to scan.")
    parser.add_argument(
        "--output",
        default="tests/fixtures/har_app_inventory.json",
        help="Destination JSON file for the legacy app-path inventory.",
    )
    args = parser.parse_args()

    registry = build_schema_registry(load_stoplight_documents())
    silver_metadata = extract_silver_inventory(har_files=args.har_files, registry=registry)
    legacy_inventory = legacy_app_inventory_records(silver_metadata)

    output_path = Path(args.output).resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(legacy_inventory, indent=2, sort_keys=True), encoding="utf-8")
    print(f"Wrote {len(legacy_inventory)} app-path endpoints to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
