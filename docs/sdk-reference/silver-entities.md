# `silver.entities` Namespace

Sync client access: `client.silver.entities`

Async client access: `client.silver.entities` with `await` on method calls.

These methods are Silver because Stoplight does not publish direct Golden contracts for them, or because the SDK intentionally wraps a narrower Silver workflow around existing Golden operations. They remain separate so undocumented or convenience behavior never overrides the documented SDK surface.

## Methods

### `get_types_fields_withoptions`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.entities.get_types_fields_withoptions(type_id=..., timeout=None)`
- Async: `await client.silver.entities.get_types_fields_withoptions(type_id=..., timeout=None)`
- Raw payload: `client.silver.entities.get_types_fields_withoptions.raw(type_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/entities/types/{type_id}/fields/withoptions`
- Observed in: `Chromebook-asset-actions.har`, `apple-asset-actions.har`, `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.entities`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `type_id` | `type_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---
