"""Tests ensuring bundled contract assets are importable from package resources."""

from __future__ import annotations

from importlib.resources import files

from incident_py_q.schema.loader import (
    load_app_schemas,
    load_contract_documents,
    load_openapi_document,
    load_openapi_metadata,
    load_silver_inventory,
    load_source_manifest,
)


def test_bundled_contract_assets_load() -> None:
    openapi_document = load_openapi_document()
    manifest = load_source_manifest()
    app_schemas = load_app_schemas()
    silver_inventory = load_silver_inventory()

    assert openapi_document["openapi"].startswith("3.")
    assert openapi_document["paths"]
    assert "golden_openapi" in manifest["sources"]
    assert "lookup_response" in app_schemas
    assert "endpoints" in silver_inventory


def test_bundled_openapi_spec_file_exists() -> None:
    openapi_dir = files("incident_py_q").joinpath("data/openapi")
    names = sorted(path.name for path in openapi_dir.iterdir() if path.name.endswith(".json"))
    assert names == ["metadata.json", "openapi-spec.json"]


def test_bundled_openapi_metadata_describes_snapshot() -> None:
    metadata = load_openapi_metadata()

    assert metadata["openapi_version"].startswith("3.")
    assert metadata["operation_count"] > 0
    assert metadata["spec_url"]
    assert metadata["synced_at"]


def test_contract_documents_convert_to_internal_shape() -> None:
    documents = load_contract_documents()

    assert len(documents) == 1
    document = documents[0]
    assert document["swagger"] == "2.0"
    assert document["definitions"]
    assert document["paths"]
