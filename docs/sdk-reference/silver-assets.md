# `silver.assets` Namespace

Sync client access: `client.silver.assets`

Async client access: `client.silver.assets` with `await` on method calls.

These methods are Silver because the published contract does not document them directly, or because the SDK intentionally wraps a narrower Silver workflow around existing Golden operations. They remain separate so undocumented or convenience behavior never overrides the documented SDK surface.

## Methods

### `add_manufacturer_to_site2`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.assets.add_manufacturer_to_site2(include_all_models=..., manufacturer_id=..., timeout=None)`
- Async: `await client.silver.assets.add_manufacturer_to_site2(include_all_models=..., manufacturer_id=..., timeout=None)`
- Raw payload: `client.silver.assets.add_manufacturer_to_site2.raw(include_all_models=..., manufacturer_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/manufacturers/{manufacturer_id}/site/{include_all_models}`
- Observed in: `migrated_from_golden_stoplight`

Remove Manufacturer

#### Remove a Manufacturer from a Site
#### Sample request:
```
POST /api/v1.0/manufacturers/70fe08d5-e67e-4495-8ac4-d92f734774af/site/true
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.assets.add_manufacturer_to_site2` (operationId `Manufacturer_AddManufacturerToSite2`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `include_all_models` | `IncludeAllModels` | `path` | `yes` | `bool` | (default false) Add all Models from this manufacturer to site |
| `manufacturer_id` | `ManufacturerId` | `path` | `yes` | `str` | Manufacturer Id to be added |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `create_asset_status_type`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.assets.create_asset_status_type(json_body=..., timeout=None)`
- Async: `await client.silver.assets.create_asset_status_type(json_body=..., timeout=None)`
- Raw payload: `client.silver.assets.create_asset_status_type.raw(json_body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/status/types/new`
- Observed in: `migrated_from_golden_stoplight`

Create a new asset status type

#### Creates a new Asset Status Type with provided attributes.  A AssetStatusID, as well a complete record of the updated Asset Status Type is returned for every successful creation of Asset Status Types.
#### Sample request:
```
POST /api/v1.0/assets/status/types/new
{
  "Update":{
		"AssetStatusTypeId":"a102cced-419d-4102-aadf-461f1e96b07b"
		"Name":"Example New Status Type",
		"IsRetired":false
		}
}
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.assets.create_asset_status_type` (operationId `AssetStatusType_CreateAssetStatusType`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `json_body` | `Item` | `body` | `yes` | `dict[str, Any] | list[Any]` | Asset Status Type to be updated, including all attributes |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `delete_asset_funding_type`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.assets.delete_asset_funding_type(asset_funding_type_id=..., timeout=None)`
- Async: `await client.silver.assets.delete_asset_funding_type(asset_funding_type_id=..., timeout=None)`
- Raw payload: `client.silver.assets.delete_asset_funding_type.raw(asset_funding_type_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/assets/funding/types/{asset_funding_type_id}`
- Observed in: `migrated_from_golden_stoplight`

Delete Asset Funding Type 

#### Delete an Asset Funding Type
#### Sample request:
```
DELETE /api/v1.0/assets/funding/types/a443fec7-45fe-4d08-8daf-11f4dd86df79
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.assets.delete_asset_funding_type` (operationId `AssetFundingType_DeleteAssetFundingType`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `asset_funding_type_id` | `AssetFundingTypeId` | `path` | `yes` | `str` | Asset Funding Type Id to be removed |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `delete_asset_status_type`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.assets.delete_asset_status_type(asset_status_type_id=..., timeout=None)`
- Async: `await client.silver.assets.delete_asset_status_type(asset_status_type_id=..., timeout=None)`
- Raw payload: `client.silver.assets.delete_asset_status_type.raw(asset_status_type_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/assets/status/types/{asset_status_type_id}`
- Observed in: `migrated_from_golden_stoplight`

Delete Asset Status Type

#### Delete an asset status type.
#### Sample request:
```
DELETE /api/v1.0/assets/status/types/a102cced-419d-4102-aadf-461f1e96b07b
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.assets.delete_asset_status_type` (operationId `AssetStatusType_DeleteAssetStatusType`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `asset_status_type_id` | `AssetStatusTypeId` | `path` | `yes` | `str` | Path parameter migrated from the previous Golden SDK. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_asset_favorites2`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.assets.get_asset_favorites2(all=..., user_id=..., timeout=None)`
- Async: `await client.silver.assets.get_asset_favorites2(all=..., user_id=..., timeout=None)`
- Raw payload: `client.silver.assets.get_asset_favorites2.raw(all=..., user_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/assets/favorites/{user_id}/{all}`
- Observed in: `migrated_from_golden_stoplight`

Get user favorites

#### Performs a query to obtain assets favorited by a given user.  For a more generalized / flexible asset query call POST `/api/v1.0/assets` to search by filter.
#### Sample request:
```
GET /api/v1.0/assets/favorites/ac6cece8-e4f4-e511-a789-005056bb000e
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.assets.get_asset_favorites2` (operationId `Asset_GetAssetFavorites2`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `all` | `All` | `path` | `yes` | `str` | Include assets within the provided user's assigned location rooms |
| `user_id` | `UserId` | `path` | `yes` | `str` | User ID to use when searching assets |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_asset_funding_type`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.assets.get_asset_funding_type(asset_funding_type_id=..., r=..., timeout=None)`
- Async: `await client.silver.assets.get_asset_funding_type(asset_funding_type_id=..., r=..., timeout=None)`
- Raw payload: `client.silver.assets.get_asset_funding_type.raw(asset_funding_type_id=..., r=..., timeout=None)`
- HTTP route: `GET /api/v1.0/assets/funding/types/{asset_funding_type_id}`
- Observed in: `migrated_from_golden_stoplight`

Get Asset Funding Type

#### Retrieve a specific asset funding type by AssetFundingTypeId
#### Sample request:
```
GET /api/v1.0/assets/funding/types/a443fec7-45fe-4d08-8daf-11f4dd86df79
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.assets.get_asset_funding_type` (operationId `AssetFundingType_GetAssetFundingType`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `asset_funding_type_id` | `AssetFundingTypeId` | `path` | `yes` | `str` | Asset Funding Type Id to be retrieved, including all attributes |
| `r` | `r` | `query` | `yes` | `Any` | Query parameter migrated from the previous Golden SDK. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_asset_funding_types2`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.assets.get_asset_funding_types2(json_body=..., timeout=None)`
- Async: `await client.silver.assets.get_asset_funding_types2(json_body=..., timeout=None)`
- Raw payload: `client.silver.assets.get_asset_funding_types2.raw(json_body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/funding/types`
- Observed in: `migrated_from_golden_stoplight`

Get Asset Funding Types

#### Retrieves a list of asset funding types. A specific location type via GET `api/v1.0/assets/funding/types/a443fec7-45fe-4d08-8daf-11f4dd86df79`.
#### Sample request:
```
GET /api/v1.0/assets/funding/types
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.assets.get_asset_funding_types2` (operationId `AssetFundingType_GetAssetFundingTypes2`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `json_body` | `r` | `body` | `yes` | `dict[str, Any] | list[Any]` | Body parameter migrated from the previous Golden SDK. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_assets_by_asset_status_type`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.assets.get_assets_by_asset_status_type(asset_status_type_id=..., timeout=None)`
- Async: `await client.silver.assets.get_assets_by_asset_status_type(asset_status_type_id=..., timeout=None)`
- Raw payload: `client.silver.assets.get_assets_by_asset_status_type.raw(asset_status_type_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/assets/assetstatustype/{asset_status_type_id}`
- Observed in: `migrated_from_golden_stoplight`

Query by status

#### Queries / searches for assets which match a given status.  For a more generalized / flexible asset query call POST `/api/v1.0/assets` to search by filter.
#### Sample request:
```
GET /api/v1.0/assets/assetstatustype/ac6cece8-e4f4-e511-a789-005056bb000e
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.assets.get_assets_by_asset_status_type` (operationId `Asset_GetAssetsByAssetStatusType`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `asset_status_type_id` | `AssetStatusTypeId` | `path` | `yes` | `str` | Asset status ID to search for |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_assets_by_asset_tag`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.assets.get_assets_by_asset_tag(asset_tag=..., timeout=None)`
- Async: `await client.silver.assets.get_assets_by_asset_tag(asset_tag=..., timeout=None)`
- Raw payload: `client.silver.assets.get_assets_by_asset_tag.raw(asset_tag=..., timeout=None)`
- HTTP route: `GET /api/v1.0/assets/assettag/{asset_tag}`
- Observed in: `migrated_from_golden_stoplight`

Query by asset tag ( exact )

#### Queries / searches for assets which exactly match a given asset tag.  Search is case-insensitive.  For a more generalized / flexible asset query call POST `/api/v1.0/assets` to search by filter.
#### Sample request:
```
GET /api/v1.0/assets/assettag/100345
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.assets.get_assets_by_asset_tag` (operationId `Asset_GetAssetsByAssetTag`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `asset_tag` | `AssetTag` | `path` | `yes` | `str` | Asset tag to search for |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_spare_assets_by_asset_tag`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.assets.get_spare_assets_by_asset_tag(asset_tag=..., timeout=None)`
- Async: `await client.silver.assets.get_spare_assets_by_asset_tag(asset_tag=..., timeout=None)`
- Raw payload: `client.silver.assets.get_spare_assets_by_asset_tag.raw(asset_tag=..., timeout=None)`
- HTTP route: `GET /api/v1.0/assets/spares/assettag/{asset_tag}`
- Observed in: `migrated_from_golden_stoplight`

Query spares by asset tag

#### Queries / searches only for spare assets which exactly match a given asset tag.  Search is case-insensitive.  For a more generalized / flexible asset query call POST `/api/v1.0/assets` to search by filter.
#### Sample request:
```
GET /api/v1.0/assets/assettag/search/100345
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.assets.get_spare_assets_by_asset_tag` (operationId `Asset_GetSpareAssetsByAssetTag`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `asset_tag` | `AssetTag` | `path` | `yes` | `str` | Asset tag to search for |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_user_assets2`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.assets.get_user_assets2(all=..., user_id=..., timeout=None)`
- Async: `await client.silver.assets.get_user_assets2(all=..., user_id=..., timeout=None)`
- Raw payload: `client.silver.assets.get_user_assets2.raw(all=..., user_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/assets/for/{user_id}/{all}`
- Observed in: `migrated_from_golden_stoplight`

Query by user

#### Queries / searches for assets which match a given user.  For a more generalized / flexible asset query call POST `/api/v1.0/assets` to search by filter.
#### Sample request:
```
GET /api/v1.0/assets/for/ac6cece8-e4f4-e511-a789-005056bb000e
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.assets.get_user_assets2` (operationId `Asset_GetUserAssets2`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `all` | `All` | `path` | `yes` | `str` | Path parameter migrated from the previous Golden SDK. |
| `user_id` | `UserId` | `path` | `yes` | `str` | User ID to search for |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `search_assets_by_asset_tag`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.assets.search_assets_by_asset_tag(asset_tag=..., timeout=None)`
- Async: `await client.silver.assets.search_assets_by_asset_tag(asset_tag=..., timeout=None)`
- Raw payload: `client.silver.assets.search_assets_by_asset_tag.raw(asset_tag=..., timeout=None)`
- HTTP route: `GET /api/v1.0/assets/assettag/search/{asset_tag}`
- Observed in: `migrated_from_golden_stoplight`

Query by asset tag ( wildcard )

#### Queries / searches for assets which loosely match a given asset tag by means of a "contains text" search.  Search is case-insensitive.  For a more generalized / flexible asset query call POST `/api/v1.0/assets` to search by filter.
#### Sample request:
```
GET /api/v1.0/assets/assettag/search/100345
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.assets.search_assets_by_asset_tag` (operationId `Asset_SearchAssetsByAssetTag`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `asset_tag` | `AssetTag` | `path` | `yes` | `str` | Asset tag to search for |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `update_asset_funding_type`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.assets.update_asset_funding_type(asset_funding_type_id=..., json_body=..., timeout=None)`
- Async: `await client.silver.assets.update_asset_funding_type(asset_funding_type_id=..., json_body=..., timeout=None)`
- Raw payload: `client.silver.assets.update_asset_funding_type.raw(asset_funding_type_id=..., json_body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/funding/types/{asset_funding_type_id}`
- Observed in: `migrated_from_golden_stoplight`

Migrated Silver route for POST /assets/funding/types/{AssetFundingTypeId}.

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.assets.update_asset_funding_type` (operationId `AssetFundingType_UpdateAssetFundingType`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `asset_funding_type_id` | `AssetFundingTypeId` | `path` | `yes` | `str` | Path parameter migrated from the previous Golden SDK. |
| `json_body` | `Item` | `body` | `yes` | `dict[str, Any] | list[Any]` | Body parameter migrated from the previous Golden SDK. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `update_asset_status_type`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.assets.update_asset_status_type(asset_status_type_id=..., json_body=..., timeout=None)`
- Async: `await client.silver.assets.update_asset_status_type(asset_status_type_id=..., json_body=..., timeout=None)`
- Raw payload: `client.silver.assets.update_asset_status_type.raw(asset_status_type_id=..., json_body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/status/types/{asset_status_type_id}`
- Observed in: `migrated_from_golden_stoplight`

Update an existing asset status type

#### Updates a previously submitted Asset Status Type with provided changes.  A AssetStatusID, as well a complete record of the updated Asset Status Type is returned for every successful update Asset Status Type call made to the API.  
#### Sample request:
```
POST /api/v1.0/assets/status/types/a102cced-419d-4102-aadf-461f1e96b07b
{
  "Update":{
		"Name":"New Status Type",
		"IsRetired":false
		}
}
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.assets.update_asset_status_type` (operationId `AssetStatusType_UpdateAssetStatusType`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `asset_status_type_id` | `AssetStatusTypeId` | `path` | `yes` | `str` | Path parameter migrated from the previous Golden SDK. |
| `json_body` | `Item` | `body` | `yes` | `dict[str, Any] | list[Any]` | Asset Status Type to be created, including all necessary attributes |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---
