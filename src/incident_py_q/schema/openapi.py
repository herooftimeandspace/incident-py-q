"""Convert the Golden OpenAPI 3.0 contract into the SDK's internal document shape.

The SDK's registry, validator, and model factory are all written against a
Swagger 2.0-shaped document: top-level `definitions`, `parameters` entries that
carry `in: body`, and `responses[code].schema`. The published Golden contract is
OpenAPI 3.0, which moves schemas under `components/schemas`, replaces body
parameters with `requestBody`, and nests response schemas under `content`.

Rather than fork every downstream consumer, this module performs one narrow,
lossless-for-our-purposes translation at load time. Conversion is deliberately
mechanical:

- `components/schemas` becomes `definitions`, and `$ref` pointers are rewritten
  from `#/components/schemas/X` to `#/definitions/X`.
- `requestBody` becomes a single `in: body` parameter named `body`.
- `responses[code].content["application/json"].schema` becomes
  `responses[code].schema`; responses without a JSON body keep no schema so they
  stay unvalidated rather than validating against the wrong media type.
- OpenAPI's `nullable: true` becomes Swagger's `x-nullable: true` so the existing
  normalization pass handles nullability in exactly one place.

Path templates are preserved verbatim (including the `/api/v1.0` prefix) because
the client routes tenant-root paths from the tenant origin.
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any, cast

_JSON_MEDIA_TYPE = "application/json"
_OPENAPI_SCHEMA_REF_PREFIX = "#/components/schemas/"
_SWAGGER_DEFINITION_REF_PREFIX = "#/definitions/"

HTTP_METHODS = ("get", "post", "put", "delete", "patch", "head", "options")


def convert_openapi_document(document: dict[str, Any]) -> dict[str, Any]:
    """Return a Swagger 2.0-shaped copy of an OpenAPI 3.0 contract document."""
    source = deepcopy(document)

    components = source.get("components")
    components = components if isinstance(components, dict) else {}
    raw_schemas = components.get("schemas")
    definitions = cast(
        dict[str, Any], _rewrite_refs(raw_schemas if isinstance(raw_schemas, dict) else {})
    )

    raw_paths = source.get("paths")
    source_paths = raw_paths if isinstance(raw_paths, dict) else {}

    paths: dict[str, Any] = {}
    for raw_path, path_item in source_paths.items():
        if not isinstance(path_item, dict):
            continue
        paths[str(raw_path)] = _convert_path_item(path_item)

    info = source.get("info")
    info = info if isinstance(info, dict) else {}

    converted: dict[str, Any] = {
        "swagger": "2.0",
        "info": {
            "title": str(info.get("title", "Incident IQ API")),
            "version": str(info.get("version", "1.0.0")),
        },
        "paths": paths,
        "definitions": definitions,
    }

    description = info.get("description")
    if isinstance(description, str) and description:
        converted["info"]["description"] = description

    return converted


def _convert_path_item(path_item: dict[str, Any]) -> dict[str, Any]:
    converted: dict[str, Any] = {}

    shared_parameters = path_item.get("parameters")
    if isinstance(shared_parameters, list):
        converted["parameters"] = [
            _convert_parameter(parameter)
            for parameter in shared_parameters
            if isinstance(parameter, dict)
        ]

    for method_name, operation in path_item.items():
        if method_name.lower() not in HTTP_METHODS or not isinstance(operation, dict):
            continue
        converted[method_name.lower()] = _convert_operation(operation)

    return converted


def _convert_operation(operation: dict[str, Any]) -> dict[str, Any]:
    converted = {
        key: value
        for key, value in operation.items()
        if key not in {"parameters", "requestBody", "responses"}
    }

    parameters: list[dict[str, Any]] = []
    raw_parameters = operation.get("parameters")
    if isinstance(raw_parameters, list):
        parameters.extend(
            _convert_parameter(parameter)
            for parameter in raw_parameters
            if isinstance(parameter, dict)
        )

    body_parameter = _convert_request_body(operation.get("requestBody"))
    if body_parameter is not None:
        parameters.append(body_parameter)

    if parameters:
        converted["parameters"] = parameters

    converted["responses"] = _convert_responses(operation.get("responses"))
    return converted


def _convert_parameter(parameter: dict[str, Any]) -> dict[str, Any]:
    converted = {key: value for key, value in parameter.items() if key != "schema"}

    schema = parameter.get("schema")
    if isinstance(schema, dict):
        rewritten = cast(dict[str, Any], _rewrite_refs(schema))
        converted["schema"] = rewritten
        # Downstream runtime code reads `type` to coerce primitive path/query
        # values, which OpenAPI 3 nests inside the parameter schema.
        schema_type = rewritten.get("type")
        if isinstance(schema_type, str):
            converted.setdefault("type", schema_type)

    return converted


def _convert_request_body(request_body: Any) -> dict[str, Any] | None:
    if not isinstance(request_body, dict):
        return None

    content = request_body.get("content")
    if not isinstance(content, dict) or not content:
        return None

    media_type = _JSON_MEDIA_TYPE if _JSON_MEDIA_TYPE in content else next(iter(content))
    media_object = content.get(media_type)
    if not isinstance(media_object, dict):
        return None

    schema = media_object.get("schema")
    if not isinstance(schema, dict):
        return None

    parameter: dict[str, Any] = {
        "name": "body",
        "in": "body",
        "required": bool(request_body.get("required", False)),
        "schema": _rewrite_refs(schema),
    }

    description = request_body.get("description")
    if isinstance(description, str) and description:
        parameter["description"] = description
    if media_type != _JSON_MEDIA_TYPE:
        parameter["x-media-type"] = media_type

    return parameter


def _convert_responses(responses: Any) -> dict[str, Any]:
    if not isinstance(responses, dict):
        return {}

    converted: dict[str, Any] = {}
    for status_code, response in responses.items():
        if not isinstance(response, dict):
            continue

        entry = {key: value for key, value in response.items() if key != "content"}
        content = response.get("content")
        if isinstance(content, dict):
            media_object = content.get(_JSON_MEDIA_TYPE)
            if isinstance(media_object, dict) and isinstance(media_object.get("schema"), dict):
                entry["schema"] = _rewrite_refs(media_object["schema"])

        converted[str(status_code)] = entry

    return converted


def _rewrite_refs(node: Any) -> Any:
    """Rewrite component refs and OpenAPI nullability into Swagger equivalents."""
    if isinstance(node, dict):
        rewritten: dict[str, Any] = {}
        for key, value in node.items():
            if key == "$ref" and isinstance(value, str):
                rewritten[key] = _rewrite_ref_pointer(value)
            elif key == "nullable":
                # Normalization understands Swagger's `x-nullable`; funnel both
                # dialects through that single code path.
                if value is True:
                    rewritten["x-nullable"] = True
            else:
                rewritten[key] = _rewrite_refs(value)
        return rewritten
    if isinstance(node, list):
        return [_rewrite_refs(item) for item in node]
    return node


def _rewrite_ref_pointer(pointer: str) -> str:
    if pointer.startswith(_OPENAPI_SCHEMA_REF_PREFIX):
        name = pointer[len(_OPENAPI_SCHEMA_REF_PREFIX) :]
        return f"{_SWAGGER_DEFINITION_REF_PREFIX}{name}"
    return pointer
