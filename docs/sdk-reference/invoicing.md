# `invoicing` Golden Namespace

Sync client access: `client.invoicing`

Async client access: `client.invoicing` with `await` on method calls.

These methods are Golden because they come from the bundled Incident IQ OpenAPI contract.

## Aliases

| Alias | Canonical Method | Route |
| --- | --- | --- |
| `create` | `create_vendor` | `POST /api/v1.0/invoicing/vendors/new` |

## Methods

### `create_vendor`

Provenance: Golden OpenAPI contract

Operation ID: `createVendor`

- Sync: `client.invoicing.create_vendor(body=..., timeout=None)`
- Async: `await client.invoicing.create_vendor(body=..., timeout=None)`
- Raw payload: `client.invoicing.create_vendor.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/invoicing/vendors/new`
- Source controller: `IncidentIQ API`
- Aliases: `create`

Create a new vendor

Creates a new vendor in the invoicing system. Vendors represent external service providers for utility billing, supplier invoicing, and cost management.

**Workflow Example**
1. Prepare vendor data including name, address, and optional utility types.
2. Call this endpoint: [POST /api/v1.0/invoicing/vendors/new](#/Invoicing/createVendor) with the vendor object.
3. Extract `Item.VendorId` from response for subsequent operations.

**Minimal Required Fields**: `Name`, `SiteId`

**Optional Fields**: `Address` (full address object), `Telephone`, `UtilityTypes` (array of utility service associations)

**Related Endpoints:**
- [GET /api/v1.0/invoicing/vendors](#/Invoicing/getAllVendors) - List existing vendors
- [POST /api/v1.0/invoicing/vendors/{id}](#/Invoicing/updateVendor) - Update vendor details

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `Vendor` | `Vendor` | The vendor object to create. |

#### Returns

- Typed call return: `VendorItemCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `VendorItemCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_vendor`

Provenance: Golden OpenAPI contract

Operation ID: `deleteVendor`

- Sync: `client.invoicing.delete_vendor(id=..., timeout=None)`
- Async: `await client.invoicing.delete_vendor(id=..., timeout=None)`
- Raw payload: `client.invoicing.delete_vendor.raw(id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/invoicing/vendors/{id}`
- Source controller: `IncidentIQ API`

Delete a vendor

Soft-deletes a vendor in the invoicing system, marking the record as deleted while preserving it for historical reporting and audit trails. Use this when a vendor should no longer be selectable in workflows, not when you need to purge data.

**Prerequisites**
1. **id** - Use [GET /api/v1.0/invoicing/vendors](#/Invoicing/getAllVendors) or [POST /api/v1.0/invoicing/vendors](#/Invoicing/searchVendors) to locate a vendor and extract `Item[].VendorId`.

**Workflow Example**
1. Find vendor: [GET /api/v1.0/invoicing/vendors](#/Invoicing/getAllVendors) -> extract `Item[].VendorId`.
2. Delete vendor: [DELETE /api/v1.0/invoicing/vendors/{id}](#/Invoicing/deleteVendor) with the selected UUID.

**Minimal Required Fields**: id (path parameter).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `id` | `path` | `yes` | `str` | `-` | The unique identifier (UUID) of the vendor to delete. |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_all_vendors`

Provenance: Golden OpenAPI contract

Operation ID: `getAllVendors`

- Sync: `client.invoicing.get_all_vendors(timeout=None)`
- Async: `await client.invoicing.get_all_vendors(timeout=None)`
- Raw payload: `client.invoicing.get_all_vendors.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/invoicing/vendors`
- Source controller: `IncidentIQ API`

Get all vendors

Retrieves a list of all vendors in the invoicing system. Vendors are external service providers (utilities, suppliers) for invoicing and cost tracking purposes.

**Workflow Example**
1. Call this endpoint: [GET /api/v1.0/invoicing/vendors](#/Invoicing/getAllVendors) to list all vendors.
2. Extract `Item[].VendorId` for use with vendor-specific operations.
3. For complex filtering, use [POST /api/v1.0/invoicing/vendors](#/Invoicing/searchVendors) instead.

**Response Fields**
- `Name` - Vendor display name
- `Address` - Full address record with street, city, state, ZIP
- `UtilityTypes` - Associated utility service types
- `Telephone` - Contact phone number

**Related Endpoints:**
- [POST /api/v1.0/invoicing/vendors/new](#/Invoicing/createVendor) - Create a new vendor
- [GET /api/v1.0/invoicing/vendors/{id}](#/Invoicing/getVendorById) - Get vendor details

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `VendorListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `VendorListGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_vendor_by_id`

Provenance: Golden OpenAPI contract

Operation ID: `getVendorById`

- Sync: `client.invoicing.get_vendor_by_id(id=..., timeout=None)`
- Async: `await client.invoicing.get_vendor_by_id(id=..., timeout=None)`
- Raw payload: `client.invoicing.get_vendor_by_id.raw(id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/invoicing/vendors/{id}`
- Source controller: `IncidentIQ API`

Get vendor by ID

Retrieves a single vendor record by its unique identifier, returning the full vendor profile (name, address, utility types, and contact details) in the standard response envelope.

**Prerequisites**
1. **id** - Use [GET /api/v1.0/invoicing/vendors](#/Invoicing/getAllVendors) or [POST /api/v1.0/invoicing/vendors](#/Invoicing/searchVendors) to locate a vendor and extract `Item[].VendorId`.

**Workflow Example**
1. List or search vendors: [GET /api/v1.0/invoicing/vendors](#/Invoicing/getAllVendors) or [POST /api/v1.0/invoicing/vendors](#/Invoicing/searchVendors) -> extract `Item[].VendorId`.
2. Fetch vendor details: [GET /api/v1.0/invoicing/vendors/{id}](#/Invoicing/getVendorById) with the selected UUID.

**Minimal Required Fields**: id (path parameter).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `id` | `path` | `yes` | `str` | `-` | The unique identifier (UUID) of the vendor to retrieve. |

#### Returns

- Typed call return: `VendorItemGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `VendorItemGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `search_vendors`

Provenance: Golden OpenAPI contract

Operation ID: `searchVendors`

- Sync: `client.invoicing.search_vendors(body=None, timeout=None)`
- Async: `await client.invoicing.search_vendors(body=None, timeout=None)`
- Raw payload: `client.invoicing.search_vendors.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/invoicing/vendors`
- Source controller: `IncidentIQ API`

Search vendors

Searches for vendors with filtering and pagination options via request body. Provides more flexibility than the GET endpoint for complex queries.

**Request Options**
- `PagingOptions` - Page number and page size for pagination
- `Filters` - Array of filter conditions for field-based queries
- `Fields` - Optional field selection to limit response data

**Workflow Example**
1. Build filter request with `PagingOptions` and optional `Filters` array.
2. Call this endpoint: [POST /api/v1.0/invoicing/vendors](#/Invoicing/searchVendors) with the request body.
3. Process paginated results using `Paging.Page` and `Paging.Total`.

**Related Endpoints:**
- [GET /api/v1.0/invoicing/vendors](#/Invoicing/getAllVendors) - Simple list without filters
- [GET /api/v1.0/invoicing/vendors/{id}](#/Invoicing/getVendorById) - Get specific vendor details

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `GetAllVendorsRequest` | `GetAllVendorsRequest` | Search parameters including filters and paging options. |

#### Returns

- Typed call return: `VendorListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `VendorListGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_vendor`

Provenance: Golden OpenAPI contract

Operation ID: `updateVendor`

- Sync: `client.invoicing.update_vendor(id=..., body=..., timeout=None)`
- Async: `await client.invoicing.update_vendor(id=..., body=..., timeout=None)`
- Raw payload: `client.invoicing.update_vendor.raw(id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/invoicing/vendors/{id}`
- Source controller: `IncidentIQ API`

Update a vendor

Updates an existing vendor's details. The VendorId in the request body must match the id in the URL path for the update to succeed.

**Prerequisites**
1. **id** - Use [GET /api/v1.0/invoicing/vendors](#/Invoicing/getAllVendors) to list vendors. Extract `Item[].VendorId` from the response.

**Workflow Example**
1. List vendors: [GET /api/v1.0/invoicing/vendors](#/Invoicing/getAllVendors) → identify target vendor.
2. Get current details: [GET /api/v1.0/invoicing/vendors/{id}](#/Invoicing/getVendorById) for the current state.
3. Update vendor: [POST /api/v1.0/invoicing/vendors/{id}](#/Invoicing/updateVendor) with modified vendor object.

**Important**: Include `VendorId` in the request body matching the path parameter.

**Related Endpoints:**
- [GET /api/v1.0/invoicing/vendors/{id}](#/Invoicing/getVendorById) - Get current vendor details
- [DELETE /api/v1.0/invoicing/vendors/{id}](#/Invoicing/deleteVendor) - Delete vendor

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `id` | `path` | `yes` | `str` | `-` | The unique identifier (UUID) of the vendor to update. |
| `body` | `body` | `body` | `yes` | `Vendor` | `Vendor` | The updated vendor object. VendorId must match the path parameter. |

#### Returns

- Typed call return: `VendorItemUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `VendorItemUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
