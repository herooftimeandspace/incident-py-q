# `inventory` Golden Namespace

Sync client access: `client.inventory`

Async client access: `client.inventory` with `await` on method calls.

These methods are Golden because they come from the bundled Incident IQ OpenAPI contract.

## Methods

### `create_inventories_batch`

Provenance: Golden OpenAPI contract

Operation ID: `createInventoriesBatch`

- Sync: `client.inventory.create_inventories_batch(body=..., timeout=None)`
- Async: `await client.inventory.create_inventories_batch(body=..., timeout=None)`
- Raw payload: `client.inventory.create_inventories_batch.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/inventory/inventories/ids`
- Source controller: `IncidentIQ API`

Create multiple inventory stock records

Creates multiple inventory stock records in a single batch request.

**Note**: This API is marked as deprecated (v1.0).

**Use Case**: Useful for initializing stock at multiple locations or importing inventory data in bulk.

**Prerequisites**:
- **InventoryItemId**: Use [POST /api/v1.0/inventory/items/query](#/Inventory/queryInventoryItems) to find catalog items
- **LocationId**: Use [GET /api/v2.0/locations](#/Locations/getAllSiteLocationsV2) to find target locations

**Workflow**:
1. Query catalog items to get `InventoryItemId` values
2. Query locations to get `LocationId` values
3. Prepare array of stock records with quantity and cost information
4. Submit the batch create request

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | Array of inventory stock records to create. |

#### Returns

- Typed call return: `InventoryBatchCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InventoryBatchCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_inventory`

Provenance: Golden OpenAPI contract

Operation ID: `createInventory`

- Sync: `client.inventory.create_inventory(body=..., timeout=None)`
- Async: `await client.inventory.create_inventory(body=..., timeout=None)`
- Raw payload: `client.inventory.create_inventory.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/inventory/inventories/new`
- Source controller: `IncidentIQ API`

Create inventory stock record

Creates a new inventory stock record for a catalog item at a specific location.

**Note**: This API is marked as deprecated (v1.0).

**Prerequisites**:
- **InventoryItemId**: Use [POST /api/v1.0/inventory-items/query](#/Inventory/queryInventoryItems) to find catalog items
- **LocationId**: Use [GET /api/v2.0/locations](#/Locations/getAllSiteLocationsV2) to find locations
- **InventoryStateTypeId**: Use reference data endpoints to get valid state type IDs

**Workflow**:
1. Search for the catalog item to get `InventoryItemId`
2. Search for the target location to get `LocationId`
3. Submit the create request with quantity, cost, and tracking settings

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `UpdateInventoryRequest` | `UpdateInventoryRequest` | Inventory stock record to create. |

#### Returns

- Typed call return: `InventoryCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InventoryCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_inventory_action`

Provenance: Golden OpenAPI contract

Operation ID: `createInventoryAction`

- Sync: `client.inventory.create_inventory_action(body=..., timeout=None)`
- Async: `await client.inventory.create_inventory_action(body=..., timeout=None)`
- Raw payload: `client.inventory.create_inventory_action.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/inventory/actions`
- Source controller: `IncidentIQ API`

Create inventory action

Creates a new inventory action record.

**Note**: This API is marked as deprecated (v1.0).

**Prerequisites**:
- **InventoryId**: Use [POST /api/v1.0/inventory/inventories](#/Inventory/queryInventories) to find stock entries
- **InventoryActionTypeId**: Use reference data endpoints to get valid action type IDs

**Workflow**:
1. Search for the inventory stock entry to get `InventoryId`
2. Determine the action type (consumption, addition, transfer, etc.)
3. Submit the action with quantity delta and optional entity reference

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `UpdateInventoryActionRequest` | `UpdateInventoryActionRequest` | Inventory action to create. |

#### Returns

- Typed call return: `InventoryActionItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InventoryActionItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_inventory_actions_batch`

Provenance: Golden OpenAPI contract

Operation ID: `createInventoryActionsBatch`

- Sync: `client.inventory.create_inventory_actions_batch(body=..., timeout=None)`
- Async: `await client.inventory.create_inventory_actions_batch(body=..., timeout=None)`
- Raw payload: `client.inventory.create_inventory_actions_batch.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/inventory/actions/ids/new`
- Source controller: `IncidentIQ API`

Create multiple inventory actions

Creates multiple inventory action records in a single batch request.

**Note**: This API is marked as deprecated (v1.0).

**Use Case**: Useful for recording multiple inventory transactions at once, such as when a repair uses several parts.

**Prerequisites**:
- **InventoryId**: Use [POST /api/v1.0/inventory/inventories](#/Inventory/queryInventories) to find stock entries
- **InventoryActionTypeId**: Use reference data endpoints to get valid action type IDs (consumption, addition, transfer)

**Workflow**:
1. Search for the inventory stock entries to get `InventoryId` values
2. Prepare an array of action objects with quantity deltas
3. Submit the batch and verify all actions were created

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | Array of inventory actions to create. |

#### Returns

- Typed call return: `InventoryActionCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InventoryActionCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_inventory_item`

Provenance: Golden OpenAPI contract

Operation ID: `createInventoryItem`

- Sync: `client.inventory.create_inventory_item(body=..., timeout=None)`
- Async: `await client.inventory.create_inventory_item(body=..., timeout=None)`
- Raw payload: `client.inventory.create_inventory_item.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/inventory/items`
- Source controller: `IncidentIQ API`

Create inventory catalog item

Creates a new inventory catalog item (part or consumable).

**Note**: This API is marked as deprecated (v1.0).

**Prerequisites**:
- **CategoryId**: Use category endpoints to find available categories
- **InventoryTypeId**: Use reference data to get valid inventory type IDs

**Workflow**:
1. Search for or create the appropriate category
2. Create the catalog item with name, item number, and cost information
3. After creation, use stock endpoints to add inventory at specific locations

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `UpdateInventoryItemRequest` | `UpdateInventoryItemRequest` | Inventory item to create. |

#### Returns

- Typed call return: `InventoryItemCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InventoryItemCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_inventory_items_batch`

Provenance: Golden OpenAPI contract

Operation ID: `createInventoryItemsBatch`

- Sync: `client.inventory.create_inventory_items_batch(body=..., timeout=None)`
- Async: `await client.inventory.create_inventory_items_batch(body=..., timeout=None)`
- Raw payload: `client.inventory.create_inventory_items_batch.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/inventory/items/ids/new`
- Source controller: `IncidentIQ API`

Create multiple inventory catalog items

Creates multiple inventory catalog items in a single batch request.

**Note**: This API is marked as deprecated (v1.0).

**Use Case**: Useful for importing catalog data or initializing multiple items at once.

**Prerequisites**:
- **CategoryId**: Use category endpoints to find or create appropriate categories
- **InventoryTypeId**: Use reference data to get valid inventory type IDs (parts, consumables)

**Workflow**:
1. Prepare an array of catalog items with name, item number, and cost info
2. Assign each item to a category using `CategoryId`
3. Submit the batch create request
4. After creation, use [POST /api/v1.0/inventory/inventories/new](#/Inventory/createInventory) to add stock at locations

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | Array of inventory items to create. |

#### Returns

- Typed call return: `InventoryItemBatchCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InventoryItemBatchCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_inventory_action`

Provenance: Golden OpenAPI contract

Operation ID: `deleteInventoryAction`

- Sync: `client.inventory.delete_inventory_action(inventory_action_id=..., timeout=None)`
- Async: `await client.inventory.delete_inventory_action(inventory_action_id=..., timeout=None)`
- Raw payload: `client.inventory.delete_inventory_action.raw(inventory_action_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/inventory/actions/{InventoryActionId}`
- Source controller: `IncidentIQ API`

Delete inventory action

Deletes an inventory action by its unique identifier.

**Note**: This API is marked as deprecated (v1.0). This performs a soft delete, marking the action as deleted.

**Prerequisites**:
- **InventoryActionId**: Use [POST /api/v1.0/inventory/actions/query](#/Inventory/queryInventoryActions) to find the action ID.

**Workflow**:
1. Query inventory actions to find the specific action to delete
2. Extract the `InventoryActionId` from the result
3. Call this endpoint with the ID to soft-delete the action

**Note**: Soft-deleted actions are marked as deleted but retained in the database for audit purposes.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `inventory_action_id` | `InventoryActionId` | `path` | `yes` | `str` | `-` | Unique identifier of the inventory action to delete. |

#### Returns

- Typed call return: `InventoryDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InventoryDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_inventory_actions_by_ids`

Provenance: Golden OpenAPI contract

Operation ID: `deleteInventoryActionsByIds`

- Sync: `client.inventory.delete_inventory_actions_by_ids(body=..., timeout=None)`
- Async: `await client.inventory.delete_inventory_actions_by_ids(body=..., timeout=None)`
- Raw payload: `client.inventory.delete_inventory_actions_by_ids.raw(body=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/inventory/actions/ids`
- Source controller: `IncidentIQ API`

Delete inventory actions by IDs

Deletes multiple inventory actions by their unique identifiers.

**Note**: This API is marked as deprecated (v1.0). Use this for targeted deletion of specific actions.

**Prerequisites**:
- **InventoryActionIds**: Use [POST /api/v1.0/inventory/actions/query](#/Inventory/queryInventoryActions) to find action IDs to delete.

**Workflow**:
1. Query actions to identify which ones to delete
2. Extract `InventoryActionId` values from the response
3. Submit the array of IDs to this endpoint

**Caution**: Deleted actions cannot be recovered. This is a soft delete operation.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | Array of inventory action IDs to delete. |

#### Returns

- Typed call return: `InventoryActionBatchDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InventoryActionBatchDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_inventory_actions_by_query`

Provenance: Golden OpenAPI contract

Operation ID: `deleteInventoryActionsByQuery`

- Sync: `client.inventory.delete_inventory_actions_by_query(body=None, timeout=None)`
- Async: `await client.inventory.delete_inventory_actions_by_query(body=None, timeout=None)`
- Raw payload: `client.inventory.delete_inventory_actions_by_query.raw(body=None, timeout=None)`
- HTTP route: `DELETE /api/v1.0/inventory/actions/query`
- Source controller: `IncidentIQ API`

Delete inventory actions by query

Deletes inventory actions matching the specified query filter.

**Note**: This API is marked as deprecated (v1.0). Use with caution - this affects all actions matching the filter criteria.

**Workflow**:
1. Build a query filter to identify target actions (e.g., by `InventoryItemId` or `InventoryId`)
2. Optionally preview matching records using [POST /api/v1.0/inventory/actions/query](#/Inventory/queryInventoryActions)
3. Submit the delete request with the same filter criteria

**Caution**: This is a bulk delete operation. Verify your filter criteria carefully before executing to avoid unintended data loss.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `GetInventoryActionsRequest` | `GetInventoryActionsRequest` | Query filter to identify actions to delete. |

#### Returns

- Typed call return: `InventoryActionBatchDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InventoryActionBatchDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_inventory_item`

Provenance: Golden OpenAPI contract

Operation ID: `deleteInventoryItem`

- Sync: `client.inventory.delete_inventory_item(inventory_item_id=..., timeout=None)`
- Async: `await client.inventory.delete_inventory_item(inventory_item_id=..., timeout=None)`
- Raw payload: `client.inventory.delete_inventory_item.raw(inventory_item_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/inventory/items/{InventoryItemId}`
- Source controller: `IncidentIQ API`

Delete inventory catalog item

Deletes an inventory catalog item by its unique identifier.

**Note**: This API is marked as deprecated (v1.0). This performs a soft delete, marking the item as deleted.

**Prerequisites**:
- **InventoryItemId**: Use [POST /api/v1.0/inventory/items/query](#/Inventory/queryInventoryItems) to find the item ID.

**Workflow**:
1. Query the catalog to find the item to delete
2. Extract the `InventoryItemId` from the result
3. Verify no active stock exists using [POST /api/v1.0/inventory/inventories](#/Inventory/queryInventories)
4. Call this endpoint to soft-delete the catalog item

**Note**: Items with active stock may be restricted from deletion.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `inventory_item_id` | `InventoryItemId` | `path` | `yes` | `str` | `-` | Unique identifier of the inventory catalog item to delete. |

#### Returns

- Typed call return: `InventoryDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InventoryDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_inventory_items_by_ids`

Provenance: Golden OpenAPI contract

Operation ID: `deleteInventoryItemsByIds`

- Sync: `client.inventory.delete_inventory_items_by_ids(body=..., timeout=None)`
- Async: `await client.inventory.delete_inventory_items_by_ids(body=..., timeout=None)`
- Raw payload: `client.inventory.delete_inventory_items_by_ids.raw(body=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/inventory/items/ids`
- Source controller: `IncidentIQ API`

Delete inventory items by IDs

Deletes multiple inventory catalog items by their unique identifiers.

**Note**: This API is marked as deprecated (v1.0). Use this for targeted deletion of specific items.

**Prerequisites**:
- **InventoryItemIds**: Use [POST /api/v1.0/inventory/items/query](#/Inventory/queryInventoryItems) to find item IDs to delete.

**Workflow**:
1. Query the catalog to identify items to delete
2. Extract `InventoryItemId` values from the response
3. Submit the array of IDs to this endpoint

**Caution**: This performs a soft delete. Items with active stock may be restricted from deletion. Verify associated stock is cleared first.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | Array of inventory item IDs to delete. |

#### Returns

- Typed call return: `InventoryItemBatchDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InventoryItemBatchDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_inventory_items_by_query`

Provenance: Golden OpenAPI contract

Operation ID: `deleteInventoryItemsByQuery`

- Sync: `client.inventory.delete_inventory_items_by_query(body=None, timeout=None)`
- Async: `await client.inventory.delete_inventory_items_by_query(body=None, timeout=None)`
- Raw payload: `client.inventory.delete_inventory_items_by_query.raw(body=None, timeout=None)`
- HTTP route: `DELETE /api/v1.0/inventory/items/query`
- Source controller: `IncidentIQ API`

Delete inventory items by query

Deletes inventory catalog items matching the specified query filter.

**Note**: This API is marked as deprecated (v1.0). Use with caution - this affects all items matching the filter criteria.

**Workflow**:
1. Build a query filter (e.g., by category, keyword, or custom facets)
2. Preview matching items using [POST /api/v1.0/inventory/items/query](#/Inventory/queryInventoryItems)
3. Submit the delete request with the same filter criteria

**Caution**: This is a bulk delete operation. Items with active stock entries may be restricted from deletion. Verify filter criteria carefully before executing to avoid unintended data loss.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `GetInventoryItemsRequest` | `GetInventoryItemsRequest` | Query filter to identify items to delete. |

#### Returns

- Typed call return: `InventoryItemBatchDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InventoryItemBatchDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_inventory_action`

Provenance: Golden OpenAPI contract

Operation ID: `getInventoryAction`

- Sync: `client.inventory.get_inventory_action(inventory_action_id=..., timeout=None)`
- Async: `await client.inventory.get_inventory_action(inventory_action_id=..., timeout=None)`
- Raw payload: `client.inventory.get_inventory_action.raw(inventory_action_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/inventory/actions/{InventoryActionId}`
- Source controller: `IncidentIQ API`

Get inventory action by ID

Retrieves a single inventory action record by its unique identifier.

**Note**: This API is marked as deprecated (v1.0). Returns the action including related Inventory, CreatedByUser, and Ticket details when requested via the Fields parameter.

**Prerequisites**:
- **InventoryActionId**: Use [POST /api/v1.0/inventory/actions/query](#/Inventory/queryInventoryActions) to search for actions and extract `InventoryActionId` from results.

**Response Includes**:
- Action details: type, quantity, cost, date
- Related `Inventory` object (stock entry)
- `CreatedByUser` who recorded the action
- `Ticket` if action is linked to a service request

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `inventory_action_id` | `InventoryActionId` | `path` | `yes` | `str` | `-` | Unique identifier of the inventory action record. |

#### Returns

- Typed call return: `InventoryActionItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InventoryActionItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_inventory_action_post`

Provenance: Golden OpenAPI contract

Operation ID: `getInventoryActionPost`

- Sync: `client.inventory.get_inventory_action_post(inventory_action_id=..., body=None, timeout=None)`
- Async: `await client.inventory.get_inventory_action_post(inventory_action_id=..., body=None, timeout=None)`
- Raw payload: `client.inventory.get_inventory_action_post.raw(inventory_action_id=..., body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/inventory/actions/{InventoryActionId}`
- Source controller: `IncidentIQ API`

Get inventory action by ID (POST)

Retrieves a single inventory action by its unique identifier using POST method.

**Note**: This API is marked as deprecated (v1.0). The POST variant allows passing additional request options in the body for field projections.

**Advantages over GET**:
- Control which related objects are expanded via `Fields` parameter
- Specify `IncludeTicket`, `IncludeInventory`, or `IncludeCreatedByUser` flags

**Related Endpoints**:
- Simple retrieval: [GET /api/v1.0/inventory/actions/{InventoryActionId}](#/Inventory/getInventoryAction)
- Query multiple: [POST /api/v1.0/inventory/actions/query](#/Inventory/queryInventoryActions)

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `inventory_action_id` | `InventoryActionId` | `path` | `yes` | `str` | `-` | Unique identifier of the inventory action record. |
| `body` | `body` | `body` | `no` | `GetInventoryActionsRequest` | `GetInventoryActionsRequest` | Optional request options for field projections. |

#### Returns

- Typed call return: `InventoryActionItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InventoryActionItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_inventory_actions_by_ids`

Provenance: Golden OpenAPI contract

Operation ID: `getInventoryActionsByIds`

- Sync: `client.inventory.get_inventory_actions_by_ids(body=..., timeout=None)`
- Async: `await client.inventory.get_inventory_actions_by_ids(body=..., timeout=None)`
- Raw payload: `client.inventory.get_inventory_actions_by_ids.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/inventory/actions/ids`
- Source controller: `IncidentIQ API`

Get inventory actions by IDs

Retrieves multiple inventory actions by their unique identifiers.

**Note**: This API is marked as deprecated (v1.0). Use this when you have a list of known action IDs and want to fetch their details in a single request.

**Route Conflict**: This endpoint shares a route with batch create (`/inventory/actions/ids/new`). The server distinguishes by request body type - this endpoint expects an array of UUIDs.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | Array of inventory action IDs to retrieve. |

#### Returns

- Typed call return: `InventoryActionListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InventoryActionListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_inventory_actions_timeline`

Provenance: Golden OpenAPI contract

Operation ID: `getInventoryActionsTimeline`

- Sync: `client.inventory.get_inventory_actions_timeline(action_type_id=None, inventory_item_id=None, inventory_id=None, inventory_action_group_key=None, timeout=None)`
- Async: `await client.inventory.get_inventory_actions_timeline(action_type_id=None, inventory_item_id=None, inventory_id=None, inventory_action_group_key=None, timeout=None)`
- Raw payload: `client.inventory.get_inventory_actions_timeline.raw(action_type_id=None, inventory_item_id=None, inventory_id=None, inventory_action_group_key=None, timeout=None)`
- HTTP route: `GET /api/v1.0/inventory/actions/timeline`
- Source controller: `IncidentIQ API`

Get inventory actions timeline

Retrieves inventory actions in timeline format, grouping related actions and including ticket associations.

**Note**: This API is marked as deprecated (v1.0).

**Use Case**: Useful for displaying a chronological history of inventory changes with ticket context.

**Filter Parameters**:
- `ActionTypeId` - Filter by action type (consumption, addition, transfer)
- `InventoryItemId` - Filter to a specific catalog item
- `InventoryId` - Filter to a specific stock entry
- `InventoryActionGroupKey` - Filter to actions in a specific group

**Response**: Returns grouped actions with expanded `Ticket`, `CreatedByUser`, and `Inventory` objects for UI timeline rendering.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `action_type_id` | `ActionTypeId` | `query` | `no` | `str` | `-` | Filter to actions of a specific type. |
| `inventory_item_id` | `InventoryItemId` | `query` | `no` | `str` | `-` | Filter to actions for a specific catalog item. |
| `inventory_id` | `InventoryId` | `query` | `no` | `str` | `-` | Filter to actions for a specific inventory stock record. |
| `inventory_action_group_key` | `InventoryActionGroupKey` | `query` | `no` | `str` | `-` | Filter to actions belonging to a specific group key. |

#### Returns

- Typed call return: `InventoryTimelineListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InventoryTimelineListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_inventory_actions_timeline_post`

Provenance: Golden OpenAPI contract

Operation ID: `getInventoryActionsTimelinePost`

- Sync: `client.inventory.get_inventory_actions_timeline_post(body=None, timeout=None)`
- Async: `await client.inventory.get_inventory_actions_timeline_post(body=None, timeout=None)`
- Raw payload: `client.inventory.get_inventory_actions_timeline_post.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/inventory/actions/timeline`
- Source controller: `IncidentIQ API`

Get inventory actions timeline (POST)

Retrieves inventory actions in timeline format using POST method.

**Note**: This API is marked as deprecated (v1.0). The POST variant allows passing additional request options in the body for field projections and paging.

**Advantages over GET**:
- Full paging support with `PageIndex`, `PageSize`, and sorting options
- Field projections to control which related objects are included
- Complex filtering via request body

**Related Endpoints**:
- For simple queries: [GET /api/v1.0/inventory/actions/timeline](#/Inventory/getInventoryActionsTimeline)
- For raw action data: [POST /api/v1.0/inventory/actions/query](#/Inventory/queryInventoryActions)

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `GetInventoryActionsRequest` | `GetInventoryActionsRequest` | Request options for timeline query. |

#### Returns

- Typed call return: `InventoryTimelineListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InventoryTimelineListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_inventory_by_id`

Provenance: Golden OpenAPI contract

Operation ID: `getInventoryById`

- Sync: `client.inventory.get_inventory_by_id(inventory_id=..., timeout=None)`
- Async: `await client.inventory.get_inventory_by_id(inventory_id=..., timeout=None)`
- Raw payload: `client.inventory.get_inventory_by_id.raw(inventory_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/inventory/inventories/{InventoryId}`
- Source controller: `IncidentIQ API`

Get inventory stock by ID

Retrieves a single inventory stock record by its unique identifier.

**Note**: This API is marked as deprecated (v1.0). Returns the inventory stock entry including related InventoryItem and Location details when requested via the Fields parameter.

**Prerequisites**:
- **InventoryId**: Use [POST /api/v1.0/inventory/inventories](#/Inventory/queryInventories) to search stock records and extract `InventoryId`.

**Response Includes**:
- Stock details: quantity, average cost, min/max thresholds
- Related `InventoryItem` (catalog item)
- `Location` where stock is held

**Related Endpoints**:
- Update: [POST /api/v1.0/inventory/inventories/{InventoryId}/update](#/Inventory/updateInventory)

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `inventory_id` | `InventoryId` | `path` | `yes` | `str` | `-` | Unique identifier of the inventory stock record. |

#### Returns

- Typed call return: `InventoryStockDetailResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InventoryStockDetailResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_inventory_by_id_post`

Provenance: Golden OpenAPI contract

Operation ID: `getInventoryByIdPost`

- Sync: `client.inventory.get_inventory_by_id_post(inventory_id=..., body=None, timeout=None)`
- Async: `await client.inventory.get_inventory_by_id_post(inventory_id=..., body=None, timeout=None)`
- Raw payload: `client.inventory.get_inventory_by_id_post.raw(inventory_id=..., body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/inventory/inventories/{InventoryId}`
- Source controller: `IncidentIQ API`

Get inventory stock by ID (POST)

Retrieves a single inventory stock record by its unique identifier using POST method.

**Note**: This API is marked as deprecated (v1.0). The POST variant allows passing additional request options in the body for field projections.

**Advantages over GET**:
- Control which related objects are expanded via `Fields` parameter
- Request `InventoryItem`, `Location`, or custom field values

**Related Endpoints**:
- Simple retrieval: [GET /api/v1.0/inventory/inventories/{InventoryId}](#/Inventory/getInventoryById)
- Query multiple: [POST /api/v1.0/inventory/inventories](#/Inventory/queryInventories)
- Update: [POST /api/v1.0/inventory/inventories/{InventoryId}/update](#/Inventory/updateInventory)

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `inventory_id` | `InventoryId` | `path` | `yes` | `str` | `-` | Unique identifier of the inventory stock record. |
| `body` | `body` | `body` | `no` | `GetInventoriesRequest` | `GetInventoriesRequest` | Optional request options for field projections. |

#### Returns

- Typed call return: `InventoryStockDetailResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InventoryStockDetailResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_inventory_by_query`

Provenance: Golden OpenAPI contract

Operation ID: `getInventoryByQuery`

- Sync: `client.inventory.get_inventory_by_query(inventory_id=..., timeout=None)`
- Async: `await client.inventory.get_inventory_by_query(inventory_id=..., timeout=None)`
- Raw payload: `client.inventory.get_inventory_by_query.raw(inventory_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/inventory/{InventoryId}`
- Source controller: `IncidentIQ API`

Query inventory with InventoryId filter

Retrieves inventory stock records filtered by the specified InventoryId. Unlike the direct get endpoint, this returns a list response and supports custom filters.

**Note**: This API is marked as deprecated (v1.0). Supports the `SupportsCustomFilters` attribute for advanced filtering.

**Use Case**: When you know a specific `InventoryId` but want list-style response formatting with custom filter support.

**Related Endpoints**:
- Single record: [GET /api/v1.0/inventory/inventories/{InventoryId}](#/Inventory/getInventoryById) - Returns single item response
- Full query: [POST /api/v1.0/inventory/inventories](#/Inventory/queryInventories) - Advanced filtering without path constraint

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `inventory_id` | `InventoryId` | `path` | `yes` | `str` | `-` | Unique identifier used as a filter for inventory stock records. |

#### Returns

- Typed call return: `InventoryListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InventoryListGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_inventory_category_summary`

Provenance: Golden OpenAPI contract

Operation ID: `getInventoryCategorySummary`

- Sync: `client.inventory.get_inventory_category_summary(timeout=None)`
- Async: `await client.inventory.get_inventory_category_summary(timeout=None)`
- Raw payload: `client.inventory.get_inventory_category_summary.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/inventory/category-summary`
- Source controller: `IncidentIQ API`

Get inventory category summary

Retrieves a hierarchical summary of inventory organized by category. Returns a tree structure showing categories, their child categories, and inventory item counts.

**Note**: This API is marked as deprecated (v1.0).

**Use Case**: Useful for building category navigation trees in inventory management interfaces, showing how much stock exists in each category.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `InventoryCategorySummaryResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InventoryCategorySummaryResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_inventory_item_by_id`

Provenance: Golden OpenAPI contract

Operation ID: `getInventoryItemById`

- Sync: `client.inventory.get_inventory_item_by_id(inventory_item_id=..., timeout=None)`
- Async: `await client.inventory.get_inventory_item_by_id(inventory_item_id=..., timeout=None)`
- Raw payload: `client.inventory.get_inventory_item_by_id.raw(inventory_item_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/inventory/items/{InventoryItemId}`
- Source controller: `IncidentIQ API`

Get inventory catalog item by ID

Retrieves a single inventory catalog item (part or consumable) by its unique identifier.

**Note**: This API is marked as deprecated (v1.0). Returns the full item details including category, custom fields, and stock information.

**Prerequisites**:
- **InventoryItemId**: Use [POST /api/v1.0/inventory/items/query](#/Inventory/queryInventoryItems) to search the catalog and extract `InventoryItemId`.

**Response Includes**:
- Item details: name, item number, description, cost
- Category information
- Custom field values
- Stock summary across locations

**Related Endpoints**:
- Update: [POST /api/v1.0/inventory/items/{InventoryItemId}/update](#/Inventory/updateInventoryItem)

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `inventory_item_id` | `InventoryItemId` | `path` | `yes` | `str` | `-` | Unique identifier of the inventory catalog item. |

#### Returns

- Typed call return: `InventoryItemGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InventoryItemGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_inventory_item_by_id_post`

Provenance: Golden OpenAPI contract

Operation ID: `getInventoryItemByIdPost`

- Sync: `client.inventory.get_inventory_item_by_id_post(inventory_item_id=..., body=None, timeout=None)`
- Async: `await client.inventory.get_inventory_item_by_id_post(inventory_item_id=..., body=None, timeout=None)`
- Raw payload: `client.inventory.get_inventory_item_by_id_post.raw(inventory_item_id=..., body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/inventory/items/{InventoryItemId}`
- Source controller: `IncidentIQ API`

Get inventory catalog item by ID (POST)

Retrieves a single inventory catalog item by its unique identifier using POST method.

**Note**: This API is marked as deprecated (v1.0). The POST variant allows passing additional request options in the body for field projections.

**Advantages over GET**:
- Control which related objects are expanded via `Fields` parameter
- Request `Category`, custom field values, or stock summaries

**Related Endpoints**:
- Simple retrieval: [GET /api/v1.0/inventory/items/{InventoryItemId}](#/Inventory/getInventoryItemById)
- Query multiple: [POST /api/v1.0/inventory/items/query](#/Inventory/queryInventoryItems)
- Update: [POST /api/v1.0/inventory/items/{InventoryItemId}/update](#/Inventory/updateInventoryItem)

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `inventory_item_id` | `InventoryItemId` | `path` | `yes` | `str` | `-` | Unique identifier of the inventory catalog item. |
| `body` | `body` | `body` | `no` | `GetInventoryItemsRequest` | `GetInventoryItemsRequest` | Optional request options for field projections. |

#### Returns

- Typed call return: `InventoryItemGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InventoryItemGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_inventory_items_by_ids`

Provenance: Golden OpenAPI contract

Operation ID: `getInventoryItemsByIds`

- Sync: `client.inventory.get_inventory_items_by_ids(body=..., timeout=None)`
- Async: `await client.inventory.get_inventory_items_by_ids(body=..., timeout=None)`
- Raw payload: `client.inventory.get_inventory_items_by_ids.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/inventory/items/ids`
- Source controller: `IncidentIQ API`

Get inventory items by IDs

Retrieves multiple inventory catalog items by their unique identifiers.

**Note**: This API is marked as deprecated (v1.0). Use this when you have a list of known item IDs and want to fetch their details in a single request.

**Prerequisites**:
- **InventoryItemIds**: Obtain IDs from [POST /api/v1.0/inventory/items/query](#/Inventory/queryInventoryItems) or from inventory stock records.

**Workflow**:
1. Query the catalog or stock records to collect `InventoryItemId` values
2. Submit an array of IDs to retrieve full item details
3. Use for bulk display or export operations

**Response**: Full item details including category, stock summary, and custom fields.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | Array of inventory item IDs to retrieve. |

#### Returns

- Typed call return: `InventoryItemListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InventoryItemListGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_inventory_location_category_summary`

Provenance: Golden OpenAPI contract

Operation ID: `getInventoryLocationCategorySummary`

- Sync: `client.inventory.get_inventory_location_category_summary(timeout=None)`
- Async: `await client.inventory.get_inventory_location_category_summary(timeout=None)`
- Raw payload: `client.inventory.get_inventory_location_category_summary.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/inventory/location-category-summary`
- Source controller: `IncidentIQ API`

Get inventory location category summary

Retrieves a hierarchical summary of inventory organized by location and category. Returns a tree structure showing locations, their categories, and inventory counts.

**Note**: This API is marked as deprecated (v1.0).

**Use Case**: Useful for building location-based inventory views, showing stock distribution across locations and categories with alert indicators for low stock.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `InventoryLocationCategorySummaryResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InventoryLocationCategorySummaryResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_inventories`

Provenance: Golden OpenAPI contract

Operation ID: `listInventories`

- Sync: `client.inventory.list_inventories(inventory_item_id=None, location_id=None, timeout=None)`
- Async: `await client.inventory.list_inventories(inventory_item_id=None, location_id=None, timeout=None)`
- Raw payload: `client.inventory.list_inventories.raw(inventory_item_id=None, location_id=None, timeout=None)`
- HTTP route: `GET /api/v1.0/inventory/inventories`
- Source controller: `IncidentIQ API`

List all inventory stock records

Retrieves a paginated list of inventory stock records. Supports filtering by InventoryItemId and LocationId query parameters.

**Note**: This API is marked as deprecated (v1.0). Supports the `SupportsCustomFilters` attribute for advanced filtering.

**Filter Parameters**:
- `InventoryItemId` - Filter to stock for a specific catalog item
- `LocationId` - Filter to stock at a specific location

**Related Endpoints**:
- For complex queries: [POST /api/v1.0/inventory/inventories](#/Inventory/queryInventories)
- Single stock record: [GET /api/v1.0/inventory/inventories/{InventoryId}](#/Inventory/getInventoryById)
- Create stock: [POST /api/v1.0/inventory/inventories/new](#/Inventory/createInventory)

**Prerequisites**
1. **LocationId** - Use [GET /api/v2.0/locations](#/Locations/getMyLocationsV2) to obtain. Extract `Items[].LocationId` from response.

**Workflow Example**
1. Obtain LocationId: [GET /api/v2.0/locations](#/Locations/getMyLocationsV2) → extract `Items[].LocationId`
2. Call this endpoint: [GET /api/v1.0/inventory/inventories](#/Locations/listInventories)

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `inventory_item_id` | `InventoryItemId` | `query` | `no` | `str` | `-` | Filter results to a specific catalog item. |
| `location_id` | `LocationId` | `query` | `no` | `str` | `-` | Filter results to a specific location. |

#### Returns

- Typed call return: `InventoryListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InventoryListGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `query_inventories`

Provenance: Golden OpenAPI contract

Operation ID: `queryInventories`

- Sync: `client.inventory.query_inventories(body=None, timeout=None)`
- Async: `await client.inventory.query_inventories(body=None, timeout=None)`
- Raw payload: `client.inventory.query_inventories.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/inventory/inventories`
- Source controller: `IncidentIQ API`

Query inventory stock records

Queries inventory stock records with advanced filtering, paging, and field projection options.

**Note**: This API is marked as deprecated (v1.0). Supports the `SupportsCustomFilters` attribute.

**Workflow**:
1. Use this endpoint to search for inventory stock at specific locations
2. Filter by `InventoryItemId` to find stock for a specific catalog item
3. Filter by `LocationId` to find all stock at a specific location
4. Results include expanded `InventoryItem` and `Location` objects when requested via Fields

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `GetInventoriesRequest` | `GetInventoriesRequest` | Request options including filters for InventoryItemId and LocationId. |

#### Returns

- Typed call return: `InventoryListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InventoryListGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `query_inventory_actions`

Provenance: Golden OpenAPI contract

Operation ID: `queryInventoryActions`

- Sync: `client.inventory.query_inventory_actions(body=None, timeout=None)`
- Async: `await client.inventory.query_inventory_actions(body=None, timeout=None)`
- Raw payload: `client.inventory.query_inventory_actions.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/inventory/actions/query`
- Source controller: `IncidentIQ API`

Query inventory actions

Queries inventory actions with advanced filtering, paging, and field projection options.

**Note**: This API is marked as deprecated (v1.0). Supports the `SupportsCustomFilters` attribute.

**Workflow**:
1. Use this endpoint to search for inventory actions
2. Filter by `InventoryItemId` to find actions for a specific catalog item
3. Filter by `InventoryId` to find actions for a specific stock entry
4. Filter by `EntityId` to find actions related to a ticket
5. Results include expanded `Inventory`, `CreatedByUser`, and `Ticket` objects when requested via Fields

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `GetInventoryActionsRequest` | `GetInventoryActionsRequest` | Request options including filters for inventory actions. |

#### Returns

- Typed call return: `InventoryActionListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InventoryActionListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `query_inventory_actions_get`

Provenance: Golden OpenAPI contract

Operation ID: `queryInventoryActionsGet`

- Sync: `client.inventory.query_inventory_actions_get(action_type_id=None, inventory_item_id=None, inventory_id=None, entity_id=None, inventory_action_group_key=None, timeout=None)`
- Async: `await client.inventory.query_inventory_actions_get(action_type_id=None, inventory_item_id=None, inventory_id=None, entity_id=None, inventory_action_group_key=None, timeout=None)`
- Raw payload: `client.inventory.query_inventory_actions_get.raw(action_type_id=None, inventory_item_id=None, inventory_id=None, entity_id=None, inventory_action_group_key=None, timeout=None)`
- HTTP route: `GET /api/v1.0/inventory/actions/query`
- Source controller: `IncidentIQ API`

Query inventory actions (GET)

Retrieves inventory actions using GET method with query parameters.

**Note**: This API is marked as deprecated (v1.0). Supports the `SupportsCustomFilters` attribute for advanced filtering.

**Use Case**: Simple filtering via query parameters. For complex queries with paging and field projections, use [POST /api/v1.0/inventory/actions/query](#/Inventory/queryInventoryActions) instead.

**Filter Parameters**:
- `ActionTypeId` - Filter by action type (consumption, addition, etc.)
- `InventoryItemId` - Filter by catalog item
- `InventoryId` - Filter by specific stock entry
- `EntityId` - Filter by related ticket or entity

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `action_type_id` | `ActionTypeId` | `query` | `no` | `str` | `-` | Filter to actions of a specific type. |
| `inventory_item_id` | `InventoryItemId` | `query` | `no` | `str` | `-` | Filter to actions for a specific catalog item. |
| `inventory_id` | `InventoryId` | `query` | `no` | `str` | `-` | Filter to actions for a specific inventory stock record. |
| `entity_id` | `EntityId` | `query` | `no` | `str` | `-` | Filter to actions related to a specific entity (e.g., ticket). |
| `inventory_action_group_key` | `InventoryActionGroupKey` | `query` | `no` | `str` | `-` | Filter to actions belonging to a specific group key. |

#### Returns

- Typed call return: `InventoryActionListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InventoryActionListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `query_inventory_by_id_post`

Provenance: Golden OpenAPI contract

Operation ID: `queryInventoryByIdPost`

- Sync: `client.inventory.query_inventory_by_id_post(inventory_id=..., body=None, timeout=None)`
- Async: `await client.inventory.query_inventory_by_id_post(inventory_id=..., body=None, timeout=None)`
- Raw payload: `client.inventory.query_inventory_by_id_post.raw(inventory_id=..., body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/inventory/{InventoryId}`
- Source controller: `IncidentIQ API`

Query inventory with InventoryId filter (POST)

Retrieves inventory stock records filtered by the specified InventoryId using POST method.

**Note**: This API is marked as deprecated (v1.0). The POST variant allows passing additional request options in the body for field projections and custom filters.

**Advantages over GET**:
- Full paging support with `PageIndex`, `PageSize`, and sorting
- Field projections to control which related objects are included
- Additional filter criteria via request body

**Related Endpoints**:
- Simple query: [GET /api/v1.0/inventory/{InventoryId}](#/Inventory/getInventoryByQuery)
- Full query: [POST /api/v1.0/inventory/inventories](#/Inventory/queryInventories)

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `inventory_id` | `InventoryId` | `path` | `yes` | `str` | `-` | Unique identifier used as a filter for inventory stock records. |
| `body` | `body` | `body` | `no` | `GetInventoriesRequest` | `GetInventoriesRequest` | Request options including filters, paging, and field projections. |

#### Returns

- Typed call return: `InventoryListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InventoryListGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `query_inventory_items`

Provenance: Golden OpenAPI contract

Operation ID: `queryInventoryItems`

- Sync: `client.inventory.query_inventory_items(body=None, timeout=None)`
- Async: `await client.inventory.query_inventory_items(body=None, timeout=None)`
- Raw payload: `client.inventory.query_inventory_items.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/inventory/items/query`
- Source controller: `IncidentIQ API`

Query inventory catalog items

Queries inventory catalog items with advanced filtering, paging, and field projection options.

**Note**: This API is marked as deprecated (v1.0). Supports the `SupportsCustomFilters` attribute.

**Workflow**:
1. Use this endpoint to search the parts catalog
2. Filter by category, keyword, or custom facets
3. Results include category details and stock information
4. Use returned `InventoryItemId` values for stock operations

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `GetInventoryItemsRequest` | `GetInventoryItemsRequest` | Request options including filters, paging, and field projections. |

#### Returns

- Typed call return: `InventoryItemListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InventoryItemListGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `query_inventory_items_legacy`

Provenance: Golden OpenAPI contract

Operation ID: `queryInventoryItemsLegacy`

- Sync: `client.inventory.query_inventory_items_legacy(timeout=None)`
- Async: `await client.inventory.query_inventory_items_legacy(timeout=None)`
- Raw payload: `client.inventory.query_inventory_items_legacy.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/inventory/items/query`
- Source controller: `IncidentIQ API`

Query inventory catalog items (legacy GET)

Queries inventory catalog items using GET method. This legacy endpoint is deprecated - use the POST variant instead.

**Note**: This API is marked as deprecated (v1.0). Supports the `SupportsCustomFilters` attribute for advanced filtering.

**Recommended Alternative**: Use [POST /api/v1.0/inventory/items/query](#/Inventory/queryInventoryItems) for full functionality including:
- Keyword and category filtering
- Paging with sort options
- Field projections
- Custom facet filters

**Response**: Returns a paginated list of catalog items with category details and stock summary information.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `InventoryItemListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InventoryItemListGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_inventories_by_ids`

Provenance: Golden OpenAPI contract

Operation ID: `updateInventoriesByIds`

- Sync: `client.inventory.update_inventories_by_ids(body=..., timeout=None)`
- Async: `await client.inventory.update_inventories_by_ids(body=..., timeout=None)`
- Raw payload: `client.inventory.update_inventories_by_ids.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/inventory/inventories/ids/update`
- Source controller: `IncidentIQ API`

Update multiple inventory records by IDs

Updates multiple inventory stock records by their unique identifiers, allowing different update values for each record.

**Note**: This API is marked as deprecated (v1.0).

**Use Case**: Useful when you need to update multiple records with different values (e.g., different quantities at different locations).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | Array of inventory stock records with their InventoryId and update values. |

#### Returns

- Typed call return: `InventoryBatchUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InventoryBatchUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_inventories_by_query`

Provenance: Golden OpenAPI contract

Operation ID: `updateInventoriesByQuery`

- Sync: `client.inventory.update_inventories_by_query(body=..., timeout=None)`
- Async: `await client.inventory.update_inventories_by_query(body=..., timeout=None)`
- Raw payload: `client.inventory.update_inventories_by_query.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/inventory/inventories/query/update`
- Source controller: `IncidentIQ API`

Update inventory records by query

Updates multiple inventory stock records matching a query filter with the same update values.

**Note**: This API is marked as deprecated (v1.0).

**Use Case**: Useful for bulk updates like adjusting minimum quantities for all stock at a location, or updating state types across multiple records.

**Workflow**:
1. Build a query filter (e.g., by `InventoryItemId` or `LocationId`)
2. Preview matching records using [POST /api/v1.0/inventory/inventories](#/Inventory/queryInventories)
3. Prepare the update object with new values
4. Submit the query-based update request

**Updatable Fields**: `QuantityAvailable`, `AverageCost`, `MinQuantityAvailable`, `MaxQuantityAvailable`, `TrackInventory`

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `UpdateInventoriesRequest` | `UpdateInventoriesRequest` | Query filter and update values to apply to matching records. |

#### Returns

- Typed call return: `InventoryBatchUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InventoryBatchUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_inventory`

Provenance: Golden OpenAPI contract

Operation ID: `updateInventory`

- Sync: `client.inventory.update_inventory(inventory_id=..., body=..., timeout=None)`
- Async: `await client.inventory.update_inventory(inventory_id=..., body=..., timeout=None)`
- Raw payload: `client.inventory.update_inventory.raw(inventory_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/inventory/inventories/{InventoryId}/update`
- Source controller: `IncidentIQ API`

Update inventory stock record

Updates an existing inventory stock record with new values.

**Note**: This API is marked as deprecated (v1.0).

**Updatable Fields**:
- `QuantityAvailable` - Current stock quantity
- `AverageCost` - Average unit cost
- `MinQuantityAvailable` - Reorder threshold
- `MaxQuantityAvailable` - Overstock threshold
- `TrackInventory` - Whether to actively track this stock
- `SupplierId` - Associated supplier
- `InventoryStateTypeId` - Current state type

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `inventory_id` | `InventoryId` | `path` | `yes` | `str` | `-` | Unique identifier of the inventory stock record to update. |
| `body` | `body` | `body` | `yes` | `UpdateInventoryRequest` | `UpdateInventoryRequest` | Updated inventory stock record data. |

#### Returns

- Typed call return: `InventoryUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InventoryUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_inventory_action`

Provenance: Golden OpenAPI contract

Operation ID: `updateInventoryAction`

- Sync: `client.inventory.update_inventory_action(inventory_action_id=..., body=..., timeout=None)`
- Async: `await client.inventory.update_inventory_action(inventory_action_id=..., body=..., timeout=None)`
- Raw payload: `client.inventory.update_inventory_action.raw(inventory_action_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/inventory/actions/{InventoryActionId}/update`
- Source controller: `IncidentIQ API`

Update inventory action

Updates an existing inventory action record.

**Note**: This API is marked as deprecated (v1.0).

**Updatable Fields**:
- `Quantity` - The quantity delta
- `UnitCost` - Unit cost for the transaction
- `Description` - Notes about the action
- `ActionDate` - When the action occurred
- `RelatedEntityId` - Link to a different entity

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `inventory_action_id` | `InventoryActionId` | `path` | `yes` | `str` | `-` | Unique identifier of the inventory action to update. |
| `body` | `body` | `body` | `yes` | `UpdateInventoryActionRequest` | `UpdateInventoryActionRequest` | Updated inventory action data. |

#### Returns

- Typed call return: `InventoryActionUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InventoryActionUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_inventory_actions_by_ids`

Provenance: Golden OpenAPI contract

Operation ID: `updateInventoryActionsByIds`

- Sync: `client.inventory.update_inventory_actions_by_ids(body=..., timeout=None)`
- Async: `await client.inventory.update_inventory_actions_by_ids(body=..., timeout=None)`
- Raw payload: `client.inventory.update_inventory_actions_by_ids.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/inventory/actions/ids/update`
- Source controller: `IncidentIQ API`

Update inventory actions by IDs

Updates multiple inventory actions by their unique identifiers, allowing different update values for each action.

**Note**: This API is marked as deprecated (v1.0).

**Use Case**: Useful when you need to update multiple actions with different values (e.g., different quantities or costs for each).

**Prerequisites**:
- **InventoryActionIds**: Use [POST /api/v1.0/inventory/actions/query](#/Inventory/queryInventoryActions) to find existing actions

**Workflow**:
1. Query actions to find records requiring updates
2. Prepare an array with each action's `InventoryActionId` and new values
3. Submit the batch update request

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | Array of inventory actions with their IDs and update values. |

#### Returns

- Typed call return: `InventoryActionBatchUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InventoryActionBatchUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_inventory_actions_by_query`

Provenance: Golden OpenAPI contract

Operation ID: `updateInventoryActionsByQuery`

- Sync: `client.inventory.update_inventory_actions_by_query(body=..., timeout=None)`
- Async: `await client.inventory.update_inventory_actions_by_query(body=..., timeout=None)`
- Raw payload: `client.inventory.update_inventory_actions_by_query.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/inventory/actions/query/update`
- Source controller: `IncidentIQ API`

Update inventory actions by query

Updates multiple inventory actions matching a query filter with the same update values.

**Note**: This API is marked as deprecated (v1.0).

**Use Case**: Useful for bulk updates like correcting unit costs across multiple actions or updating descriptions.

**Workflow**:
1. Build a query filter to identify target actions
2. Preview matching records using [POST /api/v1.0/inventory/actions/query](#/Inventory/queryInventoryActions)
3. Prepare the update object with new values
4. Submit the query-based update request

**Updatable Fields**: `Quantity`, `UnitCost`, `Description`, `ActionDate`, `RelatedEntityId`

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `UpdateInventoryActionsRequest` | `UpdateInventoryActionsRequest` | Query filter and update values to apply to matching actions. |

#### Returns

- Typed call return: `InventoryActionBatchUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InventoryActionBatchUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_inventory_item`

Provenance: Golden OpenAPI contract

Operation ID: `updateInventoryItem`

- Sync: `client.inventory.update_inventory_item(inventory_item_id=..., body=..., timeout=None)`
- Async: `await client.inventory.update_inventory_item(inventory_item_id=..., body=..., timeout=None)`
- Raw payload: `client.inventory.update_inventory_item.raw(inventory_item_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/inventory/items/{InventoryItemId}/update`
- Source controller: `IncidentIQ API`

Update inventory catalog item

Updates an existing inventory catalog item with new values.

**Note**: This API is marked as deprecated (v1.0).

**Updatable Fields**:
- `Name` - Display name
- `ItemNumber` - Part number or SKU
- `CategoryId` - Category classification
- `Description` - Long-form description
- `AverageCost` - Average unit cost
- `MinQuantityAvailable` - Reorder threshold
- `MaxQuantityAvailable` - Overstock threshold
- `TrackSupplier` / `TrackUnits` - Tracking options
- `CustomFieldValues` - Custom field data (when UpdateCustomFields is true)

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `inventory_item_id` | `InventoryItemId` | `path` | `yes` | `str` | `-` | Unique identifier of the inventory catalog item to update. |
| `body` | `body` | `body` | `yes` | `UpdateInventoryItemRequest` | `UpdateInventoryItemRequest` | Updated inventory item data. |

#### Returns

- Typed call return: `InventoryItemUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InventoryItemUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_inventory_items_by_ids`

Provenance: Golden OpenAPI contract

Operation ID: `updateInventoryItemsByIds`

- Sync: `client.inventory.update_inventory_items_by_ids(body=..., timeout=None)`
- Async: `await client.inventory.update_inventory_items_by_ids(body=..., timeout=None)`
- Raw payload: `client.inventory.update_inventory_items_by_ids.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/inventory/items/ids/update`
- Source controller: `IncidentIQ API`

Update inventory items by IDs

Updates multiple inventory catalog items by their unique identifiers, allowing different update values for each item.

**Note**: This API is marked as deprecated (v1.0).

**Use Case**: Useful when you need to update multiple items with different values (e.g., different costs or descriptions for each item).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | Array of inventory items with their IDs and update values. |

#### Returns

- Typed call return: `InventoryItemBatchUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InventoryItemBatchUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_inventory_items_by_query`

Provenance: Golden OpenAPI contract

Operation ID: `updateInventoryItemsByQuery`

- Sync: `client.inventory.update_inventory_items_by_query(body=..., timeout=None)`
- Async: `await client.inventory.update_inventory_items_by_query(body=..., timeout=None)`
- Raw payload: `client.inventory.update_inventory_items_by_query.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/inventory/items/query/update`
- Source controller: `IncidentIQ API`

Update inventory items by query

Updates multiple inventory catalog items matching a query filter with the same update values.

**Note**: This API is marked as deprecated (v1.0).

**Use Case**: Useful for bulk updates like changing category for all items matching a keyword, or updating cost across multiple items.

**Workflow**:
1. Build a query filter (e.g., by keyword or category)
2. Preview matching items using [POST /api/v1.0/inventory/items/query](#/Inventory/queryInventoryItems)
3. Prepare the update object with new values
4. Submit the query-based update request

**Updatable Fields**: `Name`, `CategoryId`, `Description`, `AverageCost`, `MinQuantityAvailable`, `MaxQuantityAvailable`

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `UpdateInventoryItemsRequest` | `UpdateInventoryItemsRequest` | Query filter and update values to apply to matching items. |

#### Returns

- Typed call return: `InventoryItemBatchUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InventoryItemBatchUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
