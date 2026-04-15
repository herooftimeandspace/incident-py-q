# `parts` Namespace

Sync client access: `client.parts`

Async client access: `client.parts` with `await` on method calls.

## Aliases

| Alias | Canonical Method | Route |
| --- | --- | --- |
| `delete` | `delete_part` | `DELETE /parts/{PartId}` |
| `get` | `get_part` | `GET /parts/{PartId}` |
| `list` | `get_parts` | `GET /parts` |
| `update` | `update_part` | `POST /parts/{PartId}` |

## Methods

### `delete_part`

Operation ID: `Part_DeletePart`

- Sync: `client.parts.delete_part(part_id=..., timeout=None)`
- Async: `await client.parts.delete_part(part_id=..., timeout=None)`
- Raw payload: `client.parts.delete_part.raw(part_id=..., timeout=None)`
- HTTP route: `DELETE /parts/{PartId}`
- Source controller: `Parts`
- Aliases: `delete`

Delete a Part

#### Delete a specific Part
#### Sample request:
```
DELETE /api/v1.0/parts/c94f81dc-8fae-4e82-8014-b5e5b5e86575
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `part_id` | `PartId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_part_supplier`

Operation ID: `Part_DeletePartSupplier`

- Sync: `client.parts.delete_part_supplier(part_supplier_id=..., timeout=None)`
- Async: `await client.parts.delete_part_supplier(part_supplier_id=..., timeout=None)`
- Raw payload: `client.parts.delete_part_supplier.raw(part_supplier_id=..., timeout=None)`
- HTTP route: `DELETE /parts/suppliers/{PartSupplierId}`
- Source controller: `Parts`

Delete a Part Supplier

#### Delete a specific part supplier.
#### Sample request:
```
DELETE /api/v1.0/parts/suppliers/e67018f1-3815-449c-a09f-e66dc6b83202
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `part_supplier_id` | `PartSupplierId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_part`

Operation ID: `Part_GetPart`

- Sync: `client.parts.get_part(part_id=..., timeout=None)`
- Async: `await client.parts.get_part(part_id=..., timeout=None)`
- Raw payload: `client.parts.get_part.raw(part_id=..., timeout=None)`
- HTTP route: `GET /parts/{PartId}`
- Source controller: `Parts`
- Aliases: `get`

Get Part

#### Retrieve a specific Part based on PartID
#### Sample request:
```
GET /api/v1.0/parts/bbfdf941-7bbe-4cc2-a9d7-9b7fbeed2358
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `part_id` | `PartId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ItemGetResponseOfPart`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemGetResponseOfPart`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_part_supplier`

Operation ID: `Part_GetPartSupplier`

- Sync: `client.parts.get_part_supplier(part_supplier_id=..., timeout=None)`
- Async: `await client.parts.get_part_supplier(part_supplier_id=..., timeout=None)`
- Raw payload: `client.parts.get_part_supplier.raw(part_supplier_id=..., timeout=None)`
- HTTP route: `GET /parts/suppliers/{PartSupplierId}`
- Source controller: `Parts`

Get Part Supplier

#### Retrieve a specific part supplier on PartSupplierId
#### Sample request:
```
GET /api/v1.0/parts/suppliers/0baa50cf-2037-43a4-9b64-391737f58d41
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `part_supplier_id` | `PartSupplierId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ItemGetResponseOfPartSupplier`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemGetResponseOfPartSupplier`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_part_suppliers`

Operation ID: `Part_GetPartSuppliers`

- Sync: `client.parts.get_part_suppliers(timeout=None)`
- Async: `await client.parts.get_part_suppliers(timeout=None)`
- Raw payload: `client.parts.get_part_suppliers.raw(timeout=None)`
- HTTP route: `GET /parts/suppliers`
- Source controller: `Parts`

Get Part Suppliers

#### Retrieves a list of parts suppliers. A specific location type via GET `api/v1.0/parts/suppliers/{PartSupplierId:guid}`.
#### Sample request:
```
GET /api/v1.0/parts/suppliers
```

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `ListGetResponseOfPartSupplier`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfPartSupplier`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_parts`

Operation ID: `Part_GetParts`

- Sync: `client.parts.get_parts(timeout=None)`
- Async: `await client.parts.get_parts(timeout=None)`
- Raw payload: `client.parts.get_parts.raw(timeout=None)`
- HTTP route: `GET /parts`
- Source controller: `Parts`
- Aliases: `list`

Get Parts

#### Retrieves a list of parts. A specific part can be retrieved via GET `api/v1.0/parts/{PartId:guid}`.
#### Sample request:
```
GET /api/v1.0/parts
```

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `ListGetResponseOfPart`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfPart`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_part`

Operation ID: `Part_UpdatePart`

- Sync: `client.parts.update_part(part_id=..., part=..., timeout=None)`
- Async: `await client.parts.update_part(part_id=..., part=..., timeout=None)`
- Raw payload: `client.parts.update_part.raw(part_id=..., part=..., timeout=None)`
- HTTP route: `POST /parts/{PartId}`
- Source controller: `Parts`
- Aliases: `update`

No contract summary provided.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `part_id` | `PartId` | `path` | `yes` | `str` | `-` | - |
| `part` | `Part` | `body` | `yes` | `Part` | `Part` | - |

#### Returns

- Typed call return: `ItemUpdateResponseOfPart`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemUpdateResponseOfPart`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_part_supplier`

Operation ID: `Part_UpdatePartSupplier`

- Sync: `client.parts.update_part_supplier(part_supplier_id=..., part_supplier=..., timeout=None)`
- Async: `await client.parts.update_part_supplier(part_supplier_id=..., part_supplier=..., timeout=None)`
- Raw payload: `client.parts.update_part_supplier.raw(part_supplier_id=..., part_supplier=..., timeout=None)`
- HTTP route: `POST /parts/suppliers/{PartSupplierId}`
- Source controller: `Parts`

No contract summary provided.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `part_supplier_id` | `PartSupplierId` | `path` | `yes` | `str` | `-` | - |
| `part_supplier` | `PartSupplier` | `body` | `yes` | `PartSupplier` | `PartSupplier` | - |

#### Returns

- Typed call return: `ItemUpdateResponseOfPartSupplier`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemUpdateResponseOfPartSupplier`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
