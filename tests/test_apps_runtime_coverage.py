"""High-coverage branch tests for app runtime services and helper functions."""

from __future__ import annotations

import asyncio
from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any, cast

import pytest

from incident_py_q.apps.models import AppLookupResponse
from incident_py_q.apps.runtime import (
    AppRegistryService,
    AppsNamespace,
    AsyncAppRegistryService,
    AsyncAppsNamespace,
    AsyncGoogleDeviceDataService,
    AsyncMicrosoftIntuneService,
    AsyncMosyleService,
    GoogleDeviceDataService,
    MicrosoftIntuneService,
    MosyleService,
    _absolute_app_url,
    _app_headers,
    _extract_external_id_lookup,
    _extract_mapping_app_id,
    _normalize_owner_type,
    _tenant_origin,
)
from incident_py_q.apps.validator import AppSchemaValidator
from incident_py_q.config import ClientConfig
from incident_py_q.exceptions import SchemaValidationError


def _config() -> ClientConfig:
    return ClientConfig(
        base_url="https://tenant.example/api/v1.0",
        api_token="token-123",
        site_id="site-42",
        client_header="ApiClient",
        auth_mode="bearer",
        app_headers={"apptoken": "app-token"},
        timeout=10.0,
        validate_responses=True,
        max_retries=0,
        backoff_base=0.01,
    )


class _ValidatorStub:
    def __init__(self, fail_on: set[str] | None = None) -> None:
        self.fail_on = fail_on or set()
        self.calls: list[str] = []

    def validate(self, schema_name: str, payload: Any) -> None:
        self.calls.append(schema_name)
        if schema_name in self.fail_on:
            raise SchemaValidationError(f"schema fail: {schema_name}")


@dataclass
class _SyncClientStub:
    config: ClientConfig
    responses: list[Any]

    def __post_init__(self) -> None:
        self.calls: list[dict[str, Any]] = []

    def request(
        self,
        method: str,
        path: str,
        *,
        path_params: Mapping[str, Any] | None = None,
        params: Mapping[str, Any] | None = None,
        json: Any | None = None,
        headers: Mapping[str, str] | None = None,
        timeout: float | None = None,
    ) -> dict[str, Any] | list[Any] | None:
        self.calls.append(
            {
                "method": method,
                "path": path,
                "path_params": path_params,
                "params": params,
                "json": json,
                "headers": dict(headers) if headers else None,
                "timeout": timeout,
            }
        )
        if not self.responses:
            raise AssertionError("No stub response available.")
        item = self.responses.pop(0)
        if isinstance(item, Exception):
            raise item
        if item is None or isinstance(item, (dict, list)):
            return item
        raise AssertionError(f"Unsupported stub response type: {type(item)!r}")


@dataclass
class _AsyncClientStub:
    config: ClientConfig
    responses: list[Any]

    def __post_init__(self) -> None:
        self.calls: list[dict[str, Any]] = []

    async def request(
        self,
        method: str,
        path: str,
        *,
        path_params: Mapping[str, Any] | None = None,
        params: Mapping[str, Any] | None = None,
        json: Any | None = None,
        headers: Mapping[str, str] | None = None,
        timeout: float | None = None,
    ) -> dict[str, Any] | list[Any] | None:
        self.calls.append(
            {
                "method": method,
                "path": path,
                "path_params": path_params,
                "params": params,
                "json": json,
                "headers": dict(headers) if headers else None,
                "timeout": timeout,
            }
        )
        if not self.responses:
            raise AssertionError("No stub response available.")
        item = self.responses.pop(0)
        if isinstance(item, Exception):
            raise item
        if item is None or isinstance(item, (dict, list)):
            return item
        raise AssertionError(f"Unsupported stub response type: {type(item)!r}")


def test_runtime_path_and_mapping_helpers() -> None:
    assert _tenant_origin("https://tenant.example/api/v1") == "https://tenant.example"
    with pytest.raises(ValueError):
        _tenant_origin("tenant.example/api/v1")

    assert _absolute_app_url("https://tenant.example/api/v1", "/apps/demo") == "https://tenant.example/apps/demo"
    assert _absolute_app_url("https://tenant.example/api/v1", "apps/demo") == "https://tenant.example/apps/demo"
    assert _absolute_app_url("https://tenant.example/api/v1", "https://other.example/a") == "https://other.example/a"

    merged = _app_headers(_config(), {"usertoken": "user-token"})
    assert merged == {"apptoken": "app-token", "usertoken": "user-token"}

    assert _extract_mapping_app_id({"DataMappings": {"Model": {"AppId": "microsoftIntune"}}}) == "microsoftIntune"
    assert _extract_mapping_app_id({"DataMappings": {"Model": "bad"}}) is None
    assert _extract_mapping_app_id({"DataMappings": "bad"}) is None
    assert _extract_mapping_app_id({}) is None

    assert _extract_external_id_lookup(
        {"DataMappings": {"Lookups": [{"Key": "ExternalId", "Value": "ext-1"}]}}
    ) == "ext-1"
    assert _extract_external_id_lookup({"DataMappings": {"Lookups": "bad"}}) is None
    assert _extract_external_id_lookup({"DataMappings": {"Lookups": [{"Key": "Other", "Value": "x"}]}}) is None
    assert _extract_external_id_lookup({"DataMappings": "bad"}) is None
    assert _extract_external_id_lookup({}) is None

    assert _normalize_owner_type("Company") == "Company"
    assert _normalize_owner_type("Personal") == "Personal"
    assert _normalize_owner_type("unexpected") == "Unknown"


def test_sync_registry_service_branches() -> None:
    validator = _ValidatorStub()
    client_none = _SyncClientStub(config=_config(), responses=[None])
    registry_none = AppRegistryService(client_none, cast(AppSchemaValidator, validator))
    assert registry_none.list_apps_raw() is None
    client_none_2 = _SyncClientStub(config=_config(), responses=[None])
    registry_none_2 = AppRegistryService(client_none_2, cast(AppSchemaValidator, validator))
    with pytest.raises(ValueError):
        registry_none_2.list_apps()

    client_bad = _SyncClientStub(config=_config(), responses=[["not-an-object"]])
    with pytest.raises(ValueError):
        AppRegistryService(client_bad, cast(AppSchemaValidator, validator)).list_apps_raw()

    client_ok = _SyncClientStub(
        config=_config(),
        responses=[{"ItemCount": 1, "StatusCode": 200, "Items": [{"AppId": "a", "Name": "A", "IsActive": True}]}],
    )
    model = AppRegistryService(client_ok, cast(AppSchemaValidator, validator)).list_apps(include_hidden=True, timeout=2.5)
    assert model.item_count == 1
    assert "registry_response" in validator.calls
    assert client_ok.calls[0]["path"] == "https://tenant.example/api/v1.0/app-registry/apps/true"


def test_sync_intune_service_branches() -> None:
    validator = _ValidatorStub()
    client = _SyncClientStub(
        config=_config(),
        responses=[
            {
                "ExternalId": "ext-company",
                "SerialNumber": "SER-1",
                "AssetTag": "SER-1",
                "CustomFields": {"ManagedDeviceOwnerType": "Company"},
            },
            [{"bad": True}],
            [{"Key": "Action1", "PermissionKey": "perm-1"}, "ignore-me"],
            {"not": "a-list"},
        ],
    )
    service = MicrosoftIntuneService(client, cast(AppSchemaValidator, validator))

    lookup = service.lookup_asset(asset_id="a1", serial_number="SER-1")
    assert lookup is not None
    assert lookup.external_id == "ext-company"
    with pytest.raises(ValueError):
        service.lookup_asset_raw(asset_id="a1", serial_number="SER-1")

    actions = service.list_remote_actions_raw()
    assert actions == [{"Key": "Action1", "PermissionKey": "perm-1"}]
    with pytest.raises(ValueError):
        service.list_remote_actions_raw()

    unknown = service.classify_owner_type_from_lookup(
        {
            "ExternalId": "ext-2",
            "SerialNumber": "SER-2",
            "AssetTag": "SER-2",
            "CustomFields": {"ManagedDeviceOwnerType": "Other"},
        },
        expected_external_id="ext-3",
    )
    assert unknown.owner_type == "Unknown"
    assert unknown.external_id_matches is False


def test_sync_partition_branches() -> None:
    validator = _ValidatorStub()
    client = _SyncClientStub(config=_config(), responses=[])
    service = MicrosoftIntuneService(client, cast(AppSchemaValidator, validator))

    lookup_map: dict[str, AppLookupResponse | None] = {
        "asset-company": AppLookupResponse.model_validate(
            {
                "ExternalId": "ext-company",
                "SerialNumber": "SER-1",
                "AssetTag": "SER-1",
                "CustomFields": {"ManagedDeviceOwnerType": "Company"},
            }
        ),
        "asset-personal": AppLookupResponse.model_validate(
            {
                "ExternalId": "ext-personal",
                "SerialNumber": "SER-2",
                "AssetTag": "SER-2",
                "CustomFields": {"ManagedDeviceOwnerType": "Personal"},
            }
        ),
        "asset-mismatch": AppLookupResponse.model_validate(
            {
                "ExternalId": "not-ext",
                "SerialNumber": "SER-3",
                "AssetTag": "SER-3",
                "CustomFields": {"ManagedDeviceOwnerType": "Company"},
            }
        ),
        "asset-none": None,
        "asset-unknown": AppLookupResponse.model_validate(
            {
                "ExternalId": "ext-unknown",
                "SerialNumber": "SER-5",
                "AssetTag": "SER-5",
                "CustomFields": {"ManagedDeviceOwnerType": "Other"},
            }
        ),
    }

    def _lookup(**kwargs: Any) -> AppLookupResponse | None:
        asset_id = kwargs["asset_id"]
        return lookup_map.get(asset_id)

    service.lookup_asset = _lookup  # type: ignore[method-assign]

    assets: list[Mapping[str, Any]] = [
        {"AssetId": "skip", "SerialNumber": "S0", "DataMappings": {"Model": {"AppId": "googleDeviceData"}}},
        {"AssetId": 1, "SerialNumber": "Sx", "DataMappings": {"Model": {"AppId": "microsoftIntune"}}},
        {
            "AssetId": "asset-company",
            "AssetTag": "SER-1",
            "SerialNumber": "SER-1",
            "DataMappings": {"Model": {"AppId": "microsoftIntune"}, "Lookups": [{"Key": "ExternalId", "Value": "ext-company"}]},
        },
        {
            "AssetId": "asset-personal",
            "AssetTag": "SER-2",
            "SerialNumber": "SER-2",
            "DataMappings": {"Model": {"AppId": "microsoftIntune"}, "Lookups": [{"Key": "ExternalId", "Value": "ext-personal"}]},
        },
        {
            "AssetId": "asset-mismatch",
            "AssetTag": "SER-3",
            "SerialNumber": "SER-3",
            "DataMappings": {"Model": {"AppId": "microsoftIntune"}, "Lookups": [{"Key": "ExternalId", "Value": "ext-mismatch"}]},
        },
        {
            "AssetId": "asset-none",
            "AssetTag": "SER-4",
            "SerialNumber": "SER-4",
            "DataMappings": {"Model": {"AppId": "microsoftIntune"}, "Lookups": [{"Key": "ExternalId", "Value": "ext-none"}]},
        },
        {
            "AssetId": "asset-unknown",
            "AssetTag": "SER-5",
            "SerialNumber": "SER-5",
            "DataMappings": {"Model": {"AppId": "microsoftIntune"}, "Lookups": [{"Key": "ExternalId", "Value": "ext-unknown"}]},
        },
    ]

    partition = service.partition_assets_by_owner_type(assets=assets)
    assert len(partition.company) == 1
    assert len(partition.personal) == 1
    assert len(partition.unknown) == 4


def test_sync_mosyle_and_google_services_branches() -> None:
    validator = _ValidatorStub()
    client = _SyncClientStub(
        config=_config(),
        responses=[
            {
                "ExternalId": "mosyle-1",
                "SerialNumber": "SER-M",
                "AssetTag": "SER-M",
                "CustomFields": {"BuildVersion": "1"},
            },
            ["bad-response"],
            [{"Key": "Wipe", "PermissionKey": "perm"}, 1],
            {"nope": True},
            {
                "ExternalId": "google-1",
                "SerialNumber": "SER-G",
                "AssetTag": "SER-G",
                "CustomFields": {"OrgUnitPath": "/Students"},
            },
            ["bad-google-lookup"],
            [{"Key": "GoogleAction", "PermissionKey": "perm"}, None],
            {"bad": "list"},
            {"Id": "sync-1", "CreateAssets": True, "UpdateAssets": True, "DeleteAssets": False},
            None,
            ["bad-sync"],
        ],
    )

    mosyle = MosyleService(client, cast(AppSchemaValidator, validator))
    google = GoogleDeviceDataService(client, cast(AppSchemaValidator, validator))

    assert mosyle.lookup_asset(asset_id="m1", serial_number="SER-M") is not None
    with pytest.raises(ValueError):
        mosyle.lookup_asset_raw(asset_id="m1", serial_number="SER-M")
    assert mosyle.list_remote_actions_raw() == [{"Key": "Wipe", "PermissionKey": "perm"}]
    with pytest.raises(ValueError):
        mosyle.list_remote_actions_raw()

    assert google.lookup_asset(asset_id="g1", serial_number="SER-G", query="q", skip=1, limit=2) is not None
    with pytest.raises(ValueError):
        google.lookup_asset_raw(asset_id="g1", serial_number="SER-G")
    assert google.list_remote_actions_raw() == [{"Key": "GoogleAction", "PermissionKey": "perm"}]
    with pytest.raises(ValueError):
        google.list_remote_actions_raw()
    assert google.get_sync_options().id == "sync-1"
    assert google.get_sync_options_raw() is None
    with pytest.raises(ValueError):
        google.get_sync_options()


def test_apps_namespace_construction() -> None:
    sync_client = _SyncClientStub(config=_config(), responses=[])
    async_client = _AsyncClientStub(config=_config(), responses=[])
    sync_ns = AppsNamespace(sync_client)
    async_ns = AsyncAppsNamespace(async_client)
    assert hasattr(sync_ns, "registry")
    assert hasattr(sync_ns, "google_device_data")
    assert hasattr(async_ns, "registry")
    assert hasattr(async_ns, "microsoft_intune")


def test_async_services_branches() -> None:
    async def run() -> None:
        validator = _ValidatorStub()
        client = _AsyncClientStub(
            config=_config(),
            responses=[
                {"ItemCount": 0, "StatusCode": 200, "Items": []},
                None,
                {
                    "ExternalId": "ext-1",
                    "SerialNumber": "SER-1",
                    "AssetTag": "SER-1",
                    "CustomFields": {"ManagedDeviceOwnerType": "Company"},
                },
                ["bad"],
                [{"Key": "Action", "PermissionKey": "perm"}, "skip"],
                {"bad": "list"},
                {
                    "ExternalId": "mosyle-1",
                    "SerialNumber": "SER-2",
                    "AssetTag": "SER-2",
                    "CustomFields": {"BuildVersion": "1"},
                },
                ["bad"],
                [{"Key": "MAction", "PermissionKey": "perm"}, "skip"],
                {"bad": "list"},
                {
                    "ExternalId": "google-1",
                    "SerialNumber": "SER-3",
                    "AssetTag": "SER-3",
                    "CustomFields": {"OrgUnitPath": "/Staff"},
                },
                ["bad"],
                [{"Key": "GAction", "PermissionKey": "perm"}, "skip"],
                {"bad": "list"},
                {"Id": "sync-1", "CreateAssets": True, "UpdateAssets": False, "DeleteAssets": False},
                None,
                ["bad-sync"],
            ],
        )

        registry = AsyncAppRegistryService(client, cast(AppSchemaValidator, validator))
        assert (await registry.list_apps()).item_count == 0
        assert await registry.list_apps_raw() is None

        intune = AsyncMicrosoftIntuneService(client, cast(AppSchemaValidator, validator))
        assert await intune.lookup_asset(asset_id="a1", serial_number="SER-1") is not None
        with pytest.raises(ValueError):
            await intune.lookup_asset_raw(asset_id="a2", serial_number="SER-2")
        assert await intune.list_remote_actions_raw() == [{"Key": "Action", "PermissionKey": "perm"}]
        with pytest.raises(ValueError):
            await intune.list_remote_actions_raw()

        mosyle = AsyncMosyleService(client, cast(AppSchemaValidator, validator))
        assert await mosyle.lookup_asset(asset_id="m1", serial_number="SER-2") is not None
        with pytest.raises(ValueError):
            await mosyle.lookup_asset_raw(asset_id="m2", serial_number="SER-2")
        assert await mosyle.list_remote_actions_raw() == [{"Key": "MAction", "PermissionKey": "perm"}]
        with pytest.raises(ValueError):
            await mosyle.list_remote_actions_raw()

        google = AsyncGoogleDeviceDataService(client, cast(AppSchemaValidator, validator))
        assert await google.lookup_asset(asset_id="g1", serial_number="SER-3") is not None
        with pytest.raises(ValueError):
            await google.lookup_asset_raw(asset_id="g2", serial_number="SER-3")
        assert await google.list_remote_actions_raw() == [{"Key": "GAction", "PermissionKey": "perm"}]
        with pytest.raises(ValueError):
            await google.list_remote_actions_raw()
        assert (await google.get_sync_options()).id == "sync-1"
        assert await google.get_sync_options_raw() is None
        with pytest.raises(ValueError):
            await google.get_sync_options()

        async_intune = AsyncMicrosoftIntuneService(
            _AsyncClientStub(config=_config(), responses=[]),
            cast(AppSchemaValidator, validator),
        )

        async def _lookup_async(**kwargs: Any) -> AppLookupResponse | None:
            aid = kwargs["asset_id"]
            if aid == "a-company":
                return AppLookupResponse.model_validate(
                    {
                        "ExternalId": "ext-company",
                        "SerialNumber": "SER-C",
                        "AssetTag": "SER-C",
                        "CustomFields": {"ManagedDeviceOwnerType": "Company"},
                    }
                )
            if aid == "a-none":
                return None
            return AppLookupResponse.model_validate(
                {
                    "ExternalId": "ext-unknown",
                    "SerialNumber": "SER-U",
                    "AssetTag": "SER-U",
                    "CustomFields": {"ManagedDeviceOwnerType": "Other"},
                }
            )

        async_intune.lookup_asset = _lookup_async  # type: ignore[method-assign]
        partition = await async_intune.partition_assets_by_owner_type(
            assets=[
                {"AssetId": 1, "SerialNumber": "SER-X", "DataMappings": {"Model": {"AppId": "microsoftIntune"}}},
                {
                    "AssetId": "a-company",
                    "SerialNumber": "SER-C",
                    "DataMappings": {"Model": {"AppId": "microsoftIntune"}, "Lookups": [{"Key": "ExternalId", "Value": "ext-company"}]},
                },
                {
                    "AssetId": "a-none",
                    "SerialNumber": "SER-N",
                    "DataMappings": {"Model": {"AppId": "microsoftIntune"}, "Lookups": [{"Key": "ExternalId", "Value": "ext-none"}]},
                },
                {
                    "AssetId": "a-unknown",
                    "SerialNumber": "SER-U",
                    "DataMappings": {"Model": {"AppId": "microsoftIntune"}, "Lookups": [{"Key": "ExternalId", "Value": "ext-unknown"}]},
                },
            ]
        )
        assert len(partition.company) == 1
        assert len(partition.unknown) == 3

    asyncio.run(run())
