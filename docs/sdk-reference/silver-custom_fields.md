# `silver.custom_fields` Namespace

Sync client access: `client.silver.custom_fields`

Async client access: `client.silver.custom_fields` with `await` on method calls.

These methods are Silver because the published contract does not document them directly, or because the SDK intentionally wraps a narrower Silver workflow around existing Golden operations. They remain separate so undocumented or convenience behavior never overrides the documented SDK surface.

## Methods

### `delete_custom_fields`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.custom_fields.delete_custom_fields(json_body=..., timeout=None)`
- Async: `await client.silver.custom_fields.delete_custom_fields(json_body=..., timeout=None)`
- Raw payload: `client.silver.custom_fields.delete_custom_fields.raw(json_body=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/custom-fields`
- Observed in: `migrated_from_golden_stoplight`

Migrated Silver route for DELETE /custom-fields.

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.custom_fields.delete_custom_fields` (operationId `CustomField_DeleteCustomFields`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `json_body` | `CustomFieldIds` | `body` | `yes` | `dict[str, Any] | list[Any]` | Body parameter migrated from the previous Golden SDK. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_custom_fields`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.custom_fields.get_custom_fields(product_filter_type=None, timeout=None)`
- Async: `await client.silver.custom_fields.get_custom_fields(product_filter_type=None, timeout=None)`
- Raw payload: `client.silver.custom_fields.get_custom_fields.raw(product_filter_type=None, timeout=None)`
- HTTP route: `GET /api/v1.0/custom-fields`
- Observed in: `migrated_from_golden_stoplight`

Migrated Silver route for GET /custom-fields.

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.custom_fields.get_custom_fields` (operationId `CustomField_GetCustomFields`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `product_filter_type` | `ProductFilterType` | `query` | `no` | `str` | Query parameter migrated from the previous Golden SDK. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---
