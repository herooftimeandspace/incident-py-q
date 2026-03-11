"""Version alignment tests for runtime and package metadata."""

from __future__ import annotations

import tomllib
from pathlib import Path

from incident_py_q import __version__


def test_runtime_version_matches_pyproject() -> None:
    pyproject = tomllib.loads(Path("pyproject.toml").read_text(encoding="utf-8"))
    assert __version__ == pyproject["project"]["version"]
