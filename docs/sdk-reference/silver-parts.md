# `silver.parts` Namespace

Sync client access: `client.silver.parts`

Async client access: `client.silver.parts` with `await` on method calls.

These methods are Silver because the published contract does not document them directly, or because the SDK intentionally wraps a narrower Silver workflow around existing Golden operations. They remain separate so undocumented or convenience behavior never overrides the documented SDK surface.

## Methods

### `delete_part`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.parts.delete_part(part_id=..., timeout=None)`
- Async: `await client.silver.parts.delete_part(part_id=..., timeout=None)`
- Raw payload: `client.silver.parts.delete_part.raw(part_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/parts/{part_id}`
- Observed in: `migrated_from_golden_stoplight`

Delete a Part

#### Delete a specific Part
#### Sample request:
```
DELETE /api/v1.0/parts/c94f81dc-8fae-4e82-8014-b5e5b5e86575
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.parts.delete_part` (operationId `Part_DeletePart`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `part_id` | `PartId` | `path` | `yes` | `str` | Path parameter migrated from the previous Golden SDK. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `delete_part_supplier`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.parts.delete_part_supplier(part_supplier_id=..., timeout=None)`
- Async: `await client.silver.parts.delete_part_supplier(part_supplier_id=..., timeout=None)`
- Raw payload: `client.silver.parts.delete_part_supplier.raw(part_supplier_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/parts/suppliers/{part_supplier_id}`
- Observed in: `migrated_from_golden_stoplight`

Delete a Part Supplier

#### Delete a specific part supplier.
#### Sample request:
```
DELETE /api/v1.0/parts/suppliers/e67018f1-3815-449c-a09f-e66dc6b83202
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.parts.delete_part_supplier` (operationId `Part_DeletePartSupplier`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `part_supplier_id` | `PartSupplierId` | `path` | `yes` | `str` | Path parameter migrated from the previous Golden SDK. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_part`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.parts.get_part(part_id=..., timeout=None)`
- Async: `await client.silver.parts.get_part(part_id=..., timeout=None)`
- Raw payload: `client.silver.parts.get_part.raw(part_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/parts/{part_id}`
- Observed in: `migrated_from_golden_stoplight`

Get Part

#### Retrieve a specific Part based on PartID
#### Sample request:
```
GET /api/v1.0/parts/bbfdf941-7bbe-4cc2-a9d7-9b7fbeed2358
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.parts.get_part` (operationId `Part_GetPart`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `part_id` | `PartId` | `path` | `yes` | `str` | Path parameter migrated from the previous Golden SDK. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_part_supplier`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.parts.get_part_supplier(part_supplier_id=..., timeout=None)`
- Async: `await client.silver.parts.get_part_supplier(part_supplier_id=..., timeout=None)`
- Raw payload: `client.silver.parts.get_part_supplier.raw(part_supplier_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/parts/suppliers/{part_supplier_id}`
- Observed in: `migrated_from_golden_stoplight`

Get Part Supplier

#### Retrieve a specific part supplier on PartSupplierId
#### Sample request:
```
GET /api/v1.0/parts/suppliers/0baa50cf-2037-43a4-9b64-391737f58d41
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.parts.get_part_supplier` (operationId `Part_GetPartSupplier`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `part_supplier_id` | `PartSupplierId` | `path` | `yes` | `str` | Path parameter migrated from the previous Golden SDK. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_part_suppliers`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.parts.get_part_suppliers(timeout=None)`
- Async: `await client.silver.parts.get_part_suppliers(timeout=None)`
- Raw payload: `client.silver.parts.get_part_suppliers.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/parts/suppliers`
- Observed in: `migrated_from_golden_stoplight`

Get Part Suppliers

#### Retrieves a list of parts suppliers. A specific location type via GET `api/v1.0/parts/suppliers/{PartSupplierId:guid}`.
#### Sample request:
```
GET /api/v1.0/parts/suppliers
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.parts.get_part_suppliers` (operationId `Part_GetPartSuppliers`).

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_parts`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.parts.get_parts(timeout=None)`
- Async: `await client.silver.parts.get_parts(timeout=None)`
- Raw payload: `client.silver.parts.get_parts.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/parts`
- Observed in: `migrated_from_golden_stoplight`

Get Parts

#### Retrieves a list of parts. A specific part can be retrieved via GET `api/v1.0/parts/{PartId:guid}`.
#### Sample request:
```
GET /api/v1.0/parts
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.parts.get_parts` (operationId `Part_GetParts`).

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `update_part`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.parts.update_part(part_id=..., json_body=..., timeout=None)`
- Async: `await client.silver.parts.update_part(part_id=..., json_body=..., timeout=None)`
- Raw payload: `client.silver.parts.update_part.raw(part_id=..., json_body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/parts/{part_id}`
- Observed in: `migrated_from_golden_stoplight`

Migrated Silver route for POST /parts/{PartId}.

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.parts.update_part` (operationId `Part_UpdatePart`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `part_id` | `PartId` | `path` | `yes` | `str` | Path parameter migrated from the previous Golden SDK. |
| `json_body` | `Part` | `body` | `yes` | `dict[str, Any] | list[Any]` | Body parameter migrated from the previous Golden SDK. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `update_part_supplier`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.parts.update_part_supplier(part_supplier_id=..., json_body=..., timeout=None)`
- Async: `await client.silver.parts.update_part_supplier(part_supplier_id=..., json_body=..., timeout=None)`
- Raw payload: `client.silver.parts.update_part_supplier.raw(part_supplier_id=..., json_body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/parts/suppliers/{part_supplier_id}`
- Observed in: `migrated_from_golden_stoplight`

Migrated Silver route for POST /parts/suppliers/{PartSupplierId}.

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.parts.update_part_supplier` (operationId `Part_UpdatePartSupplier`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `part_supplier_id` | `PartSupplierId` | `path` | `yes` | `str` | Path parameter migrated from the previous Golden SDK. |
| `json_body` | `PartSupplier` | `body` | `yes` | `dict[str, Any] | list[Any]` | Body parameter migrated from the previous Golden SDK. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---
