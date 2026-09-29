# `custom_fields` Golden Namespace

Sync client access: `client.custom_fields`

Async client access: `client.custom_fields` with `await` on method calls.

These methods are Golden because they come from the bundled Incident IQ OpenAPI contract.

## Methods

### `batch_create_custom_field_entity_mappings`

Provenance: Golden OpenAPI contract

Operation ID: `batchCreateCustomFieldEntityMappings`

- Sync: `client.custom_fields.batch_create_custom_field_entity_mappings(body=..., timeout=None)`
- Async: `await client.custom_fields.batch_create_custom_field_entity_mappings(body=..., timeout=None)`
- Raw payload: `client.custom_fields.batch_create_custom_field_entity_mappings.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/custom-fields/entity-mappings/batch`
- Source controller: `IncidentIQ API`

Batch create custom field entity mappings

Creates multiple custom field entity mappings in a single request. Each mapping defines how data flows from a source entity's custom field to a target entity's field. Returns the created mappings with their generated IDs.

**Workflow:**
1. Call GET /entity-mappings/entity-types to discover available entities and fields
2. Optionally call POST /compatible-fields to verify field compatibility
3. Submit batch request with array of mapping definitions
4. Receive created mappings with assigned IDs
5. Mappings take effect immediately for relevant entity operations

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `BatchCustomFieldEntityMappingRequest` | `BatchCustomFieldEntityMappingRequest` | - |

#### Returns

- Typed call return: `ListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `batch_create_custom_field_types`

Provenance: Golden OpenAPI contract

Operation ID: `batchCreateCustomFieldTypes`

- Sync: `client.custom_fields.batch_create_custom_field_types(body=..., timeout=None)`
- Async: `await client.custom_fields.batch_create_custom_field_types(body=..., timeout=None)`
- Raw payload: `client.custom_fields.batch_create_custom_field_types.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/custom-fields/types/new/batch`
- Source controller: `IncidentIQ API`

Batch create custom field types

Creates multiple custom field types in a single request. This endpoint is useful for bulk provisioning custom field definitions during system setup or configuration import.

**Prerequisites**: None - creates new custom field types from provided definitions

**Workflow Example**:
1. Prepare an array of custom field type definitions following the CustomFieldTypeCreateRequest schema
2. Submit all definitions in a single POST request
3. Review the returned Items array to verify all custom field types were created
4. Use the returned CustomFieldTypeId values for subsequent custom field operations

**Minimal Required Fields**: Array with at least one custom field type definition containing Name, EditorType, Scope, and IsEdit=true

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `CustomFieldTypeBatchCreateRequest` | `CustomFieldTypeBatchCreateRequest` | - |

#### Returns

- Typed call return: `ListCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `batch_delete_custom_field_entity_mappings`

Provenance: Golden OpenAPI contract

Operation ID: `batchDeleteCustomFieldEntityMappings`

- Sync: `client.custom_fields.batch_delete_custom_field_entity_mappings(body=..., timeout=None)`
- Async: `await client.custom_fields.batch_delete_custom_field_entity_mappings(body=..., timeout=None)`
- Raw payload: `client.custom_fields.batch_delete_custom_field_entity_mappings.raw(body=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/custom-fields/entity-mappings/batch`
- Source controller: `IncidentIQ API`

Batch delete custom field entity mappings

Deletes multiple custom field entity mappings by their IDs. Once deleted, data will no longer flow between the previously mapped fields.

**Workflow:**
1. Call GET /entity-mappings to list existing mappings
2. Identify mapping IDs to delete
3. Submit batch delete request with array of mapping IDs
4. Mappings are removed immediately

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `UuidList` | `UuidList` | - |

#### Returns

- Typed call return: `ListDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `batch_update_custom_field_product`

Provenance: Golden OpenAPI contract

Operation ID: `batchUpdateCustomFieldProduct`

- Sync: `client.custom_fields.batch_update_custom_field_product(body=..., timeout=None)`
- Async: `await client.custom_fields.batch_update_custom_field_product(body=..., timeout=None)`
- Raw payload: `client.custom_fields.batch_update_custom_field_product.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/custom-fields/product/update/batch`
- Source controller: `IncidentIQ API`

Batch update custom field product associations

Updates product associations for multiple custom fields in a single request. This endpoint allows bulk reassignment of custom fields to different products, useful when reorganizing custom field availability across products.

**Prerequisites**:
1. **CustomFieldIds** - Obtain field UUIDs from [POST /api/v1.0/custom-fields](#/Custom%20Fields/searchCustomFields)
2. **ProductId** - Product UUID to associate the custom fields with

**Workflow Example**:
1. Search for custom fields to identify which fields to reassign: [POST /api/v1.0/custom-fields](#/Custom Fields/searchCustomFields)
2. Extract CustomFieldId values from the response
3. Prepare product filter value with target ProductId
4. Submit update request with array of CustomFieldIds and product Values
5. Custom fields are now associated with the specified product

**Minimal Required Fields**: Ids array with CustomFieldId values, Values array with at least one EntityFilterValue containing target ProductId

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `CustomFieldProductUpdateRequest` | `CustomFieldProductUpdateRequest` | - |

#### Returns

- Typed call return: `ItemUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `batch_update_custom_field_types`

Provenance: Golden OpenAPI contract

Operation ID: `batchUpdateCustomFieldTypes`

- Sync: `client.custom_fields.batch_update_custom_field_types(body=..., timeout=None)`
- Async: `await client.custom_fields.batch_update_custom_field_types(body=..., timeout=None)`
- Raw payload: `client.custom_fields.batch_update_custom_field_types.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/custom-fields/types/update/batch`
- Source controller: `IncidentIQ API`

Batch update custom field types

Updates multiple custom field types in a single request. This endpoint is useful for bulk configuration changes across multiple custom field definitions.

**Prerequisites**:
1. **CustomFieldTypeIds** - Obtain type UUIDs from [GET /api/v1.0/custom-fields/types](#/Custom%20Fields/listCustomFieldTypes) or [POST /api/v1.0/custom-fields/types](#/Custom%20Fields/searchCustomFieldTypes)

**Workflow Example**:
1. List custom field types to identify which types to update
2. For each type to update, include its CustomFieldTypeId and the properties to change
3. Submit all updates in a single POST request
4. Review the returned Items array to verify all updates were applied

**Minimal Required Fields**: Array with at least one update object containing CustomFieldTypeId and properties to update

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `CustomFieldTypeBatchUpdateRequest` | `CustomFieldTypeBatchUpdateRequest` | - |

#### Returns

- Typed call return: `ListUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `check_custom_field_mapping_compatibility`

Provenance: Golden OpenAPI contract

Operation ID: `checkCustomFieldMappingCompatibility`

- Sync: `client.custom_fields.check_custom_field_mapping_compatibility(body=..., timeout=None)`
- Async: `await client.custom_fields.check_custom_field_mapping_compatibility(body=..., timeout=None)`
- Raw payload: `client.custom_fields.check_custom_field_mapping_compatibility.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/custom-fields/entity-mappings/check-field-compatibility`
- Source controller: `IncidentIQ API`

Check if two fields are compatible for mapping

Validates whether a source field and target field are compatible for entity mapping. Returns a boolean indicating compatibility based on data types and editor types.

**Workflow:**
1. Select source and target fields from available fields
2. Submit compatibility check request
3. Receive boolean response (true = compatible, false = incompatible)
4. Proceed with mapping creation only if compatible

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `CheckFieldMappingCompatibilityRequest` | `CheckFieldMappingCompatibilityRequest` | - |

#### Returns

- Typed call return: `ItemGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_custom_field_batch`

Provenance: Golden OpenAPI contract

Operation ID: `createCustomFieldBatch`

- Sync: `client.custom_fields.create_custom_field_batch(body=..., timeout=None)`
- Async: `await client.custom_fields.create_custom_field_batch(body=..., timeout=None)`
- Raw payload: `client.custom_fields.create_custom_field_batch.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/custom-fields/new`
- Source controller: `IncidentIQ API`

Create custom fields (batch)

Creates one or more custom field instances in bulk. This endpoint differs from [POST /api/v1.0/custom-fields/types/new](#/Custom%20Fields/createCustomFieldType) which creates custom field **types**. This operation creates custom field **instances** that apply custom field types to specific entity types (Assets, Tickets, Users, etc.).

**Key Differences**:
- This endpoint creates custom field instances (relationships between field types and entity types)
- The single-type creation endpoint creates the field type definitions themselves
- Use this for applying existing field types to entities or creating new instances

**Prerequisites**:
1. **CustomFieldTypeId** - Obtain from [POST /api/v1.0/custom-fields/types](#/Custom%20Fields/searchCustomFieldTypes) or create via [POST /api/v1.0/custom-fields/types/new](#/Custom%20Fields/createCustomFieldType)
2. **EntityTypeId** - Standard entity type UUIDs (Assets, Tickets, Users, etc.) - available from site configuration

**Workflow Example** (Adding a warranty field to assets):
1. Get or create the custom field type for "Warranty Expiration Date"
2. Call this endpoint to create the custom field instance: [POST /api/v1.0/custom-fields/new](#/Custom Fields/createCustomFieldBatch) with `CustomFieldTypeId`, `EntityTypeId` for Assets, and configuration
3. The custom field is now available for all assets

**Minimal Required Fields**: CustomFieldTypeId, EntityTypeId

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `CreateCustomFieldBatchCustomFieldsNewRequest` | `CreateCustomFieldBatchCustomFieldsNewRequest` | - |

#### Returns

- Typed call return: `CustomFieldListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CustomFieldListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_custom_field_type`

Provenance: Golden OpenAPI contract

Operation ID: `createCustomFieldType`

- Sync: `client.custom_fields.create_custom_field_type(body=..., timeout=None)`
- Async: `await client.custom_fields.create_custom_field_type(body=..., timeout=None)`
- Raw payload: `client.custom_fields.create_custom_field_type.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/custom-fields/types/new`
- Source controller: `IncidentIQ API`

Create custom field type

Creates a new custom field type that can be assigned within the specified scope.

**Prerequisites**: None. Provide all configuration details in the request payload.

**Workflow Example**:
1. Determine the target scope (e.g., `Site`) and the editor to use, referencing the `CustomFieldEditorTypeId` enumeration.
2. Submit this operation with the desired configuration payload to register the new field type.

**Minimal Required Fields**: Name, EditorType, Scope

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `CustomFieldTypeCreateRequest` | `CustomFieldTypeCreateRequest` | - |

#### Returns

- Typed call return: `CustomFieldTypeCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CustomFieldTypeCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_asset_inventory_action_custom_field_values`

Provenance: Golden OpenAPI contract

Operation ID: `deleteAssetInventoryActionCustomFieldValues`

- Sync: `client.custom_fields.delete_asset_inventory_action_custom_field_values(body=..., timeout=None)`
- Async: `await client.custom_fields.delete_asset_inventory_action_custom_field_values(body=..., timeout=None)`
- Raw payload: `client.custom_fields.delete_asset_inventory_action_custom_field_values.raw(body=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/custom-fields/values/for/asset-inventory-actions/delete`
- Source controller: `IncidentIQ API`

Delete asset inventory action custom field values

Deletes custom field values for one or more asset inventory actions based on the provided criteria.

**Key Behavior**:
- Allows bulk deletion of custom field values across multiple asset inventory actions
- Can filter by specific custom field types or delete all custom fields for specified actions
- Returns the count of deleted custom field values

**Prerequisites**:
1. **AssetInventoryActionIds** - Obtain asset inventory action UUIDs from asset inventory action search endpoints
2. **CustomFieldTypeIds** (optional) - If provided, only deletes values for these specific custom field types

**Workflow Example**:
1. Identify the asset inventory actions and extract their `AssetInventoryActionId` values
2. Optionally, identify specific custom field types to delete via [POST /api/v1.0/custom-fields/for/asset-inventory-action](#/Custom%20Fields/getCustomFieldsForAssetInventoryAction)
3. Call this endpoint with the delete request payload

**Minimal Required Fields**: IncludePkIds array (containing AssetInventoryActionId values)

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `DeleteCustomFieldValuesRequest` | `DeleteCustomFieldValuesRequest` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_custom_field`

Provenance: Golden OpenAPI contract

Operation ID: `deleteCustomField`

- Sync: `client.custom_fields.delete_custom_field(custom_field_id=..., timeout=None)`
- Async: `await client.custom_fields.delete_custom_field(custom_field_id=..., timeout=None)`
- Raw payload: `client.custom_fields.delete_custom_field.raw(custom_field_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/custom-fields/{customFieldId}`
- Source controller: `IncidentIQ API`

Delete custom field

Deletes a single custom field definition.

**Warning**: This operation permanently removes the custom field and all associated values from entities.

**Prerequisites**:
- Obtain the `CustomFieldId` from [POST /api/v1.0/custom-fields](#/Custom%20Fields/searchCustomFields)

**Workflow Example**:
1. Search for custom fields: [POST /api/v1.0/custom-fields](#/Custom Fields/searchCustomFields) → extract target `CustomFieldId`
2. Delete the field using this endpoint

**Minimal Required Fields**: customFieldId path parameter

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `custom_field_id` | `customFieldId` | `path` | `yes` | `str` | `-` | UUID of the custom field to delete |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_custom_field_type`

Provenance: Golden OpenAPI contract

Operation ID: `deleteCustomFieldType`

- Sync: `client.custom_fields.delete_custom_field_type(custom_field_type_id=..., timeout=None)`
- Async: `await client.custom_fields.delete_custom_field_type(custom_field_type_id=..., timeout=None)`
- Raw payload: `client.custom_fields.delete_custom_field_type.raw(custom_field_type_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/custom-fields/types/{customFieldTypeId}`
- Source controller: `IncidentIQ API`

Delete custom field type

Deletes an existing custom field type.

**Prerequisites**:
1. Use [GET /api/v1.0/custom-fields/types](#/Custom%20Fields/listCustomFieldTypes) to identify the `CustomFieldTypeId` value to delete.

**Workflow Example**:
1. List current custom field types and capture the `CustomFieldTypeId` for the target field.
2. Call this operation with the captured identifier to remove the field definition.

**Minimal Required Fields**: customFieldTypeId path parameter

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `custom_field_type_id` | `customFieldTypeId` | `path` | `yes` | `str` | `-` | UUID of the custom field type to delete. Obtain this value by listing custom field types and reading `Items[].CustomFieldTypeId`. |

#### Returns

- Typed call return: `CustomFieldTypeDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CustomFieldTypeDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_custom_field_values_for_assets`

Provenance: Golden OpenAPI contract

Operation ID: `deleteCustomFieldValuesForAssets`

- Sync: `client.custom_fields.delete_custom_field_values_for_assets(body=..., timeout=None)`
- Async: `await client.custom_fields.delete_custom_field_values_for_assets(body=..., timeout=None)`
- Raw payload: `client.custom_fields.delete_custom_field_values_for_assets.raw(body=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/custom-fields/values/for/assets/delete`
- Source controller: `IncidentIQ API`

Delete custom field values for assets

Deletes custom field values for one or more assets. This endpoint allows targeted deletion using custom field IDs and/or asset IDs.

**Key Behavior**:
- When `CustomFieldIds` is specified: Only deletes values for those specific custom field types
- When `IncludePkIds` is specified: Only deletes values for those specific assets
- When `ExcludePkIds` is specified: Protects those assets from deletion even if they match other criteria
- The endpoint returns the count of custom field values deleted

**Prerequisites**:
1. **CustomFieldIds** (optional) - Obtain from [POST /api/v1.0/custom-fields](#/Custom%20Fields/searchCustomFields) response `Items[].CustomFieldId`
2. **IncludePkIds** (optional) - Asset IDs from [POST /api/v1.0/assets](#/Assets/searchAssets) response `Items[].AssetId`

**Workflow Example**:
1. To delete a specific custom field value from specific assets: POST with `{"CustomFieldIds": ["field-uuid"], "IncludePkIds": ["asset-uuid-1", "asset-uuid-2"]}`
2. To delete all custom field values from a specific asset: POST with `{"IncludePkIds": ["asset-uuid"]}`
3. To delete a custom field from all assets except specific ones: POST with `{"CustomFieldIds": ["field-uuid"], "ExcludePkIds": ["protected-asset-uuid"]}`

**Minimal Required Fields**: At least one of CustomFieldIds, IncludePkIds, or ExcludePkIds

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `DeleteCustomFieldValuesRequest` | `DeleteCustomFieldValuesRequest` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_custom_field_values_for_events`

Provenance: Golden OpenAPI contract

Operation ID: `deleteCustomFieldValuesForEvents`

- Sync: `client.custom_fields.delete_custom_field_values_for_events(body=..., timeout=None)`
- Async: `await client.custom_fields.delete_custom_field_values_for_events(body=..., timeout=None)`
- Raw payload: `client.custom_fields.delete_custom_field_values_for_events.raw(body=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/custom-fields/values/for/events/delete`
- Source controller: `IncidentIQ API`

Delete custom field values for events

Deletes custom field values for one or more events. This endpoint allows targeted deletion using custom field IDs and/or event IDs.

**Key Behavior**:
- When `CustomFieldIds` is specified: Only deletes values for those specific custom field types
- When `IncludePkIds` is specified: Only deletes values for those specific events
- When `ExcludePkIds` is specified: Protects those events from deletion even if they match other criteria
- The endpoint returns the count of custom field values deleted

**Prerequisites**:
1. **CustomFieldIds** (optional) - Obtain from [POST /api/v1.0/custom-fields](#/Custom%20Fields/searchCustomFields) response `Items[].CustomFieldId`
2. **IncludePkIds** (optional) - Event IDs from event search endpoints

**Workflow Example**:
1. To delete a specific custom field value from specific events: POST with `{"CustomFieldIds": ["field-uuid"], "IncludePkIds": ["event-uuid-1", "event-uuid-2"]}`
2. To delete all custom field values from a specific event: POST with `{"IncludePkIds": ["event-uuid"]}`
3. To delete a custom field from all events except specific ones: POST with `{"CustomFieldIds": ["field-uuid"], "ExcludePkIds": ["protected-event-uuid"]}`

**Minimal Required Fields**: At least one of CustomFieldIds, IncludePkIds, or ExcludePkIds

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `DeleteCustomFieldValuesRequest` | `DeleteCustomFieldValuesRequest` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_custom_field_values_for_tickets`

Provenance: Golden OpenAPI contract

Operation ID: `deleteCustomFieldValuesForTickets`

- Sync: `client.custom_fields.delete_custom_field_values_for_tickets(body=..., timeout=None)`
- Async: `await client.custom_fields.delete_custom_field_values_for_tickets(body=..., timeout=None)`
- Raw payload: `client.custom_fields.delete_custom_field_values_for_tickets.raw(body=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/custom-fields/values/for/tickets/delete`
- Source controller: `IncidentIQ API`

Delete custom field values for tickets

Deletes custom field values for one or more tickets. This endpoint allows targeted deletion using custom field IDs and/or ticket IDs.

**Key Behavior**:
- When `CustomFieldIds` is specified: Only deletes values for those specific custom field types
- When `IncludePkIds` is specified: Only deletes values for those specific tickets
- When `ExcludePkIds` is specified: Protects those tickets from deletion even if they match other criteria
- The endpoint returns the count of custom field values deleted

**Prerequisites**:
1. **CustomFieldIds** (optional) - Obtain from [POST /api/v1.0/custom-fields](#/Custom%20Fields/searchCustomFields) response `Items[].CustomFieldId`
2. **IncludePkIds** (optional) - Ticket IDs from [POST /api/v1.0/tickets](#/Tickets/searchTickets) response `Items[].TicketId`

**Workflow Example**:
1. To delete a specific custom field value from specific tickets: POST with `{"CustomFieldIds": ["field-uuid"], "IncludePkIds": ["ticket-uuid-1", "ticket-uuid-2"]}`
2. To delete all custom field values from a specific ticket: POST with `{"IncludePkIds": ["ticket-uuid"]}`
3. To delete a custom field from all tickets except specific ones: POST with `{"CustomFieldIds": ["field-uuid"], "ExcludePkIds": ["protected-ticket-uuid"]}`

**Minimal Required Fields**: At least one of CustomFieldIds, IncludePkIds, or ExcludePkIds

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `DeleteCustomFieldValuesRequest` | `DeleteCustomFieldValuesRequest` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_custom_field_values_for_users`

Provenance: Golden OpenAPI contract

Operation ID: `deleteCustomFieldValuesForUsers`

- Sync: `client.custom_fields.delete_custom_field_values_for_users(body=..., timeout=None)`
- Async: `await client.custom_fields.delete_custom_field_values_for_users(body=..., timeout=None)`
- Raw payload: `client.custom_fields.delete_custom_field_values_for_users.raw(body=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/custom-fields/values/for/users/delete`
- Source controller: `IncidentIQ API`

Delete custom field values for users

Deletes custom field values for one or more users. This endpoint allows targeted deletion using custom field IDs and/or user IDs.

**Key Behavior**:
- When `CustomFieldIds` is specified: Only deletes values for those specific custom field types
- When `IncludePkIds` is specified: Only deletes values for those specific users
- When `ExcludePkIds` is specified: Protects those users from deletion even if they match other criteria
- The endpoint returns the count of custom field values deleted

**Prerequisites**:
1. **CustomFieldIds** (optional) - Obtain from [POST /api/v1.0/custom-fields](#/Custom%20Fields/searchCustomFields) response `Items[].CustomFieldId`
2. **IncludePkIds** (optional) - User IDs from [POST /api/v1.0/users](#/Users/searchUsers) response `Items[].UserId`

**Workflow Example**:
1. To delete a specific custom field value from specific users: POST with `{"CustomFieldIds": ["field-uuid"], "IncludePkIds": ["user-uuid-1", "user-uuid-2"]}`
2. To delete all custom field values from a specific user: POST with `{"IncludePkIds": ["user-uuid"]}`
3. To delete a custom field from all users except specific ones: POST with `{"CustomFieldIds": ["field-uuid"], "ExcludePkIds": ["protected-user-uuid"]}`

**Minimal Required Fields**: At least one of CustomFieldIds, IncludePkIds, or ExcludePkIds

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `DeleteCustomFieldValuesRequest` | `DeleteCustomFieldValuesRequest` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_asset_custom_field_values`

Provenance: Golden OpenAPI contract

Operation ID: `getAssetCustomFieldValues`

- Sync: `client.custom_fields.get_asset_custom_field_values(s=None, p=None, filter=None, timeout=None)`
- Async: `await client.custom_fields.get_asset_custom_field_values(s=None, p=None, filter=None, timeout=None)`
- Raw payload: `client.custom_fields.get_asset_custom_field_values.raw(s=None, p=None, filter=None, timeout=None)`
- HTTP route: `GET /api/v1.0/custom-fields/assets/values`
- Source controller: `IncidentIQ API`

Get asset custom field values

Retrieves a paginated list of asset custom field values across all assets. Use this endpoint to query custom field values with filtering and pagination.

**Key Behavior**:
- Returns custom field values from all assets the authenticated user has access to
- Supports pagination via `$s` (page size) and `$p` (page index) query parameters
- Supports filtering via `$filter` query parameter (refer to custom filter documentation)
- Default sort order is by CustomFieldTypeId ascending

**Use Cases**:
- Bulk export of custom field values for reporting
- Finding all assets with a specific custom field value
- Auditing custom field usage across assets

**Workflow Example**:
1. Call [GET /api/v1.0/custom-fields/assets/values](#/Custom%20Fields/getAssetCustomFieldValues) with `$s` and `$p` query parameters for pagination
2. To filter by custom field type: Use `$filter` query parameter with CustomFieldTypeId

**Minimal Required Fields**: None (uses defaults)

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of records per page |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index to retrieve |
| `filter` | `$filter` | `query` | `no` | `str` | `-` | Filter expression for custom field values |

#### Returns

- Typed call return: `AssetCustomFieldValueListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetCustomFieldValueListResponse`
- Pagination helper: `client.custom_fields.get_asset_custom_field_values.iter_pages(start_page=1, page_size=100, max_pages=None, s=None, p=None, filter=None, timeout=None)`

---

### `get_asset_inventory_action_custom_field_values`

Provenance: Golden OpenAPI contract

Operation ID: `getAssetInventoryActionCustomFieldValues`

- Sync: `client.custom_fields.get_asset_inventory_action_custom_field_values(id=..., timeout=None)`
- Async: `await client.custom_fields.get_asset_inventory_action_custom_field_values(id=..., timeout=None)`
- Raw payload: `client.custom_fields.get_asset_inventory_action_custom_field_values.raw(id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/custom-fields/values/for/asset-inventory-action/{id}`
- Source controller: `IncidentIQ API`

Get custom field values for asset inventory action

Retrieves all custom field values for a specific asset inventory action.

**Prerequisites**:
- Obtain the `AssetInventoryActionId` from asset inventory action search endpoints

**Workflow Example**:
1. Search for the asset inventory action and extract `AssetInventoryActionId`
2. Call this endpoint with the asset inventory action ID to retrieve all custom field values

**Minimal Required Fields**: id path parameter (AssetInventoryActionId)

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `id` | `path` | `yes` | `str` | `-` | UUID of the asset inventory action to retrieve custom field values for |

#### Returns

- Typed call return: `AssetInventoryActionCustomFieldValueListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetInventoryActionCustomFieldValueListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_custom_field_by_id`

Provenance: Golden OpenAPI contract

Operation ID: `getCustomFieldById`

- Sync: `client.custom_fields.get_custom_field_by_id(custom_field_id=..., timeout=None)`
- Async: `await client.custom_fields.get_custom_field_by_id(custom_field_id=..., timeout=None)`
- Raw payload: `client.custom_fields.get_custom_field_by_id.raw(custom_field_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/custom-fields/{customFieldId}`
- Source controller: `IncidentIQ API`

Get custom field by ID

Retrieves a single custom field definition by its unique identifier.

**Prerequisites**:
- Obtain the `CustomFieldId` from [POST /api/v1.0/custom-fields](#/Custom%20Fields/searchCustomFields) or from entity-specific endpoints like [POST /api/v1.0/custom-fields/for/asset](#/Custom%20Fields/getCustomFieldsForAsset).

**Workflow Example**:
1. Search for custom fields using [POST /api/v1.0/custom-fields](#/Custom Fields/searchCustomFields) → extract `Items[].CustomFieldId`
2. Call this endpoint with the CustomFieldId to get the full field definition including its type configuration

**Minimal Required Fields**: customFieldId path parameter

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `custom_field_id` | `customFieldId` | `path` | `yes` | `str` | `-` | UUID of the custom field to retrieve. Obtain from POST /api/v1.0/custom-fields response `Items[].CustomFieldId`. |

#### Returns

- Typed call return: `CustomFieldGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CustomFieldGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_custom_field_entity_mapping_entity_types`

Provenance: Golden OpenAPI contract

Operation ID: `getCustomFieldEntityMappingEntityTypes`

- Sync: `client.custom_fields.get_custom_field_entity_mapping_entity_types(timeout=None)`
- Async: `await client.custom_fields.get_custom_field_entity_mapping_entity_types(timeout=None)`
- Raw payload: `client.custom_fields.get_custom_field_entity_mapping_entity_types.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/custom-fields/entity-mappings/entity-types`
- Source controller: `IncidentIQ API`

Get available entity types for mappings

Retrieves all entity types that support custom field entity mappings, along with their available fields (both custom and database fields). This endpoint is typically called first to discover which entities and fields can participate in mappings.

**Workflow:**
1. Call this endpoint to discover available entity types
2. Examine each entity type's Fields array to see mappable fields
3. Use entity type IDs and field information when creating mappings

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `InlineObject`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InlineObject`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_custom_field_entity_mappings`

Provenance: Golden OpenAPI contract

Operation ID: `getCustomFieldEntityMappings`

- Sync: `client.custom_fields.get_custom_field_entity_mappings(timeout=None)`
- Async: `await client.custom_fields.get_custom_field_entity_mappings(timeout=None)`
- Raw payload: `client.custom_fields.get_custom_field_entity_mappings.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/custom-fields/entity-mappings`
- Source controller: `IncidentIQ API`

List all custom field entity mappings

Retrieves all custom field entity mappings for the authenticated site. Entity mappings define how data flows between custom fields on related entities (e.g., copying asset custom field values to tickets).

**Workflow:**
1. Authenticate and obtain session token
2. Call this endpoint to list all configured entity mappings
3. Examine mappings to understand data flow configuration
4. Use mapping IDs for updates or deletions

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `InlineObject`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InlineObject`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_custom_field_mapping_compatible_fields`

Provenance: Golden OpenAPI contract

Operation ID: `getCustomFieldMappingCompatibleFields`

- Sync: `client.custom_fields.get_custom_field_mapping_compatible_fields(body=..., timeout=None)`
- Async: `await client.custom_fields.get_custom_field_mapping_compatible_fields(body=..., timeout=None)`
- Raw payload: `client.custom_fields.get_custom_field_mapping_compatible_fields.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/custom-fields/entity-mappings/compatible-fields`
- Source controller: `IncidentIQ API`

Get compatible target fields for mapping

Given a source entity type and custom field, returns all compatible fields on the target entity that can be mapped to. Compatibility is determined by editor types and data types.

**Workflow:**
1. Call GET /entity-mappings/entity-types to get source entity and custom field IDs
2. Submit this request with source field and target entity type
3. Receive list of compatible fields on target entity
4. Use compatible field information when creating entity mappings

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `GetCustomFieldMappingCompatibleFieldsRequest` | `GetCustomFieldMappingCompatibleFieldsRequest` | - |

#### Returns

- Typed call return: `ListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_custom_field_type_by_id`

Provenance: Golden OpenAPI contract

Operation ID: `getCustomFieldTypeById`

- Sync: `client.custom_fields.get_custom_field_type_by_id(custom_field_type_id=..., timeout=None)`
- Async: `await client.custom_fields.get_custom_field_type_by_id(custom_field_type_id=..., timeout=None)`
- Raw payload: `client.custom_fields.get_custom_field_type_by_id.raw(custom_field_type_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/custom-fields/types/{customFieldTypeId}`
- Source controller: `IncidentIQ API`

Get custom field type

Retrieves a specific custom field type definition. Custom field IDs are commonly surfaced in asset and ticket payloads (for example, `AssetCustomFieldValue.CustomFieldTypeId` or `TicketCustomField.CustomFieldTypeId`). Use this operation whenever you need the full configuration for one of those identifiers.

**Prerequisites**:
- Obtain the `CustomFieldTypeId` from an existing record (asset, ticket, or another API response) that includes custom field metadata.

**Workflow Example**:
1. Retrieve an asset or ticket and capture the `CustomFieldTypeId` associated with a custom field value.
2. Call this operation with that identifier to inspect the custom field definition, editor configuration, and options.

**Minimal Required Fields**: customFieldTypeId path parameter

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `custom_field_type_id` | `customFieldTypeId` | `path` | `yes` | `str` | `-` | UUID of the custom field type to retrieve. Capture this value from asset or ticket responses that reference custom field definitions. |

#### Returns

- Typed call return: `CustomFieldTypeDetail`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CustomFieldTypeDetail`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_custom_field_values_for_asset`

Provenance: Golden OpenAPI contract

Operation ID: `getCustomFieldValuesForAsset`

- Sync: `client.custom_fields.get_custom_field_values_for_asset(asset_id=..., timeout=None)`
- Async: `await client.custom_fields.get_custom_field_values_for_asset(asset_id=..., timeout=None)`
- Raw payload: `client.custom_fields.get_custom_field_values_for_asset.raw(asset_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/custom-fields/values/for/asset/{assetId}`
- Source controller: `IncidentIQ API`

Get custom field values for asset

Retrieves all custom field values set for a specific asset.

**Prerequisites**:
- Obtain the `AssetId` from [POST /api/v1.0/assets](#/Assets/searchAssets) or [GET /api/v1.0/assets/by-tag/{assetTag}](#/Assets/getAssetByTag)

**Workflow Example**:
1. Search for the asset: [POST /api/v1.0/assets](#/Assets/searchAssets) to find the asset and extract `Items[0].AssetId`
2. Get custom field values: [GET /api/v1.0/custom-fields/values/for/asset/{assetId}](#/Custom Fields/getCustomFieldValuesForAsset)
3. The response includes all custom field values currently set on the asset

**Minimal Required Fields**: assetId path parameter

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_id` | `assetId` | `path` | `yes` | `str` | `-` | UUID of the asset to retrieve custom field values for. Obtain via [POST /api/v1.0/assets](#/Assets/searchAssets), extract `Items[].AssetId` from response. |

#### Returns

- Typed call return: `AssetCustomFieldValueListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AssetCustomFieldValueListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_custom_field_values_for_ticket`

Provenance: Golden OpenAPI contract

Operation ID: `getCustomFieldValuesForTicket`

- Sync: `client.custom_fields.get_custom_field_values_for_ticket(ticket_id=..., timeout=None)`
- Async: `await client.custom_fields.get_custom_field_values_for_ticket(ticket_id=..., timeout=None)`
- Raw payload: `client.custom_fields.get_custom_field_values_for_ticket.raw(ticket_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/custom-fields/values/for/ticket/{ticketId}`
- Source controller: `IncidentIQ API`

Get custom field values for ticket

Retrieves all custom field values set for a specific ticket.

**Prerequisites**:
- Obtain the `TicketId` from [POST /api/v1.0/tickets](#/Tickets/searchTickets)

**Workflow Example**:
1. Search for the ticket: [POST /api/v1.0/tickets](#/Tickets/searchTickets) to find the ticket and extract `Items[0].TicketId`
2. Get custom field values: [GET /api/v1.0/custom-fields/values/for/ticket/{ticketId}](#/Custom Fields/getCustomFieldValuesForTicket)
3. The response includes all custom field values currently set on the ticket

**Minimal Required Fields**: ticketId path parameter

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | UUID of the ticket to retrieve custom field values for |

#### Returns

- Typed call return: `TicketCustomFieldValueListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketCustomFieldValueListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_custom_field_values_for_user`

Provenance: Golden OpenAPI contract

Operation ID: `getCustomFieldValuesForUser`

- Sync: `client.custom_fields.get_custom_field_values_for_user(user_id=..., timeout=None)`
- Async: `await client.custom_fields.get_custom_field_values_for_user(user_id=..., timeout=None)`
- Raw payload: `client.custom_fields.get_custom_field_values_for_user.raw(user_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/custom-fields/values/for/user/{userId}`
- Source controller: `IncidentIQ API`

Get custom field values for user

Retrieves all custom field values set for a specific user.

**Prerequisites**:
- Obtain the `UserId` from [POST /api/v1.0/users](#/Users/searchUsers) or [POST /api/v1.0/search](#/Users/searchUsers)

**Workflow Example**:
1. Search for the user: [POST /api/v1.0/users](#/Users/searchUsers) to find the user and extract `Items[0].UserId`
2. Get custom field values: [GET /api/v1.0/custom-fields/values/for/user/{userId}](#/Custom Fields/getCustomFieldValuesForUser)
3. The response includes all custom field values currently set on the user

**Minimal Required Fields**: userId path parameter

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `userId` | `path` | `yes` | `str` | `-` | UUID of the user to retrieve custom field values for |

#### Returns

- Typed call return: `UserCustomFieldValueListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UserCustomFieldValueListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_custom_fields_for_asset`

Provenance: Golden OpenAPI contract

Operation ID: `getCustomFieldsForAsset`

- Sync: `client.custom_fields.get_custom_fields_for_asset(body=None, timeout=None)`
- Async: `await client.custom_fields.get_custom_fields_for_asset(body=None, timeout=None)`
- Raw payload: `client.custom_fields.get_custom_fields_for_asset.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/custom-fields/for/asset`
- Source controller: `IncidentIQ API`

Get custom fields for asset

Retrieves the list of custom fields applicable to an asset. This endpoint supports conditional custom fields through filter set matching.

**Request Body Behavior**:
- **Empty body `{}`**: Returns ALL custom fields defined for the Assets entity type, regardless of filter conditions.
- **With `EntityId`**: Returns only custom fields that either have no filter conditions OR whose filter conditions match the specified asset.
- **With `Entity` object**: Same as EntityId, but uses the provided asset properties for filter matching without a database lookup.
- **With `ForProductId`**: Overrides the product context from request headers.

**Filter Set Matching**:
Custom fields can have associated filter sets that control when they appear. For example, a "Warranty Expiration" field might only appear on assets with a specific AssetTypeId. When you provide an Entity or EntityId, the system evaluates these filter conditions and only returns matching fields.

**Prerequisites**:
- To filter by a specific asset, obtain the `AssetId` from [POST /api/v1.0/assets](#/Assets/searchAssets)

**Workflow Example**:
1. To get all asset custom fields: POST with empty body `{}`
2. To get custom fields for a specific asset: POST with `{"EntityId": "asset-uuid"}`
3. Use the returned `CustomFieldTypeId` values when setting custom field values via [POST /api/v1.0/custom-fields/values/for/assets](#/Custom%20Fields/upsertAssetCustomFieldValues)

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `GetCustomFieldsForAssetRequest` | `GetCustomFieldsForAssetRequest` | - |

#### Returns

- Typed call return: `CustomFieldListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CustomFieldListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_custom_fields_for_asset_inventory_action`

Provenance: Golden OpenAPI contract

Operation ID: `getCustomFieldsForAssetInventoryAction`

- Sync: `client.custom_fields.get_custom_fields_for_asset_inventory_action(body=None, timeout=None)`
- Async: `await client.custom_fields.get_custom_fields_for_asset_inventory_action(body=None, timeout=None)`
- Raw payload: `client.custom_fields.get_custom_fields_for_asset_inventory_action.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/custom-fields/for/asset-inventory-action`
- Source controller: `IncidentIQ API`

Get custom fields for asset inventory action

Retrieves the list of custom fields applicable to an asset inventory action. This endpoint supports conditional custom fields through filter set matching.

**Request Body Behavior**:
- **Empty body `{}`**: Returns ALL custom fields defined for the AssetInventoryActions entity type, regardless of filter conditions.
- **With `EntityId`**: Returns only custom fields that either have no filter conditions OR whose filter conditions match the specified asset inventory action.
- **With `Entity` object**: Same as EntityId, but uses the provided asset inventory action properties for filter matching without a database lookup.
- **With `ForProductId`**: Overrides the product context from request headers.

**Filter Set Matching**:
Custom fields can have associated filter sets that control when they appear. When you provide an Entity or EntityId, the system evaluates these filter conditions and only returns matching fields.

**Prerequisites**:
- To filter by a specific asset inventory action, obtain the `AssetInventoryActionId` from asset inventory action search endpoints

**Workflow Example**:
1. To get all asset inventory action custom fields: POST with empty body `{}`
2. To get custom fields for a specific asset inventory action: POST with `{"EntityId": "asset-inventory-action-uuid"}`
3. Use the returned `CustomFieldTypeId` values when setting custom field values via [POST /api/v1.0/custom-fields/values/for/asset-inventory-actions](#/Custom%20Fields/upsertAssetInventoryActionCustomFieldValues)

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `GetCustomFieldsForAssetInventoryActionRequest` | `GetCustomFieldsForAssetInventoryActionRequest` | - |

#### Returns

- Typed call return: `CustomFieldListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CustomFieldListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_custom_fields_for_event`

Provenance: Golden OpenAPI contract

Operation ID: `getCustomFieldsForEvent`

- Sync: `client.custom_fields.get_custom_fields_for_event(body=None, timeout=None)`
- Async: `await client.custom_fields.get_custom_fields_for_event(body=None, timeout=None)`
- Raw payload: `client.custom_fields.get_custom_fields_for_event.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/custom-fields/for/event`
- Source controller: `IncidentIQ API`

Get custom fields for event

Retrieves the list of custom fields applicable to an event. This endpoint supports conditional custom fields through filter set matching.

**Request Body Behavior**:
- **Empty body `{}`**: Returns ALL custom fields defined for the Events entity type, regardless of filter conditions.
- **With `EntityId`**: Returns only custom fields that either have no filter conditions OR whose filter conditions match the specified event.
- **With `Entity` object**: Same as EntityId, but uses the provided event properties for filter matching without a database lookup.

**Cross-Product Behavior**:
Events and organizations are effectively cross-product entities. This endpoint forces retrieval of event-specific product custom fields as well as product-agnostic event fields. The custom field manager is instantiated with the Event Reservations product context.

**Prerequisites**:
- To filter by a specific event, obtain the `EventId` from event search endpoints

**Workflow Example**:
1. To get all event custom fields: POST with empty body `{}`
2. To get custom fields for a specific event: POST with `{"EntityId": "event-uuid"}`
3. Use the returned `CustomFieldTypeId` values when setting custom field values via [POST /api/v1.0/custom-fields/values/for/events](#/Custom%20Fields/upsertEventCustomFieldValues)

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `GetCustomFieldsForEventRequest` | `GetCustomFieldsForEventRequest` | - |

#### Returns

- Typed call return: `CustomFieldListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CustomFieldListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_custom_fields_for_inventory_item`

Provenance: Golden OpenAPI contract

Operation ID: `getCustomFieldsForInventoryItem`

- Sync: `client.custom_fields.get_custom_fields_for_inventory_item(body=None, timeout=None)`
- Async: `await client.custom_fields.get_custom_fields_for_inventory_item(body=None, timeout=None)`
- Raw payload: `client.custom_fields.get_custom_fields_for_inventory_item.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/custom-fields/for/inventory-item`
- Source controller: `IncidentIQ API`

Get custom fields for inventory item

Retrieves the list of custom fields applicable to an inventory item. This endpoint supports conditional custom fields through filter set matching.

**Request Body Behavior**:
- **Empty body `{}`**: Returns ALL custom fields defined for the InventoryItems entity type, regardless of filter conditions.
- **With `EntityId`**: Returns only custom fields that either have no filter conditions OR whose filter conditions match the specified inventory item.
- **With `Entity` object**: Same as EntityId, but uses the provided inventory item properties for filter matching without a database lookup.
- **With `ForProductId`**: Overrides the product context from request headers.

**Special Product Context Behavior**:
If an EntityId is provided, the system loads the inventory item to determine its ProductId and uses that for the custom field manager context. This ensures inventory item custom fields are correctly scoped to the item's product.

**Prerequisites**:
- To filter by a specific inventory item, obtain the `InventoryItemId` from inventory item search endpoints

**Workflow Example**:
1. To get all inventory item custom fields: POST with empty body `{}`
2. To get custom fields for a specific inventory item: POST with `{"EntityId": "inventory-item-uuid"}`

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `GetCustomFieldsForInventoryItemRequest` | `GetCustomFieldsForInventoryItemRequest` | - |

#### Returns

- Typed call return: `CustomFieldListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CustomFieldListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_custom_fields_for_location`

Provenance: Golden OpenAPI contract

Operation ID: `getCustomFieldsForLocation`

- Sync: `client.custom_fields.get_custom_fields_for_location(body=None, timeout=None)`
- Async: `await client.custom_fields.get_custom_fields_for_location(body=None, timeout=None)`
- Raw payload: `client.custom_fields.get_custom_fields_for_location.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/custom-fields/for/location`
- Source controller: `IncidentIQ API`

Get custom fields for location

Retrieves the list of custom fields applicable to a location. This endpoint supports conditional custom fields through filter set matching.

**Request Body Behavior**:
- **Empty body `{}`**: Returns ALL custom fields defined for the Locations entity type, regardless of filter conditions.
- **With `EntityId`**: Returns only custom fields that either have no filter conditions OR whose filter conditions match the specified location.
- **With `Entity` object**: Same as EntityId, but uses the provided location properties for filter matching without a database lookup.
- **With `ForProductId`**: Overrides the product context from request headers.

**Filter Set Matching**:
Custom fields can have associated filter sets that control when they appear. For example, a "Principal Name" field might only appear on locations with a specific LocationTypeId. When you provide an Entity or EntityId, the system evaluates these filter conditions and only returns matching fields.

**Prerequisites**:
- To filter by a specific location, obtain the `LocationId` from location search endpoints

**Workflow Example**:
1. To get all location custom fields: POST with empty body `{}`
2. To get custom fields for a specific location: POST with `{"EntityId": "location-uuid"}`

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `GetCustomFieldsForLocationRequest` | `GetCustomFieldsForLocationRequest` | - |

#### Returns

- Typed call return: `CustomFieldListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CustomFieldListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_custom_fields_for_location_room`

Provenance: Golden OpenAPI contract

Operation ID: `getCustomFieldsForLocationRoom`

- Sync: `client.custom_fields.get_custom_fields_for_location_room(body=None, timeout=None)`
- Async: `await client.custom_fields.get_custom_fields_for_location_room(body=None, timeout=None)`
- Raw payload: `client.custom_fields.get_custom_fields_for_location_room.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/custom-fields/for/location-room`
- Source controller: `IncidentIQ API`

Get custom fields for location room

Retrieves the list of custom fields applicable to a location room. This endpoint supports conditional custom fields through filter set matching.

**Request Body Behavior**:
- **Empty body `{}`**: Returns ALL custom fields defined for the LocationRooms entity type, regardless of filter conditions.
- **With `EntityId`**: Returns only custom fields that either have no filter conditions OR whose filter conditions match the specified location room.
- **With `Entity` object**: Same as EntityId, but uses the provided location room properties for filter matching without a database lookup.
- **With `ForProductId`**: Overrides the product context from request headers.

**Filter Set Matching**:
Custom fields can have associated filter sets that control when they appear. When you provide an Entity or EntityId, the system evaluates these filter conditions and only returns matching fields.

**Prerequisites**:
- To filter by a specific location room, obtain the `LocationRoomId` from location room search endpoints

**Workflow Example**:
1. To get all location room custom fields: POST with empty body `{}`
2. To get custom fields for a specific location room: POST with `{"EntityId": "location-room-uuid"}`

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `GetCustomFieldsForLocationRoomRequest` | `GetCustomFieldsForLocationRoomRequest` | - |

#### Returns

- Typed call return: `CustomFieldListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CustomFieldListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_custom_fields_for_organization`

Provenance: Golden OpenAPI contract

Operation ID: `getCustomFieldsForOrganization`

- Sync: `client.custom_fields.get_custom_fields_for_organization(body=None, timeout=None)`
- Async: `await client.custom_fields.get_custom_fields_for_organization(body=None, timeout=None)`
- Raw payload: `client.custom_fields.get_custom_fields_for_organization.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/custom-fields/for/organization`
- Source controller: `IncidentIQ API`

Get custom fields for organization

Retrieves the list of custom fields applicable to an organization. This endpoint supports conditional custom fields through filter set matching.

**Request Body Behavior**:
- **Empty body `{}`**: Returns ALL custom fields defined for the Organizations entity type, regardless of filter conditions.
- **With `EntityId`**: Returns only custom fields that either have no filter conditions OR whose filter conditions match the specified organization.
- **With `Entity` object**: Same as EntityId, but uses the provided organization properties for filter matching without a database lookup.

**Cross-Product Behavior**:
Events and organizations are effectively cross-product entities. This endpoint forces retrieval of organization-specific product custom fields as well as product-agnostic organization fields. The custom field manager is instantiated with the Event Reservations product context.

**Prerequisites**:
- To filter by a specific organization, obtain the `OrganizationId` from organization search endpoints

**Workflow Example**:
1. To get all organization custom fields: POST with empty body `{}`
2. To get custom fields for a specific organization: POST with `{"EntityId": "organization-uuid"}`

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `GetCustomFieldsForOrganizationRequest` | `GetCustomFieldsForOrganizationRequest` | - |

#### Returns

- Typed call return: `CustomFieldListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CustomFieldListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_custom_fields_for_ticket`

Provenance: Golden OpenAPI contract

Operation ID: `getCustomFieldsForTicket`

- Sync: `client.custom_fields.get_custom_fields_for_ticket(body=None, timeout=None)`
- Async: `await client.custom_fields.get_custom_fields_for_ticket(body=None, timeout=None)`
- Raw payload: `client.custom_fields.get_custom_fields_for_ticket.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/custom-fields/for/ticket`
- Source controller: `IncidentIQ API`

Get custom fields for ticket

Retrieves the list of custom fields applicable to a ticket. This endpoint supports conditional custom fields through filter set matching.

**Request Body Behavior**:
- **Empty body `{}`**: Returns ALL custom fields defined for the Tickets entity type, regardless of filter conditions.
- **With `EntityId`**: Returns only custom fields that either have no filter conditions OR whose filter conditions match the specified ticket.
- **With `Entity` object**: Same as EntityId, but uses the provided ticket properties for filter matching without a database lookup.
- **With `ForProductId`**: Overrides the product context from request headers.

**Filter Set Matching**:
Custom fields can have associated filter sets that control when they appear. For example, a "Hardware Details" field might only appear on tickets with a specific IssueId. When you provide an Entity or EntityId, the system evaluates these filter conditions and only returns matching fields.

**Prerequisites**:
- To filter by a specific ticket, obtain the `TicketId` from [POST /api/v1.0/tickets](#/Tickets/searchTickets)

**Workflow Example**:
1. To get all ticket custom fields: POST with empty body `{}`
2. To get custom fields for a specific ticket: POST with `{"EntityId": "ticket-uuid"}`
3. Use the returned `CustomFieldTypeId` values when setting custom field values via [POST /api/v1.0/custom-fields/values/for/tickets](#/Custom%20Fields/upsertTicketCustomFieldValues)

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `GetCustomFieldsForTicketRequest` | `GetCustomFieldsForTicketRequest` | - |

#### Returns

- Typed call return: `CustomFieldListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CustomFieldListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_custom_fields_for_user`

Provenance: Golden OpenAPI contract

Operation ID: `getCustomFieldsForUser`

- Sync: `client.custom_fields.get_custom_fields_for_user(body=None, timeout=None)`
- Async: `await client.custom_fields.get_custom_fields_for_user(body=None, timeout=None)`
- Raw payload: `client.custom_fields.get_custom_fields_for_user.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/custom-fields/for/user`
- Source controller: `IncidentIQ API`

Get custom fields for user

Retrieves the list of custom fields applicable to a user. This endpoint supports conditional custom fields through filter set matching.

**Request Body Behavior**:
- **Empty body `{}`**: Returns ALL custom fields defined for the Users entity type, regardless of filter conditions.
- **With `EntityId`**: Returns only custom fields that either have no filter conditions OR whose filter conditions match the specified user.
- **With `Entity` object**: Same as EntityId, but uses the provided user properties for filter matching without a database lookup.
- **With `ForProductId`**: Overrides the product context from request headers.

**Filter Set Matching**:
Custom fields can have associated filter sets that control when they appear. For example, a "Badge Number" field might only appear on users with a specific RoleId (e.g., Staff). When you provide an Entity or EntityId, the system evaluates these filter conditions and only returns matching fields.

**Prerequisites**:
- To filter by a specific user, obtain the `UserId` from [POST /api/v1.0/users](#/Users/searchUsers)

**Workflow Example**:
1. To get all user custom fields: POST with empty body `{}`
2. To get custom fields for a specific user: POST with `{"EntityId": "user-uuid"}`
3. Use the returned `CustomFieldTypeId` values when setting custom field values via [POST /api/v1.0/custom-fields/values/for/users](#/Custom%20Fields/upsertUserCustomFieldValues)

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `GetCustomFieldsForUserRequest` | `GetCustomFieldsForUserRequest` | - |

#### Returns

- Typed call return: `CustomFieldListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CustomFieldListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_event_custom_field_values`

Provenance: Golden OpenAPI contract

Operation ID: `getEventCustomFieldValues`

- Sync: `client.custom_fields.get_event_custom_field_values(s=None, p=None, filter=None, timeout=None)`
- Async: `await client.custom_fields.get_event_custom_field_values(s=None, p=None, filter=None, timeout=None)`
- Raw payload: `client.custom_fields.get_event_custom_field_values.raw(s=None, p=None, filter=None, timeout=None)`
- HTTP route: `GET /api/v1.0/custom-fields/events/values`
- Source controller: `IncidentIQ API`

Get event custom field values

Retrieves a paginated list of event custom field values across all events. Use this endpoint to query custom field values with filtering and pagination.

**Key Behavior**:
- Returns custom field values from all events the authenticated user has access to
- Supports pagination via `$s` (page size) and `$p` (page index) query parameters
- Supports filtering via `$filter` query parameter (refer to custom filter documentation)
- Default sort order is by CustomFieldTypeId ascending

**Use Cases**:
- Bulk export of custom field values for reporting
- Finding all events with a specific custom field value
- Auditing custom field usage across events

**Workflow Example**:
1. Call [GET /api/v1.0/custom-fields/events/values](#/Custom%20Fields/getEventCustomFieldValues) with `$s` and `$p` query parameters for pagination
2. To filter by custom field type: Use `$filter` query parameter with CustomFieldTypeId

**Minimal Required Fields**: None (uses defaults)

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of records per page |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index to retrieve |
| `filter` | `$filter` | `query` | `no` | `str` | `-` | Filter expression for custom field values |

#### Returns

- Typed call return: `EventCustomFieldValueListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `EventCustomFieldValueListResponse`
- Pagination helper: `client.custom_fields.get_event_custom_field_values.iter_pages(start_page=1, page_size=100, max_pages=None, s=None, p=None, filter=None, timeout=None)`

---

### `get_ticket_custom_field_values`

Provenance: Golden OpenAPI contract

Operation ID: `getTicketCustomFieldValues`

- Sync: `client.custom_fields.get_ticket_custom_field_values(s=None, p=None, filter=None, timeout=None)`
- Async: `await client.custom_fields.get_ticket_custom_field_values(s=None, p=None, filter=None, timeout=None)`
- Raw payload: `client.custom_fields.get_ticket_custom_field_values.raw(s=None, p=None, filter=None, timeout=None)`
- HTTP route: `GET /api/v1.0/custom-fields/tickets/values`
- Source controller: `IncidentIQ API`

Get ticket custom field values

Retrieves a paginated list of ticket custom field values across all tickets. Use this endpoint to query custom field values with filtering and pagination.

**Key Behavior**:
- Returns custom field values from all tickets the authenticated user has access to
- Supports pagination via `$s` (page size) and `$p` (page index) query parameters
- Supports filtering via `$filter` query parameter (refer to custom filter documentation)
- Default sort order is by CustomFieldTypeId ascending

**Use Cases**:
- Bulk export of custom field values for reporting
- Finding all tickets with a specific custom field value
- Auditing custom field usage across tickets

**Workflow Example**:
1. Call [GET /api/v1.0/custom-fields/tickets/values](#/Custom%20Fields/getTicketCustomFieldValues) with `$s` and `$p` query parameters for pagination
2. To filter by custom field type: Use `$filter` query parameter with CustomFieldTypeId

**Minimal Required Fields**: None (uses defaults)

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of records per page |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index to retrieve |
| `filter` | `$filter` | `query` | `no` | `str` | `-` | Filter expression for custom field values |

#### Returns

- Typed call return: `TicketCustomFieldValueListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketCustomFieldValueListResponse`
- Pagination helper: `client.custom_fields.get_ticket_custom_field_values.iter_pages(start_page=1, page_size=100, max_pages=None, s=None, p=None, filter=None, timeout=None)`

---

### `get_user_custom_field_values`

Provenance: Golden OpenAPI contract

Operation ID: `getUserCustomFieldValues`

- Sync: `client.custom_fields.get_user_custom_field_values(s=None, p=None, filter=None, timeout=None)`
- Async: `await client.custom_fields.get_user_custom_field_values(s=None, p=None, filter=None, timeout=None)`
- Raw payload: `client.custom_fields.get_user_custom_field_values.raw(s=None, p=None, filter=None, timeout=None)`
- HTTP route: `GET /api/v1.0/custom-fields/users/values`
- Source controller: `IncidentIQ API`

Get user custom field values

Retrieves a paginated list of user custom field values across all users. Use this endpoint to query custom field values with filtering and pagination.

**Key Behavior**:
- Returns custom field values from all users the authenticated user has access to
- Supports pagination via `$s` (page size) and `$p` (page index) query parameters
- Supports filtering via `$filter` query parameter (refer to custom filter documentation)
- Default sort order is by CustomFieldTypeId ascending

**Use Cases**:
- Bulk export of custom field values for reporting
- Finding all users with a specific custom field value
- Auditing custom field usage across users

**Workflow Example**:
1. Call [GET /api/v1.0/custom-fields/users/values](#/Custom%20Fields/getUserCustomFieldValues) with `$s` and `$p` query parameters for pagination
2. To filter by custom field type: Use `$filter` query parameter with CustomFieldTypeId

**Minimal Required Fields**: None (uses defaults)

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of records per page |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index to retrieve |
| `filter` | `$filter` | `query` | `no` | `str` | `-` | Filter expression for custom field values |

#### Returns

- Typed call return: `UserCustomFieldValueListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UserCustomFieldValueListResponse`
- Pagination helper: `client.custom_fields.get_user_custom_field_values.iter_pages(start_page=1, page_size=100, max_pages=None, s=None, p=None, filter=None, timeout=None)`

---

### `list_custom_field_types`

Provenance: Golden OpenAPI contract

Operation ID: `listCustomFieldTypes`

- Sync: `client.custom_fields.list_custom_field_types(s=None, p=None, filter=None, timeout=None)`
- Async: `await client.custom_fields.list_custom_field_types(s=None, p=None, filter=None, timeout=None)`
- Raw payload: `client.custom_fields.list_custom_field_types.raw(s=None, p=None, filter=None, timeout=None)`
- HTTP route: `GET /api/v1.0/custom-fields/types`
- Source controller: `IncidentIQ API`

List custom field types

Retrieves a list of custom field type definitions from the system. Custom field types define the metadata structure for extending tickets, assets, users, and other entities with organization-specific fields.

**Query Parameters**
- `$s` - Page size (records per page)
- `$p` - Zero-based page index
- `$filter` - Filter expression for field names

**Workflow Example**
1. Call this endpoint: [GET /api/v1.0/custom-fields/types](#/Custom Fields/listCustomFieldTypes) to list all custom field types.
2. Extract `Items[].CustomFieldTypeId` for use with field-specific operations.
3. For complex filtering, use [POST /api/v1.0/custom-fields/types](#/Custom Fields/searchCustomFieldTypes) instead.

**Related Endpoints:**
- [POST /api/v1.0/custom-fields/types/new](#/Custom Fields/createCustomFieldType) - Create a new custom field type
- [GET /api/v1.0/custom-fields/types/{CustomFieldTypeId}](#/Custom Fields/getCustomFieldTypeById) - Get field type details

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of records per page |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index to retrieve |
| `filter` | `$filter` | `query` | `no` | `str` | `-` | Filter expression for custom field names (e.g., (Name%20contains%20Insurance)) |

#### Returns

- Typed call return: `CustomFieldTypeListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CustomFieldTypeListResponse`
- Pagination helper: `client.custom_fields.list_custom_field_types.iter_pages(start_page=1, page_size=100, max_pages=None, s=None, p=None, filter=None, timeout=None)`

---

### `lookup_site_by_searchable_value`

Provenance: Golden OpenAPI contract

Operation ID: `lookupSiteBySearchableValue`

- Sync: `client.custom_fields.lookup_site_by_searchable_value(body=..., timeout=None)`
- Async: `await client.custom_fields.lookup_site_by_searchable_value(body=..., timeout=None)`
- Raw payload: `client.custom_fields.lookup_site_by_searchable_value.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/custom-fields/complex/lookup-site-by-searchable-value`
- Source controller: `IncidentIQ API`

Lookup site by custom field searchable value

Performs a cross-site lookup to find which site owns a record based on a complex custom field searchable value. This specialized endpoint is used by integrations (like Google Devices) to locate records across multiple sites without requiring prior knowledge of the site ID.

**Key Use Case**:
- Google Devices app receives a position update for a DeviceId
- The app doesn't know which site the device belongs to
- This endpoint looks up the complex custom field value and returns the owning SiteId
- The app can then correctly route the update to the proper site

**Behavioral Notes**:
- Does **NOT** filter by SiteId (searches across all sites)
- Allows anonymous/app authorization for integration scenarios
- Searches based on custom field table name, property name, and value
- Returns the SiteId where the matching custom field value was found

**Prerequisites**:
1. **TableName** - The database table name for the custom field (e.g., `AssetCustomFields`)
2. **PropertyName** - The property/column being searched (e.g., `DeviceId`)
3. **Value** - The searchable value to look up
4. **CustomFieldTypeId** (optional) - Narrows the search to a specific field type
5. **CustomFieldComplexEditorNamespace** (optional) - For complex editor types

**Minimal Required Fields**: TableName, PropertyName, Value

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `ComplexCustomFieldSearchValueLookupRequest` | `ComplexCustomFieldSearchValueLookupRequest` | - |

#### Returns

- Typed call return: `SiteLookupBySearchableValueResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `SiteLookupBySearchableValueResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `reorder_custom_field_types`

Provenance: Golden OpenAPI contract

Operation ID: `reorderCustomFieldTypes`

- Sync: `client.custom_fields.reorder_custom_field_types(body=..., timeout=None)`
- Async: `await client.custom_fields.reorder_custom_field_types(body=..., timeout=None)`
- Raw payload: `client.custom_fields.reorder_custom_field_types.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/custom-fields/types/re-order`
- Source controller: `IncidentIQ API`

Reorder custom field types

Updates the display order for multiple custom field types. The order of IDs in the request array determines the new DisplayOrder values, allowing fine-grained control over how custom field types appear in the UI.

**Prerequisites**:
1. **CustomFieldTypeIds** - Obtain type UUIDs from [GET /api/v1.0/custom-fields/types](#/Custom%20Fields/listCustomFieldTypes) or [POST /api/v1.0/custom-fields/types](#/Custom%20Fields/searchCustomFieldTypes)

**Workflow Example**:
1. List custom field types to get current order
2. Arrange CustomFieldTypeId values in desired display order
3. Submit the reordered array
4. Custom field types will be displayed in the specified order

**Minimal Required Fields**: Array of CustomFieldTypeId values in desired order (at least one ID required)

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `CustomFieldTypeReorderRequest` | `CustomFieldTypeReorderRequest` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `reorder_custom_fields`

Provenance: Golden OpenAPI contract

Operation ID: `reorderCustomFields`

- Sync: `client.custom_fields.reorder_custom_fields(body=..., timeout=None)`
- Async: `await client.custom_fields.reorder_custom_fields(body=..., timeout=None)`
- Raw payload: `client.custom_fields.reorder_custom_fields.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/custom-fields/re-order`
- Source controller: `IncidentIQ API`

Reorder custom fields

Updates the display order for multiple custom fields. The order of IDs in the request array determines the new DisplayOrder values, allowing fine-grained control over how custom fields appear in the UI for specific entity types.

**Prerequisites**:
1. **CustomFieldIds** - Obtain field UUIDs from [POST /api/v1.0/custom-fields](#/Custom%20Fields/searchCustomFields) or entity-specific endpoints like [POST /api/v1.0/custom-fields/for/asset](#/Custom%20Fields/getCustomFieldsForAsset)

**Workflow Example**:
1. Retrieve custom fields for a specific entity type to get current order
2. Arrange CustomFieldId values in desired display order
3. Submit the reordered array
4. Custom fields will be displayed in the specified order

**Minimal Required Fields**: Array of CustomFieldId values in desired order (at least one ID required)

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `CustomFieldReorderRequest` | `CustomFieldReorderRequest` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `search_custom_field_types`

Provenance: Golden OpenAPI contract

Operation ID: `searchCustomFieldTypes`

- Sync: `client.custom_fields.search_custom_field_types(s=None, p=None, body=None, timeout=None)`
- Async: `await client.custom_fields.search_custom_field_types(s=None, p=None, body=None, timeout=None)`
- Raw payload: `client.custom_fields.search_custom_field_types.raw(s=None, p=None, body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/custom-fields/types`
- Source controller: `IncidentIQ API`

Search custom field types

Retrieves custom field types with optional request body filtering. This endpoint provides more flexibility than the GET version by supporting structured request body filters.

**Prerequisites**: None. Provide filter criteria in the request body.

**Workflow Example**:
1. To get all custom field types: POST with empty body or `{}`
2. To filter by scope: POST with `{"SiteScope": "Aggregate", "HideHidden": true}`
3. Use the returned `CustomFieldTypeId` values for subsequent operations

**Minimal Required Fields**: None (empty request returns all accessible custom field types)

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of records per page |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index to retrieve |
| `body` | `body` | `body` | `no` | `GetCustomFieldTypesRequest` | `GetCustomFieldTypesRequest` | - |

#### Returns

- Typed call return: `CustomFieldTypeListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CustomFieldTypeListResponse`
- Pagination helper: `client.custom_fields.search_custom_field_types.iter_pages(start_page=1, page_size=100, max_pages=None, s=None, p=None, body=None, timeout=None)`

---

### `search_custom_fields`

Provenance: Golden OpenAPI contract

Operation ID: `searchCustomFields`

- Sync: `client.custom_fields.search_custom_fields(s=None, p=None, body=None, timeout=None)`
- Async: `await client.custom_fields.search_custom_fields(s=None, p=None, body=None, timeout=None)`
- Raw payload: `client.custom_fields.search_custom_fields.raw(s=None, p=None, body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/custom-fields`
- Source controller: `IncidentIQ API`

Search custom fields

Retrieves a filtered list of custom field definitions. This endpoint allows searching across all custom field configurations using facet-based filters.

**Key Behavior**:
- Returns custom field definitions (not values) that match the provided filters
- Results are filtered to the current product context (from ProductId header) unless the field has no product restriction
- Supports filtering by scope, site, origin, custom field type, and entity type

**Difference from Entity-Specific Endpoints**:
- Use this endpoint when you need to search across ALL custom fields regardless of entity type
- Use [POST /api/v1.0/custom-fields/for/asset](#/Custom%20Fields/getCustomFieldsForAsset), [POST /api/v1.0/custom-fields/for/ticket](#/Custom%20Fields/getCustomFieldsForTicket), or [POST /api/v1.0/custom-fields/for/user](#/Custom%20Fields/getCustomFieldsForUser) when you need fields for a specific entity with filter set matching

**Prerequisites**: None. Provide filter criteria in the request body.

**Workflow Example**:
1. To get all custom fields: POST with empty filters `{"Filters": []}`
2. To get custom fields for a specific scope: POST with `{"Filters": [{"Facet": "Scope", "Value": "Asset"}]}`
3. Use the returned `CustomFieldId` and `CustomFieldTypeId` values for subsequent operations

**Minimal Required Fields**: None (empty request returns all accessible custom fields)

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of records to return per page |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index |
| `body` | `body` | `body` | `no` | `GetCustomFieldsRequest` | `GetCustomFieldsRequest` | - |

#### Returns

- Typed call return: `CustomFieldListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CustomFieldListResponse`
- Pagination helper: `client.custom_fields.search_custom_fields.iter_pages(start_page=1, page_size=100, max_pages=None, s=None, p=None, body=None, timeout=None)`

---

### `update_custom_field`

Provenance: Golden OpenAPI contract

Operation ID: `updateCustomField`

- Sync: `client.custom_fields.update_custom_field(custom_field_id=..., body=..., timeout=None)`
- Async: `await client.custom_fields.update_custom_field(custom_field_id=..., body=..., timeout=None)`
- Raw payload: `client.custom_fields.update_custom_field.raw(custom_field_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/custom-fields/{customFieldId}`
- Source controller: `IncidentIQ API`

Update custom field

Updates an existing custom field definition.

**Prerequisites**:
1. **CustomFieldId** - Obtain the field's UUID from [POST /api/v1.0/custom-fields](#/Custom%20Fields/searchCustomFields)
2. **Current field state** - Use [GET /api/v1.0/custom-fields/{customFieldId}](#/Custom%20Fields/getCustomFieldById) to get current values

**Workflow Example**:
1. Search for the custom field: [POST /api/v1.0/custom-fields](#/Custom Fields/searchCustomFields) → find target field and extract `CustomFieldId`
2. Get current definition: [GET /api/v1.0/custom-fields/{customFieldId}](#/Custom Fields/getCustomFieldById)
3. Modify desired properties and submit via this endpoint

**Minimal Required Fields**: customFieldId path parameter, request body with CustomFieldId

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `custom_field_id` | `customFieldId` | `path` | `yes` | `str` | `-` | UUID of the custom field to update |
| `body` | `body` | `body` | `yes` | `CustomFieldUpdateRequest` | `CustomFieldUpdateRequest` | - |

#### Returns

- Typed call return: `CustomFieldUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CustomFieldUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_custom_field_product`

Provenance: Golden OpenAPI contract

Operation ID: `updateCustomFieldProduct`

- Sync: `client.custom_fields.update_custom_field_product(custom_field_id=..., body=..., timeout=None)`
- Async: `await client.custom_fields.update_custom_field_product(custom_field_id=..., body=..., timeout=None)`
- Raw payload: `client.custom_fields.update_custom_field_product.raw(custom_field_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/custom-fields/{customFieldId}/product`
- Source controller: `IncidentIQ API`

Update custom field product association

Updates the product association for a specific custom field. This operation allows you to change which product (Technology, Facilities, etc.) a custom field is associated with.

**Key Behavior**:
- Updates the `ProductId` for the specified custom field
- Can associate or disassociate a field from a product
- Uses `FilterValueSaveRequest` which contains entity IDs and filter values

**Prerequisites**:
1. **customFieldId** (path parameter) - Obtain from [POST /api/v1.0/custom-fields](#/Custom%20Fields/searchCustomFields)
2. **FilterId** (in request body) - The filter or entity reference being updated
3. **Values** - Array of entity filter values specifying the product association

**Workflow Example** (Changing field product from Technology to Facilities):
1. Get the custom field ID from custom fields list
2. Get the target product ID (Facilities product UUID)
3. Call this endpoint with the field ID and product filter values

**Minimal Required Fields**: FilterId (in request body), Values array with Id properties

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `custom_field_id` | `customFieldId` | `path` | `yes` | `str` | `-` | UUID of the custom field to update |
| `body` | `body` | `body` | `yes` | `FilterValueSaveRequest` | `FilterValueSaveRequest` | - |

#### Returns

- Typed call return: `CustomFieldUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CustomFieldUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_custom_field_type`

Provenance: Golden OpenAPI contract

Operation ID: `updateCustomFieldType`

- Sync: `client.custom_fields.update_custom_field_type(custom_field_type_id=..., body=..., timeout=None)`
- Async: `await client.custom_fields.update_custom_field_type(custom_field_type_id=..., body=..., timeout=None)`
- Raw payload: `client.custom_fields.update_custom_field_type.raw(custom_field_type_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/custom-fields/types/{customFieldTypeId}`
- Source controller: `IncidentIQ API`

Update custom field type

Updates an existing custom field type definition.

**Prerequisites**:
1. **CustomFieldTypeId** - Obtain the type's UUID from [GET /api/v1.0/custom-fields/types](#/Custom%20Fields/listCustomFieldTypes) or [POST /api/v1.0/custom-fields/types](#/Custom%20Fields/searchCustomFieldTypes)
2. **Current type state** - Use [GET /api/v1.0/custom-fields/types/{customFieldTypeId}](#/Custom%20Fields/getCustomFieldTypeById) to get current values

**Workflow Example**:
1. List custom field types: [GET /api/v1.0/custom-fields/types](#/Custom Fields/listCustomFieldTypes) → find target and extract `CustomFieldTypeId`
2. Get current definition: [GET /api/v1.0/custom-fields/types/{customFieldTypeId}](#/Custom Fields/getCustomFieldTypeById)
3. Modify desired properties and submit via this endpoint

**Minimal Required Fields**: customFieldTypeId path parameter, request body with CustomFieldTypeId

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `custom_field_type_id` | `customFieldTypeId` | `path` | `yes` | `str` | `-` | UUID of the custom field type to update |
| `body` | `body` | `body` | `yes` | `CustomFieldTypeUpdateRequest` | `CustomFieldTypeUpdateRequest` | - |

#### Returns

- Typed call return: `CustomFieldTypeUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CustomFieldTypeUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `upsert_asset_custom_field_values`

Provenance: Golden OpenAPI contract

Operation ID: `upsertAssetCustomFieldValues`

- Sync: `client.custom_fields.upsert_asset_custom_field_values(body=..., timeout=None)`
- Async: `await client.custom_fields.upsert_asset_custom_field_values(body=..., timeout=None)`
- Raw payload: `client.custom_fields.upsert_asset_custom_field_values.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/custom-fields/values/for/assets`
- Source controller: `IncidentIQ API`

Upsert asset custom field values

Creates or updates custom field values for one or more assets. This endpoint performs an upsert operation - if a custom field value already exists for the specified asset and field type, it will be updated; otherwise, a new value will be created.

**Key Behavior**:
- This endpoint does **NOT** delete existing custom field values not included in the request (`deleteMissingValues: false` internally)
- You can update a single custom field without affecting other custom fields on the asset
- Multiple assets and/or multiple custom fields can be updated in a single request
- Read-only custom fields can be updated via this endpoint when using app authorization

**Prerequisites**:
1. **AssetId** - Obtain the asset's UUID via [POST /api/v1.0/assets](#/Assets/searchAssets) or [GET /api/v1.0/assets/by-tag/{assetTag}](#/Assets/getAssetByTag)
2. **CustomFieldTypeId** - Call [POST /api/v1.0/custom-fields/for/asset](#/Custom%20Fields/getCustomFieldsForAsset) to get available custom field definitions and extract `Items[].CustomFieldTypeId`

**Workflow Example** (Updating Warranty Expiration Date):
1. Search for the asset: [POST /api/v1.0/assets](#/Assets/searchAssets) with model/location filters → extract `Items[0].AssetId`
2. Get asset custom fields: [POST /api/v1.0/custom-fields/for/asset](#/Custom Fields/getCustomFieldsForAsset) with `{"EntityId": "asset-uuid"}` → find the warranty field and note its `CustomFieldTypeId`
3. Update the custom field value: [POST /api/v1.0/custom-fields/values/for/assets](#/Custom Fields/upsertAssetCustomFieldValues) with the asset ID, field type ID, and new value

**Minimal Required Fields**: AssetId, CustomFieldTypeId, Value (or ComplexValue for complex editors)

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `UpsertAssetCustomFieldValuesRequest` | `UpsertAssetCustomFieldValuesRequest` | - |

#### Returns

- Typed call return: `UpsertCustomFieldValuesResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UpsertCustomFieldValuesResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `upsert_asset_inventory_action_custom_field_values`

Provenance: Golden OpenAPI contract

Operation ID: `upsertAssetInventoryActionCustomFieldValues`

- Sync: `client.custom_fields.upsert_asset_inventory_action_custom_field_values(body=..., timeout=None)`
- Async: `await client.custom_fields.upsert_asset_inventory_action_custom_field_values(body=..., timeout=None)`
- Raw payload: `client.custom_fields.upsert_asset_inventory_action_custom_field_values.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/custom-fields/values/for/asset-inventory-actions`
- Source controller: `IncidentIQ API`

Upsert asset inventory action custom field values

Creates or updates custom field values for one or more asset inventory actions. This endpoint performs an upsert operation - if a custom field value already exists for the specified asset inventory action and field type, it will be updated; otherwise, a new value will be created.

**Key Behavior**:
- This endpoint does **NOT** delete existing custom field values not included in the request (`deleteMissingValues: false` internally)
- You can update a single custom field without affecting other custom fields on the asset inventory action
- Multiple asset inventory actions and/or multiple custom fields can be updated in a single request
- Read-only custom fields can be updated via this endpoint when using app authorization

**Prerequisites**:
1. **AssetInventoryActionId** - Obtain the asset inventory action's UUID from asset inventory action search endpoints
2. **CustomFieldTypeId** - Call [POST /api/v1.0/custom-fields/for/asset-inventory-action](#/Custom%20Fields/getCustomFieldsForAssetInventoryAction) to get available custom field definitions and extract `Items[].CustomFieldTypeId`

**Workflow Example**:
1. Search for the asset inventory action and extract `AssetInventoryActionId`
2. Get custom fields: [POST /api/v1.0/custom-fields/for/asset-inventory-action](#/Custom Fields/getCustomFieldsForAssetInventoryAction) with `{"EntityId": "asset-inventory-action-uuid"}` to find the field and note its `CustomFieldTypeId`
3. Update the custom field value: [POST /api/v1.0/custom-fields/values/for/asset-inventory-actions](#/Custom Fields/upsertAssetInventoryActionCustomFieldValues) with the action ID, field type ID, and new value

**Minimal Required Fields**: AssetInventoryActionId, CustomFieldTypeId, Value (or ComplexValue for complex editors)

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `UpsertAssetInventoryActionCustomFieldValuesRequest` | `UpsertAssetInventoryActionCustomFieldValuesRequest` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `upsert_event_custom_field_values`

Provenance: Golden OpenAPI contract

Operation ID: `upsertEventCustomFieldValues`

- Sync: `client.custom_fields.upsert_event_custom_field_values(body=..., timeout=None)`
- Async: `await client.custom_fields.upsert_event_custom_field_values(body=..., timeout=None)`
- Raw payload: `client.custom_fields.upsert_event_custom_field_values.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/custom-fields/values/for/events`
- Source controller: `IncidentIQ API`

Upsert event custom field values

Creates or updates custom field values for one or more events. This endpoint performs an upsert operation - if a custom field value already exists for the specified event and field type, it will be updated; otherwise, a new value will be created.

**Key Behavior**:
- This endpoint does **NOT** delete existing custom field values not included in the request (`deleteMissingValues: false` internally)
- You can update a single custom field without affecting other custom fields on the event
- Multiple events and/or multiple custom fields can be updated in a single request
- Read-only custom fields can be updated via this endpoint when using app authorization

**Prerequisites**:
1. **EventId** - Obtain the event's UUID from event search endpoints
2. **CustomFieldTypeId** - Call [POST /api/v1.0/custom-fields/for/event](#/Custom%20Fields/getCustomFieldsForEvent) to get available custom field definitions and extract `Items[].CustomFieldTypeId`

**Workflow Example** (Updating Event Resource Details):
1. Search for the event to get the EventId
2. Get event custom fields: [POST /api/v1.0/custom-fields/for/event](#/Custom Fields/getCustomFieldsForEvent) with `{"EntityId": "event-uuid"}` to find the resource details field and note its `CustomFieldTypeId`
3. Update the custom field value: [POST /api/v1.0/custom-fields/values/for/events](#/Custom Fields/upsertEventCustomFieldValues) with the event ID, field type ID, and new value

**Minimal Required Fields**: EventId, CustomFieldTypeId, Value (or ComplexValue for complex editors)

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `UpsertEventCustomFieldValuesRequest` | `UpsertEventCustomFieldValuesRequest` | - |

#### Returns

- Typed call return: `UpsertCustomFieldValuesResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UpsertCustomFieldValuesResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `upsert_ticket_custom_field_values`

Provenance: Golden OpenAPI contract

Operation ID: `upsertTicketCustomFieldValues`

- Sync: `client.custom_fields.upsert_ticket_custom_field_values(body=..., timeout=None)`
- Async: `await client.custom_fields.upsert_ticket_custom_field_values(body=..., timeout=None)`
- Raw payload: `client.custom_fields.upsert_ticket_custom_field_values.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/custom-fields/values/for/tickets`
- Source controller: `IncidentIQ API`

Upsert ticket custom field values

Creates or updates custom field values for one or more tickets. This endpoint performs an upsert operation - if a custom field value already exists for the specified ticket and field type, it will be updated; otherwise, a new value will be created.

**Key Behavior**:
- This endpoint does **NOT** delete existing custom field values not included in the request (`deleteMissingValues: false` internally)
- You can update a single custom field without affecting other custom fields on the ticket
- Multiple tickets and/or multiple custom fields can be updated in a single request
- Read-only custom fields can be updated via this endpoint when using app authorization

**Alternative Endpoint**: For more control over whether missing values are deleted, use [POST /api/v1.0/tickets/{ticketId}/custom-fields/{deleteMissingValues}](#/CustomFields/upsertTicketCustomFieldValues)

**Prerequisites**:
1. **TicketId** - Obtain the ticket's UUID via [POST /api/v1.0/tickets](#/Tickets/searchTickets)
2. **CustomFieldTypeId** - Call [POST /api/v1.0/custom-fields/for/ticket](#/Custom%20Fields/getCustomFieldsForTicket) to get available custom field definitions and extract `Items[].CustomFieldTypeId`

**Workflow Example** (Setting Priority Flag):
1. Search for the ticket: [POST /api/v1.0/tickets](#/Tickets/searchTickets) with status/assignee filters → extract `Items[0].TicketId`
2. Get ticket custom fields: [POST /api/v1.0/custom-fields/for/ticket](#/Custom Fields/getCustomFieldsForTicket) with `{"EntityId": "ticket-uuid"}` → find the priority flag field and note its `CustomFieldTypeId`
3. Update the custom field value: [POST /api/v1.0/custom-fields/values/for/tickets](#/Custom Fields/upsertTicketCustomFieldValues) with the ticket ID, field type ID, and new value

**Minimal Required Fields**: TicketId, CustomFieldTypeId, Value (or ComplexValue for complex editors)

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `UpsertTicketCustomFieldValuesRequest` | `UpsertTicketCustomFieldValuesRequest` | - |

#### Returns

- Typed call return: `UpsertCustomFieldValuesResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UpsertCustomFieldValuesResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `upsert_user_custom_field_values`

Provenance: Golden OpenAPI contract

Operation ID: `upsertUserCustomFieldValues`

- Sync: `client.custom_fields.upsert_user_custom_field_values(body=..., timeout=None)`
- Async: `await client.custom_fields.upsert_user_custom_field_values(body=..., timeout=None)`
- Raw payload: `client.custom_fields.upsert_user_custom_field_values.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/custom-fields/values/for/users`
- Source controller: `IncidentIQ API`

Upsert user custom field values

Creates or updates custom field values for one or more users. This endpoint performs an upsert operation - if a custom field value already exists for the specified user and field type, it will be updated; otherwise, a new value will be created.

**Key Behavior**:
- This endpoint does **NOT** delete existing custom field values not included in the request (`deleteMissingValues: false` internally)
- You can update a single custom field without affecting other custom fields on the user
- Multiple users and/or multiple custom fields can be updated in a single request
- Read-only custom fields can be updated via this endpoint when using app authorization

**Prerequisites**:
1. **UserId** - Obtain the user's UUID via [POST /api/v1.0/users](#/Users/searchUsers) or [POST /api/v1.0/search](#/Users/searchUsers)
2. **CustomFieldTypeId** - Call [POST /api/v1.0/custom-fields/for/user](#/Custom%20Fields/getCustomFieldsForUser) to get available custom field definitions and extract `Items[].CustomFieldTypeId`

**Workflow Example** (Updating iPad Protection Plan):
1. Search for the user: [POST /api/v1.0/users](#/Users/searchUsers) with role/keyword filters → extract `Items[0].UserId`
2. Get user custom fields: [POST /api/v1.0/custom-fields/for/user](#/Custom Fields/getCustomFieldsForUser) with `{}` → find the iPad Protection Plan field and note its `CustomFieldTypeId`
3. Update the custom field value: [POST /api/v1.0/custom-fields/values/for/users](#/Custom Fields/upsertUserCustomFieldValues) with the user ID, field type ID, and new value

**Minimal Required Fields**: UserId, CustomFieldTypeId, Value (or ComplexValue for complex editors)

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `UpsertUserCustomFieldValuesRequest` | `UpsertUserCustomFieldValuesRequest` | - |

#### Returns

- Typed call return: `UpsertCustomFieldValuesResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UpsertCustomFieldValuesResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
