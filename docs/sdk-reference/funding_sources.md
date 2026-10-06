# `funding_sources` Golden Namespace

Sync client access: `client.funding_sources`

Async client access: `client.funding_sources` with `await` on method calls.

These methods are Golden because they come from the bundled Incident IQ OpenAPI contract.

## Aliases

| Alias | Canonical Method | Route |
| --- | --- | --- |
| `create` | `create_funding_source` | `POST /api/v1.0/funding-sources/new` |

## Methods

### `create_funding_source`

Provenance: Golden OpenAPI contract

Operation ID: `createFundingSource`

- Sync: `client.funding_sources.create_funding_source(body=..., timeout=None)`
- Async: `await client.funding_sources.create_funding_source(body=..., timeout=None)`
- Raw payload: `client.funding_sources.create_funding_source.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/funding-sources/new`
- Source controller: `IncidentIQ API`
- Aliases: `create`

Create a funding source

Creates a single funding source record for budgeting and allocation tracking, returning the created resource with its assigned identifier and calculated balances.

**Prerequisites**
1. **Type/Status/Site/Product IDs** - Use [POST /api/v1.0/funding-sources/query](#/Funding%20Sources/searchFundingSources) to review existing records and reuse `FundingSourceTypeId`, `FundingSourceStatusTypeId`, `SiteId`, and `ProductId` values that are valid for your tenant.

**Workflow Example**
1. Review existing funding sources to capture valid type/status/site/product IDs.
2. Build the payload with name, allocation amount, and optional dates.
3. [POST /api/v1.0/funding-sources/new](#/Funding Sources/createFundingSource) to create the funding source.

**Minimal Required Fields**: `Name`, `FundingSourceTypeId`, `FundingSourceStatusTypeId`, `SiteId` (and any tenant-required fields such as `ProductId`).

**Note**: This API is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `UpdateFundingSourceRequest` | `UpdateFundingSourceRequest` | Funding source to create |

#### Returns

- Typed call return: `Any`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_funding_sources`

Provenance: Golden OpenAPI contract

Operation ID: `createFundingSources`

- Sync: `client.funding_sources.create_funding_sources(body=..., timeout=None)`
- Async: `await client.funding_sources.create_funding_sources(body=..., timeout=None)`
- Raw payload: `client.funding_sources.create_funding_sources.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/funding-sources/ids`
- Source controller: `IncidentIQ API`

Create multiple funding sources

Creates multiple funding sources in a single request, returning the created records with assigned identifiers. Use this when onboarding a batch of grants or budgets tied to the same fiscal cycle.

**Prerequisites**
1. **Type/Status/Site/Product IDs** - Use [POST /api/v1.0/funding-sources/query](#/Funding%20Sources/searchFundingSources) to review existing records and reuse `FundingSourceTypeId`, `FundingSourceStatusTypeId`, `SiteId`, and `ProductId` values that are valid for your tenant.

**Workflow Example**
1. Query existing funding sources to confirm valid IDs for type/status/site/product.
2. Build an array of funding source payloads with names, allocations, and dates.
3. [POST /api/v1.0/funding-sources/ids](#/Funding Sources/createFundingSources) to create them in a batch.

**Minimal Required Fields**: `Name`, `FundingSourceTypeId`, `FundingSourceStatusTypeId`, `SiteId` (and any tenant-required fields such as `ProductId`).

**Note**: This API is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | Array of funding sources to create |

#### Returns

- Typed call return: `Any`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_funding_source`

Provenance: Golden OpenAPI contract

Operation ID: `deleteFundingSource`

- Sync: `client.funding_sources.delete_funding_source(funding_source_id=..., timeout=None)`
- Async: `await client.funding_sources.delete_funding_source(funding_source_id=..., timeout=None)`
- Raw payload: `client.funding_sources.delete_funding_source.raw(funding_source_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/funding-sources/{FundingSourceId}/delete`
- Source controller: `IncidentIQ API`

Delete a funding source

Deletes a single funding source by ID. Use this to retire a funding source that should no longer be selectable in budgeting workflows.

**Prerequisites**
1. **FundingSourceId** - Use [POST /api/v1.0/funding-sources/query](#/Funding%20Sources/searchFundingSources) to locate the record and extract `Items[].FundingSourceId`.

**Workflow Example**
1. Search for the funding source to confirm the correct record.
2. [DELETE /api/v1.0/funding-sources/{FundingSourceId}/delete](#/Funding Sources/deleteFundingSource) to remove it.
3. Optionally re-query to ensure the record is gone.

**Minimal Required Fields**: `FundingSourceId` (path).

**Note**: This API is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `funding_source_id` | `FundingSourceId` | `path` | `yes` | `str` | `-` | UUID of the funding source to delete |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_funding_sources_by_ids`

Provenance: Golden OpenAPI contract

Operation ID: `deleteFundingSourcesByIds`

- Sync: `client.funding_sources.delete_funding_sources_by_ids(body=..., timeout=None)`
- Async: `await client.funding_sources.delete_funding_sources_by_ids(body=..., timeout=None)`
- Raw payload: `client.funding_sources.delete_funding_sources_by_ids.raw(body=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/funding-sources/ids`
- Source controller: `IncidentIQ API`

Delete funding sources by IDs

Deletes multiple funding sources in one call by providing a list of IDs. Use with caution; this is a bulk destructive operation and cannot be undone.

**Prerequisites**
1. **FundingSourceId list** - Use [POST /api/v1.0/funding-sources/query](#/Funding%20Sources/searchFundingSources) to identify records and collect `Items[].FundingSourceId`.

**Workflow Example**
1. Search for funding sources to confirm which records should be removed.
2. Submit [DELETE /api/v1.0/funding-sources/ids](#/Funding Sources/deleteFundingSourcesByIds) with the ID array to perform the bulk delete.
3. Optionally re-run the query to confirm the records no longer appear.

**Minimal Required Fields**: Request body array of `FundingSourceId` values.

**Note**: This API is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | Array of funding source UUIDs to delete |

#### Returns

- Typed call return: `ListDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_funding_sources_by_query`

Provenance: Golden OpenAPI contract

Operation ID: `deleteFundingSourcesByQuery`

- Sync: `client.funding_sources.delete_funding_sources_by_query(top=None, skip=None, timeout=None)`
- Async: `await client.funding_sources.delete_funding_sources_by_query(top=None, skip=None, timeout=None)`
- Raw payload: `client.funding_sources.delete_funding_sources_by_query.raw(top=None, skip=None, timeout=None)`
- HTTP route: `DELETE /api/v1.0/funding-sources/query`
- Source controller: `IncidentIQ API`

Delete funding sources by query

Deletes funding sources that match the supplied query window. Because this is a bulk destructive operation, you should always preview the result set before executing the delete.

**Prerequisites**
1. Review targets with [POST /api/v1.0/funding-sources/query](#/Funding%20Sources/searchFundingSources) and confirm the records you intend to remove.

**Workflow Example**
1. Preview matches: [POST /api/v1.0/funding-sources/query](#/Funding%20Sources/searchFundingSources) with the same filters you plan to delete.
2. Delete in batches: [DELETE /api/v1.0/funding-sources/query](#/Funding%20Sources/deleteFundingSourcesByQuery) with `$top`/`$skip` to control scope.
3. Re-run [POST /api/v1.0/funding-sources/query](#/Funding%20Sources/searchFundingSources) to confirm the records no longer appear.

**Minimal Required Fields**: None. Provide `$top`/`$skip` if you need batch control.

**Note**: This API is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `top` | `$top` | `query` | `no` | `int` | `-` | Maximum number of records to delete |
| `skip` | `$skip` | `query` | `no` | `int` | `-` | Number of records to skip |

#### Returns

- Typed call return: `ListDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_funding_source_by_id`

Provenance: Golden OpenAPI contract

Operation ID: `getFundingSourceById`

- Sync: `client.funding_sources.get_funding_source_by_id(funding_source_id=..., timeout=None)`
- Async: `await client.funding_sources.get_funding_source_by_id(funding_source_id=..., timeout=None)`
- Raw payload: `client.funding_sources.get_funding_source_by_id.raw(funding_source_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/funding-sources/{FundingSourceId}`
- Source controller: `IncidentIQ API`

Get funding source by ID

Retrieves a single funding source record for the supplied FundingSourceId, including allocation totals, status/type metadata, and lifecycle dates. Use this when you need authoritative values before editing or deleting a funding source.

**Prerequisites**
1. **FundingSourceId** - Use [POST /api/v1.0/funding-sources/query](#/Funding%20Sources/searchFundingSources) to list funding sources and extract `Items[].FundingSourceId`, or capture the ID returned from [POST /api/v1.0/funding-sources/new](#/Funding%20Sources/createFundingSource).

**Workflow Example**
1. Search: [POST /api/v1.0/funding-sources/query](#/Funding Sources/searchFundingSources) with filters (optional) to identify the funding source.
2. Retrieve detail: [GET /api/v1.0/funding-sources/{FundingSourceId}](#/Funding Sources/getFundingSourceById) to load full metadata for display or editing.

**Minimal Required Fields**: `FundingSourceId` (path).

**Note**: This API is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `funding_source_id` | `FundingSourceId` | `path` | `yes` | `str` | `-` | UUID of the funding source to retrieve |

#### Returns

- Typed call return: `Any`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_funding_sources_by_ids`

Provenance: Golden OpenAPI contract

Operation ID: `getFundingSourcesByIds`

- Sync: `client.funding_sources.get_funding_sources_by_ids(body=..., timeout=None)`
- Async: `await client.funding_sources.get_funding_sources_by_ids(body=..., timeout=None)`
- Raw payload: `client.funding_sources.get_funding_sources_by_ids.raw(body=..., timeout=None)`
- HTTP route: `GET /api/v1.0/funding-sources/ids`
- Source controller: `IncidentIQ API`

Get funding sources by IDs

Returns multiple funding sources in one call by posting an array of IDs. Useful when you already have a list of IDs from another workflow and need full objects in a single round trip.

**Prerequisites**
1. **FundingSourceId list** - Use [POST /api/v1.0/funding-sources/query](#/Funding%20Sources/searchFundingSources) to locate records and collect `Items[].FundingSourceId` (or reuse IDs returned from create endpoints).

**Workflow Example**
1. Search for funding sources and capture the IDs you need.
2. Call [GET /api/v1.0/funding-sources/ids](#/Funding Sources/getFundingSourcesByIds) with the ID array in the request body to retrieve full records.

**Minimal Required Fields**: Request body array of `FundingSourceId` values.

**Note**: This API is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | Array of funding source UUIDs to retrieve |

#### Returns

- Typed call return: `Any`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_funding_sources_legacy`

Provenance: Golden OpenAPI contract

Operation ID: `getFundingSourcesLegacy`

- Sync: `client.funding_sources.get_funding_sources_legacy(top=None, skip=None, orderby=None, orderby_direction=None, timeout=None)`
- Async: `await client.funding_sources.get_funding_sources_legacy(top=None, skip=None, orderby=None, orderby_direction=None, timeout=None)`
- Raw payload: `client.funding_sources.get_funding_sources_legacy.raw(top=None, skip=None, orderby=None, orderby_direction=None, timeout=None)`
- HTTP route: `GET /api/v1.0/funding-sources/query`
- Source controller: `IncidentIQ API`

List funding sources (legacy)

Retrieves a paginated list of funding sources using query parameters only. This legacy GET is helpful for simple paging, but it does not support the richer filter body available in the POST version.

**Prerequisites**
1. None.

**Workflow Example**
1. Call [GET /api/v1.0/funding-sources/query](#/Funding%20Sources/getFundingSourcesLegacy) with `$top`, `$skip`, and optional sort fields.
2. If you need advanced filters, switch to [POST /api/v1.0/funding-sources/query](#/Funding%20Sources/searchFundingSources) and reuse the IDs returned in `Items[].FundingSourceId`.
3. Fetch full details with [GET /api/v1.0/funding-sources/{FundingSourceId}](#/Funding%20Sources/getFundingSourceById) when preparing to update or delete.

**Minimal Required Fields**: None.

**Deprecated**: Use [POST /api/v1.0/funding-sources/query](#/Funding%20Sources/searchFundingSources) instead for complex filtering.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `top` | `$top` | `query` | `no` | `int` | `-` | Maximum number of records to return (page size) |
| `skip` | `$skip` | `query` | `no` | `int` | `-` | Number of records to skip for pagination |
| `orderby` | `$orderby` | `query` | `no` | `str` | `-` | Field name to sort by |
| `orderby_direction` | `$orderbyDirection` | `query` | `no` | `str` | `-` | Sort direction |

#### Returns

- Typed call return: `Any`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `search_funding_sources`

Provenance: Golden OpenAPI contract

Operation ID: `searchFundingSources`

- Sync: `client.funding_sources.search_funding_sources(top=None, skip=None, orderby=None, orderby_direction=None, body=None, timeout=None)`
- Async: `await client.funding_sources.search_funding_sources(top=None, skip=None, orderby=None, orderby_direction=None, body=None, timeout=None)`
- Raw payload: `client.funding_sources.search_funding_sources.raw(top=None, skip=None, orderby=None, orderby_direction=None, body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/funding-sources/query`
- Source controller: `IncidentIQ API`

Search funding sources

Searches funding sources with optional filters and pagination, returning the records that match the supplied criteria so you can pick IDs for detail, update, or delete workflows.

**Prerequisites**
1. None.

**Workflow Example**
1. Run [POST /api/v1.0/funding-sources/query](#/Funding%20Sources/searchFundingSources) with `Filters` to narrow the list and capture `Items[].FundingSourceId`.
2. Load details with [GET /api/v1.0/funding-sources/{FundingSourceId}](#/Funding%20Sources/getFundingSourceById) or apply changes with [POST /api/v1.0/funding-sources/{FundingSourceId}/update](#/Funding%20Sources/updateFundingSource).
3. If you need to retire records, call [DELETE /api/v1.0/funding-sources/{FundingSourceId}/delete](#/Funding%20Sources/deleteFundingSource) using the IDs from the search.

**Minimal Required Fields**: None. `Filters` and `OnlyShowDeleted` are optional; omit the body to return the default page.

**Note**: This API is deprecated. The entire FundingSourceController is marked as deprecated in v1.0.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `top` | `$top` | `query` | `no` | `int` | `-` | Maximum number of records to return (page size) |
| `skip` | `$skip` | `query` | `no` | `int` | `-` | Number of records to skip for pagination |
| `orderby` | `$orderby` | `query` | `no` | `str` | `-` | Field name to sort by |
| `orderby_direction` | `$orderbyDirection` | `query` | `no` | `str` | `-` | Sort direction |
| `body` | `body` | `body` | `no` | `InlineObject` | `InlineObject` | Search and filter parameters |

#### Returns

- Typed call return: `Any`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_funding_source`

Provenance: Golden OpenAPI contract

Operation ID: `updateFundingSource`

- Sync: `client.funding_sources.update_funding_source(funding_source_id=..., body=..., timeout=None)`
- Async: `await client.funding_sources.update_funding_source(funding_source_id=..., body=..., timeout=None)`
- Raw payload: `client.funding_sources.update_funding_source.raw(funding_source_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/funding-sources/{FundingSourceId}/update`
- Source controller: `IncidentIQ API`

Update a funding source

Updates a funding source by applying the fields provided in the request body. Only send the fields you want to change; omitted fields remain unchanged.

**Prerequisites**
1. **FundingSourceId** - Use [POST /api/v1.0/funding-sources/query](#/Funding%20Sources/searchFundingSources) to locate the record and extract `Items[].FundingSourceId`.
2. (Optional) Current values - Use [GET /api/v1.0/funding-sources/{FundingSourceId}](#/Funding%20Sources/getFundingSourceById) to review existing values before editing.

**Workflow Example**
1. Identify record: [POST /api/v1.0/funding-sources/query](#/Funding Sources/searchFundingSources) -> choose the target `FundingSourceId`.
2. Update: [POST /api/v1.0/funding-sources/{FundingSourceId}/update](#/Funding Sources/updateFundingSource) with the fields to change.
3. Verify: [GET /api/v1.0/funding-sources/{FundingSourceId}](#/Funding Sources/getFundingSourceById) to confirm updates.

**Minimal Required Fields**: `FundingSourceId` (path) plus at least one body field to update.

**Note**: This API is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `funding_source_id` | `FundingSourceId` | `path` | `yes` | `str` | `-` | UUID of the funding source to update |
| `body` | `body` | `body` | `yes` | `UpdateFundingSourceRequest` | `UpdateFundingSourceRequest` | Funding source fields to update |

#### Returns

- Typed call return: `ItemUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_funding_sources_by_query`

Provenance: Golden OpenAPI contract

Operation ID: `updateFundingSourcesByQuery`

- Sync: `client.funding_sources.update_funding_sources_by_query(body=..., timeout=None)`
- Async: `await client.funding_sources.update_funding_sources_by_query(body=..., timeout=None)`
- Raw payload: `client.funding_sources.update_funding_sources_by_query.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/funding-sources/query/update`
- Source controller: `IncidentIQ API`

Bulk update funding sources

Bulk-updates funding sources that match the provided filters by applying the fields in the `Update` object to every matching record. Use this to shift status, dates, or allocations across a cohort without editing records one by one.

**Prerequisites**
1. Identify targets with [POST /api/v1.0/funding-sources/query](#/Funding%20Sources/searchFundingSources) and validate the filters you plan to apply.

**Workflow Example**
1. Run [POST /api/v1.0/funding-sources/query](#/Funding%20Sources/searchFundingSources) to confirm the target set.
2. Submit [POST /api/v1.0/funding-sources/query/update](#/Funding%20Sources/updateFundingSourcesByQuery) with `Update` values and `Filters` to scope the change.
3. Verify results with [GET /api/v1.0/funding-sources/{FundingSourceId}](#/Funding%20Sources/getFundingSourceById) for a sample of updated records.

**Minimal Required Fields**: `Update` (fields to apply). Provide `Filters` to avoid updating all records.

**Note**: This API is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `UpdateFundingSourcesRequest` | `UpdateFundingSourcesRequest` | Bulk update request with filter criteria and update values |

#### Returns

- Typed call return: `ListUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
