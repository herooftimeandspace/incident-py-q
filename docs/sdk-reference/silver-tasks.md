# `silver.tasks` Namespace

Sync client access: `client.silver.tasks`

Async client access: `client.silver.tasks` with `await` on method calls.

These methods are Silver because Stoplight does not publish Golden contracts for them. They remain separate so undocumented behavior never overrides the documented SDK surface.

## Methods

### `get_endpoint`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.tasks.get_endpoint(s=..., timeout=None)`
- Async: `await client.silver.tasks.get_endpoint(s=..., timeout=None)`
- Raw payload: `client.silver.tasks.get_endpoint.raw(s=..., timeout=None)`
- HTTP route: `GET /api/v1.0/tasks`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.tasks`.

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
