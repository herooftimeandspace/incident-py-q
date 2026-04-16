# `custom_fields` Namespace

Sync client access: `client.custom_fields`

Async client access: `client.custom_fields` with `await` on method calls.

## Aliases

| Alias | Canonical Method | Route |
| --- | --- | --- |
| `delete` | `delete_custom_field` | `DELETE /custom-fields/{CustomFieldId}` |
| `get` | `get_custom_field` | `GET /custom-fields/{CustomFieldId}` |
| `list` | `get_custom_fields` | `GET /custom-fields` |
| `create` | `get_custom_fields2` | `POST /custom-fields` |
| `update` | `update_custom_field` | `POST /custom-fields/{CustomFieldId}` |

## Methods

### `delete_custom_field`

Operation ID: `CustomField_DeleteCustomField`

- Sync: `client.custom_fields.delete_custom_field(custom_field_id=..., timeout=None)`
- Async: `await client.custom_fields.delete_custom_field(custom_field_id=..., timeout=None)`
- Raw payload: `client.custom_fields.delete_custom_field.raw(custom_field_id=..., timeout=None)`
- HTTP route: `DELETE /custom-fields/{CustomFieldId}`
- Source controller: `Custom Fields`
- Aliases: `delete`

Delete Custom Field 

#### Delete a Custom Field
#### Sample request:
```
DELETE /api/v1.0/custom-fields/f10f540f-2a9f-47fe-acbd-8ca82dc73e7c
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `custom_field_id` | `CustomFieldId` | `path` | `yes` | `str` | `-` | Custom Field ID to be deleted |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_custom_field_type`

Operation ID: `CustomField_DeleteCustomFieldType`

- Sync: `client.custom_fields.delete_custom_field_type(custom_field_type_id=..., timeout=None)`
- Async: `await client.custom_fields.delete_custom_field_type(custom_field_type_id=..., timeout=None)`
- Raw payload: `client.custom_fields.delete_custom_field_type.raw(custom_field_type_id=..., timeout=None)`
- HTTP route: `DELETE /custom-fields/types/{CustomFieldTypeId}`
- Source controller: `Custom Fields`

Delete Custom Field Type

#### Delete a Custom Field Type
#### Sample request:
```
DELETE /api/v1.0/custom-fields/types/108d5344-012f-4380-b865-3eaa72f7c42f
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `custom_field_type_id` | `CustomFieldTypeId` | `path` | `yes` | `str` | `-` | Custom Field Type ID to be deleted |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_custom_fields`

Operation ID: `CustomField_DeleteCustomFields`

- Sync: `client.custom_fields.delete_custom_fields(custom_field_ids=..., timeout=None)`
- Async: `await client.custom_fields.delete_custom_fields(custom_field_ids=..., timeout=None)`
- Raw payload: `client.custom_fields.delete_custom_fields.raw(custom_field_ids=..., timeout=None)`
- HTTP route: `DELETE /custom-fields`
- Source controller: `Custom Fields`

No contract summary provided.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `custom_field_ids` | `CustomFieldIds` | `body` | `yes` | `list[Any]` | `-` | - |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_custom_field`

Operation ID: `CustomField_GetCustomField`

- Sync: `client.custom_fields.get_custom_field(custom_field_id=..., timeout=None)`
- Async: `await client.custom_fields.get_custom_field(custom_field_id=..., timeout=None)`
- Raw payload: `client.custom_fields.get_custom_field.raw(custom_field_id=..., timeout=None)`
- HTTP route: `GET /custom-fields/{CustomFieldId}`
- Source controller: `Custom Fields`
- Aliases: `get`

Get Custom Field 

#### Retrieve a specific Custom Field
#### Sample request:
```
GET /api/v1.0/custom-fields/e60c4fe8-2236-48bb-8dd0-18a6f5b4c7ae
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `custom_field_id` | `CustomFieldId` | `path` | `yes` | `str` | `-` | Custom Field ID to be retrieved |

#### Returns

- Typed call return: `ItemGetResponseOfCustomField`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemGetResponseOfCustomField`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_custom_field_type`

Operation ID: `CustomField_GetCustomFieldType`

- Sync: `client.custom_fields.get_custom_field_type(custom_field_type_id=..., timeout=None)`
- Async: `await client.custom_fields.get_custom_field_type(custom_field_type_id=..., timeout=None)`
- Raw payload: `client.custom_fields.get_custom_field_type.raw(custom_field_type_id=..., timeout=None)`
- HTTP route: `GET /custom-fields/types/{CustomFieldTypeId}`
- Source controller: `Custom Fields`

Get Custom Field Type

#### Retrieve a specific Custom Field Type
#### Sample request:
```
GET /api/v1.0/custom-fields/types/108d5344-012f-4380-b865-3eaa72f7c42f
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `custom_field_type_id` | `CustomFieldTypeId` | `path` | `yes` | `str` | `-` | Custom Field Type ID to be deleted |

#### Returns

- Typed call return: `ItemGetResponseOfCustomFieldType`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemGetResponseOfCustomFieldType`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_custom_field_types`

Operation ID: `CustomField_GetCustomFieldTypes`

- Sync: `client.custom_fields.get_custom_field_types(timeout=None)`
- Async: `await client.custom_fields.get_custom_field_types(timeout=None)`
- Raw payload: `client.custom_fields.get_custom_field_types.raw(timeout=None)`
- HTTP route: `GET /custom-fields/types`
- Source controller: `Custom Fields`

Get Custom Field Types

#### Retrieves a list of CustomFieldTypes that can then be used to retrieve the custom field type via _custom-fields/types/{CustomFieldTypeId:guid}_
#### Sample request:
```
GET /api/v1.0/custom-fields/types
```

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `ListGetResponseOfCustomFieldType`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfCustomFieldType`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_custom_field_types2`

Operation ID: `CustomField_GetCustomFieldTypes2`

- Sync: `client.custom_fields.get_custom_field_types2(custom_field_types_request=..., timeout=None)`
- Async: `await client.custom_fields.get_custom_field_types2(custom_field_types_request=..., timeout=None)`
- Raw payload: `client.custom_fields.get_custom_field_types2.raw(custom_field_types_request=..., timeout=None)`
- HTTP route: `POST /custom-fields/types`
- Source controller: `Custom Fields`

No contract summary provided.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `custom_field_types_request` | `CustomFieldTypesRequest` | `body` | `yes` | `GetCustomFieldTypesRequest` | `GetCustomFieldTypesRequest` | - |

#### Returns

- Typed call return: `ListGetResponseOfCustomFieldType`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfCustomFieldType`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_custom_field_values_for_asset`

Operation ID: `CustomField_GetCustomFieldValuesForAsset`

- Sync: `client.custom_fields.get_custom_field_values_for_asset(asset_id=..., timeout=None)`
- Async: `await client.custom_fields.get_custom_field_values_for_asset(asset_id=..., timeout=None)`
- Raw payload: `client.custom_fields.get_custom_field_values_for_asset.raw(asset_id=..., timeout=None)`
- HTTP route: `GET /custom-fields/values/for/asset/{AssetId}`
- Source controller: `Custom Fields`

Retrieve for Asset 

#### Retrieve Custom Fields for a specific Asset
#### Sample request:
```
GET /api/v1.0/custom-fields/values/for/asset/4c35d2ef-2bb1-457f-b123-dea74ee826ba
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `asset_id` | `AssetId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ListGetResponseOfAssetCustomFieldValue`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfAssetCustomFieldValue`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_custom_field_values_for_ticket`

Operation ID: `CustomField_GetCustomFieldValuesForTicket`

- Sync: `client.custom_fields.get_custom_field_values_for_ticket(ticket_id=..., timeout=None)`
- Async: `await client.custom_fields.get_custom_field_values_for_ticket(ticket_id=..., timeout=None)`
- Raw payload: `client.custom_fields.get_custom_field_values_for_ticket.raw(ticket_id=..., timeout=None)`
- HTTP route: `GET /custom-fields/values/for/ticket/{TicketId}`
- Source controller: `Custom Fields`

Retrieve for Ticket 

#### Retrieve Custom Fields for a specific Ticket
#### Sample request:
```
GET /api/v1.0/custom-fields/values/for/ticket/9933a6e3-d98b-4c5c-be04-043cf23e838e
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `TicketId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ListGetResponseOfTicketCustomFieldValue`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfTicketCustomFieldValue`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_custom_field_values_for_user`

Operation ID: `CustomField_GetCustomFieldValuesForUser`

- Sync: `client.custom_fields.get_custom_field_values_for_user(user_id=..., timeout=None)`
- Async: `await client.custom_fields.get_custom_field_values_for_user(user_id=..., timeout=None)`
- Raw payload: `client.custom_fields.get_custom_field_values_for_user.raw(user_id=..., timeout=None)`
- HTTP route: `GET /custom-fields/values/for/user/{UserId}`
- Source controller: `Custom Fields`

Retrieve for User 

#### Retrieve Custom Fields for a specific User
#### Sample request:
```
GET /api/v1.0/custom-fields/values/for/user/634d18fb-6c6e-44e6-a993-8444466910e2
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ListGetResponseOfUserCustomFieldValue`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfUserCustomFieldValue`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_custom_fields`

Operation ID: `CustomField_GetCustomFields`

- Sync: `client.custom_fields.get_custom_fields(product_filter_type=None, timeout=None)`
- Async: `await client.custom_fields.get_custom_fields(product_filter_type=None, timeout=None)`
- Raw payload: `client.custom_fields.get_custom_fields.raw(product_filter_type=None, timeout=None)`
- HTTP route: `GET /custom-fields`
- Source controller: `Custom Fields`
- Aliases: `list`

No contract summary provided.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `product_filter_type` | `ProductFilterType` | `query` | `no` | `Any` | `-` | - |

#### Returns

- Typed call return: `ListGetResponseOfCustomField`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfCustomField`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_custom_fields2`

Operation ID: `CustomField_GetCustomFields2`

- Sync: `client.custom_fields.get_custom_fields2(custom_fields_request=..., timeout=None)`
- Async: `await client.custom_fields.get_custom_fields2(custom_fields_request=..., timeout=None)`
- Raw payload: `client.custom_fields.get_custom_fields2.raw(custom_fields_request=..., timeout=None)`
- HTTP route: `POST /custom-fields`
- Source controller: `Custom Fields`
- Aliases: `create`

Get Custom Fields

#### Retrieves a list of custom fields that can then be used to retrieve a specific custom field via _Get Custom Field_
#### Sample request:
```
POST /api/v1.0/custom-fields
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `custom_fields_request` | `CustomFieldsRequest` | `body` | `yes` | `GetCustomFieldsRequest` | `GetCustomFieldsRequest` | - |

#### Returns

- Typed call return: `ListGetResponseOfCustomField`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfCustomField`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_custom_field`

Operation ID: `CustomField_UpdateCustomField`

- Sync: `client.custom_fields.update_custom_field(custom_field_id=..., custom_field=..., timeout=None)`
- Async: `await client.custom_fields.update_custom_field(custom_field_id=..., custom_field=..., timeout=None)`
- Raw payload: `client.custom_fields.update_custom_field.raw(custom_field_id=..., custom_field=..., timeout=None)`
- HTTP route: `POST /custom-fields/{CustomFieldId}`
- Source controller: `Custom Fields`
- Aliases: `update`

No contract summary provided.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `custom_field_id` | `CustomFieldId` | `path` | `yes` | `str` | `-` | - |
| `custom_field` | `CustomField` | `body` | `yes` | `CustomField` | `CustomField` | - |

#### Returns

- Typed call return: `ItemUpdateResponseOfCustomField`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemUpdateResponseOfCustomField`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_custom_field_type`

Operation ID: `CustomField_UpdateCustomFieldType`

- Sync: `client.custom_fields.update_custom_field_type(custom_field_type_id=..., custom_field_type=..., timeout=None)`
- Async: `await client.custom_fields.update_custom_field_type(custom_field_type_id=..., custom_field_type=..., timeout=None)`
- Raw payload: `client.custom_fields.update_custom_field_type.raw(custom_field_type_id=..., custom_field_type=..., timeout=None)`
- HTTP route: `POST /custom-fields/types/{CustomFieldTypeId}`
- Source controller: `Custom Fields`

No contract summary provided.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `custom_field_type_id` | `CustomFieldTypeId` | `path` | `yes` | `str` | `-` | - |
| `custom_field_type` | `CustomFieldType` | `body` | `yes` | `CustomFieldType` | `CustomFieldType` | - |

#### Returns

- Typed call return: `ItemUpdateResponseOfCustomFieldType`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemUpdateResponseOfCustomFieldType`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
