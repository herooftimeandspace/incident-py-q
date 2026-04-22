"""SDK documentation and typing artifact generation."""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path

from incident_py_q.apps import AppMethodMetadata, AppParameterMetadata, build_app_method_metadata
from incident_py_q.schema.registry import SchemaRegistry
from incident_py_q.silver import (
    SilverMethodMetadata,
    SilverParameterMetadata,
    build_silver_metadata,
)

from .runtime import SDKMethodMetadata, SDKParameterMetadata, build_sdk_metadata


def render_sdk_index(
    metadata: tuple[SDKMethodMetadata, ...],
    silver_metadata: tuple[SilverMethodMetadata, ...] | None = None,
) -> str:
    """Render the SDK reference landing page."""
    grouped = _group_metadata(metadata)
    silver = silver_metadata or build_silver_metadata()
    silver_grouped = _group_silver_metadata(silver)
    app_methods = build_app_method_metadata()
    lines = [
        "# SDK Reference",
        "",
        "Golden methods come from bundled Stoplight controller contracts. Silver methods come "
        "from HAR-observed undocumented routes and are exposed separately so they never silently "
        "override the documented Golden surface.",
        "",
        "## Golden Namespaces",
        "",
        "| Namespace | Canonical Methods | Page |",
        "| --- | ---: | --- |",
    ]
    for namespace, methods in grouped.items():
        lines.append(
            f"| `{namespace}` | {len(methods)} | [`client.{namespace}`]({namespace}.md) |"
        )

    lines.extend(
        [
            "",
            "## Silver Namespaces",
            "",
            "| Namespace | Methods | Page |",
            "| --- | ---: | --- |",
            f"| `silver` | {len(silver)} | [`client.silver`](silver.md) |",
            (
                f"| `apps` legacy alias | {len(app_methods)} manual helpers + "
                f"{len(silver_grouped.get(('apps',), ())) + sum(len(methods) for path, methods in silver_grouped.items() if path[:1] == ('apps',) and len(path) > 1)} "
                "| [`client.apps`](apps.md) |"
            ),
        ]
    )
    return "\n".join(lines) + "\n"


def render_apps_reference(
    methods: tuple[AppMethodMetadata, ...] | None = None,
    silver_metadata: tuple[SilverMethodMetadata, ...] | None = None,
) -> str:
    """Render the Silver apps reference page."""
    app_methods = methods or build_app_method_metadata()
    silver = silver_metadata or build_silver_metadata()
    grouped_manual: dict[str, list[AppMethodMetadata]] = defaultdict(list)
    service_labels: dict[str, str] = {}
    for method in app_methods:
        grouped_manual[method.service_name].append(method)
        service_labels[method.service_name] = method.service_label

    grouped_silver: dict[str, list[SilverMethodMetadata]] = defaultdict(list)
    for silver_method in silver:
        if silver_method.namespace_path[:1] != ("apps",):
            continue
        service = (
            silver_method.namespace_path[1]
            if len(silver_method.namespace_path) > 1
            else "root"
        )
        grouped_silver[service].append(silver_method)

    service_names = sorted(set(grouped_manual) | set(grouped_silver))
    lines = [
        "# `apps` Silver Namespace",
        "",
        "Primary sync access: `client.silver.apps`",
        "",
        "Legacy sync alias: `client.apps`",
        "",
        "Primary async access: `client.silver.apps` with `await` for async service methods.",
        "",
        "These methods are Silver because Stoplight does not publish Golden contracts for them. "
        "The legacy `client.apps` alias remains available so existing integrations keep working "
        "while the undocumented nature of these routes is made explicit.",
        "",
        "| Service | Manual Helpers | Generic Silver Methods | Access Path |",
        "| --- | ---: | ---: | --- |",
    ]
    for service_name in service_names:
        lines.append(
            f"| `{service_name}` | {len(grouped_manual.get(service_name, []))} | "
            f"{len(grouped_silver.get(service_name, []))} | `client.silver.apps.{service_name}` |"
        )
    lines.append("")

    for service_name in service_names:
        label = service_labels.get(service_name, service_name.replace("_", " ").title())
        lines.extend(
            [
                f"## `{service_name}`",
                "",
                f"{label} service available at `client.silver.apps.{service_name}`.",
                "",
            ]
        )
        for app_method in grouped_manual.get(service_name, []):
            lines.extend(_render_manual_app_method(app_method))
        for silver_method in grouped_silver.get(service_name, []):
            lines.extend(_render_silver_method(silver_method))
    return "\n".join(lines).rstrip() + "\n"


def render_namespace_reference(namespace: str, methods: tuple[SDKMethodMetadata, ...]) -> str:
    """Render one Golden namespace SDK reference page."""
    alias_rows: list[str] = []
    for method in methods:
        for alias_name in method.aliases:
            alias_rows.append(
                f"| `{alias_name}` | `{method.name}` | "
                f"`{method.operation.method} {method.operation.path_template}` |"
            )

    lines = [
        f"# `{namespace}` Golden Namespace",
        "",
        f"Sync client access: `client.{namespace}`",
        "",
        f"Async client access: `client.{namespace}` with `await` on method calls.",
        "",
        "These methods are Golden because they come from bundled Stoplight controller contracts.",
        "",
    ]

    if alias_rows:
        lines.extend(
            [
                "## Aliases",
                "",
                "| Alias | Canonical Method | Route |",
                "| --- | --- | --- |",
                *alias_rows,
                "",
            ]
        )

    lines.extend(["## Methods", ""])
    for method in methods:
        summary = method.operation.summary or "No contract summary provided."
        description = method.operation.description
        lines.extend(
            [
                f"### `{method.name}`",
                "",
                "Provenance: Golden Stoplight contract",
                "",
                f"Operation ID: `{method.operation.operation_id}`",
                "",
                f"- Sync: `{_sync_call_example(method)}`",
                f"- Async: `{_async_call_example(method)}`",
                f"- Raw payload: `{_sync_raw_call_example(method)}`",
                f"- HTTP route: `{method.operation.method} {method.operation.path_template}`",
                f"- Source controller: `{method.operation.source_controller}`",
            ]
        )
        if method.aliases:
            lines.append(f"- Aliases: {', '.join(f'`{alias_name}`' for alias_name in method.aliases)}")
        lines.extend(["", summary, ""])
        if description and description != summary:
            lines.extend([description, ""])
        lines.extend(_render_golden_parameters(method))
        lines.extend(_render_golden_returns(method))
        lines.extend(["", "---", ""])

    return "\n".join(lines).rstrip() + "\n"


def render_silver_overview(metadata: tuple[SilverMethodMetadata, ...] | None = None) -> str:
    """Render the Silver overview page."""
    silver = metadata or build_silver_metadata()
    grouped = _group_silver_metadata(silver)
    top_level: defaultdict[str, int] = defaultdict(int)
    for namespace_path, silver_methods in grouped.items():
        top_level[namespace_path[0]] += len(silver_methods)
    lines = [
        "# `silver` Namespace",
        "",
        "Sync client access: `client.silver`",
        "",
        "Async client access: `client.silver` with `await` on async methods.",
        "",
        "Silver routes are undocumented APIs observed in tenant HAR traffic. The SDK exposes them "
        "explicitly and separately because Golden Stoplight contracts are always preferred when "
        "they exist.",
        "",
        "| Namespace | Methods | Page |",
        "| --- | ---: | --- |",
    ]
    for namespace, count in sorted(top_level.items()):
        page = "apps.md" if namespace == "apps" else f"silver-{namespace}.md"
        lines.append(f"| `{namespace}` | {count} | [`client.silver.{namespace}`]({page}) |")
    return "\n".join(lines) + "\n"


def render_silver_namespace_reference(
    namespace_path: tuple[str, ...],
    methods: tuple[SilverMethodMetadata, ...],
) -> str:
    """Render one generic Silver namespace page."""
    namespace_display = ".".join(namespace_path)
    lines = [
        f"# `silver.{namespace_display}` Namespace",
        "",
        f"Sync client access: `client.silver.{namespace_display}`",
        "",
        f"Async client access: `client.silver.{namespace_display}` with `await` on method calls.",
        "",
        "These methods are Silver because Stoplight does not publish Golden contracts for them. "
        "They remain separate so undocumented behavior never overrides the documented SDK surface.",
        "",
        "## Methods",
        "",
    ]
    for method in methods:
        lines.extend(_render_silver_method(method))
    return "\n".join(lines).rstrip() + "\n"


def render_client_stub(registry: SchemaRegistry) -> str:
    """Render the static typing stub for the dynamic Golden and Silver client surfaces."""
    metadata = build_sdk_metadata(registry)
    grouped = _group_metadata(metadata)
    silver_metadata = build_silver_metadata()
    silver_grouped = _group_silver_metadata(silver_metadata)
    app_methods = build_app_method_metadata()
    manual_app_grouped = _group_manual_app_methods(app_methods)
    model_names = sorted(
        {
            model_name
            for method in metadata
            for model_name in [
                *(parameter.model_name for parameter in method.parameters if parameter.model_name),
                method.response_model_name,
            ]
            if model_name
        }
    )
    lines = [
        "from __future__ import annotations",
        "",
        "from collections.abc import Mapping, Sequence",
        "from os import PathLike",
        "from typing import Any, Protocol",
        "",
        "import httpx",
        "from pydantic import BaseModel",
        "",
        "from .apps.models import (",
        "    AppLookupResponse,",
        "    AppRegistryResponse,",
        "    AppRemoteAction,",
        "    GoogleSyncOptionsResponse,",
        "    IntuneOwnerClassification,",
        "    IntuneOwnershipPartition,",
        ")",
        "from .config import ClientConfig",
        "from .schema.registry import SchemaRegistry",
        "from .sdk.runtime import AsyncNamespace, Namespace",
        "from .silver import SilverMethodMetadata",
        "",
        "_JSONPayload = dict[str, Any] | list[Any] | None",
        "",
        "def _build_url(base_url: str, rendered_path: str) -> str: ...",
        "def _merge_headers(config: ClientConfig, headers: Mapping[str, str] | None) -> dict[str, str]: ...",
        "def _normalize_app_headers(app_headers: Mapping[str, str] | None) -> dict[str, str] | None: ...",
        "def _decode_payload(response: httpx.Response) -> _JSONPayload: ...",
        "",
    ]

    for model_name in model_names:
        lines.extend([f"class {model_name}(BaseModel):", "    ...", ""])

    for namespace, methods in grouped.items():
        for method in methods:
            lines.extend(_render_method_protocol(namespace, method, async_mode=False))
            lines.append("")
            lines.extend(_render_method_protocol(namespace, method, async_mode=True))
            lines.append("")
        lines.extend(_render_namespace_stub(namespace, methods, async_mode=False))
        lines.append("")
        lines.extend(_render_namespace_stub(namespace, methods, async_mode=True))
        lines.append("")

    for service_name, app_service_methods in manual_app_grouped.items():
        service_silver_methods = silver_grouped.get(("apps", service_name), ())
        lines.extend(
            _render_manual_app_service_stub(
                service_name,
                app_service_methods,
                service_silver_methods,
                async_mode=False,
            )
        )
        lines.append("")
        lines.extend(
            _render_manual_app_service_stub(
                service_name,
                app_service_methods,
                service_silver_methods,
                async_mode=True,
            )
        )
        lines.append("")

    for namespace_path, silver_methods in sorted(silver_grouped.items()):
        if namespace_path[:1] == ("apps",) and len(namespace_path) == 2 and namespace_path[1] in manual_app_grouped:
            continue
        lines.extend(_render_silver_namespace_stub(namespace_path, silver_methods, async_mode=False))
        lines.append("")
        lines.extend(_render_silver_namespace_stub(namespace_path, silver_methods, async_mode=True))
        lines.append("")

    lines.extend(_render_silver_root_stub(silver_grouped, manual_app_grouped, async_mode=False))
    lines.append("")
    lines.extend(_render_silver_root_stub(silver_grouped, manual_app_grouped, async_mode=True))
    lines.append("")
    lines.extend(_render_client_class_stub(grouped, silver_grouped, manual_app_grouped, async_mode=False))
    lines.append("")
    lines.extend(_render_client_class_stub(grouped, silver_grouped, manual_app_grouped, async_mode=True))
    lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_package_stub() -> str:
    """Render the top-level package stub."""
    return "\n".join(
        [
            "from .client import AsyncClient, Client",
            "from .version import __version__",
            "",
            "__all__ = [\"AsyncClient\", \"Client\", \"__version__\"]",
            "",
        ]
    )


def write_sdk_reference_artifacts(
    *,
    docs_root: Path,
    package_root: Path,
    registry: SchemaRegistry,
) -> None:
    """Write generated Markdown reference pages and typing stubs."""
    metadata = build_sdk_metadata(registry)
    grouped = _group_metadata(metadata)
    silver_metadata = build_silver_metadata()
    silver_grouped = _group_silver_metadata(silver_metadata)

    docs_root.mkdir(parents=True, exist_ok=True)
    for existing in docs_root.glob("*.md"):
        existing.unlink()

    (docs_root / "index.md").write_text(
        render_sdk_index(metadata, silver_metadata),
        encoding="utf-8",
    )
    (docs_root / "apps.md").write_text(
        render_apps_reference(build_app_method_metadata(), silver_metadata),
        encoding="utf-8",
    )
    (docs_root / "silver.md").write_text(render_silver_overview(silver_metadata), encoding="utf-8")
    for namespace, methods in grouped.items():
        (docs_root / f"{namespace}.md").write_text(
            render_namespace_reference(namespace, methods),
            encoding="utf-8",
        )
    for namespace_path, silver_methods in silver_grouped.items():
        if namespace_path[:1] == ("apps",):
            continue
        page_name = f"silver-{namespace_path[0]}.md"
        (docs_root / page_name).write_text(
            render_silver_namespace_reference(namespace_path, silver_methods),
            encoding="utf-8",
        )

    package_root.mkdir(parents=True, exist_ok=True)
    (package_root / "client.pyi").write_text(render_client_stub(registry), encoding="utf-8")
    (package_root / "__init__.pyi").write_text(render_package_stub(), encoding="utf-8")


def _group_metadata(
    metadata: tuple[SDKMethodMetadata, ...],
) -> dict[str, tuple[SDKMethodMetadata, ...]]:
    grouped: dict[str, list[SDKMethodMetadata]] = defaultdict(list)
    for method in metadata:
        grouped[method.namespace].append(method)
    return {
        namespace: tuple(sorted(methods, key=lambda item: item.name))
        for namespace, methods in sorted(grouped.items())
    }


def _group_silver_metadata(
    metadata: tuple[SilverMethodMetadata, ...],
) -> dict[tuple[str, ...], tuple[SilverMethodMetadata, ...]]:
    grouped: dict[tuple[str, ...], list[SilverMethodMetadata]] = defaultdict(list)
    for method in metadata:
        grouped[method.namespace_path].append(method)
    return {
        namespace_path: tuple(sorted(methods, key=lambda item: item.method_name))
        for namespace_path, methods in sorted(grouped.items())
    }


def _group_manual_app_methods(
    metadata: tuple[AppMethodMetadata, ...],
) -> dict[str, tuple[AppMethodMetadata, ...]]:
    grouped: dict[str, list[AppMethodMetadata]] = defaultdict(list)
    for method in metadata:
        grouped[method.service_name].append(method)
    return {
        service_name: tuple(sorted(methods, key=lambda item: item.method_name))
        for service_name, methods in sorted(grouped.items())
    }


def _render_golden_parameters(method: SDKMethodMetadata) -> list[str]:
    if not method.parameters:
        return ["#### Parameters", "", "This operation does not define request parameters.", ""]
    lines = [
        "#### Parameters",
        "",
        "| Python Arg | API Name | In | Required | Type | Schema / Model | Description |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for parameter in method.parameters:
        lines.append(_render_parameter_row(parameter))
    lines.append("")
    return lines


def _render_golden_returns(method: SDKMethodMetadata) -> list[str]:
    lines = [
        "#### Returns",
        "",
        f"- Typed call return: `{method.response_type_display}`",
        f"- Raw payload return: `{method.raw_return_type_display}`",
    ]
    if method.response_model_name:
        lines.append(f"- Response model: `{method.response_model_name}`")
    elif method.response_schema_ref:
        lines.append(f"- Response schema ref: `{method.response_schema_ref}`")
    else:
        lines.append("- Response model: Raw JSON payload")
    if method.supports_pagination:
        lines.append(
            f"- Pagination helper: `{_iter_pages_call_example(method)}`"
        )
    else:
        lines.append(
            "- Pagination helper: No paging query parameters detected; "
            "`iter_pages(...)` returns a single raw response."
        )
    return lines


def _render_silver_method(method: SilverMethodMetadata) -> list[str]:
    lines = [
        f"### `{method.method_name}`",
        "",
        "Provenance: Silver (HAR-derived undocumented route)",
        "",
        f"- Sync: `{_silver_sync_call_example(method)}`",
        f"- Async: `{_silver_async_call_example(method)}`",
        f"- Raw payload: `{_silver_raw_call_example(method)}`",
        f"- HTTP route: `{method.http_method} {method.route}`",
        (
            f"- Observed in: {', '.join(f'`{source}`' for source in method.sources)}"
            if method.sources
            else "- Observed in: Synthetic required Silver route"
        ),
        "",
        method.summary,
        "",
        method.description,
        "",
    ]
    if method.parameters:
        lines.extend(
            [
                "#### Parameters",
                "",
                "| Python Arg | API Name | In | Required | Type | Description |",
                "| --- | --- | --- | --- | --- | --- |",
            ]
        )
        for parameter in method.parameters:
            lines.append(_render_silver_parameter_row(parameter))
        lines.append("")
    else:
        lines.extend(["#### Parameters", "", "This Silver route does not define inferred parameters.", ""])
    lines.extend(
        [
            "#### Returns",
            "",
            f"- Typed call return: `{method.typed_return}`",
            f"- Raw payload return: `{method.raw_return}`",
            "- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.",
            "",
            "---",
            "",
        ]
    )
    return lines


def _render_manual_app_method(method: AppMethodMetadata) -> list[str]:
    sync_call = method.sync_call.replace("client.apps", "client.silver.apps")
    async_call = method.async_call.replace("client.apps", "client.silver.apps")
    lines = [
        f"### `{method.method_name}`",
        "",
        "Provenance: Silver manual helper",
        "",
        f"- Sync: `{sync_call}`",
        f"- Async: `{async_call}`",
        "- Legacy alias: replace `client.silver.apps` with `client.apps` if you need the old access path.",
    ]
    if method.http_method and method.route:
        lines.append(f"- HTTP route: `{method.http_method} {method.route}`")
    else:
        lines.append("- HTTP route: Utility helper (no HTTP request)")
    lines.extend(["", method.summary, ""])
    if method.description and method.description != method.summary:
        lines.extend([method.description, ""])
    if method.parameters:
        lines.extend(
            [
                "#### Parameters",
                "",
                "| Python Arg | API Name | In | Required | Type | Description |",
                "| --- | --- | --- | --- | --- | --- |",
            ]
        )
        for parameter in method.parameters:
            lines.append(_render_app_parameter_row(parameter))
        lines.append("")
    else:
        lines.extend(["#### Parameters", "", "This method does not define parameters.", ""])
    lines.extend(
        [
            "#### Returns",
            "",
            f"- Typed call return: `{method.typed_return}`",
            f"- Raw payload return: `{method.raw_return}`",
        ]
    )
    if method.response_model:
        lines.append(f"- Response model: `{method.response_model}`")
    elif method.response_schema:
        lines.append(f"- Response schema: `{method.response_schema}`")
    else:
        lines.append("- Response model: Method-specific Python object")
    lines.extend(["", "---", ""])
    return lines


def _render_parameter_row(parameter: SDKParameterMetadata) -> str:
    schema_or_model = parameter.model_name or parameter.schema_ref or "-"
    description = parameter.description or "-"
    return (
        f"| `{parameter.python_name}` | `{parameter.api_name}` | `{parameter.location}` | "
        f"`{'yes' if parameter.required else 'no'}` | `{parameter.annotation_display}` | "
        f"`{_escape_inline(schema_or_model)}` | {_escape_table(description)} |"
    )


def _render_app_parameter_row(parameter: AppParameterMetadata) -> str:
    return (
        f"| `{parameter.python_name}` | `{parameter.api_name}` | `{parameter.location}` | "
        f"`{'yes' if parameter.required else 'no'}` | `{parameter.type_display}` | "
        f"{_escape_table(parameter.description)} |"
    )


def _render_silver_parameter_row(parameter: SilverParameterMetadata) -> str:
    return (
        f"| `{parameter.python_name}` | `{parameter.api_name}` | `{parameter.location}` | "
        f"`{'yes' if parameter.required else 'no'}` | `{parameter.type_display}` | "
        f"{_escape_table(parameter.description)} |"
    )


def _sync_call_example(method: SDKMethodMetadata) -> str:
    return f"client.{method.namespace}.{method.name}{_signature_suffix(method)}"


def _async_call_example(method: SDKMethodMetadata) -> str:
    return f"await client.{method.namespace}.{method.name}{_signature_suffix(method)}"


def _sync_raw_call_example(method: SDKMethodMetadata) -> str:
    return f"client.{method.namespace}.{method.name}.raw{_signature_suffix(method)}"


def _silver_sync_call_example(method: SilverMethodMetadata) -> str:
    return f"client.silver.{method.namespace}.{method.method_name}{_silver_signature_suffix(method)}"


def _silver_async_call_example(method: SilverMethodMetadata) -> str:
    return f"await client.silver.{method.namespace}.{method.method_name}{_silver_signature_suffix(method)}"


def _silver_raw_call_example(method: SilverMethodMetadata) -> str:
    return f"client.silver.{method.namespace}.{method.method_name}.raw{_silver_signature_suffix(method)}"


def _iter_pages_call_example(method: SDKMethodMetadata) -> str:
    args = _render_call_arguments(method, exclude_pagination=True)
    extra = "start_page=1, page_size=100, max_pages=None"
    joined = ", ".join(part for part in [extra, args] if part)
    return f"client.{method.namespace}.{method.name}.iter_pages({joined})"


def _signature_suffix(method: SDKMethodMetadata) -> str:
    arguments = _render_call_arguments(method, exclude_pagination=False)
    return f"({arguments})" if arguments else "()"


def _silver_signature_suffix(method: SilverMethodMetadata) -> str:
    parts = []
    for parameter in method.parameters:
        placeholder = "..." if parameter.required else "None"
        parts.append(f"{parameter.python_name}={placeholder}")
    parts.append("timeout=None")
    return f"({', '.join(parts)})"


def _render_call_arguments(method: SDKMethodMetadata, *, exclude_pagination: bool) -> str:
    parts: list[str] = []
    for parameter in method.parameters:
        if exclude_pagination and _is_pagination_parameter(parameter):
            continue
        placeholder = "..." if parameter.required else "None"
        parts.append(f"{parameter.python_name}={placeholder}")
    parts.append("timeout=None")
    return ", ".join(parts)


def _render_method_protocol(
    namespace: str,
    method: SDKMethodMetadata,
    *,
    async_mode: bool,
) -> list[str]:
    protocol_name = _protocol_name(namespace, method.name, async_mode=async_mode)
    return_type = method.response_model_name or "_JSONPayload"
    lines: list[str] = []
    if not async_mode:
        lines.append(f"# OperationId: {method.operation.operation_id}")
    lines.extend(
        [
            f"class {protocol_name}(Protocol):",
            f"    {'async ' if async_mode else ''}def __call__{_stub_signature(method, return_type=return_type)}: ...",
            f"    {'async ' if async_mode else ''}def raw{_stub_signature(method, return_type='_JSONPayload')}: ...",
        ]
    )
    if not async_mode:
        lines.append(
            "    def iter_pages"
            f"{_iter_pages_signature(method, return_type='list[_JSONPayload]')}: ..."
        )
    return lines


def _render_namespace_stub(
    namespace: str,
    methods: tuple[SDKMethodMetadata, ...],
    *,
    async_mode: bool,
) -> list[str]:
    class_name = _namespace_class_name(namespace, async_mode=async_mode)
    base_name = "AsyncNamespace" if async_mode else "Namespace"
    lines = [f"class {class_name}({base_name}):", "    def list_methods(self) -> list[str]: ..."]
    for method in methods:
        protocol_name = _protocol_name(namespace, method.name, async_mode=async_mode)
        lines.append(f"    {method.name}: {protocol_name}")
        for alias_name in method.aliases:
            lines.append(f"    {alias_name}: {protocol_name}")
    return lines


def _render_manual_app_service_stub(
    service_name: str,
    methods: tuple[AppMethodMetadata, ...],
    silver_methods: tuple[SilverMethodMetadata, ...],
    *,
    async_mode: bool,
) -> list[str]:
    class_name = _manual_app_class_name(service_name, async_mode=async_mode)
    lines = [f"class {class_name}:"]
    for method in methods:
        lines.append(
            f"    {'async ' if async_mode else ''}def {method.method_name}{_manual_app_signature(method, async_mode=async_mode)}: ..."
        )
    for silver_method in silver_methods:
        lines.append(
            f"    {'async ' if async_mode else ''}def {silver_method.method_name}{_silver_stub_signature(silver_method)}: ..."
        )
    return lines


def _render_silver_namespace_stub(
    namespace_path: tuple[str, ...],
    methods: tuple[SilverMethodMetadata, ...],
    *,
    async_mode: bool,
) -> list[str]:
    class_name = _silver_namespace_class_name(namespace_path, async_mode=async_mode)
    lines = [f"class {class_name}:", "    def list_methods(self) -> list[str]: ..."]
    for method in methods:
        lines.append(
            f"    {'async ' if async_mode else ''}def {method.method_name}{_silver_stub_signature(method)}: ..."
        )
    return lines


def _render_silver_root_stub(
    silver_grouped: dict[tuple[str, ...], tuple[SilverMethodMetadata, ...]],
    manual_app_grouped: dict[str, tuple[AppMethodMetadata, ...]],
    *,
    async_mode: bool,
) -> list[str]:
    apps_class_name = "AsyncSilverAppsNamespace" if async_mode else "SilverAppsNamespace"
    root_class_name = "AsyncSilverRootNamespace" if async_mode else "SilverRootNamespace"
    lines = [f"class {apps_class_name}:", "    def list_methods(self) -> list[str]: ...", "    def list_namespaces(self) -> list[str]: ..."]
    child_services = {
        namespace_path[1]
        for namespace_path in silver_grouped
        if namespace_path[:1] == ("apps",) and len(namespace_path) > 1
    } | set(manual_app_grouped)
    for service_name in sorted(child_services):
        lines.append(
            f"    {service_name}: {_manual_app_class_name(service_name, async_mode=async_mode) if service_name in manual_app_grouped else _silver_namespace_class_name(('apps', service_name), async_mode=async_mode)}"
        )

    lines.append("")
    lines.extend(
        [
            f"class {root_class_name}:",
            "    def list_methods(self) -> list[str]: ...",
            "    def list_namespaces(self) -> list[str]: ...",
            f"    apps: {apps_class_name}",
        ]
    )
    top_level = {namespace_path[0] for namespace_path in silver_grouped if namespace_path[0] != "apps"}
    for namespace in sorted(top_level):
        lines.append(
            f"    {namespace}: {_silver_namespace_class_name((namespace,), async_mode=async_mode)}"
        )
    return lines


def _render_client_class_stub(
    grouped: dict[str, tuple[SDKMethodMetadata, ...]],
    silver_grouped: dict[tuple[str, ...], tuple[SilverMethodMetadata, ...]],
    manual_app_grouped: dict[str, tuple[AppMethodMetadata, ...]],
    *,
    async_mode: bool,
) -> list[str]:
    class_name = "AsyncClient" if async_mode else "Client"
    http_client_type = "httpx.AsyncClient | None" if async_mode else "httpx.Client | None"
    request_prefix = "async " if async_mode else ""
    close_prefix = "async " if async_mode else ""
    context_prefix = "async " if async_mode else ""
    enter_name = "__aenter__" if async_mode else "__enter__"
    exit_name = "__aexit__" if async_mode else "__exit__"
    root_class_name = "AsyncSilverRootNamespace" if async_mode else "SilverRootNamespace"
    apps_class_name = "AsyncSilverAppsNamespace" if async_mode else "SilverAppsNamespace"

    lines = [
        f"class {class_name}:",
        "    def __init__(",
        "        self,",
        "        *,",
        "        base_url: str | None = None,",
        "        api_token: str | None = None,",
        "        site_id: str | None = None,",
        "        client_header: str = 'ApiClient',",
        "        auth_mode: str = 'bearer',",
        "        app_headers: Mapping[str, str] | None = None,",
        "        timeout: float = 30.0,",
        "        validate_responses: bool = True,",
        "        max_retries: int = 2,",
        "        backoff_base: float = 0.25,",
        "        config: ClientConfig | None = None,",
        "        registry: SchemaRegistry | None = None,",
        f"        http_client: {http_client_type} = None,",
        "    ) -> None: ...",
        "    @classmethod",
        f"    def from_env(cls) -> {class_name}: ...",
        "    @classmethod",
        f"    def from_test_env(cls) -> {class_name}: ...",
        "    @property",
        "    def config(self) -> ClientConfig: ...",
        "    def sdk_inventory(self) -> list[dict[str, str]]: ...",
        "    def silver_sdk_inventory(self) -> list[dict[str, Any]]: ...",
        "    def merged_sdk_inventory(self) -> list[dict[str, Any]]: ...",
        "    def __getattr__(self, name: str) -> Any: ...",
        f"    {close_prefix}def close(self) -> None: ...",
        f"    {context_prefix}def {enter_name}(self) -> {class_name}: ...",
        f"    {context_prefix}def {exit_name}(self, *_: Any) -> None: ...",
        "    "
        + request_prefix
        + "def request("
        "self, method: str, path: str, *, path_params: Mapping[str, Any] | None = None, "
        "params: Mapping[str, Any] | None = None, json: Any | None = None, "
        "files: Mapping[str, Any] | None = None, headers: Mapping[str, str] | None = None, "
        "timeout: float | None = None"
        ") -> _JSONPayload: ...",
        "    "
        + request_prefix
        + "def request_silver("
        "self, metadata: SilverMethodMetadata, *, path_params: Mapping[str, Any] | None = None, "
        "params: Mapping[str, Any] | None = None, json: Any | None = None, "
        "files: Mapping[str, Any] | None = None, headers: Mapping[str, str] | None = None, "
        "timeout: float | None = None"
        ") -> _JSONPayload: ...",
    ]
    for namespace in grouped:
        lines.append(
            f"    {namespace}: {_namespace_class_name(namespace, async_mode=async_mode)}"
        )
    lines.append(f"    silver: {root_class_name}")
    lines.append(f"    apps: {apps_class_name}")
    return lines


def _stub_signature(method: SDKMethodMetadata, *, return_type: str) -> str:
    params = _stub_param_list(method, include_timeout=True, exclude_pagination=False)
    return f"({params}) -> {return_type}"


def _silver_stub_signature(method: SilverMethodMetadata) -> str:
    params = ["self", "*"]
    for parameter in method.parameters:
        type_display = parameter.type_display if parameter.required else f"{parameter.type_display} | None"
        default = "..." if parameter.required else "None"
        params.append(f"{parameter.python_name}: {type_display} = {default}")
    params.append("timeout: float | None = None")
    return f"({', '.join(params)}) -> _JSONPayload"


def _manual_app_signature(method: AppMethodMetadata, *, async_mode: bool) -> str:
    params = ["self", "*"]
    for parameter in method.parameters:
        type_display = _optionalized_type(parameter.type_display, parameter.required)
        default = "..." if parameter.required else "None"
        params.append(f"{parameter.python_name}: {type_display} = {default}")
    if method.http_method:
        params.append("timeout: float | None = None")
        return_type = method.typed_return if not method.method_name.endswith("_raw") else method.raw_return
    else:
        return_type = method.typed_return
    return f"({', '.join(params)}) -> {return_type}"


def _iter_pages_signature(method: SDKMethodMetadata, *, return_type: str) -> str:
    params = [
        "self",
        "*",
        "start_page: int = 1",
        "page_size: int = 100",
        "max_pages: int | None = None",
    ]
    params.extend(_stub_param_entries(method, include_timeout=False, exclude_pagination=True))
    return f"({', '.join(params)}) -> {return_type}"


def _stub_param_list(
    method: SDKMethodMetadata,
    *,
    include_timeout: bool,
    exclude_pagination: bool,
) -> str:
    entries = ["self", "*"]
    entries.extend(
        _stub_param_entries(
            method,
            include_timeout=include_timeout,
            exclude_pagination=exclude_pagination,
        )
    )
    return ", ".join(entries)


def _stub_param_entries(
    method: SDKMethodMetadata,
    *,
    include_timeout: bool,
    exclude_pagination: bool,
) -> list[str]:
    entries: list[str] = []
    for parameter in method.parameters:
        if exclude_pagination and _is_pagination_parameter(parameter):
            continue
        annotation = parameter.annotation_display
        if not parameter.required:
            annotation = f"{annotation} | None"
        default = "..." if parameter.required else "None"
        entries.append(f"{parameter.python_name}: {annotation} = {default}")
    if include_timeout:
        entries.append("timeout: float | None = None")
    return entries


def _protocol_name(namespace: str, method_name: str, *, async_mode: bool) -> str:
    prefix = "Async" if async_mode else ""
    return f"_{prefix}{_classify(namespace)}{_classify(method_name)}Method"


def _namespace_class_name(namespace: str, *, async_mode: bool) -> str:
    prefix = "Async" if async_mode else ""
    return f"{prefix}{_classify(namespace)}Namespace"


def _manual_app_class_name(service_name: str, *, async_mode: bool) -> str:
    prefix = "Async" if async_mode else ""
    return f"{prefix}SilverApps{_classify(service_name)}Service"


def _silver_namespace_class_name(namespace_path: tuple[str, ...], *, async_mode: bool) -> str:
    prefix = "Async" if async_mode else ""
    joined = "".join(_classify(part) for part in namespace_path)
    return f"{prefix}Silver{joined}Namespace"


def _classify(value: str) -> str:
    return "".join(part.capitalize() for part in value.split("_"))


def _is_pagination_parameter(parameter: SDKParameterMetadata) -> bool:
    return parameter.python_name in {"page", "page_size"}


def _escape_inline(value: str) -> str:
    return value.replace("|", "\\|")


def _escape_table(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", "<br>")


def _optionalized_type(type_display: str, required: bool) -> str:
    if required or "None" in type_display:
        return type_display
    return f"{type_display} | None"
