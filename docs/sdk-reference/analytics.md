# `analytics` Golden Namespace

Sync client access: `client.analytics`

Async client access: `client.analytics` with `await` on method calls.

These methods are Golden because they come from the bundled Incident IQ OpenAPI contract.

## Methods

### `get_asset_audit_policy_periods_by_status`

Provenance: Golden OpenAPI contract

Operation ID: `getAssetAuditPolicyPeriodsByStatus`

- Sync: `client.analytics.get_asset_audit_policy_periods_by_status(asset_audit_policy_schedule_id=..., timeout=None)`
- Async: `await client.analytics.get_asset_audit_policy_periods_by_status(asset_audit_policy_schedule_id=..., timeout=None)`
- Raw payload: `client.analytics.get_asset_audit_policy_periods_by_status.raw(asset_audit_policy_schedule_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/analytics/audit-policies/by-schedule-period-status/{AssetAuditPolicyScheduleId}`
- Source controller: `IncidentIQ API`

Get audit policy period counts by status for a schedule

Retrieves audit period statistics aggregated by status for a specific audit policy schedule. This shows the distribution of audit periods (e.g., Completed, In Progress, Overdue, Scheduled) within the schedule.

**Prerequisites:**
1. **AssetAuditPolicyScheduleId** - Obtain from [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById) response field `Item.AssetAuditPolicyScheduleId`.

**Workflow Example:**
1. Query an asset using [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById)
2. Extract the `AssetAuditPolicyScheduleId` from the response
3. Call this endpoint to retrieve period status statistics for that audit schedule

**Minimal Required Fields:**
- `AssetAuditPolicyScheduleId` (path parameter): UUID of the audit policy schedule

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_audit_policy_schedule_id` | `AssetAuditPolicyScheduleId` | `path` | `yes` | `str` | `-` | The unique identifier of the asset audit policy schedule |

#### Returns

- Typed call return: `InlineObject`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InlineObject`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_audit_policy_periods_by_status_for_asset`

Provenance: Golden OpenAPI contract

Operation ID: `getAssetAuditPolicyPeriodsByStatusForAsset`

- Sync: `client.analytics.get_asset_audit_policy_periods_by_status_for_asset(asset_audit_policy_schedule_id=..., asset_id=..., timeout=None)`
- Async: `await client.analytics.get_asset_audit_policy_periods_by_status_for_asset(asset_audit_policy_schedule_id=..., asset_id=..., timeout=None)`
- Raw payload: `client.analytics.get_asset_audit_policy_periods_by_status_for_asset.raw(asset_audit_policy_schedule_id=..., asset_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/analytics/audit-policies/by-schedule-period-status/{AssetAuditPolicyScheduleId}/for-asset/{AssetId}`
- Source controller: `IncidentIQ API`

Get audit policy period counts by status for a schedule and specific asset

Retrieves audit period statistics aggregated by status for a specific audit policy schedule scoped to an individual asset. This shows the audit history and compliance status for a single asset across schedule periods.

**Prerequisites:**
1. **AssetAuditPolicyScheduleId** - Obtain from [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById) response field `Item.AssetAuditPolicyScheduleId`.
2. **AssetId** - Use [POST /api/v1.0/assets](#/Assets/searchAssets) to search for assets and obtain `Items[].AssetId` values.

**Workflow Example:**
1. Search for assets using [POST /api/v1.0/assets](#/Assets/searchAssets)
2. Select an asset and retrieve its details using [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById)
3. Extract both `AssetId` and `AssetAuditPolicyScheduleId` from the response
4. Call this endpoint to retrieve asset-specific audit period statistics

**Minimal Required Fields:**
- `AssetAuditPolicyScheduleId` (path parameter): UUID of the audit policy schedule
- `AssetId` (path parameter): UUID of the asset

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_audit_policy_schedule_id` | `AssetAuditPolicyScheduleId` | `path` | `yes` | `str` | `-` | The unique identifier of the asset audit policy schedule |
| `asset_id` | `AssetId` | `path` | `yes` | `str` | `-` | The unique identifier of the asset |

#### Returns

- Typed call return: `InlineObject`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InlineObject`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_counts_by_audit_policy_coverage`

Provenance: Golden OpenAPI contract

Operation ID: `getAssetCountsByAuditPolicyCoverage`

- Sync: `client.analytics.get_asset_counts_by_audit_policy_coverage(timeout=None)`
- Async: `await client.analytics.get_asset_counts_by_audit_policy_coverage(timeout=None)`
- Raw payload: `client.analytics.get_asset_counts_by_audit_policy_coverage.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/analytics/assets/by-audit-policy-coverage`
- Source controller: `IncidentIQ API`

Get asset counts by audit policy coverage

Retrieves asset inventory statistics aggregated by audit policy coverage status. This endpoint shows the distribution of assets based on whether they are covered by active audit policies or not, enabling visibility into audit compliance coverage across your asset inventory.

**Use Cases:**
- Identifying gaps in audit policy coverage
- Measuring audit compliance program reach
- Generating coverage reports for compliance audits
- Planning audit policy expansion initiatives

**Minimal Required Fields:**
None - this endpoint requires no parameters and returns organization-wide aggregated coverage statistics.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `InlineObject`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InlineObject`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_counts_by_audit_policy_schedule_status`

Provenance: Golden OpenAPI contract

Operation ID: `getAssetCountsByAuditPolicyScheduleStatus`

- Sync: `client.analytics.get_asset_counts_by_audit_policy_schedule_status(asset_audit_policy_schedule_id=..., timeout=None)`
- Async: `await client.analytics.get_asset_counts_by_audit_policy_schedule_status(asset_audit_policy_schedule_id=..., timeout=None)`
- Raw payload: `client.analytics.get_asset_counts_by_audit_policy_schedule_status.raw(asset_audit_policy_schedule_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/analytics/assets/by-audit-policy-schedule-status/{AssetAuditPolicyScheduleId}`
- Source controller: `IncidentIQ API`

Get asset counts by audit policy schedule status

Returns asset counts grouped by audit policy status (Verified, Pending, At Risk, Failed) for a single audit policy schedule. This endpoint narrows the analytics query to assets currently assigned to the schedule so you can track compliance for a specific audit run cadence.

**Prerequisites**
1. **AssetAuditPolicyScheduleId** – Use [POST /api/v1.0/assets](#/Assets/searchAssets) to locate an asset governed by the target schedule, then load [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById) and read `Item.AssetAuditPolicyScheduleId` from the response.

**Workflow Example**
1. Search assets: [POST /api/v1.0/assets](#/Assets/searchAssets) and select an asset assigned to the desired audit schedule.
2. Load the asset: [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById) to capture `Item.AssetAuditPolicyScheduleId`.
3. Call [GET /api/v1.0/analytics/assets/by-audit-policy-schedule-status/{AssetAuditPolicyScheduleId}](#/Audit Policies/getAssetCountsByAuditPolicyScheduleStatus) to retrieve the compliance distribution.
4. Use the counts to populate schedule-level compliance reporting or escalation alerts.

**Minimal Required Fields**: `AssetAuditPolicyScheduleId` (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_audit_policy_schedule_id` | `AssetAuditPolicyScheduleId` | `path` | `yes` | `str` | `-` | Unique identifier of the audit policy schedule to summarize. |

#### Returns

- Typed call return: `AnalyticsAuditPolicyScheduleStatusListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AnalyticsAuditPolicyScheduleStatusListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_counts_by_audit_policy_status`

Provenance: Golden OpenAPI contract

Operation ID: `getAssetCountsByAuditPolicyStatus`

- Sync: `client.analytics.get_asset_counts_by_audit_policy_status(asset_audit_policy_id=..., timeout=None)`
- Async: `await client.analytics.get_asset_counts_by_audit_policy_status(asset_audit_policy_id=..., timeout=None)`
- Raw payload: `client.analytics.get_asset_counts_by_audit_policy_status.raw(asset_audit_policy_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/analytics/assets/by-audit-policy-status/{AssetAuditPolicyId}`
- Source controller: `IncidentIQ API`

Get asset counts by audit policy status

Returns asset counts grouped by audit policy status (Verified, Pending, At Risk, Failed) for a single audit policy. The analytics manager evaluates the policy's compliance rules against current asset verification history and summarizes the live compliance posture for that policy.

**Prerequisites**
1. **AssetAuditPolicyId** – Use [POST /api/v1.0/assets](#/Assets/searchAssets) to locate an asset that participates in the policy, then load [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById) and read `Item.AssetAuditPolicyId` from the response.

**Workflow Example**
1. Search assets: [POST /api/v1.0/assets](#/Assets/searchAssets) and select an asset that is governed by the audit policy you want to analyze.
2. Load the asset: [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById) to capture `Item.AssetAuditPolicyId`.
3. Call [GET /api/v1.0/analytics/assets/by-audit-policy-status/{AssetAuditPolicyId}](#/Audit Policies/getAssetCountsByAuditPolicyStatus) to obtain the compliance distribution.
4. Display the counts in a stacked bar or KPI tile set for the selected policy.

**Minimal Required Fields**: `AssetAuditPolicyId` (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_audit_policy_id` | `AssetAuditPolicyId` | `path` | `yes` | `str` | `-` | Unique identifier of the audit policy to summarize. |

#### Returns

- Typed call return: `AnalyticsAuditPolicyStatusListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AnalyticsAuditPolicyStatusListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_counts_by_audit_policy_verification_location`

Provenance: Golden OpenAPI contract

Operation ID: `getAssetCountsByAuditPolicyVerificationLocation`

- Sync: `client.analytics.get_asset_counts_by_audit_policy_verification_location(asset_audit_policy_id=..., timeout=None)`
- Async: `await client.analytics.get_asset_counts_by_audit_policy_verification_location(asset_audit_policy_id=..., timeout=None)`
- Raw payload: `client.analytics.get_asset_counts_by_audit_policy_verification_location.raw(asset_audit_policy_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/analytics/assets/by-audit-policy-verification-location/{AssetAuditPolicyId}`
- Source controller: `IncidentIQ API`

Get asset counts by audit verification location for a policy

Retrieves asset statistics aggregated by the location where verification occurred for a specific audit policy. This shows the geographic distribution of verification events across locations.

**Prerequisites:**
1. **AssetAuditPolicyId** - Obtain from [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById) response field `Item.AssetAuditPolicyId`.

**Workflow Example:**
1. Query an asset using [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById)
2. Extract the `AssetAuditPolicyId` from the response
3. Call this endpoint to retrieve verification location statistics for that audit policy

**Minimal Required Fields:**
- `AssetAuditPolicyId` (path parameter): UUID of the asset audit policy

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_audit_policy_id` | `AssetAuditPolicyId` | `path` | `yes` | `str` | `-` | The unique identifier of the asset audit policy |

#### Returns

- Typed call return: `InlineObject`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InlineObject`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_counts_by_audit_policy_verification_type`

Provenance: Golden OpenAPI contract

Operation ID: `getAssetCountsByAuditPolicyVerificationType`

- Sync: `client.analytics.get_asset_counts_by_audit_policy_verification_type(asset_audit_policy_id=..., timeout=None)`
- Async: `await client.analytics.get_asset_counts_by_audit_policy_verification_type(asset_audit_policy_id=..., timeout=None)`
- Raw payload: `client.analytics.get_asset_counts_by_audit_policy_verification_type.raw(asset_audit_policy_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/analytics/assets/by-audit-policy-verification-type/{AssetAuditPolicyId}`
- Source controller: `IncidentIQ API`

Get asset counts by audit verification type for a policy

Retrieves asset statistics aggregated by verification type (e.g., Barcode Scan, Manual Entry, NFC) for a specific audit policy. This shows how assets covered by the policy are being verified in practice.

**Prerequisites:**
1. **AssetAuditPolicyId** - Obtain from [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById) response field `Item.AssetAuditPolicyId`.

**Workflow Example:**
1. Query an asset using [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById)
2. Extract the `AssetAuditPolicyId` from the response
3. Call this endpoint to retrieve verification type statistics for that audit policy

**Minimal Required Fields:**
- `AssetAuditPolicyId` (path parameter): UUID of the asset audit policy

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_audit_policy_id` | `AssetAuditPolicyId` | `path` | `yes` | `str` | `-` | The unique identifier of the asset audit policy |

#### Returns

- Typed call return: `InlineObject`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InlineObject`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_counts_by_audit_status`

Provenance: Golden OpenAPI contract

Operation ID: `getAssetCountsByAuditStatus`

- Sync: `client.analytics.get_asset_counts_by_audit_status(timeout=None)`
- Async: `await client.analytics.get_asset_counts_by_audit_status(timeout=None)`
- Raw payload: `client.analytics.get_asset_counts_by_audit_status.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/analytics/assets/by-audit-status`
- Source controller: `IncidentIQ API`

Get asset counts by audit status

Retrieves asset inventory statistics aggregated by their current audit status (e.g., Compliant, Overdue, Pending Verification, Not Audited). This endpoint provides a comprehensive view of audit compliance across your asset inventory.

**Use Cases:**
- Monitoring audit compliance rates across asset inventory
- Identifying overdue or non-compliant assets requiring attention
- Building audit status dashboards and compliance reports
- Tracking audit verification progress and completion rates

**Minimal Required Fields:**
None - this endpoint requires no parameters and returns organization-wide aggregated audit status statistics.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `InlineObject`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InlineObject`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_counts_by_status_type`

Provenance: Golden OpenAPI contract

Operation ID: `getAssetCountsByStatusType`

- Sync: `client.analytics.get_asset_counts_by_status_type(timeout=None)`
- Async: `await client.analytics.get_asset_counts_by_status_type(timeout=None)`
- Raw payload: `client.analytics.get_asset_counts_by_status_type.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/analytics/assets/by-status`
- Source controller: `IncidentIQ API`

Get asset counts by status type

Returns asset counts grouped by status type (Active, Deployed, In Repair, In Storage, Retired, etc.). This endpoint is ideal for asset inventory dashboards and status distribution charts.

**Use Cases**:
- Asset inventory dashboards showing distribution across statuses
- Capacity planning for storage and repair facilities
- Tracking deployment progress across the organization
- Identifying assets that need attention (In Repair, Retired)

**Data Points Returned**:
Each data point includes:
- **Name**: Display name of the asset status (e.g., "Active", "Deployed")
- **Value**: Count of assets in this status
- **Id**: Status type identifier for drill-down operations
- **Date**: Timestamp (null for this aggregate)

**Prerequisites**: None - this endpoint uses the authenticated user's site context and permissions.

**Workflow Example**
1. Call [GET /api/v1.0/analytics/assets/by-status](#/Analytics/getAssetCountsByStatusType) to retrieve current asset counts by status
2. (Optional) Use the returned `Id` values to filter asset searches for specific status types
3. Display the data in a pie chart, bar chart, or summary cards on your dashboard

**Minimal Required Fields**: None; uses caller's authentication context.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `AnalyticsAssetStatusListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AnalyticsAssetStatusListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_summary_stats`

Provenance: Golden OpenAPI contract

Operation ID: `getAssetSummaryStats`

- Sync: `client.analytics.get_asset_summary_stats(asset_id=..., timeout=None)`
- Async: `await client.analytics.get_asset_summary_stats(asset_id=..., timeout=None)`
- Raw payload: `client.analytics.get_asset_summary_stats.raw(asset_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/analytics/asset/{AssetId}/summary-stats`
- Source controller: `IncidentIQ API`

Get asset summary statistics

Returns aggregated ticket statistics for a specific asset. This endpoint is ideal for asset detail pages, showing the ticket history and service activity for the asset.

**Statistics Returned**:
- **OpenTickets**: Currently open tickets for this asset
- **TotalTickets**: All-time ticket count
- **ClosedTickets**: Completed/closed tickets
- **AssignedTickets**: Tickets assigned related to this asset
- **Devices**: Related device count

**Prerequisites**
1. **AssetId** – Use [POST /api/v1.0/assets/search](#/Assets/searchAssets) to search for assets and capture `Items[].AssetId`.

**Workflow Example**
1. Search for asset: [POST /api/v1.0/assets/search](#/Assets/keywordSearchAssets) → extract `Items[0].AssetId`
2. Call [GET /api/v1.0/analytics/asset/{AssetId}/summary-stats](#/Analytics/getAssetSummaryStats) to retrieve summary statistics
3. Display the statistics on an asset detail page or service history panel

**Minimal Required Fields**: `AssetId` (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_id` | `AssetId` | `path` | `yes` | `str` | `-` | Unique identifier of the asset to retrieve statistics for. |

#### Returns

- Typed call return: `AggregateSummaryStatsResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AggregateSummaryStatsResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_verification_counts_by_location`

Provenance: Golden OpenAPI contract

Operation ID: `getAssetVerificationCountsByLocation`

- Sync: `client.analytics.get_asset_verification_counts_by_location(timeout=None)`
- Async: `await client.analytics.get_asset_verification_counts_by_location(timeout=None)`
- Raw payload: `client.analytics.get_asset_verification_counts_by_location.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/analytics/assets/by-verification-location`
- Source controller: `IncidentIQ API`

Get verified asset counts by location

Returns a list of locations with the number of assets whose most recent verification entry occurred at that location. The controller limits the dataset to the caller's site, discards deleted assets/verifications, and only counts each asset once by using its latest verification record.

**Prerequisites**
1. **locationId** – Use [GET /api/v2.0/locations/all](#/Locations/getAllSiteLocationsV2) to enumerate the locations that appear in your dashboard and capture `Items[].LocationId` so you can link a row from this response back to your directory data.

**Workflow Example**
1. List locations: [GET /api/v2.0/locations/all](#/Locations/getAllSiteLocationsV2) with `$s=500` to capture the full location directory and cache `LocationId`/`Name` pairs in the UI.
2. Call [GET /api/v1.0/analytics/assets/by-verification-location](#/Audit Policies/getAssetVerificationCountsByLocation) to obtain the current verification counts grouped by each location.
3. Merge the response with the cached directory data so users can click through to a location detail page or filter other queries using the same `LocationId`.

**Minimal Required Fields**: None; the endpoint uses the authenticated user's site and permissions.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `AnalyticsVerificationLocationListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AnalyticsVerificationLocationListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_verification_counts_by_type`

Provenance: Golden OpenAPI contract

Operation ID: `getAssetVerificationCountsByType`

- Sync: `client.analytics.get_asset_verification_counts_by_type(timeout=None)`
- Async: `await client.analytics.get_asset_verification_counts_by_type(timeout=None)`
- Raw payload: `client.analytics.get_asset_verification_counts_by_type.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/analytics/assets/by-verification-type`
- Source controller: `IncidentIQ API`

Get verified asset counts by verification type

Returns asset counts grouped by the verification method used for each asset's most recent verification record (for example Web Manual, Mobile Scan, Remote App). The analytics query filters out deleted assets and verifications and only counts each asset once by selecting its latest verification entry, making this ideal for compliance dashboards and process trend reporting.

**Prerequisites**: None; the endpoint runs against the authenticated user's site context.

**Workflow Example**
1. Call [GET /api/v1.0/analytics/assets/by-verification-type](#/Audit Policies/getAssetVerificationCountsByType) to retrieve the grouped counts.
2. Plot `Items[].Name` against `Items[].Value` in a bar or donut chart.
3. Compare counts week-over-week by caching the response and refreshing on a schedule.

**Minimal Required Fields**: None.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `AnalyticsVerificationTypeListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AnalyticsVerificationTypeListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_requestor_summary_stats`

Provenance: Golden OpenAPI contract

Operation ID: `getRequestorSummaryStats`

- Sync: `client.analytics.get_requestor_summary_stats(user_id=..., timeout=None)`
- Async: `await client.analytics.get_requestor_summary_stats(user_id=..., timeout=None)`
- Raw payload: `client.analytics.get_requestor_summary_stats.raw(user_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/analytics/requestor/{UserId}/summary-stats`
- Source controller: `IncidentIQ API`

Get requestor summary statistics

Returns aggregated ticket and device statistics for a specific user (requestor). This endpoint is ideal for user profile dashboards, self-service portals, and user activity reporting.

**Statistics Returned**:
- **OpenTickets**: Currently open tickets for this user
- **TotalTickets**: All-time ticket count
- **ClosedTickets**: Completed/closed tickets
- **AssignedTickets**: Tickets where this user is the agent
- **WaitingOnRequestorTickets**: Tickets pending user response
- **Devices**: Number of devices assigned to the user
- **CreatedForMeTickets**: Tickets where user is the requestor
- **CreatedForOthersTickets**: Tickets user created on behalf of others

**Prerequisites**
1. **UserId** – Use [POST /api/v1.0/search](#/Users/searchUsers) to search for users and capture `Item.Users[].UserId`, or use the special value `me` to get stats for the authenticated user.

**Workflow Example**
1. (Optional) Search for user: [POST /api/v1.0/search](#/Search/globalSearch) with UserTypes filter → extract `Item.Users[0].UserId`
2. Call [GET /api/v1.0/analytics/requestor/{UserId}/summary-stats](#/Analytics/getRequestorSummaryStats) to retrieve summary statistics
3. Display the statistics in a user profile dashboard or self-service portal

**Note**: This endpoint also supports the route `/api/v1.0/analytics/requestor/me/summary-stats` which returns statistics for the currently authenticated user without requiring a UserId.

**Minimal Required Fields**: `UserId` (path) or use `me` alias.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | Unique identifier of the user to retrieve statistics for. Use the special value `me` to get statistics for the currently authenticated user. |

#### Returns

- Typed call return: `AggregateSummaryStatsResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AggregateSummaryStatsResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
