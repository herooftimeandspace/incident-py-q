# `assets` Golden Namespace

Sync client access: `client.assets`

Async client access: `client.assets` with `await` on method calls.

These methods are Golden because they come from the bundled Incident IQ OpenAPI contract.

## Methods

### `add_asset_favorite`

Provenance: Golden OpenAPI contract

Operation ID: `addAssetFavorite`

- Sync: `client.assets.add_asset_favorite(asset_id=..., user_id=..., timeout=None)`
- Async: `await client.assets.add_asset_favorite(asset_id=..., user_id=..., timeout=None)`
- Raw payload: `client.assets.add_asset_favorite.raw(asset_id=..., user_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/favorites/{assetId}/{userId}`
- Source controller: `IncidentIQ API`

Add asset to favorites

Adds an asset to a user's favorites collection so it appears in quick-access views and ticket shortcuts.

**Prerequisites**
1. **assetId** - Call [GET /api/v1.0/assets](#/Assets/listAllAssets) and read `Items[].AssetId` from the returned assets list.
2. **userId** - Call [POST /api/v1.0/search](#/Search/globalSearch) with the user identifier (email, username, or barcode) and capture `Item.Users[].UserId`.

**Workflow Example**
1. Search for the user: [POST /api/v1.0/search](#/Search/globalSearch) to capture `UserId`.
2. List assets: [GET /api/v1.0/assets](#/Assets/listAllAssets) and select the target `AssetId`.
3. Favorite the asset: [POST /api/v1.0/assets/favorites/{assetId}/{userId}](#/Assets/addAssetFavorite).

**Minimal Required Fields**
- `AssetId` (path) - The asset to mark as a favorite.
- `UserId` (path) - The user whose favorite list is being updated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_id` | `assetId` | `path` | `yes` | `str` | `-` | UUID of the asset to add to favorites. Obtain via [POST /api/v1.0/assets](#/Assets/searchAssets), extract `Items[].AssetId` from response. |
| `user_id` | `userId` | `path` | `yes` | `str` | `-` | UUID of the user whose favorites are being updated. Obtain with POST /api/v1.0/search and read `Item.Users[].UserId`. |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `add_asset_files`

Provenance: Golden OpenAPI contract

Operation ID: `addAssetFiles`

- Sync: `client.assets.add_asset_files(asset_id=..., body=..., timeout=None)`
- Async: `await client.assets.add_asset_files(asset_id=..., body=..., timeout=None)`
- Raw payload: `client.assets.add_asset_files.raw(asset_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/{assetId}/files/new`
- Source controller: `IncidentIQ API`

Add files to asset

Attaches one or more files to an asset. Files must first be uploaded via the file upload endpoint, then associated with the asset using this endpoint.

**Prerequisites**
1. **AssetId** - Use [POST /api/v1.0/assets](#/Assets/searchAssets) to identify the asset and extract `Items[].AssetId`.
2. **FileIds** - Upload files using [POST /api/v1.0/files](#/Files/uploadFile) and extract `Item.FileId` from response.

**Workflow Example**
1. Upload file: [POST /api/v1.0/files](#/Files/uploadFile) with multipart form data.
2. Extract `Item.FileId` from upload response.
3. Call [POST /api/v1.0/assets/{assetId}/files/new](#/Assets/addAssetFiles) with the FileId(s) to attach.

**Minimal Required Fields**: FileIds array

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_id` | `assetId` | `path` | `yes` | `str` | `-` | UUID of the asset. Obtain via [POST /api/v1.0/assets](#/Assets/searchAssets), extract `Items[].AssetId` from response. |
| `body` | `body` | `body` | `yes` | `AddAssetFilesRequest` | `AddAssetFilesRequest` | - |

#### Returns

- Typed call return: `FileListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `FileListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `add_linked_assets`

Provenance: Golden OpenAPI contract

Operation ID: `addLinkedAssets`

- Sync: `client.assets.add_linked_assets(asset_id=..., body=..., timeout=None)`
- Async: `await client.assets.add_linked_assets(asset_id=..., body=..., timeout=None)`
- Raw payload: `client.assets.add_linked_assets.raw(asset_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/linked/to/{assetId}`
- Source controller: `IncidentIQ API`

Link assets to parent

Creates parent-child relationships between assets. Link peripherals, accessories, or components to a main asset for relationship tracking.

**Example Workflow:**
1. GET asset details for the parent device
2. GET asset details for peripherals to link
3. POST to this endpoint with the link definitions

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_id` | `assetId` | `path` | `yes` | `str` | `-` | UUID of the parent asset. Obtain via [POST /api/v1.0/assets](#/Assets/searchAssets), extract `Items[].AssetId` from response. |
| `body` | `body` | `body` | `yes` | `LinkedAssetListRequest` | `LinkedAssetListRequest` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `add_manufacturer_to_site`

Provenance: Golden OpenAPI contract

Operation ID: `addManufacturerToSite`

- Sync: `client.assets.add_manufacturer_to_site(manufacturer_id=..., include_all_models=None, timeout=None)`
- Async: `await client.assets.add_manufacturer_to_site(manufacturer_id=..., include_all_models=None, timeout=None)`
- Raw payload: `client.assets.add_manufacturer_to_site.raw(manufacturer_id=..., include_all_models=None, timeout=None)`
- HTTP route: `POST /api/v1.0/assets/manufacturers/{ManufacturerId}/site`
- Source controller: `IncidentIQ API`

Add manufacturer to site

Enables a global manufacturer at the current site, making it available for asset creation and management. Global manufacturers must be explicitly added to each site before they appear in that site's manufacturer lists.

**Prerequisites**
- **ManufacturerId** - Use [GET /api/v1.0/assets/manufacturers/global](#/Manufacturers/getGlobalManufacturers) to list available global manufacturers. Extract `Items[].ManufacturerId`.

**Workflow Example**
1. List global manufacturers: [GET /api/v1.0/assets/manufacturers/global](#/Manufacturers/getGlobalManufacturers)
2. Select manufacturer to enable at site
3. Add to site: [POST /api/v1.0/assets/manufacturers/{ManufacturerId}/site](#/Manufacturers/addManufacturerToSite)
4. (Optional) Set `IncludeAllModels=true` to also enable all models from this manufacturer

**Parameters**
- `IncludeAllModels` (query, optional) - When `true`, automatically adds all models from this manufacturer to the site. Default: `false`.

**Use Cases**
- Site administrator enabling new hardware vendors for their location
- Rolling out a new manufacturer across multiple sites
- Bulk setup of manufacturer and model catalog for a new site

**Related Endpoints**
- [GET /api/v1.0/assets/manufacturers/global](#/Manufacturers/getGlobalManufacturers) - List available global manufacturers
- [DELETE /api/v1.0/assets/manufacturers/{ManufacturerId}/site](#/Manufacturers/removeManufacturerFromSite) - Remove manufacturer from site
- [GET /api/v1.0/assets/manufacturers](#/Manufacturers/getManufacturers) - List manufacturers enabled at current site

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `manufacturer_id` | `ManufacturerId` | `path` | `yes` | `str` | `-` | Unique identifier of the manufacturer to add to the site |
| `include_all_models` | `IncludeAllModels` | `query` | `no` | `bool` | `-` | When true, also adds all models from this manufacturer to the site |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `bulk_create_asset_verifications`

Provenance: Golden OpenAPI contract

Operation ID: `bulkCreateAssetVerifications`

- Sync: `client.assets.bulk_create_asset_verifications(body=..., timeout=None)`
- Async: `await client.assets.bulk_create_asset_verifications(body=..., timeout=None)`
- Raw payload: `client.assets.bulk_create_asset_verifications.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/verifications/new`
- Source controller: `IncidentIQ API`

Bulk create verifications

Creates multiple asset verification records in a single request. Use this for batch verification workflows such as classroom sweeps or inventory audits.

**Workflow Example**
1. Prepare a list of assets to verify.
2. Build an array of `UpdateAssetVerificationRequest` objects.
3. [POST /api/v1.0/assets/verifications/new](#/Assets/bulkCreateAssetVerifications).

**Minimal Required Fields**: array of verification requests, each with AssetId, AssetVerificationTypeId, VerifiedByUserId, LocationId, IsSuccessful.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | - |

#### Returns

- Typed call return: `AssetVerificationBulkCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetVerificationBulkCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `bulk_delete_asset_verifications`

Provenance: Golden OpenAPI contract

Operation ID: `bulkDeleteAssetVerifications`

- Sync: `client.assets.bulk_delete_asset_verifications(body=..., timeout=None)`
- Async: `await client.assets.bulk_delete_asset_verifications(body=..., timeout=None)`
- Raw payload: `client.assets.bulk_delete_asset_verifications.raw(body=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/assets/verifications/ids/delete`
- Source controller: `IncidentIQ API`

Bulk delete verifications

Deletes multiple asset verification records by their IDs. Use this for bulk cleanup of erroneous or duplicate verifications.

**Workflow Example**
1. Query verifications to identify records for deletion.
2. Collect `AssetVerificationId` values.
3. [DELETE /api/v1.0/assets/verifications/ids/delete](#/Assets/bulkDeleteAssetVerifications) with ID array.

**Minimal Required Fields**: array of AssetVerificationId UUIDs in body.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | - |

#### Returns

- Typed call return: `ListDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `bulk_delete_linked_assets`

Provenance: Golden OpenAPI contract

Operation ID: `bulkDeleteLinkedAssets`

- Sync: `client.assets.bulk_delete_linked_assets(body=..., timeout=None)`
- Async: `await client.assets.bulk_delete_linked_assets(body=..., timeout=None)`
- Raw payload: `client.assets.bulk_delete_linked_assets.raw(body=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/assets/linked/to`
- Source controller: `IncidentIQ API`

Bulk delete linked assets

Removes multiple parent-child asset relationships in a single request. Unlike the single-parent delete endpoint, this allows unlinking assets across different parents.

**Prerequisites**
1. **Link identifiers** - For each relationship to remove, provide the `ParentAssetId` and `ChildAssetId`.

**Workflow Example**
1. Identify the linked asset relationships to remove.
2. [DELETE /api/v1.0/assets/linked/to](#/Assets/bulkDeleteLinkedAssets) with an array of LinkedAsset objects.

**Minimal Required Fields**: Array of objects with `ParentAssetId` and `ChildAssetId`.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `LinkedAssetListRequest` | `LinkedAssetListRequest` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `checkin_asset`

Provenance: Golden OpenAPI contract

Operation ID: `checkinAsset`

- Sync: `client.assets.checkin_asset(body=..., timeout=None)`
- Async: `await client.assets.checkin_asset(body=..., timeout=None)`
- Raw payload: `client.assets.checkin_asset.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/checkouts/checkin`
- Source controller: `IncidentIQ API`

Check in asset

Checks in an asset against an existing checkout and returns the resulting check-in transaction. Use this when a device is returned, swapped, or recovered so inventory status and ownership records stay accurate.

**Prerequisites**
1. **AssetId** - Use [POST /api/v1.0/assets/search](#/Assets/keywordSearchAssets) or [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById) to identify the asset being returned.
2. **OwnerId (if applicable)** - Use [POST /api/v1.0/search](#/Users/searchUsers) to identify the owner when checking in on behalf of a specific user.
3. (Optional) Validate the open checkout with [POST /api/v1.0/assets/checkouts/query/get](#/Assets/getAssetCheckoutsByQuery).

**Workflow Example**
1. Locate the asset record and confirm the active checkout.
2. [POST /api/v1.0/assets/checkouts/checkin](#/Assets/checkinAsset) with the `AssetId` and (optionally) `OwnerId` and `TicketId`.
3. Use the response transaction to update UI status or close related workflows.

**Minimal Required Fields**: `AssetId` (request body).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `AssetCheckinRequest` | `AssetCheckinRequest` | - |

#### Returns

- Typed call return: `AssetExchangeTransactionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetExchangeTransactionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `checkout_or_transfer_asset`

Provenance: Golden OpenAPI contract

Operation ID: `checkoutOrTransferAsset`

- Sync: `client.assets.checkout_or_transfer_asset(body=..., timeout=None)`
- Async: `await client.assets.checkout_or_transfer_asset(body=..., timeout=None)`
- Raw payload: `client.assets.checkout_or_transfer_asset.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/checkouts/checkout-or-transfer`
- Source controller: `IncidentIQ API`

Checkout or transfer asset

Checks out or transfers an asset to a new owner and returns the paired checkout/check-in exchange transactions when applicable. Use this for issuing devices to users, transferring assignments between users, or recording loaner activity.

**Prerequisites**
1. **AssetId** - Locate the device via [POST /api/v1.0/assets/search](#/Assets/keywordSearchAssets) and capture `Items[].AssetId`.
2. **OwnerId** - Identify the assignee via [POST /api/v1.0/search](#/Users/searchUsers) and capture `Item.Users[].UserId`.
3. (Optional) Validate existing checkouts using [POST /api/v1.0/assets/checkouts/query/get](#/Assets/getAssetCheckoutsByQuery).

**Workflow Example**
1. Identify the asset and the recipient user.
2. [POST /api/v1.0/assets/checkouts/checkout-or-transfer](#/Assets/checkoutOrTransferAsset) with the `AssetId`, `OwnerId`, and optional `DueDate`.
3. Use the returned exchange transactions for audit or receipt data.

**Minimal Required Fields**: `AssetId` (request body) and `OwnerId` when assigning to a user.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `AssetCheckoutRequest` | `AssetCheckoutRequest` | - |

#### Returns

- Typed call return: `AssetExchangeTransactionListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetExchangeTransactionListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `count_assets`

Provenance: Golden OpenAPI contract

Operation ID: `countAssets`

- Sync: `client.assets.count_assets(body=..., timeout=None)`
- Async: `await client.assets.count_assets(body=..., timeout=None)`
- Raw payload: `client.assets.count_assets.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/count`
- Source controller: `IncidentIQ API`

Count assets

Returns the total number of assets that match a saved view or ad-hoc filter set without returning the asset rows. The `Paging.TotalRows` field in the response contains the authoritative count.

**Prerequisites**
1. **SiteId/ProductId headers** – Call [GET /api/v1.0/sites/{siteUrl}](#/Sites/getSiteByUrl) to obtain `Item.SiteId`, the active `ProductId`, and the assets entity type id (`Item.Settings.EntityTypes.Assets`). Send these header values with each request.
2. **Filter catalog** – Use [GET /api/v1.0/filters/for/entitytype/{entityTypeId}](#/Filters/listFiltersForEntityType) with the assets entity type id to inspect available facets (asset type, status, location, custom fields, saved views, etc.) and capture each facet's `FilterSetId`.
3. **Filter values** – For each facet, call [GET /api/v1.0/filters/sets/{filterId}/values](#/Filters/getFilterSet) or the dedicated catalog endpoint (for example, [GET /api/v1.0/assets/types](#/Assets/listAssetTypes) or [GET /api/v2.0/locations/view](#/Locations/getMyLocationsViewV2)) to collect the GUIDs that should be passed in `Filters[].Id`.

**Workflow Example**
1. Bootstrap the site: [GET /api/v1.0/sites/{siteUrl}](#/Sites/getSiteByUrl) → read `Item.SiteId`, `Item.LicensedProducts[].ProductId`, and `Item.Settings.EntityTypes.Assets`.
2. Retrieve filter definitions: [GET /api/v1.0/filters/for/entitytype/{assetsEntityTypeId}](#/Filters/listFiltersForEntityType) → note the `FilterSetId` for `assettype`, `status`, and `location` facets.
3. Resolve the exact values you need by reading the appropriate catalog (for example, list asset types or locations) and build the filter payload. Set `Schema` to `All` for the default asset grid or to the schema identifier returned by a saved asset view (for example, `Assets.CustomView`).
4. [POST /api/v1.0/assets/count](#/Assets/countAssets) with the constructed request body and read `Paging.TotalRows` to drive dashboards, rule previews, or navigation badges.

**Minimal Required Fields**: `Schema` (defaults to `All` when not targeting a saved view) and any filters needed for the business scenario. The `Filters` array may be omitted to count the entire inventory.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `AssetSearchRequest` | `AssetSearchRequest` | - |

#### Returns

- Typed call return: `AssetCountResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetCountResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_asset`

Provenance: Golden OpenAPI contract

Operation ID: `createAsset`

- Sync: `client.assets.create_asset(body=None, timeout=None)`
- Async: `await client.assets.create_asset(body=None, timeout=None)`
- Raw payload: `client.assets.create_asset.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/assets/new`
- Source controller: `IncidentIQ API`

Create a new asset

Creates a new asset in the system using the full `AssetUpdateRequest` payload (the same model used for updates). The server initializes the asset record and returns the created asset with its assigned ID and system-generated fields.

**Prerequisites**
1. **AssetTypeId** - Use [GET /api/v1.0/assets/types](#/Assets/listAssetTypes) and extract `Items[].AssetTypeId`.
2. **StatusTypeId** - Use [GET /api/v1.0/assets/status/types](#/Assets/listAssetStatusTypes) and extract `Items[].AssetStatusTypeId`.
3. **ModelId** - Use [POST /api/v1.0/models](#/Models/searchModels) and extract `Items[].ModelId`.
4. **LocationId** - Use [GET /api/v2.0/locations](#/Locations/getMyLocationsV2) and extract `Items[].LocationId`.
5. **AssetTag** (optional) - Use [GET /api/v1.0/assets/generate-asset-tag](#/Assets/generateAssetTag) to reserve a new tag.

**Workflow Example**
1. Gather catalog IDs for asset type, status, model, and location from the endpoints above.
2. (Optional) Generate a new asset tag.
3. Call [POST /api/v1.0/assets/new](#/Assets/createAsset) with `AssetTag`, `AssetTypeId`, `StatusTypeId`, `ModelId`, `LocationId`, and any additional asset fields you want to set.

**Minimal Required Fields**: Requirements are tenant-configured. Common required fields include `AssetTag`, `AssetTypeId`, `StatusTypeId`, `ModelId`, and `LocationId`.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `AssetUpdateRequest` | `AssetUpdateRequest` | - |

#### Returns

- Typed call return: `AssetCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_asset_type`

Provenance: Golden OpenAPI contract

Operation ID: `createAssetType`

- Sync: `client.assets.create_asset_type(body=..., timeout=None)`
- Async: `await client.assets.create_asset_type(body=..., timeout=None)`
- Raw payload: `client.assets.create_asset_type.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/types/new`
- Source controller: `IncidentIQ API`

Create Asset Type

Registers a new asset type to categorize devices and control available fields. Asset types define inventory categorization such as Devices, Peripherals, or Network Equipment.

**Prerequisites**
1. **AssetInventoryTypeId** - Use [GET /api/v1.0/assets/inventory/types](#/Assets/listAssetInventoryTypes) if available, or reference existing asset types from [GET /api/v1.0/assets/types](#/Assets/listAssetTypes).

**Workflow Example**
1. Review existing types: [GET /api/v1.0/assets/types](#/Assets/listAssetTypes) to check for duplicates.
2. Build request with Name, Scope (Global/Site), and field configuration.
3. Submit [POST /api/v1.0/assets/types/new](#/Assets/createAssetType) to register the new category.

**Minimal Required Fields**: Name, AssetInventoryTypeId

**Field Configuration**: Set `IsModelFieldSupported: true` to enable model selection, `IsAssetNameFieldSupported: true` for custom naming.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `UpdateAssetTypeRequest` | `UpdateAssetTypeRequest` | - |

#### Returns

- Typed call return: `AssetTypeCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetTypeCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_asset_verification`

Provenance: Golden OpenAPI contract

Operation ID: `createAssetVerification`

- Sync: `client.assets.create_asset_verification(asset_id=..., body=..., timeout=None)`
- Async: `await client.assets.create_asset_verification(asset_id=..., body=..., timeout=None)`
- Raw payload: `client.assets.create_asset_verification.raw(asset_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/{assetId}/verifications/new`
- Source controller: `IncidentIQ API`

Verify asset

Records a manual verification for a device from the agent workspace, confirming the asset is present at the expected location and assigned to the correct user.

**Prerequisites**
1. **assetId** - Retrieve the ticket you are working via [GET /api/v1.0/tickets/{ticketId}](#/Tickets/getTicket) and read `Item.Asset.AssetId`, or search the catalog with [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById).
2. **VerifiedByUserId** - Look up the agent performing the verification using [POST /api/v1.0/search](#/Search/globalSearch) and extract `Item.Users[].UserId`.
3. **LocationId** - Load campus options with [GET /api/v2.0/locations/view](#/Locations/getMyLocationsViewV2) to confirm the device's physical location.

**Workflow Example**
1. Identify pending actions: [GET /api/v1.0/tickets/{ticketId}/next-steps](#/Tickets/getTicketNextSteps) and find the recommendation with subject "Verify Asset" and record `TicketNextStepId`.
2. Inspect the device: [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById) to confirm owner, model, and current location details displayed in the modal.
3. Submit verification: [POST /api/v1.0/assets/{assetId}/verifications/new](#/Assets/createAssetVerification) with `AssetVerificationTypeId: "web-manual"`, the agent's `VerifiedBy` profile, the confirmed `LocationId`, and `IsSuccessful: true` when the check passes.
4. Close the workflow step: [POST /api/v1.0/tickets/{ticketId}/next-steps/{ticketNextStepId}/resolve](#/Tickets/resolveTicketNextStep) to mark the recommendation complete.

**Minimal Required Fields**: AssetVerificationTypeId, VerifiedBy, VerifiedByUserId, LocationId, IsSuccessful.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_id` | `assetId` | `path` | `yes` | `str` | `-` | UUID of the asset being verified. Obtain via [POST /api/v1.0/assets](#/Assets/searchAssets), extract `Items[].AssetId` from response. |
| `body` | `body` | `body` | `yes` | `AssetVerificationCreateRequest` | `AssetVerificationCreateRequest` | - |

#### Returns

- Typed call return: `AssetVerificationCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetVerificationCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_asset_view`

Provenance: Golden OpenAPI contract

Operation ID: `createAssetView`

- Sync: `client.assets.create_asset_view(body=..., timeout=None)`
- Async: `await client.assets.create_asset_view(body=..., timeout=None)`
- Raw payload: `client.assets.create_asset_view.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/views/new`
- Source controller: `IncidentIQ API`

Create asset view

Creates a new asset view definition for the current site and user. The view definition describes filters, columns, sort order, and layout metadata used by asset grids.

**Prerequisites**
1. **UserId** - Use [POST /api/v1.0/search](#/Users/searchUsers) to locate the owner and extract `Item.Users[].UserId`.
2. **Template (optional)** - Use [GET /api/v1.0/assets/views](#/Assets/listAssetViews) to copy a similar view's `ViewTypeId`, `ProductId`, or column layout.

**Workflow Example**
1. (Optional) List existing views to find a template: [GET /api/v1.0/assets/views](#/Assets/listAssetViews).
2. Build a `ViewDefinition` payload with `Name`, `ViewTypeId`, `SiteId`, `ProductId`, and `UserId`.
3. Create the view: [POST /api/v1.0/assets/views/new](#/Assets/createAssetView).

**Minimal Required Fields**: `Name`, `ViewTypeId`, `SiteId`, `ProductId`, `UserId`.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `ViewDefinition` | `ViewDefinition` | - |

#### Returns

- Typed call return: `ViewItemCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ViewItemCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_manufacturer`

Provenance: Golden OpenAPI contract

Operation ID: `createManufacturer`

- Sync: `client.assets.create_manufacturer(body=..., timeout=None)`
- Async: `await client.assets.create_manufacturer(body=..., timeout=None)`
- Raw payload: `client.assets.create_manufacturer.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/manufacturers/new`
- Source controller: `IncidentIQ API`

Create manufacturer

Creates a new manufacturer in the system. Manufacturers represent hardware vendors (e.g., Dell, HP, Lenovo) that produce asset models.

**Scope Options**
- `Scope: "Global"` - Manufacturer is available across all sites (requires elevated permissions)
- `Scope: "Site"` - Manufacturer is only available at the current site

**Workflow Example**
1. Create manufacturer: [POST /api/v1.0/assets/manufacturers/new](#/Manufacturers/createManufacturer) with `Name` and `Scope`
2. Extract `Item.ManufacturerId` from response
3. Create models under this manufacturer using [POST /api/v1.0/assets/models/new](#/Assets/createAssetType)

**Duplicate Handling**
Set `IsDuplicateRequest: true` if intentionally creating a manufacturer with a name that already exists. Otherwise, the API may reject duplicates.

**Minimal Required Fields**: `Name`

**Optional Fields**: `Scope` (defaults to Site), `EsoIsVisible` (controls ESO portal visibility), `Icon` (Font Awesome class)

**Related Endpoints**
- [GET /api/v1.0/assets/manufacturers](#/Manufacturers/getManufacturers) - List existing manufacturers
- [POST /api/v1.0/assets/manufacturers/{ManufacturerId}](#/Manufacturers/updateManufacturer) - Update manufacturer details

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `UpdateManufacturerRequest` | `UpdateManufacturerRequest` | Manufacturer data for creation |

#### Returns

- Typed call return: `Any`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_my_classes_asset_verification`

Provenance: Golden OpenAPI contract

Operation ID: `createMyClassesAssetVerification`

- Sync: `client.assets.create_my_classes_asset_verification(asset_id=..., body=..., timeout=None)`
- Async: `await client.assets.create_my_classes_asset_verification(asset_id=..., body=..., timeout=None)`
- Raw payload: `client.assets.create_my_classes_asset_verification.raw(asset_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/{assetId}/my-classes/verifications/new`
- Source controller: `IncidentIQ API`

Create My Classes verification

Records a verification for an asset within the My Classes context. This variant applies My Classes-specific business rules and permissions.

**Prerequisites**
1. **assetId** - Asset to verify within My Classes workflow.

**Workflow Example**
1. Teacher opens My Classes device roster.
2. Verifies student device is present.
3. [POST /api/v1.0/assets/{assetId}/my-classes/verifications/new](#/Assets/createMyClassesAssetVerification).

**Minimal Required Fields**: `assetId` (path), AssetVerificationTypeId, VerifiedByUserId, LocationId, IsSuccessful.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_id` | `assetId` | `path` | `yes` | `str` | `-` | UUID of the asset to verify. Obtain via [POST /api/v1.0/assets](#/Assets/searchAssets), extract `Items[].AssetId` from response. |
| `body` | `body` | `body` | `yes` | `UpdateAssetVerificationRequest` | `UpdateAssetVerificationRequest` | - |

#### Returns

- Typed call return: `AssetVerificationCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetVerificationCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_asset`

Provenance: Golden OpenAPI contract

Operation ID: `deleteAsset`

- Sync: `client.assets.delete_asset(asset_id=..., timeout=None)`
- Async: `await client.assets.delete_asset(asset_id=..., timeout=None)`
- Raw payload: `client.assets.delete_asset.raw(asset_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/assets/{assetId}`
- Source controller: `IncidentIQ API`

Delete asset

Permanently removes an asset record from the system. This is a destructive operation and cannot be undone. The asset will be marked as deleted and will no longer appear in standard asset queries.

**Prerequisites**
1. **assetId** - Locate the device via [POST /api/v1.0/assets](#/Assets/searchAssets) or [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById) and capture `Items[].AssetId`.

**Workflow Example**
1. Search for the asset: [POST /api/v1.0/assets](#/Assets/searchAssets) to capture `Items[].AssetId`.
2. Verify the asset details: [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById) to confirm this is the correct record.
3. Delete the asset: [DELETE /api/v1.0/assets/{assetId}](#/Assets/deleteAsset).

**Note**: To restore a deleted asset, use [PUT /api/v1.0/assets/{assetId}/undelete](#/Assets/undeleteAsset).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_id` | `assetId` | `path` | `yes` | `str` | `-` | UUID of the asset to delete. Obtain from [POST /api/v1.0/assets](#/Assets/searchAssets) (`Items[].AssetId`) or [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById). |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_asset_checkout`

Provenance: Golden OpenAPI contract

Operation ID: `deleteAssetCheckout`

- Sync: `client.assets.delete_asset_checkout(asset_checkout_id=..., timeout=None)`
- Async: `await client.assets.delete_asset_checkout(asset_checkout_id=..., timeout=None)`
- Raw payload: `client.assets.delete_asset_checkout.raw(asset_checkout_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/assets/checkouts/{assetCheckoutId}/delete`
- Source controller: `IncidentIQ API`

Delete checkout

Deletes a checkout record by identifier. Use this to remove erroneous or duplicate checkout entries when no historical audit is needed, or as part of a cleanup workflow after corrective action.

**Prerequisites**
1. **assetCheckoutId** - Obtain via [POST /api/v1.0/assets/checkouts/query/get](#/Assets/getAssetCheckoutsByQuery) when filtering by asset, owner, or status.

**Workflow Example**
1. Query for the checkout to remove: [POST /api/v1.0/assets/checkouts/query/get](#/Assets/getAssetCheckoutsByQuery) -> capture `AssetCheckoutId`.
2. [DELETE /api/v1.0/assets/checkouts/{assetCheckoutId}/delete](#/Assets/deleteAssetCheckout) to remove the record.

**Minimal Required Fields**: `assetCheckoutId` (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_checkout_id` | `assetCheckoutId` | `path` | `yes` | `str` | `-` | UUID of the checkout record to delete. |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_asset_checkouts_by_ids`

Provenance: Golden OpenAPI contract

Operation ID: `deleteAssetCheckoutsByIds`

- Sync: `client.assets.delete_asset_checkouts_by_ids(body=..., timeout=None)`
- Async: `await client.assets.delete_asset_checkouts_by_ids(body=..., timeout=None)`
- Raw payload: `client.assets.delete_asset_checkouts_by_ids.raw(body=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/assets/checkouts/ids/delete`
- Source controller: `IncidentIQ API`

Delete checkouts by IDs

Deletes specific checkout records by identifier list. Use this when you have a known set of checkout IDs to remove without impacting other records.

**Prerequisites**
1. **AssetCheckoutIds** - Collect from [POST /api/v1.0/assets/checkouts/query/get](#/Assets/getAssetCheckoutsByQuery) or [POST /api/v1.0/assets/checkouts/transactions/query/get](#/Assets/getAssetCheckoutTransactions).

**Workflow Example**
1. Gather the checkout IDs that should be removed.
2. [DELETE /api/v1.0/assets/checkouts/ids/delete](#/Assets/deleteAssetCheckoutsByIds) with the array of IDs.

**Minimal Required Fields**: request body array of checkout IDs.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `UuidList` | `UuidList` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_asset_checkouts_by_query`

Provenance: Golden OpenAPI contract

Operation ID: `deleteAssetCheckoutsByQuery`

- Sync: `client.assets.delete_asset_checkouts_by_query(body=None, timeout=None)`
- Async: `await client.assets.delete_asset_checkouts_by_query(body=None, timeout=None)`
- Raw payload: `client.assets.delete_asset_checkouts_by_query.raw(body=None, timeout=None)`
- HTTP route: `DELETE /api/v1.0/assets/checkouts/query/delete`
- Source controller: `IncidentIQ API`

Delete checkouts by query

Deletes checkout records matching the supplied filters. Use this for bulk cleanup (for example, remove all checkouts for a retired asset type) after verifying the target set with a query preview.

**Prerequisites**
1. Use [POST /api/v1.0/assets/checkouts/query/get](#/Assets/getAssetCheckoutsByQuery) to preview which checkout records match your filters.

**Workflow Example**
1. Preview target checkouts with [POST /api/v1.0/assets/checkouts/query/get](#/Assets/getAssetCheckoutsByQuery).
2. [DELETE /api/v1.0/assets/checkouts/query/delete](#/Assets/deleteAssetCheckoutsByQuery) with the same filters to remove the records.

**Minimal Required Fields**: none; include filters in the request body to scope the deletion.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `GetAssetCheckoutsRequest` | `GetAssetCheckoutsRequest` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_asset_file`

Provenance: Golden OpenAPI contract

Operation ID: `deleteAssetFile`

- Sync: `client.assets.delete_asset_file(asset_id=..., file_id=..., timeout=None)`
- Async: `await client.assets.delete_asset_file(asset_id=..., file_id=..., timeout=None)`
- Raw payload: `client.assets.delete_asset_file.raw(asset_id=..., file_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/assets/{assetId}/files/{fileId}`
- Source controller: `IncidentIQ API`

Delete asset file

Removes a file attachment from an asset so it no longer appears in the asset file list. Use this to clean up outdated receipts, incorrect uploads, or obsolete documentation.

**Prerequisites**
1. **assetId** - Locate the asset via [POST /api/v1.0/assets/search](#/Assets/keywordSearchAssets) or [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById).
2. **fileId** - Call [GET /api/v1.0/assets/{assetId}/files](#/Assets/getAssetFiles) and capture the target `FileId`.

**Workflow Example**
1. List current files: [GET /api/v1.0/assets/{assetId}/files](#/Assets/getAssetFiles) -> capture `FileId`.
2. [DELETE /api/v1.0/assets/{assetId}/files/{fileId}](#/Assets/deleteAssetFile) to remove the attachment.

**Minimal Required Fields**: `assetId`, `fileId` (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_id` | `assetId` | `path` | `yes` | `str` | `-` | UUID of the asset. Obtain via [POST /api/v1.0/assets](#/Assets/searchAssets), extract `Items[].AssetId` from response. |
| `file_id` | `fileId` | `path` | `yes` | `str` | `-` | UUID of the file to remove. Obtain via [GET /api/v1.0/assets/{assetId}/files](#/Assets/getAssetFiles), extract `Items[].FileId` from response. |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_asset_view`

Provenance: Golden OpenAPI contract

Operation ID: `deleteAssetView`

- Sync: `client.assets.delete_asset_view(view_id=..., timeout=None)`
- Async: `await client.assets.delete_asset_view(view_id=..., timeout=None)`
- Raw payload: `client.assets.delete_asset_view.raw(view_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/assets/views/{viewId}`
- Source controller: `IncidentIQ API`

Delete asset view

Deletes a saved asset view so it no longer appears in user view selectors or list endpoints. Use this to clean up deprecated or duplicate views.

**Prerequisites**
1. **viewId** - Obtain from [GET /api/v1.0/assets/views](#/Assets/listAssetViews) before deleting.

**Workflow Example**
1. List views: [GET /api/v1.0/assets/views](#/Assets/listAssetViews) -> identify the view to remove.
2. Delete the view: [DELETE /api/v1.0/assets/views/{viewId}](#/Assets/deleteAssetView).

**Minimal Required Fields**: `viewId` (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `view_id` | `viewId` | `path` | `yes` | `str` | `-` | Identifier of the asset view to delete. |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_linked_assets`

Provenance: Golden OpenAPI contract

Operation ID: `deleteLinkedAssets`

- Sync: `client.assets.delete_linked_assets(asset_id=..., body=..., timeout=None)`
- Async: `await client.assets.delete_linked_assets(asset_id=..., body=..., timeout=None)`
- Raw payload: `client.assets.delete_linked_assets.raw(asset_id=..., body=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/assets/linked/to/{assetId}`
- Source controller: `IncidentIQ API`

Unlink assets from parent

Removes parent-child relationships between assets so accessories or components are no longer linked to a parent device. Use this when retiring peripherals, reassigning accessories, or correcting an incorrect relationship.

**Prerequisites**
1. **assetId** - Identify the parent asset via [POST /api/v1.0/assets/search](#/Assets/keywordSearchAssets).
2. **Child relationships** - Use [GET /api/v1.0/assets/linked/to/{assetId}](#/Assets/getLinkedAssets) to capture the linked asset IDs.

**Workflow Example**
1. Load the parent asset and list linked assets.
2. [DELETE /api/v1.0/assets/linked/to/{assetId}](#/Assets/deleteLinkedAssets) with a `LinkedAssetListRequest` payload to remove the relationships.

**Minimal Required Fields**: `assetId` (path) and child asset IDs in the request body.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_id` | `assetId` | `path` | `yes` | `str` | `-` | UUID of the parent asset. Obtain via [POST /api/v1.0/assets](#/Assets/searchAssets), extract `Items[].AssetId` from response. |
| `body` | `body` | `body` | `yes` | `LinkedAssetListRequest` | `LinkedAssetListRequest` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_manufacturer`

Provenance: Golden OpenAPI contract

Operation ID: `deleteManufacturer`

- Sync: `client.assets.delete_manufacturer(manufacturer_id=..., timeout=None)`
- Async: `await client.assets.delete_manufacturer(manufacturer_id=..., timeout=None)`
- Raw payload: `client.assets.delete_manufacturer.raw(manufacturer_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/assets/manufacturers/{ManufacturerId}`
- Source controller: `IncidentIQ API`

Delete manufacturer

Permanently deletes a manufacturer from the system. This operation will fail if the manufacturer has associated asset models.

**Prerequisites**
- **ManufacturerId** - Use [GET /api/v1.0/assets/manufacturers](#/Manufacturers/getManufacturers) to find the manufacturer. Extract `Items[].ManufacturerId`.

**Workflow Example**
1. List manufacturers: [GET /api/v1.0/assets/manufacturers](#/Manufacturers/getManufacturers) → identify target
2. Verify no models exist: Check that manufacturer has no associated models
3. Delete: [DELETE /api/v1.0/assets/manufacturers/{ManufacturerId}](#/Manufacturers/deleteManufacturer)

**Deletion Constraints**
- Cannot delete manufacturers with existing asset models - delete or reassign models first
- Cannot delete manufacturers referenced by existing assets
- For bulk deletion, use [POST /api/v1.0/manufacturers/bulk/delete](#/Manufacturers/bulkDeleteManufacturers)

**Error Responses**
- `404` - Manufacturer not found
- `409` - Manufacturer is in use and cannot be deleted

**Alternative: Site Removal**
To remove a manufacturer from a site without deleting it globally, use [DELETE /api/v1.0/assets/manufacturers/{ManufacturerId}/site](#/Manufacturers/removeManufacturerFromSite) instead.

**Related Endpoints**
- [POST /api/v1.0/manufacturers/bulk/delete](#/Manufacturers/bulkDeleteManufacturers) - Delete multiple manufacturers
- [DELETE /api/v1.0/assets/manufacturers/{ManufacturerId}/site](#/Manufacturers/removeManufacturerFromSite) - Remove from site only

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `manufacturer_id` | `ManufacturerId` | `path` | `yes` | `str` | `-` | Unique identifier of the manufacturer to delete |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `exchange_asset`

Provenance: Golden OpenAPI contract

Operation ID: `exchangeAsset`

- Sync: `client.assets.exchange_asset(body=..., timeout=None)`
- Async: `await client.assets.exchange_asset(body=..., timeout=None)`
- Raw payload: `client.assets.exchange_asset.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/exchange`
- Source controller: `IncidentIQ API`

Exchange asset

Exchanges an asset between users and optionally transfers ownership from one asset to another. Use this for device swap scenarios, loaner exchanges, or consolidating user assignments during refresh cycles.

**Prerequisites**
1. **OwnerId** - Identify the target owner via [POST /api/v1.0/search](#/Users/searchUsers).
2. **FromAssetId / ToAssetId** - Locate the assets via [POST /api/v1.0/assets/search](#/Assets/keywordSearchAssets) and capture `Items[].AssetId`.

**Workflow Example**
1. Identify the outgoing and incoming assets and the receiving user.
2. [POST /api/v1.0/assets/exchange](#/Assets/exchangeAsset) with the `OwnerId` and `FromAssetId`/`ToAssetId` values.
3. Review the action response to confirm the swap completed.

**Minimal Required Fields**: include at least one asset reference (`FromAssetId` or `ToAssetId`) and the `OwnerId` when assigning the device to a user.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `AssetExchangeRequest` | `AssetExchangeRequest` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `export_assets_by_type`

Provenance: Golden OpenAPI contract

Operation ID: `exportAssetsByType`

- Sync: `client.assets.export_assets_by_type(asset_type_id=..., p=None, s=None, o=None, timeout=None)`
- Async: `await client.assets.export_assets_by_type(asset_type_id=..., p=None, s=None, o=None, timeout=None)`
- Raw payload: `client.assets.export_assets_by_type.raw(asset_type_id=..., p=None, s=None, o=None, timeout=None)`
- HTTP route: `GET /api/v1.0/assets/export/{assetTypeId}`
- Source controller: `IncidentIQ API`

Export assets by type

Exports assets of a specific type for bulk data extraction. Supports pagination and filtering for large datasets.

**Prerequisites**
1. **AssetTypeId** - Use [GET /api/v1.0/assets/types](#/Assets/listAssetTypes) to get asset type UUIDs from `Items[].AssetTypeId`.

**Workflow Example**
1. Get asset types: [GET /api/v1.0/assets/types](#/Assets/listAssetTypes) and identify target category.
2. Call [GET /api/v1.0/assets/export/{assetTypeId}](#/Assets/exportAssetsByType) with pagination params.
3. Iterate pages until `Items.length < $s` to export complete dataset.

**Common Use Cases**
- Export Chromebooks for MDM reconciliation
- Bulk data extraction for warehouse systems
- Asset inventory audits by category

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_type_id` | `assetTypeId` | `path` | `yes` | `str` | `-` | UUID of the asset type to export |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index |
| `s` | `$s` | `query` | `no` | `int` | `-` | Page size (default 100) |
| `o` | `$o` | `query` | `no` | `Any` | `-` | Sort expression: field name followed by optional direction (e.g., `AssetTag desc`). Direction can be `asc`, `ascending`, `desc`, or `descending`. Default direction is ascending. See [AssetSortField](#/components/schemas/AssetSortField) for valid field names. |

#### Returns

- Typed call return: `AssetSearchResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetSearchResponse`
- Pagination helper: `client.assets.export_assets_by_type.iter_pages(start_page=1, page_size=100, max_pages=None, asset_type_id=..., p=None, s=None, o=None, timeout=None)`

---

### `generate_asset_tag`

Provenance: Golden OpenAPI contract

Operation ID: `generateAssetTag`

- Sync: `client.assets.generate_asset_tag(timeout=None)`
- Async: `await client.assets.generate_asset_tag(timeout=None)`
- Raw payload: `client.assets.generate_asset_tag.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/assets/generate-asset-tag`
- Source controller: `IncidentIQ API`

Generate asset tag

Generates a new unique asset tag using the tenant's configured auto-generation pattern. Returns the generated tag string and its sequence index.

**Workflow Example**
1. Call [GET /api/v1.0/assets/generate-asset-tag](#/Assets/generateAssetTag) to reserve a new tag.
2. Extract `Item.AssetTag` from the response.
3. Use the tag when creating an asset via [POST /api/v1.0/assets/new](#/Assets/createAsset).

**Common Use Cases**
- Pre-generate tags for batch asset imports
- Reserve tag sequences before labeling devices
- Maintain sequential numbering during bulk deployments

**Notes**: Tag pattern is configured at the tenant level. Contact administrator to customize the prefix or format.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `NewAssetTagResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `NewAssetTagResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_aggregated_asset_cost_values`

Provenance: Golden OpenAPI contract

Operation ID: `getAggregatedAssetCostValues`

- Sync: `client.assets.get_aggregated_asset_cost_values(force_refresh=None, body=..., timeout=None)`
- Async: `await client.assets.get_aggregated_asset_cost_values(force_refresh=None, body=..., timeout=None)`
- Raw payload: `client.assets.get_aggregated_asset_cost_values.raw(force_refresh=None, body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/aggregate-cost-values`
- Source controller: `IncidentIQ API`

Get aggregated asset cost values

Calculates aggregate cost values (purchase price, replacement cost, current value, total cost to date) for a filtered set of assets. Useful for financial reporting.

**Use Cases:**
- Calculate total asset value by location
- Generate budget reports by asset type
- Track depreciation across asset portfolios

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `force_refresh` | `forceRefresh` | `query` | `no` | `bool` | `-` | Force recalculation instead of using cached values |
| `body` | `body` | `body` | `yes` | `AssetSearchRequest` | `AssetSearchRequest` | - |

#### Returns

- Typed call return: `AssetAggregationCacheEntryResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetAggregationCacheEntryResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_activities`

Provenance: Golden OpenAPI contract

Operation ID: `getAssetActivities`

- Sync: `client.assets.get_asset_activities(asset_id=..., p=None, s=None, timeout=None)`
- Async: `await client.assets.get_asset_activities(asset_id=..., p=None, s=None, timeout=None)`
- Raw payload: `client.assets.get_asset_activities.raw(asset_id=..., p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v1.0/assets/{assetId}/activities`
- Source controller: `IncidentIQ API`

Get asset activity timeline

Returns the chronological activity log for an asset, including creation events, automation rule updates, custom field changes, and manual adjustments recorded in the asset workspace.

**Prerequisites**
1. **assetId** - Use [POST /api/v1.0/assets](#/Assets/searchAssets) to locate the device and read `Items[].AssetId` from the returned list.
2. **Context (optional)** - Call [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById) to confirm the current owner, model, or location before auditing activity history.

**Workflow Example**
1. Search for the device: [POST /api/v1.0/assets](#/Assets/searchAssets) with tag, serial, owner, or location filters to capture `Items[].AssetId`.
2. (Optional) Inspect the profile: [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById) to validate the active assignment and status.
3. Render the change history: [GET /api/v1.0/assets/{assetId}/activities](#/Assets/getAssetActivities) to display the timeline used on the asset detail card or for auditing past updates.

**Minimal Required Fields**: `assetId`

Supports pagination via optional `$p` (page index) and `$s` (page size) query parameters.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_id` | `assetId` | `path` | `yes` | `str` | `-` | UUID of the asset whose activity timeline should be retrieved. Obtain by searching assets (`Items[].AssetId`) or reusing a previously captured identifier. |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index for paginating asset activities. |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of activity records returned per page. |

#### Returns

- Typed call return: `AssetActivityTimelineResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetActivityTimelineResponse`
- Pagination helper: `client.assets.get_asset_activities.iter_pages(start_page=1, page_size=100, max_pages=None, asset_id=..., p=None, s=None, timeout=None)`

---

### `get_asset_by_id`

Provenance: Golden OpenAPI contract

Operation ID: `getAssetById`

- Sync: `client.assets.get_asset_by_id(asset_id=..., load_valuation_data=None, load_total_cost_data=None, timeout=None)`
- Async: `await client.assets.get_asset_by_id(asset_id=..., load_valuation_data=None, load_total_cost_data=None, timeout=None)`
- Raw payload: `client.assets.get_asset_by_id.raw(asset_id=..., load_valuation_data=None, load_total_cost_data=None, timeout=None)`
- HTTP route: `GET /api/v1.0/assets/{assetId}`
- Source controller: `IncidentIQ API`

Get asset by ID

Retrieves complete details for a specific asset by its UUID. Returns all asset properties including custom fields, location, owner, status, model information, and linked assets.

**Prerequisites**
1. **AssetId** - Obtain via [POST /api/v1.0/assets](#/Assets/searchAssets) and extract `Items[].AssetId`, or from [GET /api/v1.0/assets/assettag/{assetTag}](#/Assets/getAssetByTag).

**Workflow Example**
1. Search for asset: [POST /api/v1.0/assets](#/Assets/searchAssets) with filters.
2. Extract target `AssetId` from search results.
3. Call [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById) for full details.

**Response Includes**: AssetTag, SerialNumber, Model, Location, Owner, Status, CustomFields, PurchaseInfo, and linked assets.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_id` | `assetId` | `path` | `yes` | `str` | `-` | UUID of the asset to retrieve. Obtain via [POST /api/v1.0/assets](#/Assets/searchAssets), extract `Items[].AssetId` from response. |
| `load_valuation_data` | `loadValuationData` | `query` | `no` | `bool` | `-` | When true, includes valuation data in the asset response. |
| `load_total_cost_data` | `loadTotalCostData` | `query` | `no` | `bool` | `-` | When true, includes total cost data in the asset response. |

#### Returns

- Typed call return: `AssetItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_by_serial`

Provenance: Golden OpenAPI contract

Operation ID: `getAssetBySerial`

- Sync: `client.assets.get_asset_by_serial(serial=..., timeout=None)`
- Async: `await client.assets.get_asset_by_serial(serial=..., timeout=None)`
- Raw payload: `client.assets.get_asset_by_serial.raw(serial=..., timeout=None)`
- HTTP route: `GET /api/v1.0/assets/serial/{serial}`
- Source controller: `IncidentIQ API`

Get asset by serial number

Retrieves a specific asset by its exact serial number. Returns complete asset details including custom fields, location, owner, and status information.

**Prerequisites**
1. **Serial Number** - Obtain from device system info, manufacturer label, MDM sync, or [POST /api/v1.0/assets](#/Assets/searchAssets) reading `Items[].SerialNumber`.

**Workflow Example**
1. Collect serial number from device BIOS, system settings, or manufacturer sticker.
2. Call [GET /api/v1.0/assets/serial/{serial}](#/Assets/getAssetBySerial) with the exact serial value.
3. Use returned `AssetId` for subsequent operations like assigning owners or updating status.

**Notes**: Serial matching is case-insensitive. For partial/wildcard searches, use [GET /api/v1.0/assets/serial/search/{serial}](#/Assets/searchAssetsBySerial) instead.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `serial` | `serial` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `AssetSearchResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetSearchResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_change`

Provenance: Golden OpenAPI contract

Operation ID: `getAssetChange`

- Sync: `client.assets.get_asset_change(asset_change_id=..., timeout=None)`
- Async: `await client.assets.get_asset_change(asset_change_id=..., timeout=None)`
- Raw payload: `client.assets.get_asset_change.raw(asset_change_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/assets/changes/{assetChangeId}`
- Source controller: `IncidentIQ API`

Get asset change detail

Retrieves the full audit entry for a specific asset change, including the field that changed, before/after values, who made the change, and when it occurred. Use this to investigate why a device record looks different from prior audits or to surface detailed history in an admin review screen.

**Prerequisites**
1. **assetChangeId** - Obtain from [POST /api/v1.0/assets/changes/query](#/Assets/queryAssetChanges) by filtering for the asset and reading `Items[].AssetChangeId`.

**Workflow Example**
1. Query recent changes: [POST /api/v1.0/assets/changes/query](#/Assets/queryAssetChanges) with filters for the asset -> capture `AssetChangeId`.
2. Load the change detail: [GET /api/v1.0/assets/changes/{assetChangeId}](#/Assets/getAssetChange) to review the audit payload.

**Minimal Required Fields**: `assetChangeId` (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_change_id` | `assetChangeId` | `path` | `yes` | `str` | `-` | UUID of the change record |

#### Returns

- Typed call return: `AssetChangeItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetChangeItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_change_post`

Provenance: Golden OpenAPI contract

Operation ID: `getAssetChangePost`

- Sync: `client.assets.get_asset_change_post(asset_change_id=..., body=None, timeout=None)`
- Async: `await client.assets.get_asset_change_post(asset_change_id=..., body=None, timeout=None)`
- Raw payload: `client.assets.get_asset_change_post.raw(asset_change_id=..., body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/assets/changes/{assetChangeId}`
- Source controller: `IncidentIQ API`

Get asset change detail (POST)

Retrieves details for a specific asset change audit log entry using POST method. This alternative to the GET method allows passing additional request options in the body.

**Prerequisites**
1. **assetChangeId** - Obtain from [POST /api/v1.0/assets/changes/query](#/Assets/queryAssetChanges) and read `Items[].AssetChangeId`.

**Workflow Example**
1. Query recent asset changes: [POST /api/v1.0/assets/changes/query](#/Assets/queryAssetChanges) -> capture `AssetChangeId` from results.
2. Retrieve specific change details: [POST /api/v1.0/assets/changes/{assetChangeId}](#/Assets/getAssetChangePost).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_change_id` | `assetChangeId` | `path` | `yes` | `str` | `-` | UUID of the change record to retrieve |
| `body` | `body` | `body` | `no` | `GetAssetChangesRequest` | `GetAssetChangesRequest` | Optional request options for controlling the response |

#### Returns

- Typed call return: `AssetChangeItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetChangeItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_checkout`

Provenance: Golden OpenAPI contract

Operation ID: `getAssetCheckout`

- Sync: `client.assets.get_asset_checkout(asset_checkout_id=..., timeout=None)`
- Async: `await client.assets.get_asset_checkout(asset_checkout_id=..., timeout=None)`
- Raw payload: `client.assets.get_asset_checkout.raw(asset_checkout_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/assets/checkouts/{assetCheckoutId}/get`
- Source controller: `IncidentIQ API`

Get asset checkout

Retrieves a specific asset checkout record by identifier so you can inspect due dates, quantities, owner assignments, and current status for a single checkout. This is the canonical way to load a checkout record after listing or filtering results.

**Prerequisites**
1. **assetCheckoutId** - Obtain via [POST /api/v1.0/assets/checkouts/query/get](#/Assets/getAssetCheckoutsByQuery) when filtering by asset, owner, or status.

**Workflow Example**
1. Filter checkouts: [POST /api/v1.0/assets/checkouts/query/get](#/Assets/getAssetCheckoutsByQuery) with asset or owner filters -> capture `AssetCheckoutId`.
2. Retrieve the record: [GET /api/v1.0/assets/checkouts/{assetCheckoutId}/get](#/Assets/getAssetCheckout) to display checkout details or validate before an update/delete.

**Minimal Required Fields**: `assetCheckoutId` (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_checkout_id` | `assetCheckoutId` | `path` | `yes` | `str` | `-` | UUID of the checkout record. |

#### Returns

- Typed call return: `AssetCheckoutItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetCheckoutItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_checkout_for_owner`

Provenance: Golden OpenAPI contract

Operation ID: `getAssetCheckoutForOwner`

- Sync: `client.assets.get_asset_checkout_for_owner(asset_id=..., owner_id=..., timeout=None)`
- Async: `await client.assets.get_asset_checkout_for_owner(asset_id=..., owner_id=..., timeout=None)`
- Raw payload: `client.assets.get_asset_checkout_for_owner.raw(asset_id=..., owner_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/assets/{assetId}/checkouts/owner/{ownerId}`
- Source controller: `IncidentIQ API`

Get checkout for asset owner

Retrieves the checkout record for a specific asset and owner pair. Use this to confirm whether a given user currently holds a device and to inspect due date or status details before a transfer or check-in.

**Prerequisites**
1. **assetId** - Locate the asset via [POST /api/v1.0/assets/search](#/Assets/keywordSearchAssets) or [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById).
2. **ownerId** - Identify the owner via [POST /api/v1.0/search](#/Users/searchUsers).

**Workflow Example**
1. Capture the target asset ID and owner ID.
2. [GET /api/v1.0/assets/{assetId}/checkouts/owner/{ownerId}](#/Assets/getAssetCheckoutForOwner) to retrieve the checkout record for that pairing.

**Minimal Required Fields**: `assetId`, `ownerId` (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_id` | `assetId` | `path` | `yes` | `str` | `-` | UUID of the asset. Obtain via [POST /api/v1.0/assets](#/Assets/searchAssets), extract `Items[].AssetId` from response. |
| `owner_id` | `ownerId` | `path` | `yes` | `str` | `-` | UUID of the owner. Obtain via [POST /api/v1.0/users](#/Users/searchUsers), extract `Items[].UserId` from response. |

#### Returns

- Typed call return: `AssetCheckoutItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetCheckoutItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_checkout_post`

Provenance: Golden OpenAPI contract

Operation ID: `getAssetCheckoutPost`

- Sync: `client.assets.get_asset_checkout_post(asset_checkout_id=..., timeout=None)`
- Async: `await client.assets.get_asset_checkout_post(asset_checkout_id=..., timeout=None)`
- Raw payload: `client.assets.get_asset_checkout_post.raw(asset_checkout_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/checkouts/{assetCheckoutId}/get`
- Source controller: `IncidentIQ API`

Get asset checkout (POST)

POST variant of the checkout lookup for clients that require POST semantics (for example, gateways that block GETs or when you want parity with POST-based workflows). Returns the same checkout record as the GET variant.

**Prerequisites**
1. **assetCheckoutId** - Obtain via [POST /api/v1.0/assets/checkouts/query/get](#/Assets/getAssetCheckoutsByQuery) when filtering by asset, owner, or status.

**Workflow Example**
1. Filter checkouts: [POST /api/v1.0/assets/checkouts/query/get](#/Assets/getAssetCheckoutsByQuery) -> capture `AssetCheckoutId`.
2. [POST /api/v1.0/assets/checkouts/{assetCheckoutId}/get](#/Assets/getAssetCheckoutPost) to load the checkout record.

**Minimal Required Fields**: `assetCheckoutId` (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_checkout_id` | `assetCheckoutId` | `path` | `yes` | `str` | `-` | UUID of the checkout record. |

#### Returns

- Typed call return: `AssetCheckoutItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetCheckoutItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_checkout_transactions`

Provenance: Golden OpenAPI contract

Operation ID: `getAssetCheckoutTransactions`

- Sync: `client.assets.get_asset_checkout_transactions(body=None, timeout=None)`
- Async: `await client.assets.get_asset_checkout_transactions(body=None, timeout=None)`
- Raw payload: `client.assets.get_asset_checkout_transactions.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/assets/checkouts/transactions/query/get`
- Source controller: `IncidentIQ API`

List asset checkout transactions

Returns transaction-level checkout and check-in events, including associated asset, user, and location details. Supports RequestOptions filters for date ranges and entities.

**Prerequisites**
- Use [POST /api/v1.0/assets/checkouts/query/get](#/Assets/getAssetCheckoutsByQuery) to identify checkout identifiers if you need to narrow by checkout records.

**Minimal Required Fields**: none; add filters for scope.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `GetAssetCheckoutsRequest` | `GetAssetCheckoutsRequest` | - |

#### Returns

- Typed call return: `AssetCheckoutTransactionListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetCheckoutTransactionListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_checkouts_by_ids`

Provenance: Golden OpenAPI contract

Operation ID: `getAssetCheckoutsByIds`

- Sync: `client.assets.get_asset_checkouts_by_ids(body=..., timeout=None)`
- Async: `await client.assets.get_asset_checkouts_by_ids(body=..., timeout=None)`
- Raw payload: `client.assets.get_asset_checkouts_by_ids.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/checkouts/ids/get`
- Source controller: `IncidentIQ API`

Get asset checkouts by IDs

Fetches checkout records by explicit identifiers. Use this when you already have checkout IDs from a query or transaction feed and want to hydrate the full checkout details in bulk.

**Prerequisites**
1. **AssetCheckoutIds** - Use [POST /api/v1.0/assets/checkouts/query/get](#/Assets/getAssetCheckoutsByQuery) or [POST /api/v1.0/assets/checkouts/transactions/query/get](#/Assets/getAssetCheckoutTransactions) to collect checkout IDs.

**Workflow Example**
1. Query for checkouts: [POST /api/v1.0/assets/checkouts/query/get](#/Assets/getAssetCheckoutsByQuery) -> capture `Items[].AssetCheckoutId`.
2. Retrieve full records: [POST /api/v1.0/assets/checkouts/ids/get](#/Assets/getAssetCheckoutsByIds) with the ID array.

**Minimal Required Fields**: request body array of checkout IDs.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `UuidList` | `UuidList` | - |

#### Returns

- Typed call return: `AssetCheckoutListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetCheckoutListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_checkouts_by_query`

Provenance: Golden OpenAPI contract

Operation ID: `getAssetCheckoutsByQuery`

- Sync: `client.assets.get_asset_checkouts_by_query(body=None, timeout=None)`
- Async: `await client.assets.get_asset_checkouts_by_query(body=None, timeout=None)`
- Raw payload: `client.assets.get_asset_checkouts_by_query.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/assets/checkouts/query/get`
- Source controller: `IncidentIQ API`

List asset checkouts

Queries checkout records using RequestOptions filters (supports custom filters) and optional product scoping.

**Prerequisites**
- Capture `AssetId` via [POST /api/v1.0/assets](#/Assets/searchAssets) when scoping to a specific device.
- Capture `OwnerId` via [POST /api/v1.0/search](#/Users/searchUsers) when filtering by user.

**Minimal Required Fields**: none; provide filters for meaningful results.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `GetAssetCheckoutsRequest` | `GetAssetCheckoutsRequest` | - |

#### Returns

- Typed call return: `AssetCheckoutListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetCheckoutListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_files`

Provenance: Golden OpenAPI contract

Operation ID: `getAssetFiles`

- Sync: `client.assets.get_asset_files(asset_id=..., timeout=None)`
- Async: `await client.assets.get_asset_files(asset_id=..., timeout=None)`
- Raw payload: `client.assets.get_asset_files.raw(asset_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/assets/{assetId}/files`
- Source controller: `IncidentIQ API`

Get asset files

Retrieves all files attached to an asset. Files can include documentation, images, receipts, warranty documents, etc.

**Prerequisites**
1. **AssetId** - Use [POST /api/v1.0/assets](#/Assets/searchAssets) to identify the asset and extract `Items[].AssetId`.

**Workflow Example**
1. Search for asset: [POST /api/v1.0/assets](#/Assets/searchAssets) with tag or serial filter.
2. Call [GET /api/v1.0/assets/{assetId}/files](#/Assets/getAssetFiles) to list attached documents.
3. Use `FileId` from response to download or reference specific files.

**Common Use Cases**
- Retrieve warranty documents for procurement
- Access purchase receipts for audits
- Get asset images for inventory reports

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_id` | `assetId` | `path` | `yes` | `str` | `-` | UUID of the asset. Obtain via [POST /api/v1.0/assets](#/Assets/searchAssets), extract `Items[].AssetId` from response. |

#### Returns

- Typed call return: `FileListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `FileListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_ids_for_filter_sets`

Provenance: Golden OpenAPI contract

Operation ID: `getAssetIdsForFilterSets`

- Sync: `client.assets.get_asset_ids_for_filter_sets(body=..., timeout=None)`
- Async: `await client.assets.get_asset_ids_for_filter_sets(body=..., timeout=None)`
- Raw payload: `client.assets.get_asset_ids_for_filter_sets.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/ids/for/filtersets`
- Source controller: `IncidentIQ API`

Resolve asset IDs for filter sets

Returns matching asset IDs for one or more filter set definitions. Use this to preview which assets match saved filters or bulk operations without retrieving full asset records.

**Prerequisites**
1. **FilterSetIds** - Obtain from [GET /api/v1.0/filters/for/entitytype/{entityTypeId}](#/Filters/listFiltersForEntityType) using the assets entity type ID.

**Workflow Example**
1. Load filter set IDs for assets: [GET /api/v1.0/filters/for/entitytype/{entityTypeId}](#/Filters/listFiltersForEntityType).
2. Submit [POST /api/v1.0/assets/ids/for/filtersets](#/Assets/getAssetIdsForFilterSets) with `FilterSetIds`.
3. Read `Items[].MatchedIds` for each filter set result.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `GetIdsForFilterSetRequest` | `GetIdsForFilterSetRequest` | - |

#### Returns

- Typed call return: `Any`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_inventory_type`

Provenance: Golden OpenAPI contract

Operation ID: `getAssetInventoryType`

- Sync: `client.assets.get_asset_inventory_type(asset_inventory_type_id=..., timeout=None)`
- Async: `await client.assets.get_asset_inventory_type(asset_inventory_type_id=..., timeout=None)`
- Raw payload: `client.assets.get_asset_inventory_type.raw(asset_inventory_type_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/assets/inventory/types/{assetInventoryTypeId}`
- Source controller: `IncidentIQ API`

Get asset inventory type by ID

Retrieves a single asset inventory type definition by its UUID.

**Prerequisites**
1. **assetInventoryTypeId** - Use [GET /api/v1.0/assets/inventory/types](#/Assets/listAssetInventoryTypes) to retrieve available types and extract `Items[].AssetInventoryTypeId`.

**Workflow Example**
1. List inventory types: [GET /api/v1.0/assets/inventory/types](#/Assets/listAssetInventoryTypes).
2. Extract the `AssetInventoryTypeId` for the desired type.
3. Call [GET /api/v1.0/assets/inventory/types/{assetInventoryTypeId}](#/Assets/getAssetInventoryType) for full details.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_inventory_type_id` | `assetInventoryTypeId` | `path` | `yes` | `str` | `-` | UUID of the asset inventory type to retrieve. |

#### Returns

- Typed call return: `AssetInventoryTypeItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetInventoryTypeItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_stats_by_location`

Provenance: Golden OpenAPI contract

Operation ID: `getAssetStatsByLocation`

- Sync: `client.assets.get_asset_stats_by_location(timeout=None)`
- Async: `await client.assets.get_asset_stats_by_location(timeout=None)`
- Raw payload: `client.assets.get_asset_stats_by_location.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/assets/stats/locations`
- Source controller: `IncidentIQ API`

Get asset statistics by location

Retrieves asset and ticket statistics grouped by location so you can power dashboards, distribution reports, or inventory health snapshots at the campus/room level.

**Workflow Example**
1. (Optional) Load location metadata: [GET /api/v2.0/locations/view](#/Locations/getMyLocationsViewV2) to map `LocationId` values to names.
2. [GET /api/v1.0/assets/stats/locations](#/Assets/getAssetStatsByLocation) to retrieve per-location counts and aggregates.

**Minimal Required Fields**: none.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `LocationStatListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `LocationStatListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_status_type`

Provenance: Golden OpenAPI contract

Operation ID: `getAssetStatusType`

- Sync: `client.assets.get_asset_status_type(asset_status_type_id=..., timeout=None)`
- Async: `await client.assets.get_asset_status_type(asset_status_type_id=..., timeout=None)`
- Raw payload: `client.assets.get_asset_status_type.raw(asset_status_type_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/assets/status/types/{assetStatusTypeId}`
- Source controller: `IncidentIQ API`

Get asset status type

Retrieves metadata for a specific asset status such as "In Storage" or "In Service".

**Prerequisites**
1. **assetStatusTypeId** - Use [GET /api/v1.0/assets/status/types](#/Assets/listAssetStatusTypes) to list all status types and extract `Items[].AssetStatusTypeId`.

**Workflow Example**
1. List status types: [GET /api/v1.0/assets/status/types](#/Assets/listAssetStatusTypes) to retrieve available definitions.
2. Extract the `AssetStatusTypeId` for the desired status.
3. Call [GET /api/v1.0/assets/status/types/{assetStatusTypeId}](#/Assets/getAssetStatusType) for full details.

**Minimal Required Fields**: assetStatusTypeId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_status_type_id` | `assetStatusTypeId` | `path` | `yes` | `str` | `-` | UUID of the status definition to retrieve. Obtain from asset records (`Status.AssetStatusTypeId`) or spare pool search results. |

#### Returns

- Typed call return: `AssetStatusTypeResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetStatusTypeResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_total_cost`

Provenance: Golden OpenAPI contract

Operation ID: `getAssetTotalCost`

- Sync: `client.assets.get_asset_total_cost(asset_id=..., timeout=None)`
- Async: `await client.assets.get_asset_total_cost(asset_id=..., timeout=None)`
- Raw payload: `client.assets.get_asset_total_cost.raw(asset_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/assets/{assetId}/total-cost`
- Source controller: `IncidentIQ API`

Get asset total cost

Retrieves the total cost breakdown for an asset, including labor, parts, and itemized costs from related tickets. Use this for lifecycle cost analysis, replacement decisions, or budgeting reports.

**Prerequisites**
1. **assetId** - Locate the asset via [POST /api/v1.0/assets/search](#/Assets/keywordSearchAssets) or [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById).

**Workflow Example**
1. Identify the asset record and capture `AssetId`.
2. [GET /api/v1.0/assets/{assetId}/total-cost](#/Assets/getAssetTotalCost) to retrieve the cost rollup.

**Minimal Required Fields**: `assetId` (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_id` | `assetId` | `path` | `yes` | `str` | `-` | UUID of the asset. Obtain via [POST /api/v1.0/assets](#/Assets/searchAssets), extract `Items[].AssetId` from response. |

#### Returns

- Typed call return: `AssetTotalCostResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetTotalCostResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_type`

Provenance: Golden OpenAPI contract

Operation ID: `getAssetType`

- Sync: `client.assets.get_asset_type(asset_type_id=..., timeout=None)`
- Async: `await client.assets.get_asset_type(asset_type_id=..., timeout=None)`
- Raw payload: `client.assets.get_asset_type.raw(asset_type_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/assets/types/{assetTypeId}`
- Source controller: `IncidentIQ API`

Get asset type by ID

Retrieves a single asset type definition by its UUID. Asset types define categorization for inventory management (e.g., Devices, Peripherals, Network Equipment).

**Prerequisites**
1. **assetTypeId** - Use [GET /api/v1.0/assets/types](#/Assets/listAssetTypes) to retrieve available types and extract `Items[].AssetTypeId`.

**Workflow Example**
1. List asset types: [GET /api/v1.0/assets/types](#/Assets/listAssetTypes) to get available categories.
2. Extract the `AssetTypeId` for the desired type.
3. Call [GET /api/v1.0/assets/types/{assetTypeId}](#/Assets/getAssetType) for full details.

**Minimal Required Fields**: `assetTypeId` (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_type_id` | `assetTypeId` | `path` | `yes` | `str` | `-` | UUID of the asset type to retrieve. Obtain from [GET /api/v1.0/assets/types](#/Assets/listAssetTypes) (`Items[].AssetTypeId`). |

#### Returns

- Typed call return: `AssetTypeItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetTypeItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_valuation`

Provenance: Golden OpenAPI contract

Operation ID: `getAssetValuation`

- Sync: `client.assets.get_asset_valuation(asset_id=..., timeout=None)`
- Async: `await client.assets.get_asset_valuation(asset_id=..., timeout=None)`
- Raw payload: `client.assets.get_asset_valuation.raw(asset_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/assets/{assetId}/valuation`
- Source controller: `IncidentIQ API`

Get asset valuation

Retrieves depreciation and valuation data for a specific asset, including useful life, replacement cost, salvage value, and period-based depreciation schedule entries used in lifecycle reporting. Use this endpoint when building cost dashboards, exporting valuation data, or validating asset financial assumptions for a single device.

**Prerequisites**
1. **assetId** - Use [GET /api/v1.0/assets](#/Assets/listAllAssets) or [POST /api/v1.0/assets/search](#/Assets/keywordSearchAssets) to locate the asset and extract `Items[].AssetId`.

**Workflow Example**
1. Find the asset: [GET /api/v1.0/assets](#/Assets/listAllAssets) or [POST /api/v1.0/assets/search](#/Assets/keywordSearchAssets) -> extract `Items[].AssetId`.
2. Retrieve valuation: [GET /api/v1.0/assets/{assetId}/valuation](#/Assets/getAssetValuation).

**Minimal Required Fields**: assetId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_id` | `assetId` | `path` | `yes` | `str` | `-` | UUID of the asset. Obtain via [POST /api/v1.0/assets](#/Assets/searchAssets), extract `Items[].AssetId` from response. |

#### Returns

- Typed call return: `AssetValuationResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetValuationResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_verifications_for_asset`

Provenance: Golden OpenAPI contract

Operation ID: `getAssetVerificationsForAsset`

- Sync: `client.assets.get_asset_verifications_for_asset(asset_id=..., timeout=None)`
- Async: `await client.assets.get_asset_verifications_for_asset(asset_id=..., timeout=None)`
- Raw payload: `client.assets.get_asset_verifications_for_asset.raw(asset_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/assets/{assetId}/verifications`
- Source controller: `IncidentIQ API`

Get verifications for asset

Retrieves all verification records for a specific asset. Use this to view the audit history of a single device.

**Prerequisites**
1. **assetId** - Use [POST /api/v1.0/assets](#/Assets/searchAssets) or [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById) to obtain.

**Workflow Example**
1. Load asset: [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById) to confirm identity.
2. Fetch verifications: [GET /api/v1.0/assets/{assetId}/verifications](#/Assets/getAssetVerificationsForAsset).

**Minimal Required Fields**: `assetId` (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_id` | `assetId` | `path` | `yes` | `str` | `-` | UUID of the asset. Obtain via [POST /api/v1.0/assets](#/Assets/searchAssets), extract `Items[].AssetId` from response. |

#### Returns

- Typed call return: `AssetVerificationListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetVerificationListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_view`

Provenance: Golden OpenAPI contract

Operation ID: `getAssetView`

- Sync: `client.assets.get_asset_view(view_id=..., timeout=None)`
- Async: `await client.assets.get_asset_view(view_id=..., timeout=None)`
- Raw payload: `client.assets.get_asset_view.raw(view_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/assets/views/{viewId}`
- Source controller: `IncidentIQ API`

Get asset view

Returns a single asset view definition, including filters, columns, sort order, and any sharing metadata needed to render the saved layout exactly as the user configured it.

**Prerequisites**
1. **viewId** - Obtain from [GET /api/v1.0/assets/views](#/Assets/listAssetViews) by selecting the target view.

**Workflow Example**
1. List views: [GET /api/v1.0/assets/views](#/Assets/listAssetViews) -> capture `Items[].ViewId` for the desired view.
2. Retrieve the definition: [GET /api/v1.0/assets/views/{viewId}](#/Assets/getAssetView).

**Minimal Required Fields**: `viewId` (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `view_id` | `viewId` | `path` | `yes` | `str` | `-` | Identifier of the asset view to retrieve. |

#### Returns

- Typed call return: `ViewItemGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ViewItemGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_assets_by_name`

Provenance: Golden OpenAPI contract

Operation ID: `getAssetsByName`

- Sync: `client.assets.get_assets_by_name(p=None, s=None, filter=None, timeout=None)`
- Async: `await client.assets.get_assets_by_name(p=None, s=None, filter=None, timeout=None)`
- Raw payload: `client.assets.get_assets_by_name.raw(p=None, s=None, filter=None, timeout=None)`
- HTTP route: `POST /api/v1.0/assets/by-assetname`
- Source controller: `IncidentIQ API`

Search assets by name

Searches assets by the asset name field using OData-style filters and optional paging. This is a lightweight alternative to full keyword search when you only need to match names and want consistent paging behavior.

**Workflow Example**
1. Send [POST /api/v1.0/assets/by-assetname](#/Assets/getAssetsByName) with a `$filter` such as `contains(AssetName,'Chromebook')` and optional `$p`/`$s` paging.
2. Use returned `Items[].AssetId` to load full records with [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById).

**Minimal Required Fields**: none (include `$filter` for meaningful results).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index |
| `s` | `$s` | `query` | `no` | `int` | `-` | Page size |
| `filter` | `$filter` | `query` | `no` | `str` | `-` | OData filter expression |

#### Returns

- Typed call return: `AssetSearchResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetSearchResponse`
- Pagination helper: `client.assets.get_assets_by_name.iter_pages(start_page=1, page_size=100, max_pages=None, p=None, s=None, filter=None, timeout=None)`

---

### `get_assets_by_type`

Provenance: Golden OpenAPI contract

Operation ID: `getAssetsByType`

- Sync: `client.assets.get_assets_by_type(asset_type_id=..., p=None, s=None, o=None, body=None, timeout=None)`
- Async: `await client.assets.get_assets_by_type(asset_type_id=..., p=None, s=None, o=None, body=None, timeout=None)`
- Raw payload: `client.assets.get_assets_by_type.raw(asset_type_id=..., p=None, s=None, o=None, body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/assets/of/{assetTypeId}`
- Source controller: `IncidentIQ API`

Get assets by type

Retrieves a paginated list of assets filtered by asset type. This endpoint allows filtering assets by their type (e.g., Devices, Software, Peripherals) with additional filter criteria.

**Prerequisites**
1. **assetTypeId** - Obtain valid asset type IDs from [GET /api/v1.0/assets/types](#/Assets/listAssetTypes) and read `Items[].AssetTypeId`.

**Workflow Example**
1. List available asset types: [GET /api/v1.0/assets/types](#/Assets/listAssetTypes) -> capture `AssetTypeId` for 'Devices'.
2. Query assets of that type: [POST /api/v1.0/assets/of/{assetTypeId}](#/Assets/getAssetsByType) with optional filter criteria.

**Common Asset Type IDs**:
- Devices: `2a1561e5-34ff-4fcf-87de-2a146f0e1c01`
- Software: Use listAssetTypes to discover

Supports pagination via `$p` (page index) and `$s` (page size) query parameters.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_type_id` | `assetTypeId` | `path` | `yes` | `str` | `-` | UUID of the asset type to filter by. Obtain from [GET /api/v1.0/assets/types](#/Assets/listAssetTypes) (`Items[].AssetTypeId`). |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index to retrieve |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of records per page (default: 100) |
| `o` | `$o` | `query` | `no` | `Any` | `-` | Sort expression: field name followed by optional direction (e.g., `ModelName desc`). Direction can be `asc`, `ascending`, `desc`, or `descending`. Default direction is ascending. See [AssetSortField](#/components/schemas/AssetSortField) for valid field names. |
| `body` | `body` | `body` | `no` | `AssetFilterMatchListRequest` | `AssetFilterMatchListRequest` | Optional array of filter criteria to narrow down results |

#### Returns

- Typed call return: `AssetSearchResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetSearchResponse`
- Pagination helper: `client.assets.get_assets_by_type.iter_pages(start_page=1, page_size=100, max_pages=None, asset_type_id=..., p=None, s=None, o=None, body=None, timeout=None)`

---

### `get_assets_by_type_and_location`

Provenance: Golden OpenAPI contract

Operation ID: `getAssetsByTypeAndLocation`

- Sync: `client.assets.get_assets_by_type_and_location(asset_type_id=..., location_id=..., p=None, s=None, timeout=None)`
- Async: `await client.assets.get_assets_by_type_and_location(asset_type_id=..., location_id=..., p=None, s=None, timeout=None)`
- Raw payload: `client.assets.get_assets_by_type_and_location.raw(asset_type_id=..., location_id=..., p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v1.0/assets/of/{assetTypeId}/at/{locationId}`
- Source controller: `IncidentIQ API`

Get assets by type and location

Retrieves assets filtered by both type and location. Use this for targeted inventory views (for example, all Chromebooks at a specific campus) without building a full filter payload.

**Prerequisites**
1. **assetTypeId** - Obtain from [GET /api/v1.0/assets/types](#/Assets/listAssetTypes).
2. **locationId** - Obtain from [GET /api/v2.0/locations/view](#/Locations/getMyLocationsViewV2).

**Workflow Example**
1. List asset types and select the target type.
2. List locations and select the target location.
3. [GET /api/v1.0/assets/of/{assetTypeId}/at/{locationId}](#/Assets/getAssetsByTypeAndLocation) with optional paging.

**Minimal Required Fields**: `assetTypeId`, `locationId` (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_type_id` | `assetTypeId` | `path` | `yes` | `str` | `-` | UUID of the asset type |
| `location_id` | `locationId` | `path` | `yes` | `str` | `-` | UUID of the location (optional) |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index |
| `s` | `$s` | `query` | `no` | `int` | `-` | Page size |

#### Returns

- Typed call return: `AssetSearchResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetSearchResponse`
- Pagination helper: `client.assets.get_assets_by_type_and_location.iter_pages(start_page=1, page_size=100, max_pages=None, asset_type_id=..., location_id=..., p=None, s=None, timeout=None)`

---

### `get_assets_for_user_by_type`

Provenance: Golden OpenAPI contract

Operation ID: `getAssetsForUserByType`

- Sync: `client.assets.get_assets_for_user_by_type(asset_type_id=..., user_id=..., p=None, s=None, timeout=None)`
- Async: `await client.assets.get_assets_for_user_by_type(asset_type_id=..., user_id=..., p=None, s=None, timeout=None)`
- Raw payload: `client.assets.get_assets_for_user_by_type.raw(asset_type_id=..., user_id=..., p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v1.0/assets/of/{assetTypeId}/for/{userId}`
- Source controller: `IncidentIQ API`

Get user's assets by type

Retrieves assets of a specific type assigned to a user. Use this to show a user’s assigned devices by category or to validate eligibility during ticket creation.

**Prerequisites**
1. **assetTypeId** - Obtain from [GET /api/v1.0/assets/types](#/Assets/listAssetTypes).
2. **userId** - Obtain from [POST /api/v1.0/search](#/Users/searchUsers).

**Workflow Example**
1. Identify the asset type (for example, Devices).
2. Search for the user and capture `UserId`.
3. [GET /api/v1.0/assets/of/{assetTypeId}/for/{userId}](#/Assets/getAssetsForUserByType) to return the inventory list.

**Minimal Required Fields**: `assetTypeId`, `userId` (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_type_id` | `assetTypeId` | `path` | `yes` | `str` | `-` | UUID of the asset type |
| `user_id` | `userId` | `path` | `yes` | `str` | `-` | UUID of the user |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index |
| `s` | `$s` | `query` | `no` | `int` | `-` | Page size |

#### Returns

- Typed call return: `AssetSearchResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetSearchResponse`
- Pagination helper: `client.assets.get_assets_for_user_by_type.iter_pages(start_page=1, page_size=100, max_pages=None, asset_type_id=..., user_id=..., p=None, s=None, timeout=None)`

---

### `get_assets_for_user_current`

Provenance: Golden OpenAPI contract

Operation ID: `getAssetsForUserCurrent`

- Sync: `client.assets.get_assets_for_user_current(user_id=..., all=None, p=None, s=None, timeout=None)`
- Async: `await client.assets.get_assets_for_user_current(user_id=..., all=None, p=None, s=None, timeout=None)`
- Raw payload: `client.assets.get_assets_for_user_current.raw(user_id=..., all=None, p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v1.0/assets/for/{userId}`
- Source controller: `IncidentIQ API`

Get a user's currently assigned assets

Retrieves a list of assets currently assigned to the specified user. Optionally includes assets within the user's assigned location rooms when the `all` parameter is set.

**Prerequisites**
1. **userId** - Call [POST /api/v1.0/search](#/Search/globalSearch) with a user filter (email, username, or barcode) and read `Item.Users[].UserId`.

**Workflow Example**
1. Search for the requester: [POST /api/v1.0/search](#/Search/globalSearch) to capture `UserId`.
2. Call [GET /api/v1.0/assets/for/{userId}](#/Assets/getAssetsForUserCurrent) with optional paging parameters to fetch the device list for ticket creation, audits, or user reviews.
3. Set `all=all` to include assets in the user's location rooms.

**Alternative Path**: `/api/v1.0/assets/for/{userId}/all` also includes location room assets.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `userId` | `path` | `yes` | `str` | `-` | UUID of the requester whose assets should be returned. Obtain with POST /api/v1.0/search and inspect `Item.Users[].UserId`. |
| `all` | `all` | `query` | `no` | `str` | `-` | When set to 'all', includes assets within the user's assigned location rooms. Default returns only directly assigned assets. |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index to retrieve |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of records per page |

#### Returns

- Typed call return: `AssetSearchResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetSearchResponse`
- Pagination helper: `client.assets.get_assets_for_user_current.iter_pages(start_page=1, page_size=100, max_pages=None, user_id=..., all=None, p=None, s=None, timeout=None)`

---

### `get_available_asset_categories`

Provenance: Golden OpenAPI contract

Operation ID: `getAvailableAssetCategories`

- Sync: `client.assets.get_available_asset_categories(timeout=None)`
- Async: `await client.assets.get_available_asset_categories(timeout=None)`
- Raw payload: `client.assets.get_available_asset_categories.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/assets/categories/site`
- Source controller: `IncidentIQ API`

Get available asset categories for site

Returns asset categories enabled for the current site, including any site option details used to control visibility or access. Use this list to populate category picklists in asset creation/edit flows and to validate a category before enabling or disabling it. 

**Workflow Example**
1. Fetch current categories: [GET /api/v1.0/assets/categories/site](#/Assets/getAvailableAssetCategories) to populate UI choices.
2. Enable or disable a category using [POST /api/v1.0/assets/categories/{categoryId}/site](#/Assets/addCategoryToSite) or [DELETE /api/v1.0/assets/categories/{categoryId}/site](#/Assets/removeCategoryFromSite).

**Minimal Required Fields**: none.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `CategoryRolesListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CategoryRolesListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_facility_assets_by_location`

Provenance: Golden OpenAPI contract

Operation ID: `getFacilityAssetsByLocation`

- Sync: `client.assets.get_facility_assets_by_location(location_id=..., p=None, s=None, timeout=None)`
- Async: `await client.assets.get_facility_assets_by_location(location_id=..., p=None, s=None, timeout=None)`
- Raw payload: `client.assets.get_facility_assets_by_location.raw(location_id=..., p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v1.0/assets/facility/at/{locationId}`
- Source controller: `IncidentIQ API`

Get facility assets at location

Retrieves facility and equipment assets assigned to a specific location. This endpoint filters inventory to the facility equipment asset type so it is useful for maintenance lists, room audits, or fixed equipment reports.

**Prerequisites**
1. **locationId** - Use [GET /api/v2.0/locations/view](#/Locations/getMyLocationsViewV2) to obtain the location identifier.

**Workflow Example**
1. Load locations for the site and select the room or campus.
2. [GET /api/v1.0/assets/facility/at/{locationId}](#/Assets/getFacilityAssetsByLocation) to retrieve facility assets assigned to that location.

**Minimal Required Fields**: `locationId` (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `location_id` | `locationId` | `path` | `yes` | `str` | `-` | UUID of the location (optional, returns all if not specified) |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index |
| `s` | `$s` | `query` | `no` | `int` | `-` | Page size |

#### Returns

- Typed call return: `AssetSearchResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetSearchResponse`
- Pagination helper: `client.assets.get_facility_assets_by_location.iter_pages(start_page=1, page_size=100, max_pages=None, location_id=..., p=None, s=None, timeout=None)`

---

### `get_global_manufacturers`

Provenance: Golden OpenAPI contract

Operation ID: `getGlobalManufacturers`

- Sync: `client.assets.get_global_manufacturers(top=None, skip=None, orderby=None, orderby_direction=None, timeout=None)`
- Async: `await client.assets.get_global_manufacturers(top=None, skip=None, orderby=None, orderby_direction=None, timeout=None)`
- Raw payload: `client.assets.get_global_manufacturers.raw(top=None, skip=None, orderby=None, orderby_direction=None, timeout=None)`
- HTTP route: `GET /api/v1.0/assets/manufacturers/global`
- Source controller: `IncidentIQ API`

List global manufacturers

Retrieves all globally-scoped manufacturers without applying site visibility filters. Unlike the standard list endpoint, this returns the complete global manufacturer catalog regardless of which manufacturers have been enabled at the current site.

**Use Cases**
- Administrative interface for managing the global manufacturer catalog
- Selecting manufacturers to add to a specific site via [POST /api/v1.0/assets/manufacturers/{ManufacturerId}/site](#/Manufacturers/addManufacturerToSite)
- Comparing site-enabled manufacturers against the full global catalog

**Scope Behavior**
Global manufacturers have `Scope: "Global"` and `SiteId: null`. They represent the master catalog from which sites can select which manufacturers to make available.

**Filtering**
Supports standard pagination (`$top`, `$skip`) and sorting (`$orderby`, `$orderbyDirection`). For complex filters, use [POST /api/v1.0/assets/manufacturers/global](#/Manufacturers/searchGlobalManufacturers).

**Related Endpoints**
- [GET /api/v1.0/assets/manufacturers](#/Manufacturers/getManufacturers) - List site-filtered manufacturers
- [POST /api/v1.0/assets/manufacturers/{ManufacturerId}/site](#/Manufacturers/addManufacturerToSite) - Enable a global manufacturer at current site

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

### `get_linked_assets`

Provenance: Golden OpenAPI contract

Operation ID: `getLinkedAssets`

- Sync: `client.assets.get_linked_assets(asset_id=..., p=None, s=None, timeout=None)`
- Async: `await client.assets.get_linked_assets(asset_id=..., p=None, s=None, timeout=None)`
- Raw payload: `client.assets.get_linked_assets.raw(asset_id=..., p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v1.0/assets/linked/to/{assetId}`
- Source controller: `IncidentIQ API`

Get linked assets

Retrieves all assets linked to a parent asset. Asset linking creates parent-child relationships for accessories, peripherals, or component tracking.

**Use Cases:**
- View all peripherals linked to a laptop (charger, mouse, case)
- Track component relationships for facility equipment
- Build asset hierarchy reports

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_id` | `assetId` | `path` | `yes` | `str` | `-` | UUID of the parent asset. Obtain via [POST /api/v1.0/assets](#/Assets/searchAssets), extract `Items[].AssetId` from response. |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index |
| `s` | `$s` | `query` | `no` | `int` | `-` | Page size |

#### Returns

- Typed call return: `LinkedAssetListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `LinkedAssetListResponse`
- Pagination helper: `client.assets.get_linked_assets.iter_pages(start_page=1, page_size=100, max_pages=None, asset_id=..., p=None, s=None, timeout=None)`

---

### `get_manufacturer_by_id`

Provenance: Golden OpenAPI contract

Operation ID: `getManufacturerById`

- Sync: `client.assets.get_manufacturer_by_id(manufacturer_id=..., timeout=None)`
- Async: `await client.assets.get_manufacturer_by_id(manufacturer_id=..., timeout=None)`
- Raw payload: `client.assets.get_manufacturer_by_id.raw(manufacturer_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/assets/manufacturers/{ManufacturerId}`
- Source controller: `IncidentIQ API`

Get manufacturer by ID

Retrieves detailed information about a specific manufacturer by its unique identifier.

**Prerequisites**
- **ManufacturerId** - Use [GET /api/v1.0/assets/manufacturers](#/Manufacturers/getManufacturers) to list manufacturers. Extract `Items[].ManufacturerId` from the response.

**Response Fields**
- `ManufacturerId` - Unique identifier (UUID)
- `Name` - Display name of the manufacturer
- `Scope` - Either "Global" (available everywhere) or "Site" (site-specific)
- `SiteId` - The owning site for site-scoped manufacturers, null for global
- `EsoIsVisible` - Whether visible in the Employee Self-Service portal
- `LogoId` - Reference to uploaded logo image, if any
- `Icon` - Font Awesome icon class for UI display

**Use Cases**
- Display manufacturer details in asset management UI
- Pre-populate edit form when updating manufacturer
- Verify manufacturer exists before creating models

**Related Endpoints**
- [POST /api/v1.0/assets/manufacturers/{ManufacturerId}](#/Manufacturers/updateManufacturer) - Update this manufacturer
- [DELETE /api/v1.0/assets/manufacturers/{ManufacturerId}](#/Manufacturers/deleteManufacturer) - Delete this manufacturer

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `manufacturer_id` | `ManufacturerId` | `path` | `yes` | `str` | `-` | Unique identifier of the manufacturer |

#### Returns

- Typed call return: `Any`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_manufacturers`

Provenance: Golden OpenAPI contract

Operation ID: `getManufacturers`

- Sync: `client.assets.get_manufacturers(top=None, skip=None, orderby=None, orderby_direction=None, timeout=None)`
- Async: `await client.assets.get_manufacturers(top=None, skip=None, orderby=None, orderby_direction=None, timeout=None)`
- Raw payload: `client.assets.get_manufacturers.raw(top=None, skip=None, orderby=None, orderby_direction=None, timeout=None)`
- HTTP route: `GET /api/v1.0/assets/manufacturers`
- Source controller: `IncidentIQ API`

List manufacturers

Retrieves a paginated list of manufacturers available at the current site, including both site-specific and global manufacturers.

**Use Cases**
- Populate manufacturer dropdown when creating or editing assets
- Display manufacturer catalog for site administrators
- Filter assets by manufacturer in reporting workflows

**Response Structure**
Returns manufacturers with their scope (Global or Site), visibility settings, and optional logo information. Site-scoped manufacturers are only visible at their assigned site, while global manufacturers appear across all sites.

**Filtering**
Supports standard pagination (`$top`, `$skip`) and sorting (`$orderby`, `$orderbyDirection`). Use [POST /api/v1.0/assets/manufacturers](#/Manufacturers/searchManufacturers) for complex filter criteria.

**Related Endpoints**
- [GET /api/v1.0/assets/manufacturers/global](#/Manufacturers/getGlobalManufacturers) - List only global manufacturers
- [POST /api/v1.0/assets/manufacturers/new](#/Manufacturers/createManufacturer) - Create a new manufacturer

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

### `get_model_visibility`

Provenance: Golden OpenAPI contract

Operation ID: `getModelVisibility`

- Sync: `client.assets.get_model_visibility(asset_id=..., model_id=..., timeout=None)`
- Async: `await client.assets.get_model_visibility(asset_id=..., model_id=..., timeout=None)`
- Raw payload: `client.assets.get_model_visibility.raw(asset_id=..., model_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/assets/{assetId}/{modelId}/visibility`
- Source controller: `IncidentIQ API`

Get model visibility

Checks whether a specific model is visible or eligible for the given asset context. Use this when validating model selection during swaps, replacements, or category restrictions.

**Prerequisites**
1. **assetId** - Obtain from [POST /api/v1.0/assets/search](#/Assets/keywordSearchAssets) or [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById).
2. **modelId** - Obtain from the asset record or by querying models via [POST /api/v1.0/models](#/Issues/getIssuesForModels).

**Workflow Example**
1. Load the asset to confirm its current model/category.
2. Choose the candidate model and capture its `ModelId`.
3. [GET /api/v1.0/assets/{assetId}/{modelId}/visibility](#/Assets/getModelVisibility) to confirm eligibility.

**Minimal Required Fields**: `assetId`, `modelId` (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_id` | `assetId` | `path` | `yes` | `str` | `-` | UUID of the asset. Obtain via [POST /api/v1.0/assets](#/Assets/searchAssets), extract `Items[].AssetId` from response. |
| `model_id` | `modelId` | `path` | `yes` | `str` | `-` | UUID of the model. Obtain via [POST /api/v1.0/models](#/Models/searchModels), extract `Items[].ModelId` from response. |

#### Returns

- Typed call return: `AssetModelVisibilityResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetModelVisibilityResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_my_assets`

Provenance: Golden OpenAPI contract

Operation ID: `getMyAssets`

- Sync: `client.assets.get_my_assets(all=None, p=None, s=None, timeout=None)`
- Async: `await client.assets.get_my_assets(all=None, p=None, s=None, timeout=None)`
- Raw payload: `client.assets.get_my_assets.raw(all=None, p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v1.0/assets/for/me`
- Source controller: `IncidentIQ API`

Get my currently assigned assets

Retrieves a list of assets currently assigned to the authenticated user. This is a convenience endpoint that automatically uses the caller's user ID.

**Workflow Example**
1. Call [GET /api/v1.0/assets/for/me](#/Assets/getMyAssets) to retrieve your assigned devices.
2. Use optional `all` parameter to include assets in your assigned location rooms.

**Alternative Path**: `/api/v1.0/assets/for/me/all` includes location room assets.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `all` | `all` | `query` | `no` | `str` | `-` | When set to 'all', includes assets within the authenticated user's assigned location rooms. Default returns only directly assigned assets. |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index to retrieve |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of records per page |

#### Returns

- Typed call return: `AssetSearchResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetSearchResponse`
- Pagination helper: `client.assets.get_my_assets.iter_pages(start_page=1, page_size=100, max_pages=None, all=None, p=None, s=None, timeout=None)`

---

### `get_my_assets_by_type`

Provenance: Golden OpenAPI contract

Operation ID: `getMyAssetsByType`

- Sync: `client.assets.get_my_assets_by_type(asset_type_id=..., p=None, s=None, timeout=None)`
- Async: `await client.assets.get_my_assets_by_type(asset_type_id=..., p=None, s=None, timeout=None)`
- Raw payload: `client.assets.get_my_assets_by_type.raw(asset_type_id=..., p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v1.0/assets/of/{assetTypeId}/for/me`
- Source controller: `IncidentIQ API`

Get my assets by type

Retrieves assets of a specific type assigned to the authenticated user. This is a convenience endpoint that automatically uses the caller's user ID.

**Prerequisites**
1. **assetTypeId** - Obtain from [GET /api/v1.0/assets/types](#/Assets/listAssetTypes).

**Workflow Example**
1. Get asset types: [GET /api/v1.0/assets/types](#/Assets/listAssetTypes) and identify the target type.
2. [GET /api/v1.0/assets/of/{assetTypeId}/for/me](#/Assets/getMyAssetsByType) to return your assigned assets of that type.

**Minimal Required Fields**: `assetTypeId` (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_type_id` | `assetTypeId` | `path` | `yes` | `str` | `-` | UUID of the asset type to filter by |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index |
| `s` | `$s` | `query` | `no` | `int` | `-` | Page size |

#### Returns

- Typed call return: `AssetSearchResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetSearchResponse`
- Pagination helper: `client.assets.get_my_assets_by_type.iter_pages(start_page=1, page_size=100, max_pages=None, asset_type_id=..., p=None, s=None, timeout=None)`

---

### `get_n_s_a_asset_average_cost`

Provenance: Golden OpenAPI contract

Operation ID: `getNSAAssetAverageCost`

- Sync: `client.assets.get_n_s_a_asset_average_cost(asset_id=..., timeout=None)`
- Async: `await client.assets.get_n_s_a_asset_average_cost(asset_id=..., timeout=None)`
- Raw payload: `client.assets.get_n_s_a_asset_average_cost.raw(asset_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/assets/nsa/average-cost/{assetId}`
- Source controller: `IncidentIQ API`

Get NSA average cost

Retrieves the average district purchase price for a non-serialized asset (NSA). Use this to value consumables or bulk inventory items where individual serial numbers are not tracked.

**Prerequisites**
1. **assetId** - Locate the NSA asset via [POST /api/v1.0/assets/search](#/Assets/keywordSearchAssets) or by filtering for the NSA asset type in [GET /api/v1.0/assets/types](#/Assets/listAssetTypes).

**Workflow Example**
1. Identify the NSA asset record and capture its `AssetId`.
2. [GET /api/v1.0/assets/nsa/average-cost/{assetId}](#/Assets/getNSAAssetAverageCost) to retrieve average purchase price entries.

**Minimal Required Fields**: `assetId` (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_id` | `assetId` | `path` | `yes` | `str` | `-` | UUID of the NSA asset. Obtain via [POST /api/v1.0/assets](#/Assets/searchAssets), extract `Items[].AssetId` from response. |

#### Returns

- Typed call return: `NSAAverageDistrictPurchasePriceListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `NSAAverageDistrictPurchasePriceListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_overdue_asset_checkouts`

Provenance: Golden OpenAPI contract

Operation ID: `getOverdueAssetCheckouts`

- Sync: `client.assets.get_overdue_asset_checkouts(asset_id=..., body=..., timeout=None)`
- Async: `await client.assets.get_overdue_asset_checkouts(asset_id=..., body=..., timeout=None)`
- Raw payload: `client.assets.get_overdue_asset_checkouts.raw(asset_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/{assetId}/checkouts/user-ids`
- Source controller: `IncidentIQ API`

Get overdue checkouts for asset

Returns overdue or soon-to-be-overdue checkout records for a specific asset using day-based filters. Use this to drive notifications, overdue reports, or risk dashboards for a single device.

**Prerequisites**
1. **assetId** - Locate the asset via [POST /api/v1.0/assets/search](#/Assets/keywordSearchAssets) or [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById).
2. **Overdue filters** - Provide `NumberOfDaysOverdueFilters` and/or `NumberOfDaysUntilOverdueFilters` to define the threshold.

**Workflow Example**
1. Identify the asset record and capture `AssetId`.
2. Build a filter payload (for example, `NumberOfDaysOverdueFilters` with a value of 7).
3. [POST /api/v1.0/assets/{assetId}/checkouts/user-ids](#/Assets/getOverdueAssetCheckouts) to retrieve overdue checkout records.

**Minimal Required Fields**: `assetId` (path) and at least one of `NumberOfDaysOverdueFilters` or `NumberOfDaysUntilOverdueFilters` in the request body.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_id` | `assetId` | `path` | `yes` | `str` | `-` | UUID of the asset to evaluate. Obtain via [POST /api/v1.0/assets](#/Assets/searchAssets), extract `Items[].AssetId` from response. |
| `body` | `body` | `body` | `yes` | `GetOverdueAssetCheckoutsRequest` | `GetOverdueAssetCheckoutsRequest` | - |

#### Returns

- Typed call return: `AssetCheckoutListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetCheckoutListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_popular_categories_for_roles`

Provenance: Golden OpenAPI contract

Operation ID: `getPopularCategoriesForRoles`

- Sync: `client.assets.get_popular_categories_for_roles(body=..., timeout=None)`
- Async: `await client.assets.get_popular_categories_for_roles(body=..., timeout=None)`
- Raw payload: `client.assets.get_popular_categories_for_roles.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/categories/popular/for-roles`
- Source controller: `IncidentIQ API`

Get popular categories for roles

Returns the most popular asset category IDs for each role ID supplied, allowing clients to pre-populate category pickers or recommendations based on role context.

**Prerequisites**
1. **RoleIds** - Use [GET /api/v1.0/roles](#/Roles/listRoles) to retrieve roles and extract `Items[].RoleId`.

**Workflow Example**
1. List roles and select the RoleId values you care about.
2. [POST /api/v1.0/assets/categories/popular/for-roles](#/Categories/getPopularCategoriesForRoles) with the RoleId array.

**Minimal Required Fields**: request body array of RoleId values.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `UuidList` | `UuidList` | - |

#### Returns

- Typed call return: `GetPopularCategoriesForRolesResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `GetPopularCategoriesForRolesResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_recent_asset_checkout_transactions`

Provenance: Golden OpenAPI contract

Operation ID: `getRecentAssetCheckoutTransactions`

- Sync: `client.assets.get_recent_asset_checkout_transactions(body=None, timeout=None)`
- Async: `await client.assets.get_recent_asset_checkout_transactions(body=None, timeout=None)`
- Raw payload: `client.assets.get_recent_asset_checkout_transactions.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/assets/checkouts/transactions/recent-activity`
- Source controller: `IncidentIQ API`

Recent checkout activity

Returns the most recent checkout and check-in transactions for activity feeds, dashboards, or audit summaries. Use this for lightweight timelines, then pivot to detailed transaction records when you need full context or identifiers for updates.

**Workflow Example**
1. Request recent activity: [POST /api/v1.0/assets/checkouts/transactions/recent-activity](#/Assets/getRecentAssetCheckoutTransactions) with optional date or asset filters.
2. If you need more detail or identifiers, follow up with [POST /api/v1.0/assets/checkouts/transactions/query/get](#/Assets/getAssetCheckoutTransactions) for the selected time window.

**Minimal Required Fields**: none; add filters to scope results.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `GetAssetCheckoutsRequest` | `GetAssetCheckoutsRequest` | - |

#### Returns

- Typed call return: `AssetCheckoutTransactionListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetCheckoutTransactionListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_suggested_categories_for_user`

Provenance: Golden OpenAPI contract

Operation ID: `getSuggestedCategoriesForUser`

- Sync: `client.assets.get_suggested_categories_for_user(user_id=..., timeout=None)`
- Async: `await client.assets.get_suggested_categories_for_user(user_id=..., timeout=None)`
- Raw payload: `client.assets.get_suggested_categories_for_user.raw(user_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/assets/models/categories/suggested/{UserId}`
- Source controller: `IncidentIQ API`

Get suggested categories for user

Retrieves suggested model categories based on the user's history and common selections. Use this to pre-populate category pickers in the UI and improve user experience by surfacing relevant options first.

**Prerequisites**
1. **UserId** - Use [POST /api/v1.0/users/search](#/Users/searchUsers) to search for users and extract `Items[].UserId`. You can also use the alias `my` for the current authenticated user.

**Workflow Example**
1. Find user: [POST /api/v1.0/users/search](#/Users/searchUsers) → extract `Items[].UserId`.
2. Get suggestions: [GET /api/v1.0/assets/models/categories/suggested/{UserId}](#/Categories/getSuggestedCategoriesForUser).
3. Display returned categories as recommended options in your picker.

**Minimal Required Fields**: UserId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | User identifier to get suggestions for. Can use 'my' alias for current user. |

#### Returns

- Typed call return: `CategoryListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CategoryListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_suggested_online_systems_for_user`

Provenance: Golden OpenAPI contract

Operation ID: `getSuggestedOnlineSystemsForUser`

- Sync: `client.assets.get_suggested_online_systems_for_user(user_id=..., timeout=None)`
- Async: `await client.assets.get_suggested_online_systems_for_user(user_id=..., timeout=None)`
- Raw payload: `client.assets.get_suggested_online_systems_for_user.raw(user_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/assets/models/online-systems/suggested/{UserId}`
- Source controller: `IncidentIQ API`

Get suggested online systems for user

Retrieves suggested online systems (software/SaaS assets) based on the user's history and common selections. Use this to pre-populate online system pickers and improve user experience by surfacing relevant software options first.

**Prerequisites**
1. **UserId** - Use [POST /api/v1.0/users/search](#/Users/searchUsers) to search for users and extract `Items[].UserId`.

**Workflow Example**
1. Find user: [POST /api/v1.0/users/search](#/Users/searchUsers) → extract `Items[].UserId`.
2. Get suggestions: [GET /api/v1.0/assets/models/online-systems/suggested/{UserId}](#/Categories/getSuggestedOnlineSystemsForUser).
3. Display returned online systems as recommended options in your picker.

**Minimal Required Fields**: UserId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | User identifier to get suggestions for |

#### Returns

- Typed call return: `GetSuggestedOnlineSystemsForUserResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `GetSuggestedOnlineSystemsForUserResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_user_favorite_assets`

Provenance: Golden OpenAPI contract

Operation ID: `getUserFavoriteAssets`

- Sync: `client.assets.get_user_favorite_assets(user_id=..., timeout=None)`
- Async: `await client.assets.get_user_favorite_assets(user_id=..., timeout=None)`
- Raw payload: `client.assets.get_user_favorite_assets.raw(user_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/assets/favorites/{userId}`
- Source controller: `IncidentIQ API`

Get a user's favorite assets

Retrieves a list of assets that a user has marked as a favorite. This endpoint is useful for populating quick-access menus or for workflows where a user frequently interacts with the same set of devices.

**Route Variant**: To include assets in the user's assigned location rooms, append `/all` to the path: `GET /api/v1.0/assets/favorites/{userId}/all`.

**Prerequisites**
1. **userId** - Call [POST /api/v1.0/search](#/Search/globalSearch) with a user filter (email, username, or barcode) and read `Item.Users[].UserId`.

**Workflow Example**
1. Search for the user: [POST /api/v1.0/search](#/Search/globalSearch) to capture `UserId`.
2. Call [GET /api/v1.0/assets/favorites/{userId}](#/Assets/getUserFavoriteAssets) to fetch the list of favorite devices.
3. (Optional) Call `GET /api/v1.0/assets/favorites/{userId}/all` to include location room assets.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `userId` | `path` | `yes` | `str` | `-` | UUID of the user whose favorite assets should be returned. Obtain with POST /api/v1.0/search and inspect `Item.Users[].UserId`. |

#### Returns

- Typed call return: `AssetSearchResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetSearchResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `keyword_search_assets`

Provenance: Golden OpenAPI contract

Operation ID: `keywordSearchAssets`

- Sync: `client.assets.keyword_search_assets(p=None, s=None, o=None, body=..., timeout=None)`
- Async: `await client.assets.keyword_search_assets(p=None, s=None, o=None, body=..., timeout=None)`
- Raw payload: `client.assets.keyword_search_assets.raw(p=None, s=None, o=None, body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/search`
- Source controller: `IncidentIQ API`

Keyword search assets

Search assets using a keyword query with fine-grained control over which fields to search. Unlike the filter-based search (`POST /assets`), this endpoint performs text matching against specific asset fields.

**Search Fields**
Enable one or more boolean flags to control which fields are searched:
- `SearchAssetTag` - Match against asset tag
- `SearchSerial` - Match against serial number
- `SearchAssetName` - Match against asset name
- `SearchModelName` - Match against model name
- `SearchManufacturerName` - Match against manufacturer
- `SearchOwner` - Match against owner name

**Filtering Options**
- `AssetTypeId` / `AssetTypeIds` - Restrict to specific asset types
- `ExcludeAssetTypeIds` - Exclude specific asset types
- `ShowDeleted` / `ShowNotDeleted` - Control deleted asset visibility
- `SearchRoom` - Enable room-based search (increases page limit to 500)

**Example Use Cases**
1. Find assets by partial tag: `{"Query": "CHROME", "SearchAssetTag": true}`
2. Search by serial across all devices: `{"Query": "5CD", "SearchSerial": true}`
3. Find all Dell assets: `{"Query": "Dell", "SearchManufacturerName": true}`

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index |
| `s` | `$s` | `query` | `no` | `int` | `-` | Page size (max 1000, default 20; 500 when SearchRoom=true) |
| `o` | `$o` | `query` | `no` | `Any` | `-` | Sort expression: field name followed by optional direction (e.g., `ModelName desc`). Direction can be `asc`, `ascending`, `desc`, or `descending`. Default direction is ascending. See [AssetSortField](#/components/schemas/AssetSortField) for valid field names. |
| `body` | `body` | `body` | `yes` | `KeywordSearchAssetsRequest` | `KeywordSearchAssetsRequest` | - |

#### Returns

- Typed call return: `AssetSearchResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetSearchResponse`
- Pagination helper: `client.assets.keyword_search_assets.iter_pages(start_page=1, page_size=100, max_pages=None, p=None, s=None, o=None, body=..., timeout=None)`

---

### `list_all_assets`

Provenance: Golden OpenAPI contract

Operation ID: `listAllAssets`

- Sync: `client.assets.list_all_assets(s=None, o=None, filter=None, client=None, p=None, timeout=None)`
- Async: `await client.assets.list_all_assets(s=None, o=None, filter=None, client=None, p=None, timeout=None)`
- Raw payload: `client.assets.list_all_assets.raw(s=None, o=None, filter=None, client=None, p=None, timeout=None)`
- HTTP route: `GET /api/v1.0/assets`
- Source controller: `IncidentIQ API`

List assets

Retrieves a paginated list of assets across the inventory catalog and returns summary details for each asset, including status, ownership, location, and model context. Use query parameters to page (`$p`, `$s`), sort (`$o`, `$d`), and filter (`$filter`) the results so you can target specific locations, statuses, or asset types without pulling the entire dataset. The response includes paging metadata plus the asset records in `Items`, making this the common entry point for workflows that need an `AssetId` for follow-up calls.

**Workflow Example**
1. List assets with filters: [GET /api/v1.0/assets](#/Assets/listAllAssets) with `$filter`, `$p`, and `$s` query parameters -> read `Items[].AssetId`.
2. Use the selected ID for detail or valuation requests such as [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById) or [GET /api/v1.0/assets/{assetId}/valuation](#/Assets/getAssetValuation).

**Minimal Required Fields**: none.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `s` | `$s` | `query` | `no` | `int` | `-` | - |
| `o` | `$o` | `query` | `no` | `Any` | `-` | Sort expression: field name followed by optional direction (e.g., `AssetTag desc`). Direction can be `asc`, `ascending`, `desc`, or `descending`. Default direction is ascending. See [AssetSortField](#/components/schemas/AssetSortField) for valid field names. |
| `filter` | `$filter` | `query` | `no` | `str` | `-` | - |
| `client` | `Client` | `header` | `no` | `str` | `-` | - |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index to retrieve |

#### Returns

- Typed call return: `AssetSearchResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetSearchResponse`
- Pagination helper: `client.assets.list_all_assets.iter_pages(start_page=1, page_size=100, max_pages=None, s=None, o=None, filter=None, client=None, p=None, timeout=None)`

---

### `list_asset_funding_types`

Provenance: Golden OpenAPI contract

Operation ID: `listAssetFundingTypes`

- Sync: `client.assets.list_asset_funding_types(timeout=None)`
- Async: `await client.assets.list_asset_funding_types(timeout=None)`
- Raw payload: `client.assets.list_asset_funding_types.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/assets/funding/types`
- Source controller: `IncidentIQ API`

Get Asset Funding Types

Returns the catalog of funding sources that can be assigned to assets. Funding types define budget categories like Title I, E-Rate, General Fund, or Grant funding.

**Workflow Example**
1. Call [GET /api/v1.0/assets/funding/types](#/Assets/listAssetFundingTypes) to retrieve available funding sources.
2. Extract `Items[].FundingTypeId` for the appropriate budget category.
3. Include `FundingTypeId` when creating assets via [POST /api/v1.0/assets/new](#/Assets/createAsset) or updating via [POST /api/v1.0/assets/{assetId}](#/Assets/updateAsset).

**Common Use Cases**
- Populate funding source dropdowns in asset forms
- Generate financial reports grouped by funding type
- Track E-Rate or grant-funded device purchases

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `AssetFundingTypeListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetFundingTypeListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_asset_inventory_types`

Provenance: Golden OpenAPI contract

Operation ID: `listAssetInventoryTypes`

- Sync: `client.assets.list_asset_inventory_types(p=None, s=None, timeout=None)`
- Async: `await client.assets.list_asset_inventory_types(p=None, s=None, timeout=None)`
- Raw payload: `client.assets.list_asset_inventory_types.raw(p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v1.0/assets/inventory/types`
- Source controller: `IncidentIQ API`

List asset inventory types

Returns all available asset inventory types for the tenant. Inventory types classify assets into categories such as Tracked, Consumable, or Non-Inventory that control how assets are managed and counted.

**Workflow Example**
1. Call [GET /api/v1.0/assets/inventory/types](#/Assets/listAssetInventoryTypes) to retrieve available inventory classifications.
2. Extract `Items[].AssetInventoryTypeId` for use when creating asset types.
3. Reference the inventory type when creating new asset types via [POST /api/v1.0/assets/types/new](#/Assets/createAssetType).

**Common Use Cases**
- Bootstrap inventory type dropdowns when configuring asset types
- Validate inventory classification during asset import
- Build reports filtered by inventory classification

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index to retrieve |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of records per page |

#### Returns

- Typed call return: `AssetInventoryTypeListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetInventoryTypeListResponse`
- Pagination helper: `client.assets.list_asset_inventory_types.iter_pages(start_page=1, page_size=100, max_pages=None, p=None, s=None, timeout=None)`

---

### `list_asset_inventory_types_post`

Provenance: Golden OpenAPI contract

Operation ID: `listAssetInventoryTypesPost`

- Sync: `client.assets.list_asset_inventory_types_post(p=None, s=None, body=None, timeout=None)`
- Async: `await client.assets.list_asset_inventory_types_post(p=None, s=None, body=None, timeout=None)`
- Raw payload: `client.assets.list_asset_inventory_types_post.raw(p=None, s=None, body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/assets/inventory/types`
- Source controller: `IncidentIQ API`

List asset inventory types (POST)

Returns all available asset inventory types for the tenant.

This POST variant accepts filter parameters in the request body and is functionally equivalent to [GET /api/v1.0/assets/inventory/types](#/Assets/listAssetInventoryTypes).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index to retrieve |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of records per page |
| `body` | `body` | `body` | `no` | `GetAssetInventoryTypesRequest` | `GetAssetInventoryTypesRequest` | - |

#### Returns

- Typed call return: `AssetInventoryTypeListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetInventoryTypeListResponse`
- Pagination helper: `client.assets.list_asset_inventory_types_post.iter_pages(start_page=1, page_size=100, max_pages=None, p=None, s=None, body=None, timeout=None)`

---

### `list_asset_status_types`

Provenance: Golden OpenAPI contract

Operation ID: `listAssetStatusTypes`

- Sync: `client.assets.list_asset_status_types(p=None, s=None, timeout=None)`
- Async: `await client.assets.list_asset_status_types(p=None, s=None, timeout=None)`
- Raw payload: `client.assets.list_asset_status_types.raw(p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v1.0/assets/status/types`
- Source controller: `IncidentIQ API`

List asset status types

Returns all available asset status types for the tenant. Status types control asset lifecycle states such as 'In Service', 'In Repair', 'Retired', 'In Storage', etc.

**Workflow Example**
1. Call [GET /api/v1.0/assets/status/types](#/Assets/listAssetStatusTypes) to retrieve available status definitions.
2. Extract `Items[].AssetStatusTypeId` for use when updating asset status.
3. Update an asset's status via [POST /api/v1.0/assets/{assetId}/status/{assetStatusTypeId}](#/Assets/setAssetStatus).

**Common Use Cases**
- Populate status dropdowns in asset management forms
- Build asset status workflow dashboards
- Validate status transitions during asset lifecycle management

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index to retrieve |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of records per page |

#### Returns

- Typed call return: `AssetStatusTypeListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetStatusTypeListResponse`
- Pagination helper: `client.assets.list_asset_status_types.iter_pages(start_page=1, page_size=100, max_pages=None, p=None, s=None, timeout=None)`

---

### `list_asset_status_types_post`

Provenance: Golden OpenAPI contract

Operation ID: `listAssetStatusTypesPost`

- Sync: `client.assets.list_asset_status_types_post(p=None, s=None, body=None, timeout=None)`
- Async: `await client.assets.list_asset_status_types_post(p=None, s=None, body=None, timeout=None)`
- Raw payload: `client.assets.list_asset_status_types_post.raw(p=None, s=None, body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/assets/status/types`
- Source controller: `IncidentIQ API`

List asset status types (POST)

Returns all available asset status types for the tenant. This POST variant accepts filter parameters in the request body and is functionally equivalent to [GET /api/v1.0/assets/status/types](#/Assets/listAssetStatusTypes).

**Workflow Example**
1. Call [POST /api/v1.0/assets/status/types](#/Assets/listAssetStatusTypesPost) with optional filters.
2. Extract `Items[].AssetStatusTypeId` for use when updating asset status.
3. Update an asset's status via [POST /api/v1.0/assets/{assetId}/status/{assetStatusTypeId}](#/Assets/setAssetStatus).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index to retrieve |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of records per page |
| `body` | `body` | `body` | `no` | `GetAssetStatusTypesRequest` | `GetAssetStatusTypesRequest` | - |

#### Returns

- Typed call return: `AssetStatusTypeListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetStatusTypeListResponse`
- Pagination helper: `client.assets.list_asset_status_types_post.iter_pages(start_page=1, page_size=100, max_pages=None, p=None, s=None, body=None, timeout=None)`

---

### `list_asset_types`

Provenance: Golden OpenAPI contract

Operation ID: `listAssetTypes`

- Sync: `client.assets.list_asset_types(p=None, s=None, timeout=None)`
- Async: `await client.assets.list_asset_types(p=None, s=None, timeout=None)`
- Raw payload: `client.assets.list_asset_types.raw(p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v1.0/assets/types`
- Source controller: `IncidentIQ API`

List asset types

Returns the catalog of asset types available in the tenant (e.g., Devices, Peripherals, Network Equipment). Asset types define categorization for inventory management.

**Workflow Example**
1. Call [GET /api/v1.0/assets/types](#/Assets/listAssetTypes) to retrieve available categories.
2. Extract `Items[].AssetTypeId` for the desired category.
3. Use the `AssetTypeId` when creating assets via [POST /api/v1.0/assets/new](#/Assets/createAsset) or filtering via [POST /api/v1.0/assets](#/Assets/searchAssets).

**Common Use Cases**
- Populate asset type dropdowns in forms
- Filter assets by category in reports
- Bootstrap data for asset import workflows

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index to retrieve |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of records per page |

#### Returns

- Typed call return: `AssetTypeListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetTypeListResponse`
- Pagination helper: `client.assets.list_asset_types.iter_pages(start_page=1, page_size=100, max_pages=None, p=None, s=None, timeout=None)`

---

### `list_asset_types_post`

Provenance: Golden OpenAPI contract

Operation ID: `listAssetTypesPost`

- Sync: `client.assets.list_asset_types_post(p=None, s=None, body=None, timeout=None)`
- Async: `await client.assets.list_asset_types_post(p=None, s=None, body=None, timeout=None)`
- Raw payload: `client.assets.list_asset_types_post.raw(p=None, s=None, body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/assets/types`
- Source controller: `IncidentIQ API`

List asset types (POST)

Returns the catalog of asset types available in the tenant. This POST variant accepts filter parameters in the request body and is functionally equivalent to [GET /api/v1.0/assets/types](#/Assets/listAssetTypes).

**Workflow Example**
1. Call [POST /api/v1.0/assets/types](#/Assets/listAssetTypesPost) with optional filters.
2. Extract `Items[].AssetTypeId` for the desired category.
3. Use the `AssetTypeId` when creating assets via [POST /api/v1.0/assets/new](#/Assets/createAsset) or filtering via [POST /api/v1.0/assets](#/Assets/searchAssets).

**Common Use Cases**
- Populate asset type dropdowns in forms
- Filter assets by category in reports
- Bootstrap data for asset import workflows

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index to retrieve |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of records per page |
| `body` | `body` | `body` | `no` | `GetAssetTypesRequest` | `GetAssetTypesRequest` | - |

#### Returns

- Typed call return: `AssetTypeListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetTypeListResponse`
- Pagination helper: `client.assets.list_asset_types_post.iter_pages(start_page=1, page_size=100, max_pages=None, p=None, s=None, body=None, timeout=None)`

---

### `list_asset_views`

Provenance: Golden OpenAPI contract

Operation ID: `listAssetViews`

- Sync: `client.assets.list_asset_views(p=None, s=None, timeout=None)`
- Async: `await client.assets.list_asset_views(p=None, s=None, timeout=None)`
- Raw payload: `client.assets.list_asset_views.raw(p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v1.0/assets/views`
- Source controller: `IncidentIQ API`

List asset views

Returns the saved asset views available to the authenticated user, including view identifiers needed to load, update, or delete a specific view. Use this to populate view selectors and discover shared layouts.

**Workflow Example**
1. [GET /api/v1.0/assets/views](#/Assets/listAssetViews) to list available views.
2. Use `Items[].ViewId` to load a specific view with [GET /api/v1.0/assets/views/{viewId}](#/Assets/getAssetView) or to update/delete it.

**Minimal Required Fields**: none.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index. Defaults to 0 when omitted. |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of records per page. Defaults to 100 when omitted. |

#### Returns

- Typed call return: `ViewListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ViewListResponse`
- Pagination helper: `client.assets.list_asset_views.iter_pages(start_page=1, page_size=100, max_pages=None, p=None, s=None, timeout=None)`

---

### `list_assets_by_room`

Provenance: Golden OpenAPI contract

Operation ID: `listAssetsByRoom`

- Sync: `client.assets.list_assets_by_room(location_room_id=..., p=None, s=None, client=None, timeout=None)`
- Async: `await client.assets.list_assets_by_room(location_room_id=..., p=None, s=None, client=None, timeout=None)`
- Raw payload: `client.assets.list_assets_by_room.raw(location_room_id=..., p=None, s=None, client=None, timeout=None)`
- HTTP route: `GET /api/v1.0/assets/rooms/{locationRoomId}`
- Source controller: `IncidentIQ API`

List room assets

Returns the devices that are currently assigned to a specific location room so technicians can audit equipment before submitting a ticket or scheduling maintenance.

**Prerequisites**
1. **locationId** - Use [GET /api/v2.0/locations/view](#/Locations/getMyLocationsViewV2) to identify the campus that owns the room.
2. **locationRoomId** - Call [POST /api/v2.0/locations/{locationId}/rooms](#/Locations/queryLocationRoomsByLocationId) and capture `Items[].LocationRoomId` for the room where the devices reside.

**Workflow Example**
1. Discover locations: [GET /api/v2.0/locations/view](#/Locations/getMyLocationsViewV2) and pick the `LocationId` for your target school.
2. List rooms: [POST /api/v2.0/locations/{locationId}/rooms](#/Locations/queryLocationRoomsByLocationId) and filter to your target room, then capture its `LocationRoomId`.
3. Retrieve assets: [GET /api/v1.0/assets/rooms/{locationRoomId}](#/Assets/listAssetsByRoom) to review all devices staged in that space before creating a ticket or updating stock records.

**Minimal Required Fields**: `locationRoomId` (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `location_room_id` | `locationRoomId` | `path` | `yes` | `str` | `-` | UUID of the location room whose devices should be returned. Obtain from GET /api/v1.0/locations/{locationId}/rooms and read `Items[].LocationRoomId`. |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index to retrieve |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of records per page |
| `client` | `Client` | `header` | `no` | `str` | `-` | Identifies the caller platform for analytics (for example `IncidentIQ-Web` or `incidentiq-api-client`). |

#### Returns

- Typed call return: `AssetSearchResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetSearchResponse`
- Pagination helper: `client.assets.list_assets_by_room.iter_pages(start_page=1, page_size=100, max_pages=None, location_room_id=..., p=None, s=None, client=None, timeout=None)`

---

### `list_assets_by_storage_unit`

Provenance: Golden OpenAPI contract

Operation ID: `listAssetsByStorageUnit`

- Sync: `client.assets.list_assets_by_storage_unit(location_id=..., storage_unit_number=..., p=None, s=None, timeout=None)`
- Async: `await client.assets.list_assets_by_storage_unit(location_id=..., storage_unit_number=..., p=None, s=None, timeout=None)`
- Raw payload: `client.assets.list_assets_by_storage_unit.raw(location_id=..., storage_unit_number=..., p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v1.0/assets/storageunit/{locationId}/{storageUnitNumber}`
- Source controller: `IncidentIQ API`

List assets by storage unit

Returns the devices currently assigned to a specific storage unit within a given location. The lookup is case-insensitive, sorts by `ModelName` ascending, and defaults to 500 assets per page via the shared `$p` / `$s` paging parameters.

**Prerequisites**
1. **locationId** - Use [GET /api/v2.0/locations/view](#/Locations/getMyLocationsViewV2) to enumerate campuses or warehouses and capture `Items[].LocationId` for the storage facility.
2. **storageUnitNumber** - Run [POST /api/v1.0/assets](#/Assets/searchAssets) with a location filter (or reference the labeled cart/bin in the facility) and read `Items[].StorageUnitNumber` to confirm the unit identifier recorded in Incident IQ.

**Workflow Example**
1. List the available locations: [GET /api/v2.0/locations/view](#/Locations/getMyLocationsViewV2) and record the `LocationId` for your target warehouse.
2. Inspect inventory in that location: [POST /api/v1.0/assets](#/Assets/searchAssets) with a `location` facet to discover existing unit numbers.
3. Retrieve the manifest for the unit: [GET /api/v1.0/assets/storageunit/{locationId}/{storageUnitNumber}](#/Assets/listAssetsByStorageUnit) to page through every asset staged in that storage cart or cabinet.

**Minimal Required Fields**: locationId, storageUnitNumber (path). Requires standard Incident IQ authentication (user tokens or application access keys).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `location_id` | `locationId` | `path` | `yes` | `str` | `-` | UUID of the location where the storage unit exists. Obtain via [GET /api/v2.0/locations](#/Locations/getMyLocationsV2) and extract `Items[].LocationId` for the warehouse, campus, or room. |
| `storage_unit_number` | `storageUnitNumber` | `path` | `yes` | `str` | `-` | Label or number assigned to the storage unit (cart, locker, bin, etc.). Case-insensitive. Capture it from [POST /api/v1.0/assets](#/Assets/searchAssets) by filtering on the location and reading `Items[].StorageUnitNumber`, or reference the value etched onto the cabinet. |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index. Defaults to 0 when omitted. |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of records per page. Defaults to 500. |

#### Returns

- Typed call return: `AssetSearchResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetSearchResponse`
- Pagination helper: `client.assets.list_assets_by_storage_unit.iter_pages(start_page=1, page_size=100, max_pages=None, location_id=..., storage_unit_number=..., p=None, s=None, timeout=None)`

---

### `merge_assets`

Provenance: Golden OpenAPI contract

Operation ID: `mergeAssets`

- Sync: `client.assets.merge_assets(slave_asset_id=..., master_asset_id=..., timeout=None)`
- Async: `await client.assets.merge_assets(slave_asset_id=..., master_asset_id=..., timeout=None)`
- Raw payload: `client.assets.merge_assets.raw(slave_asset_id=..., master_asset_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/merge/{slaveAssetId}/into/{masterAssetId}`
- Source controller: `IncidentIQ API`

Merge assets

Merges a secondary (slave) asset into a primary (master) asset. The slave asset is retired and its history is consolidated into the master.

**Use Cases:**
- Consolidate duplicate asset records
- Merge asset data after MDM synchronization conflicts
- Combine asset histories when replacing components

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `slave_asset_id` | `slaveAssetId` | `path` | `yes` | `str` | `-` | UUID of the asset to merge from (will be retired). Obtain via [POST /api/v1.0/assets](#/Assets/searchAssets), extract `Items[].AssetId` from response. |
| `master_asset_id` | `masterAssetId` | `path` | `yes` | `str` | `-` | UUID of the asset to merge into (will be retained). Obtain via [POST /api/v1.0/assets](#/Assets/searchAssets), extract `Items[].AssetId` from response. |

#### Returns

- Typed call return: `AssetItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `query_asset_changes`

Provenance: Golden OpenAPI contract

Operation ID: `queryAssetChanges`

- Sync: `client.assets.query_asset_changes(body=None, timeout=None)`
- Async: `await client.assets.query_asset_changes(body=None, timeout=None)`
- Raw payload: `client.assets.query_asset_changes.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/assets/changes/query`
- Source controller: `IncidentIQ API`

Query asset change history

Retrieves asset change history records based on optional filters such as asset ID, date range, or change type. Use this endpoint to audit modifications, power activity timelines, or track updates to key fields like ownership and status.

**Workflow Example**
1. Submit [POST /api/v1.0/assets/changes/query](#/Assets/queryAssetChanges) with an `AssetId` to retrieve recent changes.
2. Inspect `Items[].AssetChangeId` and call [GET /api/v1.0/assets/changes/{assetChangeId}](#/Assets/getAssetChange) for detailed change payloads.

**Minimal Required Fields**: none. Provide filters to scope the change history.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `GetAssetChangesRequest` | `GetAssetChangesRequest` | - |

#### Returns

- Typed call return: `AssetChangeListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetChangeListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `remove_asset_favorite`

Provenance: Golden OpenAPI contract

Operation ID: `removeAssetFavorite`

- Sync: `client.assets.remove_asset_favorite(asset_id=..., user_id=..., timeout=None)`
- Async: `await client.assets.remove_asset_favorite(asset_id=..., user_id=..., timeout=None)`
- Raw payload: `client.assets.remove_asset_favorite.raw(asset_id=..., user_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/favorites/remove/{assetId}/{userId}`
- Source controller: `IncidentIQ API`

Remove asset from favorites

Removes an asset from a user's favorites collection. The asset will no longer appear in quick-access views or ticket shortcuts for that user.

**Prerequisites**
1. **assetId** - Call [GET /api/v1.0/assets/favorites/{userId}](#/Assets/getUserFavoriteAssets) to view current favorites and select the `AssetId` to remove.
2. **userId** - Call [POST /api/v1.0/search](#/Search/globalSearch) with the user identifier and capture `Item.Users[].UserId`.

**Workflow Example**
1. List user's favorites: [GET /api/v1.0/assets/favorites/{userId}](#/Assets/getUserFavoriteAssets) to see current favorites.
2. Call [POST /api/v1.0/assets/favorites/remove/{assetId}/{userId}](#/Assets/removeAssetFavorite) to remove the selected asset.

**Minimal Required Fields**
- `assetId` (path) - The asset to remove from favorites.
- `userId` (path) - The user whose favorite list is being updated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_id` | `assetId` | `path` | `yes` | `str` | `-` | UUID of the asset to remove from favorites. Obtain via [POST /api/v1.0/assets](#/Assets/searchAssets), extract `Items[].AssetId` from response. |
| `user_id` | `userId` | `path` | `yes` | `str` | `-` | UUID of the user whose favorites are being updated. Obtain with POST /api/v1.0/search and read `Item.Users[].UserId`. |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `remove_asset_owner`

Provenance: Golden OpenAPI contract

Operation ID: `removeAssetOwner`

- Sync: `client.assets.remove_asset_owner(asset_id=..., force=None, timeout=None)`
- Async: `await client.assets.remove_asset_owner(asset_id=..., force=None, timeout=None)`
- Raw payload: `client.assets.remove_asset_owner.raw(asset_id=..., force=None, timeout=None)`
- HTTP route: `POST /api/v1.0/assets/{assetId}/remove-owner`
- Source controller: `IncidentIQ API`

Remove asset owner

Clears ownership from an asset, making it unassigned. Use this when reclaiming a device, preparing it for reassignment, or removing a stale assignment after a return.

**Prerequisites**
1. **assetId** - Locate the asset via [POST /api/v1.0/assets](#/Assets/searchAssets) or [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById).

**Workflow Example**
1. Confirm the asset record and current owner.
2. [POST /api/v1.0/assets/{assetId}/remove-owner](#/Assets/removeAssetOwner) to clear the ownership link.
3. Optionally set `force=true` to bypass read-only and ownership checks.

**Minimal Required Fields**: `assetId` (path).

**Alternative Path**: `/api/v1.0/assets/{assetId}/remove-owner/{force}` where `force` is a boolean path parameter.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_id` | `assetId` | `path` | `yes` | `str` | `-` | UUID of the asset. Obtain via [POST /api/v1.0/assets](#/Assets/searchAssets), extract `Items[].AssetId` from response. |
| `force` | `force` | `query` | `no` | `bool` | `-` | When true, bypasses ownership checks and read-only asset restrictions. Default is false. |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `remove_manufacturer_from_site`

Provenance: Golden OpenAPI contract

Operation ID: `removeManufacturerFromSite`

- Sync: `client.assets.remove_manufacturer_from_site(manufacturer_id=..., timeout=None)`
- Async: `await client.assets.remove_manufacturer_from_site(manufacturer_id=..., timeout=None)`
- Raw payload: `client.assets.remove_manufacturer_from_site.raw(manufacturer_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/assets/manufacturers/{ManufacturerId}/site`
- Source controller: `IncidentIQ API`

Remove manufacturer from site

Removes a manufacturer's visibility from the current site. The manufacturer remains in the global catalog but will no longer appear in this site's manufacturer lists or be available for new asset creation.

**Prerequisites**
1. **ManufacturerId** - Use [GET /api/v1.0/assets/manufacturers](#/Manufacturers/getManufacturers) to list manufacturers at the current site. Extract `Items[].ManufacturerId`.

**Workflow Example**
1. List site manufacturers: [GET /api/v1.0/assets/manufacturers](#/Manufacturers/getManufacturers) → identify target.
2. Remove from site: [DELETE /api/v1.0/assets/manufacturers/{ManufacturerId}/site](#/Manufacturers/removeManufacturerFromSite).

**Notes**: Existing assets referencing this manufacturer are not affected. To permanently delete a manufacturer, use [DELETE /api/v1.0/assets/manufacturers/{ManufacturerId}](#/Manufacturers/deleteManufacturer) instead.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `manufacturer_id` | `ManufacturerId` | `path` | `yes` | `str` | `-` | Unique identifier of the manufacturer to remove from the site |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `remove_user_asset`

Provenance: Golden OpenAPI contract

Operation ID: `removeUserAsset`

- Sync: `client.assets.remove_user_asset(asset_id=..., user_id=..., timeout=None)`
- Async: `await client.assets.remove_user_asset(asset_id=..., user_id=..., timeout=None)`
- Raw payload: `client.assets.remove_user_asset.raw(asset_id=..., user_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/assets/{assetId}/for/{userId}`
- Source controller: `IncidentIQ API`

Remove asset from user

Removes an asset from a user's profile, unlinking the asset from the specified user. Use this when transferring ownership or reclaiming devices.

**Prerequisites**
1. **assetId** - Use [POST /api/v1.0/assets](#/Assets/searchAssets) to identify the asset.
2. **userId** - Use [POST /api/v1.0/search](#/Users/searchUsers) to find the user.

**Workflow Example**
1. Search for user's assets: [GET /api/v1.0/assets/for/{userId}](#/Assets/getAssetsForUserCurrent).
2. Identify the asset to remove.
3. [DELETE /api/v1.0/assets/{assetId}/for/{userId}](#/Assets/removeUserAsset) to unlink.

**Minimal Required Fields**: `assetId`, `userId` (path parameters).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_id` | `assetId` | `path` | `yes` | `str` | `-` | UUID of the asset to remove from the user. Obtain via [POST /api/v1.0/assets](#/Assets/searchAssets), extract `Items[].AssetId` from response. |
| `user_id` | `userId` | `path` | `yes` | `str` | `-` | UUID of the user to remove the asset from. Obtain via [POST /api/v1.0/users](#/Users/searchUsers), extract `Items[].UserId` from response. |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `search_asset_verifications`

Provenance: Golden OpenAPI contract

Operation ID: `searchAssetVerifications`

- Sync: `client.assets.search_asset_verifications(body=..., timeout=None)`
- Async: `await client.assets.search_asset_verifications(body=..., timeout=None)`
- Raw payload: `client.assets.search_asset_verifications.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/verifications`
- Source controller: `IncidentIQ API`

Search asset verifications

Queries asset verification records based on asset IDs and filter criteria. Use this to retrieve audit history for compliance reporting or to view all verifications for a set of assets.

**Workflow Example**
1. Identify target assets: [POST /api/v1.0/assets](#/Assets/searchAssets) to get `AssetId` values.
2. Query verifications: [POST /api/v1.0/assets/verifications](#/Assets/searchAssetVerifications) with `AssetIds` array.
3. Review individual records with [GET /api/v1.0/assets/verifications/{assetVerificationId}](#/Assets/getAssetVerificationById).

**Minimal Required Fields**: none (empty request returns all verifications).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `GetAssetVerificationsRequest` | `GetAssetVerificationsRequest` | - |

#### Returns

- Typed call return: `AssetVerificationListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetVerificationListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `search_assets`

Provenance: Golden OpenAPI contract

Operation ID: `searchAssets`

- Sync: `client.assets.search_assets(p=None, s=None, body=..., timeout=None)`
- Async: `await client.assets.search_assets(p=None, s=None, body=..., timeout=None)`
- Raw payload: `client.assets.search_assets.raw(p=None, s=None, body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets`
- Source controller: `IncidentIQ API`

Search assets

Searches and filters asset records based on specified criteria. This endpoint supports advanced querying capabilities for device and equipment inventory management. Search assets by tag, serial number, model, location, or assigned user. Returns a paginated list of matching asset records with their complete details.

**Filter Facet System**

This endpoint uses the universal `FilterMatch` pattern shared across Tickets, Assets, and Users search endpoints. Assets support **75 filter facets** organized into categories:

- **Asset Identity**: `asset`, `assettag`, `assetserialnumber`, `assetname`, `assettype`
- **Ownership**: `user`, `previousowner`, `previousownerlocation`, `previousownerrole`, `previousownergrade`
- **Location**: `location`, `locationtype`, `room`, `assetstoragelocation`, `assetstorageunit`
- **Status/Workflow**: `assetstatus`, `assetauditstatus`, `assetauditstatusbyPolicy`
- **Model/Category**: `model`, `modelcategory`, `manufacturer`
- **Financials**: `purchasedprice`, `currentbookvalue`, `totalassetcost`, `totallaborcost`, `inventoryusedtotalcost` (use `NumericExpressionSyntax`)
- **Dates**: `createddate`, `modifieddate`, `purchaseddate`, `deployeddate`, `retireddate`, `warrantyexpirationdate`, `endoflifedate` (use `DateExpressionSyntax`)
- **Verification**: `verificationdate`, `assetlastverificationstatus`, `assetlastverificationlocation`, `assetlastverificationuser`
- **Custom Fields**: `assetcustomfield`, `assetattribute`, `usercustomfield`, `locationcustomfield`
- **Duplicates**: `assetduplicateany`, `assetduplicateassettag`, `assetduplicateserialnumber`

See the `AssetSearchFilter` schema for the complete `x-facet-definitions` reference documenting all 75 facets with their required fields.

**Filter Expression Syntax**
- **Date facets**: Use `DateExpressionSyntax` - supports comparison operators (`date>=MM/DD/YYYY`, `date<=MM/DD/YYYY`), explicit ranges (`daterange:MM/DD/YYYY-MM/DD/YYYY`), and relative ranges (`range:today`, `range:thisweek`, `range:lastdays:30`).
- **Numeric facets**: Use `NumericExpressionSyntax` - format is `numoperator:<operator>:<value>` where operator is `equals`, `lessthan`, `lessthanequal`, `greaterthan`, or `greaterthanequal`.
- **Keyword/text**: Simple `Value` field for searching asset tags, serial numbers, names.
- **Entity references**: Use `Id` field with UUID (asset type, status, location, model, user).

**Prerequisites**:
- To filter by `assettype`, you need the `AssetTypeId`. Use [GET /api/v1.0/assets/types](#/Assets/listAssetTypes) to retrieve available asset types.
- To filter by `assetstatus`, you need the `StatusTypeId`. Use [GET /api/v1.0/assets/statuses](#/Assets/getAssetStatusType) or find it in the `Status` object of an existing asset.
- To filter by `location`, use [GET /api/v2.0/locations/view](#/Locations/getMyLocationsViewV2) to retrieve `LocationId` values.
- To filter by `model`, use [POST /api/v1.0/models](#/Assets/searchAssets) to search for models.
- Call [GET /api/v1.0/filters/for/entitytype/{entityTypeId}](#/Filters/listFiltersForEntityType) with entity type `888891ac-91aa-e711-80c2-100dffa00002` to enumerate all available asset filter keys.

**Pagination and sorting**
- Use `$p` (zero-based page index) and `$s` (page size) query parameters to page through results.
- The response `Paging` object provides `PageIndex`, `PageSize`, `PageCount`, and `TotalRows` for navigation.

**Performance considerations**
- Begin searches with narrow filter combinations (asset type + status + location) to avoid scanning the entire inventory.
- Cache supporting metadata (asset types, statuses, locations, models) rather than issuing lookups per request.
- Use moderate page sizes (25–50) for optimal response times.

**Workflow Example**:
1. **Get Asset Types**: Call [GET /api/v1.0/assets/types](#/Assets/listAssetTypes) to get a list of asset types. Note the `AssetTypeId` for 'Devices'.
2. **Search Assets**: Call [POST /api/v1.0/assets](#/Assets/searchAssets) with a filter for the `AssetTypeId` to get all devices.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index to retrieve |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of records per page |
| `body` | `body` | `body` | `yes` | `AssetSearchRequest` | `AssetSearchRequest` | - |

#### Returns

- Typed call return: `AssetSearchResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetSearchResponse`
- Pagination helper: `client.assets.search_assets.iter_pages(start_page=1, page_size=100, max_pages=None, p=None, s=None, body=..., timeout=None)`

---

### `search_assets_by_serial`

Provenance: Golden OpenAPI contract

Operation ID: `searchAssetsBySerial`

- Sync: `client.assets.search_assets_by_serial(serial=..., p=None, s=None, timeout=None)`
- Async: `await client.assets.search_assets_by_serial(serial=..., p=None, s=None, timeout=None)`
- Raw payload: `client.assets.search_assets_by_serial.raw(serial=..., p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v1.0/assets/serial/search/{serial}`
- Source controller: `IncidentIQ API`

Search assets by serial

Performs a wildcard search across asset serial numbers using a case-insensitive "contains" match. The service automatically appends a trailing `*` wildcard (SQL LIKE semantics) and sorts ascending by `SerialNumber` with a default page size of 20.

For complex searches (multiple filters, AND/OR groupings) call [POST /api/v1.0/assets](#/Assets/searchAssets) instead.

**Workflow**
1. Capture the serial fragment from a scanner or external inventory export.
2. Call [GET /api/v1.0/assets/serial/search/{serial}](#/Assets/searchAssetsBySerial) to retrieve candidate assets. Adjust `$s` and `$p` to page through larger result sets.
3. Once you have confirmed the exact device, call [GET /api/v1.0/assets/serial/{serial}](#/Assets/getAssetBySerial) for a single-record lookup or [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById) with the returned `AssetId` to fetch the full record for updates or ticketing workflows.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `serial` | `serial` | `path` | `yes` | `str` | `-` | Partial or full serial number text to search for. Search is case-insensitive; serial values in Incident IQ are typically uppercase alphanumeric plus optional hyphens (for example `MT500-234A1000-4300`). Trim whitespace and provide at least 3 characters to avoid overly broad result sets. |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index to retrieve |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of records per page |

#### Returns

- Typed call return: `AssetSearchResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetSearchResponse`
- Pagination helper: `client.assets.search_assets_by_serial.iter_pages(start_page=1, page_size=100, max_pages=None, serial=..., p=None, s=None, timeout=None)`

---

### `search_global_manufacturers`

Provenance: Golden OpenAPI contract

Operation ID: `searchGlobalManufacturers`

- Sync: `client.assets.search_global_manufacturers(body=None, timeout=None)`
- Async: `await client.assets.search_global_manufacturers(body=None, timeout=None)`
- Raw payload: `client.assets.search_global_manufacturers.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/assets/manufacturers/global`
- Source controller: `IncidentIQ API`

Search global manufacturers

Searches globally-scoped manufacturers using filter criteria in the request body. Returns manufacturers available across all sites without site visibility restrictions.

**Workflow Example**
1. Build filter request with `Filters` array and optional `OnlyShowDeleted` flag.
2. Call this endpoint: [POST /api/v1.0/assets/manufacturers/global](#/Manufacturers/searchGlobalManufacturers) with filter criteria.
3. Use results to identify global manufacturers for site enablement.

**Filter Options**
- `OnlyShowDeleted: true` - Returns only deleted/archived global manufacturers
- `Filters` - Array of filter conditions for field-based queries

**Related Endpoints:**
- [GET /api/v1.0/assets/manufacturers/global](#/Manufacturers/getGlobalManufacturers) - Simple list with query parameters
- [POST /api/v1.0/assets/manufacturers/{ManufacturerId}/site](#/Manufacturers/addManufacturerToSite) - Enable a global manufacturer at current site

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `InlineObject` | `InlineObject` | Search and filter parameters |

#### Returns

- Typed call return: `Any`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `search_manufacturers`

Provenance: Golden OpenAPI contract

Operation ID: `searchManufacturers`

- Sync: `client.assets.search_manufacturers(body=None, timeout=None)`
- Async: `await client.assets.search_manufacturers(body=None, timeout=None)`
- Raw payload: `client.assets.search_manufacturers.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/assets/manufacturers`
- Source controller: `IncidentIQ API`

Search manufacturers

Searches manufacturers using filter criteria in the request body. Supports complex filter objects for advanced queries beyond what the GET endpoint provides.

**Workflow Example**
1. Build filter request with `Filters` array and optional `OnlyShowDeleted` flag.
2. Call this endpoint: [POST /api/v1.0/assets/manufacturers](#/Manufacturers/searchManufacturers) with filter criteria.
3. Process paginated results to populate manufacturer selection UI.

**Filter Options**
- `OnlyShowDeleted: true` - Returns only deleted/archived manufacturers
- `Filters` - Array of filter conditions for field-based queries

**Related Endpoints:**
- [GET /api/v1.0/assets/manufacturers](#/Manufacturers/getManufacturers) - Simple list with query parameters
- [POST /api/v1.0/assets/manufacturers/global](#/Manufacturers/searchGlobalManufacturers) - Search global manufacturers only

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `InlineObject` | `InlineObject` | Search and filter parameters |

#### Returns

- Typed call return: `Any`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `set_asset_location`

Provenance: Golden OpenAPI contract

Operation ID: `setAssetLocation`

- Sync: `client.assets.set_asset_location(body=..., timeout=None)`
- Async: `await client.assets.set_asset_location(body=..., timeout=None)`
- Raw payload: `client.assets.set_asset_location.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/location`
- Source controller: `IncidentIQ API`

Set asset location

Updates an asset's location assignment to a specific building, room, or storage area. Can include free-text location details for desk or shelf placement.

**Prerequisites**
1. **AssetId** - Use [POST /api/v1.0/assets](#/Assets/searchAssets) to identify the asset and extract `Items[].AssetId`.
2. **LocationId** - Use [GET /api/v2.0/locations/all/{siteId}](#/Locations/getAllSiteLocationsV2) to get valid location UUIDs.
3. **SiteId** - Use [GET /api/v1.0/sites](#/Sites/getSiteByUrl) if operating across multiple sites.

**Workflow Example**
1. Search for asset: [POST /api/v1.0/assets](#/Assets/searchAssets) with tag or serial filter.
2. Get target location: [GET /api/v2.0/locations/all/{siteId}](#/Locations/getAllSiteLocationsV2).
3. Submit [POST /api/v1.0/assets/location](#/Assets/setAssetLocation) with AssetId and LocationId.

**Minimal Required Fields**: AssetId, LocationId, SiteId

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `SetAssetLocationRequest` | `SetAssetLocationRequest` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `set_asset_owner`

Provenance: Golden OpenAPI contract

Operation ID: `setAssetOwner`

- Sync: `client.assets.set_asset_owner(asset_id=..., body=..., timeout=None)`
- Async: `await client.assets.set_asset_owner(asset_id=..., body=..., timeout=None)`
- Raw payload: `client.assets.set_asset_owner.raw(asset_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/{assetId}/owner`
- Source controller: `IncidentIQ API`

Assign or unassign asset owner

Assigns or removes an owner for a specific asset. Updates the asset's ownership relationship which may trigger checkout workflows and update location based on the new owner.

**Prerequisites**
1. **AssetId** - Use [POST /api/v1.0/assets](#/Assets/searchAssets) to identify the asset and extract `Items[].AssetId`.
2. **OwnerId** - Use [POST /api/v1.0/search](#/Users/searchUsers) to find the user and extract `Item.Users[].UserId`.

**Workflow Example**
1. Search for asset: [POST /api/v1.0/assets](#/Assets/searchAssets) with tag or serial filter.
2. Search for user: [POST /api/v1.0/search](#/Users/searchUsers) with name or email.
3. Submit [POST /api/v1.0/assets/{assetId}/owner](#/Assets/setAssetOwner) with OwnerId to assign ownership.

**Minimal Required Fields**: OwnerId (set to null to unassign)

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_id` | `assetId` | `path` | `yes` | `str` | `-` | UUID of the asset to assign owner to. Obtain via [POST /api/v1.0/assets](#/Assets/searchAssets), extract `Items[].AssetId` from response. |
| `body` | `body` | `body` | `yes` | `SetAssetOwnerRequest` | `SetAssetOwnerRequest` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `set_asset_owner_advanced_deployment_swap`

Provenance: Golden OpenAPI contract

Operation ID: `setAssetOwnerAdvancedDeploymentSwap`

- Sync: `client.assets.set_asset_owner_advanced_deployment_swap(asset_id=..., body=..., timeout=None)`
- Async: `await client.assets.set_asset_owner_advanced_deployment_swap(asset_id=..., body=..., timeout=None)`
- Raw payload: `client.assets.set_asset_owner_advanced_deployment_swap.raw(asset_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/{assetId}/owner/requestor/swap`
- Source controller: `IncidentIQ API`

Swap asset owner via advanced deployment

Sets asset ownership with advanced deployment swap logic. This endpoint is used in scenarios where ownership needs to be transferred as part of an advanced deployment workflow, such as device exchange programs.

**Prerequisites**
1. **assetId** - Use [POST /api/v1.0/assets](#/Assets/searchAssets) to identify the asset and extract `Items[].AssetId`.
2. **OwnerId** - Use [POST /api/v1.0/search](#/Users/searchUsers) to find the user and extract `Item.Users[].UserId`.

**Workflow Example**
1. Search for asset: [POST /api/v1.0/assets](#/Assets/searchAssets) with tag or serial filter.
2. Search for new owner: [POST /api/v1.0/search](#/Users/searchUsers) with name or email.
3. Call [POST /api/v1.0/assets/{assetId}/owner/requestor/swap](#/Assets/setAssetOwnerAdvancedDeploymentSwap) to transfer ownership.

**Minimal Required Fields**: `assetId` (path), `OwnerId` (body).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_id` | `assetId` | `path` | `yes` | `str` | `-` | UUID of the asset for ownership swap. Obtain via [POST /api/v1.0/assets](#/Assets/searchAssets), extract `Items[].AssetId` from response. |
| `body` | `body` | `body` | `yes` | `SetAssetOwnerRequest` | `SetAssetOwnerRequest` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `set_asset_status`

Provenance: Golden OpenAPI contract

Operation ID: `setAssetStatus`

- Sync: `client.assets.set_asset_status(asset_id=..., asset_status_type_id=..., timeout=None)`
- Async: `await client.assets.set_asset_status(asset_id=..., asset_status_type_id=..., timeout=None)`
- Raw payload: `client.assets.set_asset_status.raw(asset_id=..., asset_status_type_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/{assetId}/status/{assetStatusTypeId}`
- Source controller: `IncidentIQ API`

Set asset status

Updates an asset's status to a new status type. Status types control asset lifecycle states like 'In Service', 'In Repair', 'Retired', etc.

**Prerequisites:**
- Get available status types from [POST /api/v1.0/assets](#/Assets/searchAssets) by reading `Items[].Status.AssetStatusTypeId`
- Select the appropriate AssetStatusTypeId

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_id` | `assetId` | `path` | `yes` | `str` | `-` | UUID of the asset to update. Obtain via [POST /api/v1.0/assets](#/Assets/searchAssets), extract `Items[].AssetId` from response. |
| `asset_status_type_id` | `assetStatusTypeId` | `path` | `yes` | `str` | `-` | UUID of the target status type. Obtain via [GET /api/v1.0/assets/statustypes](#/Assets/listAssetStatusTypes), extract `Items[].AssetStatusTypeId` from response. |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `take_asset_ownership`

Provenance: Golden OpenAPI contract

Operation ID: `takeAssetOwnership`

- Sync: `client.assets.take_asset_ownership(asset_id=..., timeout=None)`
- Async: `await client.assets.take_asset_ownership(asset_id=..., timeout=None)`
- Raw payload: `client.assets.take_asset_ownership.raw(asset_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/{assetId}/take-ownership`
- Source controller: `IncidentIQ API`

Take ownership of asset

Assigns the current authenticated user as the owner of the specified asset. This is a convenience endpoint that automatically uses the caller's user ID as the new owner.

**Prerequisites**
1. **assetId** - Use [POST /api/v1.0/assets](#/Assets/searchAssets) to identify the asset and extract `Items[].AssetId`.

**Workflow Example**
1. Search for asset: [POST /api/v1.0/assets](#/Assets/searchAssets) with tag or serial filter.
2. Call [POST /api/v1.0/assets/{assetId}/take-ownership](#/Assets/takeAssetOwnership) to claim the asset.

**Minimal Required Fields**: `assetId` (path only - no request body needed).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_id` | `assetId` | `path` | `yes` | `str` | `-` | UUID of the asset to take ownership of. Obtain via [POST /api/v1.0/assets](#/Assets/searchAssets), extract `Items[].AssetId` from response. |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `undelete_asset`

Provenance: Golden OpenAPI contract

Operation ID: `undeleteAsset`

- Sync: `client.assets.undelete_asset(asset_id=..., timeout=None)`
- Async: `await client.assets.undelete_asset(asset_id=..., timeout=None)`
- Raw payload: `client.assets.undelete_asset.raw(asset_id=..., timeout=None)`
- HTTP route: `PUT /api/v1.0/assets/{assetId}/undelete`
- Source controller: `IncidentIQ API`

Restore deleted asset

Restores a soft-deleted asset back to active status so it appears in normal inventory searches again. Use this when a deletion was accidental or when a device should be reinstated.

**Prerequisites**
1. **assetId** - Capture the asset identifier from the delete response or locate it via [POST /api/v1.0/assets/](#/Assets/searchAssets) with deleted filters enabled.

**Workflow Example**
1. Identify the deleted asset and confirm it should be restored.
2. [PUT /api/v1.0/assets/{assetId}/undelete](#/Assets/undeleteAsset) to restore the record.
3. Reopen the asset details with [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById) to verify status.

**Minimal Required Fields**: `assetId` (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_id` | `assetId` | `path` | `yes` | `str` | `-` | UUID of the deleted asset to restore. Obtain via [POST /api/v1.0/assets](#/Assets/searchAssets) with `OnlyShowDeleted: true`, extract `Items[].AssetId` from response. |

#### Returns

- Typed call return: `AssetItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `undo_asset_exchange_transaction`

Provenance: Golden OpenAPI contract

Operation ID: `undoAssetExchangeTransaction`

- Sync: `client.assets.undo_asset_exchange_transaction(body=..., timeout=None)`
- Async: `await client.assets.undo_asset_exchange_transaction(body=..., timeout=None)`
- Raw payload: `client.assets.undo_asset_exchange_transaction.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/checkouts/undo-exchange-transaction`
- Source controller: `IncidentIQ API`

Undo checkout transaction

Reverses a previously recorded checkout or check-in transaction. Use this when a transaction was recorded in error and you need to roll back the inventory movement without creating a compensating entry.

**Prerequisites**
1. **AssetCheckoutId + ExchangeActionId** - Identify the transaction via [POST /api/v1.0/assets/checkouts/transactions/query/get](#/Assets/getAssetCheckoutTransactions) or from the checkout/transfer response payload.

**Workflow Example**
1. Locate the erroneous transaction and record its identifiers.
2. [POST /api/v1.0/assets/checkouts/undo-exchange-transaction](#/Assets/undoAssetExchangeTransaction) with the identifiers to reverse it.

**Minimal Required Fields**: `AssetCheckoutId`, `ExchangeActionId` (request body).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `AssetExchangeTransactionDto` | `AssetExchangeTransactionDto` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_asset`

Provenance: Golden OpenAPI contract

Operation ID: `updateAsset`

- Sync: `client.assets.update_asset(asset_id=..., api_flags=None, body=..., timeout=None)`
- Async: `await client.assets.update_asset(asset_id=..., api_flags=None, body=..., timeout=None)`
- Raw payload: `client.assets.update_asset.raw(asset_id=..., api_flags=None, body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/{assetId}`
- Source controller: `IncidentIQ API`

Update asset

Updates an existing device record, including metadata such as owner, location, warranty details, or custom fields.

By default the API expects a fully hydrated asset payload because unspecified fields are overwritten with defaults during mapping. To send a true partial update, include the header `ApiFlags: OnlySetMappedProperties`; when this flag is present only the fields provided in the body are modified and the rest of the record remains untouched.

**Prerequisites**
1. **assetId** - Locate the device via [POST /api/v1.0/assets](#/Assets/searchAssets) or load the record with [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById) and capture `Items[].AssetId`.
2. **Related references** - When changing owners, models, or locations, retrieve valid identifiers from the respective catalog endpoints (e.g., [POST /api/v1.0/search](#/Search/globalSearch) for users or [GET /api/v2.0/locations/view](#/Locations/getMyLocationsViewV2) for campuses).

**Workflow Example**
1. Inspect the current record: [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById) to review owner, location, and custom field values.
2. Prepare the payload with the fields to change (e.g., `OwnerId`, `LocationId`, `StatusTypeId`, `CustomFieldValues`).
3. For partial updates send the header `ApiFlags: OnlySetMappedProperties` so only the supplied fields are mutated.
4. [POST /api/v1.0/assets/{assetId}](#/Assets/updateAsset) with the request body to persist the changes and receive the updated asset in the response envelope.

**Minimal Required Fields**: `assetId` (path) plus at least one mutable property in the request body (OwnerId, LocationId, AssetTag, StatusTypeId, CustomFieldValues, etc.).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_id` | `assetId` | `path` | `yes` | `str` | `-` | UUID of the asset to update. Obtain from [POST /api/v1.0/assets](#/Assets/searchAssets) (`Items[].AssetId`) or [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById). |
| `api_flags` | `ApiFlags` | `header` | `no` | `str` | `-` | Optional flag to control update behavior. When set to `OnlySetMappedProperties`, only fields explicitly included in the request payload will be updated; fields omitted from the payload will retain their existing values instead of being overwritten with null or default values. This enables true partial updates without resubmitting the entire asset payload. |
| `body` | `body` | `body` | `yes` | `AssetUpdateRequest` | `AssetUpdateRequest` | - |

#### Returns

- Typed call return: `AssetUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_asset_checkouts_by_ids`

Provenance: Golden OpenAPI contract

Operation ID: `updateAssetCheckoutsByIds`

- Sync: `client.assets.update_asset_checkouts_by_ids(body=..., timeout=None)`
- Async: `await client.assets.update_asset_checkouts_by_ids(body=..., timeout=None)`
- Raw payload: `client.assets.update_asset_checkouts_by_ids.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/checkouts/ids/update`
- Source controller: `IncidentIQ API`

Bulk update checkouts by IDs

Updates specific checkout records identified by their IDs. Use this when you have a known list of checkout records that need targeted updates without running a broader query.

**Prerequisites**
1. **AssetCheckoutIds** - Collect from [POST /api/v1.0/assets/checkouts/query/get](#/Assets/getAssetCheckoutsByQuery) or [POST /api/v1.0/assets/checkouts/transactions/query/get](#/Assets/getAssetCheckoutTransactions).

**Workflow Example**
1. Gather the checkout IDs requiring updates.
2. [POST /api/v1.0/assets/checkouts/ids/update](#/Assets/updateAssetCheckoutsByIds) with an array of update objects including `AssetCheckoutId` and the fields to change.

**Minimal Required Fields**: request body array entries that include `AssetCheckoutId` plus the fields to update.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `UpdateAssetCheckoutsByIdsRequest` | `UpdateAssetCheckoutsByIdsRequest` | - |

#### Returns

- Typed call return: `BulkAssetCheckoutUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `BulkAssetCheckoutUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_asset_checkouts_by_query`

Provenance: Golden OpenAPI contract

Operation ID: `updateAssetCheckoutsByQuery`

- Sync: `client.assets.update_asset_checkouts_by_query(body=..., timeout=None)`
- Async: `await client.assets.update_asset_checkouts_by_query(body=..., timeout=None)`
- Raw payload: `client.assets.update_asset_checkouts_by_query.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/checkouts/query/update`
- Source controller: `IncidentIQ API`

Bulk update checkouts by query

Applies updates to all checkout records matching the provided filters. Use this to extend due dates, update status fields, or apply policy changes across many checkouts in one operation.

**Prerequisites**
1. Build filter criteria using [POST /api/v1.0/assets/checkouts/query/get](#/Assets/getAssetCheckoutsByQuery) to validate which records will be affected.

**Workflow Example**
1. Preview the target set: [POST /api/v1.0/assets/checkouts/query/get](#/Assets/getAssetCheckoutsByQuery) with filters for the population.
2. [POST /api/v1.0/assets/checkouts/query/update](#/Assets/updateAssetCheckoutsByQuery) with the same filters and an `Update` payload to apply changes.

**Minimal Required Fields**: `Update` (request body). Filters are optional but recommended to avoid mass updates.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `UpdateAssetCheckoutsRequest` | `UpdateAssetCheckoutsRequest` | - |

#### Returns

- Typed call return: `BulkAssetCheckoutUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `BulkAssetCheckoutUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_asset_exchange_transaction`

Provenance: Golden OpenAPI contract

Operation ID: `updateAssetExchangeTransaction`

- Sync: `client.assets.update_asset_exchange_transaction(body=..., timeout=None)`
- Async: `await client.assets.update_asset_exchange_transaction(body=..., timeout=None)`
- Raw payload: `client.assets.update_asset_exchange_transaction.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/checkouts/update-exchange-transaction`
- Source controller: `IncidentIQ API`

Update checkout transaction

Updates quantities, due dates, or status adjustments for an existing checkout/check-in transaction. Use this to correct data entry mistakes or extend a loan without reissuing a new checkout record.

**Prerequisites**
1. **AssetCheckoutId + ExchangeActionId** - Obtain identifiers from [POST /api/v1.0/assets/checkouts/transactions/query/get](#/Assets/getAssetCheckoutTransactions) or the response from a checkout/transfer operation.

**Workflow Example**
1. Query recent transactions to find the transaction identifiers.
2. [POST /api/v1.0/assets/checkouts/update-exchange-transaction](#/Assets/updateAssetExchangeTransaction) with the identifiers and updated fields (for example `CheckoutDueDate`).

**Minimal Required Fields**: `AssetCheckoutId`, `ExchangeActionId` (request body).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `UpdateAssetExchangeTransactionRequest` | `UpdateAssetExchangeTransactionRequest` | - |

#### Returns

- Typed call return: `AssetExchangeTransactionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetExchangeTransactionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_asset_type`

Provenance: Golden OpenAPI contract

Operation ID: `updateAssetType`

- Sync: `client.assets.update_asset_type(asset_type_id=..., timeout=None)`
- Async: `await client.assets.update_asset_type(asset_type_id=..., timeout=None)`
- Raw payload: `client.assets.update_asset_type.raw(asset_type_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/types/{assetTypeId}`
- Source controller: `IncidentIQ API`

Update Asset Type

Updates an existing asset with new information. This endpoint modifies asset properties while preserving its identity and relationships. Updates can modify asset details, status, location, and assignments. Returns the updated asset with all current field values. 

**Prerequisites**: Asset operations may require location IDs, user IDs for assignments, and model/type information. Use search endpoints to obtain these identifiers.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_type_id` | `assetTypeId` | `path` | `yes` | `str` | `-` | UUID of the asset type to update. Obtain from [GET /api/v1.0/assets/types](#/Assets/listAssetTypes) (`Items[].AssetTypeId`). |

#### Returns

- Typed call return: `GenericObject`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `GenericObject`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_asset_view`

Provenance: Golden OpenAPI contract

Operation ID: `updateAssetView`

- Sync: `client.assets.update_asset_view(view_id=..., body=..., timeout=None)`
- Async: `await client.assets.update_asset_view(view_id=..., body=..., timeout=None)`
- Raw payload: `client.assets.update_asset_view.raw(view_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/views/{viewId}`
- Source controller: `IncidentIQ API`

Update asset view

Updates an existing asset view definition. If the view does not exist, the API creates it using the supplied definition. Use this to adjust columns, filters, or sorting for a saved asset grid layout.

**Prerequisites**
1. **viewId** - Obtain from [GET /api/v1.0/assets/views](#/Assets/listAssetViews).

**Workflow Example**
1. Load the existing view definition: [GET /api/v1.0/assets/views/{viewId}](#/Assets/getAssetView).
2. Update the `ViewDefinition` payload (filters, columns, sort, or name).
3. [POST /api/v1.0/assets/views/{viewId}](#/Assets/updateAssetView) to save the updated layout.

**Minimal Required Fields**: `viewId` (path) and a `ViewDefinition` payload with `Name`, `ViewTypeId`, `SiteId`, `ProductId`, and `UserId`.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `view_id` | `viewId` | `path` | `yes` | `str` | `-` | Identifier of the asset view to update. |
| `body` | `body` | `body` | `yes` | `ViewDefinition` | `ViewDefinition` | - |

#### Returns

- Typed call return: `ViewItemUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ViewItemUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_asset_view_sort`

Provenance: Golden OpenAPI contract

Operation ID: `updateAssetViewSort`

- Sync: `client.assets.update_asset_view_sort(view_id=..., body=..., timeout=None)`
- Async: `await client.assets.update_asset_view_sort(view_id=..., body=..., timeout=None)`
- Raw payload: `client.assets.update_asset_view_sort.raw(view_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/views/{viewId}/sort`
- Source controller: `IncidentIQ API`

Update asset view sort

Updates the sort configuration for an asset view so the grid loads in a consistent order. This updates only the sort metadata without changing filters or columns.

**Prerequisites**
1. **viewId** - Obtain from [GET /api/v1.0/assets/views](#/Assets/listAssetViews) or [GET /api/v1.0/assets/views/{viewId}](#/Assets/getAssetView).

**Workflow Example**
1. Confirm the view to update: [GET /api/v1.0/assets/views](#/Assets/listAssetViews) -> capture `ViewId`.
2. [POST /api/v1.0/assets/views/{viewId}/sort](#/Assets/updateAssetViewSort) with a `ViewSort` payload (`Field`, `Name`, `Direction`).

**Minimal Required Fields**: `viewId` (path), `Field`, `Name`, `Direction`.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `view_id` | `viewId` | `path` | `yes` | `str` | `-` | Identifier of the asset view to update. |
| `body` | `body` | `body` | `yes` | `ViewSort` | `ViewSort` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_manufacturer`

Provenance: Golden OpenAPI contract

Operation ID: `updateManufacturer`

- Sync: `client.assets.update_manufacturer(manufacturer_id=..., body=..., timeout=None)`
- Async: `await client.assets.update_manufacturer(manufacturer_id=..., body=..., timeout=None)`
- Raw payload: `client.assets.update_manufacturer.raw(manufacturer_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/manufacturers/{ManufacturerId}`
- Source controller: `IncidentIQ API`

Update manufacturer

Updates an existing manufacturer's details. Only the fields provided in the request body will be modified.

**Prerequisites**
- **ManufacturerId** - Use [GET /api/v1.0/assets/manufacturers](#/Manufacturers/getManufacturers) to find the manufacturer. Extract `Items[].ManufacturerId`.

**Workflow Example**
1. List manufacturers: [GET /api/v1.0/assets/manufacturers](#/Manufacturers/getManufacturers) → find target manufacturer
2. (Optional) Get current details: [GET /api/v1.0/assets/manufacturers/{ManufacturerId}](#/Manufacturers/getManufacturerById)
3. Update: [POST /api/v1.0/assets/manufacturers/{ManufacturerId}](#/Manufacturers/updateManufacturer) with modified fields

**Updatable Fields**
- `Name` - Manufacturer display name
- `Scope` - "Global" or "Site" (changing scope may require elevated permissions)
- `EsoIsVisible` - Toggle Employee Self-Service portal visibility
- `Icon` - Font Awesome icon class

**Notes**
- Include `ManufacturerId` in the request body matching the path parameter
- Changing a manufacturer's name does not affect existing assets or models referencing it
- Scope changes may affect visibility at other sites

**Related Endpoints**
- [GET /api/v1.0/assets/manufacturers/{ManufacturerId}](#/Manufacturers/getManufacturerById) - Get current manufacturer details
- [DELETE /api/v1.0/assets/manufacturers/{ManufacturerId}](#/Manufacturers/deleteManufacturer) - Delete manufacturer

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `manufacturer_id` | `ManufacturerId` | `path` | `yes` | `str` | `-` | Unique identifier of the manufacturer to update |
| `body` | `body` | `body` | `yes` | `UpdateManufacturerRequest` | `UpdateManufacturerRequest` | Manufacturer data to update |

#### Returns

- Typed call return: `Any`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_my_classes_asset_verification`

Provenance: Golden OpenAPI contract

Operation ID: `updateMyClassesAssetVerification`

- Sync: `client.assets.update_my_classes_asset_verification(asset_verification_id=..., body=..., timeout=None)`
- Async: `await client.assets.update_my_classes_asset_verification(asset_verification_id=..., body=..., timeout=None)`
- Raw payload: `client.assets.update_my_classes_asset_verification.raw(asset_verification_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/my-classes/verifications/{assetVerificationId}`
- Source controller: `IncidentIQ API`

Update My Classes verification

Updates an existing asset verification within the My Classes context. This variant applies My Classes-specific business rules and permissions.

**Prerequisites**
1. **assetVerificationId** - Existing verification ID from My Classes workflow.

**Workflow Example**
1. Load existing My Classes verification.
2. Modify fields and submit: [POST /api/v1.0/assets/my-classes/verifications/{assetVerificationId}](#/Assets/updateMyClassesAssetVerification).

**Minimal Required Fields**: `assetVerificationId` (path), updated fields in body.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_verification_id` | `assetVerificationId` | `path` | `yes` | `str` | `-` | UUID of the verification record to update |
| `body` | `body` | `body` | `yes` | `UpdateAssetVerificationRequest` | `UpdateAssetVerificationRequest` | - |

#### Returns

- Typed call return: `AssetVerificationItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetVerificationItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
