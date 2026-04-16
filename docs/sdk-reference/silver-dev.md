# `silver.dev` Namespace

Sync client access: `client.silver.dev`

Async client access: `client.silver.dev` with `await` on method calls.

These methods are Silver because Stoplight does not publish Golden contracts for them. They remain separate so undocumented behavior never overrides the documented SDK surface.

## Methods

### `post_test_url`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.dev.post_test_url(method=..., url=..., timeout=None)`
- Async: `await client.silver.dev.post_test_url(method=..., url=..., timeout=None)`
- Raw payload: `client.silver.dev.post_test_url.raw(method=..., url=..., timeout=None)`
- HTTP route: `POST /api/v1.0/dev/test-url`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented POST route for `client.silver.dev`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `method` | `Method` | `body` | `yes` | `str` | Body field inferred from HAR observations for this undocumented Silver route. |
| `url` | `Url` | `body` | `yes` | `str` | Body field inferred from HAR observations for this undocumented Silver route. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---
