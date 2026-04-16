#!/usr/bin/env python3
"""Build Shields endpoint JSON payloads for CI badges."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Final
from xml.etree import ElementTree

_STATUS_MESSAGES: Final[dict[str, str]] = {
    "success": "passing",
    "failure": "failing",
    "cancelled": "cancelled",
    "skipped": "skipped",
    "neutral": "neutral",
    "timed_out": "timed out",
    "action_required": "action required",
    "startup_failure": "startup failure",
    "stale": "stale",
}
_STATUS_COLORS: Final[dict[str, str]] = {
    "success": "brightgreen",
    "failure": "red",
    "cancelled": "orange",
    "skipped": "lightgrey",
    "neutral": "blue",
    "timed_out": "orange",
    "action_required": "orange",
    "startup_failure": "orange",
    "stale": "yellow",
}


def _write_payload(*, output: Path, label: str, message: str, color: str) -> None:
    payload = {
        "schemaVersion": 1,
        "label": label,
        "message": message,
        "color": color,
    }
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _build_coverage_badge(*, coverage_file: Path, label: str, output: Path) -> None:
    root = ElementTree.parse(coverage_file).getroot()
    line_rate = float(root.attrib.get("line-rate", "0"))
    percent = round(line_rate * 100, 2)

    if percent >= 90:
        color = "brightgreen"
    elif percent >= 80:
        color = "green"
    elif percent >= 70:
        color = "yellowgreen"
    elif percent >= 60:
        color = "yellow"
    elif percent >= 50:
        color = "orange"
    else:
        color = "red"

    _write_payload(output=output, label=label, message=f"{percent:.2f}%", color=color)


def _build_status_badge(*, conclusion: str, label: str, output: Path) -> None:
    normalized = conclusion.strip().lower() or "neutral"
    message = _STATUS_MESSAGES.get(normalized, normalized.replace("_", " "))
    color = _STATUS_COLORS.get(normalized, "lightgrey")
    _write_payload(output=output, label=label, message=message, color=color)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    coverage_parser = subparsers.add_parser("coverage", help="Build a coverage badge payload.")
    coverage_parser.add_argument("--coverage-file", type=Path, required=True)
    coverage_parser.add_argument("--label", required=True)
    coverage_parser.add_argument("--output", type=Path, required=True)

    status_parser = subparsers.add_parser("status", help="Build a workflow status badge payload.")
    status_parser.add_argument("--conclusion", required=True)
    status_parser.add_argument("--label", required=True)
    status_parser.add_argument("--output", type=Path, required=True)

    args = parser.parse_args()

    if args.command == "coverage":
        _build_coverage_badge(
            coverage_file=args.coverage_file,
            label=args.label,
            output=args.output,
        )
        return 0

    _build_status_badge(conclusion=args.conclusion, label=args.label, output=args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
