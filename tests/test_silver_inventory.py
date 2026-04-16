"""Tests for HAR-derived Silver inventory extraction."""

from __future__ import annotations

import json
from pathlib import Path

from incident_py_q.schema.registry import SchemaRegistry
from incident_py_q.silver import extract_silver_inventory


def test_extract_silver_inventory_filters_golden_and_discards_static_noise(
    tiny_registry: SchemaRegistry,
    tmp_path: Path,
) -> None:
    har_path = tmp_path / "sample.har"
    har_payload = {
        "log": {
            "entries": [
                {
                    "request": {
                        "method": "GET",
                        "url": "https://tenant.example/api/v1.0/things?page=1",
                    },
                    "response": {"status": 200},
                },
                {
                    "request": {
                        "method": "GET",
                        "url": "https://tenant.example/api/v1.0/core/app.js",
                    },
                    "response": {"status": 200},
                },
                {
                    "request": {
                        "method": "GET",
                        "url": "https://tenant.example/api/v1.0/app-registry/app/googleDeviceData",
                    },
                    "response": {"status": 200},
                },
                {
                    "request": {
                        "method": "GET",
                        "url": "https://tenant.example/api/v1.0/app-registry/app/microsoftIntune",
                    },
                    "response": {"status": 200},
                },
                {
                    "request": {
                        "method": "POST",
                        "url": "https://tenant.example/api/v1.0/custom-fields/for/ticket?$s=999999",
                        "postData": {"text": json.dumps({"Entity": {"TicketId": "ticket-1"}})},
                    },
                    "response": {"status": 200},
                },
            ]
        }
    }
    har_path.write_text(json.dumps(har_payload), encoding="utf-8")

    silver = extract_silver_inventory(har_files=[har_path], registry=tiny_registry)

    routes = {(method.http_method, method.route) for method in silver}

    assert ("GET", "/api/v1.0/app-registry/app/{app_key}") in routes
    assert ("POST", "/api/v1.0/custom-fields/for/ticket") in routes
    assert ("GET", "/assets/serial/{serial}") in routes
    assert not any("/core/" in route for _, route in routes)
    assert not any(route.endswith("/things") for _, route in routes)

    custom_fields = next(method for method in silver if method.route == "/api/v1.0/custom-fields/for/ticket")
    assert [parameter.python_name for parameter in custom_fields.parameters] == ["s", "json_body"]

