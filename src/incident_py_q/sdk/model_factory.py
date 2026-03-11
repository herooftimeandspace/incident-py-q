"""Pydantic model generation from Swagger definitions."""

from __future__ import annotations

from typing import Any, cast

from pydantic import BaseModel, ConfigDict, Field, create_model

_SWAGGER_PRIMITIVE_TO_PYTHON: dict[str, Any] = {
    "string": str,
    "integer": int,
    "number": float,
    "boolean": bool,
}


class SwaggerModelFactory:
    """Construct pydantic models for Swagger object definitions.

    The Incident IQ contract set is Swagger 2.0 and heavily definition-driven.
    This factory keeps generation conservative:
    - Unknown/complex constructs fall back to `Any`
    - `x-nullable` is mapped to `None | T`
    - Additional fields are allowed to keep compatibility with schema drift
    """

    def __init__(self, definitions: dict[str, dict[str, Any]]) -> None:
        self._definitions = definitions
        self._models: dict[str, type[BaseModel]] = {}
        self._building: set[str] = set()

    def get_model(self, name: str) -> type[BaseModel]:
        """Return a pydantic model class for a definition name."""
        existing = self._models.get(name)
        if existing is not None:
            return existing

        if name in self._building:
            return create_model(
                f"{name}Recursive",
                __config__=ConfigDict(extra="allow"),
            )

        schema = self._definitions.get(name)
        if schema is None:
            return create_model(
                f"{name}Unknown",
                __config__=ConfigDict(extra="allow"),
            )

        self._building.add(name)
        model = self._build_object_model(name, schema)
        self._models[name] = model
        self._building.remove(name)
        return model

    def type_from_schema(self, schema: dict[str, Any] | None) -> Any:
        """Convert a Swagger schema object to a Python type annotation."""
        if not schema:
            return Any

        if "enum" in schema and isinstance(schema["enum"], list) and schema["enum"]:
            enum_values = [value for value in schema["enum"] if isinstance(value, str)]
            if enum_values:
                return _apply_nullable(str, schema)

        if "$ref" in schema:
            ref_value = schema["$ref"]
            ref_name = str(ref_value).split("/")[-1]
            annotation: Any = self.get_model(ref_name)
            return _apply_nullable(annotation, schema)

        schema_type = schema.get("type")
        if isinstance(schema_type, list):
            non_null = [item for item in schema_type if item != "null"]
            if len(non_null) == 1:
                inner = self.type_from_schema({"type": non_null[0], **_without(schema, "type")})
                return inner | None
            return Any

        if schema_type == "array":
            annotation = list[Any]
            return _apply_nullable(annotation, schema)

        if schema_type == "object":
            properties = schema.get("properties")
            if isinstance(properties, dict) and properties:
                inline_name = "InlineObject"
                model = self._build_object_model(inline_name, schema)
                return _apply_nullable(model, schema)
            annotation = dict[str, Any]
            return _apply_nullable(annotation, schema)

        if isinstance(schema_type, str) and schema_type in _SWAGGER_PRIMITIVE_TO_PYTHON:
            annotation = _SWAGGER_PRIMITIVE_TO_PYTHON[schema_type]
            return _apply_nullable(annotation, schema)

        if "anyOf" in schema:
            return Any

        return Any

    def _build_object_model(self, name: str, schema: dict[str, Any]) -> type[BaseModel]:
        raw_properties = schema.get("properties")
        properties = raw_properties if isinstance(raw_properties, dict) else {}
        required_names = set(schema.get("required") or [])
        fields: dict[str, tuple[Any, Any]] = {}

        for prop_name, prop_schema in properties.items():
            annotation = self.type_from_schema(prop_schema if isinstance(prop_schema, dict) else None)
            default: Any = ... if prop_name in required_names else None
            fields[prop_name] = (annotation, Field(default=default))

        return _create_model(name, fields)


def _apply_nullable(annotation: Any, schema: dict[str, Any]) -> Any:
    nullable_type = schema.get("type")
    if schema.get("x-nullable") is True:
        return annotation | None
    if isinstance(nullable_type, list) and "null" in nullable_type:
        return annotation | None
    return annotation


def _without(schema: dict[str, Any], key: str) -> dict[str, Any]:
    return {k: v for k, v in schema.items() if k != key}


def _create_model(name: str, fields: dict[str, tuple[Any, Any]]) -> type[BaseModel]:
    model = create_model(
        name,
        __config__=ConfigDict(extra="allow"),
        **cast(Any, fields),
    )
    return cast(type[BaseModel], model)
