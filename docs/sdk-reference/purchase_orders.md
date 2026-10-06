# `purchase_orders` Golden Namespace

Sync client access: `client.purchase_orders`

Async client access: `client.purchase_orders` with `await` on method calls.

These methods are Golden because they come from the bundled Incident IQ OpenAPI contract.

## Aliases

| Alias | Canonical Method | Route |
| --- | --- | --- |
| `create` | `create_purchase_order_inventory` | `POST /api/v1.0/purchase-orders/new` |

## Methods

### `create_purchase_order_inventory`

Provenance: Golden OpenAPI contract

Operation ID: `createPurchaseOrderInventory`

- Sync: `client.purchase_orders.create_purchase_order_inventory(body=..., timeout=None)`
- Async: `await client.purchase_orders.create_purchase_order_inventory(body=..., timeout=None)`
- Raw payload: `client.purchase_orders.create_purchase_order_inventory.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/purchase-orders/new`
- Source controller: `IncidentIQ API`
- Aliases: `create`

Create purchase order

Creates a new purchase order record.

**Note**: This endpoint is part of the Inventory module API which is deprecated (v1.0).

**Workflow**:
1. Create the PO with a number and budget allocation
2. Optionally link to a supplier and funding source
3. Set initial status via `PurchaseOrderStatusTypeId`
4. Add line items via related inventory actions

**Prerequisites**:
- **SupplierId** (optional): Use supplier endpoints to find or create suppliers
- **FundingSourceId** (optional): Use funding source endpoints to get valid IDs

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `PurchaseOrder` | `PurchaseOrder` | Purchase order data to create. |

#### Returns

- Typed call return: `PurchaseOrderItemCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `PurchaseOrderItemCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_purchase_order_by_id_inventory`

Provenance: Golden OpenAPI contract

Operation ID: `getPurchaseOrderByIdInventory`

- Sync: `client.purchase_orders.get_purchase_order_by_id_inventory(purchase_order_id=..., timeout=None)`
- Async: `await client.purchase_orders.get_purchase_order_by_id_inventory(purchase_order_id=..., timeout=None)`
- Raw payload: `client.purchase_orders.get_purchase_order_by_id_inventory.raw(purchase_order_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/purchase-orders/{PurchaseOrderId}`
- Source controller: `IncidentIQ API`

Get purchase order by ID

Retrieves a single purchase order record by its unique identifier.

**Note**: This endpoint is part of the Inventory module API which is deprecated (v1.0).

**Related Endpoints**:
- Use [POST /api/v1.0/purchase-orders/query](#/Inventory/queryPurchaseOrders) to search for purchase orders
- Use [POST /api/v1.0/purchase-orders/{PurchaseOrderId}/update](#/Inventory/updatePurchaseOrderInventory) to modify this PO

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `purchase_order_id` | `PurchaseOrderId` | `path` | `yes` | `str` | `-` | Unique identifier of the purchase order. |

#### Returns

- Typed call return: `PurchaseOrderItemGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `PurchaseOrderItemGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `query_purchase_orders`

Provenance: Golden OpenAPI contract

Operation ID: `queryPurchaseOrders`

- Sync: `client.purchase_orders.query_purchase_orders(body=None, timeout=None)`
- Async: `await client.purchase_orders.query_purchase_orders(body=None, timeout=None)`
- Raw payload: `client.purchase_orders.query_purchase_orders.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/purchase-orders/query`
- Source controller: `IncidentIQ API`

Search purchase orders

Retrieves a paginated list of purchase orders matching the specified filter criteria. Supports custom filtering via the `SupportsCustomFilters` attribute.

**Note**: This endpoint is part of the Inventory module API which is deprecated (v1.0).

**Filterable Fields**:
- `PoNumber` - PO number/reference
- `SupplierId` - Filter by supplier
- `FundingSourceId` - Filter by funding source
- `PurchaseOrderStatusTypeId` - Filter by status
- `IsApproved` / `IsClosed` - Boolean status flags

**Pagination**: Use standard paging parameters (`$p`, `$s`) for large result sets.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `InlineObject` | `InlineObject` | Filter criteria for purchase order query. |

#### Returns

- Typed call return: `PurchaseOrderListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `PurchaseOrderListGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_purchase_order_inventory`

Provenance: Golden OpenAPI contract

Operation ID: `updatePurchaseOrderInventory`

- Sync: `client.purchase_orders.update_purchase_order_inventory(purchase_order_id=..., body=..., timeout=None)`
- Async: `await client.purchase_orders.update_purchase_order_inventory(purchase_order_id=..., body=..., timeout=None)`
- Raw payload: `client.purchase_orders.update_purchase_order_inventory.raw(purchase_order_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/purchase-orders/{PurchaseOrderId}/update`
- Source controller: `IncidentIQ API`

Update purchase order

Updates an existing purchase order record.

**Note**: This endpoint is part of the Inventory module API which is deprecated (v1.0).

**Updatable Fields**:
- `PoNumber` - PO number/reference
- `Budget` - Total budget amount
- `Notes` - Additional notes
- `IsApproved` - Approval status
- `IsClosed` - Closure status
- `SupplierId` - Associated supplier
- `FundingSourceId` - Funding source
- `PurchaseOrderStatusTypeId` - Status type
- `PurchaseOrderTypeId` - Order type

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `purchase_order_id` | `PurchaseOrderId` | `path` | `yes` | `str` | `-` | Unique identifier of the purchase order to update. |
| `body` | `body` | `body` | `yes` | `PurchaseOrder` | `PurchaseOrder` | Updated purchase order data. |

#### Returns

- Typed call return: `PurchaseOrderItemUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `PurchaseOrderItemUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
