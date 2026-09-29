# `views` Golden Namespace

Sync client access: `client.views`

Async client access: `client.views` with `await` on method calls.

These methods are Golden because they come from the bundled Incident IQ OpenAPI contract.

## Methods

### `create_view`

Provenance: Golden OpenAPI contract

Operation ID: `createView`

- Sync: `client.views.create_view(body=..., timeout=None)`
- Async: `await client.views.create_view(body=..., timeout=None)`
- Raw payload: `client.views.create_view.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/views/new`
- Source controller: `IncidentIQ API`

Create view

Creates a new saved view definition for any supported view type when using the generic views endpoint. Use this for programmatic creation across tickets, assets, users, or site contexts.

**Prerequisites**
1. **SiteId/ProductId** - Use [GET /api/v1.0/sites/{siteUrl}](#/Sites/getSiteByUrl) to obtain `Item.SiteId` and a `ProductId` from `Item.LicensedProducts[]`.
2. **UserId** - Use [POST /api/v1.0/search](#/Users/searchUsers) to identify the owner and extract `Item.Users[].UserId`.
3. **ViewTypeId** - Copy a valid type from [GET /api/v1.0/tickets/views](#/Tickets/listTicketViews), [GET /api/v1.0/assets/views](#/Assets/listAssetViews), [GET /api/v1.0/users/views](#/Users/listUserViews), or [GET /api/v1.0/views/for-sites](#/Views/listSiteViews).

**Workflow Example**
1. Bootstrap site context: [GET /api/v1.0/sites/{siteUrl}](#/Sites/getSiteByUrl) -> capture SiteId and ProductId.
2. Inspect existing views to choose a ViewTypeId.
3. [POST /api/v1.0/views/new](#/Views/createView) with a ViewDefinition payload.

**Minimal Required Fields**: `ViewId`, `IsDeleted`, `SiteId`, `ProductId`, `UserId`, `Name`, `ViewTypeId`, `PageSize`.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `ViewDefinition` | `ViewDefinition` | - |

#### Returns

- Typed call return: `ViewItemCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ViewItemCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_view_team`

Provenance: Golden OpenAPI contract

Operation ID: `createViewTeam`

- Sync: `client.views.create_view_team(body=..., timeout=None)`
- Async: `await client.views.create_view_team(body=..., timeout=None)`
- Raw payload: `client.views.create_view_team.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/views/teams/new`
- Source controller: `IncidentIQ API`

Create view team share

Creates a team share assignment for a view so every member of the team can access it.

**Prerequisites**
1. **viewId** - Obtain from [GET /api/v1.0/tickets/views](#/Tickets/listTicketViews), [GET /api/v1.0/assets/views](#/Assets/listAssetViews), [GET /api/v1.0/users/views](#/Users/listUserViews), or [GET /api/v1.0/views/for-sites](#/Views/listSiteViews).
2. **TeamId** - Use [GET /api/v1.0/teams](#/Teams/listTeams) to select the recipient team.

**Workflow Example**
1. Choose a view to share and copy its ViewId.
2. Select the team to receive access.
3. [POST /api/v1.0/views/teams/new](#/Views/createViewTeam) with ViewId, TeamId, and Access.

**Minimal Required Fields**: `ViewId`, `TeamId`, `Access`.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `ViewShare` | `ViewShare` | - |

#### Returns

- Typed call return: `ViewShareItemCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ViewShareItemCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_view_user`

Provenance: Golden OpenAPI contract

Operation ID: `createViewUser`

- Sync: `client.views.create_view_user(body=..., timeout=None)`
- Async: `await client.views.create_view_user(body=..., timeout=None)`
- Raw payload: `client.views.create_view_user.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/views/users/new`
- Source controller: `IncidentIQ API`

Create view user share

Creates a user share assignment for a view so a specific user can access it.

**Prerequisites**
1. **viewId** - Obtain from [GET /api/v1.0/tickets/views](#/Tickets/listTicketViews), [GET /api/v1.0/assets/views](#/Assets/listAssetViews), [GET /api/v1.0/users/views](#/Users/listUserViews), or [GET /api/v1.0/views/for-sites](#/Views/listSiteViews).
2. **UserId** - Use [POST /api/v1.0/search](#/Users/searchUsers) to find the recipient and extract `Item.Users[].UserId`.

**Workflow Example**
1. Choose a view to share and copy its ViewId.
2. Find the recipient userId via search.
3. [POST /api/v1.0/views/users/new](#/Views/createViewUser) with ViewId, UserId, and Access.

**Minimal Required Fields**: `ViewId`, `UserId`, `Access`.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `ViewShare` | `ViewShare` | - |

#### Returns

- Typed call return: `ViewShareItemCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ViewShareItemCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_view_team`

Provenance: Golden OpenAPI contract

Operation ID: `deleteViewTeam`

- Sync: `client.views.delete_view_team(view_team_id=..., timeout=None)`
- Async: `await client.views.delete_view_team(view_team_id=..., timeout=None)`
- Raw payload: `client.views.delete_view_team.raw(view_team_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/views/teams/{viewTeamId}`
- Source controller: `IncidentIQ API`

Delete view team share

Deletes a team share assignment so the team no longer has access to the view.

**Prerequisites**
1. **viewTeamId** - Use [GET /api/v1.0/views/{viewId}/teams](#/Views/listViewTeams) to list shares and extract `Items[].ViewTeamId`.

**Workflow Example**
1. List team shares: [GET /api/v1.0/views/{viewId}/teams](#/Views/listViewTeams).
2. Delete the share: [DELETE /api/v1.0/views/teams/{viewTeamId}](#/Views/deleteViewTeam).

**Minimal Required Fields**: `viewTeamId` (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `view_team_id` | `viewTeamId` | `path` | `yes` | `str` | `-` | Identifier of the view team share assignment. |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_view_user`

Provenance: Golden OpenAPI contract

Operation ID: `deleteViewUser`

- Sync: `client.views.delete_view_user(view_user_id=..., timeout=None)`
- Async: `await client.views.delete_view_user(view_user_id=..., timeout=None)`
- Raw payload: `client.views.delete_view_user.raw(view_user_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/views/users/{viewUserId}`
- Source controller: `IncidentIQ API`

Delete view user share

Deletes a user share assignment so the individual no longer has access to the view.

**Prerequisites**
1. **viewUserId** - Use [GET /api/v1.0/views/{viewId}/users](#/Views/listViewUsers) to list shares and extract `Items[].ViewUserId`.

**Workflow Example**
1. List user shares: [GET /api/v1.0/views/{viewId}/users](#/Views/listViewUsers).
2. Delete the share: [DELETE /api/v1.0/views/users/{viewUserId}](#/Views/deleteViewUser).

**Minimal Required Fields**: `viewUserId` (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `view_user_id` | `viewUserId` | `path` | `yes` | `str` | `-` | Identifier of the view user share assignment. Obtain via [POST /api/v1.0/users](#/Users/searchUsers), extract `Items[].UserId`. |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_view_definition`

Provenance: Golden OpenAPI contract

Operation ID: `getViewDefinition`

- Sync: `client.views.get_view_definition(view_id=..., timeout=None)`
- Async: `await client.views.get_view_definition(view_id=..., timeout=None)`
- Raw payload: `client.views.get_view_definition.raw(view_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/views/{viewId}`
- Source controller: `IncidentIQ API`

Get saved view definition

Retrieves the saved layout definition for ticket, asset, or user views so clients can reproduce the same filters, columns, sorting, and share metadata.

**Prerequisites**:
1. **viewId** – Obtain the view identifier from one of the list endpoints, such as [GET /api/v1.0/tickets/views](#/Tickets/listTicketViews), [GET /api/v1.0/assets/views](#/Assets/listAssetViews), or [GET /api/v1.0/views/for-sites](#/Views/listSiteViews).

**Workflow Example**:
1. List ticket views: [GET /api/v1.0/tickets/views](#/Tickets/listTicketViews) → capture the `ViewId` for "Agent SLA Compliance".
2. Retrieve the full definition: [GET /api/v1.0/views/{viewId}](#/Views/getViewDefinition).

**Minimal Required Fields**:
- `viewId` – saved view identifier returned by the list operation.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `view_id` | `viewId` | `path` | `yes` | `str` | `-` | Identifier of the saved view to retrieve. Obtain IDs by listing views for a specific module or by resolving a shared link in the UI. |

#### Returns

- Typed call return: `ViewDefinitionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ViewDefinitionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_view_filters`

Provenance: Golden OpenAPI contract

Operation ID: `getViewFilters`

- Sync: `client.views.get_view_filters(entity_type_id=..., view_id=..., timeout=None)`
- Async: `await client.views.get_view_filters(entity_type_id=..., view_id=..., timeout=None)`
- Raw payload: `client.views.get_view_filters.raw(entity_type_id=..., view_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/views/{entityTypeId}/{viewId}/filters`
- Source controller: `IncidentIQ API`

Get view filters

Returns the resolved filters for a view and entity type, combining the saved view definition with entity metadata. Use this to see the effective filter clauses that will be applied when the view runs.

**Prerequisites**
1. **entityTypeId** - Use [GET /api/v1.0/sites/{siteUrl}](#/Sites/getSiteByUrl) and read `Item.Settings.EntityTypes` for the module you are working with.
2. **viewId** - Obtain from [GET /api/v1.0/tickets/views](#/Tickets/listTicketViews), [GET /api/v1.0/assets/views](#/Assets/listAssetViews), [GET /api/v1.0/users/views](#/Users/listUserViews), or [GET /api/v1.0/views/for-sites](#/Views/listSiteViews).

**Workflow Example**
1. Get entity type ids: [GET /api/v1.0/sites/{siteUrl}](#/Sites/getSiteByUrl) -> capture the module's EntityTypeId.
2. List views and select a viewId.
3. Call [GET /api/v1.0/views/{entityTypeId}/{viewId}/filters](#/Views/getViewFilters) to retrieve resolved filter clauses.

**Minimal Required Fields**: `entityTypeId` (path), `viewId` (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `entity_type_id` | `entityTypeId` | `path` | `yes` | `str` | `-` | Entity type identifier for the filters requested. |
| `view_id` | `viewId` | `path` | `yes` | `str` | `-` | View identifier to resolve filters for. |

#### Returns

- Typed call return: `ViewFilterMatchResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ViewFilterMatchResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_view_team`

Provenance: Golden OpenAPI contract

Operation ID: `getViewTeam`

- Sync: `client.views.get_view_team(view_team_id=..., timeout=None)`
- Async: `await client.views.get_view_team(view_team_id=..., timeout=None)`
- Raw payload: `client.views.get_view_team.raw(view_team_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/views/teams/{viewTeamId}`
- Source controller: `IncidentIQ API`

Get view team share

Returns a single team share assignment for a view, including access level and response status.

**Prerequisites**
1. **viewTeamId** - Use [GET /api/v1.0/views/{viewId}/teams](#/Views/listViewTeams) to list shares and extract `Items[].ViewTeamId`.

**Workflow Example**
1. List team shares: [GET /api/v1.0/views/{viewId}/teams](#/Views/listViewTeams).
2. Get the share: [GET /api/v1.0/views/teams/{viewTeamId}](#/Views/getViewTeam).

**Minimal Required Fields**: `viewTeamId` (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `view_team_id` | `viewTeamId` | `path` | `yes` | `str` | `-` | Identifier of the view team share assignment. |

#### Returns

- Typed call return: `ViewShareItemGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ViewShareItemGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_view_user`

Provenance: Golden OpenAPI contract

Operation ID: `getViewUser`

- Sync: `client.views.get_view_user(view_user_id=..., timeout=None)`
- Async: `await client.views.get_view_user(view_user_id=..., timeout=None)`
- Raw payload: `client.views.get_view_user.raw(view_user_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/views/users/{viewUserId}`
- Source controller: `IncidentIQ API`

Get view user share

Returns a single user share assignment for a view, including access level and response status.

**Prerequisites**
1. **viewUserId** - Use [GET /api/v1.0/views/{viewId}/users](#/Views/listViewUsers) to list shares and extract `Items[].ViewUserId`.

**Workflow Example**
1. List user shares: [GET /api/v1.0/views/{viewId}/users](#/Views/listViewUsers).
2. Get the share: [GET /api/v1.0/views/users/{viewUserId}](#/Views/getViewUser).

**Minimal Required Fields**: `viewUserId` (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `view_user_id` | `viewUserId` | `path` | `yes` | `str` | `-` | Identifier of the view user share assignment. Obtain via [POST /api/v1.0/users](#/Users/searchUsers), extract `Items[].UserId`. |

#### Returns

- Typed call return: `ViewShareItemGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ViewShareItemGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_view_teams`

Provenance: Golden OpenAPI contract

Operation ID: `listViewTeams`

- Sync: `client.views.list_view_teams(view_id=..., p=None, s=None, timeout=None)`
- Async: `await client.views.list_view_teams(view_id=..., p=None, s=None, timeout=None)`
- Raw payload: `client.views.list_view_teams.raw(view_id=..., p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v1.0/views/{viewId}/teams`
- Source controller: `IncidentIQ API`

List view teams

Returns the team share assignments for a view so you can audit group access and capture viewTeamId values for updates or responses.

**Prerequisites**
1. **viewId** - Obtain from [GET /api/v1.0/tickets/views](#/Tickets/listTicketViews), [GET /api/v1.0/assets/views](#/Assets/listAssetViews), [GET /api/v1.0/users/views](#/Users/listUserViews), or [GET /api/v1.0/views/for-sites](#/Views/listSiteViews).

**Workflow Example**
1. List views and pick a viewId.
2. [GET /api/v1.0/views/{viewId}/teams](#/Views/listViewTeams) to retrieve share assignments.
3. Use viewTeamId values with update/delete/response endpoints.

**Minimal Required Fields**: `viewId` (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `view_id` | `viewId` | `path` | `yes` | `str` | `-` | Identifier of the view to list team shares for. |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index. Defaults to 0 when omitted. |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of records per page. Defaults to 100 when omitted. |

#### Returns

- Typed call return: `ViewShareListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ViewShareListResponse`
- Pagination helper: `client.views.list_view_teams.iter_pages(start_page=1, page_size=100, max_pages=None, view_id=..., p=None, s=None, timeout=None)`

---

### `list_view_users`

Provenance: Golden OpenAPI contract

Operation ID: `listViewUsers`

- Sync: `client.views.list_view_users(view_id=..., p=None, s=None, timeout=None)`
- Async: `await client.views.list_view_users(view_id=..., p=None, s=None, timeout=None)`
- Raw payload: `client.views.list_view_users.raw(view_id=..., p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v1.0/views/{viewId}/users`
- Source controller: `IncidentIQ API`

List view users

Returns the user share assignments for a view so you can see who has access and gather viewUserId values for updates or responses.

**Prerequisites**
1. **viewId** - Obtain from [GET /api/v1.0/tickets/views](#/Tickets/listTicketViews), [GET /api/v1.0/assets/views](#/Assets/listAssetViews), [GET /api/v1.0/users/views](#/Users/listUserViews), or [GET /api/v1.0/views/for-sites](#/Views/listSiteViews).

**Workflow Example**
1. List views in the module and select a viewId.
2. [GET /api/v1.0/views/{viewId}/users](#/Views/listViewUsers) to retrieve share assignments.
3. Use viewUserId values with update/delete/response endpoints.

**Minimal Required Fields**: `viewId` (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `view_id` | `viewId` | `path` | `yes` | `str` | `-` | Identifier of the view to list user shares for. |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index. Defaults to 0 when omitted. |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of records per page. Defaults to 250 when omitted. |

#### Returns

- Typed call return: `ViewShareListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ViewShareListResponse`
- Pagination helper: `client.views.list_view_users.iter_pages(start_page=1, page_size=100, max_pages=None, view_id=..., p=None, s=None, timeout=None)`

---

### `list_views_all_products`

Provenance: Golden OpenAPI contract

Operation ID: `listViewsAllProducts`

- Sync: `client.views.list_views_all_products(view_type_id=..., p=None, s=None, timeout=None)`
- Async: `await client.views.list_views_all_products(view_type_id=..., p=None, s=None, timeout=None)`
- Raw payload: `client.views.list_views_all_products.raw(view_type_id=..., p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v1.0/views/allproducts/{viewTypeId}`
- Source controller: `IncidentIQ API`

List views across all products

Returns saved views across all products for a specific view type. Use this to locate every view definition that shares the same ViewTypeId, regardless of module or site.

**Prerequisites**
1. **viewTypeId** - Use [GET /api/v1.0/tickets/views](#/Tickets/listTicketViews), [GET /api/v1.0/assets/views](#/Assets/listAssetViews), [GET /api/v1.0/users/views](#/Users/listUserViews), or [GET /api/v1.0/views/for-sites](#/Views/listSiteViews) and extract `Items[].ViewTypeId`.

**Workflow Example**
1. List module views to find a ViewTypeId.
2. Call [GET /api/v1.0/views/allproducts/{viewTypeId}](#/Views/listViewsAllProducts) with paging parameters.
3. Use the returned ViewId values to retrieve full definitions if needed.

**Minimal Required Fields**: `viewTypeId` (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `view_type_id` | `viewTypeId` | `path` | `yes` | `str` | `-` | View type identifier, such as `Tickets.CustomView` or `Assets.Group`. |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index. Defaults to 0 when omitted. |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of records per page. Defaults to 100 when omitted. |

#### Returns

- Typed call return: `ViewListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ViewListResponse`
- Pagination helper: `client.views.list_views_all_products.iter_pages(start_page=1, page_size=100, max_pages=None, view_type_id=..., p=None, s=None, timeout=None)`

---

### `update_view_schedules`

Provenance: Golden OpenAPI contract

Operation ID: `updateViewSchedules`

- Sync: `client.views.update_view_schedules(view_id=..., body=..., timeout=None)`
- Async: `await client.views.update_view_schedules(view_id=..., body=..., timeout=None)`
- Raw payload: `client.views.update_view_schedules.raw(view_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/views/{viewId}/schedules`
- Source controller: `IncidentIQ API`

Update view schedules

Replaces the schedule configuration for a saved view. This endpoint overwrites the existing schedules array with the one you supply, enabling exports or emailed deliveries on a cadence.

**Prerequisites**
1. **viewId** - Obtain from a list endpoint such as [GET /api/v1.0/tickets/views](#/Tickets/listTicketViews) or [GET /api/v1.0/views/for-sites](#/Views/listSiteViews).
2. **Schedule template** - Use [GET /api/v1.0/views/{viewId}](#/Views/getViewDefinition) to inspect current schedule objects before replacing them.

**Workflow Example**
1. Fetch the current view definition: [GET /api/v1.0/views/{viewId}](#/Views/getViewDefinition).
2. Build a new schedules array (enable/disable or update delivery settings).
3. [POST /api/v1.0/views/{viewId}/schedules](#/Views/updateViewSchedules) with the schedule array to replace existing schedules.

**Minimal Required Fields**: `viewId` (path). For each schedule: `ViewScheduleId`, `SiteId`, `ProductId`, `ViewId`, `IsEnabled`, `IsMultiRowExportEnabled`.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `view_id` | `viewId` | `path` | `yes` | `str` | `-` | Identifier of the view to update. |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_view_sort`

Provenance: Golden OpenAPI contract

Operation ID: `updateViewSort`

- Sync: `client.views.update_view_sort(view_id=..., body=..., timeout=None)`
- Async: `await client.views.update_view_sort(view_id=..., body=..., timeout=None)`
- Raw payload: `client.views.update_view_sort.raw(view_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/views/{viewId}/sort`
- Source controller: `IncidentIQ API`

Update view sort

Updates the sort configuration for a saved view without changing filters or columns. This controls the default order used when the view is executed.

**Prerequisites**
1. **viewId** - Obtain from [GET /api/v1.0/tickets/views](#/Tickets/listTicketViews), [GET /api/v1.0/assets/views](#/Assets/listAssetViews), [GET /api/v1.0/users/views](#/Users/listUserViews), or [GET /api/v1.0/views/for-sites](#/Views/listSiteViews).

**Workflow Example**
1. List views for the module and select a viewId.
2. [POST /api/v1.0/views/{viewId}/sort](#/Views/updateViewSort) with `Field`, `Name`, and `Direction`.
3. Re-run the view to validate the new ordering.

**Minimal Required Fields**: `viewId` (path), `Field`, `Name`, `Direction`.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `view_id` | `viewId` | `path` | `yes` | `str` | `-` | Identifier of the view to update. |
| `body` | `body` | `body` | `yes` | `ViewSort` | `ViewSort` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_view_team`

Provenance: Golden OpenAPI contract

Operation ID: `updateViewTeam`

- Sync: `client.views.update_view_team(view_team_id=..., body=..., timeout=None)`
- Async: `await client.views.update_view_team(view_team_id=..., body=..., timeout=None)`
- Raw payload: `client.views.update_view_team.raw(view_team_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/views/teams/{viewTeamId}`
- Source controller: `IncidentIQ API`

Update view team share

Updates a team share assignment. If the share does not exist, it is created with the supplied payload.

**Prerequisites**
1. **viewTeamId** - Use [GET /api/v1.0/views/{viewId}/teams](#/Views/listViewTeams) to list existing shares, or create one with [POST /api/v1.0/views/teams/new](#/Views/createViewTeam).
2. **TeamId** - Use [GET /api/v1.0/teams](#/Teams/listTeams) to locate the team to share with.

**Workflow Example**
1. List team shares for the view and choose a viewTeamId.
2. [POST /api/v1.0/views/teams/{viewTeamId}](#/Views/updateViewTeam) with updated Access or Response.
3. Re-fetch the share to confirm.

**Minimal Required Fields**: `viewTeamId` (path), `ViewId`, `TeamId`, `Access`.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `view_team_id` | `viewTeamId` | `path` | `yes` | `str` | `-` | Identifier of the view team share assignment. |
| `body` | `body` | `body` | `yes` | `ViewShare` | `ViewShare` | - |

#### Returns

- Typed call return: `ViewShareItemUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ViewShareItemUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_view_team_response`

Provenance: Golden OpenAPI contract

Operation ID: `updateViewTeamResponse`

- Sync: `client.views.update_view_team_response(view_team_id=..., view_user_id=..., response=..., timeout=None)`
- Async: `await client.views.update_view_team_response(view_team_id=..., view_user_id=..., response=..., timeout=None)`
- Raw payload: `client.views.update_view_team_response.raw(view_team_id=..., view_user_id=..., response=..., timeout=None)`
- HTTP route: `POST /api/v1.0/views/teams/{viewTeamId}/users/{viewUserId}/response/{response}`
- Source controller: `IncidentIQ API`

Update view team response

Records a user's response to a team shared view invitation.

**Prerequisites**
1. **viewTeamId** - Use [GET /api/v1.0/views/{viewId}/teams](#/Views/listViewTeams) to list team shares and extract `Items[].ViewTeamId`.
2. **viewUserId** - Use [GET /api/v1.0/views/{viewId}/users](#/Views/listViewUsers) to list user shares and extract `Items[].ViewUserId`.

**Workflow Example**
1. List team shares and user shares for the view.
2. [POST /api/v1.0/views/teams/{viewTeamId}/users/{viewUserId}/response/{response}](#/Views/updateViewTeamResponse) to store the response.

**Minimal Required Fields**: `viewTeamId` (path), `viewUserId` (path), `response` (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `view_team_id` | `viewTeamId` | `path` | `yes` | `str` | `-` | Identifier of the view team share assignment. |
| `view_user_id` | `viewUserId` | `path` | `yes` | `str` | `-` | Identifier of the view user share assignment. Obtain via [POST /api/v1.0/users](#/Users/searchUsers), extract `Items[].UserId`. |
| `response` | `response` | `path` | `yes` | `str` | `-` | Response value to record for the share invitation. |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_view_user`

Provenance: Golden OpenAPI contract

Operation ID: `updateViewUser`

- Sync: `client.views.update_view_user(view_user_id=..., body=..., timeout=None)`
- Async: `await client.views.update_view_user(view_user_id=..., body=..., timeout=None)`
- Raw payload: `client.views.update_view_user.raw(view_user_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/views/users/{viewUserId}`
- Source controller: `IncidentIQ API`

Update view user share

Updates a user share assignment. If the share does not exist, it is created.

**Prerequisites**
1. **viewUserId** - Use [GET /api/v1.0/views/{viewId}/users](#/Views/listViewUsers) to list existing shares, or create one with [POST /api/v1.0/views/users/new](#/Views/createViewUser).
2. **UserId** - Use [POST /api/v1.0/search](#/Users/searchUsers) to locate the recipient and extract `Item.Users[].UserId`.

**Workflow Example**
1. List user shares for the view and choose a viewUserId.
2. [POST /api/v1.0/views/users/{viewUserId}](#/Views/updateViewUser) with updated Access or Response.
3. Re-fetch the share to confirm.

**Minimal Required Fields**: `viewUserId` (path), `ViewId`, `UserId`, `Access`.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `view_user_id` | `viewUserId` | `path` | `yes` | `str` | `-` | Identifier of the view user share assignment. Obtain via [POST /api/v1.0/users](#/Users/searchUsers), extract `Items[].UserId`. |
| `body` | `body` | `body` | `yes` | `ViewShare` | `ViewShare` | - |

#### Returns

- Typed call return: `ViewShareItemUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ViewShareItemUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_view_user_response`

Provenance: Golden OpenAPI contract

Operation ID: `updateViewUserResponse`

- Sync: `client.views.update_view_user_response(view_user_id=..., response=..., timeout=None)`
- Async: `await client.views.update_view_user_response(view_user_id=..., response=..., timeout=None)`
- Raw payload: `client.views.update_view_user_response.raw(view_user_id=..., response=..., timeout=None)`
- HTTP route: `POST /api/v1.0/views/users/{viewUserId}/response/{response}`
- Source controller: `IncidentIQ API`

Update view user response

Records a user's response to a view share invitation (Accepted, Declined, or NoResponse).

**Prerequisites**
1. **viewUserId** - Use [GET /api/v1.0/views/{viewId}/users](#/Views/listViewUsers) to list shares and extract `Items[].ViewUserId`.

**Workflow Example**
1. List user shares: [GET /api/v1.0/views/{viewId}/users](#/Views/listViewUsers).
2. [POST /api/v1.0/views/users/{viewUserId}/response/{response}](#/Views/updateViewUserResponse) to capture the response.

**Minimal Required Fields**: `viewUserId` (path), `response` (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `view_user_id` | `viewUserId` | `path` | `yes` | `str` | `-` | Identifier of the view user share assignment. Obtain via [POST /api/v1.0/users](#/Users/searchUsers), extract `Items[].UserId`. |
| `response` | `response` | `path` | `yes` | `str` | `-` | Response value to record for the share invitation. |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
