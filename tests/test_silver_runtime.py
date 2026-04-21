"""Tests for the explicit Silver runtime surface."""

from __future__ import annotations

import asyncio
from pathlib import Path
from typing import Any

import httpx
import pytest
import respx

from incident_py_q import AsyncClient, Client
from incident_py_q.schema.registry import SchemaRegistry
from incident_py_q.silver.inventory import SilverMethodMetadata, SilverParameterMetadata


def _stub_silver_metadata() -> tuple[SilverMethodMetadata, ...]:
    return (
        SilverMethodMetadata(
            namespace_path=("analytics",),
            method_name="get_agent_current_stats",
            http_method="GET",
            route="/api/v1.0/analytics/agent-current-stats",
            parameters=(),
            summary="HAR-derived analytics stats route.",
            description="Silver route used for runtime testing.",
            typed_return="dict[str, Any] | list[Any] | None",
            raw_return="dict[str, Any] | list[Any] | None",
            sources=("unit-test.har",),
            status_codes=(200,),
            uses_app_headers=False,
        ),
        SilverMethodMetadata(
            namespace_path=("apps", "widgets"),
            method_name="get_widget",
            http_method="GET",
            route="/api/v1.0/apps/widgets/{widget_id}",
            parameters=(
                SilverParameterMetadata(
                    python_name="widget_id",
                    api_name="widget_id",
                    location="path",
                    required=True,
                    type_display="str",
                    description="Widget identifier.",
                ),
            ),
            summary="HAR-derived widget route.",
            description="Silver route used for runtime testing.",
            typed_return="dict[str, Any] | list[Any] | None",
            raw_return="dict[str, Any] | list[Any] | None",
            sources=("unit-test.har",),
            status_codes=(200,),
            uses_app_headers=True,
        ),
    )


@respx.mock
def test_client_exposes_explicit_silver_surface(
    tiny_registry: SchemaRegistry,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr("incident_py_q.silver.runtime.build_silver_metadata", _stub_silver_metadata)
    respx.get("https://tenant.example/api/v1.0/analytics/agent-current-stats").mock(
        return_value=httpx.Response(200, json={"count": 1})
    )
    respx.get("https://tenant.example/api/v1.0/apps/widgets/widget-123").mock(
        return_value=httpx.Response(200, json={"widgetId": "widget-123"})
    )

    client = Client(
        base_url="https://tenant.example/api/v1",
        api_token="token-123",
        registry=tiny_registry,
        app_headers={"X-App-Token": "secret"},
    )
    try:
        assert client.apps is client.silver.apps
        assert client.silver.analytics.get_agent_current_stats() == {"count": 1}
        widgets: Any = client.silver.apps.widgets
        assert widgets.get_widget(widget_id="widget-123") == {
            "widgetId": "widget-123"
        }
        inventory = client.silver_sdk_inventory()
        assert {entry["namespace"] for entry in inventory} >= {"analytics", "apps.widgets", "apps.registry"}
    finally:
        client.close()


@respx.mock
def test_client_silver_profile_picture_upload_uses_multipart_file(
    tiny_registry: SchemaRegistry,
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    monkeypatch.setattr(
        "incident_py_q.silver.runtime.build_silver_metadata",
        lambda: (
            SilverMethodMetadata(
                namespace_path=("profiles",),
                method_name="post_profile_picture",
                http_method="POST",
                route="/api/v1.0/profiles/{user_id}/picture",
                parameters=(
                    SilverParameterMetadata(
                        python_name="user_id",
                        api_name="user_id",
                        location="path",
                        required=True,
                        type_display="str",
                        description="User identifier.",
                    ),
                    SilverParameterMetadata(
                        python_name="file",
                        api_name="File",
                        location="file",
                        required=True,
                        type_display="str | PathLike[str]",
                        description="File to upload.",
                    ),
                ),
                summary="HAR-derived profile picture upload route.",
                description="Silver route used for multipart runtime testing.",
                typed_return="dict[str, Any] | list[Any] | None",
                raw_return="dict[str, Any] | list[Any] | None",
                sources=("unit-test.har",),
                status_codes=(200,),
                uses_app_headers=False,
            ),
        ),
    )
    route = respx.post("https://tenant.example/api/v1.0/profiles/user-123/picture").mock(
        return_value=httpx.Response(200, json={"ok": True})
    )
    upload_path = tmp_path / "avatar.png"
    upload_path.write_bytes(b"png-bytes")

    client = Client(
        base_url="https://tenant.example/api/v1",
        api_token="token-123",
        registry=tiny_registry,
    )
    try:
        assert client.silver.profiles.post_profile_picture(
            user_id="user-123",
            file=upload_path,
        ) == {"ok": True}
    finally:
        client.close()

    assert route.call_count == 1
    request = route.calls[0].request
    assert "multipart/form-data" in request.headers["content-type"]
    assert b'name="File"' in request.content
    assert b'filename="avatar.png"' in request.content


@respx.mock
def test_async_client_silver_profile_picture_upload_uses_multipart_file(
    tiny_registry: SchemaRegistry,
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    monkeypatch.setattr(
        "incident_py_q.silver.runtime.build_silver_metadata",
        lambda: (
            SilverMethodMetadata(
                namespace_path=("profiles",),
                method_name="post_profile_picture",
                http_method="POST",
                route="/api/v1.0/profiles/{user_id}/picture",
                parameters=(
                    SilverParameterMetadata(
                        python_name="user_id",
                        api_name="user_id",
                        location="path",
                        required=True,
                        type_display="str",
                        description="User identifier.",
                    ),
                    SilverParameterMetadata(
                        python_name="file",
                        api_name="File",
                        location="file",
                        required=True,
                        type_display="str | PathLike[str]",
                        description="File to upload.",
                    ),
                ),
                summary="HAR-derived profile picture upload route.",
                description="Silver route used for multipart runtime testing.",
                typed_return="dict[str, Any] | list[Any] | None",
                raw_return="dict[str, Any] | list[Any] | None",
                sources=("unit-test.har",),
                status_codes=(200,),
                uses_app_headers=False,
            ),
        ),
    )
    route = respx.post("https://tenant.example/api/v1.0/profiles/user-123/picture").mock(
        return_value=httpx.Response(200, json={"ok": True})
    )
    upload_path = tmp_path / "avatar.jpg"
    upload_path.write_bytes(b"jpg-bytes")

    async def run() -> None:
        client = AsyncClient(
            base_url="https://tenant.example/api/v1",
            api_token="token-123",
            registry=tiny_registry,
        )
        try:
            assert await client.silver.profiles.post_profile_picture(
                user_id="user-123",
                file=upload_path,
            ) == {"ok": True}
        finally:
            await client.close()

    asyncio.run(run())

    assert route.call_count == 1
    request = route.calls[0].request
    assert "multipart/form-data" in request.headers["content-type"]
    assert b'name="File"' in request.content
    assert b'filename="avatar.jpg"' in request.content
