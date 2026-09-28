# `filters` Golden Namespace

Sync client access: `client.filters`

Async client access: `client.filters` with `await` on method calls.

These methods are Golden because they come from the bundled Incident IQ OpenAPI contract.

## Methods

### `create_filter`

Provenance: Golden OpenAPI contract

Operation ID: `createFilter`

- Sync: `client.filters.create_filter(body=None, timeout=None)`
- Async: `await client.filters.create_filter(body=None, timeout=None)`
- Raw payload: `client.filters.create_filter.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/filters/new`
- Source controller: `IncidentIQ API`

Create a new filter

Creates a new filter definition (facet) that can be used in search payloads, views, and rule conditions. ProductId and SiteId are automatically set from the request context if not provided, which makes this useful for tenant-specific filter customization.

**Prerequisites**
1. **Filter catalog** - Use [GET /api/v1.0/filters/for/entitytype/{entityTypeId}](#/Filters/listFiltersForEntityType) to review existing filters and avoid duplicates.
2. **CategoryId** (optional) - Use [GET /api/v1.0/categories/of/filters](#/Categories/listFilterCategories) to group the new filter in the UI.

**Workflow Example**
1. Review existing filters and choose a unique `Key`.
2. Build a `FilterDefinition` with `Key`, `Name`, `FilterTypeId`, and optional `CategoryId`.
3. Create the filter: [POST /api/v1.0/filters/new](#/Filters/createFilter).

**Minimal Required Fields**: `Key`, `Name`, `FilterTypeId`.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `FilterDefinition` | `FilterDefinition` | - |

#### Returns

- Typed call return: `Any`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_filter_by_id`

Provenance: Golden OpenAPI contract

Operation ID: `createFilterById`

- Sync: `client.filters.create_filter_by_id(filter_id=..., timeout=None)`
- Async: `await client.filters.create_filter_by_id(filter_id=..., timeout=None)`
- Raw payload: `client.filters.create_filter_by_id.raw(filter_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/filters/label/{filterId}/values`
- Source controller: `IncidentIQ API`

Get Filter Value Labels

Returns display labels for a list of raw filter values associated with a specific filter definition. Use this when saved filters or view definitions store raw values (IDs, enums, codes) and you need the human-readable labels for UI chips, exports, or audit views.

**Prerequisites**
1. **filterId** - Use [GET /api/v1.0/filters/for/entitytype/{entityTypeId}](#/Filters/listFiltersForEntityType) and extract `Items[].FilterId` for the facet you are labeling.
2. **Values** - Collect raw values from a saved filter set or view definition (for example, [GET /api/v1.0/filters/sets/{filterId}/values](#/Filters/getFilterSetValues) or [GET /api/v1.0/tickets/views/{viewId}](#/Tickets/getTicketView)).

**Workflow Example**
1. Identify the filter definition for the facet you need to label.
2. Gather the stored raw values from a view or filter set.
3. Submit the values to [POST /api/v1.0/filters/label/{filterId}/values](#/Filters/createFilterById) and render the returned labels.

**Minimal Required Fields**: filterId (path) and a body array of values.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `filter_id` | `filterId` | `path` | `yes` | `str` | `-` | The filterId parameter |

#### Returns

- Typed call return: `GenericObject`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `GenericObject`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_filter_set`

Provenance: Golden OpenAPI contract

Operation ID: `createFilterSet`

- Sync: `client.filters.create_filter_set(body=..., timeout=None)`
- Async: `await client.filters.create_filter_set(body=..., timeout=None)`
- Raw payload: `client.filters.create_filter_set.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/filters/sets/new`
- Source controller: `IncidentIQ API`

Create a new filter set

Creates a new filter set with the specified configuration. Filter sets are collections of filter criteria that can be used for:

- **Views**: Saved search filters for tickets, assets, or users
- **Rules**: Condition criteria for automation rules
- **Custom Fields**: Visibility and behavior conditions
- **Knowledge Base**: Article visibility conditions
- **Apps**: Application-specific filtering criteria

**Required Fields**:
- `FilterSetType` - Type of filter set (e.g., 'View.Filters')
- `EntityTypeId` - Entity type the filters apply to
- `ProductId` - Product context

**Authentication**: Supports both user authentication and app authorization tokens.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `FilterSet` | `FilterSet` | Filter set configuration to create. |

#### Returns

- Typed call return: `FilterSetCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `FilterSetCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_filter`

Provenance: Golden OpenAPI contract

Operation ID: `deleteFilter`

- Sync: `client.filters.delete_filter(filter_id=..., timeout=None)`
- Async: `await client.filters.delete_filter(filter_id=..., timeout=None)`
- Raw payload: `client.filters.delete_filter.raw(filter_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/filters/{FilterId}`
- Source controller: `IncidentIQ API`

Delete a filter

Deletes a filter definition by ID. Use this to remove a custom facet that should no longer appear in search or view builders.

**Prerequisites**
1. **FilterId** - Use [GET /api/v1.0/filters/for/entitytype/{entityTypeId}](#/Filters/listFiltersForEntityType) and extract `Items[].FilterId`.

**Workflow Example**
1. List filters for the entity type and capture the `FilterId` to remove.
2. Delete the filter: [DELETE /api/v1.0/filters/{FilterId}](#/Filters/deleteFilter).

**Minimal Required Fields**: FilterId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `filter_id` | `FilterId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_filter_by_origin_id`

Provenance: Golden OpenAPI contract

Operation ID: `deleteFilterByOriginId`

- Sync: `client.filters.delete_filter_by_origin_id(site_id=..., origin_id=..., is_product_specific=None, timeout=None)`
- Async: `await client.filters.delete_filter_by_origin_id(site_id=..., origin_id=..., is_product_specific=None, timeout=None)`
- Raw payload: `client.filters.delete_filter_by_origin_id.raw(site_id=..., origin_id=..., is_product_specific=None, timeout=None)`
- HTTP route: `DELETE /api/v1.0/filters/{SiteId}/origin/{OriginId}`
- Source controller: `IncidentIQ API`

Delete a filter by origin ID

Deletes a filter definition by its origin identifier, scoped to a site. This is typically used by integrations or apps that track their own IDs for custom filters.

**Prerequisites**
1. **SiteId** - Use [GET /api/v1.0/sites](#/Sites/getSiteByUrl) or your site context to determine the site UUID.
2. **OriginId** - Store the origin identifier used when the filter was created.

**Workflow Example**
1. Identify the site and origin identifier used by the integration.
2. (Optional) If product-specific, set `isProductSpecific=true`.
3. Delete the filter: [DELETE /api/v1.0/filters/{SiteId}/origin/{OriginId}](#/Filters/deleteFilterByOriginId).

**Minimal Required Fields**: SiteId and OriginId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `site_id` | `SiteId` | `path` | `yes` | `str` | `-` | - |
| `origin_id` | `OriginId` | `path` | `yes` | `str` | `-` | - |
| `is_product_specific` | `isProductSpecific` | `query` | `no` | `bool` | `-` | - |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_filter_set_value`

Provenance: Golden OpenAPI contract

Operation ID: `deleteFilterSetValue`

- Sync: `client.filters.delete_filter_set_value(filter_set_value_id=..., timeout=None)`
- Async: `await client.filters.delete_filter_set_value(filter_set_value_id=..., timeout=None)`
- Raw payload: `client.filters.delete_filter_set_value.raw(filter_set_value_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/filters/sets/values/{FilterSetValueId}`
- Source controller: `IncidentIQ API`

Delete a filter set value

Removes a specific filter value from a filter set. This permanently deletes the filter value and cannot be undone.

**Note**: Deleting filter values from filter sets that are actively used by views, rules, or custom fields will affect their behavior. Ensure the filter value is no longer needed before deletion.

**Authentication**: Supports both user authentication and app authorization tokens.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `filter_set_value_id` | `FilterSetValueId` | `path` | `yes` | `str` | `-` | UUID of the filter set value to delete. |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_custom_field_filter_sets_by_ids`

Provenance: Golden OpenAPI contract

Operation ID: `getCustomFieldFilterSetsByIds`

- Sync: `client.filters.get_custom_field_filter_sets_by_ids(body=..., timeout=None)`
- Async: `await client.filters.get_custom_field_filter_sets_by_ids(body=..., timeout=None)`
- Raw payload: `client.filters.get_custom_field_filter_sets_by_ids.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/filters/custom-fields/sets/ids/get`
- Source controller: `IncidentIQ API`

Get custom field filter sets by IDs

Retrieves multiple custom field filter sets by their IDs with fully populated filter definitions. Unlike the standard `getFilterSetsByIds`, this endpoint includes:

- Filter labels and display names
- Custom field type information
- Value selection metadata
- Complex editor configuration

**Use Cases**:
- Loading filter sets for custom field condition editors
- Rendering filter criteria with proper labels in UI
- Exporting filter configurations with full context

**Authentication**: Supports both user authentication and app authorization tokens.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | Array of filter set IDs to retrieve with custom field details. |

#### Returns

- Typed call return: `CustomFieldFilterSetListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CustomFieldFilterSetListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_custom_field_filter_value_labels`

Provenance: Golden OpenAPI contract

Operation ID: `getCustomFieldFilterValueLabels`

- Sync: `client.filters.get_custom_field_filter_value_labels(filter_id=..., custom_field_type_id=..., body=None, timeout=None)`
- Async: `await client.filters.get_custom_field_filter_value_labels(filter_id=..., custom_field_type_id=..., body=None, timeout=None)`
- Raw payload: `client.filters.get_custom_field_filter_value_labels.raw(filter_id=..., custom_field_type_id=..., body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/filters/label/{filterId}/for/custom-field/{customFieldTypeId}/values`
- Source controller: `IncidentIQ API`

Get labels for custom field filter values

Returns display labels for custom field filter values. This is useful when custom field filters store raw values that need to be translated into user-friendly labels.

**Prerequisites**
1. **filterId** - Use [GET /api/v1.0/filters/for/entitytype/{entityTypeId}](#/Filters/listFiltersForEntityType) and extract `Items[].FilterId`.
2. **customFieldTypeId** - Use [GET /api/v1.0/custom-fields/types](#/Custom%20Fields/listCustomFieldTypes) and extract `Items[].CustomFieldTypeId`.

**Workflow Example**
1. Collect the raw filter values stored in a view or filter set.
2. Submit the values array: [POST /api/v1.0/filters/label/{filterId}/for/custom-field/{customFieldTypeId}/values](#/Filters/getCustomFieldFilterValueLabels).
3. Replace raw values with returned labels in the UI.

**Minimal Required Fields**: filterId, customFieldTypeId (path), and a body array of values.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `filter_id` | `filterId` | `path` | `yes` | `str` | `-` | - |
| `custom_field_type_id` | `customFieldTypeId` | `path` | `yes` | `str` | `-` | - |
| `body` | `body` | `body` | `no` | `list[Any]` | `-` | - |

#### Returns

- Typed call return: `Any`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_filter_set`

Provenance: Golden OpenAPI contract

Operation ID: `getFilterSet`

- Sync: `client.filters.get_filter_set(filter_id=..., timeout=None)`
- Async: `await client.filters.get_filter_set(filter_id=..., timeout=None)`
- Raw payload: `client.filters.get_filter_set.raw(filter_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/filters/sets/{filterId}`
- Source controller: `IncidentIQ API`

Get filter set

Retrieves a single filter set (a stored collection of filter criteria) by ID, including its type, entity type, scope, and match rules. Use this to load saved view filters, automation rule conditions, or custom field visibility logic when you already have a filter set identifier.

**Prerequisites**
1. **filterId** - Use [GET /api/v1.0/filters/sets/for/type/{FilterSetType}](#/Filters/getFilterSetsByType) or [POST /api/v1.0/filters/sets/ids/get](#/Filters/getFilterSetsByIds) to obtain filter set IDs.

**Workflow Example**
1. List filter sets by type and select a `FilterSetId`.
2. Fetch the full filter set: [GET /api/v1.0/filters/sets/{filterId}](#/Filters/getFilterSet).
3. If you need the concrete selected values, call [GET /api/v1.0/filters/sets/{filterId}/values](#/Filters/getFilterSetValues).

**Minimal Required Fields**: filterId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `filter_id` | `filterId` | `path` | `yes` | `str` | `-` | The filterId parameter |

#### Returns

- Typed call return: `GenericObject`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `GenericObject`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_filter_set_values`

Provenance: Golden OpenAPI contract

Operation ID: `getFilterSetValues`

- Sync: `client.filters.get_filter_set_values(filter_id=..., timeout=None)`
- Async: `await client.filters.get_filter_set_values(filter_id=..., timeout=None)`
- Raw payload: `client.filters.get_filter_set_values.raw(filter_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/filters/sets/{filterId}/values`
- Source controller: `IncidentIQ API`

Get Filter Set Values

Returns the list of values assigned to a filter set, typically representing the concrete selections behind saved views, rules, or app criteria. Use this endpoint to hydrate filter chips, rebuild search payloads, or audit what a filter set actually selects.

**Prerequisites**
1. **filterId** - Use [GET /api/v1.0/filters/sets/for/type/{FilterSetType}](#/Filters/getFilterSetsByType) or [POST /api/v1.0/filters/sets/ids/get](#/Filters/getFilterSetsByIds) to obtain a filter set ID.

**Workflow Example**
1. Identify the filter set you need to inspect and capture its ID.
2. Retrieve the stored values: [GET /api/v1.0/filters/sets/{filterId}/values](#/Filters/getFilterSetValues).
3. If labels are needed, resolve each `FilterId` + `Value` with [POST /api/v1.0/filters/label/{filterId}/values](#/Filters/createFilterById).

**Minimal Required Fields**: filterId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `filter_id` | `filterId` | `path` | `yes` | `str` | `-` | The filterId parameter |

#### Returns

- Typed call return: `GenericObject`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `GenericObject`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_filter_sets_by_ids`

Provenance: Golden OpenAPI contract

Operation ID: `getFilterSetsByIds`

- Sync: `client.filters.get_filter_sets_by_ids(body=..., timeout=None)`
- Async: `await client.filters.get_filter_sets_by_ids(body=..., timeout=None)`
- Raw payload: `client.filters.get_filter_sets_by_ids.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/filters/sets/ids/get`
- Source controller: `IncidentIQ API`

Get filter sets by IDs

Retrieves multiple filter sets by their IDs in a single request. This is more efficient than making multiple individual requests when you need to load several filter sets.

**Use Cases**:
- Loading filter sets for multiple views at once
- Bulk processing of rule conditions
- Pre-fetching filter sets for UI rendering

**Authentication**: Supports both user authentication and app authorization tokens.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | Array of filter set IDs to retrieve. |

#### Returns

- Typed call return: `FilterSetListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `FilterSetListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_filter_sets_by_type`

Provenance: Golden OpenAPI contract

Operation ID: `getFilterSetsByType`

- Sync: `client.filters.get_filter_sets_by_type(filter_set_type=..., timeout=None)`
- Async: `await client.filters.get_filter_sets_by_type(filter_set_type=..., timeout=None)`
- Raw payload: `client.filters.get_filter_sets_by_type.raw(filter_set_type=..., timeout=None)`
- HTTP route: `GET /api/v1.0/filters/sets/for/type/{FilterSetType}`
- Source controller: `IncidentIQ API`

Get filter sets by type

Retrieves all filter sets matching the specified type. Filter sets are used throughout the system for views, rules, custom field conditions, and app-specific filtering.

**Common Filter Set Types**:
- `View.Filters` - Filter criteria saved with views
- `Rule.Condition` - Conditions used in automation rules
- `CustomField.Condition` - Conditions for custom field visibility/behavior
- `KbArticle.Condition` - Conditions for knowledge base articles
- `App.SparePool.Criteria` - Spare pool application criteria

**Authentication**: Supports both user authentication and app authorization tokens.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `filter_set_type` | `FilterSetType` | `path` | `yes` | `str` | `-` | The type of filter sets to retrieve. Use dot notation format (e.g., 'View.Filters', 'Rule.Condition'). |

#### Returns

- Typed call return: `FilterSetListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `FilterSetListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_filter_value_label`

Provenance: Golden OpenAPI contract

Operation ID: `getFilterValueLabel`

- Sync: `client.filters.get_filter_value_label(filter_id=..., value=..., timeout=None)`
- Async: `await client.filters.get_filter_value_label(filter_id=..., value=..., timeout=None)`
- Raw payload: `client.filters.get_filter_value_label.raw(filter_id=..., value=..., timeout=None)`
- HTTP route: `GET /api/v1.0/filters/label/{FilterId}/{Value}`
- Source controller: `IncidentIQ API`

Get the label for a filter value

Returns the display label for a specific filter value. Use this to turn stored filter values into human-friendly labels when rendering saved searches or audit logs.

**Prerequisites**
1. **FilterId** - Use [GET /api/v1.0/filters/for/entitytype/{entityTypeId}](#/Filters/listFiltersForEntityType) and extract `Items[].FilterId`.
2. **Value** - Use a value previously stored in a filter set or view definition.

**Workflow Example**
1. Identify the filter and value from a saved view or filter set.
2. Call [GET /api/v1.0/filters/label/{FilterId}/{Value}](#/Filters/getFilterValueLabel).
3. Render the returned label in the UI.

**Minimal Required Fields**: FilterId and Value (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `filter_id` | `FilterId` | `path` | `yes` | `str` | `-` | - |
| `value` | `Value` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `Any`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_filters`

Provenance: Golden OpenAPI contract

Operation ID: `listFilters`

- Sync: `client.filters.list_filters(timeout=None)`
- Async: `await client.filters.list_filters(timeout=None)`
- Raw payload: `client.filters.list_filters.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/filters`
- Source controller: `IncidentIQ API`

Get Filters

Returns the full catalog of filter definitions (facets) available to the tenant, including keys, labels, UI control types, and metadata used when building filter UIs or search payloads. Use this endpoint when you need a complete sync across entity types, then narrow the catalog with [GET /api/v1.0/filters/for/entitytype/{entityTypeId}](#/Filters/listFiltersForEntityType) for entity-specific pickers.

**Prerequisites**
1. None.

**Workflow Example**
1. Call this endpoint to cache all available filters for the tenant.
2. For a specific entity type, call [GET /api/v1.0/filters/for/entitytype/{entityTypeId}](#/Filters/listFiltersForEntityType) and match by `FilterId` or `Key`.
3. Use the selected filter keys in search requests, view definitions, or rule conditions.

**Minimal Required Fields**: None.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `GenericObject`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `GenericObject`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_filters_for_entity_type`

Provenance: Golden OpenAPI contract

Operation ID: `listFiltersForEntityType`

- Sync: `client.filters.list_filters_for_entity_type(entity_type_id=..., timeout=None)`
- Async: `await client.filters.list_filters_for_entity_type(entity_type_id=..., timeout=None)`
- Raw payload: `client.filters.list_filters_for_entity_type.raw(entity_type_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/filters/for/entitytype/{entityTypeId}`
- Source controller: `IncidentIQ API`

List filters for entity type

Returns all filter definitions (facets) that can be applied when searching for the specified entity type.

**Filter Metadata:**
- Facet key
- UI label
- Category
- Filter control type

Combine this endpoint with [GET /api/v1.0/categories/of/filters](#/Filters/listFilterCategories) to present filters grouped by category before constructing search payloads.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `entity_type_id` | `entityTypeId` | `path` | `yes` | `str` | `-` | Entity type identifier for which to retrieve available filters. Tickets, assets, and other modules each expose unique IDs for their filter catalogs. Retrieve entity type identifiers from [GET /api/v1.0/sites/my/settings](#/Sites/getMySiteSettings) by reading `Item.EntityTypes[].EntityTypeId`. |

#### Returns

- Typed call return: `FilterDefinitionListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `FilterDefinitionListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `save_filter_values_for_kb_articles`

Provenance: Golden OpenAPI contract

Operation ID: `saveFilterValuesForKbArticles`

- Sync: `client.filters.save_filter_values_for_kb_articles(body=None, timeout=None)`
- Async: `await client.filters.save_filter_values_for_kb_articles(body=None, timeout=None)`
- Raw payload: `client.filters.save_filter_values_for_kb_articles.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/filters/values/for/kb-articles`
- Source controller: `IncidentIQ API`

Save filter values for knowledge base articles

Saves filter values for one or more knowledge base articles. Use this when tagging KB content with filter metadata so it can be discovered by saved searches or view filters.

**Prerequisites**
1. **Ids** - Use your KB article list/search endpoints to collect article IDs.
2. **Values** - Build `EntityFilterValue` entries for each filter/value pair to assign.

**Workflow Example**
1. Identify target KB articles and collect their IDs.
2. Build a `FilterValueSaveRequest` with `Ids` and `Values`.
3. Save values: [POST /api/v1.0/filters/values/for/kb-articles](#/Filters/saveFilterValuesForKbArticles).

**Minimal Required Fields**: `Ids` and `Values`.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `FilterValueSaveRequest` | `FilterValueSaveRequest` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `save_filter_values_for_views`

Provenance: Golden OpenAPI contract

Operation ID: `saveFilterValuesForViews`

- Sync: `client.filters.save_filter_values_for_views(body=None, timeout=None)`
- Async: `await client.filters.save_filter_values_for_views(body=None, timeout=None)`
- Raw payload: `client.filters.save_filter_values_for_views.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/filters/values/for/views`
- Source controller: `IncidentIQ API`

Save filter values for views

Saves filter values for one or more saved views. Use this to associate filter metadata with view records so they can be listed, shared, or executed consistently.

**Prerequisites**
1. **Ids** - Use view list endpoints (for example, [GET /api/v1.0/tickets/views](#/Tickets/listTicketViews)) to collect view IDs.
2. **Values** - Build `EntityFilterValue` entries that represent the filters assigned to the view.

**Workflow Example**
1. List views and collect the target IDs.
2. Build a `FilterValueSaveRequest` with `Ids` and `Values`.
3. Save values: [POST /api/v1.0/filters/values/for/views](#/Filters/saveFilterValuesForViews).

**Minimal Required Fields**: `Ids` and `Values`.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `FilterValueSaveRequest` | `FilterValueSaveRequest` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_filter`

Provenance: Golden OpenAPI contract

Operation ID: `updateFilter`

- Sync: `client.filters.update_filter(filter_id=..., body=None, timeout=None)`
- Async: `await client.filters.update_filter(filter_id=..., body=None, timeout=None)`
- Raw payload: `client.filters.update_filter.raw(filter_id=..., body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/filters/{FilterId}`
- Source controller: `IncidentIQ API`

Update an existing filter

Updates an existing filter definition (facet) so you can rename it, move it into a different category, or tweak UI metadata without creating a new key. This preserves saved views, rule conditions, and other references that rely on the existing `FilterId`.

**Prerequisites**
1. **FilterId** - Use [GET /api/v1.0/filters/for/entitytype/{entityTypeId}](#/Filters/listFiltersForEntityType) and extract `Items[].FilterId` for the filter you want to update.

**Workflow Example**
1. List filters for the entity type and capture the `FilterId` to update.
2. Build a `FilterDefinition` with only the fields you want to change (for example, `Name`, `CategoryId`, or visibility flags).
3. Save the update: [POST /api/v1.0/filters/{FilterId}](#/Filters/updateFilter).

**Minimal Required Fields**: `FilterId` (path) plus at least one field in the body to update (commonly `Name` or `CategoryId`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `filter_id` | `FilterId` | `path` | `yes` | `str` | `-` | - |
| `body` | `body` | `body` | `no` | `FilterDefinition` | `FilterDefinition` | - |

#### Returns

- Typed call return: `Any`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
