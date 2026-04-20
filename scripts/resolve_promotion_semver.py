#!/usr/bin/env python3
"""Resolve the semver label to apply to an automated promotion pull request."""

from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = PROJECT_ROOT / "src" / "incident_py_q" / "release_semver.py"


def _load_release_semver_helper() -> Any:
    spec = importlib.util.spec_from_file_location("release_semver_helper", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load semver helper from {MODULE_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


resolve_promotion_semver_label = _load_release_semver_helper().resolve_promotion_semver_label


def _gh_json(*args: str) -> Any:
    result = subprocess.run(
        ["gh", *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(result.stdout)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True)
    parser.add_argument("--sha", required=True)
    parser.add_argument("--base-ref")
    parser.add_argument("--default-label", default="semver:patch")
    args = parser.parse_args()

    pulls = _gh_json("api", f"repos/{args.repo}/commits/{args.sha}/pulls")
    pr_number, label = resolve_promotion_semver_label(
        pulls,
        base_ref=args.base_ref,
        default_label=args.default_label,
    )

    if pr_number is None:
        print(
            f"No associated pull request found for {args.sha}; defaulting to {label}.",
            file=sys.stderr,
        )
    else:
        print(f"Resolved {label} from PR #{pr_number}.", file=sys.stderr)

    print(label)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
