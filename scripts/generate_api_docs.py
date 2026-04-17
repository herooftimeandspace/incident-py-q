#!/usr/bin/env python3
"""Generate pdoc HTML API reference into the MkDocs source tree."""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path

_CSS_REWRITES: tuple[tuple[str, str], ...] = (
    (
        "[type=button],[type=reset],[type=submit],button{-webkit-appearance:button}",
        "[type=button],[type=reset],[type=submit],button{appearance:button;-webkit-appearance:button}",
    ),
    (
        "[type=search]{outline-offset:-2px;-webkit-appearance:textfield}",
        "[type=search]{outline-offset:-2px;appearance:textfield;-webkit-appearance:textfield}",
    ),
    (
        "::-webkit-search-decoration{-webkit-appearance:none}",
        "::-webkit-search-decoration{appearance:none;-webkit-appearance:none}",
    ),
    (
        "::-webkit-file-upload-button{font:inherit;-webkit-appearance:button}",
        "::-webkit-file-upload-button{font:inherit;appearance:button;-webkit-appearance:button}",
    ),
    (
        ".view-source-button{display:inline-block;float:right;",
        ".view-source-button{float:right;",
    ),
)


def _sanitize_pdoc_html(path: Path) -> None:
    content = path.read_text(encoding="utf-8")
    updated = content
    for needle, replacement in _CSS_REWRITES:
        updated = updated.replace(needle, replacement)
    if updated != content:
        path.write_text(updated, encoding="utf-8")


def _sanitize_generated_docs(docs_api_dir: Path) -> None:
    for html_path in docs_api_dir.rglob("*.html"):
        _sanitize_pdoc_html(html_path)


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
    if completed.returncode != 0:
        return completed.returncode
    _sanitize_generated_docs(docs_api_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
