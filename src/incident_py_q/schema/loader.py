"""Load bundled contract artifacts used by runtime validation and SDK generation."""

from __future__ import annotations

import json
from importlib.resources import files
from typing import Any, cast

from .openapi import convert_openapi_document


def load_openapi_document() -> dict[str, Any]:
    """Load the bundled Golden OpenAPI 3.0 contract document as published."""
    path = files("incident_py_q").joinpath("data/openapi/openapi-spec.json")
    loaded = json.loads(path.read_text(encoding="utf-8"))
    return cast(dict[str, Any], loaded)


def load_openapi_metadata() -> dict[str, Any]:
    """Load sync metadata describing the bundled Golden contract snapshot."""
    path = files("incident_py_q").joinpath("data/openapi/metadata.json")
    loaded = json.loads(path.read_text(encoding="utf-8"))
    return cast(dict[str, Any], loaded)


def load_contract_documents() -> list[dict[str, Any]]:
    """Load Golden contract documents in the SDK's internal Swagger-shaped form."""
    return [convert_openapi_document(load_openapi_document())]


def load_legacy_contract_document() -> dict[str, Any]:
    """Load the pruned legacy contract for routes migrated onto the Silver surface.

    The published Golden contract is a locked allowlist profile and stopped
    documenting a set of routes the SDK previously exposed. Those routes moved to
    Silver rather than being dropped, and this bundle keeps their Swagger 2.0
    schemas so they retain strict response validation.
    """
    path = files("incident_py_q").joinpath("data/legacy/contract.json")
    loaded = json.loads(path.read_text(encoding="utf-8"))
    return cast(dict[str, Any], loaded)


def load_legacy_aliases() -> dict[str, Any]:
    """Load the deprecated alias map from the Golden OpenAPI migration."""
    path = files("incident_py_q").joinpath("data/legacy/aliases.json")
    loaded = json.loads(path.read_text(encoding="utf-8"))
    return cast(dict[str, Any], loaded)


def load_source_manifest() -> dict[str, Any]:
    """Load schema source metadata used by sync tooling."""
    path = files("incident_py_q").joinpath("data/source_manifest.json")
    loaded = json.loads(path.read_text(encoding="utf-8"))
    return cast(dict[str, Any], loaded)


def load_app_schemas() -> dict[str, Any]:
    """Load bundled undocumented app-path JSON schemas."""
    path = files("incident_py_q").joinpath("data/app_schemas.json")
    loaded = json.loads(path.read_text(encoding="utf-8"))
    return cast(dict[str, Any], loaded)


def load_silver_inventory() -> dict[str, Any]:
    """Load bundled HAR-derived Silver inventory metadata."""
    path = files("incident_py_q").joinpath("data/silver_inventory.json")
    loaded = json.loads(path.read_text(encoding="utf-8"))
    return cast(dict[str, Any], loaded)
