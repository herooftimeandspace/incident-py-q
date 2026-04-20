"""Coverage-oriented tests for Silver helper branches."""

from __future__ import annotations

import asyncio
import json
from pathlib import Path
from types import SimpleNamespace
from typing import Any

import pytest

from incident_py_q.config import ClientConfig
from incident_py_q.schema.registry import SchemaRegistry
from incident_py_q.silver import inventory as inventory_module
from incident_py_q.silver.inventory import (
    SilverMethodMetadata,
    SilverParameterMetadata,
    _Aggregate,
    _build_body_parameters,
    _build_description,
    _build_method_name,
    _build_query_parameters,
    _build_summary,
    _build_variable_position_map,
    _can_parameterize_named_segment,
    _dedupe_method_names,
    _infer_type_display,
    _is_discarded_candidate,
    _load_observed_requests,
    _namespace_path_from_normalized,
    _normalize_for_matching,
    _ObservedRequest,
    _parse_request_body,
    _path_parameter_name,
    _route_shape,
    _template_raw_path,
    legacy_app_inventory_records,
    load_silver_inventory,
    silver_inventory_payload,
    silver_inventory_records,
)
from incident_py_q.silver.runtime import (
    AsyncSilverAppsNamespace,
    AsyncSilverOperationMethod,
    SilverGenericNamespace,
    SilverNamespaceBase,
    SilverRootNamespace,
    _absolute_silver_url,
    _annotation_for_parameter,
    _ensure_namespace,
    _silver_headers,
    _split_request_arguments,
    _tenant_origin,
)


def test_inventory_loader_helpers_and_serializers(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    (data_dir / "silver_inventory.json").write_text(json.dumps({"endpoints": {}}), encoding="utf-8")
    monkeypatch.setattr(inventory_module, "files", lambda _: tmp_path)
    with pytest.raises(ValueError):
        load_silver_inventory()

    (data_dir / "silver_inventory.json").write_text(
        json.dumps({"endpoints": ["skip-me", {"namespace_path": ["analytics"], "method_name": "get_stats", "http_method": "GET", "route": "/api/v1.0/analytics/agent-current-stats", "parameters": [], "summary": "s", "description": "d", "typed_return": "_JSONPayload", "raw_return": "_JSONPayload", "sources": ["sample.har"], "status_codes": [200], "uses_app_headers": False}]}),
        encoding="utf-8",
    )
    loaded = load_silver_inventory()
    assert loaded[0].method_name == "get_stats"
    assert silver_inventory_payload(loaded)["endpoints"]
    assert silver_inventory_records(loaded)[0]["provenance"] == "silver"
    assert any(
        entry["path"] == "/api/v1.0/app-registry/apps/false"
        for entry in legacy_app_inventory_records(loaded)
    )


def test_inventory_private_helpers_cover_branch_cases(
    tiny_registry: SchemaRegistry,
    tmp_path: Path,
) -> None:
    assert _normalize_for_matching("/api/v1.0/assets/") == "/assets"
    assert _namespace_path_from_normalized("/") == ("root",)
    assert _build_method_name(
        http_method="GET",
        namespace_path=("apps", "google_device_data"),
        normalized_route="/apps/googleDeviceData/api/googleDeviceData/data/models/distinct",
    ) == "get_models_distinct"
    assert _route_shape("/api/v1.0/app-registry/app/{app_key}") == "/api/v1.0/app-registry/app/{}"
    assert _can_parameterize_named_segment(["app-registry", "app", "foo"], 2, {"foo", "bar"}) is True
    assert _path_parameter_name(segments=["assets", "serial", "{serial}"], position=2, values=["ABC123"]) == "serial"
    assert _infer_type_display(["true", "false"]) == "bool"
    assert _infer_type_display(["1", "2"]) == "int"
    assert _infer_type_display([1.5, 2.5]) == "float"
    assert _is_discarded_candidate(raw_path="/%7B%7B%20$ctrl.IconUri%20%7D%7D", normalized_path="/%7B%7B%20$ctrl.IconUri%20%7D%7D")

    har_path = tmp_path / "edge.har"
    har_payload = {
        "log": {
            "entries": [
                "skip-me",
                {"request": {}, "response": {}},
                {
                    "request": {"method": "GET", "url": "https://tenant.example/api/v1.0/things"},
                    "response": {"status": 200},
                },
                {
                    "request": {"method": "GET", "url": "https://tenant.example/api/v1.0/img/logo.png"},
                    "response": {"status": 200},
                },
                {
                    "request": {"method": "POST", "url": "https://tenant.example/api/v1.0/files/entity/one/two", "postData": {"text": "not-json"}},
                    "response": {"status": 202},
                },
            ]
        }
    }
    har_path.write_text(json.dumps(har_payload), encoding="utf-8")
    observed = _load_observed_requests(har_files=[har_path], registry=tiny_registry)
    assert len(observed) == 1
    assert _parse_request_body({"postData": {"text": "not-json"}}) == "not-json"

    variable_positions = _build_variable_position_map(
        [
            _ObservedRequest("GET", "/api/v1.0/app-registry/app/googleDeviceData", "/app-registry/app/googleDeviceData", "a.har", 200, {}, None),
            _ObservedRequest("GET", "/api/v1.0/app-registry/app/microsoftIntune", "/app-registry/app/microsoftIntune", "a.har", 200, {}, None),
        ]
    )
    assert _template_raw_path(
        "/api/v1.0/app-registry/app/googleDeviceData",
        "/app-registry/app/googleDeviceData",
        variable_positions,
    ) == "/api/v1.0/app-registry/app/{app_key}"

    body_text_params = _build_body_parameters(
        [_ObservedRequest("POST", "/x", "/x", "a.har", 200, {}, "text-body")]
    )
    assert body_text_params[0].python_name == "json_body"

    complex_body_params = _build_body_parameters(
        [_ObservedRequest("POST", "/x", "/x", "a.har", 200, {}, {"Entity": {"Id": "1"}})]
    )
    assert complex_body_params[0].type_display == "Mapping[str, Any]"

    simple_query_params = _build_query_parameters(
        [
            _ObservedRequest("GET", "/x", "/x", "a.har", 200, {"limit": "10"}, None),
            _ObservedRequest("GET", "/x", "/x", "a.har", 200, {"limit": "20"}, None),
        ]
    )
    assert simple_query_params[0].python_name == "limit"

    duplicate_methods = _dedupe_method_names(
        [
            SilverMethodMetadata(("analytics",), "get_stats", "GET", "/one", (), "s", "d", "_JSONPayload", "_JSONPayload", ("a.har",), (), False),
            SilverMethodMetadata(("analytics",), "get_stats", "GET", "/two", (), "s", "d", "_JSONPayload", "_JSONPayload", ("a.har",), (), False),
        ]
    )
    assert duplicate_methods[1].method_name == "get_stats_2"

    aggregate = _Aggregate(
        method="GET",
        route="/api/v1.0/analytics/agent-current-stats",
        normalized_route="/analytics/agent-current-stats",
        namespace_path=("analytics",),
        method_name="get_agent_current_stats",
        uses_app_headers=False,
        parameters=[],
        sources={"a.har"},
        status_codes={200},
    )
    assert "Silver" in _build_description(aggregate)
    assert "client.silver.analytics" in _build_summary(aggregate)


def test_runtime_helper_branches() -> None:
    with pytest.raises(ValueError):
        _tenant_origin("tenant.example")

    assert _absolute_silver_url("https://tenant.example/api/v1", "https://override.example/x") == "https://override.example/x"
    assert _absolute_silver_url("https://tenant.example/api/v1", "/apps/test") == "https://tenant.example/apps/test"
    assert _absolute_silver_url("https://tenant.example/api/v1", "/assets/serial/{serial}") == "/assets/serial/{serial}"

    assert _annotation_for_parameter(
        SilverParameterMetadata("flag", "flag", "query", False, "bool", "flag")
    ) is bool
    assert _annotation_for_parameter(
        SilverParameterMetadata("value", "value", "query", False, "Mapping[str, Any]", "body")
    ) is Any

    config = ClientConfig(base_url="https://tenant.example/api/v1", api_token="token", app_headers={"X-App-Token": "secret"})
    metadata = SilverMethodMetadata(
        namespace_path=("apps", "widgets"),
        method_name="get_widget",
        http_method="GET",
        route="/api/v1.0/apps/widgets/{widget_id}",
        parameters=(
            SilverParameterMetadata("widget_id", "widget_id", "path", True, "str", "id"),
            SilverParameterMetadata("expand", "expand", "query", False, "str", "expand"),
            SilverParameterMetadata("json_body", "json_body", "body", False, "Mapping[str, Any]", "body"),
        ),
        summary="s",
        description="d",
        typed_return="_JSONPayload",
        raw_return="_JSONPayload",
        sources=("a.har",),
        status_codes=(200,),
        uses_app_headers=True,
    )
    assert _silver_headers(config, metadata) == {"X-App-Token": "secret"}
    path_params, query_params, json_body = _split_request_arguments(
        metadata,
        {"widget_id": "abc", "expand": "full", "json_body": {"ok": True}},
    )
    assert path_params == {"widget_id": "abc"}
    assert query_params == {"expand": "full"}
    assert json_body == {"ok": True}

    namespace = SilverNamespaceBase("root")
    namespace._register_method("ping", lambda: None)
    child = SilverGenericNamespace("child")
    namespace._register_namespace("child", child)
    assert namespace.list_methods() == ["ping"]
    assert namespace.list_namespaces() == ["child"]
    assert "ping" in dir(namespace)


def test_async_runtime_helper_and_namespace_merge() -> None:
    captured: dict[str, Any] = {}

    class AsyncClientStub:
        def __init__(self) -> None:
            self.config = ClientConfig(
                base_url="https://tenant.example/api/v1",
                api_token="token",
                app_headers={"X-App-Token": "secret"},
            )

        async def request(self, method: str, path: str, **kwargs: Any) -> dict[str, Any]:
            captured["request_method"] = method
            captured["request_path"] = path
            captured["request_kwargs"] = kwargs
            return {"ok": True}

        async def request_silver(
            self,
            metadata: SilverMethodMetadata,
            **kwargs: Any,
        ) -> dict[str, Any]:
            captured["metadata"] = metadata
            captured["method"] = metadata.http_method
            captured["path"] = metadata.route
            captured["kwargs"] = kwargs
            return {"ok": True}

    metadata = SilverMethodMetadata(
        namespace_path=("apps", "widgets"),
        method_name="get_widget",
        http_method="POST",
        route="/api/v1.0/apps/widgets/{widget_id}",
        parameters=(
            SilverParameterMetadata("widget_id", "widget_id", "path", True, "str", "id"),
            SilverParameterMetadata("json_body", "json_body", "body", False, "Mapping[str, Any]", "body"),
        ),
        summary="s",
        description="d",
        typed_return="_JSONPayload",
        raw_return="_JSONPayload",
        sources=("a.har",),
        status_codes=(200,),
        uses_app_headers=True,
    )
    method = AsyncSilverOperationMethod(client=AsyncClientStub(), metadata=metadata)
    assert asyncio.run(method(widget_id="abc", json_body={"ok": True})) == {"ok": True}
    assert captured["path"] == "/api/v1.0/apps/widgets/{widget_id}"
    assert captured["kwargs"]["path_params"] == {"widget_id": "abc"}
    assert captured["kwargs"]["headers"] == {"X-App-Token": "secret"}

    root = SilverRootNamespace("silver")
    lookup: dict[tuple[str, ...], Any] = {}
    namespace = _ensure_namespace(
        root=root,
        namespace_lookup=lookup,
        namespace_path=("apps",),
        async_mode=True,
        client=SimpleNamespace(
            config=ClientConfig(base_url="https://tenant.example/api/v1", api_token="token"),
            request=None,
            request_silver=None,
        ),
    )
    assert isinstance(namespace, AsyncSilverAppsNamespace)
