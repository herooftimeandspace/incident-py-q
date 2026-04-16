# `manufacturers` Golden Namespace

Sync client access: `client.manufacturers`

Async client access: `client.manufacturers` with `await` on method calls.

These methods are Golden because they come from bundled Stoplight controller contracts.

## Aliases

| Alias | Canonical Method | Route |
| --- | --- | --- |
| `delete` | `delete_manufacturer2` | `DELETE /manufacturers/{ManufacturerId}` |
| `get` | `get_manufacturer2` | `GET /manufacturers/{ManufacturerId}` |
| `update` | `update_manufacturer2` | `POST /manufacturers/{ManufacturerId}` |

## Methods

### `add_manufacturer_to_site3`

Provenance: Golden Stoplight contract

Operation ID: `Manufacturer_AddManufacturerToSite3`

- Sync: `client.manufacturers.add_manufacturer_to_site3(manufacturer_id=..., include_all_models=None, timeout=None)`
- Async: `await client.manufacturers.add_manufacturer_to_site3(manufacturer_id=..., include_all_models=None, timeout=None)`
- Raw payload: `client.manufacturers.add_manufacturer_to_site3.raw(manufacturer_id=..., include_all_models=None, timeout=None)`
- HTTP route: `POST /manufacturers/{ManufacturerId}/site`
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

### `add_manufacturer_to_site4`

Provenance: Golden Stoplight contract

Operation ID: `Manufacturer_AddManufacturerToSite4`

- Sync: `client.manufacturers.add_manufacturer_to_site4(manufacturer_id=..., include_all_models=..., timeout=None)`
- Async: `await client.manufacturers.add_manufacturer_to_site4(manufacturer_id=..., include_all_models=..., timeout=None)`
- Raw payload: `client.manufacturers.add_manufacturer_to_site4.raw(manufacturer_id=..., include_all_models=..., timeout=None)`
- HTTP route: `POST /manufacturers/{ManufacturerId}/site/{IncludeAllModels}`
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

### `delete_manufacturer2`

Provenance: Golden Stoplight contract

Operation ID: `Manufacturer_DeleteManufacturer2`

- Sync: `client.manufacturers.delete_manufacturer2(manufacturer_id=..., timeout=None)`
- Async: `await client.manufacturers.delete_manufacturer2(manufacturer_id=..., timeout=None)`
- Raw payload: `client.manufacturers.delete_manufacturer2.raw(manufacturer_id=..., timeout=None)`
- HTTP route: `DELETE /manufacturers/{ManufacturerId}`
- Source controller: `Manufacturers`
- Aliases: `delete`

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

### `get_global_manufacturers3`

Provenance: Golden Stoplight contract

Operation ID: `Manufacturer_GetGlobalManufacturers3`

- Sync: `client.manufacturers.get_global_manufacturers3(r=..., timeout=None)`
- Async: `await client.manufacturers.get_global_manufacturers3(r=..., timeout=None)`
- Raw payload: `client.manufacturers.get_global_manufacturers3.raw(r=..., timeout=None)`
- HTTP route: `GET /manufacturers/global`
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

### `get_global_manufacturers4`

Provenance: Golden Stoplight contract

Operation ID: `Manufacturer_GetGlobalManufacturers4`

- Sync: `client.manufacturers.get_global_manufacturers4(r=..., timeout=None)`
- Async: `await client.manufacturers.get_global_manufacturers4(r=..., timeout=None)`
- Raw payload: `client.manufacturers.get_global_manufacturers4.raw(r=..., timeout=None)`
- HTTP route: `POST /manufacturers/global`
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

### `get_manufacturer2`

Provenance: Golden Stoplight contract

Operation ID: `Manufacturer_GetManufacturer2`

- Sync: `client.manufacturers.get_manufacturer2(manufacturer_id=..., r=..., timeout=None)`
- Async: `await client.manufacturers.get_manufacturer2(manufacturer_id=..., r=..., timeout=None)`
- Raw payload: `client.manufacturers.get_manufacturer2.raw(manufacturer_id=..., r=..., timeout=None)`
- HTTP route: `GET /manufacturers/{ManufacturerId}`
- Source controller: `Manufacturers`
- Aliases: `get`

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

### `remove_manufacturer_from_site2`

Provenance: Golden Stoplight contract

Operation ID: `Manufacturer_RemoveManufacturerFromSite2`

- Sync: `client.manufacturers.remove_manufacturer_from_site2(manufacturer_id=..., timeout=None)`
- Async: `await client.manufacturers.remove_manufacturer_from_site2(manufacturer_id=..., timeout=None)`
- Raw payload: `client.manufacturers.remove_manufacturer_from_site2.raw(manufacturer_id=..., timeout=None)`
- HTTP route: `DELETE /manufacturers/{ManufacturerId}/site`
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

### `update_manufacturer2`

Provenance: Golden Stoplight contract

Operation ID: `Manufacturer_UpdateManufacturer2`

- Sync: `client.manufacturers.update_manufacturer2(manufacturer_id=..., item=..., timeout=None)`
- Async: `await client.manufacturers.update_manufacturer2(manufacturer_id=..., item=..., timeout=None)`
- Raw payload: `client.manufacturers.update_manufacturer2.raw(manufacturer_id=..., item=..., timeout=None)`
- HTTP route: `POST /manufacturers/{ManufacturerId}`
- Source controller: `Manufacturers`
- Aliases: `update`

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
