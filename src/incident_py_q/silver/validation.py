"""Silver-specific response-schema overrides for known live-data contract drift."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from jsonschema import RefResolver, validators
from jsonschema import ValidationError as JSONSchemaValidationError

from incident_py_q.exceptions import SchemaValidationError
from incident_py_q.schema.loader import load_legacy_contract_document
from incident_py_q.schema.normalize import normalize_swagger_document
from incident_py_q.schema.registry import SchemaRegistry

_HTTP_METHODS = ("get", "post", "put", "delete", "patch", "head", "options")


@dataclass(frozen=True, slots=True)
class _SilverOverride:
    operation_id: str
    response_schemas: dict[str, dict[str, Any]]
    validator_cls: Any
    resolver: RefResolver


class SilverResponseSchemaValidator:
    """Validate Silver responses against explicit Silver-only overrides when needed."""

    def __init__(self, registry: SchemaRegistry) -> None:
        self._registry = registry
        self._overrides = _build_overrides(registry)

    def validate_if_override(
        self,
        *,
        method: str,
        route: str,
        status_code: int,
        payload: Any,
    ) -> bool:
        """Validate against a Silver override if one exists for the route."""
        override = self._overrides.get((method.upper(), route))
        if override is None:
            return False

        response_schema = _pick_response_schema(
            response_schemas=override.response_schemas,
            status_code=status_code,
        )
        if response_schema is None:
            return True

        validator = override.validator_cls(
            response_schema,
            resolver=override.resolver,
        )

        try:
            validator.validate(payload)
        except JSONSchemaValidationError as exc:
            raise SchemaValidationError(
                f"Silver response schema validation failed for {method.upper()} {route} "
                f"({override.operation_id}): {exc.message}"
            ) from exc
        return True


# Silver response overrides exist for one situation: a route Silver exposes because the
# published Golden contract does not document it, but for which the SDK still holds a
# schema worth enforcing.
#
# Every override registered today comes from the Golden OpenAPI migration. The published
# contract is a locked allowlist profile that stopped documenting a set of routes the SDK
# previously served from Golden. Those routes were migrated onto Silver rather than being
# dropped, and the pruned legacy contract keeps their schemas so they did not silently
# lose strict response validation on the way across.
#
# Routes discovered from HAR traffic have no schema and are not represented here; they
# validate structurally at the runtime layer only. Drift on a route the published contract
# *does* document belongs in `incident_py_q.schema.normalize`, not here.
def _build_overrides(registry: SchemaRegistry) -> dict[tuple[str, str], _SilverOverride]:
    document = normalize_swagger_document(load_legacy_contract_document())
    validator_cls = validators.validator_for(document)
    resolver = RefResolver.from_schema(document)

    overrides: dict[tuple[str, str], _SilverOverride] = {}
    paths = document.get("paths")
    if not isinstance(paths, dict):
        return overrides

    for route, path_item in paths.items():
        if not isinstance(path_item, dict):
            continue
        for method_name, operation in path_item.items():
            if method_name.lower() not in _HTTP_METHODS or not isinstance(operation, dict):
                continue
            response_schemas: dict[str, dict[str, Any]] = {}
            for status_code, response in (operation.get("responses") or {}).items():
                if isinstance(response, dict) and isinstance(response.get("schema"), dict):
                    response_schemas[str(status_code)] = response["schema"]

            operation_id = operation.get("operationId")
            overrides[(method_name.upper(), str(route))] = _SilverOverride(
                operation_id=str(operation_id) if operation_id else f"{method_name.upper()} {route}",
                response_schemas=response_schemas,
                validator_cls=validator_cls,
                resolver=resolver,
            )

    return overrides


def _pick_response_schema(
    *,
    response_schemas: dict[str, dict[str, Any]],
    status_code: int,
) -> dict[str, Any] | None:
    exact = response_schemas.get(str(status_code))
    if exact is not None:
        return exact

    class_prefix = f"{str(status_code)[0]}xx"
    for candidate in response_schemas:
        if candidate.lower() == class_prefix:
            return response_schemas[candidate]

    return response_schemas.get("default")
