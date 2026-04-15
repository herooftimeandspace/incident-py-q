# `purchaseorders` Namespace

Sync client access: `client.purchaseorders`

Async client access: `client.purchaseorders` with `await` on method calls.

## Aliases

| Alias | Canonical Method | Route |
| --- | --- | --- |
| `delete` | `delete_purchase_order` | `DELETE /purchaseorders/{PurchaseOrderId}` |
| `get` | `get_purchase_order` | `GET /purchaseorders/{PurchaseOrderId}` |
| `list` | `get_purchase_orders` | `GET /purchaseorders` |
| `update` | `update_purchase_order` | `POST /purchaseorders/{PurchaseOrderId}` |

## Methods

### `delete_purchase_order`

Operation ID: `Part_DeletePurchaseOrder`

- Sync: `client.purchaseorders.delete_purchase_order(purchase_order_id=..., timeout=None)`
- Async: `await client.purchaseorders.delete_purchase_order(purchase_order_id=..., timeout=None)`
- Raw payload: `client.purchaseorders.delete_purchase_order.raw(purchase_order_id=..., timeout=None)`
- HTTP route: `DELETE /purchaseorders/{PurchaseOrderId}`
- Source controller: `Parts`
- Aliases: `delete`

Delete a Purchase Order

#### Delete a specific purchase order.
#### Sample request:
```
DELETE /api/v1.0/purchaseorders/b199f092-e1a9-418b-8eef-f6e44e273539
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `purchase_order_id` | `PurchaseOrderId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_purchase_order`

Operation ID: `Part_GetPurchaseOrder`

- Sync: `client.purchaseorders.get_purchase_order(purchase_order_id=..., timeout=None)`
- Async: `await client.purchaseorders.get_purchase_order(purchase_order_id=..., timeout=None)`
- Raw payload: `client.purchaseorders.get_purchase_order.raw(purchase_order_id=..., timeout=None)`
- HTTP route: `GET /purchaseorders/{PurchaseOrderId}`
- Source controller: `Parts`
- Aliases: `get`

Get Purchase Order

#### Retrieve a specific purchase order with a specific PurchaseOrderId
#### Sample request:
```
GET /api/v1.0/purchaseorders/b199f092-e1a9-418b-8eef-f6e44e273539
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `purchase_order_id` | `PurchaseOrderId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ItemGetResponseOfPurchaseOrder`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemGetResponseOfPurchaseOrder`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_purchase_orders`

Operation ID: `Part_GetPurchaseOrders`

- Sync: `client.purchaseorders.get_purchase_orders(timeout=None)`
- Async: `await client.purchaseorders.get_purchase_orders(timeout=None)`
- Raw payload: `client.purchaseorders.get_purchase_orders.raw(timeout=None)`
- HTTP route: `GET /purchaseorders`
- Source controller: `Parts`
- Aliases: `list`

Get Purchase Orders

#### Retrieves a list of purchase orders. A specific purchase order can be retrieved via GET `api/v1.0/purchaseorders/{PurchaseOrderId:guid}`.
#### Sample request:
```
GET /api/v1.0/purchaseorders
```

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `ListGetResponseOfPurchaseOrder`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfPurchaseOrder`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_purchase_order`

Operation ID: `Part_UpdatePurchaseOrder`

- Sync: `client.purchaseorders.update_purchase_order(purchase_order_id=..., purchase_order=..., timeout=None)`
- Async: `await client.purchaseorders.update_purchase_order(purchase_order_id=..., purchase_order=..., timeout=None)`
- Raw payload: `client.purchaseorders.update_purchase_order.raw(purchase_order_id=..., purchase_order=..., timeout=None)`
- HTTP route: `POST /purchaseorders/{PurchaseOrderId}`
- Source controller: `Parts`
- Aliases: `update`

No contract summary provided.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `purchase_order_id` | `PurchaseOrderId` | `path` | `yes` | `str` | `-` | - |
| `purchase_order` | `PurchaseOrder` | `body` | `yes` | `PurchaseOrder` | `PurchaseOrder` | - |

#### Returns

- Typed call return: `ItemUpdateResponseOfPurchaseOrder`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemUpdateResponseOfPurchaseOrder`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
