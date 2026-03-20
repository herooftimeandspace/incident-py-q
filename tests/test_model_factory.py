"""Tests for Swagger model generation helpers."""

from __future__ import annotations

from typing import Any, get_origin

from pydantic import BaseModel

from incident_py_q.sdk.model_factory import SwaggerModelFactory


def _factory() -> SwaggerModelFactory:
    return SwaggerModelFactory(
        {
            "Thing": {
                "type": "object",
                "required": ["id"],
                "properties": {
                    "id": {"type": "string"},
                    "flag": {"type": "boolean", "x-nullable": True},
                },
            },
            "Node": {
                "type": "object",
                "properties": {"child": {"$ref": "#/definitions/Node"}},
            },
        }
    )


def test_get_model_returns_cached_and_unknown_models() -> None:
    factory = _factory()

    thing_model = factory.get_model("Thing")
    assert factory.get_model("Thing") is thing_model

    unknown_model = factory.get_model("Missing")
    payload = unknown_model.model_validate({"extra": "value"})
    assert payload.model_dump()["extra"] == "value"


def test_get_model_handles_recursive_definitions() -> None:
    factory = _factory()
    node_model = factory.get_model("Node")

    payload = node_model.model_validate({"child": {"child": {}}})
    assert "child" in payload.model_dump()


def test_type_from_schema_covers_refs_inline_objects_and_primitives() -> None:
    factory = _factory()

    ref_type = factory.type_from_schema({"$ref": "#/definitions/Thing"})
    inline_type = factory.type_from_schema(
        {
            "type": "object",
            "required": ["name"],
            "properties": {"name": {"type": "string"}},
        }
    )
    array_type = factory.type_from_schema({"type": "array", "items": {"type": "string"}})
    dict_type = factory.type_from_schema({"type": "object"})

    assert isinstance(ref_type, type)
    assert issubclass(ref_type, BaseModel)
    assert isinstance(inline_type, type)
    assert issubclass(inline_type, BaseModel)
    assert get_origin(array_type) is list
    assert get_origin(dict_type) is dict
    assert factory.type_from_schema({"type": "integer"}) is int
    assert factory.type_from_schema({"type": "number"}) is float
    assert factory.type_from_schema({"type": "boolean"}) is bool


def test_type_from_schema_handles_nullable_and_fallback_cases() -> None:
    factory = _factory()

    nullable_enum = factory.type_from_schema({"enum": ["a", "b"], "x-nullable": True})
    nullable_union = factory.type_from_schema({"type": ["string", "null"]})
    ambiguous_union = factory.type_from_schema({"type": ["string", "number", "null"]})
    any_of = factory.type_from_schema({"anyOf": [{"type": "string"}]})
    empty = factory.type_from_schema(None)

    assert type(None) in nullable_enum.__args__
    assert type(None) in nullable_union.__args__
    assert ambiguous_union is Any
    assert any_of is Any
    assert empty is Any
