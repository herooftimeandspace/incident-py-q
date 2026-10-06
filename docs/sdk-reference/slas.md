# `slas` Golden Namespace

Sync client access: `client.slas`

Async client access: `client.slas` with `await` on method calls.

These methods are Golden because they come from the bundled Incident IQ OpenAPI contract.

## Aliases

| Alias | Canonical Method | Route |
| --- | --- | --- |
| `create` | `create_sla` | `POST /api/v1.0/slas/new` |

## Methods

### `activate_sla`

Provenance: Golden OpenAPI contract

Operation ID: `activateSla`

- Sync: `client.slas.activate_sla(client=None, product_id=None, site_id=None, sla_id=..., timeout=None)`
- Async: `await client.slas.activate_sla(client=None, product_id=None, site_id=None, sla_id=..., timeout=None)`
- Raw payload: `client.slas.activate_sla.raw(client=None, product_id=None, site_id=None, sla_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/slas/{SlaId}/activate`
- Source controller: `IncidentIQ API`

Activate SLA

Activates a service level agreement, enabling it to be applied to tickets. An active SLA defines response and resolution time targets that help ensure consistent service quality.

**Prerequisites**
1. **SlaId** - Use [GET /api/v1.0/slas](#/SLAs/listSlas) to list available SLAs. Extract `Items[].SlaId` from the response.

**Workflow Example**
1. List SLAs: [GET /api/v1.0/slas](#/SLAs/listSlas) → find the SLA you want to activate
2. Activate: [POST /api/v1.0/slas/{SlaId}/activate](#/SLAs/activateSla)

**Notes**: Only inactive SLAs can be activated. Activating an SLA makes it available for assignment to tickets. Use [POST /api/v1.0/slas/{SlaId}/deactivate](#/SLAs/deactivateSla) to disable an SLA.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `client` | `Client` | `header` | `no` | `str` | `-` | - |
| `product_id` | `ProductId` | `header` | `no` | `int` | `-` | - |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | - |
| `sla_id` | `SlaId` | `path` | `yes` | `str` | `-` | The unique identifier of the SLA |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `add_sla_days_to_date`

Provenance: Golden OpenAPI contract

Operation ID: `addSlaDaysToDate`

- Sync: `client.slas.add_sla_days_to_date(client=None, product_id=None, site_id=None, date=..., days=..., timeout=None)`
- Async: `await client.slas.add_sla_days_to_date(client=None, product_id=None, site_id=None, date=..., days=..., timeout=None)`
- Raw payload: `client.slas.add_sla_days_to_date.raw(client=None, product_id=None, site_id=None, date=..., days=..., timeout=None)`
- HTTP route: `GET /api/v1.0/slas/date/{date}/add-days/{days}`
- Source controller: `IncidentIQ API`

Add SLA days to date

Calculates a future date by adding a specified number of SLA business days to a starting date. This calculation respects the system's SLA calendar configuration, excluding weekends, holidays, and other non-working days.

**Parameters**
- **date** - Starting date in ISO 8601 format (e.g., `2025-12-19T10:00:00Z`)
- **days** - Number of business days to add (integer)

**Workflow Example**
1. Call this endpoint: [GET /api/v1.0/slas/date/{date}/add-days/{days}](#/SLAs/addSlaDaysToDate)
2. The response `Item` contains the calculated future date.
3. Use this for SLA deadline projections and ticket due date calculations.

**Use Cases**: Projecting SLA deadlines, calculating expected resolution dates, planning capacity.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `client` | `Client` | `header` | `no` | `str` | `-` | - |
| `product_id` | `ProductId` | `header` | `no` | `int` | `-` | - |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | - |
| `date` | `date` | `path` | `yes` | `str` | `-` | The starting date |
| `days` | `days` | `path` | `yes` | `int` | `-` | The number of days to add |

#### Returns

- Typed call return: `Any`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_sla`

Provenance: Golden OpenAPI contract

Operation ID: `createSla`

- Sync: `client.slas.create_sla(client=None, product_id=None, site_id=None, timeout=None)`
- Async: `await client.slas.create_sla(client=None, product_id=None, site_id=None, timeout=None)`
- Raw payload: `client.slas.create_sla.raw(client=None, product_id=None, site_id=None, timeout=None)`
- HTTP route: `POST /api/v1.0/slas/new`
- Source controller: `IncidentIQ API`
- Aliases: `create`

Create New SLA

Creates a new service level agreement definition. SLAs specify response and resolution time targets that are applied to tickets to track service performance.

**Workflow Example**
1. Review available metrics: [GET /api/v1.0/metrics/types](#/SLAs/listMetrics) for metric type IDs.
2. Build the SLA definition in the request body (name, targets, applicable conditions).
3. Call this endpoint: [POST /api/v1.0/slas/new](#/SLAs/createSla) with the SLA configuration.
4. Activate the SLA: [POST /api/v1.0/slas/{SlaId}/activate](#/SLAs/activateSla) to enable it.

**Related Endpoints:**
- [GET /api/v1.0/slas](#/SLAs/listSlas) - List all SLAs
- [POST /api/v1.0/metrics/for/sla/{id}](#/SLAs/createMetricById) - Configure metrics for the SLA

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `client` | `Client` | `header` | `no` | `str` | `-` | - |
| `product_id` | `ProductId` | `header` | `no` | `int` | `-` | - |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | - |

#### Returns

- Typed call return: `GenericObject`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `GenericObject`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `deactivate_sla`

Provenance: Golden OpenAPI contract

Operation ID: `deactivateSla`

- Sync: `client.slas.deactivate_sla(client=None, product_id=None, site_id=None, sla_id=..., timeout=None)`
- Async: `await client.slas.deactivate_sla(client=None, product_id=None, site_id=None, sla_id=..., timeout=None)`
- Raw payload: `client.slas.deactivate_sla.raw(client=None, product_id=None, site_id=None, sla_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/slas/{SlaId}/deactivate`
- Source controller: `IncidentIQ API`

Deactivate SLA

Deactivates a service level agreement, preventing it from being applied to new tickets. Existing tickets with this SLA assigned will retain their current SLA settings until resolved.

**Prerequisites**
1. **SlaId** - Use [GET /api/v1.0/slas](#/SLAs/listSlas) to list available SLAs. Extract `Items[].SlaId` from the response.

**Workflow Example**
1. List SLAs: [GET /api/v1.0/slas](#/SLAs/listSlas) → identify the active SLA to deactivate
2. Deactivate: [POST /api/v1.0/slas/{SlaId}/deactivate](#/SLAs/deactivateSla)

**Notes**: Deactivating an SLA does not affect tickets already assigned to it. To re-enable the SLA later, use [POST /api/v1.0/slas/{SlaId}/activate](#/SLAs/activateSla).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `client` | `Client` | `header` | `no` | `str` | `-` | - |
| `product_id` | `ProductId` | `header` | `no` | `int` | `-` | - |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | - |
| `sla_id` | `SlaId` | `path` | `yes` | `str` | `-` | The unique identifier of the SLA |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_sla_by_id`

Provenance: Golden OpenAPI contract

Operation ID: `deleteSlaById`

- Sync: `client.slas.delete_sla_by_id(client=None, product_id=None, site_id=None, id=..., timeout=None)`
- Async: `await client.slas.delete_sla_by_id(client=None, product_id=None, site_id=None, id=..., timeout=None)`
- Raw payload: `client.slas.delete_sla_by_id.raw(client=None, product_id=None, site_id=None, id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/slas/{id}`
- Source controller: `IncidentIQ API`

Delete SLA

Permanently deletes a service level agreement from the system. This removes the SLA definition and all associated metric configurations.

**Prerequisites**
1. **id** - Use [GET /api/v1.0/slas](#/SLAs/listSlas) to list SLAs. Extract the target `SlaId` from the response.

**Workflow Example**
1. List SLAs: [GET /api/v1.0/slas](#/SLAs/listSlas) → identify SLA to delete.
2. Deactivate first: [POST /api/v1.0/slas/{SlaId}/deactivate](#/SLAs/deactivateSla) if currently active.
3. Call this endpoint: [DELETE /api/v1.0/slas/{id}](#/SLAs/deleteSlaById) with the SLA UUID.

**Warning**: Deletion is permanent. Existing tickets with this SLA will retain historical SLA data but no new tickets can reference it.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `client` | `Client` | `header` | `no` | `str` | `-` | - |
| `product_id` | `ProductId` | `header` | `no` | `int` | `-` | - |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | - |
| `id` | `id` | `path` | `yes` | `str` | `-` | The id parameter |

#### Returns

- Typed call return: `UnauthorizedError`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UnauthorizedError`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_slas`

Provenance: Golden OpenAPI contract

Operation ID: `listSlas`

- Sync: `client.slas.list_slas(fields=None, client=None, product_id=None, site_id=None, timeout=None)`
- Async: `await client.slas.list_slas(fields=None, client=None, product_id=None, site_id=None, timeout=None)`
- Raw payload: `client.slas.list_slas.raw(fields=None, client=None, product_id=None, site_id=None, timeout=None)`
- HTTP route: `GET /api/v1.0/slas`
- Source controller: `IncidentIQ API`

Get SLAs

Retrieves all service level agreements (SLAs) configured for the current site. SLAs define response time and resolution time targets that help ensure consistent service quality for tickets.

**Workflow Example**
1. Call this endpoint: [GET /api/v1.0/slas](#/SLAs/listSlas) to list all SLA definitions.
2. Use `$fields=metrics.*` to include metric configuration details.
3. Extract `SlaId` values for use with activation, deactivation, or deletion endpoints.

**Related Endpoints:**
- [POST /api/v1.0/slas/new](#/SLAs/createSla) - Create a new SLA
- [POST /api/v1.0/slas/{SlaId}/activate](#/SLAs/activateSla) - Activate an SLA
- [DELETE /api/v1.0/slas/{id}](#/SLAs/deleteSlaById) - Delete an SLA

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `fields` | `$fields` | `query` | `no` | `str` | `-` | - |
| `client` | `Client` | `header` | `no` | `str` | `-` | - |
| `product_id` | `ProductId` | `header` | `no` | `int` | `-` | - |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | - |

#### Returns

- Typed call return: `GenericObject`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `GenericObject`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
