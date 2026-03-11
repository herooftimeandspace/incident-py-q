#!/usr/bin/env python3
"""Regenerate the golden SDK inventory snapshot."""

from __future__ import annotations

import json
from pathlib import Path

from incident_py_q import Client


def main() -> int:
    destination = Path("tests/contract/golden_sdk_inventory.json")
    destination.parent.mkdir(parents=True, exist_ok=True)

    client = Client(
        base_url="https://example.incidentiq.com",
        api_token="placeholder-token",
        validate_responses=True,
    )
    inventory = client.sdk_inventory()
    destination.write_text(json.dumps(inventory, indent=2, sort_keys=True), encoding="utf-8")
    client.close()
    print(f"Wrote {len(inventory)} SDK inventory entries to {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

