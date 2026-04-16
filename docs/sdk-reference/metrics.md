# `metrics` Namespace

Sync client access: `client.metrics`

Async client access: `client.metrics` with `await` on method calls.

## Aliases

| Alias | Canonical Method | Route |
| --- | --- | --- |
| `delete` | `delete_metric` | `DELETE /metrics/{MetricId}` |
| `get` | `get_metric` | `GET /metrics/{MetricId}` |
| `list` | `get_metrics` | `GET /metrics` |
| `update` | `update_metric` | `POST /metrics/{MetricId}` |

## Methods

### `delete_metric`

Operation ID: `Sla_DeleteMetric`

- Sync: `client.metrics.delete_metric(metric_id=..., timeout=None)`
- Async: `await client.metrics.delete_metric(metric_id=..., timeout=None)`
- Raw payload: `client.metrics.delete_metric.raw(metric_id=..., timeout=None)`
- HTTP route: `DELETE /metrics/{MetricId}`
- Source controller: `SLAs`
- Aliases: `delete`

Delete SLA Metric

#### Delete a specific SLA Metric
#### Sample request:
```
DELETE /api/v1.0/metrics/2c6101d2-1ac8-4320-b234-74f51a3b2e58
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `metric_id` | `MetricId` | `path` | `yes` | `str` | `-` | MetricID to be deleted |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_metric_type`

Operation ID: `Sla_DeleteMetricType`

- Sync: `client.metrics.delete_metric_type(metric_type_id=..., timeout=None)`
- Async: `await client.metrics.delete_metric_type(metric_type_id=..., timeout=None)`
- Raw payload: `client.metrics.delete_metric_type.raw(metric_type_id=..., timeout=None)`
- HTTP route: `DELETE /metrics/types/{MetricTypeId}`
- Source controller: `SLAs`

Delete Metric Type

#### Delete a specific SLA Metric Type
#### Sample request:
```
DELETE /api/v1.0/metrics/types/67a39334-d778-487c-95ae-07a776ed8201
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `metric_type_id` | `MetricTypeId` | `path` | `yes` | `str` | `-` | MetricTypeID of the MetricType to be deleted |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_metric`

Operation ID: `Sla_GetMetric`

- Sync: `client.metrics.get_metric(metric_id=..., r=..., timeout=None)`
- Async: `await client.metrics.get_metric(metric_id=..., r=..., timeout=None)`
- Raw payload: `client.metrics.get_metric.raw(metric_id=..., r=..., timeout=None)`
- HTTP route: `GET /metrics/{MetricId}`
- Source controller: `SLAs`
- Aliases: `get`

Get SLA Metric

#### Retrieve a specific metric type by MetricId
#### Sample request:
```
GET /api/v1.0/metrics/2c6101d2-1ac8-4320-b234-74f51a3b2e58
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `metric_id` | `MetricId` | `path` | `yes` | `str` | `-` | MetricId of Metric being requested |
| `r` | `r` | `query` | `yes` | `Any` | `-` | Request Options specified for the Metric(s) |

#### Returns

- Typed call return: `ItemGetResponseOfMetric`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemGetResponseOfMetric`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_metric_type`

Operation ID: `Sla_GetMetricType`

- Sync: `client.metrics.get_metric_type(metric_type_id=..., r=..., timeout=None)`
- Async: `await client.metrics.get_metric_type(metric_type_id=..., r=..., timeout=None)`
- Raw payload: `client.metrics.get_metric_type.raw(metric_type_id=..., r=..., timeout=None)`
- HTTP route: `GET /metrics/types/{MetricTypeId}`
- Source controller: `SLAs`

Get Metric Type

#### Retrieve a specific metric type by MetricTypeId
#### Sample request:
```
GET /api/v1.0/metrics/types/67a39334-d778-487c-95ae-07a776ed8201
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `metric_type_id` | `MetricTypeId` | `path` | `yes` | `str` | `-` | MetricTypeId of the MetricType being requested |
| `r` | `r` | `query` | `yes` | `Any` | `-` | Request Options specified for the MetricType(s) |

#### Returns

- Typed call return: `ItemGetResponseOfMetricType`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemGetResponseOfMetricType`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_metric_types`

Operation ID: `Sla_GetMetricTypes`

- Sync: `client.metrics.get_metric_types(r=..., timeout=None)`
- Async: `await client.metrics.get_metric_types(r=..., timeout=None)`
- Raw payload: `client.metrics.get_metric_types.raw(r=..., timeout=None)`
- HTTP route: `GET /metrics/types`
- Source controller: `SLAs`

Get Metric Types

#### Retrieves a list of metric types. A specific metric type can be retrieved via GET `api/v1.0/metrics/types/{MetricTypeId}`.
#### Sample request:
```
GET /api/v1.0/metrics/types
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `r` | `r` | `query` | `yes` | `Any` | `-` | Request Options specified for the MetricType(s) |

#### Returns

- Typed call return: `ListGetResponseOfMetricType`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfMetricType`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_metrics`

Operation ID: `Sla_GetMetrics`

- Sync: `client.metrics.get_metrics(r=..., timeout=None)`
- Async: `await client.metrics.get_metrics(r=..., timeout=None)`
- Raw payload: `client.metrics.get_metrics.raw(r=..., timeout=None)`
- HTTP route: `GET /metrics`
- Source controller: `SLAs`
- Aliases: `list`

Get All SLA Metrics

#### Retrieves a list of metrics. A specific metric can be retrieved via GET `api/v1.0/metrics/{MetricId}`.
#### Sample request:
```
GET /api/v1.0/metrics/
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `r` | `r` | `query` | `yes` | `Any` | `-` | Request Options specified for the Metric(s) |

#### Returns

- Typed call return: `ListGetResponseOfMetric`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfMetric`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_metrics_for_sla`

Operation ID: `Sla_GetMetricsForSla`

- Sync: `client.metrics.get_metrics_for_sla(sla_id=..., r=..., timeout=None)`
- Async: `await client.metrics.get_metrics_for_sla(sla_id=..., r=..., timeout=None)`
- Raw payload: `client.metrics.get_metrics_for_sla.raw(sla_id=..., r=..., timeout=None)`
- HTTP route: `GET /metrics/for/sla/{SlaId}`
- Source controller: `SLAs`

Get Metrics for an SLA

#### Retrieves a list of metrics for a specific SLA.
#### Sample request:
```
GET /api/v1.0/metrics/for/sla/bd64e104-4c83-4744-a888-eeb760c03bfe
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `sla_id` | `SlaId` | `path` | `yes` | `str` | `-` | SlaId of SLA containing the Metrics being requested |
| `r` | `r` | `query` | `yes` | `Any` | `-` | Request Options specified for the Sla Metrics |

#### Returns

- Typed call return: `ListGetResponseOfMetric`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfMetric`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_metric`

Operation ID: `Sla_UpdateMetric`

- Sync: `client.metrics.update_metric(metric_id=..., item=..., timeout=None)`
- Async: `await client.metrics.update_metric(metric_id=..., item=..., timeout=None)`
- Raw payload: `client.metrics.update_metric.raw(metric_id=..., item=..., timeout=None)`
- HTTP route: `POST /metrics/{MetricId}`
- Source controller: `SLAs`
- Aliases: `update`

No contract summary provided.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `metric_id` | `MetricId` | `path` | `yes` | `str` | `-` | - |
| `item` | `Item` | `body` | `yes` | `UpdateMetricRequest` | `UpdateMetricRequest` | - |

#### Returns

- Typed call return: `ItemUpdateResponseOfGuid`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemUpdateResponseOfGuid`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_metric_type`

Operation ID: `Sla_UpdateMetricType`

- Sync: `client.metrics.update_metric_type(metric_type_id=..., item=..., timeout=None)`
- Async: `await client.metrics.update_metric_type(metric_type_id=..., item=..., timeout=None)`
- Raw payload: `client.metrics.update_metric_type.raw(metric_type_id=..., item=..., timeout=None)`
- HTTP route: `POST /metrics/types/{MetricTypeId}`
- Source controller: `SLAs`

No contract summary provided.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `metric_type_id` | `MetricTypeId` | `path` | `yes` | `str` | `-` | - |
| `item` | `Item` | `body` | `yes` | `UpdateMetricTypeRequest` | `UpdateMetricTypeRequest` | - |

#### Returns

- Typed call return: `ItemUpdateResponseOfGuid`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemUpdateResponseOfGuid`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_metrics_for_sla`

Operation ID: `Sla_UpdateMetricsForSla`

- Sync: `client.metrics.update_metrics_for_sla(sla_id=..., items=..., timeout=None)`
- Async: `await client.metrics.update_metrics_for_sla(sla_id=..., items=..., timeout=None)`
- Raw payload: `client.metrics.update_metrics_for_sla.raw(sla_id=..., items=..., timeout=None)`
- HTTP route: `POST /metrics/for/sla/{SlaId}`
- Source controller: `SLAs`

No contract summary provided.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `sla_id` | `SlaId` | `path` | `yes` | `str` | `-` | - |
| `items` | `Items` | `body` | `yes` | `list[Any]` | `-` | - |

#### Returns

- Typed call return: `ListUpdateResponseOfGuid`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListUpdateResponseOfGuid`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
