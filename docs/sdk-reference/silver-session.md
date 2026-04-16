# `silver.session` Namespace

Sync client access: `client.silver.session`

Async client access: `client.silver.session` with `await` on method calls.

These methods are Silver because Stoplight does not publish Golden contracts for them. They remain separate so undocumented behavior never overrides the documented SDK surface.

## Methods

### `post_state`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.session.post_state(session_state_id=..., value=..., timeout=None)`
- Async: `await client.silver.session.post_state(session_state_id=..., value=..., timeout=None)`
- Raw payload: `client.silver.session.post_state.raw(session_state_id=..., value=..., timeout=None)`
- HTTP route: `POST /api/v1.0/session/state`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented POST route for `client.silver.session`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `session_state_id` | `SessionStateId` | `body` | `yes` | `str` | Body field inferred from HAR observations for this undocumented Silver route. |
| `value` | `Value` | `body` | `yes` | `str` | Body field inferred from HAR observations for this undocumented Silver route. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---
