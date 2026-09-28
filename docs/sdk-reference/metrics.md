# `metrics` Golden Namespace

Sync client access: `client.metrics`

Async client access: `client.metrics` with `await` on method calls.

These methods are Golden because they come from the bundled Incident IQ OpenAPI contract.

## Aliases

| Alias | Canonical Method | Route |
| --- | --- | --- |
| `create` | `create_metric` | `POST /api/v1.0/metrics/new` |

## Methods

### `create_metric`

Provenance: Golden OpenAPI contract

Operation ID: `createMetric`

- Sync: `client.metrics.create_metric(client=None, product_id=None, site_id=None, timeout=None)`
- Async: `await client.metrics.create_metric(client=None, product_id=None, site_id=None, timeout=None)`
- Raw payload: `client.metrics.create_metric.raw(client=None, product_id=None, site_id=None, timeout=None)`
- HTTP route: `POST /api/v1.0/metrics/new`
- Source controller: `IncidentIQ API`
- Aliases: `create`

Create New Custom Metric

Creates a new custom metric type for tracking SLA performance. Custom metrics allow organizations to define organization-specific measurements beyond the built-in metric types.

**Workflow Example**
1. Review existing metrics: [GET /api/v1.0/metrics/types](#/SLAs/listMetrics) to avoid duplicates.
2. Define the metric configuration in the request body (name, calculation method, thresholds).
3. Call this endpoint: [POST /api/v1.0/metrics/new](#/SLAs/createMetric) with the metric definition.
4. Use the returned MetricId when configuring SLAs.

**Related Endpoints:**
- [GET /api/v1.0/metrics](#/SLAs/listMetricMetrics) - List all custom metrics
- [DELETE /api/v1.0/metrics/{id}](#/SLAs/deleteMetricMetrics) - Remove a custom metric

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

### `create_metric_by_id`

Provenance: Golden OpenAPI contract

Operation ID: `createMetricById`

- Sync: `client.metrics.create_metric_by_id(client=None, product_id=None, site_id=None, id=..., timeout=None)`
- Async: `await client.metrics.create_metric_by_id(client=None, product_id=None, site_id=None, id=..., timeout=None)`
- Raw payload: `client.metrics.create_metric_by_id.raw(client=None, product_id=None, site_id=None, id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/metrics/for/sla/{id}`
- Source controller: `IncidentIQ API`

Update Metrics for SLA

Retrieves or recalculates SLA-related metrics for the specified SLA record, returning aggregated counts used for reporting and dashboard widgets. Use this endpoint after creating or updating an SLA, or when you need a fresh metrics snapshot for compliance reporting.

**Prerequisites**
1. **id** - Use [GET /api/v1.0/slas](#/SLAs/listSlas) to list SLAs and extract `Items[].SlaId`.

**Workflow Example**
1. List SLAs: [GET /api/v1.0/slas](#/SLAs/listSlas) -> capture the target `SlaId`.
2. Refresh metrics: [POST /api/v1.0/metrics/for/sla/{id}](#/SLAs/createMetricById) with the SLA UUID.
3. Use the response data to populate SLA dashboards or export metrics.

**Minimal Required Fields**: id (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `client` | `Client` | `header` | `no` | `str` | `-` | - |
| `product_id` | `ProductId` | `header` | `no` | `int` | `-` | - |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | - |
| `id` | `id` | `path` | `yes` | `str` | `-` | The id parameter |

#### Returns

- Typed call return: `GenericObject`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `GenericObject`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_metric_metrics`

Provenance: Golden OpenAPI contract

Operation ID: `deleteMetricMetrics`

- Sync: `client.metrics.delete_metric_metrics(client=None, product_id=None, site_id=None, id=..., timeout=None)`
- Async: `await client.metrics.delete_metric_metrics(client=None, product_id=None, site_id=None, id=..., timeout=None)`
- Raw payload: `client.metrics.delete_metric_metrics.raw(client=None, product_id=None, site_id=None, id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/metrics/{id}`
- Source controller: `IncidentIQ API`

Delete Custom Metric

Deletes a custom metric type from the system. This permanently removes the metric definition and may affect SLAs that reference it.

**Prerequisites**
1. **id** - Use [GET /api/v1.0/metrics](#/SLAs/listMetricMetrics) to list custom metrics. Extract the target metric's UUID from the response.

**Workflow Example**
1. List custom metrics: [GET /api/v1.0/metrics](#/SLAs/listMetricMetrics) → identify metric to delete.
2. Verify no active SLAs depend on this metric.
3. Call this endpoint: [DELETE /api/v1.0/metrics/{id}](#/SLAs/deleteMetricMetrics) with the metric UUID.

**Warning**: Deleting a metric may affect historical reporting data. Consider deactivating SLAs that use this metric first.

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

### `get_metric_by_id`

Provenance: Golden OpenAPI contract

Operation ID: `getMetricById`

- Sync: `client.metrics.get_metric_by_id(client=None, product_id=None, site_id=None, type_id=..., timeout=None)`
- Async: `await client.metrics.get_metric_by_id(client=None, product_id=None, site_id=None, type_id=..., timeout=None)`
- Raw payload: `client.metrics.get_metric_by_id.raw(client=None, product_id=None, site_id=None, type_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/metrics/types/{typeId}`
- Source controller: `IncidentIQ API`

Get Metric Type

Retrieves a specific metric type definition by its unique identifier. Returns the metric configuration including name, calculation method, and threshold settings.

**Prerequisites**
1. **typeId** - Use [GET /api/v1.0/metrics/types](#/SLAs/listMetrics) to list available metric types. Extract `Items[].MetricTypeId` from the response.

**Workflow Example**
1. List metric types: [GET /api/v1.0/metrics/types](#/SLAs/listMetrics) → identify target metric.
2. Call this endpoint: [GET /api/v1.0/metrics/types/{typeId}](#/SLAs/getMetricById) with the metric type UUID.

**Related Endpoints:**
- [DELETE /api/v1.0/metrics/{id}](#/SLAs/deleteMetricMetrics) - Delete a custom metric type

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `client` | `Client` | `header` | `no` | `str` | `-` | - |
| `product_id` | `ProductId` | `header` | `no` | `int` | `-` | - |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | - |
| `type_id` | `typeId` | `path` | `yes` | `str` | `-` | The typeId parameter |

#### Returns

- Typed call return: `GenericObject`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `GenericObject`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_metric_metrics`

Provenance: Golden OpenAPI contract

Operation ID: `listMetricMetrics`

- Sync: `client.metrics.list_metric_metrics(client=None, product_id=None, site_id=None, timeout=None)`
- Async: `await client.metrics.list_metric_metrics(client=None, product_id=None, site_id=None, timeout=None)`
- Raw payload: `client.metrics.list_metric_metrics.raw(client=None, product_id=None, site_id=None, timeout=None)`
- HTTP route: `GET /api/v1.0/metrics`
- Source controller: `IncidentIQ API`

Get Metrics

Retrieves all custom metrics configured for the current site. Custom metrics extend the default SLA measurements with organization-specific performance indicators.

**Workflow Example**
1. Call this endpoint: [GET /api/v1.0/metrics](#/SLAs/listMetricMetrics) to list all custom metrics.
2. Use returned metric IDs when configuring SLA definitions or building reports.
3. Create new metrics via [POST /api/v1.0/metrics/new](#/SLAs/createMetric) if needed.

**Related Endpoints:**
- [GET /api/v1.0/metrics/types](#/SLAs/listMetrics) - List metric type definitions
- [POST /api/v1.0/metrics/for/sla/{id}](#/SLAs/createMetricById) - Refresh metrics for a specific SLA

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

### `list_metrics`

Provenance: Golden OpenAPI contract

Operation ID: `listMetrics`

- Sync: `client.metrics.list_metrics(client=None, product_id=None, site_id=None, timeout=None)`
- Async: `await client.metrics.list_metrics(client=None, product_id=None, site_id=None, timeout=None)`
- Raw payload: `client.metrics.list_metrics.raw(client=None, product_id=None, site_id=None, timeout=None)`
- HTTP route: `GET /api/v1.0/metrics/types`
- Source controller: `IncidentIQ API`

Get Metric Types

Retrieves all available metric type definitions used to measure SLA performance. Metric types define the categories of measurements tracked for service level agreements, such as response time, resolution time, and customer satisfaction.

**Workflow Example**
1. Call this endpoint: [GET /api/v1.0/metrics/types](#/SLAs/listMetrics) to list all metric types.
2. Use the returned metric type IDs when creating or configuring SLAs.
3. Reference specific metrics via [GET /api/v1.0/metrics/types/{typeId}](#/SLAs/getMetricById).

**Related Endpoints:**
- [POST /api/v1.0/metrics/new](#/SLAs/createMetric) - Create a new custom metric type
- [GET /api/v1.0/slas](#/SLAs/listSlas) - List SLAs that use these metrics

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
