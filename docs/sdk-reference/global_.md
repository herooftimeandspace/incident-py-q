# `global_` Golden Namespace

Sync client access: `client.global_`

Async client access: `client.global_` with `await` on method calls.

These methods are Golden because they come from the bundled Incident IQ OpenAPI contract.

## Methods

### `get_ticket_stats_global`

Provenance: Golden OpenAPI contract

Operation ID: `getTicketStatsGlobal`

- Sync: `client.global_.get_ticket_stats_global(body=None, timeout=None)`
- Async: `await client.global_.get_ticket_stats_global(body=None, timeout=None)`
- Raw payload: `client.global_.get_ticket_stats_global.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/global/tickets/stats`
- Source controller: `IncidentIQ API`

Get global ticket statistics

Retrieves aggregated ticket statistics across all sites the caller has access to. Useful for district-level dashboards and executive reporting.

**Use Cases**
- District dashboard widgets showing total open tickets
- Cross-site SLA compliance reporting
- Workload distribution analysis across locations

**Request Body**: Provide an array of `FilterMatch` entries to scope the statistics. Omit the body to compute stats across all accessible tickets.

**Note**: Statistics reflect only tickets from sites the caller can access.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `list[Any]` | `-` | Optional filter criteria for statistics calculation |

#### Returns

- Typed call return: `TicketsStatListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketsStatListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `search_tickets_global`

Provenance: Golden OpenAPI contract

Operation ID: `searchTicketsGlobal`

- Sync: `client.global_.search_tickets_global(p=None, s=None, body=None, timeout=None)`
- Async: `await client.global_.search_tickets_global(p=None, s=None, body=None, timeout=None)`
- Raw payload: `client.global_.search_tickets_global.raw(p=None, s=None, body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/global/tickets`
- Source controller: `IncidentIQ API`

Search tickets globally

Searches tickets across all sites the caller has access to. This endpoint is useful for district-level reporting and cross-site ticket visibility. Unlike the site-scoped [POST /api/v1.0/tickets](#/Tickets/searchTickets), this endpoint does not require a SiteId header and returns tickets from all accessible sites.

**Use Cases**
- District administrators viewing tickets across all schools
- Cross-site reporting and analytics
- Finding tickets regardless of site assignment

**Filter Support**
Supports the same filter facets as the site-scoped search endpoint. See [POST /api/v1.0/tickets](#/Tickets/searchTickets) for complete filter documentation.

**Note**: Results are limited by the caller's permissions. Only tickets from sites the caller can access will be returned.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index to retrieve |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of records per page |
| `body` | `body` | `body` | `no` | `list[Any]` | `-` | Optional array of `FilterMatch` entries used to scope the global ticket search. |

#### Returns

- Typed call return: `TicketSearchResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketSearchResponse`
- Pagination helper: `client.global_.search_tickets_global.iter_pages(start_page=1, page_size=100, max_pages=None, p=None, s=None, body=None, timeout=None)`

---
