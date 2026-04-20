"""Helpers for promotion PR semantic-version label selection."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any, Final

DEFAULT_SEMVER_LABEL: Final[str] = "semver:patch"
VALID_SEMVER_LABELS: Final[tuple[str, str, str]] = (
    "semver:patch",
    "semver:minor",
    "semver:major",
)


def select_semver_label(
    labels: Sequence[str],
    *,
    default_label: str = DEFAULT_SEMVER_LABEL,
) -> str:
    """Return the single semver label from a label list or a safe default."""
    _validate_default_label(default_label)
    unique_labels = list(dict.fromkeys(label for label in labels if label in VALID_SEMVER_LABELS))
    if not unique_labels:
        return default_label
    if len(unique_labels) > 1:
        raise ValueError(
            "Expected at most one semver label, found "
            f"{', '.join(unique_labels)}."
        )
    return unique_labels[0]


def choose_associated_pull(
    pulls: Sequence[Mapping[str, Any]],
    *,
    base_ref: str | None = None,
) -> Mapping[str, Any] | None:
    """Prefer the associated pull request that targets the expected base branch."""
    if base_ref is not None:
        for pull in pulls:
            if _pull_base_ref(pull) == base_ref:
                return pull
    return pulls[0] if pulls else None


def resolve_promotion_semver_label(
    pulls: Sequence[Mapping[str, Any]],
    *,
    base_ref: str | None = None,
    default_label: str = DEFAULT_SEMVER_LABEL,
) -> tuple[int | None, str]:
    """Resolve the semver label for a promotion from associated pull request metadata."""
    pull = choose_associated_pull(pulls, base_ref=base_ref)
    if pull is None:
        return (None, default_label)
    return (_pull_number(pull), select_semver_label(_pull_label_names(pull), default_label=default_label))


def _validate_default_label(default_label: str) -> None:
    if default_label not in VALID_SEMVER_LABELS:
        raise ValueError(f"Unsupported default semver label: {default_label}")


def _pull_base_ref(pull: Mapping[str, Any]) -> str | None:
    base = pull.get("base")
    if not isinstance(base, Mapping):
        return None
    base_ref = base.get("ref")
    return base_ref if isinstance(base_ref, str) else None


def _pull_label_names(pull: Mapping[str, Any]) -> list[str]:
    raw_labels = pull.get("labels")
    if not isinstance(raw_labels, Sequence):
        return []
    names: list[str] = []
    for label in raw_labels:
        if not isinstance(label, Mapping):
            continue
        name = label.get("name")
        if isinstance(name, str):
            names.append(name)
    return names


def _pull_number(pull: Mapping[str, Any]) -> int | None:
    number = pull.get("number")
    return number if isinstance(number, int) else None
