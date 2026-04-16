"""Async runtime tests for undocumented app-path services."""

from __future__ import annotations

import asyncio
from typing import Any

import httpx
import respx

from incident_py_q import AsyncClient
from incident_py_q.schema.registry import SchemaRegistry


def _build_client(tiny_registry: SchemaRegistry, **kwargs: Any) -> AsyncClient:
    return AsyncClient(
        base_url="https://tenant.example/api/v1.0",
        api_token="token-123",
        app_headers={"apptoken": "app-token"},
        registry=tiny_registry,
        max_retries=0,
        **kwargs,
    )


@respx.mock
def test_async_registry_and_lookup(tiny_registry: SchemaRegistry) -> None:
    respx.get("https://tenant.example/api/v1.0/app-registry/apps/false").mock(
        return_value=httpx.Response(
            200,
            json={
                "ItemCount": 1,
                "StatusCode": 200,
                "Items": [
                    {
                        "AppId": "mosyleManager",
                        "Name": "Mosyle Manager",
                        "IsActive": True,
                        "Settings": {"ProvidesAssetData": True},
                    }
                ],
            },
        )
    )
    respx.post("https://tenant.example/apps/mosyleManager/api/mosyleManager/data/assets/lookup").mock(
        return_value=httpx.Response(
            200,
            json={
                "ExternalId": "mosyle-ext",
                "SerialNumber": "SER-1",
                "AssetTag": "SER-1",
                "CustomFields": {"BuildVersion": "1.0"},
            },
        )
    )

    client = _build_client(tiny_registry)

    async def run() -> tuple[str, str]:
        apps = await client.apps.registry.list_apps()
        lookup = await client.apps.mosyle.lookup_asset(asset_id="asset-1", serial_number="SER-1")
        await client.close()
        assert lookup is not None
        return apps.items[0].app_id, lookup.external_id

    app_id, external_id = asyncio.run(run())
    assert app_id == "mosyleManager"
    assert external_id == "mosyle-ext"


@respx.mock
def test_async_lookup_returns_none_for_204(tiny_registry: SchemaRegistry) -> None:
    respx.post(
        "https://tenant.example/apps/googleDeviceData/api/googleDeviceData/data/assets/get-google-device"
    ).mock(return_value=httpx.Response(204))

    client = _build_client(tiny_registry)

    async def run() -> Any:
        result = await client.apps.google_device_data.lookup_asset(
            asset_id="asset-1",
            serial_number="SER-1",
        )
        await client.close()
        return result

    assert asyncio.run(run()) is None
