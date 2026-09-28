# `filter` Golden Namespace

Sync client access: `client.filter`

Async client access: `client.filter` with `await` on method calls.

These methods are Golden because they come from the bundled Incident IQ OpenAPI contract.

## Methods

### `get_filter_by_key_and_product_id`

Provenance: Golden OpenAPI contract

Operation ID: `getFilterByKeyAndProductId`

- Sync: `client.filter.get_filter_by_key_and_product_id(filter_key=..., product_id=None, timeout=None)`
- Async: `await client.filter.get_filter_by_key_and_product_id(filter_key=..., product_id=None, timeout=None)`
- Raw payload: `client.filter.get_filter_by_key_and_product_id.raw(filter_key=..., product_id=None, timeout=None)`
- HTTP route: `GET /api/v1.0/filter/for/product/{filterKey}`
- Source controller: `IncidentIQ API`

Get a filter by key and product ID

Returns the filter definition for a specific filter key, optionally scoped to a product ID. Use this to resolve a known facet key into its full definition and UI metadata.

**Prerequisites**
1. **filterKey** - Use [GET /api/v1.0/filters/for/entitytype/{entityTypeId}](#/Filters/listFiltersForEntityType) and extract `Items[].Key`.

**Workflow Example**
1. List filters for an entity type and identify the desired `Key`.
2. Call [GET /api/v1.0/filter/for/product/{filterKey}](#/Filters/getFilterByKeyAndProductId), optionally passing `productId`.
3. Use the returned `FilterDefinition` to render filter controls.

**Minimal Required Fields**: filterKey (path). Optional: productId (query).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `filter_key` | `filterKey` | `path` | `yes` | `str` | `-` | - |
| `product_id` | `productId` | `query` | `no` | `str` | `-` | - |

#### Returns

- Typed call return: `Any`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
