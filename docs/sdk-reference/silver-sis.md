# `silver.sis` Namespace

Sync client access: `client.silver.sis`

Async client access: `client.silver.sis` with `await` on method calls.

These methods are Silver because the published contract does not document them directly, or because the SDK intentionally wraps a narrower Silver workflow around existing Golden operations. They remain separate so undocumented or convenience behavior never overrides the documented SDK surface.

## Methods

### `get_classes_for__user`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.sis.get_classes_for__user(user_id=..., s=..., timeout=None)`
- Async: `await client.silver.sis.get_classes_for__user(user_id=..., s=..., timeout=None)`
- Raw payload: `client.silver.sis.get_classes_for__user.raw(user_id=..., s=..., timeout=None)`
- HTTP route: `GET /api/v1.0/sis/classes/for/user/{user_id}`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.sis`.

This route is kept on the Silver surface because the published Incident IQ OpenAPI contract does not document it. The Golden contract remains the preferred source whenever it documents a route, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `user_id` | `user_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because the published OpenAPI contract does not document it. |
| `s` | `$s` | `query` | `yes` | `int` | Query parameter inferred from HAR observations for this undocumented Silver route. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---
