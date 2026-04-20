"""Tests for promotion semver label selection."""

from __future__ import annotations

from typing import Any

import pytest

from incident_py_q.release_semver import (
    DEFAULT_SEMVER_LABEL,
    choose_associated_pull,
    resolve_promotion_semver_label,
    select_semver_label,
)


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
