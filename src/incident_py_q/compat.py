"""Deprecated method aliases carried over from the pre-OpenAPI SDK surface.

Migrating the Golden contract to the published OpenAPI document renamed most
operations and moved a set of routes onto the Silver surface. Both changes would
otherwise break every caller on upgrade, so the previous method names stay
available here as deprecated aliases that forward to their new location and warn.

Aliases are deliberately kept out of `sdk_inventory()`. That snapshot is the
semver-governed public surface, and it should describe the contract as it is now,
not the compatibility shims layered on top of it.

One class of change cannot be aliased: a legacy method name that a *different*
new operation now occupies. Redirecting it would shadow a real method, so those
are recorded as conflicts in `data/legacy/aliases.json` and surfaced through
`legacy_alias_conflicts()` instead of being silently rewired.
"""

from __future__ import annotations

import warnings
from typing import Any

from .schema.loader import load_legacy_aliases

__all__ = [
    "DeprecatedMethodAlias",
    "install_legacy_aliases",
    "legacy_alias_conflicts",
]


class DeprecatedMethodAlias:
    """Forwarding proxy for a method that moved or was renamed.

    Calls are forwarded to the target without awaiting, so the same proxy works
    for both the sync and async clients: an async target simply returns its
    coroutine or async iterator to the caller untouched.
    """

    def __init__(
        self,
        *,
        target: Any,
        legacy_path: str,
        replacement_path: str,
        surface: str,
    ) -> None:
        self._target = target
        self.legacy_path = legacy_path
        self.replacement_path = replacement_path
        self.surface = surface
        self.__name__ = getattr(target, "__name__", legacy_path.rsplit(".", 1)[-1])
        signature = getattr(target, "__signature__", None)
        if signature is not None:
            self.__signature__ = signature
        self.__doc__ = (
            f"Deprecated alias for `{replacement_path}`.\n\n"
            f"`{legacy_path}` was part of the SDK surface before the Golden contract "
            f"moved to the published OpenAPI document. It still works and forwards to "
            f"`{replacement_path}`, but it emits a DeprecationWarning and will be "
            f"removed in a future release.\n\n"
            f"{getattr(target, '__doc__', '') or ''}"
        )

    def _warn(self) -> None:
        warnings.warn(
            f"`{self.legacy_path}` is deprecated and will be removed in a future release; "
            f"use `{self.replacement_path}` instead.",
            DeprecationWarning,
            stacklevel=3,
        )

    def __call__(self, **kwargs: Any) -> Any:
        self._warn()
        return self._target(**kwargs)

    def raw(self, **kwargs: Any) -> Any:
        self._warn()
        return self._target.raw(**kwargs)

    def iter_pages(self, **kwargs: Any) -> Any:
        self._warn()
        return self._target.iter_pages(**kwargs)

    def __getattr__(self, name: str) -> Any:
        # Metadata access (signature, operation, models) is not itself a usage of
        # the deprecated route, so it forwards without warning.
        return getattr(self._target, name)

    def __repr__(self) -> str:
        return (
            f"DeprecatedMethodAlias({self.legacy_path!r} -> {self.replacement_path!r}, "
            f"surface={self.surface!r})"
        )


def legacy_alias_conflicts() -> tuple[dict[str, Any], ...]:
    """Return legacy method names that a different new operation now occupies.

    These are the only names that could not be preserved. Calling one still works,
    but it now reaches a different route than it did before the migration, so
    callers must review them by hand.
    """
    payload = load_legacy_aliases()
    conflicts = payload.get("conflicts", [])
    if not isinstance(conflicts, list):
        return ()
    return tuple(conflict for conflict in conflicts if isinstance(conflict, dict))


def install_legacy_aliases(
    *,
    client: Any,
    namespace_factory: Any,
) -> tuple[DeprecatedMethodAlias, ...]:
    """Attach deprecated aliases for the pre-OpenAPI method names.

    `namespace_factory` builds an empty namespace object for legacy namespaces the
    new contract no longer has (for example `parts`), so those names keep working.
    """
    payload = load_legacy_aliases()
    records = payload.get("aliases", [])
    if not isinstance(records, list):
        return ()

    installed: list[DeprecatedMethodAlias] = []
    for record in records:
        if not isinstance(record, dict):
            continue

        target = _resolve_target(client=client, record=record)
        if target is None:
            continue

        legacy_namespace = str(record["legacy_namespace"])
        legacy_name = str(record["legacy_name"])
        namespace_obj = getattr(client, legacy_namespace, None)
        if namespace_obj is None:
            namespace_obj = namespace_factory(legacy_namespace)
            setattr(client, legacy_namespace, namespace_obj)

        # Never shadow a real method; the generator records those as conflicts.
        if getattr(namespace_obj, legacy_name, None) is not None:
            continue

        surface = str(record.get("surface", "golden"))
        replacement_prefix = "client.silver." if surface == "silver" else "client."
        alias = DeprecatedMethodAlias(
            target=target,
            legacy_path=f"client.{legacy_namespace}.{legacy_name}",
            replacement_path=(
                f"{replacement_prefix}{record['target_namespace']}.{record['target_name']}"
            ),
            surface=surface,
        )
        namespace_obj._register(legacy_name, alias)
        installed.append(alias)

    return tuple(installed)


def _resolve_target(*, client: Any, record: dict[str, Any]) -> Any | None:
    namespace_name = str(record.get("target_namespace", ""))
    method_name = str(record.get("target_name", ""))
    if not namespace_name or not method_name:
        return None

    if str(record.get("surface", "golden")) == "silver":
        root = getattr(client, "silver", None)
        namespace_obj = getattr(root, namespace_name, None) if root is not None else None
    else:
        namespace_obj = getattr(client, namespace_name, None)

    if namespace_obj is None:
        return None
    return getattr(namespace_obj, method_name, None)
