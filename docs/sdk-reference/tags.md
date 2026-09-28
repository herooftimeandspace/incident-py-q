# `tags` Golden Namespace

Sync client access: `client.tags`

Async client access: `client.tags` with `await` on method calls.

These methods are Golden because they come from the bundled Incident IQ OpenAPI contract.

## Aliases

| Alias | Canonical Method | Route |
| --- | --- | --- |
| `create` | `create_tags` | `POST /api/v1.0/tags/ids/new` |

## Methods

### `create_tag`

Provenance: Golden OpenAPI contract

Operation ID: `createTag`

- Sync: `client.tags.create_tag(body=..., timeout=None)`
- Async: `await client.tags.create_tag(body=..., timeout=None)`
- Raw payload: `client.tags.create_tag.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tags`
- Source controller: `IncidentIQ API`

Create a tag

Creates a new tag record for legacy workflows that need to categorize assets, tickets, or other entities by tag.

**Workflow Example**
1. Determine the appropriate tag type for your use case (for example, asset vs. ticket tagging).
2. Call [POST /api/v1.0/tags](#/Tags/createTag) with a name and tag type to create the tag.
3. Use the returned TagId in later tagging operations.

**Minimal Required Fields**: Name, TagTypeId

**Note**: This API is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `UpdateTagRequest` | `UpdateTagRequest` | - |

#### Returns

- Typed call return: `TagCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TagCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_tags`

Provenance: Golden OpenAPI contract

Operation ID: `createTags`

- Sync: `client.tags.create_tags(body=..., timeout=None)`
- Async: `await client.tags.create_tags(body=..., timeout=None)`
- Raw payload: `client.tags.create_tags.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tags/ids/new`
- Source controller: `IncidentIQ API`
- Aliases: `create`

Create multiple tags

Creates multiple new tags in a single request, returning each created tag with its assigned TagId.

**Workflow Example**
1. Build an array of tag objects with the desired names and tag types.
2. Call [POST /api/v1.0/tags/ids/new](#/Tags/createTags) to create them in bulk.
3. Store the returned TagId values for downstream tagging operations.

**Minimal Required Fields**: Name, TagTypeId (per item)

**Note**: This API is deprecated. The route `/api/v1.0/tags/ids` (POST) also maps to this operation.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | - |

#### Returns

- Typed call return: `TagBatchCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TagBatchCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_tag`

Provenance: Golden OpenAPI contract

Operation ID: `deleteTag`

- Sync: `client.tags.delete_tag(tag_id=..., timeout=None)`
- Async: `await client.tags.delete_tag(tag_id=..., timeout=None)`
- Raw payload: `client.tags.delete_tag.raw(tag_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/tags/{TagId}`
- Source controller: `IncidentIQ API`

Delete a tag

Soft-deletes a tag by TagId so it no longer appears in standard tag lists, while preserving the record for audit and restore workflows.

**Prerequisites**
1. **TagId** - Use [GET /api/v1.0/tags/query](#/Tags/getTagsByQuery) to list tags and extract `Items[].TagId`.

**Workflow Example**
1. Retrieve candidate tags with [GET /api/v1.0/tags/query](#/Tags/getTagsByQuery).
2. Call [DELETE /api/v1.0/tags/{TagId}](#/Tags/deleteTag) to mark the tag as deleted.
3. Optionally restore it with [PUT /api/v1.0/tags/{TagId}/undelete](#/Tags/undeleteTag).

**Minimal Required Fields**: TagId (path)

**Note**: This API is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `tag_id` | `TagId` | `path` | `yes` | `str` | `-` | Unique identifier for the tag to delete |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_tags_by_ids`

Provenance: Golden OpenAPI contract

Operation ID: `deleteTagsByIds`

- Sync: `client.tags.delete_tags_by_ids(body=..., timeout=None)`
- Async: `await client.tags.delete_tags_by_ids(body=..., timeout=None)`
- Raw payload: `client.tags.delete_tags_by_ids.raw(body=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/tags/ids`
- Source controller: `IncidentIQ API`

Delete tags by IDs

Soft-deletes multiple tags by TagId, allowing bulk cleanup while preserving records for restore workflows.

**Prerequisites**
1. **TagId list** - Use [GET /api/v1.0/tags/query](#/Tags/getTagsByQuery) to locate tags and extract `Items[].TagId`.

**Workflow Example**
1. Identify the TagId values to remove.
2. Call [DELETE /api/v1.0/tags/ids](#/Tags/deleteTagsByIds) with the TagId array.
3. Restore an individual tag later with [PUT /api/v1.0/tags/{TagId}/undelete](#/Tags/undeleteTag).

**Minimal Required Fields**: TagId array (request body)

**Note**: This API is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | - |

#### Returns

- Typed call return: `ListDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_tags_by_query`

Provenance: Golden OpenAPI contract

Operation ID: `deleteTagsByQuery`

- Sync: `client.tags.delete_tags_by_query(p=None, s=None, timeout=None)`
- Async: `await client.tags.delete_tags_by_query(p=None, s=None, timeout=None)`
- Raw payload: `client.tags.delete_tags_by_query.raw(p=None, s=None, timeout=None)`
- HTTP route: `DELETE /api/v1.0/tags/query`
- Source controller: `IncidentIQ API`

Delete tags by query

Soft-deletes all tags matched by the legacy query parameters, removing them from standard tag lists while keeping records available for restore.

**Workflow Example**
1. Identify the target set via [GET /api/v1.0/tags/query](#/Tags/getTagsByQuery).
2. Call [DELETE /api/v1.0/tags/query](#/Tags/deleteTagsByQuery) with the same paging parameters to delete that slice of results.
3. Restore a specific tag later via [PUT /api/v1.0/tags/{TagId}/undelete](#/Tags/undeleteTag).

**Minimal Required Fields**: none

**Note**: This API is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `p` | `$p` | `query` | `no` | `int` | `-` | Page index (0-based) |
| `s` | `$s` | `query` | `no` | `int` | `-` | Page size |

#### Returns

- Typed call return: `ListDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListDeleteResponse`
- Pagination helper: `client.tags.delete_tags_by_query.iter_pages(start_page=1, page_size=100, max_pages=None, p=None, s=None, timeout=None)`

---

### `get_tag`

Provenance: Golden OpenAPI contract

Operation ID: `getTag`

- Sync: `client.tags.get_tag(tag_id=..., timeout=None)`
- Async: `await client.tags.get_tag(tag_id=..., timeout=None)`
- Raw payload: `client.tags.get_tag.raw(tag_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/tags/{TagId}`
- Source controller: `IncidentIQ API`

Get a tag by ID

Retrieves a single tag record by TagId for legacy integrations that still depend on tag metadata.

**Prerequisites**
1. **TagId** - Use [GET /api/v1.0/tags/query](#/Tags/getTagsByQuery) or [POST /api/v1.0/tags/query](#/Tags/searchTagsByQuery) to list tags, then extract `Items[].TagId`.

**Workflow Example**
1. Search tags by name/type via [POST /api/v1.0/tags/query](#/Tags/searchTagsByQuery) and note `Items[0].TagId`.
2. Call [GET /api/v1.0/tags/{TagId}](#/Tags/getTag) to retrieve the full tag record.

**Minimal Required Fields**: TagId (path)

**Note**: This API is deprecated. Prefer newer tag management endpoints when available.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `tag_id` | `TagId` | `path` | `yes` | `str` | `-` | Unique identifier for the tag |

#### Returns

- Typed call return: `TagItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TagItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_tags_by_ids`

Provenance: Golden OpenAPI contract

Operation ID: `getTagsByIds`

- Sync: `client.tags.get_tags_by_ids(body=..., timeout=None)`
- Async: `await client.tags.get_tags_by_ids(body=..., timeout=None)`
- Raw payload: `client.tags.get_tags_by_ids.raw(body=..., timeout=None)`
- HTTP route: `GET /api/v1.0/tags/ids`
- Source controller: `IncidentIQ API`

Get tags by IDs

Retrieves multiple tags by TagId in a single call, useful when a client already has a list of identifiers to hydrate.

**Prerequisites**
1. **TagId list** - Use [GET /api/v1.0/tags/query](#/Tags/getTagsByQuery) or [POST /api/v1.0/tags/query](#/Tags/searchTagsByQuery) to gather tag IDs and extract `Items[].TagId`.

**Workflow Example**
1. Collect TagId values from a search.
2. Call [GET /api/v1.0/tags/ids](#/Tags/getTagsByIds) with the TagId array in the request body.

**Minimal Required Fields**: TagId array (request body)

**Note**: This API is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | - |

#### Returns

- Typed call return: `TagListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TagListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_tags_by_query`

Provenance: Golden OpenAPI contract

Operation ID: `getTagsByQuery`

- Sync: `client.tags.get_tags_by_query(p=None, s=None, timeout=None)`
- Async: `await client.tags.get_tags_by_query(p=None, s=None, timeout=None)`
- Raw payload: `client.tags.get_tags_by_query.raw(p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v1.0/tags/query`
- Source controller: `IncidentIQ API`

Query tags (GET)

Retrieves tags using legacy query parameters and paging, returning a list that can be used to populate dropdowns or locate TagId values.

**Workflow Example**
1. Request the first page with [GET /api/v1.0/tags/query](#/Tags/getTagsByQuery) using `$p=0` and `$s=25`.
2. Read `Items[].TagId`, `Items[].Name`, and `Items[].TagTypeId` from the response for follow-up calls.

**Minimal Required Fields**: none

**Note**: This API is deprecated. Prefer newer tag search endpoints when available.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `p` | `$p` | `query` | `no` | `int` | `-` | Page index (0-based) |
| `s` | `$s` | `query` | `no` | `int` | `-` | Page size |

#### Returns

- Typed call return: `TagListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TagListResponse`
- Pagination helper: `client.tags.get_tags_by_query.iter_pages(start_page=1, page_size=100, max_pages=None, p=None, s=None, timeout=None)`

---

### `get_tags_by_type`

Provenance: Golden OpenAPI contract

Operation ID: `getTagsByType`

- Sync: `client.tags.get_tags_by_type(tag_type_id=..., timeout=None)`
- Async: `await client.tags.get_tags_by_type(tag_type_id=..., timeout=None)`
- Raw payload: `client.tags.get_tags_by_type.raw(tag_type_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/tags/of/type/{tagTypeId}`
- Source controller: `IncidentIQ API`

Get tags by type (GET)

Retrieves all tags of a specific type, enabling clients to list tags for a given category (such as asset tags or ticket tags).

**Prerequisites**
1. **tagTypeId** - Use [GET /api/v1.0/tags/query](#/Tags/getTagsByQuery) to inspect existing tags and extract `Items[].TagTypeId` values.

**Workflow Example**
1. Identify the desired tag type ID from existing tags.
2. Call [GET /api/v1.0/tags/of/type/{tagTypeId}](#/Tags/getTagsByType) to retrieve the list for that type.

**Minimal Required Fields**: tagTypeId (path)

**Note**: This API is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `tag_type_id` | `tagTypeId` | `path` | `yes` | `int` | `-` | Tag type identifier |

#### Returns

- Typed call return: `TagListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TagListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `search_tags_by_query`

Provenance: Golden OpenAPI contract

Operation ID: `searchTagsByQuery`

- Sync: `client.tags.search_tags_by_query(p=None, s=None, body=None, timeout=None)`
- Async: `await client.tags.search_tags_by_query(p=None, s=None, body=None, timeout=None)`
- Raw payload: `client.tags.search_tags_by_query.raw(p=None, s=None, body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/tags/query`
- Source controller: `IncidentIQ API`

Search tags by query

Searches for tags using filter criteria in the request body, enabling more targeted lookups than the GET variant.

**Workflow Example**
1. Build filter rules in `Filters` (for example, by tag type or name fragment).
2. Call [POST /api/v1.0/tags/query](#/Tags/searchTagsByQuery) and review `Items[]` for matching tags.
3. Use the returned TagId values for update, delete, or detail retrieval calls.

**Minimal Required Fields**: none (Filters optional)

**Note**: This API is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `p` | `$p` | `query` | `no` | `int` | `-` | Page index (0-based) |
| `s` | `$s` | `query` | `no` | `int` | `-` | Page size |
| `body` | `body` | `body` | `no` | `InlineObject` | `InlineObject` | - |

#### Returns

- Typed call return: `TagListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TagListResponse`
- Pagination helper: `client.tags.search_tags_by_query.iter_pages(start_page=1, page_size=100, max_pages=None, p=None, s=None, body=None, timeout=None)`

---

### `search_tags_by_type`

Provenance: Golden OpenAPI contract

Operation ID: `searchTagsByType`

- Sync: `client.tags.search_tags_by_type(tag_type_id=..., body=None, timeout=None)`
- Async: `await client.tags.search_tags_by_type(tag_type_id=..., body=None, timeout=None)`
- Raw payload: `client.tags.search_tags_by_type.raw(tag_type_id=..., body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/tags/of/type/{tagTypeId}`
- Source controller: `IncidentIQ API`

Search tags by type

Searches for tags of a specific type with optional filters in the request body, supporting narrower queries than the GET variant.

**Prerequisites**
1. **tagTypeId** - Use [GET /api/v1.0/tags/query](#/Tags/getTagsByQuery) to inspect existing tags and extract `Items[].TagTypeId` values.

**Workflow Example**
1. Identify the tag type ID you want to search.
2. Call [POST /api/v1.0/tags/of/type/{tagTypeId}](#/Tags/searchTagsByType) with optional Filters to refine results.
3. Use returned TagId values for update or delete operations.

**Minimal Required Fields**: tagTypeId (path)

**Note**: This API is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `tag_type_id` | `tagTypeId` | `path` | `yes` | `int` | `-` | Tag type identifier |
| `body` | `body` | `body` | `no` | `InlineObject` | `InlineObject` | - |

#### Returns

- Typed call return: `TagListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TagListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `undelete_tag`

Provenance: Golden OpenAPI contract

Operation ID: `undeleteTag`

- Sync: `client.tags.undelete_tag(tag_id=..., timeout=None)`
- Async: `await client.tags.undelete_tag(tag_id=..., timeout=None)`
- Raw payload: `client.tags.undelete_tag.raw(tag_id=..., timeout=None)`
- HTTP route: `PUT /api/v1.0/tags/{TagId}/undelete`
- Source controller: `IncidentIQ API`

Restore a deleted tag

Restores a previously soft-deleted tag by TagId so it can be returned in standard tag searches again.

**Prerequisites**
1. **TagId** - Use [GET /api/v1.0/tags/query](#/Tags/getTagsByQuery) to find deleted tags and extract `Items[].TagId`.

**Workflow Example**
1. Locate deleted tags via [GET /api/v1.0/tags/query](#/Tags/getTagsByQuery) (include a filter for deleted items if supported).
2. Call [PUT /api/v1.0/tags/{TagId}/undelete](#/Tags/undeleteTag) to restore the tag.

**Minimal Required Fields**: TagId (path)

**Note**: This API is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `tag_id` | `TagId` | `path` | `yes` | `str` | `-` | Unique identifier for the tag to restore |

#### Returns

- Typed call return: `ItemUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_tag`

Provenance: Golden OpenAPI contract

Operation ID: `updateTag`

- Sync: `client.tags.update_tag(tag_id=..., body=..., timeout=None)`
- Async: `await client.tags.update_tag(tag_id=..., body=..., timeout=None)`
- Raw payload: `client.tags.update_tag.raw(tag_id=..., body=..., timeout=None)`
- HTTP route: `PUT /api/v1.0/tags/{TagId}/update`
- Source controller: `IncidentIQ API`

Update a tag

Updates an existing tag by TagId, allowing legacy integrations to change the display name or tag type and adjust scope metadata.

**Prerequisites**
1. **TagId** - Use [GET /api/v1.0/tags/query](#/Tags/getTagsByQuery) or [GET /api/v1.0/tags/of/type/{tagTypeId}](#/Tags/getTagsByType) to locate a tag and extract `Items[].TagId`.

**Workflow Example**
1. Identify the tag to edit using [GET /api/v1.0/tags/query](#/Tags/getTagsByQuery).
2. Submit [PUT /api/v1.0/tags/{TagId}/update](#/Tags/updateTag) with the new name/type values.

**Minimal Required Fields**: TagId (path), Name, TagTypeId

**Note**: This API is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `tag_id` | `TagId` | `path` | `yes` | `str` | `-` | Unique identifier for the tag to update |
| `body` | `body` | `body` | `yes` | `UpdateTagRequest` | `UpdateTagRequest` | - |

#### Returns

- Typed call return: `ItemUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_tags_by_ids`

Provenance: Golden OpenAPI contract

Operation ID: `updateTagsByIds`

- Sync: `client.tags.update_tags_by_ids(body=..., timeout=None)`
- Async: `await client.tags.update_tags_by_ids(body=..., timeout=None)`
- Raw payload: `client.tags.update_tags_by_ids.raw(body=..., timeout=None)`
- HTTP route: `PUT /api/v1.0/tags/ids/update`
- Source controller: `IncidentIQ API`

Update tags by IDs

Updates multiple tags by TagId in a single request, applying per-tag changes in the request body array.

**Prerequisites**
1. **TagId list** - Use [GET /api/v1.0/tags/query](#/Tags/getTagsByQuery) or [GET /api/v1.0/tags/of/type/{tagTypeId}](#/Tags/getTagsByType) to locate tags and extract `Items[].TagId`.

**Workflow Example**
1. Gather TagId values to update.
2. Submit [PUT /api/v1.0/tags/ids/update](#/Tags/updateTagsByIds) with one object per tag including the TagId and new values.

**Minimal Required Fields**: TagId, Name, TagTypeId (per item)

**Note**: This API is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | - |

#### Returns

- Typed call return: `ListUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_tags_by_query`

Provenance: Golden OpenAPI contract

Operation ID: `updateTagsByQuery`

- Sync: `client.tags.update_tags_by_query(body=..., timeout=None)`
- Async: `await client.tags.update_tags_by_query(body=..., timeout=None)`
- Raw payload: `client.tags.update_tags_by_query.raw(body=..., timeout=None)`
- HTTP route: `PUT /api/v1.0/tags/query/update`
- Source controller: `IncidentIQ API`

Update tags by query

Updates multiple tags that match a query filter in a single request, applying the same update payload across the result set.

**Workflow Example**
1. Confirm the target set using [POST /api/v1.0/tags/query](#/Tags/searchTagsByQuery).
2. Send [PUT /api/v1.0/tags/query/update](#/Tags/updateTagsByQuery) with an `Update` object containing the fields to change.
3. Optionally include `OnlyFields` to limit which properties are overwritten.

**Minimal Required Fields**: Update

**Note**: This API is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `UpdateTagsRequest` | `UpdateTagsRequest` | - |

#### Returns

- Typed call return: `ListUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
