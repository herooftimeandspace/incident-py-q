# `labor` Golden Namespace

Sync client access: `client.labor`

Async client access: `client.labor` with `await` on method calls.

These methods are Golden because they come from the bundled Incident IQ OpenAPI contract.

## Methods

### `create_labor_rate`

Provenance: Golden OpenAPI contract

Operation ID: `createLaborRate`

- Sync: `client.labor.create_labor_rate(body=..., timeout=None)`
- Async: `await client.labor.create_labor_rate(body=..., timeout=None)`
- Raw payload: `client.labor.create_labor_rate.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/labor/rates/new`
- Source controller: `IncidentIQ API`

Create a new labor rate

Creates a new labor rate record for a user, specifying the hourly billing rate and labor type category. The created rate is returned with its server-generated UserLaborRateId.

**Prerequisites**
1. **UserId** — Obtain via [POST /api/v1.0/users](#/Users/searchUsers). Extract `Items[].UserId` from the response.
2. **LaborTypeId** — Obtain from an existing user's labor rates via [GET /api/v1.0/labor/rates/user/{UserId}](#/Labor Rates/getUserLaborRates).

**Workflow Example**
1. Search for the target user: [POST /api/v1.0/users](#/Users/searchUsers).
2. Extract `UserId` from the response.
3. Create the labor rate: `POST /api/v1.0/labor/rates/new` with `UserId`, `HourlyRate`, and `LaborTypeId`.
4. Extract `Item.UserLaborRateId` from the response for future updates.

**Minimal Required Fields**: `UserId`, `HourlyRate`, `LaborTypeId` in the request body.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `UpdateLaborRateRequest` | `UpdateLaborRateRequest` | Labor rate creation payload with user, rate, and labor type information. |

#### Returns

- Typed call return: `ItemCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_labor_type`

Provenance: Golden OpenAPI contract

Operation ID: `createLaborType`

- Sync: `client.labor.create_labor_type(body=..., timeout=None)`
- Async: `await client.labor.create_labor_type(body=..., timeout=None)`
- Raw payload: `client.labor.create_labor_type.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/labor/types/new`
- Source controller: `IncidentIQ API`

Create Labor Type

Creates a new labor type for categorizing time entries on work orders. Labor types define whether hours are standard or overtime, specify a multiplier for overtime calculation, and can be scoped globally or per-site.

**Prerequisites**
1. **SiteId** (optional) - Use [GET /api/v1.0/sites](#/Sites/listSites) to obtain a SiteId when creating a site-scoped labor type.
2. **ProductId** (optional) - Use [GET /api/v1.0/products/all](#/Products/listProducts) to obtain a ProductId.

**Workflow Example**
1. (Optional) Review existing types: [GET /api/v1.0/labor/types](#/Labor Types/listLaborTypes) to avoid duplicates.
2. Build request with Name, overtime settings, and scope.
3. Submit: [POST /api/v1.0/labor/types/new](#/Labor Types/createLaborType).
4. Extract `Item.LaborTypeId` from the response for future reference.

**Minimal Required Fields**: `Name`

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `UpdateLaborTypeRequest` | `UpdateLaborTypeRequest` | - |

#### Returns

- Typed call return: `ItemCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_labor_rate`

Provenance: Golden OpenAPI contract

Operation ID: `deleteLaborRate`

- Sync: `client.labor.delete_labor_rate(user_labor_rate_id=..., timeout=None)`
- Async: `await client.labor.delete_labor_rate(user_labor_rate_id=..., timeout=None)`
- Raw payload: `client.labor.delete_labor_rate.raw(user_labor_rate_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/labor/rates/{UserLaborRateId}`
- Source controller: `IncidentIQ API`

Delete a labor rate

Deletes a labor rate record identified by its UserLaborRateId. This performs a soft-delete, marking the record as deleted without permanently removing it from the system.

**Prerequisites**
1. **UserLaborRateId** — Obtain via [POST /api/v1.0/labor/rates/new](#/Labor Rates/createLaborRate) at `Item.UserLaborRateId`, or from [GET /api/v1.0/labor/rates/user/{UserId}](#/Labor Rates/getUserLaborRates) at `Items[].UserLaborRateId`.

**Workflow Example**
1. List labor rates for a user: [GET /api/v1.0/labor/rates/user/{UserId}](#/Labor Rates/getUserLaborRates).
2. Extract `UserLaborRateId` from the rate to delete.
3. Delete the rate: `DELETE /api/v1.0/labor/rates/{UserLaborRateId}`.

**Minimal Required Fields**: `UserLaborRateId` path parameter.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_labor_rate_id` | `UserLaborRateId` | `path` | `yes` | `str` | `-` | Unique identifier of the labor rate to delete. |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_labor_type`

Provenance: Golden OpenAPI contract

Operation ID: `deleteLaborType`

- Sync: `client.labor.delete_labor_type(labor_type_id=..., timeout=None)`
- Async: `await client.labor.delete_labor_type(labor_type_id=..., timeout=None)`
- Raw payload: `client.labor.delete_labor_type.raw(labor_type_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/labor/types/{LaborTypeId}`
- Source controller: `IncidentIQ API`

Delete Labor Type

Permanently deletes a labor type identified by LaborTypeId. Once deleted, the labor type can no longer be assigned to new labor entries. Existing labor entries that reference this type are not affected.

**Prerequisites**
1. **LaborTypeId** - Use [GET /api/v1.0/labor/types](#/Labor Types/listLaborTypes) to obtain the LaborTypeId from `Items[].LaborTypeId`.

**Workflow Example**
1. List labor types: [GET /api/v1.0/labor/types](#/Labor Types/listLaborTypes).
2. Identify the labor type to remove from `Items[].LaborTypeId`.
3. Delete: [DELETE /api/v1.0/labor/types/{LaborTypeId}](#/Labor Types/deleteLaborType).

**Caution**: This operation is irreversible. Verify the LaborTypeId before submitting.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `labor_type_id` | `LaborTypeId` | `path` | `yes` | `str` | `-` | The unique identifier of the labor type to delete. |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_labor_activity_by_tickets`

Provenance: Golden OpenAPI contract

Operation ID: `getLaborActivityByTickets`

- Sync: `client.labor.get_labor_activity_by_tickets(body=..., timeout=None)`
- Async: `await client.labor.get_labor_activity_by_tickets(body=..., timeout=None)`
- Raw payload: `client.labor.get_labor_activity_by_tickets.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/labor/rates/tickets`
- Source controller: `IncidentIQ API`

Get labor rate activity by ticket IDs

Retrieves labor rate activity records for a list of tickets. Accepts an array of ticket GUIDs and returns LaborRateActivity records showing labor effort and cost breakdowns per user and labor type. Supports server-side paging and filtering via query parameters.

**Prerequisites**
1. **TicketIds** — Obtain via [POST /api/v1.0/tickets](#/Tickets/searchTickets). Extract `Items[].TicketId` from the response.

**Workflow Example**
1. Search for target tickets: [POST /api/v1.0/tickets](#/Tickets/searchTickets).
2. Collect `TicketId` values from the response.
3. Retrieve labor activity: `POST /api/v1.0/labor/rates/tickets` with the array of TicketIds.

**Minimal Required Fields**: Array of ticket UUID strings in the request body.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | Array of ticket identifiers to retrieve labor activity for. |

#### Returns

- Typed call return: `InlineObject`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InlineObject`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_labor_activity_by_tickets_grouped_by_user`

Provenance: Golden OpenAPI contract

Operation ID: `getLaborActivityByTicketsGroupedByUser`

- Sync: `client.labor.get_labor_activity_by_tickets_grouped_by_user(body=..., timeout=None)`
- Async: `await client.labor.get_labor_activity_by_tickets_grouped_by_user(body=..., timeout=None)`
- Raw payload: `client.labor.get_labor_activity_by_tickets_grouped_by_user.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/labor/rates-by-user/tickets`
- Source controller: `IncidentIQ API`

Get labor rate activity by ticket IDs grouped by user

Retrieves labor rate activity records for a list of tickets, grouped by user. Accepts an array of ticket GUIDs and returns LaborRateActivity records organized per user showing their individual labor effort and cost contributions. Supports server-side paging and filtering via query parameters.

**Prerequisites**
1. **TicketIds** — Obtain via [POST /api/v1.0/tickets](#/Tickets/searchTickets). Extract `Items[].TicketId` from the response.

**Workflow Example**
1. Search for target tickets: [POST /api/v1.0/tickets](#/Tickets/searchTickets).
2. Collect `TicketId` values from the response.
3. Retrieve labor activity grouped by user: `POST /api/v1.0/labor/rates-by-user/tickets` with the array of TicketIds.

**Minimal Required Fields**: Array of ticket UUID strings in the request body.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | Array of ticket identifiers to retrieve user-grouped labor activity for. |

#### Returns

- Typed call return: `ListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_labor_rate`

Provenance: Golden OpenAPI contract

Operation ID: `getLaborRate`

- Sync: `client.labor.get_labor_rate(user_labor_rate_id=..., timeout=None)`
- Async: `await client.labor.get_labor_rate(user_labor_rate_id=..., timeout=None)`
- Raw payload: `client.labor.get_labor_rate.raw(user_labor_rate_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/labor/rates/{UserLaborRateId}`
- Source controller: `IncidentIQ API`

Get a labor rate by ID

Retrieves a single labor rate record by its unique UserLaborRateId. Returns the full labor rate object including user, hourly rate, labor type, and timestamp information.

**Prerequisites**
1. **UserLaborRateId** — Obtain via [POST /api/v1.0/labor/rates/new](#/Labor Rates/createLaborRate) at `Item.UserLaborRateId`, or from [GET /api/v1.0/labor/rates/user/{UserId}](#/Labor Rates/getUserLaborRates) at `Items[].UserLaborRateId`.

**Workflow Example**
1. List labor rates for a user: [GET /api/v1.0/labor/rates/user/{UserId}](#/Labor Rates/getUserLaborRates).
2. Extract `UserLaborRateId` from the desired rate.
3. Retrieve full details: `GET /api/v1.0/labor/rates/{UserLaborRateId}`.

**Minimal Required Fields**: `UserLaborRateId` path parameter.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_labor_rate_id` | `UserLaborRateId` | `path` | `yes` | `str` | `-` | Unique identifier of the labor rate to retrieve. |

#### Returns

- Typed call return: `InlineObject`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `InlineObject`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_labor_type`

Provenance: Golden OpenAPI contract

Operation ID: `getLaborType`

- Sync: `client.labor.get_labor_type(labor_type_id=..., timeout=None)`
- Async: `await client.labor.get_labor_type(labor_type_id=..., timeout=None)`
- Raw payload: `client.labor.get_labor_type.raw(labor_type_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/labor/types/{LaborTypeId}`
- Source controller: `IncidentIQ API`

Get Labor Type by ID

Retrieves a single labor type by its unique identifier. Returns the full labor type configuration including name, overtime settings, multiplier, icon, and scope information.

**Prerequisites**
1. **LaborTypeId** - Use [GET /api/v1.0/labor/types](#/Labor Types/listLaborTypes) or [POST /api/v1.0/labor/types](#/Labor Types/queryLaborTypes) to obtain the LaborTypeId from `Items[].LaborTypeId`.

**Workflow Example**
1. List labor types: [GET /api/v1.0/labor/types](#/Labor Types/listLaborTypes).
2. Extract the desired `LaborTypeId` from `Items[].LaborTypeId`.
3. Fetch details: [GET /api/v1.0/labor/types/{LaborTypeId}](#/Labor Types/getLaborType).

**Response Envelope**: Returns `ItemGetResponse` with the LaborType object in the `Item` property.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `labor_type_id` | `LaborTypeId` | `path` | `yes` | `str` | `-` | The unique identifier of the labor type to retrieve. |

#### Returns

- Typed call return: `ItemGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_user_labor_rates`

Provenance: Golden OpenAPI contract

Operation ID: `getUserLaborRates`

- Sync: `client.labor.get_user_labor_rates(user_id=..., timeout=None)`
- Async: `await client.labor.get_user_labor_rates(user_id=..., timeout=None)`
- Raw payload: `client.labor.get_user_labor_rates.raw(user_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/labor/rates/user/{UserId}`
- Source controller: `IncidentIQ API`

Get labor rates for a user

Retrieves all labor rate records for a specific user. Returns a list of LaborRate objects showing the user's configured hourly rates and labor type assignments. Supports optional route parameters for product filtering and permission checks.

**Prerequisites**
1. **UserId** — Obtain via [POST /api/v1.0/users](#/Users/searchUsers). Extract `Items[].UserId` from the response.

**Workflow Example**
1. Search for the target user: [POST /api/v1.0/users](#/Users/searchUsers).
2. Extract `UserId` from the response.
3. Retrieve labor rates: `GET /api/v1.0/labor/rates/user/{UserId}`.

**Minimal Required Fields**: `UserId` path parameter.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | Unique identifier of the user whose labor rates to retrieve. |

#### Returns

- Typed call return: `ListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_users_labor_ticket_activity_actions`

Provenance: Golden OpenAPI contract

Operation ID: `getUsersLaborTicketActivityActions`

- Sync: `client.labor.get_users_labor_ticket_activity_actions(body=..., timeout=None)`
- Async: `await client.labor.get_users_labor_ticket_activity_actions(body=..., timeout=None)`
- Raw payload: `client.labor.get_users_labor_ticket_activity_actions.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/labor/rates`
- Source controller: `IncidentIQ API`

Get labor ticket activity actions by user IDs

Retrieves labor-related ticket activity actions for a list of users. Accepts an array of user GUIDs and returns TicketActivityAction records representing labor entries logged against tickets. Supports server-side paging and filtering via query parameters.

**Prerequisites**
1. **UserIds** — Obtain via [POST /api/v1.0/users](#/Users/searchUsers). Extract `Items[].UserId` from the response.

**Workflow Example**
1. Search for target users: [POST /api/v1.0/users](#/Users/searchUsers).
2. Collect `UserId` values from the response.
3. Retrieve labor activity actions: `POST /api/v1.0/labor/rates` with the array of UserIds.

**Minimal Required Fields**: Array of user UUID strings in the request body.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | Array of user identifiers to retrieve labor activity actions for. |

#### Returns

- Typed call return: `ListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_labor_types`

Provenance: Golden OpenAPI contract

Operation ID: `listLaborTypes`

- Sync: `client.labor.list_labor_types(product_id=None, timeout=None)`
- Async: `await client.labor.list_labor_types(product_id=None, timeout=None)`
- Raw payload: `client.labor.list_labor_types.raw(product_id=None, timeout=None)`
- HTTP route: `GET /api/v1.0/labor/types`
- Source controller: `IncidentIQ API`

List Labor Types

Retrieves a paginated list of labor types configured in the system. Labor types categorize time entries for work-order labor tracking (e.g., Standard, Overtime, Emergency). Results can be filtered by ProductId to return only labor types associated with a specific product module.

**Prerequisites**
- None required for basic listing.
- **ProductId** (optional) - Use [GET /api/v1.0/products/all](#/Products/listProducts) to obtain a ProductId for filtering.

**Workflow Example**
1. Call [GET /api/v1.0/labor/types](#/Labor Types/listLaborTypes) with optional query parameters.
2. Extract `Items[].LaborTypeId` from the response for use with update or delete operations.

**Response Envelope**: Returns `ListGetResponse` with `Items` array of LaborType objects, plus pagination metadata.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `product_id` | `ProductId` | `query` | `no` | `str` | `-` | Filter labor types by product module identifier. Obtain from [GET /api/v1.0/sites/my/settings](#/Sites/getMySiteSettings) via `Item.Products[].ProductId`. |

#### Returns

- Typed call return: `ListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `query_labor_types`

Provenance: Golden OpenAPI contract

Operation ID: `queryLaborTypes`

- Sync: `client.labor.query_labor_types(body=None, timeout=None)`
- Async: `await client.labor.query_labor_types(body=None, timeout=None)`
- Raw payload: `client.labor.query_labor_types.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/labor/types`
- Source controller: `IncidentIQ API`

Query Labor Types

Retrieves a paginated list of labor types using a POST request body for advanced filtering and pagination options. This endpoint supports custom filters and is functionally equivalent to [GET /api/v1.0/labor/types](#/Labor Types/listLaborTypes) but accepts the query parameters in the request body instead of the URL.

**Prerequisites**
- None required for basic querying.
- **ProductId** (optional) - Use [GET /api/v1.0/products/all](#/Products/listProducts) to obtain a ProductId for filtering.

**Workflow Example**
1. Build a `GetLaborTypesRequest` with optional ProductId filter and pagination settings.
2. Submit via [POST /api/v1.0/labor/types](#/Labor Types/queryLaborTypes).
3. Extract `Items[].LaborTypeId` from the response.

**Minimal Required Fields**: None (all fields are optional).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `GetLaborTypesRequest` | `GetLaborTypesRequest` | - |

#### Returns

- Typed call return: `ListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_labor_rate`

Provenance: Golden OpenAPI contract

Operation ID: `updateLaborRate`

- Sync: `client.labor.update_labor_rate(user_labor_rate_id=..., body=..., timeout=None)`
- Async: `await client.labor.update_labor_rate(user_labor_rate_id=..., body=..., timeout=None)`
- Raw payload: `client.labor.update_labor_rate.raw(user_labor_rate_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/labor/rates/{UserLaborRateId}`
- Source controller: `IncidentIQ API`

Update an existing labor rate

Updates an existing labor rate record identified by its UserLaborRateId. Submit the labor rate object with the fields to change. The updated rate is returned in the response.

**Prerequisites**
1. **UserLaborRateId** — Obtain via [POST /api/v1.0/labor/rates/new](#/Labor Rates/createLaborRate) at `Item.UserLaborRateId`, or from [GET /api/v1.0/labor/rates/user/{UserId}](#/Labor Rates/getUserLaborRates) at `Items[].UserLaborRateId`.

**Workflow Example**
1. List labor rates for a user: [GET /api/v1.0/labor/rates/user/{UserId}](#/Labor Rates/getUserLaborRates).
2. Extract `UserLaborRateId` from the rate to update.
3. Submit changes: `POST /api/v1.0/labor/rates/{UserLaborRateId}`.
4. Verify: [GET /api/v1.0/labor/rates/{UserLaborRateId}](#/Labor Rates/getLaborRate).

**Minimal Required Fields**: `UserLaborRateId` path parameter plus the fields to update in the request body.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_labor_rate_id` | `UserLaborRateId` | `path` | `yes` | `str` | `-` | Unique identifier of the labor rate to update. |
| `body` | `body` | `body` | `yes` | `UpdateLaborRateRequest` | `UpdateLaborRateRequest` | Updated labor rate payload. |

#### Returns

- Typed call return: `ItemUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_labor_type`

Provenance: Golden OpenAPI contract

Operation ID: `updateLaborType`

- Sync: `client.labor.update_labor_type(labor_type_id=..., body=..., timeout=None)`
- Async: `await client.labor.update_labor_type(labor_type_id=..., body=..., timeout=None)`
- Raw payload: `client.labor.update_labor_type.raw(labor_type_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/labor/types/{LaborTypeId}`
- Source controller: `IncidentIQ API`

Update Labor Type

Updates an existing labor type identified by LaborTypeId. Allows modifying the labor type name, overtime flag, overtime multiplier, icon, and scope settings.

**Prerequisites**
1. **LaborTypeId** - Use [GET /api/v1.0/labor/types](#/Labor Types/listLaborTypes) to obtain the LaborTypeId from `Items[].LaborTypeId`.
2. **SiteId** (optional) - Use [GET /api/v1.0/sites](#/Sites/listSites) to obtain a SiteId when setting site-level scope.
3. **ProductId** (optional) - Use [GET /api/v1.0/products/all](#/Products/listProducts) to obtain a ProductId.

**Workflow Example**
1. Get the current labor type: [GET /api/v1.0/labor/types/{LaborTypeId}](#/Labor Types/getLaborType).
2. Modify the desired fields in the request body.
3. Submit: [POST /api/v1.0/labor/types/{LaborTypeId}](#/Labor Types/updateLaborType).

**Minimal Required Fields**: `Name`

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `labor_type_id` | `LaborTypeId` | `path` | `yes` | `str` | `-` | The unique identifier of the labor type to update. |
| `body` | `body` | `body` | `yes` | `UpdateLaborTypeRequest` | `UpdateLaborTypeRequest` | - |

#### Returns

- Typed call return: `ItemUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
