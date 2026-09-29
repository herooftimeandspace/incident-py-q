# `silver.analytics` Namespace

Sync client access: `client.silver.analytics`

Async client access: `client.silver.analytics` with `await` on method calls.

These methods are Silver because the published contract does not document them directly, or because the SDK intentionally wraps a narrower Silver workflow around existing Golden operations. They remain separate so undocumented or convenience behavior never overrides the documented SDK surface.

## Methods

### `get_agent_current_stats`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.analytics.get_agent_current_stats(timeout=None)`
- Async: `await client.silver.analytics.get_agent_current_stats(timeout=None)`
- Raw payload: `client.silver.analytics.get_agent_current_stats.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/analytics/agent-current-stats`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.analytics`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic. The April 22, 2026 resize HAR showed the upload plus a later `GET /img/...?...w=150&h=150`, but no separate persisted crop endpoint, so the SDK applies the avatar framing locally. It accepts common local raster image formats including JPG/JPEG, PNG, GIF, WEBP, and BMP. For non-square inputs it uses the largest centered square crop, then converts the result inside `client.silver.profiles.post_profile_picture(...)` to PNG and downscales it until the uploaded PNG payload stays at or below 1 MB.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_agent_location_stats`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.analytics.get_agent_location_stats(timeout=None)`
- Async: `await client.silver.analytics.get_agent_location_stats(timeout=None)`
- Raw payload: `client.silver.analytics.get_agent_location_stats.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/analytics/agent-location-stats`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.analytics`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic. The April 22, 2026 resize HAR showed the upload plus a later `GET /img/...?...w=150&h=150`, but no separate persisted crop endpoint, so the SDK applies the avatar framing locally. For non-square inputs it uses the largest centered square crop, then converts the result inside `client.silver.profiles.post_profile_picture(...)` to PNG and downscales it until the uploaded PNG payload stays at or below 1 MB.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_report`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.analytics.get_report(report_id=..., timeout=None)`
- Async: `await client.silver.analytics.get_report(report_id=..., timeout=None)`
- Raw payload: `client.silver.analytics.get_report.raw(report_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/analytics/reports/{report_id}`
- Observed in: `migrated_from_golden_stoplight`

Get report details

#### Get information related to a given report.  Meta information for the overall report is returned.  For a listing of defined report elements associated with this report call GET `/api/v1.0/analytics/reports/elements/{ReportId}`.
#### Sample request:
```
GET /api/v1.0/analytics/reports/ac6cece8-e4f4-e511-a789-005056bb000e
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.analytics.get_report` (operationId `Analytics_GetReport`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `report_id` | `ReportId` | `path` | `yes` | `str` | Report ID of the record to modify |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_report_elements`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.analytics.get_report_elements(report_id=..., timeout=None)`
- Async: `await client.silver.analytics.get_report_elements(report_id=..., timeout=None)`
- Raw payload: `client.silver.analytics.get_report_elements.raw(report_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/analytics/reports/elements/{report_id}`
- Observed in: `migrated_from_golden_stoplight`

Get report elements

#### Get all elements defined for a given report.  Meta information for the overall report is not returned in this endpoint.  To obtain information regarding the overall report call GET `/api/v1.0/analytics/reports/{ReportId}`.
#### Sample request:
```
GET /api/v1.0/analytics/reports/elements/ac6cece8-e4f4-e511-a789-005056bb000e
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.analytics.get_report_elements` (operationId `Analytics_GetReportElements`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `report_id` | `ReportId` | `path` | `yes` | `str` | Report ID of the record to modify |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_report_queries`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.analytics.get_report_queries(report_id=..., timeout=None)`
- Async: `await client.silver.analytics.get_report_queries(report_id=..., timeout=None)`
- Raw payload: `client.silver.analytics.get_report_queries.raw(report_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/analytics/reports/queries/{report_id}`
- Observed in: `migrated_from_golden_stoplight`

Get report queries

#### Get all queries defined for a given report.  Meta information for the overall report is not returned in this endpoint.  To obtain information regarding the overall report call GET `/api/v1.0/analytics/reports/{ReportId}`.
#### Sample request:
```
GET /api/v1.0/analytics/reports/queries/ac6cece8-e4f4-e511-a789-005056bb000e
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.analytics.get_report_queries` (operationId `Analytics_GetReportQueries`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `report_id` | `ReportId` | `path` | `yes` | `str` | Report ID of the record to modify |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_reports`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.analytics.get_reports(timeout=None)`
- Async: `await client.silver.analytics.get_reports(timeout=None)`
- Raw payload: `client.silver.analytics.get_reports.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/analytics/reports`
- Observed in: `migrated_from_golden_stoplight`

Get all reports

#### Get all currently active and defined reports
#### Sample request:
```
GET /api/v1.0/analytics/reports
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.analytics.get_reports` (operationId `Analytics_GetReports`).

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---
