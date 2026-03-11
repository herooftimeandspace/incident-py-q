"""Contract checks against the bundled APIHub Postman collection."""

from __future__ import annotations

from collections.abc import Iterator
from typing import Any
from urllib.parse import urlparse

from incident_py_q.schema.loader import load_postman_collection, load_stoplight_documents
from incident_py_q.schema.registry import build_schema_registry


def _iter_postman_requests(items: list[dict[str, Any]]) -> Iterator[dict[str, Any]]:
    for item in items:
        nested = item.get("item")
        if isinstance(nested, list):
            yield from _iter_postman_requests([entry for entry in nested if isinstance(entry, dict)])
            continue
        request = item.get("request")
        if isinstance(request, dict):
            yield request


def _normalize_postman_path(url_value: Any) -> str | None:
    raw_path: str | None = None
    if isinstance(url_value, str):
        raw_path = urlparse(url_value).path
    elif isinstance(url_value, dict):
        raw = url_value.get("raw")
        if isinstance(raw, str):
            raw_path = urlparse(raw).path
        else:
            path = url_value.get("path")
            if isinstance(path, list):
                raw_path = "/" + "/".join(str(part) for part in path)
            elif isinstance(path, str):
                raw_path = path

    if not raw_path:
        return None

    normalized = raw_path
    for prefix in ("/api/v1.0", "/api/v1", "/v1.0", "/v1"):
        if normalized.startswith(prefix + "/"):
            normalized = normalized[len(prefix) :]
            break
    return normalized.rstrip("/") or "/"


def test_postman_collection_has_requests() -> None:
    postman = load_postman_collection()
    requests = list(_iter_postman_requests(postman.get("item", [])))
    assert requests
    assert all(isinstance(request.get("method"), str) for request in requests)


def test_postman_collection_has_path_overlap_with_stoplight_contract() -> None:
    postman = load_postman_collection()
    registry = build_schema_registry(load_stoplight_documents())

    postman_pairs: set[tuple[str, str]] = set()
    for request in _iter_postman_requests(postman.get("item", [])):
        method = request.get("method")
        path = _normalize_postman_path(request.get("url"))
        if isinstance(method, str) and path:
            postman_pairs.add((method.upper(), path))

    registry_pairs = {(operation.method, operation.path_template) for operation in registry.operations}
    overlap = postman_pairs.intersection(registry_pairs)
    assert overlap
