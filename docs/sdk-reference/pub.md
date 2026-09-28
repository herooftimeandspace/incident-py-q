# `pub` Golden Namespace

Sync client access: `client.pub`

Async client access: `client.pub` with `await` on method calls.

These methods are Golden because they come from the bundled Incident IQ OpenAPI contract.

## Methods

### `search_spare_pool_assets`

Provenance: Golden OpenAPI contract

Operation ID: `searchSparePoolAssets`

- Sync: `client.pub.search_spare_pool_assets(s=None, body=..., timeout=None)`
- Async: `await client.pub.search_spare_pool_assets(s=None, body=..., timeout=None)`
- Raw payload: `client.pub.search_spare_pool_assets.raw(s=None, body=..., timeout=None)`
- HTTP route: `POST /pub/iq-modules-assets-search/v1/assets`
- Source controller: `IncidentIQ API`

Search spare pool assets

Queries the spare pool management service for loaner devices that satisfy the supplied filters.

**Prerequisites**
1. **Pool selection** – Call POST /apps/sparePoolManagement/api/pools to list available pools and capture `Id`.
2. **Custom field filters** – Review spare-specific metadata requirements (for example `IssueDate`) so you can add the appropriate `AssetCustomField` filter.

**Workflow Example**
1. Load spare pools: POST /apps/sparePoolManagement/api/pools and select the pool closest to the ticket location.
2. Search for available devices: POST /pub/iq-modules-assets-search/v1/assets with filters such as `assetsparepool`, `AssetCustomField` (IssueDate not set), and `ParentAsset` null.
3. Issue a spare: submit the selected `AssetId` to POST /apps/sparePoolManagement/api/asset/issue along with the ticket and agent identifiers.

**Minimal Required Fields**: Filters array (must include `assetsparepool`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of records to return per page. |
| `body` | `body` | `body` | `yes` | `SparePoolAssetSearchRequest` | `SparePoolAssetSearchRequest` | - |

#### Returns

- Typed call return: `SparePoolAssetSearchResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `SparePoolAssetSearchResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
