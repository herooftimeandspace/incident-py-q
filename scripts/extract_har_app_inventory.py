#!/usr/bin/env python3
"""Extract app-path endpoint inventory from one or more HAR files."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import urlparse


@dataclass(slots=True)
class _EndpointAggregate:
    method: str
    path: str
    status_codes: set[int] = field(default_factory=set)
    sources: set[str] = field(default_factory=set)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("har_files", nargs="+", help="Input HAR files to scan.")
    parser.add_argument(
        "--output",
        default="tests/fixtures/har_app_inventory.json",
        help="Destination JSON file for normalized endpoint inventory.",
    )
    args = parser.parse_args()

    endpoint_map: dict[tuple[str, str], _EndpointAggregate] = {}
    for har_path in args.har_files:
        path = Path(har_path).resolve()
        payload = json.loads(path.read_text(encoding="utf-8"))
        entries = payload.get("log", {}).get("entries", [])
        if not isinstance(entries, list):
            continue

        for entry in entries:
            if not isinstance(entry, dict):
                continue
            request = entry.get("request", {})
            response = entry.get("response", {})
            if not isinstance(request, dict) or not isinstance(response, dict):
                continue

            method = request.get("method")
            url = request.get("url")
            if not isinstance(method, str) or not isinstance(url, str):
                continue

            parsed = urlparse(url)
            endpoint_path = parsed.path
            if "/apps/" not in endpoint_path and endpoint_path != "/api/v1.0/app-registry/apps/false":
                continue

            key = (method.upper(), endpoint_path)
            item = endpoint_map.setdefault(
                key,
                _EndpointAggregate(
                    method=method.upper(),
                    path=endpoint_path,
                ),
            )
            status_code = response.get("status")
            if isinstance(status_code, int):
                item.status_codes.add(status_code)
            item.sources.add(path.name)

    normalized = []
    for (_, _), value in sorted(endpoint_map.items(), key=lambda kv: (kv[0][1], kv[0][0])):
        normalized.append(
            {
                "method": value.method,
                "path": value.path,
                "status_codes": sorted(value.status_codes),
                "sources": sorted(value.sources),
            }
        )

    output_path = Path(args.output).resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(normalized, indent=2, sort_keys=True), encoding="utf-8")
    print(f"Wrote {len(normalized)} app-path endpoints to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
