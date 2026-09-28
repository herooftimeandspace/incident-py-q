# `suppliers` Golden Namespace

Sync client access: `client.suppliers`

Async client access: `client.suppliers` with `await` on method calls.

These methods are Golden because they come from the bundled Incident IQ OpenAPI contract.

## Aliases

| Alias | Canonical Method | Route |
| --- | --- | --- |
| `create` | `create_suppliers_batch` | `POST /api/v1.0/suppliers/ids/new` |

## Methods

### `create_supplier`

Provenance: Golden OpenAPI contract

Operation ID: `createSupplier`

- Sync: `client.suppliers.create_supplier(body=..., timeout=None)`
- Async: `await client.suppliers.create_supplier(body=..., timeout=None)`
- Raw payload: `client.suppliers.create_supplier.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/suppliers`
- Source controller: `IncidentIQ API`

Create supplier

Creates a new supplier record for tracking vendors and purchase order sources. Suppliers represent external companies from which assets and parts are procured.

**Workflow Example**
1. Prepare supplier data including name, contact information, and optional address.
2. Call this endpoint: [POST /api/v1.0/suppliers](#/Suppliers/createSupplier) with the supplier object.
3. Extract `Item.SupplierId` from response for subsequent operations.
4. Reference the supplier when creating purchase orders or parts.

**Minimal Required Fields**: `Name`

**Optional Fields**: `Phone`, `ContactName`, `ContactEmail`, `SupplierUrl`

**Related Endpoints:**
- [GET /api/v1.0/suppliers](#/Suppliers/getSupplierByIdPost) - List existing suppliers
- [POST /api/v1.0/suppliers/{supplierId}/update](#/Suppliers/updateSupplier) - Update supplier details

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `UpdateSupplierRequest` | `UpdateSupplierRequest` | Supplier data to create. |

#### Returns

- Typed call return: `SupplierItemCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `SupplierItemCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_suppliers_batch`

Provenance: Golden OpenAPI contract

Operation ID: `createSuppliersBatch`

- Sync: `client.suppliers.create_suppliers_batch(body=..., timeout=None)`
- Async: `await client.suppliers.create_suppliers_batch(body=..., timeout=None)`
- Raw payload: `client.suppliers.create_suppliers_batch.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/suppliers/ids/new`
- Source controller: `IncidentIQ API`
- Aliases: `create`

Create suppliers (batch)

Creates multiple supplier records in a single request. Pass an array of supplier objects in the request body. Each object follows the same schema as the single-create endpoint.

**Workflow Example**
1. Prepare an array of supplier objects, each containing at minimum a `Name` field.
2. Submit the batch: [POST /api/v1.0/suppliers/ids/new](#/Suppliers/createSuppliersBatch).
3. Extract `Items[].SupplierId` from the response for subsequent operations.

**Minimal Required Fields per item**: `Name`

**Related Endpoints**:
- [POST /api/v1.0/suppliers](#/Suppliers/createSupplier) - Create a single supplier
- [POST /api/v1.0/suppliers/query](#/Suppliers/getSuppliersByQuery) - Query suppliers after creation

**Notes**: Also available via the `/ids` route alias. Returns a list response with all created records.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | Array of supplier objects to create. |

#### Returns

- Typed call return: `SupplierListCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `SupplierListCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_supplier`

Provenance: Golden OpenAPI contract

Operation ID: `deleteSupplier`

- Sync: `client.suppliers.delete_supplier(supplier_id=..., timeout=None)`
- Async: `await client.suppliers.delete_supplier(supplier_id=..., timeout=None)`
- Raw payload: `client.suppliers.delete_supplier.raw(supplier_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/suppliers/{supplierId}`
- Source controller: `IncidentIQ API`

Delete supplier

Permanently deletes a supplier record from the system by its unique identifier.

**Prerequisites**
1. **supplierId** - Obtain by creating a supplier via [POST /api/v1.0/suppliers](#/Suppliers/createSupplier), or retrieve existing suppliers.

**Workflow Example**
1. Identify the supplier to delete by its `SupplierId`
2. Verify no active purchase orders or assets reference this supplier
3. Delete the supplier: [DELETE /api/v1.0/suppliers/{supplierId}](#/Suppliers/deleteSupplier)

**Important Considerations**:
- This operation is permanent and cannot be undone
- Ensure the supplier is not referenced by active purchase orders, assets, or parts before deletion
- Users must have appropriate inventory management permissions to delete suppliers

**Response**: Returns an `ItemDeleteResponse` indicating whether the deletion was successful via the `IsSuccess` property.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `supplier_id` | `supplierId` | `path` | `yes` | `str` | `-` | Unique identifier of the supplier to delete. |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_suppliers_by_query`

Provenance: Golden OpenAPI contract

Operation ID: `deleteSuppliersByQuery`

- Sync: `client.suppliers.delete_suppliers_by_query(body=None, timeout=None)`
- Async: `await client.suppliers.delete_suppliers_by_query(body=None, timeout=None)`
- Raw payload: `client.suppliers.delete_suppliers_by_query.raw(body=None, timeout=None)`
- HTTP route: `DELETE /api/v1.0/suppliers/query`
- Source controller: `IncidentIQ API`

Delete suppliers by query

Deletes supplier records that match the query options provided in `RequestOptions`. This is a bulk destructive operation; the service enforces business constraints and may reject suppliers that are still referenced by purchase orders.

**Prerequisites**
1. Preview the target set via [POST /api/v1.0/suppliers/query](#/Suppliers/getSuppliersByQuery) and confirm the suppliers you intend to remove.

**Workflow Example**
1. Build and test filters with [POST /api/v1.0/suppliers/query](#/Suppliers/getSuppliersByQuery).
2. Submit [DELETE /api/v1.0/suppliers/query](#/Suppliers/deleteSuppliersByQuery) with the same `RequestOptions` to delete matching suppliers.
3. Re-run the query to verify the records are removed and handle any validation failures for suppliers still in use.

**Minimal Required Fields**: None. `RequestOptions.Filters` is strongly recommended to avoid broad deletions.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `GetSuppliersRequest` | `GetSuppliersRequest` | Optional query options that select which suppliers to delete. |

#### Returns

- Typed call return: `ListDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_supplier_by_id`

Provenance: Golden OpenAPI contract

Operation ID: `getSupplierById`

- Sync: `client.suppliers.get_supplier_by_id(supplier_id=..., timeout=None)`
- Async: `await client.suppliers.get_supplier_by_id(supplier_id=..., timeout=None)`
- Raw payload: `client.suppliers.get_supplier_by_id.raw(supplier_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/suppliers/{supplierId}`
- Source controller: `IncidentIQ API`

Get supplier by ID

Retrieves a single supplier record by its unique identifier.

**Prerequisites**
1. **supplierId** - Obtain by creating a supplier via [POST /api/v1.0/suppliers](#/Suppliers/createSupplier), which returns `Item.SupplierId` in the response.

**Workflow Example**
1. Create a new supplier: [POST /api/v1.0/suppliers](#/Suppliers/createSupplier) with required fields → extract `Item.SupplierId`
2. Retrieve supplier details: [GET /api/v1.0/suppliers/{supplierId}](#/Suppliers/getSupplierById)

**Response**: Returns the full `Supplier` object including name, contact information, address, and supplier type. The response wrapper includes `IsSuccess` boolean and `Item` containing the supplier data.

**Notes**: This endpoint also supports the POST method for scenarios where request body options are needed.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `supplier_id` | `supplierId` | `path` | `yes` | `str` | `-` | Unique identifier of the supplier. |

#### Returns

- Typed call return: `SupplierItemGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `SupplierItemGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_supplier_by_id_post`

Provenance: Golden OpenAPI contract

Operation ID: `getSupplierByIdPost`

- Sync: `client.suppliers.get_supplier_by_id_post(supplier_id=..., timeout=None)`
- Async: `await client.suppliers.get_supplier_by_id_post(supplier_id=..., timeout=None)`
- Raw payload: `client.suppliers.get_supplier_by_id_post.raw(supplier_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/suppliers/{supplierId}`
- Source controller: `IncidentIQ API`

Get supplier by ID (POST)

Retrieves a single supplier record by its unique identifier using the POST method. This variant allows passing request options in the body for advanced filtering and field selection.

**Prerequisites**
1. **supplierId** - Obtain by creating a supplier via [POST /api/v1.0/suppliers](#/Suppliers/createSupplier), which returns `Item.SupplierId` in the response.

**Workflow Example**
1. Create a new supplier: [POST /api/v1.0/suppliers](#/Suppliers/createSupplier) with required fields → extract `Item.SupplierId`
2. Retrieve supplier with options: [POST /api/v1.0/suppliers/{supplierId}](#/Suppliers/getSupplierByIdPost) with optional request body

**When to Use POST vs GET**: Use the POST variant when you need to pass complex filtering options or specific field selections in the request body. Use GET for simple retrieval without additional options.

**Response**: Returns the full `Supplier` object wrapped in an `ItemGetResponse` envelope with `IsSuccess` and `Item` properties.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `supplier_id` | `supplierId` | `path` | `yes` | `str` | `-` | Unique identifier of the supplier. |

#### Returns

- Typed call return: `SupplierItemGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `SupplierItemGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_suppliers_by_query`

Provenance: Golden OpenAPI contract

Operation ID: `getSuppliersByQuery`

- Sync: `client.suppliers.get_suppliers_by_query(body=None, timeout=None)`
- Async: `await client.suppliers.get_suppliers_by_query(body=None, timeout=None)`
- Raw payload: `client.suppliers.get_suppliers_by_query.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/suppliers/query`
- Source controller: `IncidentIQ API`

Query suppliers

Returns supplier records that match optional paging, sorting, field projection, and filter criteria supplied in `RequestOptions`. This is the canonical query endpoint for supplier discovery workflows in the v1 inventory API.

**Prerequisites**
1. None. You can call this endpoint without a request body to get the default page.

**Workflow Example**
1. Call [POST /api/v1.0/suppliers/query](#/Suppliers/getSuppliersByQuery) with optional `RequestOptions.Filters` and `RequestOptions.Paging`.
2. Capture `Items[].SupplierId` from the response.
3. Load one supplier in detail via [GET /api/v1.0/suppliers/{supplierId}](#/Suppliers/getSupplierById), or run a bulk delete preview before [DELETE /api/v1.0/suppliers/query](#/Suppliers/deleteSuppliersByQuery).

**Minimal Required Fields**: None. `RequestOptions` is optional.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `GetSuppliersRequest` | `GetSuppliersRequest` | Optional query options for filtering, sorting, paging, and sparse field selection. |

#### Returns

- Typed call return: `SupplierListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `SupplierListGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_suppliers_by_query_legacy`

Provenance: Golden OpenAPI contract

Operation ID: `getSuppliersByQueryLegacy`

- Sync: `client.suppliers.get_suppliers_by_query_legacy(timeout=None)`
- Async: `await client.suppliers.get_suppliers_by_query_legacy(timeout=None)`
- Raw payload: `client.suppliers.get_suppliers_by_query_legacy.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/suppliers/query`
- Source controller: `IncidentIQ API`

Query suppliers (legacy GET)

Retrieves suppliers using the legacy GET variant of the query endpoint. The controller marks this route as obsolete and recommends the POST version for modern integrations, because POST supports richer request-option payload patterns.

**Prerequisites**
1. None. Use this when a client must use GET semantics.

**Workflow Example**
1. Start with [GET /api/v1.0/suppliers/query](#/Suppliers/getSuppliersByQueryLegacy) for basic retrieval.
2. When you need richer filter payloads, switch to [POST /api/v1.0/suppliers/query](#/Suppliers/getSuppliersByQuery).
3. Use returned `Items[].SupplierId` values with [GET /api/v1.0/suppliers/{supplierId}](#/Suppliers/getSupplierById) or update/delete workflows.

**Minimal Required Fields**: None.

**Deprecated Behavior**: The source marks this GET route as obsolete in favor of POST.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `SupplierListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `SupplierListGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_supplier`

Provenance: Golden OpenAPI contract

Operation ID: `updateSupplier`

- Sync: `client.suppliers.update_supplier(supplier_id=..., body=..., timeout=None)`
- Async: `await client.suppliers.update_supplier(supplier_id=..., body=..., timeout=None)`
- Raw payload: `client.suppliers.update_supplier.raw(supplier_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/suppliers/{supplierId}/update`
- Source controller: `IncidentIQ API`

Update supplier

Updates an existing supplier record.

**Updatable Fields**:
- `Name` - Supplier display name
- `Phone` - Primary phone number
- `SupplierNumber` - Internal vendor number
- `SupplierUrl` - Website URL
- `ContactName` / `ContactEmail` - Primary contact
- `AdditionalContactName` / `AdditionalContactEmail` - Secondary contact
- `Description` - Notes about the supplier
- `SupplierTypeId` - Supplier category
- `AddressId` - Associated address

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `supplier_id` | `supplierId` | `path` | `yes` | `str` | `-` | Unique identifier of the supplier to update. |
| `body` | `body` | `body` | `yes` | `UpdateSupplierRequest` | `UpdateSupplierRequest` | Updated supplier data. |

#### Returns

- Typed call return: `SupplierItemUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `SupplierItemUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
