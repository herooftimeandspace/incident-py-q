# `silver.manufacturers` Namespace

Sync client access: `client.silver.manufacturers`

Async client access: `client.silver.manufacturers` with `await` on method calls.

These methods are Silver because the published contract does not document them directly, or because the SDK intentionally wraps a narrower Silver workflow around existing Golden operations. They remain separate so undocumented or convenience behavior never overrides the documented SDK surface.

## Methods

### `add_manufacturer_to_site3`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.manufacturers.add_manufacturer_to_site3(manufacturer_id=..., include_all_models=None, timeout=None)`
- Async: `await client.silver.manufacturers.add_manufacturer_to_site3(manufacturer_id=..., include_all_models=None, timeout=None)`
- Raw payload: `client.silver.manufacturers.add_manufacturer_to_site3.raw(manufacturer_id=..., include_all_models=None, timeout=None)`
- HTTP route: `POST /api/v1.0/manufacturers/{manufacturer_id}/site`
- Observed in: `migrated_from_golden_stoplight`

Remove Manufacturer

#### Remove a Manufacturer from a Site
#### Sample request:
```
POST /api/v1.0/manufacturers/70fe08d5-e67e-4495-8ac4-d92f734774af/site/true
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.manufacturers.add_manufacturer_to_site3` (operationId `Manufacturer_AddManufacturerToSite3`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `manufacturer_id` | `ManufacturerId` | `path` | `yes` | `str` | Manufacturer Id to be added |
| `include_all_models` | `IncludeAllModels` | `query` | `no` | `bool` | (default false) Add all Models from this manufacturer to site |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `add_manufacturer_to_site4`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.manufacturers.add_manufacturer_to_site4(include_all_models=..., manufacturer_id=..., timeout=None)`
- Async: `await client.silver.manufacturers.add_manufacturer_to_site4(include_all_models=..., manufacturer_id=..., timeout=None)`
- Raw payload: `client.silver.manufacturers.add_manufacturer_to_site4.raw(include_all_models=..., manufacturer_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/manufacturers/{manufacturer_id}/site/{include_all_models}`
- Observed in: `migrated_from_golden_stoplight`

Remove Manufacturer

#### Remove a Manufacturer from a Site
#### Sample request:
```
POST /api/v1.0/manufacturers/70fe08d5-e67e-4495-8ac4-d92f734774af/site/true
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.manufacturers.add_manufacturer_to_site4` (operationId `Manufacturer_AddManufacturerToSite4`).

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

### `delete_manufacturer2`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.manufacturers.delete_manufacturer2(manufacturer_id=..., timeout=None)`
- Async: `await client.silver.manufacturers.delete_manufacturer2(manufacturer_id=..., timeout=None)`
- Raw payload: `client.silver.manufacturers.delete_manufacturer2.raw(manufacturer_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/manufacturers/{manufacturer_id}`
- Observed in: `migrated_from_golden_stoplight`

Migrated Silver route for DELETE /manufacturers/{ManufacturerId}.

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.manufacturers.delete_manufacturer2` (operationId `Manufacturer_DeleteManufacturer2`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `manufacturer_id` | `ManufacturerId` | `path` | `yes` | `str` | Path parameter migrated from the previous Golden SDK. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_global_manufacturers3`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.manufacturers.get_global_manufacturers3(r=..., timeout=None)`
- Async: `await client.silver.manufacturers.get_global_manufacturers3(r=..., timeout=None)`
- Raw payload: `client.silver.manufacturers.get_global_manufacturers3.raw(r=..., timeout=None)`
- HTTP route: `GET /api/v1.0/manufacturers/global`
- Observed in: `migrated_from_golden_stoplight`

Get Manufacturers

#### Retrieves a list of all manufacturers.
#### Sample request:
```
GET /api/v1.0/manufacturers/global
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.manufacturers.get_global_manufacturers3` (operationId `Manufacturer_GetGlobalManufacturers3`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `r` | `r` | `query` | `yes` | `Any` | Query parameter migrated from the previous Golden SDK. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_global_manufacturers4`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.manufacturers.get_global_manufacturers4(json_body=..., timeout=None)`
- Async: `await client.silver.manufacturers.get_global_manufacturers4(json_body=..., timeout=None)`
- Raw payload: `client.silver.manufacturers.get_global_manufacturers4.raw(json_body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/manufacturers/global`
- Observed in: `migrated_from_golden_stoplight`

Get Manufacturers

#### Retrieves a list of all manufacturers.
#### Sample request:
```
GET /api/v1.0/manufacturers/global
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.manufacturers.get_global_manufacturers4` (operationId `Manufacturer_GetGlobalManufacturers4`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `json_body` | `r` | `body` | `yes` | `dict[str, Any] | list[Any]` | Body parameter migrated from the previous Golden SDK. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_manufacturer2`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.manufacturers.get_manufacturer2(manufacturer_id=..., r=..., timeout=None)`
- Async: `await client.silver.manufacturers.get_manufacturer2(manufacturer_id=..., r=..., timeout=None)`
- Raw payload: `client.silver.manufacturers.get_manufacturer2.raw(manufacturer_id=..., r=..., timeout=None)`
- HTTP route: `GET /api/v1.0/manufacturers/{manufacturer_id}`
- Observed in: `migrated_from_golden_stoplight`

Get Manufacturer

#### Retrieve a specific manufacturer by Manufacturer Id
#### Sample request:
```
GET /api/v1.0/parts/manufacturers/70fe08d5-e67e-4495-8ac4-d92f734774af/site
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.manufacturers.get_manufacturer2` (operationId `Manufacturer_GetManufacturer2`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `manufacturer_id` | `ManufacturerId` | `path` | `yes` | `str` | Manufacturer ID to be retrieved |
| `r` | `r` | `query` | `yes` | `Any` | Query parameter migrated from the previous Golden SDK. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `remove_manufacturer_from_site2`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.manufacturers.remove_manufacturer_from_site2(manufacturer_id=..., timeout=None)`
- Async: `await client.silver.manufacturers.remove_manufacturer_from_site2(manufacturer_id=..., timeout=None)`
- Raw payload: `client.silver.manufacturers.remove_manufacturer_from_site2.raw(manufacturer_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/manufacturers/{manufacturer_id}/site`
- Observed in: `migrated_from_golden_stoplight`

Remove Manufacturer

#### Remove a Manufacturer
#### Sample request:
```
DELETE /api/v1.0/manufacturers/70fe08d5-e67e-4495-8ac4-d92f734774af/site
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.manufacturers.remove_manufacturer_from_site2` (operationId `Manufacturer_RemoveManufacturerFromSite2`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `manufacturer_id` | `ManufacturerId` | `path` | `yes` | `str` | Manufacturer Id to be removed |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `update_manufacturer2`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.manufacturers.update_manufacturer2(manufacturer_id=..., json_body=..., timeout=None)`
- Async: `await client.silver.manufacturers.update_manufacturer2(manufacturer_id=..., json_body=..., timeout=None)`
- Raw payload: `client.silver.manufacturers.update_manufacturer2.raw(manufacturer_id=..., json_body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/manufacturers/{manufacturer_id}`
- Observed in: `migrated_from_golden_stoplight`

Migrated Silver route for POST /manufacturers/{ManufacturerId}.

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.manufacturers.update_manufacturer2` (operationId `Manufacturer_UpdateManufacturer2`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `manufacturer_id` | `ManufacturerId` | `path` | `yes` | `str` | Path parameter migrated from the previous Golden SDK. |
| `json_body` | `Item` | `body` | `yes` | `dict[str, Any] | list[Any]` | Body parameter migrated from the previous Golden SDK. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---
