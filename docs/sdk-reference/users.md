# `users` Namespace

Sync client access: `client.users`

Async client access: `client.users` with `await` on method calls.

## Aliases

| Alias | Canonical Method | Route |
| --- | --- | --- |
| `delete` | `delete_user` | `DELETE /users/{UserId}` |
| `get` | `get_user` | `GET /users/{UserId}` |
| `list` | `get_users_legacy` | `GET /users` |
| `update` | `update_user` | `POST /users/{UserId}` |

## Methods

### `create_local_user`

Operation ID: `User_CreateLocalUser`

- Sync: `client.users.create_local_user(user=..., timeout=None)`
- Async: `await client.users.create_local_user(user=..., timeout=None)`
- Raw payload: `client.users.create_local_user.raw(user=..., timeout=None)`
- HTTP route: `POST /users/local/new`
- Source controller: `Users`

Create User

#### Creates the user(s) with attributes as specified.
#### Will need to include both a LocationId which can be queried at `GET /api/v1.0/locations/all`.
#### Along with a RoleId:
| RoleId | Name |
| ----------- | ----------- |
| 6D5FEE76-E05E-43C0-B8E9-B8447746E501 | Student |
| 6D5FEE76-E05E-43C0-B8E9-B8447746E502 | Faculty |
| 6D5FEE76-E05E-43C0-B8E9-B8447746E503 | Staff |
| 6D5FEE76-E05E-43C0-B8E9-B8447746E504 | Agent |
| 6D5FEE76-E05E-43C0-B8E9-B8447746E507 | Parent / Guardian |
#### Sample request:
```
POST /api/v1.0/users/local/new
{
"PreventProviderUpdates": false,
"DataMappings": {},
"FirstName": "John",
"LastName": "Smith",
"Email": "johnsmith@smith.com",
"SchoolIdNumber": "SMT12",
"Phone": "555-5555",
"Password": "T3STP@SS",
"PasswordExpirationDate": "09/01/2022",
"InternalComments": "lorem ipsum dias",
"Grade": "4",
"LocationId": "1fd1574a-2243-e611-a93b-a45e60e682da",
"RoleId": "6d5fee76-e05e-43c0-b8e9-b8447746e504",
"UpdateCustomFields": true,
"CustomFieldValues": []
}
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user` | `User` | `body` | `yes` | `User` | `User` | The User to be created |

#### Returns

- Typed call return: `ItemCreateResponseOfUser`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemCreateResponseOfUser`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_user`

Operation ID: `User_DeleteUser`

- Sync: `client.users.delete_user(user_id=..., timeout=None)`
- Async: `await client.users.delete_user(user_id=..., timeout=None)`
- Raw payload: `client.users.delete_user.raw(user_id=..., timeout=None)`
- HTTP route: `DELETE /users/{UserId}`
- Source controller: `Users`
- Aliases: `delete`

No contract summary provided.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_user_view`

Operation ID: `View_DeleteUserView`

- Sync: `client.users.delete_user_view(view_id=..., timeout=None)`
- Async: `await client.users.delete_user_view(view_id=..., timeout=None)`
- Raw payload: `client.users.delete_user_view.raw(view_id=..., timeout=None)`
- HTTP route: `DELETE /users/views/{ViewId}`
- Source controller: `Views`

No contract summary provided.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `view_id` | `ViewId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_agents`

Operation ID: `User_GetAgents`

- Sync: `client.users.get_agents(request_info=..., timeout=None)`
- Async: `await client.users.get_agents(request_info=..., timeout=None)`
- Raw payload: `client.users.get_agents.raw(request_info=..., timeout=None)`
- HTTP route: `POST /users/agents`
- Source controller: `Users`

Get Agents

#### Retrieves a list of agent based on filters set within the request object.
#### Sample request:
```
POST /api/v1.0/users/agents
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `request_info` | `RequestInfo` | `body` | `yes` | `GetUsersRequestV1` | `GetUsersRequestV1` | Request object containing filters |

#### Returns

- Typed call return: `ListGetResponseOfUser`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfUser`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_agents_legacy`

Operation ID: `User_GetAgentsLegacy`

- Sync: `client.users.get_agents_legacy(timeout=None)`
- Async: `await client.users.get_agents_legacy(timeout=None)`
- Raw payload: `client.users.get_agents_legacy.raw(timeout=None)`
- HTTP route: `GET /users/agents`
- Source controller: `Users`

No contract summary provided.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `ListGetResponseOfUser`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfUser`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_user`

Operation ID: `User_GetUser`

- Sync: `client.users.get_user(user_id=..., timeout=None)`
- Async: `await client.users.get_user(user_id=..., timeout=None)`
- Raw payload: `client.users.get_user.raw(user_id=..., timeout=None)`
- HTTP route: `GET /users/{UserId}`
- Source controller: `Users`
- Aliases: `get`

Get User

#### Retrieve a User's information.
#### Sample request:
```
GET /api/v1.0/users/0b92ee98-edef-4423-9e15-98fe5726c1af
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | User Id of the user details to be retrieved |

#### Returns

- Typed call return: `ItemGetResponseOfUser`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemGetResponseOfUser`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_user_view`

Operation ID: `View_GetUserView`

- Sync: `client.users.get_user_view(view_id=..., timeout=None)`
- Async: `await client.users.get_user_view(view_id=..., timeout=None)`
- Raw payload: `client.users.get_user_view.raw(view_id=..., timeout=None)`
- HTTP route: `GET /users/views/{ViewId}`
- Source controller: `Views`

Get User View

#### Retrieves details about a single user view in IIQ.   User lists can then be retrieved via GET `api/v1.0/users/view/{ViewId:guid}`.
#### Sample request:
```
GET /api/v1.0/users/views/{ViewId:guid}
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `view_id` | `ViewId` | `path` | `yes` | `str` | `-` | View Id which details are to be retrieved |

#### Returns

- Typed call return: `ItemGetResponseOfView`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemGetResponseOfView`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_user_views`

Operation ID: `View_GetUserViews`

- Sync: `client.users.get_user_views(timeout=None)`
- Async: `await client.users.get_user_views(timeout=None)`
- Raw payload: `client.users.get_user_views.raw(timeout=None)`
- HTTP route: `GET /users/views`
- Source controller: `Views`

Get User View List

#### Retrieves a list of all user views in IIQ.   User lists can then be retrieved via GET `api/v1.0/users/view/{ViewId:guid}`.
#### Sample request:
```
GET /api/v1.0/users/views
```

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `ListGetResponseOfView`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfView`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_users`

Operation ID: `User_GetUsers`

- Sync: `client.users.get_users(request_info=..., timeout=None)`
- Async: `await client.users.get_users(request_info=..., timeout=None)`
- Raw payload: `client.users.get_users.raw(request_info=..., timeout=None)`
- HTTP route: `POST /users`
- Source controller: `Users`

Get Users

#### Retrieves a list of users. A specific user can be retrieved via GET `api/v1.0/users/cb347afd-e235-43aa-832c-cddc89680e3c` with documentation under the _Get User_ section.
#### Sample request:
```
POST /api/v1.0/users
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `request_info` | `RequestInfo` | `body` | `yes` | `GetUsersRequestV1` | `GetUsersRequestV1` | Request object containing filters |

#### Returns

- Typed call return: `ListGetResponseOfUser`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfUser`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_users_for_view`

Operation ID: `User_GetUsersForView`

- Sync: `client.users.get_users_for_view(view_id=..., body_filters=..., timeout=None)`
- Async: `await client.users.get_users_for_view(view_id=..., body_filters=..., timeout=None)`
- Raw payload: `client.users.get_users_for_view.raw(view_id=..., body_filters=..., timeout=None)`
- HTTP route: `POST /users/view/{ViewId}`
- Source controller: `Users`

Get Users for View

#### Retrieves a list of all users in IIQ that fit the criteria of the view requested. A list of applicable User Views can be retrieved via GET `/api/v1.0/users/views`. More documentation available under the _Views_ section.
#### Sample request:
```
POST /api/v1.0/users/view/4e6817c9-86b5-4810-84d8-ae99dfb6ba81
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `view_id` | `ViewId` | `path` | `yes` | `str` | `-` | The ViewId to use |
| `body_filters` | `BodyFilters` | `body` | `yes` | `list[Any]` | `-` | Other filtration to use to filter the returned view's user list |

#### Returns

- Typed call return: `ListGetResponseOfUser`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfUser`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_users_legacy`

Operation ID: `User_GetUsersLegacy`

- Sync: `client.users.get_users_legacy(timeout=None)`
- Async: `await client.users.get_users_legacy(timeout=None)`
- Raw payload: `client.users.get_users_legacy.raw(timeout=None)`
- HTTP route: `GET /users`
- Source controller: `Users`
- Aliases: `list`

No contract summary provided.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `ListGetResponseOfUser`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfUser`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_users_per_grade`

Operation ID: `User_GetUsersPerGrade`

- Sync: `client.users.get_users_per_grade(timeout=None)`
- Async: `await client.users.get_users_per_grade(timeout=None)`
- Raw payload: `client.users.get_users_per_grade.raw(timeout=None)`
- HTTP route: `GET /users/stats/grades`
- Source controller: `Users`

Get User Counts Per Grade

#### Retrieve a list of grades with assigned user counts
#### Sample request:
```
GET /api/v1.0/users/stats/grades
```

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `ListGetResponseOfGradeStat`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfGradeStat`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_users_per_location`

Operation ID: `User_GetUsersPerLocation`

- Sync: `client.users.get_users_per_location(timeout=None)`
- Async: `await client.users.get_users_per_location(timeout=None)`
- Raw payload: `client.users.get_users_per_location.raw(timeout=None)`
- HTTP route: `GET /users/stats/locations`
- Source controller: `Users`

Get User Counts Per Location

#### Retrieve a list of locations with assigned user counts
#### Sample request:
```
GET /api/v1.0/users/stats/locations
```

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `ListGetResponseOfLocationStat`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfLocationStat`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_users_with_location_permission`

Operation ID: `User_GetUsersWithLocationPermission`

- Sync: `client.users.get_users_with_location_permission(location_id=..., timeout=None)`
- Async: `await client.users.get_users_with_location_permission(location_id=..., timeout=None)`
- Raw payload: `client.users.get_users_with_location_permission.raw(location_id=..., timeout=None)`
- HTTP route: `GET /users/location/{LocationId}`
- Source controller: `Users`

Get Location User Permissions

#### Retrieves a the user(s) requested along with their permissions for the locationId specified.  Locations can be queried at `GET /api/v1.0/locations/all`.  More details in the Locations section under _Get Locations_.
#### Sample request:
```
GET /api/v1.0/users/location/1e997655-cbce-4cc3-85a6-5420aa9c6206
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `location_id` | `LocationId` | `path` | `yes` | `str` | `-` | The LocationId of the Location to be queried |

#### Returns

- Typed call return: `ListGetResponseOfUserWithLocationPermission`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfUserWithLocationPermission`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_user`

Operation ID: `User_UpdateUser`

- Sync: `client.users.update_user(user_id=..., user=..., timeout=None)`
- Async: `await client.users.update_user(user_id=..., user=..., timeout=None)`
- Raw payload: `client.users.update_user.raw(user_id=..., user=..., timeout=None)`
- HTTP route: `POST /users/{UserId}`
- Source controller: `Users`
- Aliases: `update`

Update User

#### Updates specified user with attributes as specified.
#### Will need to include both a LocationId which can be queried at `GET /api/v1.0/locations/all`.
#### Along with a RoleId:
| RoleId | Name |
| ----------- | ----------- |
| 6D5FEE76-E05E-43C0-B8E9-B8447746E501 | Student |
| 6D5FEE76-E05E-43C0-B8E9-B8447746E502 | Faculty |
| 6D5FEE76-E05E-43C0-B8E9-B8447746E503 | Staff |
| 6D5FEE76-E05E-43C0-B8E9-B8447746E504 | Agent |
| 6D5FEE76-E05E-43C0-B8E9-B8447746E507 | Parent / Guardian |
#### Sample request:
```
POST /api/v1.0/users/88c33434-34c5-4e03-968c-db99b7d6606b
UpdateUserRequest: {
"PreventProviderUpdates": false,
"DataMappings": {},
"FirstName": "John",
"LastName": "Smith",
"Email": "johnsmith@gmail.com",
"SchoolIdNumber": "SMT12",
"Phone": "555-5555",
"Password": "T3STP@SS",
"PasswordExpirationDate": "09/01/2022",
"InternalComments": "lorem ipsum dias",
"Grade": "4",
"LocationId": "1fd1574a-2243-e611-a93b-a45e60e682da",
"RoleId": "6d5fee76-e05e-43c0-b8e9-b8447746e504",
"UpdateCustomFields": true,
"CustomFieldValues": []
}
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | The UserId of the user to be updated |
| `user` | `User` | `body` | `yes` | `UpdateUserRequest` | `UpdateUserRequest` | The user details to be updated |

#### Returns

- Typed call return: `ItemUpdateResponseOfUser`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemUpdateResponseOfUser`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_user_view`

Operation ID: `View_UpdateUserView`

- Sync: `client.users.update_user_view(view_id=..., user_view=..., timeout=None)`
- Async: `await client.users.update_user_view(view_id=..., user_view=..., timeout=None)`
- Raw payload: `client.users.update_user_view.raw(view_id=..., user_view=..., timeout=None)`
- HTTP route: `POST /users/views/{ViewId}`
- Source controller: `Views`

No contract summary provided.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `view_id` | `ViewId` | `path` | `yes` | `str` | `-` | - |
| `user_view` | `UserView` | `body` | `yes` | `View` | `View` | - |

#### Returns

- Typed call return: `ItemUpdateResponseOfView`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemUpdateResponseOfView`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
