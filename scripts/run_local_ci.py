#!/usr/bin/env python3
"""Run the same branch-specific checks that GitHub Actions enforces."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from collections.abc import Sequence

TARGETS = ("dev", "staging", "main")
_REQUIRED_INTEGRATION_ENV = (
    "INCIDENTIQ_TEST_BASE_URL",
    "INCIDENTIQ_TEST_API_TOKEN",
)


def _run(cmd: Sequence[str]) -> int:
    completed = subprocess.run(list(cmd), check=False)
    return completed.returncode


def _require_integration_env() -> int:
    missing = [name for name in _REQUIRED_INTEGRATION_ENV if not os.environ.get(name)]
    if missing:
        joined = ", ".join(missing)
        print(
            f"Integration checks require these environment variables to be set: {joined}",
            file=sys.stderr,
        )
        return 1
    return 0


def _commands_for_target(target: str) -> list[tuple[str, list[str]]]:
    commands: list[tuple[str, list[str]]] = [
        (
            "pip-audit",
            [
                sys.executable,
                "-m",
                "pip_audit",
                "--cache-dir",
                ".cache/pip-audit",
            ],
        ),
        ("ruff", [sys.executable, "-m", "ruff", "check", "."]),
        ("mypy", [sys.executable, "-m", "mypy", "src", "tests", "scripts"]),
        (
            "unit-tests",
            [
                sys.executable,
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
                sys.executable,
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
    if target in {"staging", "main"}:
        commands.append(
            ("integration-tests", [sys.executable, "-m", "pytest", "-m", "integration"])
        )
    if target == "main":
        commands.append(("docs-build", [sys.executable, "scripts/build_docs.py"]))
    return commands


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run the same branch-specific checks that GitHub Actions enforces.",
    )
    parser.add_argument(
        "--target",
        choices=TARGETS,
        default="dev",
        help="Branch policy to mirror locally. Defaults to dev.",
    )
    args = parser.parse_args()

    if args.target in {"staging", "main"} and _require_integration_env() != 0:
        return 1

    for name, cmd in _commands_for_target(args.target):
        print(f"==> {name}: {' '.join(cmd)}")
        if _run(cmd) != 0:
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
