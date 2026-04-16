"""Typed request and response models for app-path Incident IQ endpoints."""

from __future__ import annotations

from enum import StrEnum
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class AppRegistryItem(BaseModel):
    """Single app item returned by the app registry endpoint."""

    model_config = ConfigDict(extra="allow")

    app_id: str = Field(alias="AppId")
    name: str = Field(alias="Name")
    is_active: bool = Field(alias="IsActive")
    settings: dict[str, Any] = Field(alias="Settings", default_factory=dict)


class AppRegistryResponse(BaseModel):
    """Envelope response for app registry listing."""

    model_config = ConfigDict(extra="allow")

    items: list[AppRegistryItem] = Field(alias="Items", default_factory=list)
    item_count: int = Field(alias="ItemCount")
    status_code: int = Field(alias="StatusCode")


class AppRemoteAction(BaseModel):
    """Remote action descriptor for app-integrated device actions."""

    model_config = ConfigDict(extra="allow")

    key: str = Field(alias="Key")
    permission_key: str = Field(alias="PermissionKey")


class IntuneLookupRequest(BaseModel):
    """Lookup payload for Microsoft Intune app endpoint."""

    model_config = ConfigDict(extra="forbid", populate_by_name=True)

    asset_id: str = Field(alias="AssetId")
    asset_tag: str | None = Field(alias="AssetTag", default=None)
    serial_number: str = Field(alias="SerialNumber")


class MosyleLookupRequest(BaseModel):
    """Lookup payload for Mosyle app endpoint."""

    model_config = ConfigDict(extra="forbid", populate_by_name=True)

    asset_id: str = Field(alias="AssetId")
    asset_tag: str | None = Field(alias="AssetTag", default=None)
    serial_number: str = Field(alias="SerialNumber")


class GoogleDeviceLookupRequest(BaseModel):
    """Lookup payload for Google Device Data endpoint."""

    model_config = ConfigDict(extra="forbid", populate_by_name=True)

    asset_id: str = Field(alias="AssetId")
    asset_tag: str | None = Field(alias="AssetTag", default=None)
    serial_number: str = Field(alias="SerialNumber")
    query: str | None = Field(alias="Query", default=None)
    skip: int = Field(alias="Skip", default=0)
    limit: int = Field(alias="Limit", default=1)


class AppLookupResponse(BaseModel):
    """Generic lookup response shape shared by Intune/Mosyle/Google app lookups."""

    model_config = ConfigDict(extra="allow")

    external_id: str = Field(alias="ExternalId")
    serial_number: str = Field(alias="SerialNumber")
    asset_tag: str | None = Field(alias="AssetTag", default=None)
    custom_fields: dict[str, Any] = Field(alias="CustomFields", default_factory=dict)


class OwnerType(StrEnum):
    """Owner classification labels used by Intune convenience helpers."""

    COMPANY = "Company"
    PERSONAL = "Personal"
    UNKNOWN = "Unknown"


class IntuneOwnerClassification(BaseModel):
    """Result object from owner-type classification helper methods."""

    model_config = ConfigDict(extra="forbid")

    owner_type: Literal["Company", "Personal", "Unknown"]
    external_id_matches: bool


class IntuneOwnershipPartition(BaseModel):
    """Partitioned asset groups by owner type."""

    model_config = ConfigDict(extra="forbid")

    company: list[dict[str, Any]]
    personal: list[dict[str, Any]]
    unknown: list[dict[str, Any]]


class GoogleSyncOptionsResponse(BaseModel):
    """Google Device Data sync options payload."""

    model_config = ConfigDict(extra="allow")

    id: str = Field(alias="Id")
    create_assets: bool = Field(alias="CreateAssets")
    update_assets: bool = Field(alias="UpdateAssets")
    delete_assets: bool = Field(alias="DeleteAssets")
