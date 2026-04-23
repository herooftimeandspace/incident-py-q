"""Tests for promotion semver label selection."""

from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path
from typing import Any

import pytest

from incident_py_q.release_semver import (
    DEFAULT_SEMVER_LABEL,
    choose_associated_pull,
    resolve_promotion_semver_label,
    select_semver_label,
)

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RESOLVER_PATH = PROJECT_ROOT / "scripts" / "resolve_promotion_semver.py"
PROMOTION_WORKFLOW_PATH = PROJECT_ROOT / ".github" / "workflows" / "promotion.yml"


def _load_resolver_module() -> Any:
    spec = importlib.util.spec_from_file_location("resolve_promotion_semver", RESOLVER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load resolver script from {RESOLVER_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _pull(number: int, base_ref: str, *labels: str) -> dict[str, Any]:
    return {
        "number": number,
        "base": {"ref": base_ref},
        "labels": [{"name": label} for label in labels],
    }


def test_select_semver_label_defaults_to_patch() -> None:
    assert select_semver_label(["docs", "ci"]) == DEFAULT_SEMVER_LABEL


def test_select_semver_label_keeps_single_semver_value() -> None:
    assert select_semver_label(["docs", "semver:minor", "ci"]) == "semver:minor"


def test_select_semver_label_rejects_multiple_semver_values() -> None:
    with pytest.raises(ValueError, match="Expected at most one semver label"):
        select_semver_label(["semver:patch", "semver:minor"])


def test_choose_associated_pull_prefers_matching_base_ref() -> None:
    pulls = [
        _pull(35, "staging"),
        _pull(37, "main"),
    ]

    assert choose_associated_pull(pulls, base_ref="main") == pulls[1]


def test_resolve_promotion_semver_label_uses_matching_pull_label() -> None:
    pr_number, label = resolve_promotion_semver_label(
        [
            _pull(35, "staging", "docs"),
            _pull(37, "main", "semver:minor"),
        ],
        base_ref="main",
    )

    assert pr_number == 37
    assert label == "semver:minor"


def test_resolve_promotion_semver_label_defaults_when_pull_has_no_semver_label() -> None:
    pr_number, label = resolve_promotion_semver_label([_pull(35, "staging")], base_ref="staging")

    assert pr_number == 35
    assert label == DEFAULT_SEMVER_LABEL


def test_resolve_promotion_semver_label_defaults_when_no_pull_is_associated() -> None:
    pr_number, label = resolve_promotion_semver_label([], base_ref="main")

    assert pr_number is None
    assert label == DEFAULT_SEMVER_LABEL


def test_resolver_script_uses_matching_pull_label(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    resolver = _load_resolver_module()

    def fake_run(
        args: list[str],
        *,
        check: bool,
        capture_output: bool,
        text: bool,
    ) -> subprocess.CompletedProcess[str]:
        assert args == ["gh", "api", "repos/example/repo/commits/abc123/pulls"]
        assert check is True
        assert capture_output is True
        assert text is True
        return subprocess.CompletedProcess(
            args,
            0,
            stdout='[{"number": 42, "base": {"ref": "dev"}, "labels": [{"name": "semver:minor"}]}]',
            stderr="",
        )

    monkeypatch.setattr(subprocess, "run", fake_run)
    monkeypatch.setattr(
        sys,
        "argv",
        ["resolve_promotion_semver.py", "--repo", "example/repo", "--sha", "abc123", "--base-ref", "dev"],
    )

    assert resolver.main() == 0

    output = capsys.readouterr()
    assert output.out == "semver:minor\n"
    assert "Resolved semver:minor from PR #42." in output.err


def test_resolver_script_defaults_when_no_pull_is_associated(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    resolver = _load_resolver_module()

    def fake_run(
        args: list[str],
        *,
        check: bool,
        capture_output: bool,
        text: bool,
    ) -> subprocess.CompletedProcess[str]:
        return subprocess.CompletedProcess(args, 0, stdout="[]", stderr="")

    monkeypatch.setattr(subprocess, "run", fake_run)
    monkeypatch.setattr(
        sys,
        "argv",
        ["resolve_promotion_semver.py", "--repo", "example/repo", "--sha", "abc123", "--base-ref", "dev"],
    )

    assert resolver.main() == 0

    output = capsys.readouterr()
    assert output.out == f"{DEFAULT_SEMVER_LABEL}\n"
    assert "No associated pull request found for abc123" in output.err


def test_resolver_script_defaults_when_gh_lookup_fails(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    resolver = _load_resolver_module()

    def fake_run(
        args: list[str],
        *,
        check: bool,
        capture_output: bool,
        text: bool,
    ) -> subprocess.CompletedProcess[str]:
        raise subprocess.CalledProcessError(4, args, stderr="authentication required")

    monkeypatch.setattr(subprocess, "run", fake_run)
    monkeypatch.setattr(
        sys,
        "argv",
        ["resolve_promotion_semver.py", "--repo", "example/repo", "--sha", "abc123", "--base-ref", "dev"],
    )

    assert resolver.main() == 0

    output = capsys.readouterr()
    assert output.out == f"{DEFAULT_SEMVER_LABEL}\n"
    assert "Could not resolve pull requests associated with abc123" in output.err
    assert "defaulting to semver:patch" in output.err
    assert "authentication required" in output.err


def test_promotion_workflow_authenticates_before_semver_resolution() -> None:
    workflow = PROMOTION_WORKFLOW_PATH.read_text(encoding="utf-8")
    resolver_call = 'resolved_label="$(python scripts/resolve_promotion_semver.py'
    chunks = workflow.split(resolver_call)

    assert len(chunks) == 3
    for chunk in chunks[:-1]:
        api_auth_index = chunk.rfind('export GH_TOKEN="${GH_API_TOKEN}"')
        pr_auth_index = chunk.rfind('export GH_TOKEN="${GH_PR_TOKEN}"')

        assert api_auth_index != -1
        assert pr_auth_index == -1 or api_auth_index > pr_auth_index
