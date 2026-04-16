"""Tests for the explicit Silver runtime surface."""

from __future__ import annotations

from typing import Any

import httpx
import pytest
import respx

from incident_py_q import Client
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
