"""Tests for the local CI runner script."""

from __future__ import annotations

import importlib.util
from pathlib import Path
from types import ModuleType

import pytest


def _load_run_local_ci_module() -> ModuleType:
    script_path = Path("scripts/run_local_ci.py")
    spec = importlib.util.spec_from_file_location("run_local_ci_script", script_path)
    if spec is None or spec.loader is None:
        raise AssertionError("Unable to load scripts/run_local_ci.py for testing.")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_commands_for_dev_match_quality_workflow() -> None:
    module = _load_run_local_ci_module()

    commands = module._commands_for_target("dev")

    assert commands == [
        (
            "pip-audit",
            [
                module.sys.executable,
                "-m",
                "pip_audit",
                "--cache-dir",
                ".cache/pip-audit",
            ],
        ),
        ("ruff", [module.sys.executable, "-m", "ruff", "check", "."]),
        ("mypy", [module.sys.executable, "-m", "mypy", "src", "tests", "scripts"]),
        (
            "unit-tests",
            [
                module.sys.executable,
                "-m",
                "pytest",
                "--cov=incident_py_q",
                "--cov-report=xml",
                "--cov-report=term-missing",
                "--cov-fail-under=95",
                "-m",
                "not integration",
            ],
        ),
        (
            "wheel",
            [
                module.sys.executable,
                "-m",
                "pip",
                "wheel",
                "--no-deps",
                "--no-build-isolation",
                "--wheel-dir",
                "dist",
                ".",
            ],
        ),
    ]


def test_commands_for_main_include_integration_and_docs() -> None:
    module = _load_run_local_ci_module()

    commands = module._commands_for_target("main")

    assert commands[-2:] == [
        ("integration-tests", [module.sys.executable, "-m", "pytest", "-m", "integration"]),
        ("docs-build", [module.sys.executable, "scripts/build_docs.py"]),
    ]


def test_main_requires_integration_environment(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    module = _load_run_local_ci_module()
    monkeypatch.delenv("INCIDENTIQ_TEST_BASE_URL", raising=False)
    monkeypatch.delenv("INCIDENTIQ_TEST_API_TOKEN", raising=False)
    monkeypatch.setattr(module.sys, "argv", ["run_local_ci.py", "--target", "main"])

    assert module.main() == 1
    assert "Integration checks require these environment variables" in capsys.readouterr().err


def test_dev_runs_all_commands_until_failure(monkeypatch: pytest.MonkeyPatch) -> None:
    module = _load_run_local_ci_module()
    monkeypatch.setattr(module.sys, "argv", ["run_local_ci.py", "--target", "dev"])
    seen: list[list[str]] = []

    def fake_run(cmd: list[str]) -> int:
        seen.append(cmd)
        return 0

    monkeypatch.setattr(module, "_run", fake_run)

    assert module.main() == 0
    assert seen == [command for _, command in module._commands_for_target("dev")]
