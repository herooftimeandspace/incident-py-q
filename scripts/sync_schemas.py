#!/usr/bin/env python3
"""Sync bundled Incident IQ contract artifacts from official upstream sources."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, cast

import httpx

PROJECT_QUERY = """
query ResolveProject($workspace: String!, $project: String!) {
  projects(where: {slug: {_eq: $project}, workspace: {slug: {_eq: $workspace}}}) {
    id
    slug
    name
    workspace {
      slug
    }
  }
}
"""

DEFAULT_BRANCH_QUERY = """
query ResolveDefaultBranch($projectId: Int!) {
  branches(where: {projectId: {_eq: $projectId}, isDefault: {_eq: true}}) {
    id
    slug
    isDefault
    projectId
  }
}
"""

CONTROLLER_NODES_QUERY = """
query ResolveControllerNodes($branchId: Int!, $uriPattern: String!) {
  branchNodes(
    where: {
      branchId: {_eq: $branchId}
      node: {uri: {_regex: $uriPattern}}
    }
    limit: 500
  ) {
    name
    slug
    node {
      uri
      format
    }
    snapshot {
      id
      data
      summary
    }
  }
}
"""


@dataclass(slots=True)
class SyncResult:
    source: str
    success: bool
    detail: str
    required: bool


def _read_manifest(path: Path) -> dict[str, Any]:
    loaded = json.loads(path.read_text(encoding="utf-8"))
    return cast(dict[str, Any], loaded)


def _post_graphql(endpoint: str, query: str, variables: dict[str, Any]) -> dict[str, Any]:
    response = httpx.post(
        endpoint,
        json={"query": query, "variables": variables},
        timeout=30.0,
    )
    response.raise_for_status()
    payload = cast(dict[str, Any], response.json())
    if payload.get("errors"):
        raise RuntimeError(f"GraphQL returned errors: {payload['errors']}")
    data = payload.get("data")
    if not isinstance(data, dict):
        raise RuntimeError("GraphQL response payload did not include object 'data'.")
    return cast(dict[str, Any], data)


def _sync_stoplight(manifest: dict[str, Any], output_root: Path) -> str:
    source = manifest["sources"]["stoplight"]
    endpoint = source["endpoint"]
    workspace_slug = source["workspace_slug"]
    project_slug = source["project_slug"]
    uri_pattern = source["controller_uri_regex"]

    project_data = _post_graphql(
        endpoint,
        PROJECT_QUERY,
        {"workspace": workspace_slug, "project": project_slug},
    )
    projects = project_data.get("projects", [])
    if not projects:
        raise RuntimeError("No Stoplight project matched workspace_slug + project_slug.")
    project_id = int(projects[0]["id"])

    branch_data = _post_graphql(endpoint, DEFAULT_BRANCH_QUERY, {"projectId": project_id})
    branches = branch_data.get("branches", [])
    if not branches:
        raise RuntimeError("No default branch found for Incident IQ Stoplight project.")
    branch_id = int(branches[0]["id"])

    node_data = _post_graphql(
        endpoint,
        CONTROLLER_NODES_QUERY,
        {"branchId": branch_id, "uriPattern": uri_pattern},
    )
    branch_nodes = node_data.get("branchNodes", [])
    if not branch_nodes:
        raise RuntimeError("No controller nodes returned from Stoplight graph query.")

    controllers_dir = output_root / "stoplight" / "controllers"
    controllers_dir.mkdir(parents=True, exist_ok=True)

    saved = 0
    for node in sorted(branch_nodes, key=lambda item: item["node"]["uri"]):
        uri = str(node["node"]["uri"])
        filename = uri.split("/")[-1]
        raw_data = node["snapshot"]["data"]
        if not isinstance(raw_data, str):
            raise RuntimeError(f"Unexpected snapshot payload type for {uri!r}")
        parsed = json.loads(raw_data)
        destination = controllers_dir / filename
        destination.write_text(json.dumps(parsed, indent=2, sort_keys=True), encoding="utf-8")
        saved += 1

    metadata = {
        "synced_at": datetime.now(UTC).isoformat(),
        "project_id": project_id,
        "branch_id": branch_id,
        "workspace_slug": workspace_slug,
        "project_slug": project_slug,
        "controllers_saved": saved,
    }
    (output_root / "stoplight" / "metadata.json").write_text(
        json.dumps(metadata, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    return f"saved {saved} controller specs"


def _sync_postman(manifest: dict[str, Any], output_root: Path) -> str:
    source = manifest["sources"]["apihub_postman"]
    url = source["url"]
    response = httpx.get(url, timeout=45.0)
    response.raise_for_status()
    payload = response.json()

    postman_dir = output_root / "postman"
    postman_dir.mkdir(parents=True, exist_ok=True)
    destination = postman_dir / "collection.json"
    destination.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
    return f"saved Postman collection to {destination}"


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

    for source_name in ("stoplight", "apihub_postman"):
        if source_name not in source_map:
            continue
        required = bool(source_map[source_name].get("required", False))
        try:
            if source_name == "stoplight":
                detail = _sync_stoplight(manifest, output_root)
            elif source_name == "apihub_postman":
                detail = _sync_postman(manifest, output_root)
            else:
                detail = "skipped unknown source"
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
