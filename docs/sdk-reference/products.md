# `products` Golden Namespace

Sync client access: `client.products`

Async client access: `client.products` with `await` on method calls.

These methods are Golden because they come from the bundled Incident IQ OpenAPI contract.

## Methods

### `list_products`

Provenance: Golden OpenAPI contract

Operation ID: `listProducts`

- Sync: `client.products.list_products(timeout=None)`
- Async: `await client.products.list_products(timeout=None)`
- Raw payload: `client.products.list_products.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/products/all`
- Source controller: `IncidentIQ API`

List all products

Retrieves all licensed product modules available in IncidentIQ. Products represent functional modules such as Technology, Facilities, and HR. Use this endpoint to discover available ProductIds for filtering or module-specific operations.

**Common Use Cases:**
- Populate product selection dropdowns in UI
- Determine which modules are available for configuration
- Obtain ProductIds for use in other API calls that require product filtering

**Response:** Returns an array of Product objects containing ProductId, ProductName, ProductKey, Icon, and DisplayOrder.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `ProductListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ProductListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
