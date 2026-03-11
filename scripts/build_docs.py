#!/usr/bin/env python3
"""Build API docs with pdoc and then build the MkDocs site."""

from __future__ import annotations

import subprocess
import sys


def _run(cmd: list[str]) -> int:
    completed = subprocess.run(cmd, check=False)
    return completed.returncode


def main() -> int:
    if _run([sys.executable, "scripts/generate_api_docs.py"]) != 0:
        return 1
    if _run([sys.executable, "-m", "mkdocs", "build", "--strict"]) != 0:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

