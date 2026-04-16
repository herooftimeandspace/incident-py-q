"""Sync runtime tests for undocumented app-path services."""

from __future__ import annotations

from typing import Any

import httpx
import pytest
import respx
from pydantic import ValidationError

from incident_py_q import Client
from incident_py_q.schema.registry import SchemaRegistry


def _build_client(tiny_registry: SchemaRegistry, **kwargs: Any) -> Client:
    return Client(
        base_url="https://tenant.example/api/v1.0",
        api_token="token-123",
        site_id="site-42",
        app_headers={"apptoken": "app-token", "usertoken": "user-token"},
        registry=tiny_registry,
        max_retries=0,
        **kwargs,
    )


@respx.mock
def test_registry_list_apps_uses_app_headers_and_origin_path(tiny_registry: SchemaRegistry) -> None:
    route = respx.get("https://tenant.example/api/v1.0/app-registry/apps/false").mock(
        return_value=httpx.Response(
            200,
            json={
                "ItemCount": 1,
                "StatusCode": 200,
                "Items": [
                    {
                        "AppId": "microsoftIntune",
                        "Name": "Microsoft Intune",
                        "IsActive": True,
                        "Settings": {"ProvidesAssetData": True},
                    }
                ],
            },
        )
    )
    client = _build_client(tiny_registry)
    response = client.apps.registry.list_apps()
    client.close()

    assert response.item_count == 1
    assert response.items[0].app_id == "microsoftIntune"
    assert route.call_count == 1
    sent_headers = route.calls[0].request.headers
    assert sent_headers["Authorization"] == "Bearer token-123"
    assert sent_headers["apptoken"] == "app-token"
    assert sent_headers["usertoken"] == "user-token"
    assert sent_headers["SiteId"] == "site-42"


@respx.mock
def test_intune_lookup_uses_apps_root_path(tiny_registry: SchemaRegistry) -> None:
    route = respx.post(
        "https://tenant.example/apps/microsoftIntune/api/microsoftIntune/data/assets/lookup"
    ).mock(
        return_value=httpx.Response(
            200,
            json={
                "ExternalId": "ext-1",
                "SerialNumber": "ABC123",
                "AssetTag": "ABC123",
                "CustomFields": {"ManagedDeviceOwnerType": "Company"},
            },
        )
    )
    client = _build_client(tiny_registry)
    response = client.apps.microsoft_intune.lookup_asset(asset_id="asset-1", serial_number="ABC123")
    client.close()

    assert response is not None
    assert response.external_id == "ext-1"
    assert route.call_count == 1
    assert route.calls[0].request.url.path.startswith("/apps/microsoftIntune/api/")


@respx.mock
def test_lookup_returns_none_for_204(tiny_registry: SchemaRegistry) -> None:
    respx.post("https://tenant.example/apps/mosyleManager/api/mosyleManager/data/assets/lookup").mock(
        return_value=httpx.Response(204)
    )
    client = _build_client(tiny_registry)
    response = client.apps.mosyle.lookup_asset(asset_id="asset-1", serial_number="ABC123")
    client.close()

    assert response is None


def test_lookup_request_validation_rejects_invalid_type(tiny_registry: SchemaRegistry) -> None:
    client = _build_client(tiny_registry)
    with pytest.raises(ValidationError):
        client.apps.microsoft_intune.lookup_asset(asset_id="asset-1", serial_number=123)  # type: ignore[arg-type]
    client.close()


@respx.mock
def test_partition_assets_by_owner_type(tiny_registry: SchemaRegistry) -> None:
    respx.post("https://tenant.example/apps/microsoftIntune/api/microsoftIntune/data/assets/lookup").mock(
        side_effect=[
            httpx.Response(
                200,
                json={
                    "ExternalId": "ext-company",
                    "SerialNumber": "SER-1",
                    "AssetTag": "SER-1",
                    "CustomFields": {"ManagedDeviceOwnerType": "Company"},
                },
            ),
            httpx.Response(
                200,
                json={
                    "ExternalId": "ext-personal",
                    "SerialNumber": "SER-2",
                    "AssetTag": "SER-2",
                    "CustomFields": {"ManagedDeviceOwnerType": "Personal"},
                },
            ),
        ]
    )
    client = _build_client(tiny_registry)
    assets = [
        {
            "AssetId": "asset-1",
            "AssetTag": "SER-1",
            "SerialNumber": "SER-1",
            "DataMappings": {
                "Model": {"AppId": "microsoftIntune"},
                "Lookups": [{"Key": "ExternalId", "Value": "ext-company"}],
            },
        },
        {
            "AssetId": "asset-2",
            "AssetTag": "SER-2",
            "SerialNumber": "SER-2",
            "DataMappings": {
                "Model": {"AppId": "microsoftIntune"},
                "Lookups": [{"Key": "ExternalId", "Value": "ext-personal"}],
            },
        },
        {
            "AssetId": "asset-3",
            "AssetTag": "SER-3",
            "SerialNumber": "SER-3",
            "DataMappings": {
                "Model": {"AppId": "googleDeviceData"},
                "Lookups": [{"Key": "ExternalId", "Value": "ext-ignore"}],
            },
        },
    ]
    partition = client.apps.microsoft_intune.partition_assets_by_owner_type(assets=assets)
    client.close()

    assert len(partition.company) == 1
    assert len(partition.personal) == 1
    assert len(partition.unknown) == 0


@respx.mock
def test_google_sync_options_and_remote_actions(tiny_registry: SchemaRegistry) -> None:
    respx.get("https://tenant.example/apps/googleDeviceData/api/googleDeviceData/sync/options").mock(
        return_value=httpx.Response(
            200,
            json={
                "Id": "sync-1",
                "CreateAssets": True,
                "UpdateAssets": True,
                "DeleteAssets": False,
            },
        )
    )
    respx.get("https://tenant.example/apps/googleDeviceData/api/googleDeviceData/remoteactions").mock(
        return_value=httpx.Response(
            200,
            json=[{"Key": "WipeDevice", "PermissionKey": "app.googledevices.write.device.wipe"}],
        )
    )

    client = _build_client(tiny_registry)
    options = client.apps.google_device_data.get_sync_options()
    actions = client.apps.google_device_data.list_remote_actions()
    client.close()

    assert options.id == "sync-1"
    assert actions[0].key == "WipeDevice"
