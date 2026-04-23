# `silver.tickets` Namespace

Sync client access: `client.silver.tickets`

Async client access: `client.silver.tickets` with `await` on method calls.

These methods are Silver because Stoplight does not publish direct Golden contracts for them, or because the SDK intentionally wraps a narrower Silver workflow around existing Golden operations. They remain separate so undocumented or convenience behavior never overrides the documented SDK surface.

## Methods

### `get_ticket_activities`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.tickets.get_ticket_activities(ticket_id=..., timeout=None)`
- Async: `await client.silver.tickets.get_ticket_activities(ticket_id=..., timeout=None)`
- Raw payload: `client.silver.tickets.get_ticket_activities.raw(ticket_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/tickets/{ticket_id}/activities`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.tickets`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticket_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_ticket_kb_articles`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.tickets.get_ticket_kb_articles(ticket_id=..., timeout=None)`
- Async: `await client.silver.tickets.get_ticket_kb_articles(ticket_id=..., timeout=None)`
- Raw payload: `client.silver.tickets.get_ticket_kb_articles.raw(ticket_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/tickets/{ticket_id}/kb-articles`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.tickets`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticket_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_ticket_next_steps`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.tickets.get_ticket_next_steps(ticket_id=..., timeout=None)`
- Async: `await client.silver.tickets.get_ticket_next_steps(ticket_id=..., timeout=None)`
- Raw payload: `client.silver.tickets.get_ticket_next_steps.raw(ticket_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/tickets/{ticket_id}/next-steps`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.tickets`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticket_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_ticket_status`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.tickets.get_ticket_status(ticket_id=..., timeout=None)`
- Async: `await client.silver.tickets.get_ticket_status(ticket_id=..., timeout=None)`
- Raw payload: `client.silver.tickets.get_ticket_status.raw(ticket_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/tickets/{ticket_id}/status`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.tickets`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticket_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_wizards_site`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.tickets.get_wizards_site(site_id=..., s=..., timeout=None)`
- Async: `await client.silver.tickets.get_wizards_site(site_id=..., s=..., timeout=None)`
- Raw payload: `client.silver.tickets.get_wizards_site.raw(site_id=..., s=..., timeout=None)`
- HTTP route: `GET /api/v1.0/tickets/wizards/site/{site_id}`
- Observed in: `apple-asset-actions.har`, `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.tickets`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `site_id` | `site_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |
| `s` | `$s` | `query` | `yes` | `int` | Query parameter inferred from HAR observations for this undocumented Silver route. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_endpoint`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.tickets.post_endpoint(o=..., s=..., json_body=..., timeout=None)`
- Async: `await client.silver.tickets.post_endpoint(o=..., s=..., json_body=..., timeout=None)`
- Raw payload: `client.silver.tickets.post_endpoint.raw(o=..., s=..., json_body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented POST route for `client.silver.tickets`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `o` | `$o` | `query` | `yes` | `str` | Query parameter inferred from HAR observations for this undocumented Silver route. |
| `s` | `$s` | `query` | `yes` | `int` | Query parameter inferred from HAR observations for this undocumented Silver route. |
| `json_body` | `json_body` | `body` | `yes` | `Mapping[str, Any]` | Request body observed in HAR traffic. The SDK uses a single `json_body` payload because the Silver route carries a complex undocumented schema. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_ticket_timeline`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.tickets.post_ticket_timeline(ticket_id=..., timeout=None)`
- Async: `await client.silver.tickets.post_ticket_timeline(ticket_id=..., timeout=None)`
- Raw payload: `client.silver.tickets.post_ticket_timeline.raw(ticket_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticket_id}/timeline`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented POST route for `client.silver.tickets`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticket_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---
