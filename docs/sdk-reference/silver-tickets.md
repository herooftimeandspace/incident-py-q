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

### `list_current_user_assigned_tickets`

Provenance: Silver manual helper

- Sync: `client.silver.tickets.list_current_user_assigned_tickets(page_size=100, sort_by="TicketModifiedDate", sort_direction="Descending", timeout=None)`
- Async: `await client.silver.tickets.list_current_user_assigned_tickets(page_size=100, sort_by="TicketModifiedDate", sort_direction="Descending", timeout=None)`
- Raw payload: No public `.raw(...)`; the helper returns the raw JSON-compatible payload directly.
- Backing routes: `POST /services/tickets/-/-/AssignedToMe_Unassigned`, `POST /services/tickets/-/-/AssignedToMe_Unassigned with configured Client header`, `POST /services/tickets/-/-/AssignedToMe_Unassigned with legacy o/d sort query`, `POST /services/tickets with AssignedToMe_Unassigned schema body`

List the current user's UI-style assigned/open ticket queue through the `AssignedToMe_Unassigned` services route.

This helper exists because tenant analytics summaries and saved-view routes can return zero rows for current-user ticket queues even when the Incident IQ web UI shows assigned work. The bundled Postman corpus includes the UI-observed `/services/tickets/-/-/AssignedToMe_Unassigned` route for open assigned tickets, so the SDK exposes a narrow read-only helper around that route instead of asking callers to construct a services URL by hand. The route uses POST for query semantics and some tenants only expose it to the UI-style `Client: WebBrowser` header, so the helper sends that header with page size, sort field, and sort direction parameters and does not send a mutation body. If the UI-shaped request returns 404, the helper retries once with the caller's configured client header for older tenants that accepted the pre-0.2.5 SDK request shape, then tries the Postman-observed legacy sort-query spelling that uses `$s`, `o`, and `d`. Some tenants, including WUSD as validated for issue #73, do not expose the direct queue route but do expose the same queue through `POST /services/tickets` with `{"Schema": "AssignedToMe_Unassigned"}`, so that schema body is the final read-only fallback.

#### Examples

- Default UI queue: `client.silver.tickets.list_current_user_assigned_tickets(timeout=None)`
- Priority order: `client.silver.tickets.list_current_user_assigned_tickets(page_size=100, sort_by="TicketPriority", sort_direction="Descending", timeout=None)`
- Async default queue: `await client.silver.tickets.list_current_user_assigned_tickets(timeout=None)`

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `page_size` | `$s` | `query` | `no` | `int` | Maximum number of ticket rows to return from the queue. |
| `sort_by` | `$o` | `query` | `no` | `str` | Incident IQ ticket field used for ordering returned rows. |
| `sort_direction` | `$d` | `query` | `no` | `str` | Sort direction, either `Ascending` or `Descending`. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this manual helper has no typed response model.

---
