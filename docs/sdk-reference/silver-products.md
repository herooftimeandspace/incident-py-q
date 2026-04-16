# `silver.products` Namespace

Sync client access: `client.silver.products`

Async client access: `client.silver.products` with `await` on method calls.

These methods are Silver because Stoplight does not publish Golden contracts for them. They remain separate so undocumented behavior never overrides the documented SDK surface.

## Methods

### `get_available_features`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.products.get_available_features(timeout=None)`
- Async: `await client.silver.products.get_available_features(timeout=None)`
- Raw payload: `client.silver.products.get_available_features.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/products/available-features`
- Observed in: `apple-asset-actions.har`

HAR-derived undocumented GET route for `client.silver.products`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---
