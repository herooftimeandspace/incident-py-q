"""Load bundled contract artifacts used by runtime validation and SDK generation."""

from __future__ import annotations

import json
from importlib.resources import files
from typing import Any, cast


def load_stoplight_documents() -> list[dict[str, Any]]:
    """Load bundled Stoplight Swagger controller documents."""
    root = files("incident_py_q").joinpath("data/stoplight/controllers")
    documents: list[dict[str, Any]] = []
    for entry in sorted(root.iterdir(), key=lambda item: item.name):
        if not entry.name.endswith(".json"):
            continue
        documents.append(json.loads(entry.read_text(encoding="utf-8")))
    return documents


def load_postman_collection() -> dict[str, Any]:
    """Load the bundled APIHub Postman collection document."""
    path = files("incident_py_q").joinpath("data/postman/collection.json")
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
