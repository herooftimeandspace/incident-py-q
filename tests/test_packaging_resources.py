"""Tests ensuring bundled contract assets are importable from package resources."""

from __future__ import annotations

from importlib.resources import files

from incident_py_q.schema.loader import (
    load_postman_collection,
    load_source_manifest,
    load_stoplight_documents,
)


def test_bundled_contract_assets_load() -> None:
    stoplight_docs = load_stoplight_documents()
    postman = load_postman_collection()
    manifest = load_source_manifest()

    assert stoplight_docs
    assert "item" in postman
    assert "sources" in manifest


def test_bundled_controller_files_exist() -> None:
    controllers_dir = files("incident_py_q").joinpath("data/stoplight/controllers")
    controller_names = sorted(path.name for path in controllers_dir.iterdir() if path.name.endswith(".json"))
    assert controller_names
    assert "Tickets.json" in controller_names
