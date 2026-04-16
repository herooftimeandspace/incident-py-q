#!/usr/bin/env python3
"""Bump repository version metadata using semantic version parts."""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Final

_VERSION_RE: Final[re.Pattern[str]] = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")


def _parse_version(raw_version: str) -> tuple[int, int, int]:
    match = _VERSION_RE.fullmatch(raw_version.strip())
    if match is None:
        raise ValueError(f"Unsupported version format: {raw_version!r}")
    major, minor, patch = match.groups()
    return (int(major), int(minor), int(patch))


def _next_version(raw_version: str, part: str) -> str:
    major, minor, patch = _parse_version(raw_version)
    if part == "major":
        return f"{major + 1}.0.0"
    if part == "minor":
        return f"{major}.{minor + 1}.0"
    return f"{major}.{minor}.{patch + 1}"


def _update_pyproject(path: Path, version: str) -> None:
    pattern = re.compile(r'(?m)^version = "[^"]+"$')
    current = path.read_text(encoding="utf-8")
    updated, count = pattern.subn(f'version = "{version}"', current, count=1)
    if count != 1:
        raise ValueError(f"Could not update version in {path}")
    path.write_text(updated, encoding="utf-8")


def _update_version_module(path: Path, version: str) -> None:
    pattern = re.compile(r'(?m)^__version__ = "[^"]+"$')
    current = path.read_text(encoding="utf-8")
    updated, count = pattern.subn(f'__version__ = "{version}"', current, count=1)
    if count != 1:
        raise ValueError(f"Could not update version in {path}")
    path.write_text(updated, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--part", choices=("patch", "minor", "major"), required=True)
    parser.add_argument("--current-version")
    parser.add_argument("--pyproject", type=Path, default=Path("pyproject.toml"))
    parser.add_argument(
        "--version-file",
        type=Path,
        default=Path("src/incident_py_q/version.py"),
    )
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    current_version = args.current_version
    if current_version is None:
        pyproject_text = args.pyproject.read_text(encoding="utf-8")
        match = re.search(r'(?m)^version = "([^"]+)"$', pyproject_text)
        if match is None:
            raise ValueError(f"Could not read version from {args.pyproject}")
        current_version = match.group(1)

    new_version = _next_version(current_version, args.part)
    if args.write:
        _update_pyproject(args.pyproject, new_version)
        _update_version_module(args.version_file, new_version)

    print(new_version)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
