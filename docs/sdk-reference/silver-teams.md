# `silver.teams` Namespace

Sync client access: `client.silver.teams`

Async client access: `client.silver.teams` with `await` on method calls.

These methods are Silver because Stoplight does not publish direct Golden contracts for them, or because the SDK intentionally wraps a narrower Silver workflow around existing Golden operations. They remain separate so undocumented or convenience behavior never overrides the documented SDK surface.

## Methods

### `get_endpoint`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.teams.get_endpoint(filter=..., s=..., timeout=None)`
- Async: `await client.silver.teams.get_endpoint(filter=..., s=..., timeout=None)`
- Raw payload: `client.silver.teams.get_endpoint.raw(filter=..., s=..., timeout=None)`
- HTTP route: `GET /api/v1.0/teams`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.teams`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `filter` | `$filter` | `query` | `yes` | `str` | Query parameter inferred from HAR observations for this undocumented Silver route. |
| `s` | `$s` | `query` | `yes` | `int` | Query parameter inferred from HAR observations for this undocumented Silver route. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_for_`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.teams.get_for_(for__id=..., timeout=None)`
- Async: `await client.silver.teams.get_for_(for__id=..., timeout=None)`
- Raw payload: `client.silver.teams.get_for_.raw(for__id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/teams/for/{for__id}`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.teams`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `for__id` | `for__id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---
