"""Contract tests derived from bundled Incident IQ schemas."""

from __future__ import annotations

from typing import Any

from jsonschema import validators

from incident_py_q import Client
from incident_py_q.schema.loader import load_stoplight_documents
from incident_py_q.schema.registry import build_schema_registry


def test_bundled_registry_has_expected_shape() -> None:
    documents = load_stoplight_documents()
    registry = build_schema_registry(documents)

    assert len(documents) >= 1
    assert len(registry.operations) >= 1
    assert len(registry.operations_by_namespace) >= 1

    method_path_pairs = {(op.method, op.path_template) for op in registry.operations}
    assert len(method_path_pairs) == len(registry.operations)


def test_all_response_schemas_are_jsonschema_valid() -> None:
    registry = build_schema_registry(load_stoplight_documents())
    validator_cls = validators.validator_for(registry.merged_document)

    for operation in registry.operations:
        for schema in operation.response_schemas.values():
            validator_cls.check_schema(schema)


def test_sdk_inventory_maps_all_operations() -> None:
    registry = build_schema_registry(load_stoplight_documents())
    client = Client(
        base_url="https://example.incidentiq.com/api/v1",
        api_token="placeholder-token",
        registry=registry,
        validate_responses=True,
    )
    inventory = client.sdk_inventory()
    client.close()

    operation_ids = {op.operation_id for op in registry.operations}
    inventory_ids = {entry["operation_id"] for entry in inventory}
    assert operation_ids == inventory_ids


def test_namespace_methods_have_callable_runtime_surface() -> None:
    registry = build_schema_registry(load_stoplight_documents())
    client = Client(
        base_url="https://example.incidentiq.com/api/v1",
        api_token="placeholder-token",
        registry=registry,
    )
    try:
        for namespace in registry.operations_by_namespace:
            namespace_obj: Any = getattr(client, namespace)
            methods = namespace_obj.list_methods()
            assert methods
            for method_name in methods:
                method = getattr(namespace_obj, method_name)
                assert callable(method)
    finally:
        client.close()
