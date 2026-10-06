# `custom_fields_new` Golden Namespace

Sync client access: `client.custom_fields_new`

Async client access: `client.custom_fields_new` with `await` on method calls.

These methods are Golden because they come from the bundled Incident IQ OpenAPI contract.

## Methods

### `list_custom_field_types_new`

Provenance: Golden OpenAPI contract

Operation ID: `listCustomFieldTypesNew`

- Sync: `client.custom_fields_new.list_custom_field_types_new(s=None, p=None, filter=None, timeout=None)`
- Async: `await client.custom_fields_new.list_custom_field_types_new(s=None, p=None, filter=None, timeout=None)`
- Raw payload: `client.custom_fields_new.list_custom_field_types_new.raw(s=None, p=None, filter=None, timeout=None)`
- HTTP route: `POST /api/v1.0/custom-fields-new/types`
- Source controller: `IncidentIQ API`

List custom field types (alternate endpoint)

Retrieves custom field types using an alternate endpoint path. This endpoint differs from [POST /api/v1.0/custom-fields/types](#/Custom%20Fields/searchCustomFieldTypes) only in its URL path segment (`custom-fields-new` vs `custom-fields`).

**Behavioral Notes**:
- Calls `GetCustomFieldTypesNew()` manager method internally (slightly different from the main types endpoint)
- Supports the same pagination and filtering via query parameters
- Returns the same response structure as the main types endpoint
- This endpoint exists for backward compatibility with certain client implementations

**Query Parameters**: Supports standard `$s` (page size), `$p` (page index), and `$filter` parameters for paging and filtering.

**Minimal Required Fields**: None (empty request body returns all accessible types)

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of records per page |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index to retrieve |
| `filter` | `$filter` | `query` | `no` | `str` | `-` | Filter expression for custom field type names (e.g., (Name%20contains%20Warranty)) |

#### Returns

- Typed call return: `CustomFieldTypeListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CustomFieldTypeListResponse`
- Pagination helper: `client.custom_fields_new.list_custom_field_types_new.iter_pages(start_page=1, page_size=100, max_pages=None, s=None, p=None, filter=None, timeout=None)`

---
