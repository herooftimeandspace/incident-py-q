"""HAR-derived contract tests for undocumented app-path endpoint support."""

from __future__ import annotations

import json
from pathlib import Path

from incident_py_q.apps.validator import AppSchemaValidator


def test_required_har_endpoints_are_present() -> None:
    inventory = json.loads(Path("tests/fixtures/har_app_inventory.json").read_text(encoding="utf-8"))
    endpoints = {(entry["method"], entry["path"]) for entry in inventory}

    required = {
        ("GET", "/api/v1.0/app-registry/apps/false"),
        ("POST", "/apps/microsoftIntune/api/microsoftIntune/data/assets/lookup"),
        ("GET", "/apps/microsoftIntune/api/microsoftIntune/remoteactions"),
        ("POST", "/apps/mosyleManager/api/mosyleManager/data/assets/lookup"),
        ("GET", "/apps/mosyleManager/api/mosyleManager/remoteactions"),
        ("POST", "/apps/googleDeviceData/api/googleDeviceData/data/assets/get-google-device"),
        ("GET", "/apps/googleDeviceData/api/googleDeviceData/remoteactions"),
        ("GET", "/apps/googleDeviceData/api/googleDeviceData/sync/options"),
    }
    assert required.issubset(endpoints)


def test_har_sample_payloads_conform_to_bundled_schemas() -> None:
    payloads = json.loads(Path("tests/fixtures/har_app_payloads.json").read_text(encoding="utf-8"))
    validator = AppSchemaValidator()

    validator.validate("registry_response", payloads["registry_response"])
    validator.validate("intune_lookup_request", payloads["intune_lookup_request"])
    validator.validate("mosyle_lookup_request", payloads["mosyle_lookup_request"])
    validator.validate("google_lookup_request", payloads["google_lookup_request"])
    validator.validate("lookup_response", payloads["intune_lookup_response"])
    validator.validate("lookup_response", payloads["mosyle_lookup_response"])
    validator.validate("lookup_response", payloads["google_lookup_response"])
    validator.validate("remote_actions_response", payloads["remote_actions_response"])
    validator.validate("google_sync_options_response", payloads["google_sync_options_response"])
