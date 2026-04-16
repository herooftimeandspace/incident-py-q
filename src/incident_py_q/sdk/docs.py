"""SDK documentation and typing artifact generation."""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path

from incident_py_q.apps import AppMethodMetadata, AppParameterMetadata, build_app_method_metadata
from incident_py_q.schema.registry import SchemaRegistry

from .runtime import SDKMethodMetadata, SDKParameterMetadata, build_sdk_metadata


def render_sdk_index(metadata: tuple[SDKMethodMetadata, ...]) -> str:
    """Render the SDK reference landing page."""
    grouped = _group_metadata(metadata)
    app_methods = build_app_method_metadata()
    lines = [
        "# SDK Reference",
        "",
        "Generated from bundled Incident IQ controller contracts.",
        "",
        "Use these pages to discover the dynamic namespace methods available on "
        "`Client` and `AsyncClient`.",
        "",
        "| Namespace | Canonical Methods | Page |",
        "| --- | ---: | --- |",
    ]
    lines.append(
        f"| `apps` | {len(app_methods)} | [`client.apps`](apps.md) |"
    )
    for namespace, methods in grouped.items():
        lines.append(
            f"| `{namespace}` | {len(methods)} | "
            f"[`client.{namespace}`]({namespace}.md) |"
        )
    return "\n".join(lines) + "\n"


def render_apps_reference(methods: tuple[AppMethodMetadata, ...] | None = None) -> str:
    """Render the manual app-path reference page."""
    app_methods = methods or build_app_method_metadata()
    grouped: dict[str, list[AppMethodMetadata]] = defaultdict(list)
    labels: dict[str, str] = {}
    for method in app_methods:
        grouped[method.service_name].append(method)
        labels[method.service_name] = method.service_label

    lines = [
        "# `apps` Namespace",
        "",
        "Sync client access: `client.apps`",
        "",
        "Async client access: `client.apps` with `await` for async service methods.",
        "",
        "These methods cover the HAR-derived app-path APIs that are not part of the "
        "schema-driven controller SDK surface.",
        "",
        "| Service | Methods | Access Path |",
        "| --- | ---: | --- |",
    ]
    for service_name, methods_for_service in grouped.items():
        lines.append(
            f"| `{service_name}` | {len(methods_for_service)} | "
            f"`client.apps.{service_name}` |"
        )
    lines.append("")

    for service_name, methods_for_service in grouped.items():
        lines.extend(
            [
                f"## `{service_name}`",
                "",
                f"{labels[service_name]} service available at `client.apps.{service_name}`.",
                "",
            ]
        )
        for method in methods_for_service:
            lines.extend(
                [
                    f"### `{method.method_name}`",
                    "",
                    f"- Sync: `{method.sync_call}`",
                    f"- Async: `{method.async_call}`",
                ]
            )
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

    return "\n".join(lines).rstrip() + "\n"


def render_namespace_reference(namespace: str, methods: tuple[SDKMethodMetadata, ...]) -> str:
    """Render one namespace SDK reference page."""
    alias_rows: list[str] = []
    for method in methods:
        for alias_name in method.aliases:
            alias_rows.append(
                f"| `{alias_name}` | `{method.name}` | "
                f"`{method.operation.method} {method.operation.path_template}` |"
            )

    lines = [
        f"# `{namespace}` Namespace",
        "",
        f"Sync client access: `client.{namespace}`",
        "",
        f"Async client access: `client.{namespace}` with `await` on method calls.",
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

        if method.parameters:
            lines.extend(
                [
                    "#### Parameters",
                    "",
                    "| Python Arg | API Name | In | Required | Type | Schema / Model | Description |",
                    "| --- | --- | --- | --- | --- | --- | --- |",
                ]
            )
            for parameter in method.parameters:
                lines.append(_render_parameter_row(parameter))
            lines.append("")
        else:
            lines.extend(["#### Parameters", "", "This operation does not define request parameters.", ""])

        lines.extend(
            [
                "#### Returns",
                "",
                f"- Typed call return: `{method.response_type_display}`",
                f"- Raw payload return: `{method.raw_return_type_display}`",
            ]
        )
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
        lines.extend(["", "---", ""])

    return "\n".join(lines).rstrip() + "\n"


def render_client_stub(registry: SchemaRegistry) -> str:
    """Render the static typing stub for the dynamic client surface."""
    metadata = build_sdk_metadata(registry)
    grouped = _group_metadata(metadata)
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
        "from collections.abc import Mapping",
        "from typing import Any, Protocol",
        "",
        "import httpx",
        "from pydantic import BaseModel",
        "",
        "from .apps import AppsNamespace, AsyncAppsNamespace",
        "from .config import ClientConfig",
        "from .schema.registry import SchemaRegistry",
        "from .sdk.runtime import AsyncNamespace, Namespace",
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

    lines.extend(_render_client_class_stub(grouped, async_mode=False))
    lines.append("")
    lines.extend(_render_client_class_stub(grouped, async_mode=True))
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

    docs_root.mkdir(parents=True, exist_ok=True)
    for existing in docs_root.glob("*.md"):
        existing.unlink()

    (docs_root / "index.md").write_text(render_sdk_index(metadata), encoding="utf-8")
    (docs_root / "apps.md").write_text(render_apps_reference(), encoding="utf-8")
    for namespace, methods in grouped.items():
        (docs_root / f"{namespace}.md").write_text(
            render_namespace_reference(namespace, methods),
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


def _sync_call_example(method: SDKMethodMetadata) -> str:
    return f"client.{method.namespace}.{method.name}{_signature_suffix(method)}"


def _async_call_example(method: SDKMethodMetadata) -> str:
    return f"await client.{method.namespace}.{method.name}{_signature_suffix(method)}"


def _sync_raw_call_example(method: SDKMethodMetadata) -> str:
    return f"client.{method.namespace}.{method.name}.raw{_signature_suffix(method)}"


def _iter_pages_call_example(method: SDKMethodMetadata) -> str:
    args = _render_call_arguments(method, exclude_pagination=True)
    extra = "start_page=1, page_size=100, max_pages=None"
    joined = ", ".join(part for part in [extra, args] if part)
    return f"client.{method.namespace}.{method.name}.iter_pages({joined})"


def _signature_suffix(method: SDKMethodMetadata) -> str:
    arguments = _render_call_arguments(method, exclude_pagination=False)
    return f"({arguments})" if arguments else "()"


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
    raw_return = "_JSONPayload"
    lines: list[str] = []
    if not async_mode:
        lines.append(f"# OperationId: {method.operation.operation_id}")
    lines.extend(
        [
            f"class {protocol_name}(Protocol):",
            f"    {'async ' if async_mode else ''}def __call__{_stub_signature(method, return_type=return_type)}: ...",
            f"    {'async ' if async_mode else ''}def raw{_stub_signature(method, return_type=raw_return)}: ...",
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
    lines = [f"class {class_name}({base_name}):"]
    lines.append("    def list_methods(self) -> list[str]: ...")
    for method in methods:
        protocol_name = _protocol_name(namespace, method.name, async_mode=async_mode)
        lines.append(f"    {method.name}: {protocol_name}")
        for alias_name in method.aliases:
            lines.append(f"    {alias_name}: {protocol_name}")
    return lines


def _render_client_class_stub(
    grouped: dict[str, tuple[SDKMethodMetadata, ...]],
    *,
    async_mode: bool,
) -> list[str]:
    class_name = "AsyncClient" if async_mode else "Client"
    http_client_type = "httpx.AsyncClient | None" if async_mode else "httpx.Client | None"
    return_type = "_JSONPayload"
    request_prefix = "async " if async_mode else ""
    close_prefix = "async " if async_mode else ""
    context_prefix = "async " if async_mode else ""
    enter_name = "__aenter__" if async_mode else "__enter__"
    exit_name = "__aexit__" if async_mode else "__exit__"

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
        "    def __getattr__(self, name: str) -> Any: ...",
        f"    {close_prefix}def close(self) -> None: ...",
        f"    {context_prefix}def {enter_name}(self) -> {class_name}: ...",
        f"    {context_prefix}def {exit_name}(self, *_: Any) -> None: ...",
        "    "
        + request_prefix
        + "def request("
        "self, method: str, path: str, *, path_params: Mapping[str, Any] | None = None, "
        "params: Mapping[str, Any] | None = None, json: Any | None = None, "
        "headers: Mapping[str, str] | None = None, timeout: float | None = None"
        f") -> {return_type}: ...",
    ]

    for namespace in grouped:
        lines.append(
            f"    {namespace}: {_namespace_class_name(namespace, async_mode=async_mode)}"
        )
    lines.append(f"    apps: {'AsyncAppsNamespace' if async_mode else 'AppsNamespace'}")
    return lines


def _stub_signature(method: SDKMethodMetadata, *, return_type: str) -> str:
    params = _stub_param_list(method, include_timeout=True, exclude_pagination=False)
    return f"({params}) -> {return_type}"


def _iter_pages_signature(method: SDKMethodMetadata, *, return_type: str) -> str:
    params = [
        "self",
        "*",
        "start_page: int = 1",
        "page_size: int = 100",
        "max_pages: int | None = None",
    ]
    call_params = _stub_param_entries(method, include_timeout=False, exclude_pagination=True)
    params.extend(call_params)
    return f"({', '.join(params)}) -> {return_type}"


def _stub_param_list(
    method: SDKMethodMetadata,
    *,
    include_timeout: bool,
    exclude_pagination: bool,
) -> str:
    params = ["self", "*"]
    params.extend(
        _stub_param_entries(
            method,
            include_timeout=include_timeout,
            exclude_pagination=exclude_pagination,
        )
    )
    return ", ".join(params)


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
            annotation = _optional_stub_annotation(annotation)
        default = "" if parameter.required else " = None"
        entries.append(f"{parameter.python_name}: {annotation}{default}")
    if include_timeout:
        entries.append("timeout: float | None = None")
    return entries


def _protocol_name(namespace: str, method_name: str, *, async_mode: bool) -> str:
    prefix = "Async" if async_mode else ""
    return f"_{prefix}{_to_pascal_case(namespace)}{_to_pascal_case(method_name)}Method"


def _namespace_class_name(namespace: str, *, async_mode: bool) -> str:
    prefix = "Async" if async_mode else ""
    return f"{prefix}{_to_pascal_case(namespace)}Namespace"


def _to_pascal_case(value: str) -> str:
    return "".join(part[:1].upper() + part[1:] for part in value.split("_") if part)


def _is_pagination_parameter(parameter: SDKParameterMetadata) -> bool:
    return parameter.python_name in {"page", "page_number", "page_size", "s", "p", "limit"}


def _optional_stub_annotation(annotation: str) -> str:
    if "None" in annotation:
        return annotation
    return f"{annotation} | None"


def _escape_table(value: str) -> str:
    return value.replace("\n", " ").replace("|", "\\|")


def _escape_inline(value: str) -> str:
    return value.replace("`", "")
