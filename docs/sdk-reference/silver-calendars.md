# `silver.calendars` Namespace

Sync client access: `client.silver.calendars`

Async client access: `client.silver.calendars` with `await` on method calls.

These methods are Silver because Stoplight does not publish direct Golden contracts for them, or because the SDK intentionally wraps a narrower Silver workflow around existing Golden operations. They remain separate so undocumented or convenience behavior never overrides the documented SDK surface.

## Methods

### `get_events_key`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.calendars.get_events_key(timeout=None)`
- Async: `await client.silver.calendars.get_events_key(timeout=None)`
- Raw payload: `client.silver.calendars.get_events_key.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/calendars/events/key`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.calendars`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_events`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.calendars.post_events(json_body=..., timeout=None)`
- Async: `await client.silver.calendars.post_events(json_body=..., timeout=None)`
- Raw payload: `client.silver.calendars.post_events.raw(json_body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/calendars/events`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented POST route for `client.silver.calendars`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `json_body` | `json_body` | `body` | `yes` | `Mapping[str, Any]` | Request body observed in HAR traffic. The SDK uses a single `json_body` payload because the Silver route carries a complex undocumented schema. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---
