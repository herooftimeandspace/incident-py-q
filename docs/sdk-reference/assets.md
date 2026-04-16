# `assets` Golden Namespace

Sync client access: `client.assets`

Async client access: `client.assets` with `await` on method calls.

These methods are Golden because they come from bundled Stoplight controller contracts.

## Aliases

| Alias | Canonical Method | Route |
| --- | --- | --- |
| `delete` | `delete_asset` | `DELETE /assets/{AssetId}` |
| `get` | `get_asset` | `GET /assets/{AssetId}` |
| `update` | `update_asset` | `POST /assets/{AssetId}` |

## Methods

### `add_manufacturer_to_site`

Provenance: Golden Stoplight contract

Operation ID: `Manufacturer_AddManufacturerToSite`

- Sync: `client.assets.add_manufacturer_to_site(manufacturer_id=..., include_all_models=None, timeout=None)`
- Async: `await client.assets.add_manufacturer_to_site(manufacturer_id=..., include_all_models=None, timeout=None)`
- Raw payload: `client.assets.add_manufacturer_to_site.raw(manufacturer_id=..., include_all_models=None, timeout=None)`
- HTTP route: `POST /assets/manufacturers/{ManufacturerId}/site`
- Source controller: `Manufacturers`

Remove Manufacturer

#### Remove a Manufacturer from a Site
#### Sample request:
```
POST /api/v1.0/manufacturers/70fe08d5-e67e-4495-8ac4-d92f734774af/site/true
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `manufacturer_id` | `ManufacturerId` | `path` | `yes` | `str` | `-` | Manufacturer Id to be added |
| `include_all_models` | `IncludeAllModels` | `query` | `no` | `bool` | `-` | (default false) Add all Models from this manufacturer to site |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `add_manufacturer_to_site2`

Provenance: Golden Stoplight contract

Operation ID: `Manufacturer_AddManufacturerToSite2`

- Sync: `client.assets.add_manufacturer_to_site2(manufacturer_id=..., include_all_models=..., timeout=None)`
- Async: `await client.assets.add_manufacturer_to_site2(manufacturer_id=..., include_all_models=..., timeout=None)`
- Raw payload: `client.assets.add_manufacturer_to_site2.raw(manufacturer_id=..., include_all_models=..., timeout=None)`
- HTTP route: `POST /assets/manufacturers/{ManufacturerId}/site/{IncludeAllModels}`
- Source controller: `Manufacturers`

Remove Manufacturer

#### Remove a Manufacturer from a Site
#### Sample request:
```
POST /api/v1.0/manufacturers/70fe08d5-e67e-4495-8ac4-d92f734774af/site/true
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `manufacturer_id` | `ManufacturerId` | `path` | `yes` | `str` | `-` | Manufacturer Id to be added |
| `include_all_models` | `IncludeAllModels` | `path` | `yes` | `bool` | `-` | (default false) Add all Models from this manufacturer to site |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `add_user_favorite_asset`

Provenance: Golden Stoplight contract

Operation ID: `Asset_AddUserFavoriteAsset`

- Sync: `client.assets.add_user_favorite_asset(asset_id=..., user_id=..., timeout=None)`
- Async: `await client.assets.add_user_favorite_asset(asset_id=..., user_id=..., timeout=None)`
- Raw payload: `client.assets.add_user_favorite_asset.raw(asset_id=..., user_id=..., timeout=None)`
- HTTP route: `POST /assets/favorites/{AssetId}/{UserId}`
- Source controller: `Assets`

Mark as favorite

#### Marks a given asset for a user as a favorite
#### Sample request:
```
POST /api/v1.0/assets/favorites/ac6cece8-e4f4-e511-a789-005056bb000e/ac6cece8-e4f4-e511-a789-005056bb000e
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_id` | `AssetId` | `path` | `yes` | `str` | `-` | Asset ID to mark as favorite |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | User ID of the user to be linked to the provided asset |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_asset_status_type`

Provenance: Golden Stoplight contract

Operation ID: `AssetStatusType_CreateAssetStatusType`

- Sync: `client.assets.create_asset_status_type(item=..., timeout=None)`
- Async: `await client.assets.create_asset_status_type(item=..., timeout=None)`
- Raw payload: `client.assets.create_asset_status_type.raw(item=..., timeout=None)`
- HTTP route: `POST /assets/status/types/new`
- Source controller: `Assets`

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

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `item` | `Item` | `body` | `yes` | `UpdateAssetStatusTypeRequest` | `UpdateAssetStatusTypeRequest` | Asset Status Type to be updated, including all attributes |

#### Returns

- Typed call return: `ItemCreateResponseOfAssetStatusType`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemCreateResponseOfAssetStatusType`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_asset`

Provenance: Golden Stoplight contract

Operation ID: `Asset_DeleteAsset`

- Sync: `client.assets.delete_asset(asset_id=..., timeout=None)`
- Async: `await client.assets.delete_asset(asset_id=..., timeout=None)`
- Raw payload: `client.assets.delete_asset.raw(asset_id=..., timeout=None)`
- HTTP route: `DELETE /assets/{AssetId}`
- Source controller: `Assets`
- Aliases: `delete`

No contract summary provided.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_id` | `AssetId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_asset_funding_type`

Provenance: Golden Stoplight contract

Operation ID: `AssetFundingType_DeleteAssetFundingType`

- Sync: `client.assets.delete_asset_funding_type(asset_funding_type_id=..., timeout=None)`
- Async: `await client.assets.delete_asset_funding_type(asset_funding_type_id=..., timeout=None)`
- Raw payload: `client.assets.delete_asset_funding_type.raw(asset_funding_type_id=..., timeout=None)`
- HTTP route: `DELETE /assets/funding/types/{AssetFundingTypeId}`
- Source controller: `Assets`

Delete Asset Funding Type 

#### Delete an Asset Funding Type
#### Sample request:
```
DELETE /api/v1.0/assets/funding/types/a443fec7-45fe-4d08-8daf-11f4dd86df79
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_funding_type_id` | `AssetFundingTypeId` | `path` | `yes` | `str` | `-` | Asset Funding Type Id to be removed |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_asset_status_type`

Provenance: Golden Stoplight contract

Operation ID: `AssetStatusType_DeleteAssetStatusType`

- Sync: `client.assets.delete_asset_status_type(asset_status_type_id=..., timeout=None)`
- Async: `await client.assets.delete_asset_status_type(asset_status_type_id=..., timeout=None)`
- Raw payload: `client.assets.delete_asset_status_type.raw(asset_status_type_id=..., timeout=None)`
- HTTP route: `DELETE /assets/status/types/{AssetStatusTypeId}`
- Source controller: `Assets`

Delete Asset Status Type

#### Delete an asset status type.
#### Sample request:
```
DELETE /api/v1.0/assets/status/types/a102cced-419d-4102-aadf-461f1e96b07b
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_status_type_id` | `AssetStatusTypeId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_manufacturer`

Provenance: Golden Stoplight contract

Operation ID: `Manufacturer_DeleteManufacturer`

- Sync: `client.assets.delete_manufacturer(manufacturer_id=..., timeout=None)`
- Async: `await client.assets.delete_manufacturer(manufacturer_id=..., timeout=None)`
- Raw payload: `client.assets.delete_manufacturer.raw(manufacturer_id=..., timeout=None)`
- HTTP route: `DELETE /assets/manufacturers/{ManufacturerId}`
- Source controller: `Manufacturers`

No contract summary provided.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `manufacturer_id` | `ManufacturerId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset`

Provenance: Golden Stoplight contract

Operation ID: `Asset_GetAsset`

- Sync: `client.assets.get_asset(asset_id=..., timeout=None)`
- Async: `await client.assets.get_asset(asset_id=..., timeout=None)`
- Raw payload: `client.assets.get_asset.raw(asset_id=..., timeout=None)`
- HTTP route: `GET /assets/{AssetId}`
- Source controller: `Assets`
- Aliases: `get`

Get an asset

#### Get information related to a given asset.  Properties and meta information for the asset is returned.  For a listing of associated tickets call GET `/api/v1.0/tickets`.  For timeline / historical data call GET `/api/v1.0/assets/{AssetId:guid}/activities`
#### Sample request:
```
GET /api/v1.0/assets/ac6cece8-e4f4-e511-a789-005056bb000e
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_id` | `AssetId` | `path` | `yes` | `str` | `-` | Asset ID of the record to modify |

#### Returns

- Typed call return: `ItemGetResponseOfAsset`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemGetResponseOfAsset`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_activities`

Provenance: Golden Stoplight contract

Operation ID: `Asset_GetAssetActivities`

- Sync: `client.assets.get_asset_activities(asset_id=..., timeout=None)`
- Async: `await client.assets.get_asset_activities(asset_id=..., timeout=None)`
- Raw payload: `client.assets.get_asset_activities.raw(asset_id=..., timeout=None)`
- HTTP route: `GET /assets/{AssetId}/activities`
- Source controller: `Assets`

Get asset change history

#### Gets timeline / change history information related to a given asset.  Timestamps and associated data related to the activity or update are included.  For a listing of associated tickets call GET `/api/v1.0/tickets`.  For high-level asset information call GET `/api/v1.0/assets/{AssetId:guid}`.
#### Sample request:
```
GET /api/v1.0/assets/ac6cece8-e4f4-e511-a789-005056bb000e/activities
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_id` | `AssetId` | `path` | `yes` | `str` | `-` | Asset ID of the record to modify |

#### Returns

- Typed call return: `ListGetResponseOfActivity`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfActivity`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_favorites`

Provenance: Golden Stoplight contract

Operation ID: `Asset_GetAssetFavorites`

- Sync: `client.assets.get_asset_favorites(user_id=..., all=None, timeout=None)`
- Async: `await client.assets.get_asset_favorites(user_id=..., all=None, timeout=None)`
- Raw payload: `client.assets.get_asset_favorites.raw(user_id=..., all=None, timeout=None)`
- HTTP route: `GET /assets/favorites/{UserId}`
- Source controller: `Assets`

Get user favorites

#### Performs a query to obtain assets favorited by a given user.  For a more generalized / flexible asset query call POST `/api/v1.0/assets` to search by filter.
#### Sample request:
```
GET /api/v1.0/assets/favorites/ac6cece8-e4f4-e511-a789-005056bb000e
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | User ID to use when searching assets |
| `all` | `All` | `query` | `no` | `Any` | `-` | Include assets within the provided user's assigned location rooms |

#### Returns

- Typed call return: `ListGetResponseOfAsset`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfAsset`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_favorites2`

Provenance: Golden Stoplight contract

Operation ID: `Asset_GetAssetFavorites2`

- Sync: `client.assets.get_asset_favorites2(user_id=..., all=..., timeout=None)`
- Async: `await client.assets.get_asset_favorites2(user_id=..., all=..., timeout=None)`
- Raw payload: `client.assets.get_asset_favorites2.raw(user_id=..., all=..., timeout=None)`
- HTTP route: `GET /assets/favorites/{UserId}/{All}`
- Source controller: `Assets`

Get user favorites

#### Performs a query to obtain assets favorited by a given user.  For a more generalized / flexible asset query call POST `/api/v1.0/assets` to search by filter.
#### Sample request:
```
GET /api/v1.0/assets/favorites/ac6cece8-e4f4-e511-a789-005056bb000e
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | User ID to use when searching assets |
| `all` | `All` | `path` | `yes` | `str` | `-` | Include assets within the provided user's assigned location rooms |

#### Returns

- Typed call return: `ListGetResponseOfAsset`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfAsset`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_funding_type`

Provenance: Golden Stoplight contract

Operation ID: `AssetFundingType_GetAssetFundingType`

- Sync: `client.assets.get_asset_funding_type(asset_funding_type_id=..., r=..., timeout=None)`
- Async: `await client.assets.get_asset_funding_type(asset_funding_type_id=..., r=..., timeout=None)`
- Raw payload: `client.assets.get_asset_funding_type.raw(asset_funding_type_id=..., r=..., timeout=None)`
- HTTP route: `GET /assets/funding/types/{AssetFundingTypeId}`
- Source controller: `Assets`

Get Asset Funding Type

#### Retrieve a specific asset funding type by AssetFundingTypeId
#### Sample request:
```
GET /api/v1.0/assets/funding/types/a443fec7-45fe-4d08-8daf-11f4dd86df79
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_funding_type_id` | `AssetFundingTypeId` | `path` | `yes` | `str` | `-` | Asset Funding Type Id to be retrieved, including all attributes |
| `r` | `r` | `query` | `yes` | `Any` | `-` | - |

#### Returns

- Typed call return: `ItemGetResponseOfAssetFundingType`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemGetResponseOfAssetFundingType`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_funding_types`

Provenance: Golden Stoplight contract

Operation ID: `AssetFundingType_GetAssetFundingTypes`

- Sync: `client.assets.get_asset_funding_types(r=..., timeout=None)`
- Async: `await client.assets.get_asset_funding_types(r=..., timeout=None)`
- Raw payload: `client.assets.get_asset_funding_types.raw(r=..., timeout=None)`
- HTTP route: `GET /assets/funding/types`
- Source controller: `Assets`

Get Asset Funding Types

#### Retrieves a list of asset funding types. A specific location type via GET `api/v1.0/assets/funding/types/a443fec7-45fe-4d08-8daf-11f4dd86df79`.
#### Sample request:
```
GET /api/v1.0/assets/funding/types
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `r` | `r` | `query` | `yes` | `Any` | `-` | - |

#### Returns

- Typed call return: `ListGetResponseOfAssetFundingType`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfAssetFundingType`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_funding_types2`

Provenance: Golden Stoplight contract

Operation ID: `AssetFundingType_GetAssetFundingTypes2`

- Sync: `client.assets.get_asset_funding_types2(r=..., timeout=None)`
- Async: `await client.assets.get_asset_funding_types2(r=..., timeout=None)`
- Raw payload: `client.assets.get_asset_funding_types2.raw(r=..., timeout=None)`
- HTTP route: `POST /assets/funding/types`
- Source controller: `Assets`

Get Asset Funding Types

#### Retrieves a list of asset funding types. A specific location type via GET `api/v1.0/assets/funding/types/a443fec7-45fe-4d08-8daf-11f4dd86df79`.
#### Sample request:
```
GET /api/v1.0/assets/funding/types
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `r` | `r` | `body` | `yes` | `GetAssetFundingTypesRequest` | `GetAssetFundingTypesRequest` | - |

#### Returns

- Typed call return: `ListGetResponseOfAssetFundingType`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfAssetFundingType`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_status_type`

Provenance: Golden Stoplight contract

Operation ID: `AssetStatusType_GetAssetStatusType`

- Sync: `client.assets.get_asset_status_type(asset_status_type_id=..., r=..., timeout=None)`
- Async: `await client.assets.get_asset_status_type(asset_status_type_id=..., r=..., timeout=None)`
- Raw payload: `client.assets.get_asset_status_type.raw(asset_status_type_id=..., r=..., timeout=None)`
- HTTP route: `GET /assets/status/types/{AssetStatusTypeId}`
- Source controller: `Assets`

Get Asset Status Type

#### Retrieve a specific asset status type based on supplied AssetStatusTypeId
#### Sample request:
```
GET /api/v1.0/assets/status/types/a102cced-419d-4102-aadf-461f1e96b07b
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_status_type_id` | `AssetStatusTypeId` | `path` | `yes` | `str` | `-` | - |
| `r` | `r` | `query` | `yes` | `Any` | `-` | - |

#### Returns

- Typed call return: `ItemGetResponseOfAssetStatusType`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemGetResponseOfAssetStatusType`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_status_types`

Provenance: Golden Stoplight contract

Operation ID: `AssetStatusType_GetAssetStatusTypes`

- Sync: `client.assets.get_asset_status_types(r=..., timeout=None)`
- Async: `await client.assets.get_asset_status_types(r=..., timeout=None)`
- Raw payload: `client.assets.get_asset_status_types.raw(r=..., timeout=None)`
- HTTP route: `GET /assets/status/types`
- Source controller: `Assets`

Get Asset Status Types

#### Retrieves a list of asset status types. A specific asset status type can be retrieved via GET `api/v1.0/assets/status/types/{AssetStatusTypeId:guid}`.
#### Sample request:
```
GET /api/v1.0/assets/status/types
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `r` | `r` | `query` | `yes` | `Any` | `-` | - |

#### Returns

- Typed call return: `ListGetResponseOfAssetStatusType`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfAssetStatusType`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_status_types2`

Provenance: Golden Stoplight contract

Operation ID: `AssetStatusType_GetAssetStatusTypes2`

- Sync: `client.assets.get_asset_status_types2(r=..., timeout=None)`
- Async: `await client.assets.get_asset_status_types2(r=..., timeout=None)`
- Raw payload: `client.assets.get_asset_status_types2.raw(r=..., timeout=None)`
- HTTP route: `POST /assets/status/types`
- Source controller: `Assets`

Get Asset Status Types

#### Retrieves a list of asset status types. A specific asset status type can be retrieved via GET `api/v1.0/assets/status/types/{AssetStatusTypeId:guid}`.
#### Sample request:
```
GET /api/v1.0/assets/status/types
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `r` | `r` | `body` | `yes` | `GetAssetStatusTypesRequest` | `GetAssetStatusTypesRequest` | - |

#### Returns

- Typed call return: `ListGetResponseOfAssetStatusType`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfAssetStatusType`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_assets`

Provenance: Golden Stoplight contract

Operation ID: `Asset_GetAssets`

- Sync: `client.assets.get_assets(request_info=..., timeout=None)`
- Async: `await client.assets.get_assets(request_info=..., timeout=None)`
- Raw payload: `client.assets.get_assets.raw(request_info=..., timeout=None)`
- HTTP route: `POST /assets`
- Source controller: `Assets`

Get assets by filter

#### Performs a query to obtain assets which match the provided filter conditions.  This allows for a very flexible search as filter conditions may be expressed in AND / OR groups to facilitate the query.  This API call returns full asset details.  To obtain high-level asset counts for a given query / filter set call POST `/api/v1.0/assets/counts` and provide the same filters.
#### Sample request:
```
POST /api/v1.0/assets
{
   "Filters":[
      {
         "Facet":"location",
         "Id":"ca6ffef3-cb32-40cb-a62c-7b1068b5cc21",
         "Negative":false
      },
      {
         "Facet":"AssetType",
         "Id":"2a1561e5-34ff-4fcf-87de-2a146f0e1c01"
      }
   ]
}
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `request_info` | `RequestInfo` | `body` | `yes` | `GetAssetsRequest` | `GetAssetsRequest` | Search parameters including optional filter definitions |

#### Returns

- Typed call return: `ListGetResponseOfAsset`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfAsset`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_assets_by_asset_status_type`

Provenance: Golden Stoplight contract

Operation ID: `Asset_GetAssetsByAssetStatusType`

- Sync: `client.assets.get_assets_by_asset_status_type(asset_status_type_id=..., timeout=None)`
- Async: `await client.assets.get_assets_by_asset_status_type(asset_status_type_id=..., timeout=None)`
- Raw payload: `client.assets.get_assets_by_asset_status_type.raw(asset_status_type_id=..., timeout=None)`
- HTTP route: `GET /assets/assetstatustype/{AssetStatusTypeId}`
- Source controller: `Assets`

Query by status

#### Queries / searches for assets which match a given status.  For a more generalized / flexible asset query call POST `/api/v1.0/assets` to search by filter.
#### Sample request:
```
GET /api/v1.0/assets/assetstatustype/ac6cece8-e4f4-e511-a789-005056bb000e
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_status_type_id` | `AssetStatusTypeId` | `path` | `yes` | `str` | `-` | Asset status ID to search for |

#### Returns

- Typed call return: `ListGetResponseOfAsset`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfAsset`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_assets_by_asset_tag`

Provenance: Golden Stoplight contract

Operation ID: `Asset_GetAssetsByAssetTag`

- Sync: `client.assets.get_assets_by_asset_tag(asset_tag=..., timeout=None)`
- Async: `await client.assets.get_assets_by_asset_tag(asset_tag=..., timeout=None)`
- Raw payload: `client.assets.get_assets_by_asset_tag.raw(asset_tag=..., timeout=None)`
- HTTP route: `GET /assets/assettag/{AssetTag}`
- Source controller: `Assets`

Query by asset tag ( exact )

#### Queries / searches for assets which exactly match a given asset tag.  Search is case-insensitive.  For a more generalized / flexible asset query call POST `/api/v1.0/assets` to search by filter.
#### Sample request:
```
GET /api/v1.0/assets/assettag/100345
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_tag` | `AssetTag` | `path` | `yes` | `str` | `-` | Asset tag to search for |

#### Returns

- Typed call return: `ListGetResponseOfAsset`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfAsset`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_assets_by_location_room`

Provenance: Golden Stoplight contract

Operation ID: `Asset_GetAssetsByLocationRoom`

- Sync: `client.assets.get_assets_by_location_room(location_room_id=..., timeout=None)`
- Async: `await client.assets.get_assets_by_location_room(location_room_id=..., timeout=None)`
- Raw payload: `client.assets.get_assets_by_location_room.raw(location_room_id=..., timeout=None)`
- HTTP route: `GET /assets/rooms/{LocationRoomId}`
- Source controller: `Assets`

Query by room

#### Queries / searches for assets which match a given location room.  For a more generalized / flexible asset query call POST `/api/v1.0/assets` to search by filter.
#### Sample request:
```
GET /api/v1.0/assets/rooms/ac6cece8-e4f4-e511-a789-005056bb000e
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `location_room_id` | `LocationRoomId` | `path` | `yes` | `str` | `-` | Room ID to search for |

#### Returns

- Typed call return: `ListGetResponseOfAsset`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfAsset`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_assets_by_serial`

Provenance: Golden Stoplight contract

Operation ID: `Asset_GetAssetsBySerial`

- Sync: `client.assets.get_assets_by_serial(serial=..., timeout=None)`
- Async: `await client.assets.get_assets_by_serial(serial=..., timeout=None)`
- Raw payload: `client.assets.get_assets_by_serial.raw(serial=..., timeout=None)`
- HTTP route: `GET /assets/serial/{Serial}`
- Source controller: `Assets`

Query by serial number ( exact )

#### Queries / searches for assets which exactly match a given serial number.  Search is case-insensitive.  For a more generalized / flexible asset query call POST `/api/v1.0/assets` to search by filter.
#### Sample request:
```
GET /api/v1.0/assets/serial/MT500-234A1000-4300
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `serial` | `Serial` | `path` | `yes` | `str` | `-` | Serial number to search for |

#### Returns

- Typed call return: `ListGetResponseOfAsset`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfAsset`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_assets_by_storage_unit_number`

Provenance: Golden Stoplight contract

Operation ID: `Asset_GetAssetsByStorageUnitNumber`

- Sync: `client.assets.get_assets_by_storage_unit_number(location_id=..., storage_unit_number=..., timeout=None)`
- Async: `await client.assets.get_assets_by_storage_unit_number(location_id=..., storage_unit_number=..., timeout=None)`
- Raw payload: `client.assets.get_assets_by_storage_unit_number.raw(location_id=..., storage_unit_number=..., timeout=None)`
- HTTP route: `GET /assets/storageunit/{LocationId}/{StorageUnitNumber}`
- Source controller: `Assets`

Query by storage unit

#### Queries / searches for assets at a given storage unit number.  Search is case-insensitive.  For a more generalized / flexible asset query call POST `/api/v1.0/assets` to search by filter.
#### Sample request:
```
GET /api/v1.0/assets/storageunit/ac6cece8-e4f4-e511-a789-005056bb000e/1050
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `location_id` | `LocationId` | `path` | `yes` | `str` | `-` | Location ID of the location used to search |
| `storage_unit_number` | `StorageUnitNumber` | `path` | `yes` | `str` | `-` | Storage unit number to search for |

#### Returns

- Typed call return: `ListGetResponseOfAsset`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfAsset`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_assets_count`

Provenance: Golden Stoplight contract

Operation ID: `Asset_GetAssetsCount`

- Sync: `client.assets.get_assets_count(request_info=..., timeout=None)`
- Async: `await client.assets.get_assets_count(request_info=..., timeout=None)`
- Raw payload: `client.assets.get_assets_count.raw(request_info=..., timeout=None)`
- HTTP route: `POST /assets/count`
- Source controller: `Assets`

Get counts by filter

#### Performs a query to obtain asset counts which match the provided filter conditions.  This allows for a very flexible search as filter conditions may be expressed in AND / OR groups to facilitate the query.  This API call does not return assets and only returns high-level asset counts.  To return a list of assets which represent the counts returned call POST `/api/v1.0/assets` and provide the same filters.
#### Sample request:
```
POST /api/v1.0/assets/count
{
   "Filters":[
      {
         "Facet":"location",
         "Id":"ca6ffef3-cb32-40cb-a62c-7b1068b5cc21",
         "Negative":false
      },
      {
         "Facet":"AssetType",
         "Id":"2a1561e5-34ff-4fcf-87de-2a146f0e1c01"
      }
   ]
}
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `request_info` | `RequestInfo` | `body` | `yes` | `GetAssetsRequest` | `GetAssetsRequest` | Search parameters including optional filter definitions |

#### Returns

- Typed call return: `ListGetResponseOfAsset`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfAsset`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_global_manufacturers`

Provenance: Golden Stoplight contract

Operation ID: `Manufacturer_GetGlobalManufacturers`

- Sync: `client.assets.get_global_manufacturers(r=..., timeout=None)`
- Async: `await client.assets.get_global_manufacturers(r=..., timeout=None)`
- Raw payload: `client.assets.get_global_manufacturers.raw(r=..., timeout=None)`
- HTTP route: `GET /assets/manufacturers/global`
- Source controller: `Manufacturers`

Get Manufacturers

#### Retrieves a list of all manufacturers.
#### Sample request:
```
GET /api/v1.0/manufacturers/global
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `r` | `r` | `query` | `yes` | `Any` | `-` | - |

#### Returns

- Typed call return: `ListGetResponseOfManufacturer`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfManufacturer`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_global_manufacturers2`

Provenance: Golden Stoplight contract

Operation ID: `Manufacturer_GetGlobalManufacturers2`

- Sync: `client.assets.get_global_manufacturers2(r=..., timeout=None)`
- Async: `await client.assets.get_global_manufacturers2(r=..., timeout=None)`
- Raw payload: `client.assets.get_global_manufacturers2.raw(r=..., timeout=None)`
- HTTP route: `POST /assets/manufacturers/global`
- Source controller: `Manufacturers`

Get Manufacturers

#### Retrieves a list of all manufacturers.
#### Sample request:
```
GET /api/v1.0/manufacturers/global
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `r` | `r` | `body` | `yes` | `GetManufacturersRequest` | `GetManufacturersRequest` | - |

#### Returns

- Typed call return: `ListGetResponseOfManufacturer`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfManufacturer`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_manufacturer`

Provenance: Golden Stoplight contract

Operation ID: `Manufacturer_GetManufacturer`

- Sync: `client.assets.get_manufacturer(manufacturer_id=..., r=..., timeout=None)`
- Async: `await client.assets.get_manufacturer(manufacturer_id=..., r=..., timeout=None)`
- Raw payload: `client.assets.get_manufacturer.raw(manufacturer_id=..., r=..., timeout=None)`
- HTTP route: `GET /assets/manufacturers/{ManufacturerId}`
- Source controller: `Manufacturers`

Get Manufacturer

#### Retrieve a specific manufacturer by Manufacturer Id
#### Sample request:
```
GET /api/v1.0/parts/manufacturers/70fe08d5-e67e-4495-8ac4-d92f734774af/site
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `manufacturer_id` | `ManufacturerId` | `path` | `yes` | `str` | `-` | Manufacturer ID to be retrieved |
| `r` | `r` | `query` | `yes` | `Any` | `-` | - |

#### Returns

- Typed call return: `ItemGetResponseOfManufacturer`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemGetResponseOfManufacturer`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_spare_assets_by_asset_tag`

Provenance: Golden Stoplight contract

Operation ID: `Asset_GetSpareAssetsByAssetTag`

- Sync: `client.assets.get_spare_assets_by_asset_tag(asset_tag=..., timeout=None)`
- Async: `await client.assets.get_spare_assets_by_asset_tag(asset_tag=..., timeout=None)`
- Raw payload: `client.assets.get_spare_assets_by_asset_tag.raw(asset_tag=..., timeout=None)`
- HTTP route: `GET /assets/spares/assettag/{AssetTag}`
- Source controller: `Assets`

Query spares by asset tag

#### Queries / searches only for spare assets which exactly match a given asset tag.  Search is case-insensitive.  For a more generalized / flexible asset query call POST `/api/v1.0/assets` to search by filter.
#### Sample request:
```
GET /api/v1.0/assets/assettag/search/100345
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_tag` | `AssetTag` | `path` | `yes` | `str` | `-` | Asset tag to search for |

#### Returns

- Typed call return: `ListGetResponseOfSpareAsset`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfSpareAsset`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_user_assets`

Provenance: Golden Stoplight contract

Operation ID: `Asset_GetUserAssets`

- Sync: `client.assets.get_user_assets(user_id=..., all=None, timeout=None)`
- Async: `await client.assets.get_user_assets(user_id=..., all=None, timeout=None)`
- Raw payload: `client.assets.get_user_assets.raw(user_id=..., all=None, timeout=None)`
- HTTP route: `GET /assets/for/{UserId}`
- Source controller: `Assets`

Query by user

#### Queries / searches for assets which match a given user.  For a more generalized / flexible asset query call POST `/api/v1.0/assets` to search by filter.
#### Sample request:
```
GET /api/v1.0/assets/for/ac6cece8-e4f4-e511-a789-005056bb000e
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | User ID to search for |
| `all` | `All` | `query` | `no` | `Any` | `-` | - |

#### Returns

- Typed call return: `ListGetResponseOfAsset`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfAsset`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_user_assets2`

Provenance: Golden Stoplight contract

Operation ID: `Asset_GetUserAssets2`

- Sync: `client.assets.get_user_assets2(user_id=..., all=..., timeout=None)`
- Async: `await client.assets.get_user_assets2(user_id=..., all=..., timeout=None)`
- Raw payload: `client.assets.get_user_assets2.raw(user_id=..., all=..., timeout=None)`
- HTTP route: `GET /assets/for/{UserId}/{All}`
- Source controller: `Assets`

Query by user

#### Queries / searches for assets which match a given user.  For a more generalized / flexible asset query call POST `/api/v1.0/assets` to search by filter.
#### Sample request:
```
GET /api/v1.0/assets/for/ac6cece8-e4f4-e511-a789-005056bb000e
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | User ID to search for |
| `all` | `All` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ListGetResponseOfAsset`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfAsset`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `remove_manufacturer_from_site`

Provenance: Golden Stoplight contract

Operation ID: `Manufacturer_RemoveManufacturerFromSite`

- Sync: `client.assets.remove_manufacturer_from_site(manufacturer_id=..., timeout=None)`
- Async: `await client.assets.remove_manufacturer_from_site(manufacturer_id=..., timeout=None)`
- Raw payload: `client.assets.remove_manufacturer_from_site.raw(manufacturer_id=..., timeout=None)`
- HTTP route: `DELETE /assets/manufacturers/{ManufacturerId}/site`
- Source controller: `Manufacturers`

Remove Manufacturer

#### Remove a Manufacturer
#### Sample request:
```
DELETE /api/v1.0/manufacturers/70fe08d5-e67e-4495-8ac4-d92f734774af/site
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `manufacturer_id` | `ManufacturerId` | `path` | `yes` | `str` | `-` | Manufacturer Id to be removed |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `remove_user_favorite_asset`

Provenance: Golden Stoplight contract

Operation ID: `Asset_RemoveUserFavoriteAsset`

- Sync: `client.assets.remove_user_favorite_asset(asset_id=..., user_id=..., timeout=None)`
- Async: `await client.assets.remove_user_favorite_asset(asset_id=..., user_id=..., timeout=None)`
- Raw payload: `client.assets.remove_user_favorite_asset.raw(asset_id=..., user_id=..., timeout=None)`
- HTTP route: `POST /assets/favorites/remove/{AssetId}/{UserId}`
- Source controller: `Assets`

Unmark as favorite

#### Unmarks a given asset for a user as a favorite
#### Sample request:
```
POST /api/v1.0/assets/favorites/remove/ac6cece8-e4f4-e511-a789-005056bb000e/ac6cece8-e4f4-e511-a789-005056bb000e
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_id` | `AssetId` | `path` | `yes` | `str` | `-` | Asset ID to unmark as favorite |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | User ID of the user to be unlinked to the provided asset |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `search_assets_by_asset_tag`

Provenance: Golden Stoplight contract

Operation ID: `Asset_SearchAssetsByAssetTag`

- Sync: `client.assets.search_assets_by_asset_tag(asset_tag=..., timeout=None)`
- Async: `await client.assets.search_assets_by_asset_tag(asset_tag=..., timeout=None)`
- Raw payload: `client.assets.search_assets_by_asset_tag.raw(asset_tag=..., timeout=None)`
- HTTP route: `GET /assets/assettag/search/{AssetTag}`
- Source controller: `Assets`

Query by asset tag ( wildcard )

#### Queries / searches for assets which loosely match a given asset tag by means of a "contains text" search.  Search is case-insensitive.  For a more generalized / flexible asset query call POST `/api/v1.0/assets` to search by filter.
#### Sample request:
```
GET /api/v1.0/assets/assettag/search/100345
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_tag` | `AssetTag` | `path` | `yes` | `str` | `-` | Asset tag to search for |

#### Returns

- Typed call return: `ListGetResponseOfAsset`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfAsset`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `search_assets_by_serial`

Provenance: Golden Stoplight contract

Operation ID: `Asset_SearchAssetsBySerial`

- Sync: `client.assets.search_assets_by_serial(serial=..., timeout=None)`
- Async: `await client.assets.search_assets_by_serial(serial=..., timeout=None)`
- Raw payload: `client.assets.search_assets_by_serial.raw(serial=..., timeout=None)`
- HTTP route: `GET /assets/serial/search/{Serial}`
- Source controller: `Assets`

Query by serial number ( wildcard )

#### Queries / searches for assets which loosely match a given serial number by means of a "contains text" search.  Search is case-insensitive.  For a more generalized / flexible asset query call POST `/api/v1.0/assets` to search by filter.
#### Sample request:
```
GET /api/v1.0/assets/serial/MT500-234A1000-4300
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `serial` | `Serial` | `path` | `yes` | `str` | `-` | Serial number to search for |

#### Returns

- Typed call return: `ListGetResponseOfAsset`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfAsset`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_asset`

Provenance: Golden Stoplight contract

Operation ID: `Asset_UpdateAsset`

- Sync: `client.assets.update_asset(asset_id=..., asset=..., timeout=None)`
- Async: `await client.assets.update_asset(asset_id=..., asset=..., timeout=None)`
- Raw payload: `client.assets.update_asset.raw(asset_id=..., asset=..., timeout=None)`
- HTTP route: `POST /assets/{AssetId}`
- Source controller: `Assets`
- Aliases: `update`

No contract summary provided.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_id` | `AssetId` | `path` | `yes` | `str` | `-` | - |
| `asset` | `Asset` | `body` | `yes` | `UpdateAssetRequest` | `UpdateAssetRequest` | - |

#### Returns

- Typed call return: `ItemUpdateResponseOfAsset`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemUpdateResponseOfAsset`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_asset_funding_type`

Provenance: Golden Stoplight contract

Operation ID: `AssetFundingType_UpdateAssetFundingType`

- Sync: `client.assets.update_asset_funding_type(asset_funding_type_id=..., item=..., timeout=None)`
- Async: `await client.assets.update_asset_funding_type(asset_funding_type_id=..., item=..., timeout=None)`
- Raw payload: `client.assets.update_asset_funding_type.raw(asset_funding_type_id=..., item=..., timeout=None)`
- HTTP route: `POST /assets/funding/types/{AssetFundingTypeId}`
- Source controller: `Assets`

No contract summary provided.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_funding_type_id` | `AssetFundingTypeId` | `path` | `yes` | `str` | `-` | - |
| `item` | `Item` | `body` | `yes` | `UpdateAssetFundingTypeRequest` | `UpdateAssetFundingTypeRequest` | - |

#### Returns

- Typed call return: `ItemUpdateResponseOfGuid`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemUpdateResponseOfGuid`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_asset_status_type`

Provenance: Golden Stoplight contract

Operation ID: `AssetStatusType_UpdateAssetStatusType`

- Sync: `client.assets.update_asset_status_type(asset_status_type_id=..., item=..., timeout=None)`
- Async: `await client.assets.update_asset_status_type(asset_status_type_id=..., item=..., timeout=None)`
- Raw payload: `client.assets.update_asset_status_type.raw(asset_status_type_id=..., item=..., timeout=None)`
- HTTP route: `POST /assets/status/types/{AssetStatusTypeId}`
- Source controller: `Assets`

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

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_status_type_id` | `AssetStatusTypeId` | `path` | `yes` | `str` | `-` | - |
| `item` | `Item` | `body` | `yes` | `UpdateAssetStatusTypeRequest` | `UpdateAssetStatusTypeRequest` | Asset Status Type to be created, including all necessary attributes |

#### Returns

- Typed call return: `ItemUpdateResponseOfGuid`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemUpdateResponseOfGuid`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_manufacturer`

Provenance: Golden Stoplight contract

Operation ID: `Manufacturer_UpdateManufacturer`

- Sync: `client.assets.update_manufacturer(manufacturer_id=..., item=..., timeout=None)`
- Async: `await client.assets.update_manufacturer(manufacturer_id=..., item=..., timeout=None)`
- Raw payload: `client.assets.update_manufacturer.raw(manufacturer_id=..., item=..., timeout=None)`
- HTTP route: `POST /assets/manufacturers/{ManufacturerId}`
- Source controller: `Manufacturers`

No contract summary provided.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `manufacturer_id` | `ManufacturerId` | `path` | `yes` | `str` | `-` | - |
| `item` | `Item` | `body` | `yes` | `UpdateManufacturerRequest` | `UpdateManufacturerRequest` | - |

#### Returns

- Typed call return: `ItemUpdateResponseOfGuid`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemUpdateResponseOfGuid`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
