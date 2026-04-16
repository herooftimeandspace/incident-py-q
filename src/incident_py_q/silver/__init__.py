"""Explicit Silver-path runtime and inventory support."""

from .inventory import (
    SilverMethodMetadata,
    SilverParameterMetadata,
    extract_silver_inventory,
    legacy_app_inventory_records,
    load_silver_inventory,
    silver_inventory_payload,
    silver_inventory_records,
)
from .runtime import (
    AsyncSilverAppsNamespace,
    SilverAppsNamespace,
    SilverArtifacts,
    SilverGenericNamespace,
    SilverRootNamespace,
    build_silver_metadata,
    build_silver_sdk,
    format_silver_docstring,
)

__all__ = [
    "AsyncSilverAppsNamespace",
    "SilverAppsNamespace",
    "SilverArtifacts",
    "SilverGenericNamespace",
    "SilverMethodMetadata",
    "SilverParameterMetadata",
    "SilverRootNamespace",
    "build_silver_metadata",
    "build_silver_sdk",
    "extract_silver_inventory",
    "format_silver_docstring",
    "legacy_app_inventory_records",
    "load_silver_inventory",
    "silver_inventory_payload",
    "silver_inventory_records",
]
