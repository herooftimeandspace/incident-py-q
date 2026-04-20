#!/usr/bin/env python3
"""Resolve the semver label to apply to an automated promotion pull request."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from typing import Any

from incident_py_q.release_semver import resolve_promotion_semver_label


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
