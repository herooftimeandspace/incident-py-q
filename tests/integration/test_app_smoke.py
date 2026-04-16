"""Live integration smoke tests for undocumented Incident IQ app-path APIs."""

from __future__ import annotations

import os
from collections.abc import Mapping
from typing import Any

import httpx
import pytest

from incident_py_q import Client


def _require_integration_env() -> None:
    required = ("INCIDENTIQ_TEST_BASE_URL", "INCIDENTIQ_TEST_API_TOKEN")
    missing = [name for name in required if not os.environ.get(name)]
    if missing:
        joined = ", ".join(missing)
        pytest.skip(f"Integration credentials not configured: missing {joined}")


def _app_is_active(apps: list[Mapping[str, Any]], app_id: str) -> bool:
    return any(item.get("AppId") == app_id and item.get("IsActive") is True for item in apps)


def _skip_if_app_unavailable(exc: httpx.HTTPStatusError, app_name: str) -> None:
    if exc.response.status_code in {403, 404}:
        pytest.skip(f"{app_name} app endpoint unavailable on tenant (status {exc.response.status_code}).")
    raise exc


@pytest.mark.integration
def test_app_registry_and_remote_actions_smoke() -> None:
    _require_integration_env()
    client = Client.from_test_env()
    try:
        registry = client.apps.registry.list_apps_raw(include_hidden=False)
        if registry is None:
            pytest.skip("App registry returned no payload.")
        items = registry.get("Items")
        if not isinstance(items, list):
            raise ValueError("App registry payload missing Items list.")

        if _app_is_active(items, "microsoftIntune"):
            try:
                actions = client.apps.microsoft_intune.list_remote_actions_raw()
                assert isinstance(actions, list)
            except httpx.HTTPStatusError as exc:
                _skip_if_app_unavailable(exc, "Microsoft Intune")

        if _app_is_active(items, "mosyleManager"):
            try:
                actions = client.apps.mosyle.list_remote_actions_raw()
                assert isinstance(actions, list)
            except httpx.HTTPStatusError as exc:
                _skip_if_app_unavailable(exc, "Mosyle")

        if _app_is_active(items, "googleDeviceData"):
            try:
                actions = client.apps.google_device_data.list_remote_actions_raw()
                assert isinstance(actions, list)
            except httpx.HTTPStatusError as exc:
                _skip_if_app_unavailable(exc, "Google Device Data")
    finally:
        client.close()


def _lookup_identifier(prefix: str) -> tuple[str, str, str | None]:
    asset_id = os.environ.get(f"{prefix}_ASSET_ID")
    serial = os.environ.get(f"{prefix}_ASSET_SERIAL")
    tag = os.environ.get(f"{prefix}_ASSET_TAG")
    if not asset_id and not serial:
        raise LookupError(
            f"Missing lookup identifiers: set {prefix}_ASSET_ID or {prefix}_ASSET_SERIAL."
        )
    resolved_id = asset_id or serial
    resolved_serial = serial or asset_id
    assert resolved_id is not None and resolved_serial is not None
    return resolved_id, resolved_serial, tag


@pytest.mark.integration
def test_lookup_smoke_optional() -> None:
    _require_integration_env()
    client = Client.from_test_env()
    try:
        try:
            intune_id, intune_serial, intune_tag = _lookup_identifier("INCIDENTIQ_TEST_INTUNE")
            try:
                payload = client.apps.microsoft_intune.lookup_asset_raw(
                    asset_id=intune_id,
                    serial_number=intune_serial,
                    asset_tag=intune_tag,
                )
                assert payload is None or isinstance(payload, dict)
            except httpx.HTTPStatusError as exc:
                _skip_if_app_unavailable(exc, "Microsoft Intune")
        except LookupError:
            pass

        try:
            mosyle_id, mosyle_serial, mosyle_tag = _lookup_identifier("INCIDENTIQ_TEST_MOSYLE")
            try:
                payload = client.apps.mosyle.lookup_asset_raw(
                    asset_id=mosyle_id,
                    serial_number=mosyle_serial,
                    asset_tag=mosyle_tag,
                )
                assert payload is None or isinstance(payload, dict)
            except httpx.HTTPStatusError as exc:
                _skip_if_app_unavailable(exc, "Mosyle")
        except LookupError:
            pass

        try:
            google_id, google_serial, google_tag = _lookup_identifier("INCIDENTIQ_TEST_GOOGLE_DEVICE")
            try:
                payload = client.apps.google_device_data.lookup_asset_raw(
                    asset_id=google_id,
                    serial_number=google_serial,
                    asset_tag=google_tag,
                )
                assert payload is None or isinstance(payload, dict)
            except httpx.HTTPStatusError as exc:
                _skip_if_app_unavailable(exc, "Google Device Data")
        except LookupError:
            pass
    finally:
        client.close()
