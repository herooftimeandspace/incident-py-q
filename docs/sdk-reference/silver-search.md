# `silver.search` Namespace

Sync client access: `client.silver.search`

Async client access: `client.silver.search` with `await` on method calls.

These methods are Silver because Stoplight does not publish direct Golden contracts for them, or because the SDK intentionally wraps a narrower Silver workflow around existing Golden operations. They remain separate so undocumented or convenience behavior never overrides the documented SDK surface.

## Methods

### `post_scan`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.search.post_scan(limit=..., query=..., timeout=None)`
- Async: `await client.silver.search.post_scan(limit=..., query=..., timeout=None)`
- Raw payload: `client.silver.search.post_scan.raw(limit=..., query=..., timeout=None)`
- HTTP route: `POST /api/v1.0/search/scan`
- Observed in: `Chromebook-asset-actions.har`, `apple-asset-actions.har`

HAR-derived undocumented POST route for `client.silver.search`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `limit` | `Limit` | `body` | `yes` | `int` | Body field inferred from HAR observations for this undocumented Silver route. |
| `query` | `Query` | `body` | `yes` | `str` | Body field inferred from HAR observations for this undocumented Silver route. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---
