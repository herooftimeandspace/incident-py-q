# `analytics` Namespace

Sync client access: `client.analytics`

Async client access: `client.analytics` with `await` on method calls.

## Methods

### `get_asset_counts_by_audit_policy_coverage`

Operation ID: `Analytics_GetAssetCountsByAuditPolicyCoverage`

- Sync: `client.analytics.get_asset_counts_by_audit_policy_coverage(timeout=None)`
- Async: `await client.analytics.get_asset_counts_by_audit_policy_coverage(timeout=None)`
- Raw payload: `client.analytics.get_asset_counts_by_audit_policy_coverage.raw(timeout=None)`
- HTTP route: `GET /analytics/assets/by-audit-policy-coverage`
- Source controller: `Analytics`

Get audit policy coverage

#### Performs an analytics query to obtain a breakdown of asset counts grouped by asset audit policy coverage
#### Sample request:
```
GET /api/v1.0/analytics/assets/by-audit-policy-coverage
```

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `ListGetResponseOfAnalyticsDataPoint`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfAnalyticsDataPoint`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_counts_by_audit_policy_schedule_status`

Operation ID: `Analytics_GetAssetCountsByAuditPolicyScheduleStatus`

- Sync: `client.analytics.get_asset_counts_by_audit_policy_schedule_status(asset_audit_policy_schedule_id=..., timeout=None)`
- Async: `await client.analytics.get_asset_counts_by_audit_policy_schedule_status(asset_audit_policy_schedule_id=..., timeout=None)`
- Raw payload: `client.analytics.get_asset_counts_by_audit_policy_schedule_status.raw(asset_audit_policy_schedule_id=..., timeout=None)`
- HTTP route: `GET /analytics/assets/by-audit-policy-schedule-status/{AssetAuditPolicyScheduleId}`
- Source controller: `Analytics`

Get status by schedule

#### Performs an analytics query to obtain a breakdown of asset counts grouped by asset audit status for a given audit policy schedule
#### Sample request:
```
GET /api/v1.0/analytics/assets/by-audit-schedule-status/ac6cece8-e4f4-e511-a789-005056bb000e
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_audit_policy_schedule_id` | `AssetAuditPolicyScheduleId` | `path` | `yes` | `str` | `-` | Audit Policy Schedule ID of the record to modify |

#### Returns

- Typed call return: `ListGetResponseOfAnalyticsDataPoint`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfAnalyticsDataPoint`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_counts_by_audit_policy_status`

Operation ID: `Analytics_GetAssetCountsByAuditPolicyStatus`

- Sync: `client.analytics.get_asset_counts_by_audit_policy_status(asset_audit_policy_id=..., timeout=None)`
- Async: `await client.analytics.get_asset_counts_by_audit_policy_status(asset_audit_policy_id=..., timeout=None)`
- Raw payload: `client.analytics.get_asset_counts_by_audit_policy_status.raw(asset_audit_policy_id=..., timeout=None)`
- HTTP route: `GET /analytics/assets/by-audit-policy-status/{AssetAuditPolicyId}`
- Source controller: `Analytics`

Get status by policy

#### Performs an analytics query to obtain a breakdown of asset counts grouped by asset audit status for a given audit policy
#### Sample request:
```
GET /api/v1.0/analytics/assets/by-audit-status/ac6cece8-e4f4-e511-a789-005056bb000e
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_audit_policy_id` | `AssetAuditPolicyId` | `path` | `yes` | `str` | `-` | Audit Policy ID of the record to modify |

#### Returns

- Typed call return: `ListGetResponseOfAnalyticsDataPoint`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfAnalyticsDataPoint`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_counts_by_audit_status`

Operation ID: `Analytics_GetAssetCountsByAuditStatus`

- Sync: `client.analytics.get_asset_counts_by_audit_status(timeout=None)`
- Async: `await client.analytics.get_asset_counts_by_audit_status(timeout=None)`
- Raw payload: `client.analytics.get_asset_counts_by_audit_status.raw(timeout=None)`
- HTTP route: `GET /analytics/assets/by-audit-status`
- Source controller: `Analytics`

Get audit policy status

#### Performs an analytics query to obtain a breakdown of asset counts grouped by asset audit status
#### Sample request:
```
GET /api/v1.0/analytics/assets/by-audit-status
```

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `ListGetResponseOfAnalyticsDataPoint`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfAnalyticsDataPoint`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_counts_by_verification_location`

Operation ID: `Analytics_GetAssetCountsByVerificationLocation`

- Sync: `client.analytics.get_asset_counts_by_verification_location(timeout=None)`
- Async: `await client.analytics.get_asset_counts_by_verification_location(timeout=None)`
- Raw payload: `client.analytics.get_asset_counts_by_verification_location.raw(timeout=None)`
- HTTP route: `GET /analytics/assets/by-verification-location`
- Source controller: `Analytics`

Get assets by verification location

#### Performs an analytics query to obtain a breakdown of asset counts grouped by asset verification location
#### Sample request:
```
GET /api/v1.0/analytics/assets/by-verification-location
```

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `ListGetResponseOfAnalyticsDataPoint`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfAnalyticsDataPoint`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_counts_by_verification_type`

Operation ID: `Analytics_GetAssetCountsByVerificationType`

- Sync: `client.analytics.get_asset_counts_by_verification_type(timeout=None)`
- Async: `await client.analytics.get_asset_counts_by_verification_type(timeout=None)`
- Raw payload: `client.analytics.get_asset_counts_by_verification_type.raw(timeout=None)`
- HTTP route: `GET /analytics/assets/by-verification-type`
- Source controller: `Analytics`

Get assets by verification type

#### Performs an analytics query to obtain a breakdown of asset counts grouped by asset verification type
#### Sample request:
```
GET /api/v1.0/analytics/assets/by-verification-type
```

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `ListGetResponseOfAnalyticsDataPoint`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfAnalyticsDataPoint`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_report`

Operation ID: `Analytics_GetReport`

- Sync: `client.analytics.get_report(report_id=..., timeout=None)`
- Async: `await client.analytics.get_report(report_id=..., timeout=None)`
- Raw payload: `client.analytics.get_report.raw(report_id=..., timeout=None)`
- HTTP route: `GET /analytics/reports/{ReportId}`
- Source controller: `Analytics`

Get report details

#### Get information related to a given report.  Meta information for the overall report is returned.  For a listing of defined report elements associated with this report call GET `/api/v1.0/analytics/reports/elements/{ReportId}`.
#### Sample request:
```
GET /api/v1.0/analytics/reports/ac6cece8-e4f4-e511-a789-005056bb000e
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `report_id` | `ReportId` | `path` | `yes` | `str` | `-` | Report ID of the record to modify |

#### Returns

- Typed call return: `ItemGetResponseOfReport`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemGetResponseOfReport`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_report_elements`

Operation ID: `Analytics_GetReportElements`

- Sync: `client.analytics.get_report_elements(report_id=..., timeout=None)`
- Async: `await client.analytics.get_report_elements(report_id=..., timeout=None)`
- Raw payload: `client.analytics.get_report_elements.raw(report_id=..., timeout=None)`
- HTTP route: `GET /analytics/reports/elements/{ReportId}`
- Source controller: `Analytics`

Get report elements

#### Get all elements defined for a given report.  Meta information for the overall report is not returned in this endpoint.  To obtain information regarding the overall report call GET `/api/v1.0/analytics/reports/{ReportId}`.
#### Sample request:
```
GET /api/v1.0/analytics/reports/elements/ac6cece8-e4f4-e511-a789-005056bb000e
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `report_id` | `ReportId` | `path` | `yes` | `str` | `-` | Report ID of the record to modify |

#### Returns

- Typed call return: `ListGetResponseOfReportElement`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfReportElement`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_report_queries`

Operation ID: `Analytics_GetReportQueries`

- Sync: `client.analytics.get_report_queries(report_id=..., timeout=None)`
- Async: `await client.analytics.get_report_queries(report_id=..., timeout=None)`
- Raw payload: `client.analytics.get_report_queries.raw(report_id=..., timeout=None)`
- HTTP route: `GET /analytics/reports/queries/{ReportId}`
- Source controller: `Analytics`

Get report queries

#### Get all queries defined for a given report.  Meta information for the overall report is not returned in this endpoint.  To obtain information regarding the overall report call GET `/api/v1.0/analytics/reports/{ReportId}`.
#### Sample request:
```
GET /api/v1.0/analytics/reports/queries/ac6cece8-e4f4-e511-a789-005056bb000e
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `report_id` | `ReportId` | `path` | `yes` | `str` | `-` | Report ID of the record to modify |

#### Returns

- Typed call return: `ListGetResponseOfReportQuery`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfReportQuery`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_reports`

Operation ID: `Analytics_GetReports`

- Sync: `client.analytics.get_reports(timeout=None)`
- Async: `await client.analytics.get_reports(timeout=None)`
- Raw payload: `client.analytics.get_reports.raw(timeout=None)`
- HTTP route: `GET /analytics/reports`
- Source controller: `Analytics`

Get all reports

#### Get all currently active and defined reports
#### Sample request:
```
GET /api/v1.0/analytics/reports
```

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `ListGetResponseOfReport`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfReport`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
