"""Tests for the deprecated aliases kept across the Golden OpenAPI migration."""

from __future__ import annotations

import json
import warnings
from pathlib import Path

import httpx
import pytest
import respx

from incident_py_q import Client
from incident_py_q.compat import DeprecatedMethodAlias, legacy_alias_conflicts
from incident_py_q.schema.loader import load_legacy_aliases

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
