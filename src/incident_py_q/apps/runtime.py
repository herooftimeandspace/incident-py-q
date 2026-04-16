"""Sync and async runtime services for undocumented Incident IQ app endpoints."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Any, Literal, Protocol
from urllib.parse import urlsplit

from incident_py_q.config import ClientConfig

from .models import (
    AppLookupResponse,
    AppRegistryResponse,
    AppRemoteAction,
    GoogleDeviceLookupRequest,
    GoogleSyncOptionsResponse,
    IntuneLookupRequest,
    IntuneOwnerClassification,
    IntuneOwnershipPartition,
    MosyleLookupRequest,
    OwnerType,
)
from .validator import AppSchemaValidator


class _SyncRequestClient(Protocol):
    @property
    def config(self) -> ClientConfig: ...

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
    ) -> dict[str, Any] | list[Any] | None: ...


class _AsyncRequestClient(Protocol):
    @property
    def config(self) -> ClientConfig: ...

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
    ) -> dict[str, Any] | list[Any] | None: ...


@dataclass(slots=True, frozen=True)
class AppParameterMetadata:
    """Documentation metadata for one app-path method parameter."""

    python_name: str
    api_name: str
    location: str
    required: bool
    type_display: str
    description: str


@dataclass(slots=True, frozen=True)
class AppMethodMetadata:
    """Documentation metadata for one app-path method."""

    service_name: str
    service_label: str
    method_name: str
    summary: str
    description: str
    sync_call: str
    async_call: str
    http_method: str | None
    route: str | None
    parameters: tuple[AppParameterMetadata, ...]
    typed_return: str
    raw_return: str
    response_model: str | None = None
    response_schema: str | None = None


def _tenant_origin(base_url: str) -> str:
    parsed = urlsplit(base_url)
    if not parsed.scheme or not parsed.netloc:
        raise ValueError(f"Invalid tenant base URL {base_url!r}")
    return f"{parsed.scheme}://{parsed.netloc}"


def _absolute_app_url(base_url: str, path: str) -> str:
    if path.startswith("http://") or path.startswith("https://"):
        return path
    safe_path = path if path.startswith("/") else f"/{path}"
    return f"{_tenant_origin(base_url)}{safe_path}"


def _app_headers(config: ClientConfig, extra_headers: Mapping[str, str] | None = None) -> dict[str, str]:
    merged: dict[str, str] = {}
    if config.app_headers:
        merged.update(config.app_headers)
    if extra_headers:
        merged.update(extra_headers)
    return merged


class AppRegistryService:
    """Operations for the Incident IQ app registry endpoint."""

    def __init__(self, client: _SyncRequestClient, validator: AppSchemaValidator) -> None:
        self._client = client
        self._validator = validator

    def list_apps(self, *, include_hidden: bool = False, timeout: float | None = None) -> AppRegistryResponse:
        payload = self.list_apps_raw(include_hidden=include_hidden, timeout=timeout)
        if not isinstance(payload, dict):
            raise ValueError("Expected app registry response object.")
        return AppRegistryResponse.model_validate(payload)

    def list_apps_raw(
        self, *, include_hidden: bool = False, timeout: float | None = None
    ) -> dict[str, Any] | None:
        path = f"/api/v1.0/app-registry/apps/{str(include_hidden).lower()}"
        payload = self._client.request(
            "GET",
            _absolute_app_url(self._client.config.base_url, path),
            headers=_app_headers(self._client.config),
            timeout=timeout,
        )
        if payload is None:
            return None
        if not isinstance(payload, dict):
            raise ValueError("Expected app registry response object.")
        self._validator.validate("registry_response", payload)
        return payload


class AsyncAppRegistryService:
    """Async operations for the Incident IQ app registry endpoint."""

    def __init__(self, client: _AsyncRequestClient, validator: AppSchemaValidator) -> None:
        self._client = client
        self._validator = validator

    async def list_apps(
        self, *, include_hidden: bool = False, timeout: float | None = None
    ) -> AppRegistryResponse:
        payload = await self.list_apps_raw(include_hidden=include_hidden, timeout=timeout)
        if not isinstance(payload, dict):
            raise ValueError("Expected app registry response object.")
        return AppRegistryResponse.model_validate(payload)

    async def list_apps_raw(
        self, *, include_hidden: bool = False, timeout: float | None = None
    ) -> dict[str, Any] | None:
        path = f"/api/v1.0/app-registry/apps/{str(include_hidden).lower()}"
        payload = await self._client.request(
            "GET",
            _absolute_app_url(self._client.config.base_url, path),
            headers=_app_headers(self._client.config),
            timeout=timeout,
        )
        if payload is None:
            return None
        if not isinstance(payload, dict):
            raise ValueError("Expected app registry response object.")
        self._validator.validate("registry_response", payload)
        return payload


class MicrosoftIntuneService:
    """Microsoft Intune app-path operations and ownership helpers."""

    _lookup_path = "/apps/microsoftIntune/api/microsoftIntune/data/assets/lookup"
    _remote_actions_path = "/apps/microsoftIntune/api/microsoftIntune/remoteactions"

    def __init__(self, client: _SyncRequestClient, validator: AppSchemaValidator) -> None:
        self._client = client
        self._validator = validator

    def lookup_asset(
        self,
        *,
        asset_id: str,
        serial_number: str,
        asset_tag: str | None = None,
        timeout: float | None = None,
    ) -> AppLookupResponse | None:
        payload = self.lookup_asset_raw(
            asset_id=asset_id,
            serial_number=serial_number,
            asset_tag=asset_tag,
            timeout=timeout,
        )
        if payload is None:
            return None
        return AppLookupResponse.model_validate(payload)

    def lookup_asset_raw(
        self,
        *,
        asset_id: str,
        serial_number: str,
        asset_tag: str | None = None,
        timeout: float | None = None,
    ) -> dict[str, Any] | None:
        request_model = IntuneLookupRequest(
            AssetId=asset_id,
            AssetTag=asset_tag,
            SerialNumber=serial_number,
        )
        request_payload = request_model.model_dump(by_alias=True)
        self._validator.validate("intune_lookup_request", request_payload)

        payload = self._client.request(
            "POST",
            _absolute_app_url(self._client.config.base_url, self._lookup_path),
            json=request_payload,
            headers=_app_headers(self._client.config),
            timeout=timeout,
        )
        if payload is None:
            return None
        if not isinstance(payload, dict):
            raise ValueError("Expected Intune lookup response object.")
        self._validator.validate("lookup_response", payload)
        return payload

    def list_remote_actions(self, *, timeout: float | None = None) -> list[AppRemoteAction]:
        payload = self.list_remote_actions_raw(timeout=timeout)
        return [AppRemoteAction.model_validate(item) for item in payload]

    def list_remote_actions_raw(self, *, timeout: float | None = None) -> list[dict[str, Any]]:
        payload = self._client.request(
            "GET",
            _absolute_app_url(self._client.config.base_url, self._remote_actions_path),
            headers=_app_headers(self._client.config),
            timeout=timeout,
        )
        if not isinstance(payload, list):
            raise ValueError("Expected Intune remote actions response list.")
        self._validator.validate("remote_actions_response", payload)
        return [item for item in payload if isinstance(item, dict)]

    def classify_owner_type_from_lookup(
        self,
        lookup_response: AppLookupResponse | Mapping[str, Any],
        *,
        expected_external_id: str | None = None,
    ) -> IntuneOwnerClassification:
        lookup_model = (
            lookup_response
            if isinstance(lookup_response, AppLookupResponse)
            else AppLookupResponse.model_validate(lookup_response)
        )
        owner_value = lookup_model.custom_fields.get("ManagedDeviceOwnerType")
        owner_type = _normalize_owner_type(owner_value)

        external_id_matches = (
            True if expected_external_id is None else lookup_model.external_id == expected_external_id
        )
        return IntuneOwnerClassification(
            owner_type=owner_type,
            external_id_matches=external_id_matches,
        )

    def partition_assets_by_owner_type(
        self,
        *,
        assets: Sequence[Mapping[str, Any]],
        timeout: float | None = None,
    ) -> IntuneOwnershipPartition:
        company: list[dict[str, Any]] = []
        personal: list[dict[str, Any]] = []
        unknown: list[dict[str, Any]] = []

        for asset in assets:
            normalized = dict(asset)
            app_id = _extract_mapping_app_id(normalized)
            if app_id != "microsoftIntune":
                continue

            asset_id = normalized.get("AssetId")
            serial_number = normalized.get("SerialNumber")
            if not isinstance(asset_id, str) or not isinstance(serial_number, str):
                normalized["OwnerType"] = OwnerType.UNKNOWN.value
                unknown.append(normalized)
                continue

            external_id = _extract_external_id_lookup(normalized)
            asset_tag = normalized.get("AssetTag")
            lookup = self.lookup_asset(
                asset_id=asset_id,
                serial_number=serial_number,
                asset_tag=asset_tag if isinstance(asset_tag, str) else None,
                timeout=timeout,
            )
            if lookup is None:
                normalized["OwnerType"] = OwnerType.UNKNOWN.value
                unknown.append(normalized)
                continue

            classification = self.classify_owner_type_from_lookup(
                lookup,
                expected_external_id=external_id,
            )
            normalized["OwnerType"] = classification.owner_type
            normalized["ExternalIdMatches"] = classification.external_id_matches

            if not classification.external_id_matches:
                unknown.append(normalized)
            elif classification.owner_type == OwnerType.COMPANY.value:
                company.append(normalized)
            elif classification.owner_type == OwnerType.PERSONAL.value:
                personal.append(normalized)
            else:
                unknown.append(normalized)

        return IntuneOwnershipPartition(
            company=company,
            personal=personal,
            unknown=unknown,
        )


class AsyncMicrosoftIntuneService:
    """Async Microsoft Intune app-path operations and ownership helpers."""

    _lookup_path = "/apps/microsoftIntune/api/microsoftIntune/data/assets/lookup"
    _remote_actions_path = "/apps/microsoftIntune/api/microsoftIntune/remoteactions"

    def __init__(self, client: _AsyncRequestClient, validator: AppSchemaValidator) -> None:
        self._client = client
        self._validator = validator

    async def lookup_asset(
        self,
        *,
        asset_id: str,
        serial_number: str,
        asset_tag: str | None = None,
        timeout: float | None = None,
    ) -> AppLookupResponse | None:
        payload = await self.lookup_asset_raw(
            asset_id=asset_id,
            serial_number=serial_number,
            asset_tag=asset_tag,
            timeout=timeout,
        )
        if payload is None:
            return None
        return AppLookupResponse.model_validate(payload)

    async def lookup_asset_raw(
        self,
        *,
        asset_id: str,
        serial_number: str,
        asset_tag: str | None = None,
        timeout: float | None = None,
    ) -> dict[str, Any] | None:
        request_model = IntuneLookupRequest(
            AssetId=asset_id,
            AssetTag=asset_tag,
            SerialNumber=serial_number,
        )
        request_payload = request_model.model_dump(by_alias=True)
        self._validator.validate("intune_lookup_request", request_payload)

        payload = await self._client.request(
            "POST",
            _absolute_app_url(self._client.config.base_url, self._lookup_path),
            json=request_payload,
            headers=_app_headers(self._client.config),
            timeout=timeout,
        )
        if payload is None:
            return None
        if not isinstance(payload, dict):
            raise ValueError("Expected Intune lookup response object.")
        self._validator.validate("lookup_response", payload)
        return payload

    async def list_remote_actions(self, *, timeout: float | None = None) -> list[AppRemoteAction]:
        payload = await self.list_remote_actions_raw(timeout=timeout)
        return [AppRemoteAction.model_validate(item) for item in payload]

    async def list_remote_actions_raw(self, *, timeout: float | None = None) -> list[dict[str, Any]]:
        payload = await self._client.request(
            "GET",
            _absolute_app_url(self._client.config.base_url, self._remote_actions_path),
            headers=_app_headers(self._client.config),
            timeout=timeout,
        )
        if not isinstance(payload, list):
            raise ValueError("Expected Intune remote actions response list.")
        self._validator.validate("remote_actions_response", payload)
        return [item for item in payload if isinstance(item, dict)]

    def classify_owner_type_from_lookup(
        self,
        lookup_response: AppLookupResponse | Mapping[str, Any],
        *,
        expected_external_id: str | None = None,
    ) -> IntuneOwnerClassification:
        lookup_model = (
            lookup_response
            if isinstance(lookup_response, AppLookupResponse)
            else AppLookupResponse.model_validate(lookup_response)
        )
        owner_value = lookup_model.custom_fields.get("ManagedDeviceOwnerType")
        owner_type = _normalize_owner_type(owner_value)

        external_id_matches = (
            True if expected_external_id is None else lookup_model.external_id == expected_external_id
        )
        return IntuneOwnerClassification(
            owner_type=owner_type,
            external_id_matches=external_id_matches,
        )

    async def partition_assets_by_owner_type(
        self,
        *,
        assets: Sequence[Mapping[str, Any]],
        timeout: float | None = None,
    ) -> IntuneOwnershipPartition:
        company: list[dict[str, Any]] = []
        personal: list[dict[str, Any]] = []
        unknown: list[dict[str, Any]] = []

        for asset in assets:
            normalized = dict(asset)
            app_id = _extract_mapping_app_id(normalized)
            if app_id != "microsoftIntune":
                continue

            asset_id = normalized.get("AssetId")
            serial_number = normalized.get("SerialNumber")
            if not isinstance(asset_id, str) or not isinstance(serial_number, str):
                normalized["OwnerType"] = OwnerType.UNKNOWN.value
                unknown.append(normalized)
                continue

            external_id = _extract_external_id_lookup(normalized)
            asset_tag = normalized.get("AssetTag")
            lookup = await self.lookup_asset(
                asset_id=asset_id,
                serial_number=serial_number,
                asset_tag=asset_tag if isinstance(asset_tag, str) else None,
                timeout=timeout,
            )
            if lookup is None:
                normalized["OwnerType"] = OwnerType.UNKNOWN.value
                unknown.append(normalized)
                continue

            classification = self.classify_owner_type_from_lookup(
                lookup,
                expected_external_id=external_id,
            )
            normalized["OwnerType"] = classification.owner_type
            normalized["ExternalIdMatches"] = classification.external_id_matches

            if not classification.external_id_matches:
                unknown.append(normalized)
            elif classification.owner_type == OwnerType.COMPANY.value:
                company.append(normalized)
            elif classification.owner_type == OwnerType.PERSONAL.value:
                personal.append(normalized)
            else:
                unknown.append(normalized)

        return IntuneOwnershipPartition(
            company=company,
            personal=personal,
            unknown=unknown,
        )


class MosyleService:
    """Mosyle Manager app-path operations."""

    _lookup_path = "/apps/mosyleManager/api/mosyleManager/data/assets/lookup"
    _remote_actions_path = "/apps/mosyleManager/api/mosyleManager/remoteactions"

    def __init__(self, client: _SyncRequestClient, validator: AppSchemaValidator) -> None:
        self._client = client
        self._validator = validator

    def lookup_asset(
        self,
        *,
        asset_id: str,
        serial_number: str,
        asset_tag: str | None = None,
        timeout: float | None = None,
    ) -> AppLookupResponse | None:
        payload = self.lookup_asset_raw(
            asset_id=asset_id,
            serial_number=serial_number,
            asset_tag=asset_tag,
            timeout=timeout,
        )
        if payload is None:
            return None
        return AppLookupResponse.model_validate(payload)

    def lookup_asset_raw(
        self,
        *,
        asset_id: str,
        serial_number: str,
        asset_tag: str | None = None,
        timeout: float | None = None,
    ) -> dict[str, Any] | None:
        request_model = MosyleLookupRequest(
            AssetId=asset_id,
            AssetTag=asset_tag,
            SerialNumber=serial_number,
        )
        request_payload = request_model.model_dump(by_alias=True)
        self._validator.validate("mosyle_lookup_request", request_payload)

        payload = self._client.request(
            "POST",
            _absolute_app_url(self._client.config.base_url, self._lookup_path),
            json=request_payload,
            headers=_app_headers(self._client.config),
            timeout=timeout,
        )
        if payload is None:
            return None
        if not isinstance(payload, dict):
            raise ValueError("Expected Mosyle lookup response object.")
        self._validator.validate("lookup_response", payload)
        return payload

    def list_remote_actions(self, *, timeout: float | None = None) -> list[AppRemoteAction]:
        payload = self.list_remote_actions_raw(timeout=timeout)
        return [AppRemoteAction.model_validate(item) for item in payload]

    def list_remote_actions_raw(self, *, timeout: float | None = None) -> list[dict[str, Any]]:
        payload = self._client.request(
            "GET",
            _absolute_app_url(self._client.config.base_url, self._remote_actions_path),
            headers=_app_headers(self._client.config),
            timeout=timeout,
        )
        if not isinstance(payload, list):
            raise ValueError("Expected Mosyle remote actions response list.")
        self._validator.validate("remote_actions_response", payload)
        return [item for item in payload if isinstance(item, dict)]


class AsyncMosyleService:
    """Async Mosyle Manager app-path operations."""

    _lookup_path = "/apps/mosyleManager/api/mosyleManager/data/assets/lookup"
    _remote_actions_path = "/apps/mosyleManager/api/mosyleManager/remoteactions"

    def __init__(self, client: _AsyncRequestClient, validator: AppSchemaValidator) -> None:
        self._client = client
        self._validator = validator

    async def lookup_asset(
        self,
        *,
        asset_id: str,
        serial_number: str,
        asset_tag: str | None = None,
        timeout: float | None = None,
    ) -> AppLookupResponse | None:
        payload = await self.lookup_asset_raw(
            asset_id=asset_id,
            serial_number=serial_number,
            asset_tag=asset_tag,
            timeout=timeout,
        )
        if payload is None:
            return None
        return AppLookupResponse.model_validate(payload)

    async def lookup_asset_raw(
        self,
        *,
        asset_id: str,
        serial_number: str,
        asset_tag: str | None = None,
        timeout: float | None = None,
    ) -> dict[str, Any] | None:
        request_model = MosyleLookupRequest(
            AssetId=asset_id,
            AssetTag=asset_tag,
            SerialNumber=serial_number,
        )
        request_payload = request_model.model_dump(by_alias=True)
        self._validator.validate("mosyle_lookup_request", request_payload)

        payload = await self._client.request(
            "POST",
            _absolute_app_url(self._client.config.base_url, self._lookup_path),
            json=request_payload,
            headers=_app_headers(self._client.config),
            timeout=timeout,
        )
        if payload is None:
            return None
        if not isinstance(payload, dict):
            raise ValueError("Expected Mosyle lookup response object.")
        self._validator.validate("lookup_response", payload)
        return payload

    async def list_remote_actions(self, *, timeout: float | None = None) -> list[AppRemoteAction]:
        payload = await self.list_remote_actions_raw(timeout=timeout)
        return [AppRemoteAction.model_validate(item) for item in payload]

    async def list_remote_actions_raw(self, *, timeout: float | None = None) -> list[dict[str, Any]]:
        payload = await self._client.request(
            "GET",
            _absolute_app_url(self._client.config.base_url, self._remote_actions_path),
            headers=_app_headers(self._client.config),
            timeout=timeout,
        )
        if not isinstance(payload, list):
            raise ValueError("Expected Mosyle remote actions response list.")
        self._validator.validate("remote_actions_response", payload)
        return [item for item in payload if isinstance(item, dict)]


class GoogleDeviceDataService:
    """Google Device Data app-path operations."""

    _lookup_path = "/apps/googleDeviceData/api/googleDeviceData/data/assets/get-google-device"
    _remote_actions_path = "/apps/googleDeviceData/api/googleDeviceData/remoteactions"
    _sync_options_path = "/apps/googleDeviceData/api/googleDeviceData/sync/options"

    def __init__(self, client: _SyncRequestClient, validator: AppSchemaValidator) -> None:
        self._client = client
        self._validator = validator

    def lookup_asset(
        self,
        *,
        asset_id: str,
        serial_number: str,
        asset_tag: str | None = None,
        query: str | None = None,
        skip: int = 0,
        limit: int = 1,
        timeout: float | None = None,
    ) -> AppLookupResponse | None:
        payload = self.lookup_asset_raw(
            asset_id=asset_id,
            serial_number=serial_number,
            asset_tag=asset_tag,
            query=query,
            skip=skip,
            limit=limit,
            timeout=timeout,
        )
        if payload is None:
            return None
        return AppLookupResponse.model_validate(payload)

    def lookup_asset_raw(
        self,
        *,
        asset_id: str,
        serial_number: str,
        asset_tag: str | None = None,
        query: str | None = None,
        skip: int = 0,
        limit: int = 1,
        timeout: float | None = None,
    ) -> dict[str, Any] | None:
        request_model = GoogleDeviceLookupRequest(
            AssetId=asset_id,
            AssetTag=asset_tag,
            SerialNumber=serial_number,
            Query=query,
            Skip=skip,
            Limit=limit,
        )
        request_payload = request_model.model_dump(by_alias=True)
        self._validator.validate("google_lookup_request", request_payload)

        payload = self._client.request(
            "POST",
            _absolute_app_url(self._client.config.base_url, self._lookup_path),
            json=request_payload,
            headers=_app_headers(self._client.config),
            timeout=timeout,
        )
        if payload is None:
            return None
        if not isinstance(payload, dict):
            raise ValueError("Expected Google Device Data lookup response object.")
        self._validator.validate("lookup_response", payload)
        return payload

    def list_remote_actions(self, *, timeout: float | None = None) -> list[AppRemoteAction]:
        payload = self.list_remote_actions_raw(timeout=timeout)
        return [AppRemoteAction.model_validate(item) for item in payload]

    def list_remote_actions_raw(self, *, timeout: float | None = None) -> list[dict[str, Any]]:
        payload = self._client.request(
            "GET",
            _absolute_app_url(self._client.config.base_url, self._remote_actions_path),
            headers=_app_headers(self._client.config),
            timeout=timeout,
        )
        if not isinstance(payload, list):
            raise ValueError("Expected Google Device Data remote actions response list.")
        self._validator.validate("remote_actions_response", payload)
        return [item for item in payload if isinstance(item, dict)]

    def get_sync_options(self, *, timeout: float | None = None) -> GoogleSyncOptionsResponse:
        payload = self.get_sync_options_raw(timeout=timeout)
        if not isinstance(payload, dict):
            raise ValueError("Expected Google Device Data sync options object.")
        return GoogleSyncOptionsResponse.model_validate(payload)

    def get_sync_options_raw(self, *, timeout: float | None = None) -> dict[str, Any] | None:
        payload = self._client.request(
            "GET",
            _absolute_app_url(self._client.config.base_url, self._sync_options_path),
            headers=_app_headers(self._client.config),
            timeout=timeout,
        )
        if payload is None:
            return None
        if not isinstance(payload, dict):
            raise ValueError("Expected Google Device Data sync options object.")
        self._validator.validate("google_sync_options_response", payload)
        return payload


class AsyncGoogleDeviceDataService:
    """Async Google Device Data app-path operations."""

    _lookup_path = "/apps/googleDeviceData/api/googleDeviceData/data/assets/get-google-device"
    _remote_actions_path = "/apps/googleDeviceData/api/googleDeviceData/remoteactions"
    _sync_options_path = "/apps/googleDeviceData/api/googleDeviceData/sync/options"

    def __init__(self, client: _AsyncRequestClient, validator: AppSchemaValidator) -> None:
        self._client = client
        self._validator = validator

    async def lookup_asset(
        self,
        *,
        asset_id: str,
        serial_number: str,
        asset_tag: str | None = None,
        query: str | None = None,
        skip: int = 0,
        limit: int = 1,
        timeout: float | None = None,
    ) -> AppLookupResponse | None:
        payload = await self.lookup_asset_raw(
            asset_id=asset_id,
            serial_number=serial_number,
            asset_tag=asset_tag,
            query=query,
            skip=skip,
            limit=limit,
            timeout=timeout,
        )
        if payload is None:
            return None
        return AppLookupResponse.model_validate(payload)

    async def lookup_asset_raw(
        self,
        *,
        asset_id: str,
        serial_number: str,
        asset_tag: str | None = None,
        query: str | None = None,
        skip: int = 0,
        limit: int = 1,
        timeout: float | None = None,
    ) -> dict[str, Any] | None:
        request_model = GoogleDeviceLookupRequest(
            AssetId=asset_id,
            AssetTag=asset_tag,
            SerialNumber=serial_number,
            Query=query,
            Skip=skip,
            Limit=limit,
        )
        request_payload = request_model.model_dump(by_alias=True)
        self._validator.validate("google_lookup_request", request_payload)

        payload = await self._client.request(
            "POST",
            _absolute_app_url(self._client.config.base_url, self._lookup_path),
            json=request_payload,
            headers=_app_headers(self._client.config),
            timeout=timeout,
        )
        if payload is None:
            return None
        if not isinstance(payload, dict):
            raise ValueError("Expected Google Device Data lookup response object.")
        self._validator.validate("lookup_response", payload)
        return payload

    async def list_remote_actions(self, *, timeout: float | None = None) -> list[AppRemoteAction]:
        payload = await self.list_remote_actions_raw(timeout=timeout)
        return [AppRemoteAction.model_validate(item) for item in payload]

    async def list_remote_actions_raw(self, *, timeout: float | None = None) -> list[dict[str, Any]]:
        payload = await self._client.request(
            "GET",
            _absolute_app_url(self._client.config.base_url, self._remote_actions_path),
            headers=_app_headers(self._client.config),
            timeout=timeout,
        )
        if not isinstance(payload, list):
            raise ValueError("Expected Google Device Data remote actions response list.")
        self._validator.validate("remote_actions_response", payload)
        return [item for item in payload if isinstance(item, dict)]

    async def get_sync_options(self, *, timeout: float | None = None) -> GoogleSyncOptionsResponse:
        payload = await self.get_sync_options_raw(timeout=timeout)
        if not isinstance(payload, dict):
            raise ValueError("Expected Google Device Data sync options object.")
        return GoogleSyncOptionsResponse.model_validate(payload)

    async def get_sync_options_raw(self, *, timeout: float | None = None) -> dict[str, Any] | None:
        payload = await self._client.request(
            "GET",
            _absolute_app_url(self._client.config.base_url, self._sync_options_path),
            headers=_app_headers(self._client.config),
            timeout=timeout,
        )
        if payload is None:
            return None
        if not isinstance(payload, dict):
            raise ValueError("Expected Google Device Data sync options object.")
        self._validator.validate("google_sync_options_response", payload)
        return payload


class AppsNamespace:
    """Root namespace for undocumented app-path services on sync clients."""

    def __init__(self, client: _SyncRequestClient) -> None:
        validator = AppSchemaValidator()
        self.registry = AppRegistryService(client, validator)
        self.microsoft_intune = MicrosoftIntuneService(client, validator)
        self.mosyle = MosyleService(client, validator)
        self.google_device_data = GoogleDeviceDataService(client, validator)


class AsyncAppsNamespace:
    """Root namespace for undocumented app-path services on async clients."""

    def __init__(self, client: _AsyncRequestClient) -> None:
        validator = AppSchemaValidator()
        self.registry = AsyncAppRegistryService(client, validator)
        self.microsoft_intune = AsyncMicrosoftIntuneService(client, validator)
        self.mosyle = AsyncMosyleService(client, validator)
        self.google_device_data = AsyncGoogleDeviceDataService(client, validator)


def build_app_method_metadata() -> tuple[AppMethodMetadata, ...]:
    """Return stable documentation metadata for app-path services."""
    return (
        AppMethodMetadata(
            service_name="registry",
            service_label="App Registry",
            method_name="list_apps",
            summary="List registered tenant apps.",
            description=(
                "Calls the tenant app registry endpoint and returns the typed registry "
                "response envelope."
            ),
            sync_call="client.apps.registry.list_apps(include_hidden=False, timeout=None)",
            async_call="await client.apps.registry.list_apps(include_hidden=False, timeout=None)",
            http_method="GET",
            route="/api/v1.0/app-registry/apps/{include_hidden}",
            parameters=(
                AppParameterMetadata(
                    "include_hidden",
                    "include_hidden",
                    "path",
                    False,
                    "bool",
                    "Whether to include hidden app registrations.",
                ),
            ),
            typed_return="AppRegistryResponse",
            raw_return="dict[str, Any] | None",
            response_model="AppRegistryResponse",
            response_schema="registry_response",
        ),
        AppMethodMetadata(
            service_name="registry",
            service_label="App Registry",
            method_name="list_apps_raw",
            summary="List registered tenant apps and return raw JSON.",
            description="Same request as `list_apps`, but returns validated raw JSON.",
            sync_call="client.apps.registry.list_apps_raw(include_hidden=False, timeout=None)",
            async_call="await client.apps.registry.list_apps_raw(include_hidden=False, timeout=None)",
            http_method="GET",
            route="/api/v1.0/app-registry/apps/{include_hidden}",
            parameters=(
                AppParameterMetadata(
                    "include_hidden",
                    "include_hidden",
                    "path",
                    False,
                    "bool",
                    "Whether to include hidden app registrations.",
                ),
            ),
            typed_return="dict[str, Any] | None",
            raw_return="dict[str, Any] | None",
            response_schema="registry_response",
        ),
        AppMethodMetadata(
            service_name="microsoft_intune",
            service_label="Microsoft Intune",
            method_name="lookup_asset",
            summary="Look up an Incident IQ asset against Microsoft Intune.",
            description=(
                "Posts the asset lookup payload to the Intune app endpoint and returns the "
                "typed lookup response when available."
            ),
            sync_call=(
                "client.apps.microsoft_intune.lookup_asset("
                "asset_id=..., serial_number=..., asset_tag=None, timeout=None)"
            ),
            async_call=(
                "await client.apps.microsoft_intune.lookup_asset("
                "asset_id=..., serial_number=..., asset_tag=None, timeout=None)"
            ),
            http_method="POST",
            route="/apps/microsoftIntune/api/microsoftIntune/data/assets/lookup",
            parameters=(
                AppParameterMetadata("asset_id", "AssetId", "body", True, "str", "Incident IQ asset identifier."),
                AppParameterMetadata(
                    "serial_number",
                    "SerialNumber",
                    "body",
                    True,
                    "str",
                    "Serial number sent to the Intune lookup endpoint.",
                ),
                AppParameterMetadata("asset_tag", "AssetTag", "body", False, "str | None", "Optional asset tag."),
            ),
            typed_return="AppLookupResponse | None",
            raw_return="dict[str, Any] | None",
            response_model="AppLookupResponse",
            response_schema="lookup_response",
        ),
        AppMethodMetadata(
            service_name="microsoft_intune",
            service_label="Microsoft Intune",
            method_name="lookup_asset_raw",
            summary="Look up an asset against Microsoft Intune and return raw JSON.",
            description="Same request as `lookup_asset`, but returns validated raw JSON.",
            sync_call=(
                "client.apps.microsoft_intune.lookup_asset_raw("
                "asset_id=..., serial_number=..., asset_tag=None, timeout=None)"
            ),
            async_call=(
                "await client.apps.microsoft_intune.lookup_asset_raw("
                "asset_id=..., serial_number=..., asset_tag=None, timeout=None)"
            ),
            http_method="POST",
            route="/apps/microsoftIntune/api/microsoftIntune/data/assets/lookup",
            parameters=(
                AppParameterMetadata("asset_id", "AssetId", "body", True, "str", "Incident IQ asset identifier."),
                AppParameterMetadata(
                    "serial_number",
                    "SerialNumber",
                    "body",
                    True,
                    "str",
                    "Serial number sent to the Intune lookup endpoint.",
                ),
                AppParameterMetadata("asset_tag", "AssetTag", "body", False, "str | None", "Optional asset tag."),
            ),
            typed_return="dict[str, Any] | None",
            raw_return="dict[str, Any] | None",
            response_schema="lookup_response",
        ),
        AppMethodMetadata(
            service_name="microsoft_intune",
            service_label="Microsoft Intune",
            method_name="list_remote_actions",
            summary="List available Intune remote actions.",
            description="Calls the Intune remote actions endpoint and returns typed action records.",
            sync_call="client.apps.microsoft_intune.list_remote_actions(timeout=None)",
            async_call="await client.apps.microsoft_intune.list_remote_actions(timeout=None)",
            http_method="GET",
            route="/apps/microsoftIntune/api/microsoftIntune/remoteactions",
            parameters=(),
            typed_return="list[AppRemoteAction]",
            raw_return="list[dict[str, Any]]",
            response_model="AppRemoteAction",
            response_schema="remote_actions_response",
        ),
        AppMethodMetadata(
            service_name="microsoft_intune",
            service_label="Microsoft Intune",
            method_name="list_remote_actions_raw",
            summary="List available Intune remote actions and return raw JSON.",
            description="Same request as `list_remote_actions`, but returns validated raw JSON.",
            sync_call="client.apps.microsoft_intune.list_remote_actions_raw(timeout=None)",
            async_call="await client.apps.microsoft_intune.list_remote_actions_raw(timeout=None)",
            http_method="GET",
            route="/apps/microsoftIntune/api/microsoftIntune/remoteactions",
            parameters=(),
            typed_return="list[dict[str, Any]]",
            raw_return="list[dict[str, Any]]",
            response_schema="remote_actions_response",
        ),
        AppMethodMetadata(
            service_name="microsoft_intune",
            service_label="Microsoft Intune",
            method_name="classify_owner_type_from_lookup",
            summary="Classify Intune owner type from a lookup payload.",
            description=(
                "Utility helper that derives owner type and optional external-id match state "
                "from a lookup response; no HTTP request is made."
            ),
            sync_call=(
                "client.apps.microsoft_intune.classify_owner_type_from_lookup("
                "lookup_response=..., expected_external_id=None)"
            ),
            async_call=(
                "client.apps.microsoft_intune.classify_owner_type_from_lookup("
                "lookup_response=..., expected_external_id=None)"
            ),
            http_method=None,
            route=None,
            parameters=(
                AppParameterMetadata(
                    "lookup_response",
                    "lookup_response",
                    "python",
                    True,
                    "AppLookupResponse | Mapping[str, Any]",
                    "Lookup payload or model to classify.",
                ),
                AppParameterMetadata(
                    "expected_external_id",
                    "expected_external_id",
                    "python",
                    False,
                    "str | None",
                    "Optional external id used to flag mismatches.",
                ),
            ),
            typed_return="IntuneOwnerClassification",
            raw_return="IntuneOwnerClassification",
            response_model="IntuneOwnerClassification",
        ),
        AppMethodMetadata(
            service_name="microsoft_intune",
            service_label="Microsoft Intune",
            method_name="partition_assets_by_owner_type",
            summary="Partition Intune-linked assets by owner type.",
            description=(
                "Utility helper that performs lookups as needed and groups assets into "
                "company, personal, and unknown partitions."
            ),
            sync_call=(
                "client.apps.microsoft_intune.partition_assets_by_owner_type("
                "assets=..., timeout=None)"
            ),
            async_call=(
                "await client.apps.microsoft_intune.partition_assets_by_owner_type("
                "assets=..., timeout=None)"
            ),
            http_method=None,
            route=None,
            parameters=(
                AppParameterMetadata(
                    "assets",
                    "assets",
                    "python",
                    True,
                    "Sequence[Mapping[str, Any]]",
                    "Asset payloads containing Intune app mapping data.",
                ),
            ),
            typed_return="IntuneOwnershipPartition",
            raw_return="IntuneOwnershipPartition",
            response_model="IntuneOwnershipPartition",
        ),
        AppMethodMetadata(
            service_name="mosyle",
            service_label="Mosyle",
            method_name="lookup_asset",
            summary="Look up an Incident IQ asset against Mosyle.",
            description="Posts the asset lookup payload to the Mosyle app endpoint.",
            sync_call=(
                "client.apps.mosyle.lookup_asset("
                "asset_id=..., serial_number=..., asset_tag=None, timeout=None)"
            ),
            async_call=(
                "await client.apps.mosyle.lookup_asset("
                "asset_id=..., serial_number=..., asset_tag=None, timeout=None)"
            ),
            http_method="POST",
            route="/apps/mosyleManager/api/mosyleManager/data/assets/lookup",
            parameters=(
                AppParameterMetadata("asset_id", "AssetId", "body", True, "str", "Incident IQ asset identifier."),
                AppParameterMetadata("serial_number", "SerialNumber", "body", True, "str", "Serial number."),
                AppParameterMetadata("asset_tag", "AssetTag", "body", False, "str | None", "Optional asset tag."),
            ),
            typed_return="AppLookupResponse | None",
            raw_return="dict[str, Any] | None",
            response_model="AppLookupResponse",
            response_schema="lookup_response",
        ),
        AppMethodMetadata(
            service_name="mosyle",
            service_label="Mosyle",
            method_name="lookup_asset_raw",
            summary="Look up an asset against Mosyle and return raw JSON.",
            description="Same request as `lookup_asset`, but returns validated raw JSON.",
            sync_call=(
                "client.apps.mosyle.lookup_asset_raw("
                "asset_id=..., serial_number=..., asset_tag=None, timeout=None)"
            ),
            async_call=(
                "await client.apps.mosyle.lookup_asset_raw("
                "asset_id=..., serial_number=..., asset_tag=None, timeout=None)"
            ),
            http_method="POST",
            route="/apps/mosyleManager/api/mosyleManager/data/assets/lookup",
            parameters=(
                AppParameterMetadata("asset_id", "AssetId", "body", True, "str", "Incident IQ asset identifier."),
                AppParameterMetadata("serial_number", "SerialNumber", "body", True, "str", "Serial number."),
                AppParameterMetadata("asset_tag", "AssetTag", "body", False, "str | None", "Optional asset tag."),
            ),
            typed_return="dict[str, Any] | None",
            raw_return="dict[str, Any] | None",
            response_schema="lookup_response",
        ),
        AppMethodMetadata(
            service_name="mosyle",
            service_label="Mosyle",
            method_name="list_remote_actions",
            summary="List available Mosyle remote actions.",
            description="Calls the Mosyle remote actions endpoint and returns typed action records.",
            sync_call="client.apps.mosyle.list_remote_actions(timeout=None)",
            async_call="await client.apps.mosyle.list_remote_actions(timeout=None)",
            http_method="GET",
            route="/apps/mosyleManager/api/mosyleManager/remoteactions",
            parameters=(),
            typed_return="list[AppRemoteAction]",
            raw_return="list[dict[str, Any]]",
            response_model="AppRemoteAction",
            response_schema="remote_actions_response",
        ),
        AppMethodMetadata(
            service_name="mosyle",
            service_label="Mosyle",
            method_name="list_remote_actions_raw",
            summary="List available Mosyle remote actions and return raw JSON.",
            description="Same request as `list_remote_actions`, but returns validated raw JSON.",
            sync_call="client.apps.mosyle.list_remote_actions_raw(timeout=None)",
            async_call="await client.apps.mosyle.list_remote_actions_raw(timeout=None)",
            http_method="GET",
            route="/apps/mosyleManager/api/mosyleManager/remoteactions",
            parameters=(),
            typed_return="list[dict[str, Any]]",
            raw_return="list[dict[str, Any]]",
            response_schema="remote_actions_response",
        ),
        AppMethodMetadata(
            service_name="google_device_data",
            service_label="Google Device Data",
            method_name="lookup_asset",
            summary="Look up an Incident IQ asset against Google Device Data.",
            description="Posts the asset lookup payload to the Google Device Data endpoint.",
            sync_call=(
                "client.apps.google_device_data.lookup_asset("
                "asset_id=..., serial_number=..., asset_tag=None, query=None, skip=0, limit=1, timeout=None)"
            ),
            async_call=(
                "await client.apps.google_device_data.lookup_asset("
                "asset_id=..., serial_number=..., asset_tag=None, query=None, skip=0, limit=1, timeout=None)"
            ),
            http_method="POST",
            route="/apps/googleDeviceData/api/googleDeviceData/data/assets/get-google-device",
            parameters=(
                AppParameterMetadata("asset_id", "AssetId", "body", True, "str", "Incident IQ asset identifier."),
                AppParameterMetadata("serial_number", "SerialNumber", "body", True, "str", "Serial number."),
                AppParameterMetadata("asset_tag", "AssetTag", "body", False, "str | None", "Optional asset tag."),
                AppParameterMetadata("query", "Query", "body", False, "str | None", "Optional search query."),
                AppParameterMetadata("skip", "Skip", "body", False, "int", "Result offset for the Google endpoint."),
                AppParameterMetadata("limit", "Limit", "body", False, "int", "Maximum results requested."),
            ),
            typed_return="AppLookupResponse | None",
            raw_return="dict[str, Any] | None",
            response_model="AppLookupResponse",
            response_schema="lookup_response",
        ),
        AppMethodMetadata(
            service_name="google_device_data",
            service_label="Google Device Data",
            method_name="lookup_asset_raw",
            summary="Look up an asset against Google Device Data and return raw JSON.",
            description="Same request as `lookup_asset`, but returns validated raw JSON.",
            sync_call=(
                "client.apps.google_device_data.lookup_asset_raw("
                "asset_id=..., serial_number=..., asset_tag=None, query=None, skip=0, limit=1, timeout=None)"
            ),
            async_call=(
                "await client.apps.google_device_data.lookup_asset_raw("
                "asset_id=..., serial_number=..., asset_tag=None, query=None, skip=0, limit=1, timeout=None)"
            ),
            http_method="POST",
            route="/apps/googleDeviceData/api/googleDeviceData/data/assets/get-google-device",
            parameters=(
                AppParameterMetadata("asset_id", "AssetId", "body", True, "str", "Incident IQ asset identifier."),
                AppParameterMetadata("serial_number", "SerialNumber", "body", True, "str", "Serial number."),
                AppParameterMetadata("asset_tag", "AssetTag", "body", False, "str | None", "Optional asset tag."),
                AppParameterMetadata("query", "Query", "body", False, "str | None", "Optional search query."),
                AppParameterMetadata("skip", "Skip", "body", False, "int", "Result offset for the Google endpoint."),
                AppParameterMetadata("limit", "Limit", "body", False, "int", "Maximum results requested."),
            ),
            typed_return="dict[str, Any] | None",
            raw_return="dict[str, Any] | None",
            response_schema="lookup_response",
        ),
        AppMethodMetadata(
            service_name="google_device_data",
            service_label="Google Device Data",
            method_name="list_remote_actions",
            summary="List available Google Device Data remote actions.",
            description="Calls the Google Device Data remote actions endpoint and returns typed action records.",
            sync_call="client.apps.google_device_data.list_remote_actions(timeout=None)",
            async_call="await client.apps.google_device_data.list_remote_actions(timeout=None)",
            http_method="GET",
            route="/apps/googleDeviceData/api/googleDeviceData/remoteactions",
            parameters=(),
            typed_return="list[AppRemoteAction]",
            raw_return="list[dict[str, Any]]",
            response_model="AppRemoteAction",
            response_schema="remote_actions_response",
        ),
        AppMethodMetadata(
            service_name="google_device_data",
            service_label="Google Device Data",
            method_name="list_remote_actions_raw",
            summary="List available Google Device Data remote actions and return raw JSON.",
            description="Same request as `list_remote_actions`, but returns validated raw JSON.",
            sync_call="client.apps.google_device_data.list_remote_actions_raw(timeout=None)",
            async_call="await client.apps.google_device_data.list_remote_actions_raw(timeout=None)",
            http_method="GET",
            route="/apps/googleDeviceData/api/googleDeviceData/remoteactions",
            parameters=(),
            typed_return="list[dict[str, Any]]",
            raw_return="list[dict[str, Any]]",
            response_schema="remote_actions_response",
        ),
        AppMethodMetadata(
            service_name="google_device_data",
            service_label="Google Device Data",
            method_name="get_sync_options",
            summary="Fetch Google Device Data sync options.",
            description="Calls the sync options endpoint and returns the typed options model.",
            sync_call="client.apps.google_device_data.get_sync_options(timeout=None)",
            async_call="await client.apps.google_device_data.get_sync_options(timeout=None)",
            http_method="GET",
            route="/apps/googleDeviceData/api/googleDeviceData/sync/options",
            parameters=(),
            typed_return="GoogleSyncOptionsResponse",
            raw_return="dict[str, Any] | None",
            response_model="GoogleSyncOptionsResponse",
            response_schema="google_sync_options_response",
        ),
        AppMethodMetadata(
            service_name="google_device_data",
            service_label="Google Device Data",
            method_name="get_sync_options_raw",
            summary="Fetch Google Device Data sync options and return raw JSON.",
            description="Same request as `get_sync_options`, but returns validated raw JSON.",
            sync_call="client.apps.google_device_data.get_sync_options_raw(timeout=None)",
            async_call="await client.apps.google_device_data.get_sync_options_raw(timeout=None)",
            http_method="GET",
            route="/apps/googleDeviceData/api/googleDeviceData/sync/options",
            parameters=(),
            typed_return="dict[str, Any] | None",
            raw_return="dict[str, Any] | None",
            response_schema="google_sync_options_response",
        ),
    )


def _extract_mapping_app_id(asset: Mapping[str, Any]) -> str | None:
    mappings = asset.get("DataMappings")
    if not isinstance(mappings, Mapping):
        return None
    model = mappings.get("Model")
    if not isinstance(model, Mapping):
        return None
    app_id = model.get("AppId")
    return app_id if isinstance(app_id, str) else None


def _extract_external_id_lookup(asset: Mapping[str, Any]) -> str | None:
    mappings = asset.get("DataMappings")
    if not isinstance(mappings, Mapping):
        return None
    lookups = mappings.get("Lookups")
    if not isinstance(lookups, list):
        return None
    for lookup in lookups:
        if not isinstance(lookup, Mapping):
            continue
        if lookup.get("Key") == "ExternalId" and isinstance(lookup.get("Value"), str):
            return str(lookup["Value"])
    return None


def _normalize_owner_type(value: Any) -> Literal["Company", "Personal", "Unknown"]:
    if value == OwnerType.COMPANY.value:
        return OwnerType.COMPANY.value
    if value == OwnerType.PERSONAL.value:
        return OwnerType.PERSONAL.value
    return OwnerType.UNKNOWN.value
