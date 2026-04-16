"""Coverage tests for Swagger model factory branches."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel

from incident_py_q.sdk.model_factory import (
    SwaggerModelFactory,
    _apply_nullable,
    _create_model,
    _without,
)


def test_factory_get_model_unknown_and_cached_paths() -> None:
    factory = SwaggerModelFactory(definitions={})
    unknown = factory.get_model("Missing")
    assert issubclass(unknown, BaseModel)
    assert unknown.__name__.endswith("Unknown")

    defs = {
        "Thing": {
            "type": "object",
            "required": ["id"],
            "properties": {"id": {"type": "string"}},
        }
    }
    factory2 = SwaggerModelFactory(definitions=defs)
    first = factory2.get_model("Thing")
    second = factory2.get_model("Thing")
    assert first is second


def test_factory_recursive_definition_branch() -> None:
    defs = {
        "Node": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "child": {"$ref": "#/definitions/Node"},
            },
        }
    }
    factory = SwaggerModelFactory(definitions=defs)
    model = factory.get_model("Node")
    instance = model.model_validate({"name": "root", "child": {"name": "leaf"}})
    assert instance.model_dump()["name"] == "root"


def test_type_from_schema_branches() -> None:
    factory = SwaggerModelFactory(
        definitions={
            "Thing": {"type": "object", "properties": {"id": {"type": "string"}}},
        }
    )
    assert factory.type_from_schema(None) is Any
    assert factory.type_from_schema({}) is Any

    enum_type = factory.type_from_schema({"enum": ["a", "b"]})
    assert enum_type is str

    ref_type = factory.type_from_schema({"$ref": "#/definitions/Thing"})
    assert isinstance(ref_type, type) and issubclass(ref_type, BaseModel)

    array_nullable = factory.type_from_schema({"type": "array", "x-nullable": True})
    assert array_nullable == list[Any] | None

    object_inline = factory.type_from_schema(
        {"type": "object", "properties": {"id": {"type": "string"}}}
    )
    assert isinstance(object_inline, type) and issubclass(object_inline, BaseModel)

    object_dict = factory.type_from_schema({"type": "object"})
    assert object_dict == dict[str, Any]

    primitive = factory.type_from_schema({"type": "integer"})
    assert primitive is int

    list_nullable_one = factory.type_from_schema({"type": ["string", "null"]})
    assert list_nullable_one == str | None

    list_nullable_many = factory.type_from_schema({"type": ["string", "integer", "null"]})
    assert list_nullable_many is Any

    any_of_branch = factory.type_from_schema({"anyOf": [{"type": "string"}]})
    assert any_of_branch is Any

    fallback = factory.type_from_schema({"type": "custom"})
    assert fallback is Any


def test_model_factory_internal_helpers() -> None:
    assert _apply_nullable(str, {"x-nullable": True}) == str | None
    assert _apply_nullable(str, {"type": ["string", "null"]}) == str | None
    assert _apply_nullable(str, {"type": "string"}) is str

    assert _without({"a": 1, "b": 2}, "a") == {"b": 2}

    model = _create_model("Inline", {"id": (str, ...)})
    parsed = model.model_validate({"id": "abc", "extra": "ok"})
    assert parsed.model_dump()["id"] == "abc"
