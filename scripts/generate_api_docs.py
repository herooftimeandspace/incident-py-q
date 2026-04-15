#!/usr/bin/env python3
"""Generate pdoc HTML API reference into the MkDocs source tree."""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path


def main() -> int:
    docs_api_dir = Path("docs/api")
    src_dir = Path("src").resolve()
    if docs_api_dir.exists():
        shutil.rmtree(docs_api_dir)
    docs_api_dir.mkdir(parents=True, exist_ok=True)

    env = dict(os.environ)
    existing_pythonpath = env.get("PYTHONPATH")
    env["PYTHONPATH"] = (
        f"{src_dir}{os.pathsep}{existing_pythonpath}" if existing_pythonpath else str(src_dir)
    )

    cmd = [
        sys.executable,
        "-m",
        "pdoc",
        "--output-directory",
        str(docs_api_dir),
        "incident_py_q",
    ]
    completed = subprocess.run(cmd, check=False, env=env)
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
