# `silver.metrics` Namespace

Sync client access: `client.silver.metrics`

Async client access: `client.silver.metrics` with `await` on method calls.

These methods are Silver because the published contract does not document them directly, or because the SDK intentionally wraps a narrower Silver workflow around existing Golden operations. They remain separate so undocumented or convenience behavior never overrides the documented SDK surface.

## Methods

### `delete_metric_type`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.metrics.delete_metric_type(metric_type_id=..., timeout=None)`
- Async: `await client.silver.metrics.delete_metric_type(metric_type_id=..., timeout=None)`
- Raw payload: `client.silver.metrics.delete_metric_type.raw(metric_type_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/metrics/types/{metric_type_id}`
- Observed in: `migrated_from_golden_stoplight`

Delete Metric Type

#### Delete a specific SLA Metric Type
#### Sample request:
```
DELETE /api/v1.0/metrics/types/67a39334-d778-487c-95ae-07a776ed8201
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.metrics.delete_metric_type` (operationId `Sla_DeleteMetricType`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `metric_type_id` | `MetricTypeId` | `path` | `yes` | `str` | MetricTypeID of the MetricType to be deleted |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_metric`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.metrics.get_metric(metric_id=..., r=..., timeout=None)`
- Async: `await client.silver.metrics.get_metric(metric_id=..., r=..., timeout=None)`
- Raw payload: `client.silver.metrics.get_metric.raw(metric_id=..., r=..., timeout=None)`
- HTTP route: `GET /api/v1.0/metrics/{metric_id}`
- Observed in: `migrated_from_golden_stoplight`

Get SLA Metric

#### Retrieve a specific metric type by MetricId
#### Sample request:
```
GET /api/v1.0/metrics/2c6101d2-1ac8-4320-b234-74f51a3b2e58
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.metrics.get_metric` (operationId `Sla_GetMetric`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `metric_id` | `MetricId` | `path` | `yes` | `str` | MetricId of Metric being requested |
| `r` | `r` | `query` | `yes` | `Any` | Request Options specified for the Metric(s) |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_metrics_for_sla`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.metrics.get_metrics_for_sla(sla_id=..., r=..., timeout=None)`
- Async: `await client.silver.metrics.get_metrics_for_sla(sla_id=..., r=..., timeout=None)`
- Raw payload: `client.silver.metrics.get_metrics_for_sla.raw(sla_id=..., r=..., timeout=None)`
- HTTP route: `GET /api/v1.0/metrics/for/sla/{sla_id}`
- Observed in: `migrated_from_golden_stoplight`

Get Metrics for an SLA

#### Retrieves a list of metrics for a specific SLA.
#### Sample request:
```
GET /api/v1.0/metrics/for/sla/bd64e104-4c83-4744-a888-eeb760c03bfe
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.metrics.get_metrics_for_sla` (operationId `Sla_GetMetricsForSla`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `sla_id` | `SlaId` | `path` | `yes` | `str` | SlaId of SLA containing the Metrics being requested |
| `r` | `r` | `query` | `yes` | `Any` | Request Options specified for the Sla Metrics |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `update_metric`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.metrics.update_metric(metric_id=..., json_body=..., timeout=None)`
- Async: `await client.silver.metrics.update_metric(metric_id=..., json_body=..., timeout=None)`
- Raw payload: `client.silver.metrics.update_metric.raw(metric_id=..., json_body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/metrics/{metric_id}`
- Observed in: `migrated_from_golden_stoplight`

Migrated Silver route for POST /metrics/{MetricId}.

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.metrics.update_metric` (operationId `Sla_UpdateMetric`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `metric_id` | `MetricId` | `path` | `yes` | `str` | Path parameter migrated from the previous Golden SDK. |
| `json_body` | `Item` | `body` | `yes` | `dict[str, Any] | list[Any]` | Body parameter migrated from the previous Golden SDK. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `update_metric_type`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.metrics.update_metric_type(metric_type_id=..., json_body=..., timeout=None)`
- Async: `await client.silver.metrics.update_metric_type(metric_type_id=..., json_body=..., timeout=None)`
- Raw payload: `client.silver.metrics.update_metric_type.raw(metric_type_id=..., json_body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/metrics/types/{metric_type_id}`
- Observed in: `migrated_from_golden_stoplight`

Migrated Silver route for POST /metrics/types/{MetricTypeId}.

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.metrics.update_metric_type` (operationId `Sla_UpdateMetricType`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `metric_type_id` | `MetricTypeId` | `path` | `yes` | `str` | Path parameter migrated from the previous Golden SDK. |
| `json_body` | `Item` | `body` | `yes` | `dict[str, Any] | list[Any]` | Body parameter migrated from the previous Golden SDK. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---
