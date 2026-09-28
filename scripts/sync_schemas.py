#!/usr/bin/env python3
"""Sync the bundled Incident IQ Golden contract from the published OpenAPI spec.

The Golden path is the published Incident IQ API reference:
https://scopousiiq.github.io/iiq-docusaurus-docs/docs/api/

That documentation site is rendered from a single OpenAPI 3.0 document, which is
the machine-readable contract this script pulls. It supersedes the previous
Stoplight GraphQL controller sync and the APIHub Postman collection sync.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, cast

import httpx

HTTP_METHODS = ("get", "post", "put", "delete", "patch", "head", "options")


@dataclass(slots=True)
class SyncResult:
    source: str
    success: bool
    detail: str
    required: bool


def _read_manifest(path: Path) -> dict[str, Any]:
    loaded = json.loads(path.read_text(encoding="utf-8"))
    return cast(dict[str, Any], loaded)


def _fetch_json(url: str, timeout: float) -> dict[str, Any]:
    response = httpx.get(url, timeout=timeout, follow_redirects=True)
    response.raise_for_status()
    payload = response.json()
    if not isinstance(payload, dict):
        raise RuntimeError(f"Expected a JSON object from {url!r}, got {type(payload).__name__}.")
    return cast(dict[str, Any], payload)


def _validate_openapi_document(document: dict[str, Any]) -> tuple[int, int, int]:
    """Assert the payload is a usable OpenAPI 3 contract and summarize its size."""
    version = document.get("openapi")
    if not isinstance(version, str) or not version.startswith("3."):
        raise RuntimeError(f"Expected an OpenAPI 3.x document, got openapi={version!r}.")

    paths = document.get("paths")
    if not isinstance(paths, dict) or not paths:
        raise RuntimeError("OpenAPI document did not contain any paths.")

    operations = 0
    for path_item in paths.values():
        if not isinstance(path_item, dict):
            continue
        operations += sum(1 for method in path_item if method.lower() in HTTP_METHODS)
    if operations == 0:
        raise RuntimeError("OpenAPI document did not contain any operations.")

    components = document.get("components")
    components = components if isinstance(components, dict) else {}
    schemas = components.get("schemas")
    schema_count = len(schemas) if isinstance(schemas, dict) else 0
    if schema_count == 0:
        raise RuntimeError("OpenAPI document did not contain any component schemas.")

    return len(paths), operations, schema_count


def _sync_golden_openapi(manifest: dict[str, Any], output_root: Path) -> str:
    source = manifest["sources"]["golden_openapi"]
    url = source["spec_url"]
    timeout = float(source.get("timeout_seconds", 60.0))

    document = _fetch_json(url, timeout)
    path_count, operation_count, schema_count = _validate_openapi_document(document)

    openapi_dir = output_root / "openapi"
    openapi_dir.mkdir(parents=True, exist_ok=True)

    spec_destination = openapi_dir / "openapi-spec.json"
    spec_destination.write_text(
        json.dumps(document, indent=2, sort_keys=True),
        encoding="utf-8",
    )

    info = document.get("info")
    info = info if isinstance(info, dict) else {}
    metadata: dict[str, Any] = {
        "synced_at": datetime.now(UTC).isoformat(),
        "spec_url": url,
        "documentation_url": source.get("documentation_url"),
        "openapi_version": document.get("openapi"),
        "api_title": info.get("title"),
        "api_version": info.get("version"),
        "path_count": path_count,
        "operation_count": operation_count,
        "schema_count": schema_count,
    }

    # The published spec is a locked allowlist profile; carrying its provenance
    # forward makes it obvious which upstream profile the bundle was cut from.
    merge_metadata = document.get("x-merge-metadata")
    if isinstance(merge_metadata, dict):
        metadata["upstream_profile"] = {
            key: merge_metadata.get(key)
            for key in ("profileId", "profileName", "generatedAt", "keptPathsCount")
            if key in merge_metadata
        }

    (openapi_dir / "metadata.json").write_text(
        json.dumps(metadata, indent=2, sort_keys=True),
        encoding="utf-8",
    )

    return (
        f"saved {operation_count} operations across {path_count} paths "
        f"and {schema_count} schemas to {spec_destination}"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--manifest",
        default="src/incident_py_q/data/source_manifest.json",
        help="Path to schema source manifest JSON.",
    )
    parser.add_argument(
        "--output-root",
        default="src/incident_py_q/data",
        help="Bundle root where synced artifacts will be written.",
    )
    args = parser.parse_args()

    manifest_path = Path(args.manifest).resolve()
    output_root = Path(args.output_root).resolve()
    manifest = _read_manifest(manifest_path)

    results: list[SyncResult] = []
    source_map = manifest.get("sources", {})

    for source_name in ("golden_openapi",):
        if source_name not in source_map:
            continue
        required = bool(source_map[source_name].get("required", False))
        try:
            detail = _sync_golden_openapi(manifest, output_root)
            results.append(
                SyncResult(source=source_name, success=True, detail=detail, required=required)
            )
        except Exception as exc:
            results.append(
                SyncResult(
                    source=source_name,
                    success=False,
                    detail=f"{type(exc).__name__}: {exc}",
                    required=required,
                )
            )

    for result in results:
        status = "OK" if result.success else "FAIL"
        requirement = "required" if result.required else "optional"
        print(f"[{status}] {result.source} ({requirement}) - {result.detail}")

    required_failures = [result for result in results if result.required and not result.success]
    if required_failures:
        return 1

    manifest["generated_at"] = datetime.now(UTC).isoformat()
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
