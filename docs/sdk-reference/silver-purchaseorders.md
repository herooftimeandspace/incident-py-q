# `silver.purchaseorders` Namespace

Sync client access: `client.silver.purchaseorders`

Async client access: `client.silver.purchaseorders` with `await` on method calls.

These methods are Silver because the published contract does not document them directly, or because the SDK intentionally wraps a narrower Silver workflow around existing Golden operations. They remain separate so undocumented or convenience behavior never overrides the documented SDK surface.

## Methods

### `delete_purchase_order`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.purchaseorders.delete_purchase_order(purchase_order_id=..., timeout=None)`
- Async: `await client.silver.purchaseorders.delete_purchase_order(purchase_order_id=..., timeout=None)`
- Raw payload: `client.silver.purchaseorders.delete_purchase_order.raw(purchase_order_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/purchaseorders/{purchase_order_id}`
- Observed in: `migrated_from_golden_stoplight`

Delete a Purchase Order

#### Delete a specific purchase order.
#### Sample request:
```
DELETE /api/v1.0/purchaseorders/b199f092-e1a9-418b-8eef-f6e44e273539
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.purchaseorders.delete_purchase_order` (operationId `Part_DeletePurchaseOrder`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `purchase_order_id` | `PurchaseOrderId` | `path` | `yes` | `str` | Path parameter migrated from the previous Golden SDK. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_purchase_order`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.purchaseorders.get_purchase_order(purchase_order_id=..., timeout=None)`
- Async: `await client.silver.purchaseorders.get_purchase_order(purchase_order_id=..., timeout=None)`
- Raw payload: `client.silver.purchaseorders.get_purchase_order.raw(purchase_order_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/purchaseorders/{purchase_order_id}`
- Observed in: `migrated_from_golden_stoplight`

Get Purchase Order

#### Retrieve a specific purchase order with a specific PurchaseOrderId
#### Sample request:
```
GET /api/v1.0/purchaseorders/b199f092-e1a9-418b-8eef-f6e44e273539
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.purchaseorders.get_purchase_order` (operationId `Part_GetPurchaseOrder`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `purchase_order_id` | `PurchaseOrderId` | `path` | `yes` | `str` | Path parameter migrated from the previous Golden SDK. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_purchase_orders`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.purchaseorders.get_purchase_orders(timeout=None)`
- Async: `await client.silver.purchaseorders.get_purchase_orders(timeout=None)`
- Raw payload: `client.silver.purchaseorders.get_purchase_orders.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/purchaseorders`
- Observed in: `migrated_from_golden_stoplight`

Get Purchase Orders

#### Retrieves a list of purchase orders. A specific purchase order can be retrieved via GET `api/v1.0/purchaseorders/{PurchaseOrderId:guid}`.
#### Sample request:
```
GET /api/v1.0/purchaseorders
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.purchaseorders.get_purchase_orders` (operationId `Part_GetPurchaseOrders`).

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `update_purchase_order`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.purchaseorders.update_purchase_order(purchase_order_id=..., json_body=..., timeout=None)`
- Async: `await client.silver.purchaseorders.update_purchase_order(purchase_order_id=..., json_body=..., timeout=None)`
- Raw payload: `client.silver.purchaseorders.update_purchase_order.raw(purchase_order_id=..., json_body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/purchaseorders/{purchase_order_id}`
- Observed in: `migrated_from_golden_stoplight`

Migrated Silver route for POST /purchaseorders/{PurchaseOrderId}.

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.purchaseorders.update_purchase_order` (operationId `Part_UpdatePurchaseOrder`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `purchase_order_id` | `PurchaseOrderId` | `path` | `yes` | `str` | Path parameter migrated from the previous Golden SDK. |
| `json_body` | `PurchaseOrder` | `body` | `yes` | `dict[str, Any] | list[Any]` | Body parameter migrated from the previous Golden SDK. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---
