"""Tests for the deprecated aliases kept across the Golden OpenAPI migration."""

from __future__ import annotations

import json
import warnings
from pathlib import Path
from unittest import mock

import httpx
import pytest
import respx

from incident_py_q import Client
from incident_py_q.compat import (
    DeprecatedMethodAlias,
    install_legacy_aliases,
    legacy_alias_conflicts,
)
from incident_py_q.schema.loader import load_legacy_aliases
from incident_py_q.sdk.runtime import Namespace
from incident_py_q.silver.runtime import build_silver_metadata, superseded_by_golden

IDENTIFIER = "11111111-1111-1111-1111-111111111111"


def _client() -> Client:
    return Client(
        base_url="https://tenant.example",
        api_token="token-123",
        validate_responses=True,
    )


def _part_payload() -> dict[str, object]:
    return {
        "UserToken": IDENTIFIER,
        "RequestDate": "2026-09-28T00:00:00Z",
        "ExecutionTime": 0.01,
        "StatusCode": 200,
        "ProcessId": 1,
        "Item": {
            "PartId": IDENTIFIER,
            "SiteId": IDENTIFIER,
            "ProductId": IDENTIFIER,
            "CreatedDate": "2026-09-28T00:00:00Z",
            "ModifiedDate": "2026-09-28T00:00:00Z",
            "StandardCostEach": 12.5,
            "StandardSupplierId": IDENTIFIER,
            "Name": "Screen",
        },
    }


def test_every_recorded_alias_is_installed() -> None:
    records = load_legacy_aliases()["aliases"]
    client = _client()
    try:
        for record in records:
            namespace = getattr(client, record["legacy_namespace"], None)
            assert namespace is not None, record["legacy_namespace"]
            alias = getattr(namespace, record["legacy_name"], None)
            assert isinstance(alias, DeprecatedMethodAlias), record
    finally:
        client.close()


def test_aliases_are_excluded_from_the_golden_inventory() -> None:
    """The semver-governed surface describes the contract, not the compatibility shims."""
    golden_path = Path("tests/contract/golden_sdk_inventory.json")
    expected = json.loads(golden_path.read_text(encoding="utf-8"))

    client = _client()
    try:
        assert client.sdk_inventory() == expected
    finally:
        client.close()


def test_renamed_golden_method_alias_forwards_and_warns() -> None:
    client = _client()
    try:
        alias = client.tickets.get_ticket_statuses
        assert isinstance(alias, DeprecatedMethodAlias)
        assert alias.replacement_path == "client.tickets.list_ticket_statuses"
        assert alias.surface == "golden"
        assert alias._target is client.tickets.list_ticket_statuses
    finally:
        client.close()


def test_alias_for_a_namespace_the_new_contract_dropped() -> None:
    """`parts` is gone from the published contract but still reachable."""
    client = _client()
    try:
        alias = client.parts.get_part
        assert isinstance(alias, DeprecatedMethodAlias)
        assert alias.replacement_path == "client.silver.parts.get_part"
        assert alias.surface == "silver"
    finally:
        client.close()


@respx.mock
def test_migrated_route_is_callable_through_its_alias() -> None:
    respx.get(f"https://tenant.example/api/v1.0/parts/{IDENTIFIER}").mock(
        return_value=httpx.Response(200, json=_part_payload())
    )

    client = _client()
    try:
        with pytest.warns(DeprecationWarning, match="client.parts.get_part"):
            payload = client.parts.get_part(part_id=IDENTIFIER)
    finally:
        client.close()

    assert isinstance(payload, dict)
    assert payload["Item"]["Name"] == "Screen"


@respx.mock
def test_new_location_does_not_warn() -> None:
    respx.get(f"https://tenant.example/api/v1.0/parts/{IDENTIFIER}").mock(
        return_value=httpx.Response(200, json=_part_payload())
    )

    client = _client()
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("error", DeprecationWarning)
            payload = client.silver.parts.get_part(part_id=IDENTIFIER)
    finally:
        client.close()

    assert isinstance(payload, dict)
    assert payload["Item"]["Name"] == "Screen"


def test_aliases_never_shadow_a_real_method() -> None:
    """A legacy name reused by a different new operation is a conflict, not an alias."""
    conflicts = legacy_alias_conflicts()
    assert conflicts

    client = _client()
    try:
        for conflict in conflicts:
            namespace = getattr(client, conflict["legacy_namespace"])
            occupant = getattr(namespace, conflict["legacy_name"])
            assert not isinstance(occupant, DeprecatedMethodAlias), conflict
            assert occupant.operation.operation_id == conflict["now_resolves_to_operation_id"]
    finally:
        client.close()


def test_recorded_conflicts_are_not_also_recorded_as_aliases() -> None:
    payload = load_legacy_aliases()
    alias_keys = {(item["legacy_namespace"], item["legacy_name"]) for item in payload["aliases"]}
    conflict_keys = {
        (item["legacy_namespace"], item["legacy_name"]) for item in payload["conflicts"]
    }

    assert alias_keys.isdisjoint(conflict_keys)


def test_alias_forwards_raw_iter_pages_and_metadata() -> None:
    """The proxy forwards call, raw, and paging, and exposes target metadata."""
    calls: list[tuple[str, dict[str, object]]] = []

    class _Target:
        __name__ = "list_ticket_statuses"
        __doc__ = "Target docstring."
        operation = "sentinel-operation"

        def __call__(self, **kwargs: object) -> str:
            calls.append(("call", kwargs))
            return "called"

        def raw(self, **kwargs: object) -> str:
            calls.append(("raw", kwargs))
            return "raw"

        def iter_pages(self, **kwargs: object) -> str:
            calls.append(("iter_pages", kwargs))
            return "pages"

    alias = DeprecatedMethodAlias(
        target=_Target(),
        legacy_path="client.tickets.get_ticket_statuses",
        replacement_path="client.tickets.list_ticket_statuses",
        surface="golden",
    )

    for invoke, expected in (
        (lambda: alias(page=1), "called"),
        (lambda: alias.raw(page=2), "raw"),
        (lambda: alias.iter_pages(page=3), "pages"),
    ):
        with pytest.warns(DeprecationWarning, match="get_ticket_statuses"):
            assert invoke() == expected

    assert [name for name, _ in calls] == ["call", "raw", "iter_pages"]
    # Metadata access is not a use of the deprecated route, so it must not warn.
    with warnings.catch_warnings():
        warnings.simplefilter("error", DeprecationWarning)
        assert alias.operation == "sentinel-operation"
    assert alias.__name__ == "list_ticket_statuses"
    assert "client.tickets.list_ticket_statuses" in (alias.__doc__ or "")
    assert "Target docstring." in (alias.__doc__ or "")
    assert "get_ticket_statuses" in repr(alias)


def test_alias_without_a_target_signature_is_still_usable() -> None:
    class _Bare:
        def __call__(self, **kwargs: object) -> str:
            return "ok"

    alias = DeprecatedMethodAlias(
        target=_Bare(),
        legacy_path="client.parts.get_part",
        replacement_path="client.silver.parts.get_part",
        surface="silver",
    )

    assert not hasattr(alias, "__signature__")
    assert alias.__name__ == "get_part"


def test_unresolvable_alias_records_are_skipped() -> None:
    """A record pointing at a namespace or method that does not exist is ignored."""
    records = {
        "aliases": [
            "not-a-record",
            {"legacy_namespace": "tickets", "legacy_name": "x", "target_namespace": ""},
            {
                "legacy_namespace": "tickets",
                "legacy_name": "ghost_method",
                "surface": "golden",
                "target_namespace": "tickets",
                "target_name": "does_not_exist",
            },
            {
                "legacy_namespace": "tickets",
                "legacy_name": "ghost_namespace",
                "surface": "silver",
                "target_namespace": "does_not_exist",
                "target_name": "whatever",
            },
        ]
    }

    client = _client()
    try:
        with mock.patch(
            "incident_py_q.compat.load_legacy_aliases",
            return_value=records,
        ):
            installed = install_legacy_aliases(client=client, namespace_factory=Namespace)
        assert installed == ()
        assert not hasattr(client.tickets, "ghost_method")
    finally:
        client.close()


def test_malformed_alias_payloads_are_tolerated() -> None:
    client = _client()
    try:
        with mock.patch(
            "incident_py_q.compat.load_legacy_aliases",
            return_value={"aliases": "not-a-list"},
        ):
            assert install_legacy_aliases(client=client, namespace_factory=Namespace) == ()
    finally:
        client.close()


def test_conflicts_tolerate_a_malformed_payload() -> None:
    with mock.patch(
        "incident_py_q.compat.load_legacy_aliases",
        return_value={"conflicts": "not-a-list"},
    ):
        assert legacy_alias_conflicts() == ()


def test_silver_surface_is_unfiltered_without_a_registry() -> None:
    """Golden cannot supersede anything when there is no contract to compare against."""
    assert superseded_by_golden(build_silver_metadata(), None) == ()
