#!/usr/bin/env python3
"""Build the legacy compatibility bundle for the Golden OpenAPI migration.

The published Golden contract is a locked allowlist profile that documents fewer
routes than the retired Stoplight controller set. Rather than drop the routes it
no longer documents, this script migrates them onto the Silver surface and
records the deprecated aliases that keep the previous SDK method names working.

It reads the retired artifacts from a git ref (the commit before the migration),
so the output is reproducible without keeping the Stoplight bundle checked in:

    python scripts/build_legacy_compat.py --from-ref <commit>

Outputs:
- `data/legacy/contract.json`  pruned Swagger contract for the migrated routes
- `data/legacy/aliases.json`   deprecated old-name -> new-location mapping
- appends the migrated routes to `data/silver_inventory.json`
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

LEGACY_CONTROLLER_DIR = "src/incident_py_q/data/stoplight/controllers"
LEGACY_INVENTORY_PATH = "tests/contract/golden_sdk_inventory.json"
HTTP_METHODS = ("get", "post", "put", "delete", "patch", "head", "options")
TENANT_API_PREFIX = "/api/v1.0"


def _git_show(ref: str, path: str) -> str:
    result = subprocess.run(
        ["git", "show", f"{ref}:{path}"],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise SystemExit(f"Could not read {path!r} at ref {ref!r}: {result.stderr.strip()}")
    return result.stdout


def _git_ls_controllers(ref: str) -> list[str]:
    result = subprocess.run(
        ["git", "ls-tree", "--name-only", f"{ref}:{LEGACY_CONTROLLER_DIR}"],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise SystemExit(f"Could not list legacy controllers at ref {ref!r}: {result.stderr.strip()}")
    return [name for name in result.stdout.splitlines() if name.endswith(".json")]


def _normalize_for_compare(path: str) -> str:
    without_params = re.sub(r"\{[^}]+\}", "{}", path)
    without_prefix = re.sub(r"^/api/v[0-9.]+", "", without_params)
    return without_prefix.rstrip("/").lower()


def _collect_refs(node: Any, found: set[str]) -> None:
    if isinstance(node, dict):
        ref = node.get("$ref")
        if isinstance(ref, str) and ref.startswith("#/definitions/"):
            found.add(ref[len("#/definitions/") :])
        for value in node.values():
            _collect_refs(value, found)
    elif isinstance(node, list):
        for item in node:
            _collect_refs(item, found)


def _reachable_definitions(
    seeds: list[Any],
    all_definitions: dict[str, Any],
) -> dict[str, Any]:
    """Return every definition transitively referenced by the seed nodes."""
    pending: set[str] = set()
    for seed in seeds:
        _collect_refs(seed, pending)

    resolved: dict[str, Any] = {}
    while pending:
        name = pending.pop()
        if name in resolved:
            continue
        definition = all_definitions.get(name)
        if definition is None:
            continue
        resolved[name] = definition
        nested: set[str] = set()
        _collect_refs(definition, nested)
        pending |= nested - resolved.keys()
    return resolved


def _type_display(parameter: dict[str, Any]) -> str:
    mapping = {
        "string": "str",
        "integer": "int",
        "number": "float",
        "boolean": "bool",
        "array": "list[Any]",
        "file": "Any",
    }
    if parameter.get("in") == "body":
        return "dict[str, Any] | list[Any]"
    raw_type = parameter.get("type")
    if isinstance(raw_type, str):
        return mapping.get(raw_type, "Any")
    return "Any"


def _snake_case_path(path: str) -> str:
    """Rewrite `{PartId}` style placeholders to the Silver runtime's `{part_id}` form.

    Silver renders path templates using the Python parameter name rather than the
    wire name, so migrated routes must use snake_case placeholders to be callable.
    """
    return re.sub(r"\{([^}]+)\}", lambda match: "{" + _to_snake_case(match.group(1)) + "}", path)


def _to_snake_case(value: str) -> str:
    from incident_py_q._utils import to_snake_case

    return to_snake_case(value)


def _silver_parameters(operation: dict[str, Any], shared: list[dict[str, Any]]) -> list[dict[str, Any]]:
    parameters: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()
    for parameter in [*shared, *operation.get("parameters", [])]:
        if not isinstance(parameter, dict):
            continue
        location = parameter.get("in")
        if location not in {"path", "query", "body"}:
            continue
        api_name = str(parameter.get("name", ""))
        if not api_name:
            continue
        key = (location, api_name)
        if key in seen:
            continue
        seen.add(key)

        python_name = "json_body" if location == "body" else _to_snake_case(api_name)
        description = parameter.get("description")
        parameters.append(
            {
                "python_name": python_name,
                "api_name": api_name,
                "location": location,
                "required": bool(parameter.get("required", location == "path")),
                "type_display": _type_display(parameter),
                "description": str(description)
                if isinstance(description, str) and description
                else f"{location.title()} parameter migrated from the previous Golden SDK.",
            }
        )
    # Path parameters first keeps generated signatures stable and readable.
    order = {"path": 0, "query": 1, "body": 2}
    parameters.sort(key=lambda item: (order[str(item["location"])], str(item["python_name"])))
    return parameters


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--from-ref",
        default="HEAD",
        help="Git ref that still contains the retired Stoplight bundle.",
    )
    parser.add_argument(
        "--project-root",
        default=str(Path(__file__).resolve().parents[1]),
        help="Repository root.",
    )
    args = parser.parse_args()

    project_root = Path(args.project_root).resolve()
    src_root = project_root / "src"
    if str(src_root) not in sys.path:
        sys.path.insert(0, str(src_root))

    ref = args.from_ref

    legacy_inventory: list[dict[str, Any]] = json.loads(_git_show(ref, LEGACY_INVENTORY_PATH))
    current_inventory: list[dict[str, Any]] = json.loads(
        (project_root / "tests/contract/golden_sdk_inventory.json").read_text(encoding="utf-8")
    )

    current_by_route: dict[tuple[str, str], dict[str, Any]] = {
        (entry["method"], _normalize_for_compare(entry["path"])): entry
        for entry in current_inventory
    }

    # A legacy method name can be reused by a *different* new operation. Aliasing it
    # would shadow the real new method, so those are recorded as conflicts instead:
    # they need a human decision, not a silent redirect.
    current_by_name: dict[tuple[str, str], dict[str, Any]] = {
        (entry["namespace"], entry["name"]): entry for entry in current_inventory
    }

    migrated: list[dict[str, Any]] = []
    aliases: list[dict[str, Any]] = []
    conflicts: list[dict[str, Any]] = []

    def _record_alias(entry: dict[str, Any], surface: str, target: dict[str, Any]) -> None:
        occupant = current_by_name.get((entry["namespace"], entry["name"]))
        if occupant is not None:
            conflicts.append(
                {
                    "legacy_namespace": entry["namespace"],
                    "legacy_name": entry["name"],
                    "legacy_operation_id": entry["operation_id"],
                    "legacy_route": f"{entry['method']} {entry['path']}",
                    "now_resolves_to_operation_id": occupant["operation_id"],
                    "now_resolves_to_route": f"{occupant['method']} {occupant['path']}",
                    "previous_behavior_moved_to": (
                        f"{target['namespace']}.{target['name']}"
                        if surface == "golden"
                        else f"silver.{target['namespace']}.{target['name']}"
                    ),
                    "surface": surface,
                }
            )
            return
        aliases.append(
            {
                "legacy_namespace": entry["namespace"],
                "legacy_name": entry["name"],
                "legacy_operation_id": entry["operation_id"],
                "surface": surface,
                "target_namespace": target["namespace"],
                "target_name": target["name"],
                "target_operation_id": target["operation_id"],
            }
        )

    for entry in legacy_inventory:
        target = current_by_route.get((entry["method"], _normalize_for_compare(entry["path"])))
        if target is None:
            migrated.append(entry)
            continue
        if target["namespace"] == entry["namespace"] and target["name"] == entry["name"]:
            continue
        _record_alias(entry, "golden", target)

    # Load the retired controller documents and index their operations.
    legacy_paths: dict[str, dict[str, Any]] = {}
    legacy_definitions: dict[str, Any] = {}
    for controller_name in _git_ls_controllers(ref):
        document = json.loads(_git_show(ref, f"{LEGACY_CONTROLLER_DIR}/{controller_name}"))
        for name, schema in (document.get("definitions") or {}).items():
            legacy_definitions.setdefault(name, schema)
        for raw_path, path_item in (document.get("paths") or {}).items():
            if not isinstance(path_item, dict):
                continue
            merged = legacy_paths.setdefault(raw_path, {})
            for key, value in path_item.items():
                merged.setdefault(key, value)

    pruned_paths: dict[str, Any] = {}
    silver_endpoints: list[dict[str, Any]] = []
    seed_nodes: list[Any] = []

    for entry in migrated:
        raw_path = entry["path"]
        path_item = legacy_paths.get(raw_path)
        if path_item is None:
            raise SystemExit(f"Legacy contract has no path item for {raw_path!r}.")
        method = str(entry["method"]).lower()
        operation = path_item.get(method)
        if not isinstance(operation, dict):
            raise SystemExit(f"Legacy contract has no {method.upper()} operation for {raw_path!r}.")

        shared = [p for p in path_item.get("parameters", []) if isinstance(p, dict)]
        absolute_path = _snake_case_path(f"{TENANT_API_PREFIX}{raw_path}")

        pruned_entry = pruned_paths.setdefault(absolute_path, {})
        if shared:
            pruned_entry.setdefault("parameters", shared)
        pruned_entry[method] = operation
        seed_nodes.append(operation)
        seed_nodes.extend(shared)

        status_codes = sorted(
            int(code) for code in (operation.get("responses") or {}) if str(code).isdigit()
        )
        summary = operation.get("summary")
        description = operation.get("description")
        migration_note = (
            "Migrated from the previous Golden SDK. The published Golden OpenAPI contract "
            "no longer documents this route, so it moved to the Silver surface to preserve "
            f"access. Previously `client.{entry['namespace']}.{entry['name']}` "
            f"(operationId `{entry['operation_id']}`)."
        )
        silver_endpoints.append(
            {
                "namespace_path": [entry["namespace"]],
                "method_name": entry["name"],
                "http_method": entry["method"],
                "route": absolute_path,
                "parameters": _silver_parameters(operation, shared),
                "summary": str(summary)
                if isinstance(summary, str) and summary
                else f"Migrated Silver route for {entry['method']} {raw_path}.",
                "description": (
                    f"{description}\n\n{migration_note}"
                    if isinstance(description, str) and description
                    else migration_note
                ),
                "typed_return": "dict[str, Any] | list[Any] | None",
                "raw_return": "dict[str, Any] | list[Any] | None",
                "sources": ["migrated_from_golden_stoplight"],
                "status_codes": status_codes,
                "uses_app_headers": False,
            }
        )

        _record_alias(entry, "silver", entry)

    definitions = _reachable_definitions(seed_nodes, legacy_definitions)

    legacy_dir = project_root / "src/incident_py_q/data/legacy"
    legacy_dir.mkdir(parents=True, exist_ok=True)

    contract = {
        "swagger": "2.0",
        "info": {
            "title": "Incident IQ (Migrated Legacy Contract)",
            "version": "1.0.0",
            "description": (
                "Pruned Swagger 2.0 contract for routes the published Golden OpenAPI "
                "document no longer documents. These routes are exposed on the Silver "
                "surface and validated against these schemas."
            ),
        },
        "x-legacy-metadata": {
            "generated_at": datetime.now(UTC).isoformat(),
            "source_ref": subprocess.run(
                ["git", "rev-parse", ref], capture_output=True, text=True, check=False
            ).stdout.strip(),
            "operation_count": len(migrated),
            "definition_count": len(definitions),
        },
        "paths": pruned_paths,
        "definitions": definitions,
    }
    (legacy_dir / "contract.json").write_text(
        json.dumps(contract, indent=2, sort_keys=True), encoding="utf-8"
    )

    aliases.sort(key=lambda item: (item["legacy_namespace"], item["legacy_name"]))
    conflicts.sort(key=lambda item: (item["legacy_namespace"], item["legacy_name"]))
    (legacy_dir / "aliases.json").write_text(
        json.dumps({"aliases": aliases, "conflicts": conflicts}, indent=2, sort_keys=True),
        encoding="utf-8",
    )

    # Merge the migrated routes into the bundled Silver inventory.
    silver_path = project_root / "src/incident_py_q/data/silver_inventory.json"
    silver_payload = json.loads(silver_path.read_text(encoding="utf-8"))
    existing = [
        endpoint
        for endpoint in silver_payload.get("endpoints", [])
        if "migrated_from_golden_stoplight" not in (endpoint.get("sources") or [])
    ]
    combined = [*existing, *silver_endpoints]
    combined.sort(key=lambda item: (item["namespace_path"], item["method_name"]))
    silver_payload["endpoints"] = combined
    silver_path.write_text(json.dumps(silver_payload, indent=2, sort_keys=True), encoding="utf-8")

    print(f"Migrated {len(migrated)} route(s) to the Silver surface.")
    print(f"Recorded {len(aliases)} deprecated alias(es).")
    if conflicts:
        print(f"\n{len(conflicts)} legacy name(s) are now taken by a DIFFERENT new operation:")
        for conflict in conflicts:
            print(
                f"  client.{conflict['legacy_namespace']}.{conflict['legacy_name']}: "
                f"was {conflict['legacy_route']}, now resolves to "
                f"{conflict['now_resolves_to_route']}; previous behavior is at "
                f"{conflict['previous_behavior_moved_to']}"
            )
    print(f"Pruned legacy contract: {len(pruned_paths)} paths, {len(definitions)} definitions.")
    print(f"Bundled Silver inventory now has {len(combined)} endpoints.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
