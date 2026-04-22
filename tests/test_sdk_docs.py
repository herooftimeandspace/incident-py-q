"""Tests for generated SDK docs and typing artifacts."""

from __future__ import annotations

from pathlib import Path

from incident_py_q.schema.registry import SchemaRegistry
from incident_py_q.sdk.docs import (
    render_apps_reference,
    render_client_stub,
    render_namespace_reference,
    render_silver_namespace_reference,
    render_sdk_index,
    write_sdk_reference_artifacts,
)
from incident_py_q.silver import build_silver_metadata
from incident_py_q.sdk.runtime import build_sdk_metadata, format_operation_docstring


def test_build_sdk_metadata_and_docstring_include_runtime_details(
    tiny_registry: SchemaRegistry,
) -> None:
    metadata = build_sdk_metadata(tiny_registry)
    get_things = next(method for method in metadata if method.name == "get_things")

    assert get_things.aliases == ("list",)
    assert [parameter.python_name for parameter in get_things.parameters] == ["page", "page_size"]
    assert get_things.supports_pagination is True

    docstring = format_operation_docstring(get_things, async_mode=False)
    assert "No contract summary provided." in docstring
    assert "HTTP route: GET /things" in docstring
    assert "client.things.get_things.raw(...)" in docstring
    assert "iter_pages" in docstring


def test_render_namespace_reference_orders_parameters_and_documents_aliases(
    tiny_registry: SchemaRegistry,
) -> None:
    metadata = build_sdk_metadata(tiny_registry)
    methods = tuple(method for method in metadata if method.namespace == "things")

    page = render_namespace_reference("things", methods)

    assert page.count("### `get_things`") == 1
    assert "### `list`" not in page
    assert "| `list` | `get_things` | `GET /things` |" in page
    assert page.index("`page`") < page.index("`page_size`")
    assert "No contract summary provided." in page
    assert "client.things.get_things.iter_pages(start_page=1, page_size=100, max_pages=None, timeout=None)" in page


def test_render_sdk_index_lists_namespaces(tiny_registry: SchemaRegistry) -> None:
    metadata = build_sdk_metadata(tiny_registry)

    index = render_sdk_index(metadata)

    assert "# SDK Reference" in index
    assert "[`client.silver`](silver.md)" in index
    assert "[`client.apps`](apps.md)" in index
    assert "[`client.things`](things.md)" in index


def test_render_client_stub_includes_namespaces_aliases_and_sync_async_methods(
    tiny_registry: SchemaRegistry,
) -> None:
    stub = render_client_stub(tiny_registry)

    assert "class ThingsNamespace(Namespace):" in stub
    assert "class AsyncThingsNamespace(AsyncNamespace):" in stub
    assert "get_things: _ThingsGetThingsMethod" in stub
    assert "list: _ThingsGetThingsMethod" in stub
    assert "async def __call__(self, *, page: int | None = None, page_size: int | None = None, timeout: float | None = None) -> ThingList: ..." in stub
    assert "def iter_pages(self, *, start_page: int = 1, page_size: int = 100, max_pages: int | None = None) -> list[_JSONPayload]: ..." in stub
    assert "things: ThingsNamespace" in stub
    assert "things: AsyncThingsNamespace" in stub
    assert "silver: SilverRootNamespace" in stub
    assert "silver: AsyncSilverRootNamespace" in stub
    assert "apps: SilverAppsNamespace" in stub
    assert "apps: AsyncSilverAppsNamespace" in stub
    assert "from os import PathLike" in stub
    assert "def request(self, method: str, path: str, *, path_params: Mapping[str, Any] | None = None, params: Mapping[str, Any] | None = None, json: Any | None = None, files: Mapping[str, Any] | None = None" in stub
    assert "def post_profile_picture(self, *, user_id: str = ..., file: str | PathLike[str] = ..., timeout: float | None = None) -> _JSONPayload: ..." in stub
    assert "post_my_picture" not in stub
    assert stub.count("# OperationId: Things_GetThings") == 1


def test_render_apps_reference_documents_app_runtime_surface() -> None:
    page = render_apps_reference()

    assert "# `apps` Silver Namespace" in page
    assert "client.silver.apps.microsoft_intune.lookup_asset" in page
    assert "Legacy sync alias: `client.apps`" in page
    assert "POST /apps/microsoftIntune/api/microsoftIntune/data/assets/lookup" in page
    assert "Utility helper (no HTTP request)" in page


def test_write_sdk_reference_artifacts_writes_markdown_and_stub_files(
    tiny_registry: SchemaRegistry,
    tmp_path: Path,
) -> None:
    docs_root = tmp_path / "docs" / "sdk-reference"
    package_root = tmp_path / "src" / "incident_py_q"

    write_sdk_reference_artifacts(
        docs_root=docs_root,
        package_root=package_root,
        registry=tiny_registry,
    )

    assert (docs_root / "index.md").exists()
    assert (docs_root / "apps.md").exists()
    assert (docs_root / "silver.md").exists()
    assert (docs_root / "silver-profiles.md").exists()
    assert (docs_root / "things.md").exists()
    assert (package_root / "client.pyi").exists()
    assert (package_root / "__init__.pyi").exists()


def test_render_silver_profiles_reference_documents_png_normalization() -> None:
    metadata = build_silver_metadata()
    profiles = tuple(method for method in metadata if method.namespace == "profiles")

    page = render_silver_namespace_reference(("profiles",), profiles)

    assert "converts it to PNG" in page
    assert "uploads a PNG no larger than 1 MB" in page
