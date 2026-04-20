"""Silver-specific response-schema overrides for known live-data contract drift."""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from typing import Any

from jsonschema import RefResolver, validators
from jsonschema import ValidationError as JSONSchemaValidationError

from incident_py_q.exceptions import SchemaValidationError
from incident_py_q.schema.registry import OperationSpec, SchemaRegistry


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


# This override is intentionally verbose because the distinction is easy to lose later if someone
# only sees "remove some required fields" in a diff. The live `/assets/serial/{serial}` route is
# exposed under `client.silver.*` because Silver is our HAR-derived, inferred view of the API as it
# behaves in production traffic. Golden is different: Golden is the published Stoplight contract
# that we treat as the authoritative source of truth for documented behavior. For this route, the
# live tenant payload omits a handful of fields that the Golden contract still marks as required.
# We do not want to "fix" Golden to match that drift, because doing so would erase evidence that
# the published contract and the live service disagree. Instead, we add a narrow Silver-only schema
# clone that documents a business decision: Silver may accept the live response shape as a tactical
# compatibility workaround for scripts that need the route to function today, while Golden remains
# strict so upstream contract drift stays visible. If IncidentIQ aligns the live payload and the
# published schema later, this override should be revisited and ideally removed rather than copied
# to more routes.
def _build_overrides(registry: SchemaRegistry) -> dict[tuple[str, str], _SilverOverride]:
    serial_lookup_operation = _find_operation(
        registry,
        method="GET",
        path_template="/assets/serial/{Serial}",
    )
    if serial_lookup_operation is None:
        return {}
    serial_lookup_override = _build_asset_get_assets_by_serial_override(
        registry=registry,
        operation=serial_lookup_operation,
    )
    return {
        ("GET", "/assets/serial/{serial}"): serial_lookup_override,
    }


def _build_asset_get_assets_by_serial_override(
    *,
    registry: SchemaRegistry,
    operation: OperationSpec,
) -> _SilverOverride:
    document = deepcopy(registry.merged_document)
    definitions = document.setdefault("definitions", {})

    custom_field_name = "SilverAssetGetAssetsBySerialAssetCustomFieldValue"
    site_name = "SilverAssetGetAssetsBySerialSite"
    asset_name = "SilverAssetGetAssetsBySerialAsset"
    response_name = "SilverAssetGetAssetsBySerialResponse"

    relaxed_custom_field = deepcopy(definitions["AssetCustomFieldValue"])
    _remove_required_fields(relaxed_custom_field, {"AssetId"})

    relaxed_site = deepcopy(definitions["Site"])
    _remove_required_fields(
        relaxed_site,
        {
            "DefaultWorkflowId",
            "DefaultWorkflowInitialStepId",
            "EnableAnalytics",
            "EnableUsersnap",
        },
    )

    relaxed_asset = deepcopy(definitions["Asset"])
    _remove_required_fields(
        relaxed_asset,
        {
            "IsTraining",
            "IsReadOnly",
            "IsExternallyManaged",
        },
    )
    asset_properties = relaxed_asset.setdefault("properties", {})
    custom_field_values = asset_properties.setdefault("CustomFieldValues", {})
    custom_field_values["items"] = {"$ref": f"#/definitions/{custom_field_name}"}
    asset_properties["Site"] = {"$ref": f"#/definitions/{site_name}"}

    relaxed_response = deepcopy(definitions["ListGetResponseOfAsset"])
    response_properties = relaxed_response.setdefault("properties", {})
    items = response_properties.setdefault("Items", {})
    items["items"] = {"$ref": f"#/definitions/{asset_name}"}

    definitions[custom_field_name] = relaxed_custom_field
    definitions[site_name] = relaxed_site
    definitions[asset_name] = relaxed_asset
    definitions[response_name] = relaxed_response

    response_schemas = dict(operation.response_schemas)
    response_schemas["200"] = {"$ref": f"#/definitions/{response_name}"}

    return _SilverOverride(
        operation_id=operation.operation_id,
        response_schemas=response_schemas,
        validator_cls=validators.validator_for(document),
        resolver=RefResolver.from_schema(document),
    )


def _find_operation(
    registry: SchemaRegistry,
    *,
    method: str,
    path_template: str,
) -> OperationSpec | None:
    for operation in registry.operations:
        if operation.method == method and operation.path_template == path_template:
            return operation
    return None


def _remove_required_fields(schema: dict[str, Any], fields: set[str]) -> None:
    required = schema.get("required")
    if not isinstance(required, list):
        return
    schema["required"] = [field for field in required if field not in fields]


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
