"""Tests for the docs build orchestration script."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from types import ModuleType

import pytest


def _load_build_docs_module() -> ModuleType:
    script_path = Path("scripts/build_docs.py")
    spec = importlib.util.spec_from_file_location("build_docs_script", script_path)
    if spec is None or spec.loader is None:
        raise AssertionError("Unable to load scripts/build_docs.py for testing.")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_build_docs_runs_sdk_reference_generation_before_mkdocs(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    module = _load_build_docs_module()
    commands: list[list[str]] = []

    def fake_run(cmd: list[str]) -> int:
        commands.append(cmd)
        return 0

    monkeypatch.setattr(module, "_run", fake_run)

    assert module.main() == 0
    assert commands == [
        [sys.executable, "scripts/generate_api_docs.py"],
        [sys.executable, "scripts/generate_sdk_reference.py"],
        [sys.executable, "-m", "mkdocs", "build", "--strict"],
    ]


def test_build_docs_stops_when_sdk_reference_generation_fails(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    module = _load_build_docs_module()
    commands: list[list[str]] = []

    def fake_run(cmd: list[str]) -> int:
        commands.append(cmd)
        if cmd == [sys.executable, "scripts/generate_sdk_reference.py"]:
            return 1
        return 0

    monkeypatch.setattr(module, "_run", fake_run)

    assert module.main() == 1
    assert commands == [
        [sys.executable, "scripts/generate_api_docs.py"],
        [sys.executable, "scripts/generate_sdk_reference.py"],
    ]
