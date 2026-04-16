# `silver.categories` Namespace

Sync client access: `client.silver.categories`

Async client access: `client.silver.categories` with `await` on method calls.

These methods are Silver because Stoplight does not publish Golden contracts for them. They remain separate so undocumented behavior never overrides the documented SDK surface.

## Methods

### `get_of_filters`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.categories.get_of_filters(timeout=None)`
- Async: `await client.silver.categories.get_of_filters(timeout=None)`
- Raw payload: `client.silver.categories.get_of_filters.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/categories/of/filters`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.categories`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_of_models`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.categories.get_of_models(s=..., timeout=None)`
- Async: `await client.silver.categories.get_of_models(s=..., timeout=None)`
- Raw payload: `client.silver.categories.get_of_models.raw(s=..., timeout=None)`
- HTTP route: `GET /api/v1.0/categories/of/models`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.categories`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `s` | `$s` | `query` | `yes` | `int` | Query parameter inferred from HAR observations for this undocumented Silver route. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---
