"""Tests for the OpenAPI 3 -> internal Swagger-shaped contract converter."""

from __future__ import annotations

from typing import Any

from incident_py_q.schema.openapi import convert_openapi_document


def _document(**overrides: Any) -> dict[str, Any]:
    base: dict[str, Any] = {
        "openapi": "3.0.0",
        "info": {"title": "Test API", "version": "2.0.0"},
        "paths": {},
        "components": {"schemas": {}},
    }
    base.update(overrides)
    return base


def test_components_schemas_become_definitions_with_rewritten_refs() -> None:
    document = _document(
        components={
            "schemas": {
                "Widget": {
                    "type": "object",
                    "properties": {"part": {"$ref": "#/components/schemas/Part"}},
                },
                "Part": {"type": "object"},
            }
        }
    )

    converted = convert_openapi_document(document)

    assert converted["swagger"] == "2.0"
    assert set(converted["definitions"]) == {"Widget", "Part"}
    assert converted["definitions"]["Widget"]["properties"]["part"]["$ref"] == (
        "#/definitions/Part"
    )


def test_nullable_becomes_x_nullable_for_the_normalization_pass() -> None:
    document = _document(
        components={"schemas": {"Widget": {"type": "string", "nullable": True}}}
    )

    converted = convert_openapi_document(document)
    widget = converted["definitions"]["Widget"]

    assert widget.get("x-nullable") is True
    assert "nullable" not in widget


def test_nullable_false_is_dropped_rather_than_translated() -> None:
    document = _document(
        components={"schemas": {"Widget": {"type": "string", "nullable": False}}}
    )

    widget = convert_openapi_document(document)["definitions"]["Widget"]

    assert "x-nullable" not in widget
    assert "nullable" not in widget


def test_request_body_becomes_a_body_parameter() -> None:
    document = _document(
        paths={
            "/api/v1.0/widgets": {
                "post": {
                    "operationId": "createWidget",
                    "requestBody": {
                        "required": True,
                        "description": "Widget to create",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Widget"}
                            }
                        },
                    },
                    "responses": {},
                }
            }
        }
    )

    operation = convert_openapi_document(document)["paths"]["/api/v1.0/widgets"]["post"]
    body = operation["parameters"][0]

    assert body["name"] == "body"
    assert body["in"] == "body"
    assert body["required"] is True
    assert body["description"] == "Widget to create"
    assert body["schema"]["$ref"] == "#/definitions/Widget"
    assert "x-media-type" not in body


def test_non_json_request_body_records_its_media_type() -> None:
    document = _document(
        paths={
            "/api/v1.0/widgets/import": {
                "post": {
                    "operationId": "importWidgets",
                    "requestBody": {
                        "content": {"multipart/form-data": {"schema": {"type": "object"}}}
                    },
                    "responses": {},
                }
            }
        }
    )

    operation = convert_openapi_document(document)["paths"]["/api/v1.0/widgets/import"]["post"]
    body = operation["parameters"][0]

    assert body["x-media-type"] == "multipart/form-data"
    assert body["required"] is False


def test_request_body_without_a_usable_schema_yields_no_body_parameter() -> None:
    cases: list[Any] = [
        {"required": True},
        {"required": True, "content": {}},
        {"required": True, "content": {"application/json": "not-a-media-object"}},
        {"required": True, "content": {"application/json": {"schema": "not-a-schema"}}},
        "not-a-request-body",
    ]

    for request_body in cases:
        document = _document(
            paths={
                "/api/v1.0/widgets": {
                    "post": {
                        "operationId": "createWidget",
                        "requestBody": request_body,
                        "responses": {},
                    }
                }
            }
        )

        operation = convert_openapi_document(document)["paths"]["/api/v1.0/widgets"]["post"]

        assert "parameters" not in operation, request_body


def test_parameter_schema_type_is_lifted_for_runtime_coercion() -> None:
    document = _document(
        paths={
            "/api/v1.0/widgets/{widgetId}": {
                "parameters": [
                    {"name": "widgetId", "in": "path", "required": True, "schema": {"type": "string"}}
                ],
                "get": {
                    "operationId": "getWidget",
                    "parameters": [
                        {"name": "page", "in": "query", "schema": {"type": "integer"}},
                        {"name": "raw", "in": "query"},
                    ],
                    "responses": {},
                },
            }
        }
    )

    path_item = convert_openapi_document(document)["paths"]["/api/v1.0/widgets/{widgetId}"]

    assert path_item["parameters"][0]["type"] == "string"
    assert path_item["get"]["parameters"][0]["type"] == "integer"
    assert "type" not in path_item["get"]["parameters"][1]


def test_json_response_schema_is_flattened_and_others_are_left_unvalidated() -> None:
    document = _document(
        paths={
            "/api/v1.0/widgets": {
                "get": {
                    "operationId": "listWidgets",
                    "responses": {
                        "200": {
                            "description": "ok",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/Widget"}
                                }
                            },
                        },
                        "204": {"description": "no content"},
                        "500": {
                            "description": "spreadsheet",
                            "content": {"application/octet-stream": {"schema": {"type": "string"}}},
                        },
                        "bad": "not-a-response",
                    },
                }
            }
        }
    )

    responses = convert_openapi_document(document)["paths"]["/api/v1.0/widgets"]["get"]["responses"]

    assert responses["200"]["schema"]["$ref"] == "#/definitions/Widget"
    assert "schema" not in responses["204"]
    assert "schema" not in responses["500"]
    assert "bad" not in responses


def test_non_schema_refs_and_non_dict_path_items_are_left_alone() -> None:
    document = _document(
        paths={
            "/api/v1.0/widgets": "not-a-path-item",
            "/api/v1.0/parts": {
                "get": {
                    "operationId": "listParts",
                    "responses": {"200": {"$ref": "#/components/responses/Shared"}},
                },
                "x-extension": {"kept": True},
            },
        }
    )

    converted = convert_openapi_document(document)

    assert "/api/v1.0/widgets" not in converted["paths"]
    parts = converted["paths"]["/api/v1.0/parts"]
    assert parts["get"]["responses"]["200"]["$ref"] == "#/components/responses/Shared"
    assert "x-extension" not in parts


def test_missing_sections_produce_an_empty_but_valid_document() -> None:
    converted = convert_openapi_document({"openapi": "3.0.0"})

    assert converted["definitions"] == {}
    assert converted["paths"] == {}
    assert converted["info"]["title"] == "Incident IQ API"
    assert "description" not in converted["info"]


def test_info_description_is_preserved_when_present() -> None:
    converted = convert_openapi_document(
        _document(info={"title": "T", "version": "1", "description": "Docs"})
    )

    assert converted["info"]["description"] == "Docs"
