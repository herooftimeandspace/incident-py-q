#!/usr/bin/env python3
"""Generate SDK reference Markdown pages and typing stubs."""

from __future__ import annotations

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from incident_py_q.schema.loader import load_stoplight_documents
from incident_py_q.schema.registry import build_schema_registry
from incident_py_q.sdk.docs import write_sdk_reference_artifacts


def main() -> int:
    registry = build_schema_registry(load_stoplight_documents())
    docs_root = Path("docs/sdk-reference")
    package_root = Path("src/incident_py_q")
    write_sdk_reference_artifacts(
        docs_root=docs_root,
        package_root=package_root,
        registry=registry,
    )
    print(f"Wrote SDK reference pages to {docs_root} and typing stubs to {package_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
