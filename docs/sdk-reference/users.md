# `users` Golden Namespace

Sync client access: `client.users`

Async client access: `client.users` with `await` on method calls.

These methods are Golden because they come from the bundled Incident IQ OpenAPI contract.

## Methods

### `add_room_to_user`

Provenance: Golden OpenAPI contract

Operation ID: `addRoomToUser`

- Sync: `client.users.add_room_to_user(user_id=..., location_room_id=..., timeout=None)`
- Async: `await client.users.add_room_to_user(user_id=..., location_room_id=..., timeout=None)`
- Raw payload: `client.users.add_room_to_user.raw(user_id=..., location_room_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/users/{UserId}/rooms/{LocationRoomId}`
- Source controller: `IncidentIQ API`

Add room to user

Adds a single room assignment to a user without affecting existing room assignments. Use this when incrementally assigning rooms rather than replacing the full list.

**Prerequisites**
1. **UserId** - Use [POST /api/v1.0/users](#/Users/searchUsers) to locate the user. Extract `Items[].UserId`.
2. **LocationRoomId** - Use [POST /api/v2.0/locations/{locationId}/rooms](#/Locations/queryLocationRoomsByLocationId) to list rooms. Extract `Items[].LocationRoomId` (LocationId can be found via [GET /api/v1.0/locations/view](#/Locations/getAllSiteLocationsV2)).

**Workflow Example**
1. Identify user: [POST /api/v1.0/users](#/Users/searchUsers) → extract UserId.
2. Identify room: [POST /api/v2.0/locations/{locationId}/rooms](#/Locations/queryLocationRoomsByLocationId) → extract LocationRoomId.
3. POST this endpoint to add the room assignment.

**Minimal Required Fields**: UserId, LocationRoomId (path parameters)

**Notes**: Existing room assignments remain unchanged. Use DELETE on this same path to remove the assignment.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | User identifier. Obtain via [POST /api/v1.0/users](#/Users/searchUsers), extract `Items[].UserId`. |
| `location_room_id` | `LocationRoomId` | `path` | `yes` | `str` | `-` | Room identifier to add. |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `award_achievement`

Provenance: Golden OpenAPI contract

Operation ID: `awardAchievement`

- Sync: `client.users.award_achievement(user_id=..., achievement_id=..., timeout=None)`
- Async: `await client.users.award_achievement(user_id=..., achievement_id=..., timeout=None)`
- Raw payload: `client.users.award_achievement.raw(user_id=..., achievement_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/users/{UserId}/achievements/award/{AchievementId}`
- Source controller: `IncidentIQ API`

Award achievement to user

Awards a specific achievement to a user. This is typically used by administrators or automated systems to recognize accomplishments and milestones.

**Prerequisites**
1. **UserId** - Use [POST /api/v1.0/users](#/Users/searchUsers) to locate the user. Extract `Items[].UserId`.
2. **AchievementId** - Obtain from your achievements catalog or from [GET /api/v1.0/users/{UserId}/achievements](#/Users/getUserAchievements) if re-awarding an existing achievement.

**Workflow Example**
1. Search for the user: [POST /api/v1.0/users](#/Users/searchUsers) → extract UserId.
2. Identify the achievement to award (AchievementId).
3. POST this endpoint with UserId and AchievementId.

**Minimal Required Fields**: UserId, AchievementId (path parameters)

**Notes**: Typically restricted to admin roles or automated services. Duplicate awards may be ignored depending on server rules.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | UUID of the user to award Obtain via [POST /api/v1.0/users](#/Users/searchUsers), extract `Items[].UserId`. |
| `achievement_id` | `AchievementId` | `path` | `yes` | `str` | `-` | UUID of the achievement to award |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `bulk_set_user_rooms`

Provenance: Golden OpenAPI contract

Operation ID: `bulkSetUserRooms`

- Sync: `client.users.bulk_set_user_rooms(body=..., timeout=None)`
- Async: `await client.users.bulk_set_user_rooms(body=..., timeout=None)`
- Raw payload: `client.users.bulk_set_user_rooms.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/users/rooms/set`
- Source controller: `IncidentIQ API`

Bulk set room assignments for users

Sets room assignments for multiple users at once. Use this to align staff or students with physical rooms and keep location metadata consistent.

**Prerequisites**
1. **UserIds** - Use [POST /api/v1.0/users](#/Users/searchUsers) to gather `Items[].UserId` values.
2. **LocationId/Room** - Use [GET /api/v1.0/locations/view](#/Locations/getAllSiteLocationsV2) to obtain LocationId values and valid room names.

**Workflow Example**
1. Search for users and collect UserIds.
2. Build an array of `SetUserLocationRequest` objects with UserId and Rooms.
3. POST this endpoint to apply room assignments.

**Minimal Required Fields**: For each entry, UserId plus Rooms (and optionally LocationId).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `BulkSetUserRoomsUsersRoomsSetRequest` | `BulkSetUserRoomsUsersRoomsSetRequest` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `change_user_password`

Provenance: Golden OpenAPI contract

Operation ID: `changeUserPassword`

- Sync: `client.users.change_user_password(user_id=..., body=..., timeout=None)`
- Async: `await client.users.change_user_password(user_id=..., body=..., timeout=None)`
- Raw payload: `client.users.change_user_password.raw(user_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/users/{UserId}/change-password`
- Source controller: `IncidentIQ API`

Change user password

Changes the password for a user account. This is an administrative password set operation; for user-initiated reset flows, use the reset-password endpoint.

**Prerequisites**
1. **UserId** - Use [POST /api/v1.0/users](#/Users/searchUsers) to locate the user and extract `Items[].UserId`.

**Workflow Example**
1. Search for the user: [POST /api/v1.0/users](#/Users/searchUsers) -> extract UserId.
2. POST this endpoint with `Password` and `ConfirmPassword`.
3. Inform the user to sign in with the new credentials.

**Minimal Required Fields**: UserId (path), Password, ConfirmPassword.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | User identifier. Obtain via [POST /api/v1.0/users](#/Users/searchUsers), extract `Items[].UserId`. |
| `body` | `body` | `body` | `yes` | `SetUserPasswordRequest` | `SetUserPasswordRequest` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `complete_external_user_registration`

Provenance: Golden OpenAPI contract

Operation ID: `completeExternalUserRegistration`

- Sync: `client.users.complete_external_user_registration(body=..., timeout=None)`
- Async: `await client.users.complete_external_user_registration(body=..., timeout=None)`
- Raw payload: `client.users.complete_external_user_registration.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/users/external/complete-registration`
- Source controller: `IncidentIQ API`

Complete external user registration

Completes the registration process for an external user after email verification. Allows anonymous access.

**Prerequisites**
1. **Token** - Obtain from the registration email generated by [POST /api/v1.0/users/external/register](#/Users/registerExternalUser).

**Workflow Example**
1. User registers: [POST /api/v1.0/users/external/register](#/Users/registerExternalUser).
2. User receives token via email.
3. POST this endpoint with Token, Password, and ConfirmPassword to activate the account.

**Minimal Required Fields**: Token, Password, ConfirmPassword.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `CompleteExternalUserRegistrationRequest` | `CompleteExternalUserRegistrationRequest` | - |

#### Returns

- Typed call return: `AuthorizedUserGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AuthorizedUserGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `convert_user_to_local`

Provenance: Golden OpenAPI contract

Operation ID: `convertUserToLocal`

- Sync: `client.users.convert_user_to_local(user_id=..., body=..., timeout=None)`
- Async: `await client.users.convert_user_to_local(user_id=..., body=..., timeout=None)`
- Raw payload: `client.users.convert_user_to_local.raw(user_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/users/convert/to/local/{UserId}`
- Source controller: `IncidentIQ API`

Convert user to local account

Converts an existing user (for example, SSO/SAML) to a local account with a password so they can authenticate directly.

**Prerequisites**
1. **UserId** - Use [POST /api/v1.0/users](#/Users/searchUsers) to locate the user and extract `Items[].UserId`.
2. Ensure you have a password that meets site policy requirements.

**Workflow Example**
1. Search for the user: [POST /api/v1.0/users](#/Users/searchUsers) -> extract UserId.
2. POST this endpoint with the UserId path value and the new password in the request body.
3. Confirm the user can authenticate locally.

**Minimal Required Fields**: UserId (path) and a password string in the request body.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | UUID of the user to convert Obtain via [POST /api/v1.0/users](#/Users/searchUsers), extract `Items[].UserId`. |
| `body` | `body` | `body` | `yes` | `ConvertUserToLocalUsersConvertToLocalByUserIdRequest` | `ConvertUserToLocalUsersConvertToLocalByUserIdRequest` | - |

#### Returns

- Typed call return: `GuidCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `GuidCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `count_users`

Provenance: Golden OpenAPI contract

Operation ID: `countUsers`

- Sync: `client.users.count_users(body=None, timeout=None)`
- Async: `await client.users.count_users(body=None, timeout=None)`
- Raw payload: `client.users.count_users.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/users/count`
- Source controller: `IncidentIQ API`

Count users matching filters

Returns the count of users matching the specified filter criteria without returning full user records. Useful for pagination UI, dashboards, and report previews.

**Prerequisites**
1. **RoleId** (optional) - Use [GET /api/v1.0/roles](#/Roles/listRoles).
2. **LocationId** (optional) - Use [GET /api/v1.0/locations/view](#/Locations/getAllSiteLocationsV2).
3. **TeamId** (optional) - Use [GET /api/v1.0/teams](#/Teams/listTeams).

**Workflow Example**
1. Build Filters the same way as [POST /api/v1.0/users](#/Users/searchUsers).
2. POST this endpoint with those filters to get `Paging.TotalRows`.
3. Use the count to size pagination controls before retrieving full records.

**Minimal Required Fields**: None. Filters are optional.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `GetUsersRequestV1` | `GetUsersRequestV1` | - |

#### Returns

- Typed call return: `UsersListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UsersListGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_local_user`

Provenance: Golden OpenAPI contract

Operation ID: `createLocalUser`

- Sync: `client.users.create_local_user(body=..., timeout=None)`
- Async: `await client.users.create_local_user(body=..., timeout=None)`
- Raw payload: `client.users.create_local_user.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/users/local/new`
- Source controller: `IncidentIQ API`

Create a new local user

Creates a new local user account and returns the created user record.

**Prerequisites**: This endpoint requires UUIDs from other API calls:
1. **LocationId** - Use [GET /api/v1.0/locations/view](#/Locations/getAllSiteLocationsV2) → Extract `Items[].LocationId`
2. **RoleId** - Use [GET /api/v1.0/roles](#/Roles/listRoles) → Extract `Items[].RoleId`

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `NewLocalUserRequest` | `NewLocalUserRequest` | - |

#### Returns

- Typed call return: `UserDetailCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UserDetailCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_local_user_from_sis`

Provenance: Golden OpenAPI contract

Operation ID: `createLocalUserFromSis`

- Sync: `client.users.create_local_user_from_sis(sis_user_id=..., body=..., timeout=None)`
- Async: `await client.users.create_local_user_from_sis(sis_user_id=..., body=..., timeout=None)`
- Raw payload: `client.users.create_local_user_from_sis.raw(sis_user_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/users/local/from/sis/{SisUserId}`
- Source controller: `IncidentIQ API`

Create local user from SIS user

Creates a local IncidentIQ user account from an existing SIS user record, linking the SIS identity to a new local account.

**Prerequisites**
1. **SisUserId** - Use [POST /api/v1.0/users](#/Users/searchUsers) with SIS-related filters (for example `sisclass`, `sisuserstatus`) and capture the `SisUserId` from the user record.
2. **LocationId/RoleId** (if required) - Use [GET /api/v1.0/locations/view](#/Locations/getAllSiteLocationsV2) and [GET /api/v1.0/sites/roles](#/Sites/listRoles).

**Workflow Example**
1. Locate the SIS user and capture SisUserId.
2. Build the User payload with required profile fields.
3. POST this endpoint with SisUserId and the User body to create the local account.

**Minimal Required Fields**: SisUserId (path) and required fields in the User payload (commonly FirstName, LastName, Email).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `sis_user_id` | `SisUserId` | `path` | `yes` | `str` | `-` | UUID of the SIS user to create from Obtain via [POST /api/v1.0/users](#/Users/searchUsers), extract `Items[].UserId`. |
| `body` | `body` | `body` | `yes` | `User` | `User` | - |

#### Returns

- Typed call return: `UserDetailCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UserDetailCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_shell_user`

Provenance: Golden OpenAPI contract

Operation ID: `createShellUser`

- Sync: `client.users.create_shell_user(body=..., timeout=None)`
- Async: `await client.users.create_shell_user(body=..., timeout=None)`
- Raw payload: `client.users.create_shell_user.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/users/shell/new`
- Source controller: `IncidentIQ API`

Create shell user

Creates a shell user account, which is a placeholder record that can be converted into a full account later. Useful for pre-provisioning users before onboarding completes.

**Prerequisites**
1. **LocationId** (if required) - Use [GET /api/v1.0/locations/view](#/Locations/getAllSiteLocationsV2).
2. **RoleId** (if required) - Use [GET /api/v1.0/sites/roles](#/Sites/listRoles).

**Workflow Example**
1. Assemble the User payload with minimal identity fields.
2. POST this endpoint to create the shell user.
3. Later, update the record via [POST /api/v1.0/users/{UserId}](#/Users/updateUser) or convert to local with [POST /api/v1.0/users/convert/to/local/{UserId}](#/Users/convertUserToLocal).

**Minimal Required Fields**: Fields required by `User` for your tenant (commonly FirstName, LastName, Email, LocationId).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `User` | `User` | - |

#### Returns

- Typed call return: `UserDetailCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UserDetailCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_shortcut`

Provenance: Golden OpenAPI contract

Operation ID: `createShortcut`

- Sync: `client.users.create_shortcut(body=..., timeout=None)`
- Async: `await client.users.create_shortcut(body=..., timeout=None)`
- Raw payload: `client.users.create_shortcut.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/users/shortcut/new`
- Source controller: `IncidentIQ API`

Create a new shortcut

Creates a new rule-based shortcut linking a filter set and rule configuration for quick access to filtered entity views.

**Prerequisites**
1. **RuleId** - Use the Rules API to create or retrieve a rule configuration.
2. **ForEntityTypeId** - Entity type UUID (Ticket, Asset, User, etc.).
3. **FilterSetId** (optional) - Use [GET /api/v1.0/filters/sets/for/type/{FilterSetType}](#/Filters/getFilterSetsByType) to retrieve filter set IDs by type.

**Workflow Example**
1. Create or select a rule: obtain RuleId from Rules API.
2. Determine entity type: use ForEntityTypeId for the target entity (e.g., Ticket entity type).
3. POST to this endpoint with shortcut configuration.
4. Extract `Item.ShortcutId` from response for future reference.

**Minimal Required Fields**: Name, Scope, RuleId, ForEntityTypeId

**Notes**: Scope determines visibility: User (personal), Role (shared with role members), Team (team members), Site (site-wide), Global (all sites). OwnerId should match the user, role, or team ID based on Scope.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `Shortcut` | `Shortcut` | - |

#### Returns

- Typed call return: `ShortcutCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ShortcutCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_temp_user`

Provenance: Golden OpenAPI contract

Operation ID: `createTempUser`

- Sync: `client.users.create_temp_user(body=..., timeout=None)`
- Async: `await client.users.create_temp_user(body=..., timeout=None)`
- Raw payload: `client.users.create_temp_user.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/users/local/temp`
- Source controller: `IncidentIQ API`

Create temporary user

Creates a temporary user account for short-term or guest access. This endpoint allows anonymous access and returns a lightweight user record.

**Prerequisites**
1. **LocationId** (if required) - Use [GET /api/v1.0/locations/view](#/Locations/getAllSiteLocationsV2) to select a location.

**Workflow Example**
1. Build a minimal SimpleUser payload with name and contact details.
2. POST this endpoint to create the temporary account.
3. Use the returned UserId for ticket creation or check-in workflows.

**Minimal Required Fields**: Fields required by `SimpleUser` (typically FirstName, LastName, Email; LocationId when enforced).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `SimpleUser` | `SimpleUser` | - |

#### Returns

- Typed call return: `SimpleUserCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `SimpleUserCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_user_view`

Provenance: Golden OpenAPI contract

Operation ID: `createUserView`

- Sync: `client.users.create_user_view(body=..., timeout=None)`
- Async: `await client.users.create_user_view(body=..., timeout=None)`
- Raw payload: `client.users.create_user_view.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/users/views/new`
- Source controller: `IncidentIQ API`

Create user view

Creates a new custom view definition for filtering and displaying user records. Views allow users to save frequently used filter combinations and column configurations.

**Prerequisites**
1. **SiteId** - Use [GET /api/v2.0/users/my/locations](#/Users/getCurrentUserLocationsV2) to get available locations. Extract `Items[].SiteId`.
2. **ProductId** - Product identifier for view context (e.g., Ticketing, Assets).

**Workflow Example**
1. Get site context: [GET /api/v2.0/users/my/locations](#/Users/getCurrentUserLocationsV2) → extract SiteId
2. Create view: POST this endpoint with view configuration
3. Extract `Item.ViewId` from response for future reference

**Minimal Required Fields**: Name, ViewTypeId, SiteId, ProductId

**Notes**: Views are user-specific. The ViewTypeId determines what entity type the view filters (e.g., 'Users.CustomView'). Set PageSize to control default pagination.

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

### `delete_shortcut`

Provenance: Golden OpenAPI contract

Operation ID: `deleteShortcut`

- Sync: `client.users.delete_shortcut(shortcut_id=..., timeout=None)`
- Async: `await client.users.delete_shortcut(shortcut_id=..., timeout=None)`
- Raw payload: `client.users.delete_shortcut.raw(shortcut_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/users/shortcut/{ShortcutId}`
- Source controller: `IncidentIQ API`

Delete a shortcut

Permanently removes a rule-based shortcut configuration.

**Prerequisites**
1. **ShortcutId** - Use [GET /api/v1.0/users/shortcuts/available](#/Users/getAvailableShortcuts) to list shortcuts. Extract `Items[].ShortcutId`.

**Workflow Example**
1. List shortcuts: [GET /api/v1.0/users/shortcuts/available](#/Users/getAvailableShortcuts) → identify shortcut to remove
2. Delete shortcut: DELETE this endpoint with the ShortcutId

**Notes**: Only shortcuts the user owns or has permission to manage can be deleted. This action is permanent and cannot be undone.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `shortcut_id` | `ShortcutId` | `path` | `yes` | `str` | `-` | Shortcut identifier. |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_user`

Provenance: Golden OpenAPI contract

Operation ID: `deleteUser`

- Sync: `client.users.delete_user(user_id=..., timeout=None)`
- Async: `await client.users.delete_user(user_id=..., timeout=None)`
- Raw payload: `client.users.delete_user.raw(user_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/users/{UserId}`
- Source controller: `IncidentIQ API`

Delete user

**Prerequisites**: This endpoint requires UUIDs from other API calls:
1. **UserId** - Use [POST /api/v1.0/users](#/Users/searchUsers) → Extract `Items[].UserId`

**Workflow Example**:
1. Search for user: [POST /api/v1.0/users](#/Users/searchUsers)
2. Extract UserId from response
3. [DELETE /api/v1.0/users/{UserId}](#/Users/deleteUser)

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | User identifier. |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_user_by_id`

Provenance: Golden OpenAPI contract

Operation ID: `deleteUserById`

- Sync: `client.users.delete_user_by_id(view_id=..., timeout=None)`
- Async: `await client.users.delete_user_by_id(view_id=..., timeout=None)`
- Raw payload: `client.users.delete_user_by_id.raw(view_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/users/views/{viewId}`
- Source controller: `IncidentIQ API`

Delete a user view

Deletes a saved user view (filter configuration) from the system. This removes the saved search criteria and column settings permanently.

**Prerequisites**
1. **viewId** - Use [GET /api/v1.0/users/views](#/Users/listUserViews) to list available views. Extract `Items[].ViewId` from the response.

**Workflow Example**
1. List user views: [GET /api/v1.0/users/views](#/Users/listUserViews) → identify view to delete.
2. Call this endpoint: [DELETE /api/v1.0/users/views/{viewId}](#/Views/deleteUserById) with the view UUID.

**Notes**: Deleting a view does not affect the underlying user data. Only the saved filter configuration is removed. Default system views cannot be deleted.

**Related Endpoints:**
- [GET /api/v1.0/users/views/{viewId}](#/Views/getUserView) - Get view details before deletion

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `view_id` | `viewId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `Any`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_user_v2`

Provenance: Golden OpenAPI contract

Operation ID: `deleteUserV2`

- Sync: `client.users.delete_user_v2(user_id=..., timeout=None)`
- Async: `await client.users.delete_user_v2(user_id=..., timeout=None)`
- Raw payload: `client.users.delete_user_v2.raw(user_id=..., timeout=None)`
- HTTP route: `DELETE /api/v2.0/users/delete/{userId}`
- Source controller: `IncidentIQ API`

Delete user

Permanently deletes a single user by their unique identifier.

**Use Cases**:
- Employee offboarding
- Student graduation/transfer cleanup
- GDPR/data retention compliance

**Warning**: This action is permanent. The user account, along with associated assignments and permissions, will be removed. Ticket history and audit logs may be retained for compliance purposes.

**Prerequisites**:
- Verify the user exists using [GET /api/v2.0/users/get/{userId}](#/Users/getUserById)
- Ensure no critical open tickets are assigned to this user

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `userId` | `path` | `yes` | `str` | `-` | Unique identifier of the user to delete. |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_users_by_ids_v2`

Provenance: Golden OpenAPI contract

Operation ID: `deleteUsersByIdsV2`

- Sync: `client.users.delete_users_by_ids_v2(body=..., timeout=None)`
- Async: `await client.users.delete_users_by_ids_v2(body=..., timeout=None)`
- Raw payload: `client.users.delete_users_by_ids_v2.raw(body=..., timeout=None)`
- HTTP route: `DELETE /api/v2.0/users/delete`
- Source controller: `IncidentIQ API`

Delete users by ID list

Permanently deletes multiple users by providing an array of user IDs.

**Use Cases**:
- Bulk offboarding of terminated employees
- Mass cleanup of graduated students
- Removing batch-imported test accounts

**Warning**: This action is permanent. All specified user accounts will be removed.

**Request Body**: Array of user UUIDs to delete.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | Array of user IDs to delete. |

#### Returns

- Typed call return: `ListDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_users_by_query_v2`

Provenance: Golden OpenAPI contract

Operation ID: `deleteUsersByQueryV2`

- Sync: `client.users.delete_users_by_query_v2(body=None, timeout=None)`
- Async: `await client.users.delete_users_by_query_v2(body=None, timeout=None)`
- Raw payload: `client.users.delete_users_by_query_v2.raw(body=None, timeout=None)`
- HTTP route: `DELETE /api/v2.0/users/delete/list`
- Source controller: `IncidentIQ API`

Delete users by query filter

Permanently deletes users matching the specified filter criteria. This is a powerful bulk operation that should be used with caution.

**Use Cases**:
- Delete all users matching specific role criteria
- Remove users from a specific location after school closure
- Cleanup users by employment status

**Warning**: This action is permanent and can affect many users. Always preview the affected users first using [POST /api/v2.0/users/get/list](#/Users/searchUsers) with the same filters before executing the delete.

**Supported Filters**:
- All standard user search filters (role, location, status, etc.)
- Use the `Filters` array with `Facet` and `Values` to specify criteria

**Safety Recommendation**: First call the GET/list endpoint with identical filters to verify which users will be affected before executing this delete operation.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `GetUsersRequestV1` | `GetUsersRequestV1` | Filter criteria to identify users to delete. Uses the same filter structure as the user search endpoint. |

#### Returns

- Typed call return: `ListDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_all_users`

Provenance: Golden OpenAPI contract

Operation ID: `getAllUsers`

- Sync: `client.users.get_all_users(p=None, s=None, body=None, timeout=None)`
- Async: `await client.users.get_all_users(p=None, s=None, body=None, timeout=None)`
- Raw payload: `client.users.get_all_users.raw(p=None, s=None, body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/users/all`
- Source controller: `IncidentIQ API`

Search all users including deleted

Returns a paginated list of users including soft-deleted records. Use this endpoint for audits or to locate accounts that can be restored.

**Prerequisites**
1. **RoleId** (optional filters) - Use [GET /api/v1.0/roles](#/Roles/listRoles) to list roles.
2. **LocationId** (optional filters) - Use [GET /api/v1.0/locations/view](#/Locations/getAllSiteLocationsV2) to list locations.
3. **TeamId** (optional filters) - Use [GET /api/v1.0/teams](#/Teams/listTeams) to list teams.

**Workflow Example**
1. (Optional) Gather filter ids from roles/locations/teams.
2. Call [POST /api/v1.0/users/all](#/Users/getAllUsers) with Filters to include deleted accounts.
3. If a user should be restored, call [PUT /api/v1.0/users/{UserId}/undelete](#/Users/undeleteUser).

**Minimal Required Fields**: None. Filters are optional; `IncludeDeleted` is applied automatically.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index. |
| `s` | `$s` | `query` | `no` | `int` | `-` | Page size. |
| `body` | `body` | `body` | `no` | `GetUsersRequestV1` | `GetUsersRequestV1` | - |

#### Returns

- Typed call return: `UsersListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UsersListGetResponse`
- Pagination helper: `client.users.get_all_users.iter_pages(start_page=1, page_size=100, max_pages=None, p=None, s=None, body=None, timeout=None)`

---

### `get_available_shortcuts`

Provenance: Golden OpenAPI contract

Operation ID: `getAvailableShortcuts`

- Sync: `client.users.get_available_shortcuts(timeout=None)`
- Async: `await client.users.get_available_shortcuts(timeout=None)`
- Raw payload: `client.users.get_available_shortcuts.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/users/shortcuts/available`
- Source controller: `IncidentIQ API`

Get available shortcuts

Retrieves all rule-based shortcuts available to the authenticated user based on their scope (user, role, team, site, or global). Shortcuts are configurations that link to saved filter sets and rules for quick access to filtered entity views.

**Workflow Example**
1. GET this endpoint to retrieve all available shortcuts
2. Display shortcuts in user's navigation menu
3. Use ShortcutId from response for update/delete operations

**Use Cases**:
- Populate user's shortcut navigation menu
- List shortcuts for management UI
- Identify ShortcutIds before update/delete operations

**Response Fields**: ShortcutId, OwnerId, Name, Scope (User/Role/Team/Site/App/Global/System/All), RuleId, ForEntityTypeId, Snippet, FilterSetId

**Notes**: No parameters required. Returns all shortcuts the user can access based on their roles, teams, and location. Scope determines visibility: User (personal), Role (role members), Team (team members), Site (site-wide), Global (all sites), System (built-in).

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `ShortcutsListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ShortcutsListGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_current_user_locations_filtered_v2`

Provenance: Golden OpenAPI contract

Operation ID: `getCurrentUserLocationsFilteredV2`

- Sync: `client.users.get_current_user_locations_filtered_v2(site_id=None, body=None, timeout=None)`
- Async: `await client.users.get_current_user_locations_filtered_v2(site_id=None, body=None, timeout=None)`
- Raw payload: `client.users.get_current_user_locations_filtered_v2.raw(site_id=None, body=None, timeout=None)`
- HTTP route: `POST /api/v2.0/users/my/locations`
- Source controller: `IncidentIQ API`

Get current user locations (filtered)

Returns locations accessible to the currently authenticated user with advanced filtering via request body. Use this when you need to filter by location type, permissions, or pagination beyond query parameters.

**Workflow Example**
1. Build a `GetUserLocationsRequest` with filters and paging.
2. Submit: [POST /api/v2.0/users/my/locations](#/Locations/getCurrentUserLocationsFilteredV2).
3. Use the returned list to render location selectors or permission-aware views.

**Minimal Required Fields**: None. Filters are optional.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |
| `body` | `body` | `body` | `no` | `GetUserLocationsRequest` | `GetUserLocationsRequest` | - |

#### Returns

- Typed call return: `LocationWithPermissionListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `LocationWithPermissionListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_current_user_locations_v2`

Provenance: Golden OpenAPI contract

Operation ID: `getCurrentUserLocationsV2`

- Sync: `client.users.get_current_user_locations_v2(site_id=None, p=None, s=None, timeout=None)`
- Async: `await client.users.get_current_user_locations_v2(site_id=None, p=None, s=None, timeout=None)`
- Raw payload: `client.users.get_current_user_locations_v2.raw(site_id=None, p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v2.0/users/my/locations`
- Source controller: `IncidentIQ API`

Get current user locations

Returns locations accessible to the currently authenticated user. This is a convenience alias that uses the authenticated user's ID automatically.

**Equivalent to:** [GET /api/v2.0/users/{UserId}/locations](#/Locations/getUserLocationsV2) (using the current user's ID)

**Related Endpoints:**
- [GET /api/v2.0/locations](#/Locations/getMyLocationsV2) - Same result via different path
- [GET /api/v2.0/users/{UserId}/locations](#/Locations/getUserLocationsV2) - Explicit user ID version

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index |
| `s` | `$s` | `query` | `no` | `int` | `-` | Page size |

#### Returns

- Typed call return: `LocationWithPermissionListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `LocationWithPermissionListResponse`
- Pagination helper: `client.users.get_current_user_locations_v2.iter_pages(start_page=1, page_size=100, max_pages=None, site_id=None, p=None, s=None, timeout=None)`

---

### `get_current_user_locations_view_filtered_v2`

Provenance: Golden OpenAPI contract

Operation ID: `getCurrentUserLocationsViewFilteredV2`

- Sync: `client.users.get_current_user_locations_view_filtered_v2(site_id=None, body=None, timeout=None)`
- Async: `await client.users.get_current_user_locations_view_filtered_v2(site_id=None, body=None, timeout=None)`
- Raw payload: `client.users.get_current_user_locations_view_filtered_v2.raw(site_id=None, body=None, timeout=None)`
- HTTP route: `POST /api/v2.0/users/my/locations/view`
- Source controller: `IncidentIQ API`

Get current user locations (view, filtered)

Alias for [POST /api/v2.0/users/my/locations](#/Locations/getCurrentUserLocationsFilteredV2). Returns locations with view-specific formatting and advanced filtering.

**Workflow Example**
1. Build a `GetUserLocationsRequest` with filters and paging.
2. Submit: [POST /api/v2.0/users/my/locations/view](#/Locations/getCurrentUserLocationsViewFilteredV2).
3. Use the returned list for view-based location selection.

**Minimal Required Fields**: None. Filters are optional.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |
| `body` | `body` | `body` | `no` | `GetUserLocationsRequest` | `GetUserLocationsRequest` | - |

#### Returns

- Typed call return: `LocationWithPermissionListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `LocationWithPermissionListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_current_user_locations_view_v2`

Provenance: Golden OpenAPI contract

Operation ID: `getCurrentUserLocationsViewV2`

- Sync: `client.users.get_current_user_locations_view_v2(site_id=None, p=None, s=None, timeout=None)`
- Async: `await client.users.get_current_user_locations_view_v2(site_id=None, p=None, s=None, timeout=None)`
- Raw payload: `client.users.get_current_user_locations_view_v2.raw(site_id=None, p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v2.0/users/my/locations/view`
- Source controller: `IncidentIQ API`

Get current user locations (view)

Alias for [GET /api/v2.0/users/my/locations](#/Locations/getCurrentUserLocationsV2). Returns the authenticated user's locations with permission flags in view format.

**Workflow Example**
1. Call [GET /api/v2.0/users/my/locations/view](#/Locations/getCurrentUserLocationsViewV2) with optional paging.
2. Use the response to populate read-only location lists or views.

**Minimal Required Fields**: None. Optional paging via `$p`/`$s`.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index |
| `s` | `$s` | `query` | `no` | `int` | `-` | Page size |

#### Returns

- Typed call return: `LocationWithPermissionListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `LocationWithPermissionListResponse`
- Pagination helper: `client.users.get_current_user_locations_view_v2.iter_pages(start_page=1, page_size=100, max_pages=None, site_id=None, p=None, s=None, timeout=None)`

---

### `get_intercom_jwt`

Provenance: Golden OpenAPI contract

Operation ID: `getIntercomJwt`

- Sync: `client.users.get_intercom_jwt(timeout=None)`
- Async: `await client.users.get_intercom_jwt(timeout=None)`
- Raw payload: `client.users.get_intercom_jwt.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/users/intercom/jwt`
- Source controller: `IncidentIQ API`

Generate Intercom JWT token and boot data

Generates a JWT token and Intercom boot data for the authenticated user. This endpoint is used to establish secure, authenticated sessions with Intercom's messaging platform. The response includes a HS256-signed JWT token along with complete user and company attributes needed for Intercom integration.

**Security Requirements**: Requires authenticated user session or app authorization.

**JWT Token Details**: The returned JWT token is a HS256-signed credential containing:
- `iss`: Issuer claim ("spark-services")
- `sub`: Subject claim (User ID)
- `iat`: Issued-at timestamp
- `exp`: Expiration timestamp (typically 1 hour)
- `user_id`: User ID claim for identity verification

The `Token` field should be passed as the user_hash parameter in Intercom.boot() calls.

**Usage Workflow**:
1. Call this endpoint to retrieve the JWT token and user/company attributes
2. Pass the Token as `user_hash` to Intercom.boot()
3. Include UserAttributes and CompanyAttributes in the Intercom boot configuration
4. The token includes an expiration time; generate a new token if needed for long-lived sessions

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `IntercomBootDataGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `IntercomBootDataGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_my_options`

Provenance: Golden OpenAPI contract

Operation ID: `getMyOptions`

- Sync: `client.users.get_my_options(timeout=None)`
- Async: `await client.users.get_my_options(timeout=None)`
- Raw payload: `client.users.get_my_options.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/users/my/options`
- Source controller: `IncidentIQ API`

Get current user's options/preferences

Retrieves the authenticated user's personal options and preferences, including notification settings, UI preferences, and feature flags. This is a convenience endpoint equivalent to [GET /api/v1.0/users/{UserId}/options](#/Users/getUserOptions) but automatically uses the authenticated user's ID.

**Use Cases**:
- Load user preferences at application startup
- Display current notification settings in a settings page
- Check feature flags for the current user

**Notes**: No parameters required. Uses the authenticated user's identity from the bearer token.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `UserOptionsGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UserOptionsGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_my_shortcuts`

Provenance: Golden OpenAPI contract

Operation ID: `getMyShortcuts`

- Sync: `client.users.get_my_shortcuts(timeout=None)`
- Async: `await client.users.get_my_shortcuts(timeout=None)`
- Raw payload: `client.users.get_my_shortcuts.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/users/my/shortcuts`
- Source controller: `IncidentIQ API`

Get current user's shortcuts

Retrieves the list of navigation shortcuts configured for the authenticated user. This is a convenience endpoint equivalent to [GET /api/v1.0/users/{UserId}/shortcuts](#/Users/getUserShortcuts) but automatically uses the authenticated user's ID.

**Use Cases**:
- Load user's shortcuts at application startup
- Populate quick navigation menu
- Display shortcuts in user's profile settings

**Notes**: No parameters required. Uses the authenticated user's identity from the bearer token. For all available shortcuts (including shared and system), use [GET /api/v1.0/users/shortcuts/available](#/Users/getAvailableShortcuts).

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `ShortcutsListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ShortcutsListGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_my_students_with_tickets`

Provenance: Golden OpenAPI contract

Operation ID: `getMyStudentsWithTickets`

- Sync: `client.users.get_my_students_with_tickets(timeout=None)`
- Async: `await client.users.get_my_students_with_tickets(timeout=None)`
- Raw payload: `client.users.get_my_students_with_tickets.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/users/my/students/with/tickets`
- Source controller: `IncidentIQ API`

Get students I've submitted tickets for

Retrieves the students associated with tickets created by the authenticated user, returning a deduplicated list of student profiles tied to that user's requestor history. This is commonly used in guardian/teacher portals to quickly pick a student when filing a new ticket or reviewing prior interactions.

**Workflow Example**
1. Call [GET /api/v1.0/users/my/students/with/tickets](#/Users/getMyStudentsWithTickets) to retrieve the student list tied to the current user.
2. Use the returned `UserId` values when creating tickets on behalf of a student.

**Minimal Required Fields**: none.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `UsersListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UsersListGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_simple_user`

Provenance: Golden OpenAPI contract

Operation ID: `getSimpleUser`

- Sync: `client.users.get_simple_user(user_id=..., timeout=None)`
- Async: `await client.users.get_simple_user(user_id=..., timeout=None)`
- Raw payload: `client.users.get_simple_user.raw(user_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/users/simple/{UserId}`
- Source controller: `IncidentIQ API`

Get simplified user record

Returns a lightweight user record containing only essential fields (UserId, Name, Email, LocationId, RoleId). Use this endpoint when full user details are not needed to reduce payload size.

**Prerequisites**: This endpoint requires a UserId from:
- [POST /api/v1.0/users](#/Users/searchUsers) → Extract `Items[].UserId`

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | User identifier to retrieve. Obtain via [POST /api/v1.0/users](#/Users/searchUsers), extract `Items[].UserId`. |

#### Returns

- Typed call return: `SimpleUserGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `SimpleUserGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_site_system_user_id`

Provenance: Golden OpenAPI contract

Operation ID: `getSiteSystemUserId`

- Sync: `client.users.get_site_system_user_id(site_id=..., timeout=None)`
- Async: `await client.users.get_site_system_user_id(site_id=..., timeout=None)`
- Raw payload: `client.users.get_site_system_user_id.raw(site_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/users/system-user/{SiteId}`
- Source controller: `IncidentIQ API`

Get system user ID for a site

Returns the system user ID for the specified site. The system user is a special internal account used for automated actions, background processes, and system-generated activities.

**Prerequisites**
1. **SiteId** - Use [GET /api/v2.0/users/my/locations](#/Users/getCurrentUserLocationsV2) to list user locations. Extract `Items[].SiteId`.

**Workflow Example**
1. Identify site: [GET /api/v2.0/users/my/locations](#/Users/getCurrentUserLocationsV2) → extract SiteId
2. Get system user: GET this endpoint with SiteId
3. Use returned UserId for system-level operations

**Use Cases**:
- Identify actor for automated ticket creation
- Attribution for system-generated changes
- Exclude system actions from user activity reports
- Integration development requiring system context

**Notes**: Every site has exactly one system user. This account cannot log in interactively. Actions performed as system user are audited separately from human users.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `site_id` | `SiteId` | `path` | `yes` | `str` | `-` | Site identifier. |

#### Returns

- Typed call return: `GuidGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `GuidGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_user_achievements`

Provenance: Golden OpenAPI contract

Operation ID: `getUserAchievements`

- Sync: `client.users.get_user_achievements(user_id=..., timeout=None)`
- Async: `await client.users.get_user_achievements(user_id=..., timeout=None)`
- Raw payload: `client.users.get_user_achievements.raw(user_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/users/{UserId}/achievements`
- Source controller: `IncidentIQ API`

Get user achievements

Retrieves the list of achievements earned by a specific user. Use this to display badges, recognize milestones, or drive gamification features in user profiles.

**Prerequisites**
1. **UserId** - Use [POST /api/v1.0/users](#/Users/searchUsers) to locate the user. Extract `Items[].UserId`.

**Workflow Example**
1. Search for the user: [POST /api/v1.0/users](#/Users/searchUsers) → extract UserId.
2. Fetch achievements: [GET /api/v1.0/users/{UserId}/achievements](#/Users/getUserAchievements).
3. Use returned AchievementId values when calling [POST /api/v1.0/users/{UserId}/achievements/award/{AchievementId}](#/Users/awardAchievement).

**Minimal Required Fields**: UserId (path)

**Notes**: Returns an empty list if the user has not earned any achievements yet.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | UUID of the user whose achievements to retrieve Obtain via [POST /api/v1.0/users](#/Users/searchUsers), extract `Items[].UserId`. |

#### Returns

- Typed call return: `AchievementsListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AchievementsListGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_user_activities`

Provenance: Golden OpenAPI contract

Operation ID: `getUserActivities`

- Sync: `client.users.get_user_activities(user_id=..., p=None, s=None, timeout=None)`
- Async: `await client.users.get_user_activities(user_id=..., p=None, s=None, timeout=None)`
- Raw payload: `client.users.get_user_activities.raw(user_id=..., p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v1.0/users/{UserId}/activities`
- Source controller: `IncidentIQ API`

Get user activity timeline

**Prerequisites**: This endpoint requires UUIDs from other API calls:
1. **UserId** - Use [POST /api/v1.0/users](#/Users/searchUsers) → Extract `Items[].UserId`

**Workflow Example**:
1. Search for user: [POST /api/v1.0/users](#/Users/searchUsers)
2. Extract UserId from response
3. [GET /api/v1.0/users/{UserId}/activities](#/Users/getUserActivities)

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | User identifier. |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index to retrieve |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of records per page |

#### Returns

- Typed call return: `UserActivitiesListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UserActivitiesListGetResponse`
- Pagination helper: `client.users.get_user_activities.iter_pages(start_page=1, page_size=100, max_pages=None, user_id=..., p=None, s=None, timeout=None)`

---

### `get_user_at_associated_site`

Provenance: Golden OpenAPI contract

Operation ID: `getUserAtAssociatedSite`

- Sync: `client.users.get_user_at_associated_site(site_id=..., email_address=..., external_id=..., timeout=None)`
- Async: `await client.users.get_user_at_associated_site(site_id=..., email_address=..., external_id=..., timeout=None)`
- Raw payload: `client.users.get_user_at_associated_site.raw(site_id=..., email_address=..., external_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/users/at-associated-site/{SiteId}/{EmailAddress}/{ExternalId}`
- Source controller: `IncidentIQ API`

Get user at associated site

Retrieves a user by email address and external ID at a specific associated site. Used for cross-site user lookups in multi-tenant or federated district environments.

**Prerequisites**
1. **SiteId** - Use [GET /api/v2.0/users/my/locations](#/Users/getCurrentUserLocationsV2) to list accessible locations. Extract `Items[].SiteId`.
2. **EmailAddress** - Known email address of the user to locate
3. **ExternalId** - External system identifier (e.g., SIS ID, AD GUID)

**Workflow Example**
1. List sites: [GET /api/v2.0/users/my/locations](#/Users/getCurrentUserLocationsV2) → extract target SiteId
2. Lookup user: POST this endpoint with SiteId, EmailAddress, and ExternalId

**Use Cases**:
- SSO user provisioning across federated sites
- Cross-district user synchronization
- External system integration with user matching

**Notes**: All three path parameters are required. Returns full user details if found, 404 if no match.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `site_id` | `SiteId` | `path` | `yes` | `str` | `-` | UUID of the site to search |
| `email_address` | `EmailAddress` | `path` | `yes` | `str` | `-` | Email address to search for |
| `external_id` | `ExternalId` | `path` | `yes` | `str` | `-` | External system identifier |

#### Returns

- Typed call return: `UserDetailGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UserDetailGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_user_by_email`

Provenance: Golden OpenAPI contract

Operation ID: `getUserByEmail`

- Sync: `client.users.get_user_by_email(site_id=..., email_address=..., timeout=None)`
- Async: `await client.users.get_user_by_email(site_id=..., email_address=..., timeout=None)`
- Raw payload: `client.users.get_user_by_email.raw(site_id=..., email_address=..., timeout=None)`
- HTTP route: `GET /api/v1.0/users/by-email/{SiteId}/{EmailAddress}`
- Source controller: `IncidentIQ API`

Get user by email address

Retrieves complete user details by their email address within a specific site context. Email lookups are case-insensitive and match against the user's primary email field.

**Prerequisites**
1. **SiteId** - Use [GET /api/v2.0/users/my/locations](#/Users/getCurrentUserLocationsV2) to list accessible locations. Extract `Items[].SiteId`.
2. **EmailAddress** - The email address to search for

**Workflow Example**
1. Identify site: [GET /api/v2.0/users/my/locations](#/Users/getCurrentUserLocationsV2) → extract SiteId
2. Lookup user: GET this endpoint with SiteId and EmailAddress

**Use Cases**:
- User discovery during ticket submission ("For" user lookup)
- Email-based user validation for notifications
- User deduplication checks before account creation

**Notes**: Returns 404 if no user exists with the specified email in the site. For username-based lookups, use [GET /api/v1.0/users/by-username/{SiteId}/{Username}](#/Users/getUserByUsername).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `site_id` | `SiteId` | `path` | `yes` | `str` | `-` | Site identifier to scope the email lookup. |
| `email_address` | `EmailAddress` | `path` | `yes` | `str` | `-` | Email address to search for. |

#### Returns

- Typed call return: `UserDetailGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UserDetailGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_user_by_external_email`

Provenance: Golden OpenAPI contract

Operation ID: `getUserByExternalEmail`

- Sync: `client.users.get_user_by_external_email(body=..., timeout=None)`
- Async: `await client.users.get_user_by_external_email(body=..., timeout=None)`
- Raw payload: `client.users.get_user_by_external_email.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/users/external`
- Source controller: `IncidentIQ API`

Get user by external email

Retrieves a user by their external email address, typically used for users created through external systems like SIS imports, LDAP sync, or third-party integrations. Searches across external identity providers.

**Workflow Example**
1. Prepare request: Include the external email address in the request body
2. Lookup user: POST this endpoint with email
3. Receive full user details if found

**Use Cases**:
- SSO integration user matching
- SIS (Student Information System) user synchronization
- External ticketing system user lookup
- LDAP/Active Directory user resolution

**Minimal Required Fields**: EmailAddress

**Notes**: Searches external email fields which may differ from the primary IncidentIQ email. Returns 404 if no matching user found. For primary email lookups, use [GET /api/v1.0/users/by-email](#/Users/getUserByEmail).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `GetUserByEmailRequest` | `GetUserByEmailRequest` | - |

#### Returns

- Typed call return: `UserDetailGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UserDetailGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_user_by_id`

Provenance: Golden OpenAPI contract

Operation ID: `getUserById`

- Sync: `client.users.get_user_by_id(user_id=..., site_id=None, product_id=None, timeout=None)`
- Async: `await client.users.get_user_by_id(user_id=..., site_id=None, product_id=None, timeout=None)`
- Raw payload: `client.users.get_user_by_id.raw(user_id=..., site_id=None, product_id=None, timeout=None)`
- HTTP route: `GET /api/v1.0/users/{UserId}`
- Source controller: `IncidentIQ API`

Retrieve user by identifier

**Prerequisites**: This endpoint requires UUIDs from other API calls:
1. **UserId** - Use [POST /api/v1.0/users](#/Users/searchUsers) → Extract `Items[].UserId`

**Workflow Example**:
1. Search for user: [POST /api/v1.0/users](#/Users/searchUsers)
2. Extract UserId from response
3. Call this endpoint with the UserId

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | User identifier. |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Overrides the default Site context when supplied |
| `product_id` | `ProductId` | `header` | `no` | `str` | `-` | Overrides the default Product context when supplied |

#### Returns

- Typed call return: `UserDetailGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UserDetailGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_user_by_username`

Provenance: Golden OpenAPI contract

Operation ID: `getUserByUsername`

- Sync: `client.users.get_user_by_username(site_id=..., username=..., timeout=None)`
- Async: `await client.users.get_user_by_username(site_id=..., username=..., timeout=None)`
- Raw payload: `client.users.get_user_by_username.raw(site_id=..., username=..., timeout=None)`
- HTTP route: `GET /api/v1.0/users/by-username/{SiteId}/{Username}`
- Source controller: `IncidentIQ API`

Get user by username

Retrieves complete user details by their username within a specific site context. Username lookups are case-insensitive and support both standard usernames and email-style usernames.

**Prerequisites**
1. **SiteId** - Use [GET /api/v2.0/users/my/locations](#/Users/getCurrentUserLocationsV2) to list accessible locations. Extract `Items[].SiteId`.
2. **Username** - The login username (often email address) for the user

**Workflow Example**
1. Identify site: [GET /api/v2.0/users/my/locations](#/Users/getCurrentUserLocationsV2) → extract SiteId
2. Lookup user: GET this endpoint with SiteId and Username

**Use Cases**:
- User lookup during SSO authentication flows
- Username validation during account creation
- User profile retrieval by login identifier

**Notes**: Returns 404 if no user exists with the specified username in the site. For email-based lookups, use [GET /api/v1.0/users/by-email/{SiteId}/{EmailAddress}](#/Users/getUserByEmail).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `site_id` | `SiteId` | `path` | `yes` | `str` | `-` | Site identifier to scope the username lookup. |
| `username` | `Username` | `path` | `yes` | `str` | `-` | Username to search for. |

#### Returns

- Typed call return: `UserDetailGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UserDetailGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_user_ids_for_filter_sets`

Provenance: Golden OpenAPI contract

Operation ID: `getUserIdsForFilterSets`

- Sync: `client.users.get_user_ids_for_filter_sets(body=..., timeout=None)`
- Async: `await client.users.get_user_ids_for_filter_sets(body=..., timeout=None)`
- Raw payload: `client.users.get_user_ids_for_filter_sets.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/users/ids/for/filtersets`
- Source controller: `IncidentIQ API`

Get user IDs matching filter sets

Returns user IDs that match the specified filter set criteria. Enables building dynamic user lists based on complex filter combinations without retrieving full user records.

**Workflow Example**
1. Define filter criteria: location, role, team, custom fields, etc.
2. POST this endpoint with FilterSets array
3. Receive list of matching UserIds for bulk operations

**Use Cases**:
- Pre-filtering users before bulk operations
- Building notification recipient lists
- Dynamic group membership calculation
- Export or reporting user selection

**Minimal Required Fields**: FilterSets (array of filter definitions)

**Notes**: Returns only UserIds for performance. Use returned IDs with bulk endpoints or [GET /api/v1.0/users/{UserId}](#/Users/getUserById) for full details. Supports AND/OR logic within filter sets.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `GetIdsForFilterSetRequest` | `GetIdsForFilterSetRequest` | - |

#### Returns

- Typed call return: `IdsForFilterSetsListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `IdsForFilterSetsListGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_user_locations_filtered_v2`

Provenance: Golden OpenAPI contract

Operation ID: `getUserLocationsFilteredV2`

- Sync: `client.users.get_user_locations_filtered_v2(user_id=..., site_id=None, body=None, timeout=None)`
- Async: `await client.users.get_user_locations_filtered_v2(user_id=..., site_id=None, body=None, timeout=None)`
- Raw payload: `client.users.get_user_locations_filtered_v2.raw(user_id=..., site_id=None, body=None, timeout=None)`
- HTTP route: `POST /api/v2.0/users/{UserId}/locations`
- Source controller: `IncidentIQ API`

Get user locations (filtered)

Returns locations accessible to a specific user with advanced filtering via request body. Use this to build permission-aware location lists for another user (for example, an admin viewing a user's access).

**Prerequisites**
1. **UserId** - Use [POST /api/v1.0/users](#/Users/searchUsers) and extract `Items[].UserId`.

**Workflow Example**
1. Identify the target user ID.
2. Build a `GetUserLocationsRequest` with filters and paging.
3. Submit: [POST /api/v2.0/users/{UserId}/locations](#/Locations/getUserLocationsFilteredV2).

**Minimal Required Fields**: UserId (path). Filters are optional.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | Unique identifier of the user |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |
| `body` | `body` | `body` | `no` | `GetUserLocationsRequest` | `GetUserLocationsRequest` | - |

#### Returns

- Typed call return: `LocationWithPermissionListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `LocationWithPermissionListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_user_locations_v2`

Provenance: Golden OpenAPI contract

Operation ID: `getUserLocationsV2`

- Sync: `client.users.get_user_locations_v2(user_id=..., site_id=None, p=None, s=None, timeout=None)`
- Async: `await client.users.get_user_locations_v2(user_id=..., site_id=None, p=None, s=None, timeout=None)`
- Raw payload: `client.users.get_user_locations_v2.raw(user_id=..., site_id=None, p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v2.0/users/{UserId}/locations`
- Source controller: `IncidentIQ API`

Get user locations

Returns locations accessible to a specific user, including their effective permissions for each location.

**Supports Custom Filters:** This endpoint accepts filter parameters.

**Related Endpoints:**
- [GET /api/v2.0/users/my/locations](#/Locations/getCurrentUserLocationsV2) - Current user's locations
- [GET /api/v2.0/users/{UserId}/locations/view](#/Locations/getUserLocationsViewV2) - Alias endpoint

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | Unique identifier of the user whose locations to retrieve |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index |
| `s` | `$s` | `query` | `no` | `int` | `-` | Page size |

#### Returns

- Typed call return: `LocationWithPermissionListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `LocationWithPermissionListResponse`
- Pagination helper: `client.users.get_user_locations_v2.iter_pages(start_page=1, page_size=100, max_pages=None, user_id=..., site_id=None, p=None, s=None, timeout=None)`

---

### `get_user_locations_view_filtered_v2`

Provenance: Golden OpenAPI contract

Operation ID: `getUserLocationsViewFilteredV2`

- Sync: `client.users.get_user_locations_view_filtered_v2(user_id=..., site_id=None, body=None, timeout=None)`
- Async: `await client.users.get_user_locations_view_filtered_v2(user_id=..., site_id=None, body=None, timeout=None)`
- Raw payload: `client.users.get_user_locations_view_filtered_v2.raw(user_id=..., site_id=None, body=None, timeout=None)`
- HTTP route: `POST /api/v2.0/users/{UserId}/locations/view`
- Source controller: `IncidentIQ API`

Get user locations (view, filtered)

Alias for [POST /api/v2.0/users/{UserId}/locations](#/Locations/getUserLocationsFilteredV2). Returns locations with filtering and view formatting for the specified user.

**Prerequisites**
1. **UserId** - Use [POST /api/v1.0/users](#/Users/searchUsers) and extract `Items[].UserId`.

**Workflow Example**
1. Build a `GetUserLocationsRequest` with filters and paging.
2. Submit: [POST /api/v2.0/users/{UserId}/locations/view](#/Locations/getUserLocationsViewFilteredV2).
3. Use the response for admin review or user access auditing.

**Minimal Required Fields**: UserId (path). Filters are optional.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | Unique identifier of the user |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |
| `body` | `body` | `body` | `no` | `GetUserLocationsRequest` | `GetUserLocationsRequest` | - |

#### Returns

- Typed call return: `LocationWithPermissionListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `LocationWithPermissionListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_user_locations_view_v2`

Provenance: Golden OpenAPI contract

Operation ID: `getUserLocationsViewV2`

- Sync: `client.users.get_user_locations_view_v2(user_id=..., site_id=None, p=None, s=None, timeout=None)`
- Async: `await client.users.get_user_locations_view_v2(user_id=..., site_id=None, p=None, s=None, timeout=None)`
- Raw payload: `client.users.get_user_locations_view_v2.raw(user_id=..., site_id=None, p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v2.0/users/{UserId}/locations/view`
- Source controller: `IncidentIQ API`

Get user locations (view)

Alias for [GET /api/v2.0/users/{UserId}/locations](#/Locations/getUserLocationsV2). Returns the specified user's locations with permission metadata in view format.

**Prerequisites**
1. **UserId** - Use [POST /api/v1.0/users](#/Users/searchUsers) and extract `Items[].UserId`.

**Workflow Example**
1. Identify the user ID.
2. Call [GET /api/v2.0/users/{UserId}/locations/view](#/Locations/getUserLocationsViewV2).
3. Use the response to display location access for the user.

**Minimal Required Fields**: UserId (path). Optional paging via `$p`/`$s`.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | Unique identifier of the user |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index |
| `s` | `$s` | `query` | `no` | `int` | `-` | Page size |

#### Returns

- Typed call return: `LocationWithPermissionListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `LocationWithPermissionListResponse`
- Pagination helper: `client.users.get_user_locations_view_v2.iter_pages(start_page=1, page_size=100, max_pages=None, user_id=..., site_id=None, p=None, s=None, timeout=None)`

---

### `get_user_options`

Provenance: Golden OpenAPI contract

Operation ID: `getUserOptions`

- Sync: `client.users.get_user_options(user_id=..., timeout=None)`
- Async: `await client.users.get_user_options(user_id=..., timeout=None)`
- Raw payload: `client.users.get_user_options.raw(user_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/users/{UserId}/options`
- Source controller: `IncidentIQ API`

Get user options/preferences

Retrieves the user's personal options and preferences, including notification settings, UI preferences, and feature flags.

**Prerequisites**
1. **UserId** - Use [POST /api/v1.0/users](#/Users/searchUsers) to locate the user and extract `Items[].UserId`.

**Workflow Example**
1. Find the user: [POST /api/v1.0/users](#/Users/searchUsers) -> capture UserId.
2. Call [GET /api/v1.0/users/{UserId}/options](#/Users/getUserOptions) to retrieve current settings.
3. Update settings (if needed) via [POST /api/v1.0/users/{UserId}/options](#/Users/setUserOptions).

**Minimal Required Fields**: UserId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | User identifier. Obtain via [POST /api/v1.0/users](#/Users/searchUsers), extract `Items[].UserId`. |

#### Returns

- Typed call return: `UserOptionsGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UserOptionsGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_user_relationships`

Provenance: Golden OpenAPI contract

Operation ID: `getUserRelationships`

- Sync: `client.users.get_user_relationships(user_id=..., timeout=None)`
- Async: `await client.users.get_user_relationships(user_id=..., timeout=None)`
- Raw payload: `client.users.get_user_relationships.raw(user_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/users/{UserId}/relationships`
- Source controller: `IncidentIQ API`

Get user relationships (guardians/students)

Retrieves the list of relationships for a user, including guardian (parent) and student (child) associations. This endpoint is essential for workflows that need to identify guardians for a student or students for a guardian.

**Relationship Types**:
- **Parent**: The related user is a guardian/parent of the queried user (queried user is a student)
- **Child**: The related user is a student/child of the queried user (queried user is a guardian)
- **None**: No specific relationship type defined

**Use Case: Adding Guardians as Ticket Followers**

To automatically add guardians as followers on student tickets:
1. When a ticket is created for a student, get the student's `UserId` from the ticket's `ForId` field
2. Call this endpoint with the student's `UserId` to retrieve their guardian relationships
3. Filter for relationships where `RelationshipType` = "Parent"
4. Extract the `RelatedUserId` values (guardian user IDs)
5. Update the ticket using [POST /api/v1.0/tickets/{ticketId}](#/Tickets/updateTicket) with `TicketFollowerUserIds` containing the guardian IDs and `UpdateTicketFollowers: true`

**Workflow Example**:
```
1. Ticket created for student (ForId: "student-uuid")
2. [GET /api/v1.0/users/{student-uuid}/relationships](#/Users/getUserRelationships)
   → Returns [{RelatedUserId: "guardian-uuid", RelationshipType: "Parent"}]
3. [POST /api/v1.0/tickets/{ticketId}](#/Tickets/updateTicket)
   Body: {
     "TicketFollowerUserIds": ["guardian-uuid"],
     "UpdateTicketFollowers": true
   }
```

**Note**: This endpoint returns relationships for a specific user by UserId. There is no equivalent endpoint for the authenticated user's relationships.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | UUID of the user whose relationships to retrieve. Can be a student (to find guardians) or a guardian (to find students). |

#### Returns

- Typed call return: `UserRelationshipsListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UserRelationshipsListGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_user_rooms`

Provenance: Golden OpenAPI contract

Operation ID: `getUserRooms`

- Sync: `client.users.get_user_rooms(user_id=..., p=None, s=None, timeout=None)`
- Async: `await client.users.get_user_rooms(user_id=..., p=None, s=None, timeout=None)`
- Raw payload: `client.users.get_user_rooms.raw(user_id=..., p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v1.0/users/{UserId}/rooms`
- Source controller: `IncidentIQ API`

Get user's assigned rooms

Retrieves the list of location rooms assigned to a user. Rooms represent physical spaces (classrooms, offices, labs) that the user is associated with for ticket routing and reporting.

**Prerequisites**
1. **UserId** - Use [POST /api/v1.0/users](#/Users/searchUsers) to locate the user. Extract `Items[].UserId`.

**Workflow Example**
1. Search for the user: [POST /api/v1.0/users](#/Users/searchUsers) → extract UserId.
2. Call [GET /api/v1.0/users/{UserId}/rooms](#/Users/getUserRooms) to retrieve assigned rooms.
3. Use returned LocationRoomId values for add/remove operations.

**Minimal Required Fields**: UserId (path)

**Notes**: Results are paged via `$p` and `$s` query parameters. For bulk room lookups across many users, use [POST /api/v1.0/users/rooms/get](#/Users/getUserRoomsBulk).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | User identifier. Obtain via [POST /api/v1.0/users](#/Users/searchUsers), extract `Items[].UserId`. |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index. |
| `s` | `$s` | `query` | `no` | `int` | `-` | Page size. |

#### Returns

- Typed call return: `LocationRoomsListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `LocationRoomsListGetResponse`
- Pagination helper: `client.users.get_user_rooms.iter_pages(start_page=1, page_size=100, max_pages=None, user_id=..., p=None, s=None, timeout=None)`

---

### `get_user_rooms_bulk`

Provenance: Golden OpenAPI contract

Operation ID: `getUserRoomsBulk`

- Sync: `client.users.get_user_rooms_bulk(timeout=None)`
- Async: `await client.users.get_user_rooms_bulk(timeout=None)`
- Raw payload: `client.users.get_user_rooms_bulk.raw(timeout=None)`
- HTTP route: `POST /api/v1.0/users/rooms/get`
- Source controller: `IncidentIQ API`

Get room assignments for users

Retrieves room assignments for multiple users based on filter criteria. Returns a list of user-to-room associations showing which physical spaces (classrooms, offices, labs) are assigned to which users.

**Workflow Example**
1. (Optional) Prepare filter criteria: UserIds, LocationIds, or search parameters
2. POST this endpoint with request body
3. Receive list of user-room associations with room details

**Use Cases**:
- Audit room assignments across multiple users
- Export room assignment reports
- Validate room coverage for locations
- Bulk room assignment verification before changes

**Notes**: Returns all matching user-room pairs. Use filter parameters to limit results. For single-user room lookups, see [GET /api/v1.0/users/{UserId}/rooms](#/Users/getUserRooms). To modify assignments, use POST/DELETE on /api/v1.0/users/{UserId}/rooms/{LocationRoomId}.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `UserRoomsListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UserRoomsListGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_user_shortcuts`

Provenance: Golden OpenAPI contract

Operation ID: `getUserShortcuts`

- Sync: `client.users.get_user_shortcuts(user_id=..., timeout=None)`
- Async: `await client.users.get_user_shortcuts(user_id=..., timeout=None)`
- Raw payload: `client.users.get_user_shortcuts.raw(user_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/users/{UserId}/shortcuts`
- Source controller: `IncidentIQ API`

Get user's shortcuts

Retrieves the list of navigation shortcuts configured for a specific user. Shortcuts provide quick access to frequently used views and filters.

**Prerequisites**
1. **UserId** - Use [POST /api/v1.0/users](#/Users/searchUsers) to locate the user and extract `Items[].UserId`.

**Workflow Example**
1. Find the user: [POST /api/v1.0/users](#/Users/searchUsers) -> capture UserId.
2. Call [GET /api/v1.0/users/{UserId}/shortcuts](#/Users/getUserShortcuts).
3. For the authenticated user, use [GET /api/v1.0/users/my/shortcuts](#/Users/getMyShortcuts).

**Minimal Required Fields**: UserId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | User identifier. Obtain via [POST /api/v1.0/users](#/Users/searchUsers), extract `Items[].UserId`. |

#### Returns

- Typed call return: `ShortcutsListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ShortcutsListGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_user_view`

Provenance: Golden OpenAPI contract

Operation ID: `getUserView`

- Sync: `client.users.get_user_view(view_id=..., timeout=None)`
- Async: `await client.users.get_user_view(view_id=..., timeout=None)`
- Raw payload: `client.users.get_user_view.raw(view_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/users/views/{viewId}`
- Source controller: `IncidentIQ API`

Get a specific user view

Retrieves a specific saved user view (filter configuration) by its unique identifier. User views store saved search criteria and column configurations for the users list interface.

**Prerequisites**
1. **viewId** - Use [GET /api/v1.0/users/views](#/Users/listUserViews) to list available views. Extract `Items[].ViewId` from the response.

**Workflow Example**
1. List user views: [GET /api/v1.0/users/views](#/Users/listUserViews) → identify target view.
2. Call this endpoint: [GET /api/v1.0/users/views/{viewId}](#/Views/getUserView) with the view UUID.
3. Use returned filter configuration to apply saved search criteria.

**Related Endpoints:**
- [DELETE /api/v1.0/users/views/{viewId}](#/Views/deleteUserById) - Delete this view
- [POST /api/v1.0/users/views/new](#/Views/createUserView) - Create a new view

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `view_id` | `viewId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `UserView`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UserView`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_users_for_my_classes`

Provenance: Golden OpenAPI contract

Operation ID: `getUsersForMyClasses`

- Sync: `client.users.get_users_for_my_classes(sis_class_id=..., body=..., timeout=None)`
- Async: `await client.users.get_users_for_my_classes(sis_class_id=..., body=..., timeout=None)`
- Raw payload: `client.users.get_users_for_my_classes.raw(sis_class_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/users/for/sisclass/{SisClassId}`
- Source controller: `IncidentIQ API`

Get users for my classes

Returns a list of users enrolled in a specific SIS class. This is a specialized variant of user search that bypasses location-based permission checks, specifically used for the 'My Classes' interface.

**Note**: This endpoint is marked obsolete and exists for backward compatibility. Use [POST /api/v1.0/users](#/Users/searchUsers) with a `sisclass` filter for standard search operations.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `sis_class_id` | `SisClassId` | `path` | `yes` | `str` | `-` | Unique identifier for the SIS class. |
| `body` | `body` | `body` | `yes` | `GetUsersRequestV1` | `GetUsersRequestV1` | - |

#### Returns

- Typed call return: `UsersListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UsersListGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_users_for_requestor_swap`

Provenance: Golden OpenAPI contract

Operation ID: `getUsersForRequestorSwap`

- Sync: `client.users.get_users_for_requestor_swap(body=None, timeout=None)`
- Async: `await client.users.get_users_for_requestor_swap(body=None, timeout=None)`
- Raw payload: `client.users.get_users_for_requestor_swap.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/users/requestor/swap`
- Source controller: `IncidentIQ API`

Search users for requestor swap

Searches for users eligible to be assigned as requestors in advanced deployment scenarios, returning only the users allowed for requestor reassignment. Use this when you need to swap the requestor on a ticket or asset deployment and want the same eligibility rules enforced by the UI.

**Workflow Example**
1. Submit filters or a source hint (for example `Source: "EditRequestor"`) to constrain the candidate list.
2. Read eligible users from the response and select the new `UserId` for the downstream requestor update.

**Minimal Required Fields**: none (filters optional).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `GetUsersRequestV1` | `GetUsersRequestV1` | - |

#### Returns

- Typed call return: `UsersListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UsersListGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_users_for_view`

Provenance: Golden OpenAPI contract

Operation ID: `getUsersForView`

- Sync: `client.users.get_users_for_view(view_id=..., body=None, timeout=None)`
- Async: `await client.users.get_users_for_view(view_id=..., body=None, timeout=None)`
- Raw payload: `client.users.get_users_for_view.raw(view_id=..., body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/users/view/{ViewId}`
- Source controller: `IncidentIQ API`

Get users matching a saved view

Retrieves users that match the criteria of a saved view. Views store reusable filter and sort configurations, making this endpoint ideal for dashboards and exports that need consistent user slices.

**Prerequisites**
1. **ViewId** - Use [GET /api/v1.0/users/views](#/Users/listUserViews) to list available views. Extract `Items[].ViewId`.

**Workflow Example**
1. List views: [GET /api/v1.0/users/views](#/Users/listUserViews) and select the desired ViewId.
2. Execute the view: POST this endpoint with the ViewId and optional paging settings in the request body.
3. Use the returned user list to populate UI grids or exports.

**Minimal Required Fields**: ViewId (path)

**Notes**: The request body is optional and can be used to control paging or execution options when supported by the view.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `view_id` | `ViewId` | `path` | `yes` | `str` | `-` | UUID of the saved view |
| `body` | `body` | `body` | `no` | `GetUsersForViewUsersViewByViewIdRequest` | `GetUsersForViewUsersViewByViewIdRequest` | - |

#### Returns

- Typed call return: `UsersListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UsersListGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_users_per_grade`

Provenance: Golden OpenAPI contract

Operation ID: `getUsersPerGrade`

- Sync: `client.users.get_users_per_grade(timeout=None)`
- Async: `await client.users.get_users_per_grade(timeout=None)`
- Raw payload: `client.users.get_users_per_grade.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/users/stats/grades`
- Source controller: `IncidentIQ API`

Get user count by grade level

Returns aggregate counts of users grouped by grade level (K-12, staff, etc.). Provides a quick summary of user distribution across educational grade levels.

**Workflow Example**
1. GET this endpoint to retrieve grade-level statistics
2. Process GradeLevel and UserCount for each grade
3. Use data for dashboards, device allocation, or enrollment reports

**Use Cases**:
- Student distribution dashboards by grade
- Device allocation planning by grade level
- Enrollment verification and compliance
- 1:1 device program tracking
- Student support staffing ratios

**Response Fields**: GradeLevel, UserCount for each grade

**Notes**: No parameters required. Counts include students and staff with assigned grade levels. Staff may appear under specific grade designations or "Staff" category. For location-based distribution, see [GET /api/v1.0/users/stats/locations](#/Users/getUsersPerLocation).

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `GradeStatsListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `GradeStatsListGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_users_per_location`

Provenance: Golden OpenAPI contract

Operation ID: `getUsersPerLocation`

- Sync: `client.users.get_users_per_location(timeout=None)`
- Async: `await client.users.get_users_per_location(timeout=None)`
- Raw payload: `client.users.get_users_per_location.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/users/stats/locations`
- Source controller: `IncidentIQ API`

Get location statistics

Returns aggregate statistics per location including ticket counts, asset counts, and user assignments. Provides a comprehensive snapshot of each location's operational metrics.

**Workflow Example**
1. GET this endpoint to retrieve location statistics
2. Process statistics for dashboards, capacity planning, or reports
3. Use `AssignedUsers` for user distribution analysis

**Use Cases**:
- Executive dashboards showing location workload distribution
- Capacity planning for IT support staffing per location
- Asset allocation analysis by location
- Ticket volume monitoring per location
- Inventory (Parts) tracking by location

**Response Fields**:
- `LocationId` - UUID of the location (nullable)
- `OpenTickets` - Number of currently open tickets
- `AvailableTickets` - Number of available/unassigned tickets
- `TotalTickets` - Total ticket count at this location
- `TotalAssets` - Total number of assets at this location
- `AssignedUsers` - Number of users assigned to assets at this location
- `Parts` - Number of parts in inventory at this location

**Notes**: No parameters required. For grade-level user distribution, see [GET /api/v1.0/users/stats/grades](#/Users/getUsersPerGrade).

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `LocationStatsListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `LocationStatsListGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_users_with_location_permission`

Provenance: Golden OpenAPI contract

Operation ID: `getUsersWithLocationPermission`

- Sync: `client.users.get_users_with_location_permission(location_id=..., timeout=None)`
- Async: `await client.users.get_users_with_location_permission(location_id=..., timeout=None)`
- Raw payload: `client.users.get_users_with_location_permission.raw(location_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/users/location/{LocationId}`
- Source controller: `IncidentIQ API`

Get users with location permission

Retrieves all users who have been granted permissions to access a specific location (school, building, or site). Includes user details along with their specific location permission assignments.

**Prerequisites**
1. **LocationId** - Use [GET /api/v2.0/locations](#/Locations/getAllSiteLocationsV2) or [POST /api/v1.0/search](#/Search/globalSearch) with entity type 'Location'. Extract `Items[].LocationId`.

**Workflow Example**
1. Identify location: [GET /api/v2.0/locations](#/Locations/getMyLocationsV2) → extract LocationId
2. Get permitted users: GET this endpoint with LocationId
3. Process user list with location permission details

**Use Cases**:
- Audit location access permissions
- Build location-specific agent rosters
- Validate ticket routing to location-assigned staff
- Generate location access reports

**Notes**: Returns users with any permission level at the location. Includes both direct assignments and inherited permissions from parent locations.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `location_id` | `LocationId` | `path` | `yes` | `str` | `-` | UUID of the location |

#### Returns

- Typed call return: `UsersWithLocationPermissionListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UsersWithLocationPermissionListGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `is_user_online_legacy`

Provenance: Golden OpenAPI contract

Operation ID: `isUserOnlineLegacy`

- Sync: `client.users.is_user_online_legacy(source=..., user_id=..., timeout=None)`
- Async: `await client.users.is_user_online_legacy(source=..., user_id=..., timeout=None)`
- Raw payload: `client.users.is_user_online_legacy.raw(source=..., user_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/users/is-online/{Source}/{UserId}`
- Source controller: `IncidentIQ API`

Check if user is online (legacy)

Checks whether a specific user is currently online. The Source parameter indicates the client type (web, mobile, etc.). Allows anonymous access for real-time presence checks.

**Prerequisites**
1. **UserId** - Use [POST /api/v1.0/users](#/Users/searchUsers) to locate the user and extract `Items[].UserId`.

**Workflow Example**
1. Determine the client source string (for example, `Web`).
2. Call [GET /api/v1.0/users/is-online/{Source}/{UserId}](#/Users/isUserOnlineLegacy) to retrieve the boolean status.
3. Optionally refresh status after a heartbeat via [POST /api/v1.0/users/heartbeat](#/Users/sendUserHeartbeat).

**Minimal Required Fields**: Source (path) and UserId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `source` | `Source` | `path` | `yes` | `str` | `-` | Source identifier (e.g., 'web', 'mobile') |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | UUID of the user to check Obtain via [POST /api/v1.0/users](#/Users/searchUsers), extract `Items[].UserId`. |

#### Returns

- Typed call return: `BooleanGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `BooleanGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_agents`

Provenance: Golden OpenAPI contract

Operation ID: `listAgents`

- Sync: `client.users.list_agents(p=None, s=None, body=None, timeout=None)`
- Async: `await client.users.list_agents(p=None, s=None, body=None, timeout=None)`
- Raw payload: `client.users.list_agents.raw(p=None, s=None, body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/users/agents/list`
- Source controller: `IncidentIQ API`

List support agents (simplified)

Returns a paginated list of simplified user records for support agents. Combines the performance benefits of the `/list` endpoint with automatic agent role filtering for users with Agent, iiQ Administrator, or Global Admin roles.

**Workflow Example**
1. (Optional) Prepare filters: location, team, or custom criteria
2. List agents: POST this endpoint with optional Filters array
3. Use $p and $s query parameters to navigate paginated results

**Use Cases**:
- Lightweight agent dropdowns for ticket assignment
- Quick agent selection in routing workflows
- Performance-optimized agent lists for large districts

**Minimal Required Fields**: None (all parameters optional)

**Notes**: Returns simplified records (UserId, Name, Email, RoleId). For full agent details, use [POST /api/v1.0/users/agents](#/Users/searchAgents). Default page size is 200.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index. |
| `s` | `$s` | `query` | `no` | `int` | `-` | Page size (default 200). |
| `body` | `body` | `body` | `no` | `GetUsersRequestV1` | `GetUsersRequestV1` | - |

#### Returns

- Typed call return: `SimpleUsersListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `SimpleUsersListGetResponse`
- Pagination helper: `client.users.list_agents.iter_pages(start_page=1, page_size=100, max_pages=None, p=None, s=None, body=None, timeout=None)`

---

### `list_agents_legacy_get`

Provenance: Golden OpenAPI contract

Operation ID: `listAgentsLegacyGet`

- Sync: `client.users.list_agents_legacy_get(timeout=None)`
- Async: `await client.users.list_agents_legacy_get(timeout=None)`
- Raw payload: `client.users.list_agents_legacy_get.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/users/agents/list`
- Source controller: `IncidentIQ API`

List support agents (legacy GET)

Legacy GET variant of the simplified agents list. This route returns the same lightweight agent records as the POST variant but without the optional request body filters.

**Workflow Example**
1. Call [GET /api/v1.0/users/agents/list](#/Users/listAgentsLegacyGet) to fetch the default agent list.
2. Use the response paging metadata to navigate additional pages.
3. If you need filters or advanced search facets, use [POST /api/v1.0/users/agents/list](#/Users/listAgents).

**Minimal Required Fields**: None

**Notes**: This endpoint is deprecated and maintained for backward compatibility. Prefer the POST variant for future-proof integrations.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `SimpleUsersListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `SimpleUsersListGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_user_views`

Provenance: Golden OpenAPI contract

Operation ID: `listUserViews`

- Sync: `client.users.list_user_views(p=None, s=None, timeout=None)`
- Async: `await client.users.list_user_views(p=None, s=None, timeout=None)`
- Raw payload: `client.users.list_user_views.raw(p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v1.0/users/views`
- Source controller: `IncidentIQ API`

Get User Custom Views

Returns saved custom views for the Users module. Use this to list view definitions, discover ViewId values, and drive view management UIs.

**Workflow Example**
1. Call [GET /api/v1.0/users/views](#/Users/listUserViews) with `$p`/`$s` to page results.
2. Retrieve a specific view definition via [GET /api/v1.0/users/views/{viewId}](#/Views/getUserView).
3. Create new views with [POST /api/v1.0/users/views/new](#/Users/createUserView) when needed.

**Minimal Required Fields**: None. Optional query params: `$p`, `$s`.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index to retrieve |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of records per page |

#### Returns

- Typed call return: `UserViewsListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UserViewsListResponse`
- Pagination helper: `client.users.list_user_views.iter_pages(start_page=1, page_size=100, max_pages=None, p=None, s=None, timeout=None)`

---

### `list_users_simple`

Provenance: Golden OpenAPI contract

Operation ID: `listUsersSimple`

- Sync: `client.users.list_users_simple(p=None, s=None, body=None, timeout=None)`
- Async: `await client.users.list_users_simple(p=None, s=None, body=None, timeout=None)`
- Raw payload: `client.users.list_users_simple.raw(p=None, s=None, body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/users/list`
- Source controller: `IncidentIQ API`

List users (simplified records)

Returns a paginated list of simplified user records (SimpleUser) matching the specified filter criteria. Use this endpoint when you need basic user info (name, email, location, role) without full profile details.

**Performance**: Returns smaller payload than the standard search endpoint, making it ideal for dropdowns, autocomplete, and selection UIs.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index. |
| `s` | `$s` | `query` | `no` | `int` | `-` | Page size. |
| `body` | `body` | `body` | `no` | `GetUsersRequestV1` | `GetUsersRequestV1` | - |

#### Returns

- Typed call return: `SimpleUsersListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `SimpleUsersListGetResponse`
- Pagination helper: `client.users.list_users_simple.iter_pages(start_page=1, page_size=100, max_pages=None, p=None, s=None, body=None, timeout=None)`

---

### `migrate_user`

Provenance: Golden OpenAPI contract

Operation ID: `migrateUser`

- Sync: `client.users.migrate_user(body=..., timeout=None)`
- Async: `await client.users.migrate_user(body=..., timeout=None)`
- Raw payload: `client.users.migrate_user.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/users/change`
- Source controller: `IncidentIQ API`

Migrate user data to other users

Migrates a user's data (asset assignments, ticket ownership, and ticket assignments) to other specified users. This is typically used when a user is leaving the organization and their responsibilities need to be transferred to other team members.

**Prerequisites**
1. **UserId** - The user being decommissioned. Use [POST /api/v1.0/users](#/Users/searchUsers) to find and extract `Items[].UserId`.
2. **NewAssetUserId** (optional) - User to receive asset assignments. Use [POST /api/v1.0/users/agents](#/Users/searchAgents) to find eligible agents.
3. **NewTicketOwnerId** (optional) - User to receive ticket ownership.
4. **NewTicketAssignedToId** (optional) - User to receive ticket assignments.

**Workflow Example**
1. Identify user leaving: [POST /api/v1.0/users](#/Users/searchUsers) → extract UserId of departing user.
2. Identify replacement users: [POST /api/v1.0/users/agents](#/Users/searchAgents) → extract UserIds of replacement agents.
3. Migrate data: POST this endpoint with:
   - `UserId`: departing user
   - `NewAssetUserId`: user inheriting assets
   - `NewTicketOwnerId`: user inheriting ticket ownership
   - `NewTicketAssignedToId`: user inheriting ticket assignments

**Minimal Required Fields**: UserId (others are optional - only specified fields will be migrated)

**Use Cases**:
- Employee offboarding - transfer workload to replacement
- Team restructuring - reassign assets and tickets
- User decommissioning - ensure continuity of service

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `MigrateUserRequest` | `MigrateUserRequest` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `register_external_user`

Provenance: Golden OpenAPI contract

Operation ID: `registerExternalUser`

- Sync: `client.users.register_external_user(body=..., timeout=None)`
- Async: `await client.users.register_external_user(body=..., timeout=None)`
- Raw payload: `client.users.register_external_user.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/users/external/register`
- Source controller: `IncidentIQ API`

Register external user

Initiates registration for an external (guest) user. This starts the self-registration flow and typically triggers an email with a completion token. Allows anonymous access.

**Prerequisites**
1. **LocationId** (if required by tenant) - Use [GET /api/v1.0/locations/view](#/Locations/getAllSiteLocationsV2) to select a location.

**Workflow Example**
1. Submit registration details with email and name.
2. User receives a verification email containing a token.
3. Complete setup via [POST /api/v1.0/users/external/complete-registration](#/Users/completeExternalUserRegistration).

**Minimal Required Fields**: Email, FirstName, LastName (LocationId may be required by policy).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `RegisterExternalUserRequest` | `RegisterExternalUserRequest` | - |

#### Returns

- Typed call return: `RegisterExternalUserResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `RegisterExternalUserResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `remove_room_from_user`

Provenance: Golden OpenAPI contract

Operation ID: `removeRoomFromUser`

- Sync: `client.users.remove_room_from_user(user_id=..., location_room_id=..., timeout=None)`
- Async: `await client.users.remove_room_from_user(user_id=..., location_room_id=..., timeout=None)`
- Raw payload: `client.users.remove_room_from_user.raw(user_id=..., location_room_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/users/{UserId}/rooms/{LocationRoomId}`
- Source controller: `IncidentIQ API`

Remove room from user

Removes a specific room assignment from a user's profile. Room assignments determine which physical rooms a user is associated with for ticket routing and location-based filtering.

**Prerequisites**
1. **UserId** - Use [POST /api/v1.0/search](#/Search/globalSearch) with entity type 'User'. Extract `Item.Users[].UserId`.
2. **LocationRoomId** - Use [POST /api/v1.0/users/rooms/get](#/Users/getUserRooms) to list assigned rooms. Extract `Items[].LocationRoomId`.

**Workflow Example**
1. Search users: [POST /api/v1.0/search](#/Search/globalSearch) → extract UserId
2. List rooms: [POST /api/v1.0/users/rooms/get](#/Users/getUserRoomsBulk) with UserId → find LocationRoomId to remove
3. Remove room: DELETE this endpoint

**Notes**: Other room assignments for the user remain unchanged. Use [POST /api/v1.0/users/{UserId}/rooms/{LocationRoomId}](#/Users/addRoomToUser) to add rooms.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | User identifier. Obtain via [POST /api/v1.0/users](#/Users/searchUsers), extract `Items[].UserId`. |
| `location_room_id` | `LocationRoomId` | `path` | `yes` | `str` | `-` | Room identifier to remove. |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `reset_user_password`

Provenance: Golden OpenAPI contract

Operation ID: `resetUserPassword`

- Sync: `client.users.reset_user_password(user_id=..., timeout=None)`
- Async: `await client.users.reset_user_password(user_id=..., timeout=None)`
- Raw payload: `client.users.reset_user_password.raw(user_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/users/{UserId}/reset-password`
- Source controller: `IncidentIQ API`

Reset user password

Initiates a password reset for the specified user and triggers the standard reset workflow (typically by emailing a reset link to the user's address on file).

**Prerequisites**
1. **UserId** - Use [POST /api/v1.0/users](#/Users/searchUsers) to locate the user. Extract `Items[].UserId`.

**Workflow Example**
1. Search for the user: [POST /api/v1.0/users](#/Users/searchUsers) → extract UserId.
2. POST this endpoint to initiate the reset process.
3. Monitor for the success message and confirm the user received the reset email.

**Minimal Required Fields**: UserId (path)

**Notes**: Ensure the user's email address is correct before issuing a reset. Use [POST /api/v1.0/users/{UserId}/change-password](#/Users/changeUserPassword) when setting a password directly.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | User identifier. Obtain via [POST /api/v1.0/users](#/Users/searchUsers), extract `Items[].UserId`. |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `restore_i_i_q_admin_accounts`

Provenance: Golden OpenAPI contract

Operation ID: `restoreIIQAdminAccounts`

- Sync: `client.users.restore_i_i_q_admin_accounts(body=..., timeout=None)`
- Async: `await client.users.restore_i_i_q_admin_accounts(body=..., timeout=None)`
- Raw payload: `client.users.restore_i_i_q_admin_accounts.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/users/restore-account`
- Source controller: `IncidentIQ API`

Restore Incident IQ admin accounts

Restores default Incident IQ administrative accounts for a specified site. This is a recovery operation for situations where admin accounts have been accidentally deleted, disabled, or corrupted.

**Prerequisites**
1. **SiteId** - Use [GET /api/v2.0/users/my/locations](#/Users/getCurrentUserLocationsV2) to list locations. Extract `Items[].SiteId`.
2. Requires Global Administrator role

**Workflow Example**
1. Identify site needing admin restoration: [GET /api/v2.0/users/my/locations](#/Users/getCurrentUserLocationsV2) → extract SiteId
2. Restore admins: POST this endpoint with SiteId and optional FullName
3. Default admin accounts are recreated/restored

**Minimal Required Fields**: SiteId

**Use Cases**:
- Recover from accidental admin account deletion
- Reset admin access after lockout
- Initial admin provisioning for new sites

**Notes**: Restricted to Global Administrators only. Creates or restores standard iiQ admin accounts. Does not affect non-admin user accounts. Use with caution in production environments.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `RestoreIIQAdminAccountsRequest` | `RestoreIIQAdminAccountsRequest` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `search_agents`

Provenance: Golden OpenAPI contract

Operation ID: `searchAgents`

- Sync: `client.users.search_agents(p=None, s=None, body=None, timeout=None)`
- Async: `await client.users.search_agents(p=None, s=None, body=None, timeout=None)`
- Raw payload: `client.users.search_agents.raw(p=None, s=None, body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/users/agents`
- Source controller: `IncidentIQ API`

Search support agents

Returns a paginated, searchable list of users who have support agent roles (Agent, iiQ Administrator, or Global Admin). Automatically applies role filters to return only agent-type users.

**Workflow Example**
1. (Optional) Define filters: location, team, or custom criteria
2. Search agents: POST this endpoint with optional Filters array
3. Use pagination parameters ($p, $s) to navigate results

**Use Cases**:
- Populate agent assignment dropdowns for ticket routing
- Build team rosters and workload dashboards
- Filter agents by location for localized support

**Minimal Required Fields**: None (Filters optional)

**Notes**: Default page size is 200. Results include agent name, email, roles, and location assignments. For GET-based legacy access, use [GET /api/v1.0/users/agents/list](#/Users/listAgents).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index. |
| `s` | `$s` | `query` | `no` | `int` | `-` | Page size (default 200). |
| `body` | `body` | `body` | `no` | `GetUsersRequestV1` | `GetUsersRequestV1` | - |

#### Returns

- Typed call return: `UsersListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UsersListGetResponse`
- Pagination helper: `client.users.search_agents.iter_pages(start_page=1, page_size=100, max_pages=None, p=None, s=None, body=None, timeout=None)`

---

### `search_agents_legacy_get`

Provenance: Golden OpenAPI contract

Operation ID: `searchAgentsLegacyGet`

- Sync: `client.users.search_agents_legacy_get(timeout=None)`
- Async: `await client.users.search_agents_legacy_get(timeout=None)`
- Raw payload: `client.users.search_agents_legacy_get.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/users/agents`
- Source controller: `IncidentIQ API`

Search support agents (legacy GET)

Legacy GET variant of the agents search endpoint that returns the agent-only roster without request body filters. This route exists for backward compatibility and should be replaced by the POST search endpoint for new integrations.

**Workflow Example**
1. Call [GET /api/v1.0/users/agents](#/Users/searchAgentsLegacyGet) to retrieve the default agent list.
2. Use paging information in the response to iterate through results.
3. For advanced filtering or facets, switch to [POST /api/v1.0/users/agents](#/Users/searchAgents).

**Minimal Required Fields**: None

**Notes**: This endpoint is deprecated and may be removed in a future release. It does not accept the Filters array used by the POST variant.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `UsersListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UsersListGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `search_users`

Provenance: Golden OpenAPI contract

Operation ID: `searchUsers`

- Sync: `client.users.search_users(p=None, s=None, o=None, site_id=None, product_id=None, x_revision_date=None, body=..., timeout=None)`
- Async: `await client.users.search_users(p=None, s=None, o=None, site_id=None, product_id=None, x_revision_date=None, body=..., timeout=None)`
- Raw payload: `client.users.search_users.raw(p=None, s=None, o=None, site_id=None, product_id=None, x_revision_date=None, body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/users`
- Source controller: `IncidentIQ API`

Search users

Returns paginated user data filtered by one or more facet criteria such as role, keyword, licensed products, or SIS metadata.

**Filter Facet System**

This endpoint uses the universal `FilterMatch` pattern shared across Tickets, Assets, and Users search endpoints. Users support **41 filter facets** organized into categories:

- **Identity**: `user`, `keyword`, `username`, `email`, `personalemail`, `schoolidnumber`
- **Organization**: `role`, `location`, `locationtype`, `site`, `team`, `department`, `orgunit`
- **SIS Integration**: `grade`, `homeroom`, `sisclass`, `siscourse`, `sisteacher`, `sisuserstatus`
- **Status**: `userstatus`, `employmentstatus`, `authenticatedby`
- **Labor Tracking**: `labortype`, `laborhourlyrate`, `laboractivitydate` (use `NumericExpressionSyntax` and `DateExpressionSyntax`)
- **Device Assignment**: `hasassigneddevice`, `usermultipledevices`
- **Forms**: `form`, `formsubmissionstatus`
- **Files**: `hasfileswithincategory`, `hasfileswithkeyword`
- **Duplicates**: `userduplicateany`, `userduplicateemail`, `userduplicateschoolid`, `userduplicateusername`
- **Custom Fields**: `usercustomfield`, `userattribute`
- **App Links**: `userapplink`, `performedbyapp`

See the `UserSearchFilter` schema for the complete `x-facet-definitions` reference documenting all 41 facets with their required fields.

**Filter Expression Syntax**
- **Date facets** (e.g., `laboractivitydate`): Use `DateExpressionSyntax` - supports comparison operators (`date>=MM/DD/YYYY`) and relative ranges (`range:lastdays:30`).
- **Numeric facets** (e.g., `laborhourlyrate`): Use `NumericExpressionSyntax` - format is `numoperator:<operator>:<value>` where operator is `equals`, `lessthan`, `lessthanequal`, `greaterthan`, or `greaterthanequal`.
- **Keyword/text**: Simple `Value` field for searching names, emails, usernames, school IDs.
- **Entity references**: Use `Id` field with UUID (role, location, site, team, form).
- **Boolean facets** (e.g., `hasassigneddevice`, `usermultipledevices`): Use `Name: "yes"` and `Value: "yes"` (or `"no"`).

**Prerequisites**
- To filter by `role`, use [GET /api/v1.0/roles](#/Roles/listRoles) to retrieve `RoleId` values.
- To filter by `location`, use [GET /api/v1.0/locations/view](#/Locations/getAllSiteLocationsV2) to retrieve `LocationId` values.
- To filter by `team`, use [GET /api/v1.0/teams](#/Teams/listTeams) to retrieve `TeamId` values.
- Call [GET /api/v1.0/filters/for/entitytype/{entityTypeId}](#/Filters/listFiltersForEntityType) with entity type `888891ac-91aa-e711-80c2-100dffa00003` to enumerate all available user filter keys.

**Pagination and sorting**
- Use `$p` (zero-based page index) and `$s` (page size) query parameters to page through results.
- The response `Paging` object provides `PageIndex`, `PageSize`, `PageCount`, and `TotalRows` for navigation.

**Performance considerations**
- Begin searches with narrow filter combinations (role + location + keyword) to avoid scanning the entire user directory.
- Cache supporting metadata (roles, locations, teams) rather than issuing lookups per request.
- Use moderate page sizes (25–100) for optimal response times.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index to retrieve. |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of records to return per page. |
| `o` | `$o` | `query` | `no` | `Any` | `-` | Sort expression: field name followed by optional direction (e.g., `FullName desc`). Direction can be `asc`, `ascending`, `desc`, or `descending`. Default direction is ascending. Default sort is `FullName asc`. See [UserSortField](#/components/schemas/UserSortField) for valid field names. |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Overrides the default Site context when supplied. |
| `product_id` | `ProductId` | `header` | `no` | `str` | `-` | Overrides the default Product context when supplied. |
| `x_revision_date` | `x-revision-date` | `header` | `no` | `str` | `-` | Optional revision date used to retrieve user directory data as of a specific point in time. |
| `body` | `body` | `body` | `yes` | `GetUsersRequestV1` | `GetUsersRequestV1` | - |

#### Returns

- Typed call return: `UsersListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UsersListGetResponse`
- Pagination helper: `client.users.search_users.iter_pages(start_page=1, page_size=100, max_pages=None, p=None, s=None, o=None, site_id=None, product_id=None, x_revision_date=None, body=..., timeout=None)`

---

### `search_users_by_keyword`

Provenance: Golden OpenAPI contract

Operation ID: `searchUsersByKeyword`

- Sync: `client.users.search_users_by_keyword(query=..., p=None, s=None, timeout=None)`
- Async: `await client.users.search_users_by_keyword(query=..., p=None, s=None, timeout=None)`
- Raw payload: `client.users.search_users_by_keyword.raw(query=..., p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v1.0/users/search/{Query}`
- Source controller: `IncidentIQ API`

Search users by keyword

Searches users by a keyword query string, matching against name, email, and username fields for fast lookups and autocomplete experiences. Use this endpoint when you need a lightweight, path-based search without the full filter-facet payload required by [POST /api/v1.0/users](#/Users/searchUsers). Results can be paged using `$p` and `$s` to support typeahead or pickers.

**Workflow Example**
1. Capture a query fragment from user input (name, email, or username).
2. Call [GET /api/v1.0/users/search/{Query}](#/Users/searchUsersByKeyword) with optional `$p`/`$s` for paging.
3. Use the response `Items[]` to populate search results and select a `UserId` for downstream actions.

**Minimal Required Fields**: Query (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `query` | `Query` | `path` | `yes` | `str` | `-` | Search keyword to match against user name, email, or username. |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index. |
| `s` | `$s` | `query` | `no` | `int` | `-` | Page size. |

#### Returns

- Typed call return: `UsersListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UsersListGetResponse`
- Pagination helper: `client.users.search_users_by_keyword.iter_pages(start_page=1, page_size=100, max_pages=None, query=..., p=None, s=None, timeout=None)`

---

### `search_users_legacy_get`

Provenance: Golden OpenAPI contract

Operation ID: `searchUsersLegacyGet`

- Sync: `client.users.search_users_legacy_get(p=None, s=None, o=None, site_id=None, product_id=None, timeout=None)`
- Async: `await client.users.search_users_legacy_get(p=None, s=None, o=None, site_id=None, product_id=None, timeout=None)`
- Raw payload: `client.users.search_users_legacy_get.raw(p=None, s=None, o=None, site_id=None, product_id=None, timeout=None)`
- HTTP route: `GET /api/v1.0/users`
- Source controller: `IncidentIQ API`

Search users (legacy GET)

Legacy GET variant of the user search endpoint. This route is marked obsolete in the source controller and exists primarily for backward compatibility when request bodies are not supported.

**Workflow Example**
1. For legacy clients, call [GET /api/v1.0/users](#/Users/searchUsersLegacyGet) with `$p`/`$s` to page through the directory.
2. For filterable search, switch to [POST /api/v1.0/users](#/Users/searchUsers) and supply Filters.
3. Use the response `Paging` object to iterate remaining pages.

**Minimal Required Fields**: None. Optional query params: `$p`, `$s`.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index to retrieve. |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of records to return per page. |
| `o` | `$o` | `query` | `no` | `Any` | `-` | Sort expression: field name followed by optional direction (e.g., `FullName desc`). Direction can be `asc`, `ascending`, `desc`, or `descending`. Default direction is ascending. Default sort is `FullName asc`. See [UserSortField](#/components/schemas/UserSortField) for valid field names. |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Overrides the default Site context when supplied. |
| `product_id` | `ProductId` | `header` | `no` | `str` | `-` | Overrides the default Product context when supplied. |

#### Returns

- Typed call return: `UsersListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UsersListGetResponse`
- Pagination helper: `client.users.search_users_legacy_get.iter_pages(start_page=1, page_size=100, max_pages=None, p=None, s=None, o=None, site_id=None, product_id=None, timeout=None)`

---

### `send_user_heartbeat`

Provenance: Golden OpenAPI contract

Operation ID: `sendUserHeartbeat`

- Sync: `client.users.send_user_heartbeat(product_id=None, client=None, timeout=None)`
- Async: `await client.users.send_user_heartbeat(product_id=None, client=None, timeout=None)`
- Raw payload: `client.users.send_user_heartbeat.raw(product_id=None, client=None, timeout=None)`
- HTTP route: `POST /api/v1.0/users/heartbeat`
- Source controller: `IncidentIQ API`

Send user heartbeat

Records a heartbeat for the authenticated user session to mark the user as online. The platform derives the client type from the authenticated user context (for example, `Web` or `Mobile` based on the `Client` header).

**Workflow Example**
1. Client sends periodic heartbeats (for example, every 60 seconds) using [POST /api/v1.0/users/heartbeat](#/Users/sendUserHeartbeat).
2. Presence is updated and can be queried via [GET /api/v1.0/users/is-online/{Source}/{UserId}](#/Users/isUserOnlineLegacy).
3. If heartbeats stop, maintenance routines may mark the user offline.

**Minimal Required Fields**: None. Optional headers: `Client`, `ProductId`.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `product_id` | `ProductId` | `header` | `no` | `str` | `-` | Optional product context used when deriving presence scope. |
| `client` | `Client` | `header` | `no` | `str` | `-` | Client identifier used to infer the requesting platform (for example `WebBrowser` or `Mobile`). |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `send_welcome_package`

Provenance: Golden OpenAPI contract

Operation ID: `sendWelcomePackage`

- Sync: `client.users.send_welcome_package(user_id=..., timeout=None)`
- Async: `await client.users.send_welcome_package(user_id=..., timeout=None)`
- Raw payload: `client.users.send_welcome_package.raw(user_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/users/{UserId}/send-welcome-package`
- Source controller: `IncidentIQ API`

Send welcome package to user

Manually triggers the welcome package email for a specific user. The welcome package typically includes login instructions, onboarding links, and initial setup information.

**Prerequisites**
1. **UserId** - Use [POST /api/v1.0/users](#/Users/searchUsers) to locate the user and extract `Items[].UserId`.

**Workflow Example**
1. Find the user: [POST /api/v1.0/users](#/Users/searchUsers) -> capture UserId.
2. Call [POST /api/v1.0/users/{UserId}/send-welcome-package](#/Users/sendWelcomePackage).
3. Confirm the user receives the email and can sign in.

**Minimal Required Fields**: UserId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | User identifier. Obtain via [POST /api/v1.0/users](#/Users/searchUsers), extract `Items[].UserId`. |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `send_welcome_packages_to_enabled_roles`

Provenance: Golden OpenAPI contract

Operation ID: `sendWelcomePackagesToEnabledRoles`

- Sync: `client.users.send_welcome_packages_to_enabled_roles(timeout=None)`
- Async: `await client.users.send_welcome_packages_to_enabled_roles(timeout=None)`
- Raw payload: `client.users.send_welcome_packages_to_enabled_roles.raw(timeout=None)`
- HTTP route: `POST /api/v1.0/users/send-welcome-packages-to-enabled-roles`
- Source controller: `IncidentIQ API`

Send welcome packages to all enabled roles

Triggers welcome package emails for all users in roles that have welcome packages enabled. Welcome packages introduce users to IncidentIQ with login instructions, feature guides, and onboarding resources.

**Workflow Example**
1. Ensure welcome packages are configured in role settings
2. POST this endpoint to trigger mass email distribution
3. System sends emails to all eligible users in enabled roles

**Use Cases**:
- Mass onboarding at semester/year start
- Re-send welcome emails after system migration
- New role rollout with welcome notification
- District-wide IncidentIQ introduction

**Notes**: No request body required. Only sends to roles with welcome packages enabled in configuration. Users who have already received welcome packages may receive duplicates. Requires administrative privileges. Email delivery depends on site email configuration. Check email logs for delivery status.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `set_my_options`

Provenance: Golden OpenAPI contract

Operation ID: `setMyOptions`

- Sync: `client.users.set_my_options(body=..., timeout=None)`
- Async: `await client.users.set_my_options(body=..., timeout=None)`
- Raw payload: `client.users.set_my_options.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/users/my/options`
- Source controller: `IncidentIQ API`

Update current user's options/preferences

Updates the authenticated user's personal options and preference settings. This is a convenience endpoint equivalent to [POST /api/v1.0/users/{UserId}/options](#/Users/setUserOptions) but automatically uses the authenticated user's ID.

**Workflow Example**
1. Retrieve current options: [GET /api/v1.0/users/my/options](#/Users/getMyOptions)
2. Modify the desired settings in the `UserOptions` payload
3. Submit [POST /api/v1.0/users/my/options](#/Users/setMyOptions) to persist the changes

**Use Cases**:
- Self-service preferences update from settings page
- Toggle notification preferences
- Update UI display options

**Minimal Required Fields**: A request body object. If setting `Notifications`, include all required fields in the `UserNotificationSettings` schema.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `UserOptions` | `UserOptions` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `set_user_active`

Provenance: Golden OpenAPI contract

Operation ID: `setUserActive`

- Sync: `client.users.set_user_active(timeout=None)`
- Async: `await client.users.set_user_active(timeout=None)`
- Raw payload: `client.users.set_user_active.raw(timeout=None)`
- HTTP route: `POST /api/v1.0/users/my/is-online/active`
- Source controller: `IncidentIQ API`

Set current user as active

Sets the authenticated user's presence status to active (online) and clears any away status. Used to indicate the user is available for ticket assignment and real-time collaboration.

**Workflow Example**
1. User returns from break or starts their work session
2. POST this endpoint to mark as active
3. User appears as online in presence indicators and routing

**Use Cases**:
- Return from away status after break
- Session initialization at login
- Manual presence toggle in UI
- Automated presence via activity detection

**Notes**: No request body required. Updates presence immediately. Other users will see the status change in real-time if presence features are enabled. To set away status, use [POST /api/v1.0/users/my/is-online/away](#/Users/setUserAway).

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `set_user_away`

Provenance: Golden OpenAPI contract

Operation ID: `setUserAway`

- Sync: `client.users.set_user_away(body=..., timeout=None)`
- Async: `await client.users.set_user_away(body=..., timeout=None)`
- Raw payload: `client.users.set_user_away.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/users/my/is-online/away`
- Source controller: `IncidentIQ API`

Set current user as away

Sets the authenticated user's presence status to away (unavailable). Used to indicate the user is temporarily unavailable for ticket assignment and routing.

**Workflow Example**
1. User is stepping away (meeting, lunch, etc.)
2. POST this endpoint with optional `ExpirationDate` for auto-return
3. User appears as away in presence indicators
4. Ticket routing may skip this user based on away status
5. If `ExpirationDate` is set, user automatically returns to active when the time passes

**Minimal Required Fields**: None (ExpirationDate is optional)

**Use Cases**:
- Manual away toggle in UI
- Calendar integration for scheduled meetings
- Lunch break with automatic return time
- Out-of-office status with expiration

**Notes**: To return to active status before expiration, use [POST /api/v1.0/users/my/is-online/active](#/Users/setUserActive). The away status may integrate with calendar events for automatic out-of-office management.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `SetUserAwayRequest` | `SetUserAwayRequest` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `set_user_initial_product`

Provenance: Golden OpenAPI contract

Operation ID: `setUserInitialProduct`

- Sync: `client.users.set_user_initial_product(body=..., timeout=None)`
- Async: `await client.users.set_user_initial_product(body=..., timeout=None)`
- Raw payload: `client.users.set_user_initial_product.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/users/set-initial-product`
- Source controller: `IncidentIQ API`

Set user's initial product

Sets the initial product module (Technology, Facilities, HR, etc.) for a user. This determines which dashboard and default views the user sees upon login to IncidentIQ.

**Workflow Example**
1. Identify user and target product: UserId and ProductId
2. POST this endpoint to set initial product preference
3. User will see the selected product dashboard on next login

**Use Cases**:
- New user onboarding with correct product context
- Reassigning users to different product areas
- Bulk product assignment during role changes
- Default product setup for multi-product users

**Minimal Required Fields**: UserId, ProductId

**Notes**: Available products depend on site licensing (Technology, Facilities, HR, etc.). Users can still switch products after login if they have access to multiple products. This only sets the default/initial view. Does not restrict access to other licensed products.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `SetUserInitialProductRequest` | `SetUserInitialProductRequest` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `set_user_options`

Provenance: Golden OpenAPI contract

Operation ID: `setUserOptions`

- Sync: `client.users.set_user_options(user_id=..., body=..., timeout=None)`
- Async: `await client.users.set_user_options(user_id=..., body=..., timeout=None)`
- Raw payload: `client.users.set_user_options.raw(user_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/users/{UserId}/options`
- Source controller: `IncidentIQ API`

Update user options/preferences

Updates a user's personal options and preference settings, such as notification toggles and other profile-level configuration stored under `UserOptions`. Use this endpoint when an administrator or integration needs to update another user's settings; for self-service updates, prefer [POST /api/v1.0/users/my/options](#/Users/setMyOptions).

**Prerequisites**
1. **UserId** - Use [GET /api/v1.0/users/search/{Query}](#/Users/searchUsersByKeyword) or [POST /api/v1.0/users](#/Users/searchUsers) to locate the user and extract `Items[].UserId`.

**Workflow Example**
1. Find the user: [GET /api/v1.0/users/search/{Query}](#/Users/searchUsersByKeyword) -> capture `UserId`.
2. Build the `UserOptions` payload (for example, update notification booleans).
3. Submit [POST /api/v1.0/users/{UserId}/options](#/Users/setUserOptions) to persist the changes.

**Minimal Required Fields**: UserId (path) and a request body object. If setting `Notifications`, include all required fields in the `UserNotificationSettings` schema.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | User identifier. Obtain via [POST /api/v1.0/users](#/Users/searchUsers), extract `Items[].UserId`. |
| `body` | `body` | `body` | `yes` | `UserOptions` | `UserOptions` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `set_user_role`

Provenance: Golden OpenAPI contract

Operation ID: `setUserRole`

- Sync: `client.users.set_user_role(user_id=..., body=..., timeout=None)`
- Async: `await client.users.set_user_role(user_id=..., body=..., timeout=None)`
- Raw payload: `client.users.set_user_role.raw(user_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/users/{UserId}/role`
- Source controller: `IncidentIQ API`

Set user role

Updates the role assignment for a user, which directly controls permissions, access to modules, and administrative capabilities.

**Prerequisites**
1. **UserId** - Use [POST /api/v1.0/users](#/Users/searchUsers) to locate the user. Extract `Items[].UserId`.
2. **RoleId** - Use [GET /api/v1.0/sites/roles](#/Sites/listRoles) to list available roles. Extract `Items[].RoleId`.

**Workflow Example**
1. List roles: [GET /api/v1.0/sites/roles](#/Sites/listRoles) → select the target RoleId.
2. Search for the user: [POST /api/v1.0/users](#/Users/searchUsers) → extract UserId.
3. POST this endpoint with RoleId to update access.

**Minimal Required Fields**: RoleId (request body)

**Notes**: Role changes take effect immediately and may alter the user's visibility and administrative permissions.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | User identifier. Obtain via [POST /api/v1.0/users](#/Users/searchUsers), extract `Items[].UserId`. |
| `body` | `body` | `body` | `yes` | `SetUserRoleRequest` | `SetUserRoleRequest` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `set_user_rooms`

Provenance: Golden OpenAPI contract

Operation ID: `setUserRooms`

- Sync: `client.users.set_user_rooms(user_id=..., body=..., timeout=None)`
- Async: `await client.users.set_user_rooms(user_id=..., body=..., timeout=None)`
- Raw payload: `client.users.set_user_rooms.raw(user_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/users/{UserId}/rooms`
- Source controller: `IncidentIQ API`

Set user's room assignments

Replaces all room assignments for a user with the provided list. This clears existing assignments and sets the new room list in a single operation.

**Prerequisites**
1. **UserId** - Use [POST /api/v1.0/users](#/Users/searchUsers) to locate the user. Extract `Items[].UserId`.
2. **LocationRoomId values** - Use [POST /api/v2.0/locations/{locationId}/rooms](#/Locations/queryLocationRoomsByLocationId) and extract `Items[].LocationRoomId` (use [GET /api/v1.0/locations/view](#/Locations/getAllSiteLocationsV2) to find LocationId).

**Workflow Example**
1. Identify the user: [POST /api/v1.0/users](#/Users/searchUsers) → extract UserId.
2. Query rooms for a location: [POST /api/v2.0/locations/{locationId}/rooms](#/Locations/queryLocationRoomsByLocationId) → collect LocationRoomId values.
3. POST this endpoint with the list of room IDs to replace the user's assignments.

**Minimal Required Fields**: Request body list of LocationRoomId values

**Notes**: This is a full replacement. To add a single room without clearing existing assignments, use [POST /api/v1.0/users/{UserId}/rooms/{LocationRoomId}](#/Users/addRoomToUser).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | User identifier. Obtain via [POST /api/v1.0/users](#/Users/searchUsers), extract `Items[].UserId`. |
| `body` | `body` | `body` | `yes` | `UuidList` | `UuidList` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `undelete_user`

Provenance: Golden OpenAPI contract

Operation ID: `undeleteUser`

- Sync: `client.users.undelete_user(user_id=..., timeout=None)`
- Async: `await client.users.undelete_user(user_id=..., timeout=None)`
- Raw payload: `client.users.undelete_user.raw(user_id=..., timeout=None)`
- HTTP route: `PUT /api/v1.0/users/{UserId}/undelete`
- Source controller: `IncidentIQ API`

Restore a deleted user

Restores a soft-deleted user account and reactivates their access with previous role and permissions.

**Prerequisites**
1. **UserId** - Use [POST /api/v1.0/users/all](#/Users/getAllUsers) to include deleted records and extract `Items[].UserId`.

**Workflow Example**
1. Search all users (including deleted): [POST /api/v1.0/users/all](#/Users/getAllUsers).
2. Identify the deleted user and capture UserId.
3. Call [PUT /api/v1.0/users/{UserId}/undelete](#/Users/undeleteUser) to restore the account.

**Minimal Required Fields**: UserId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | User identifier of the deleted user to restore. Obtain via [POST /api/v1.0/users](#/Users/searchUsers), extract `Items[].UserId`. |

#### Returns

- Typed call return: `UserDetailGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UserDetailGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_all_users_out_of_office_status`

Provenance: Golden OpenAPI contract

Operation ID: `updateAllUsersOutOfOfficeStatus`

- Sync: `client.users.update_all_users_out_of_office_status(timeout=None)`
- Async: `await client.users.update_all_users_out_of_office_status(timeout=None)`
- Raw payload: `client.users.update_all_users_out_of_office_status.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/users/out-of-office/update-all`
- Source controller: `IncidentIQ API`

Update all users out-of-office status

Triggers a global maintenance task to synchronize user out-of-office statuses with calendar events and existing OOO records. Restricted to Global Administrators.

**Workflow Example**
1. Call [GET /api/v1.0/users/out-of-office/update-all](#/Users/updateAllUsersOutOfOfficeStatus) during scheduled maintenance.
2. Review the response `UserActions` list to see who was set in or out of office.
3. Use results for audit or to validate calendar integration.

**Minimal Required Fields**: None.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `UserOutOfOfficeUpdateAllResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UserOutOfOfficeUpdateAllResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_shortcut`

Provenance: Golden OpenAPI contract

Operation ID: `updateShortcut`

- Sync: `client.users.update_shortcut(shortcut_id=..., body=..., timeout=None)`
- Async: `await client.users.update_shortcut(shortcut_id=..., body=..., timeout=None)`
- Raw payload: `client.users.update_shortcut.raw(shortcut_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/users/shortcut/{ShortcutId}`
- Source controller: `IncidentIQ API`

Update a shortcut

Updates an existing rule-based shortcut's configuration including name, scope, rule association, or filter set.

**Prerequisites**
1. **ShortcutId** - Use [GET /api/v1.0/users/shortcuts/available](#/Users/getAvailableShortcuts) to list shortcuts. Extract `Items[].ShortcutId`.

**Workflow Example**
1. List shortcuts: [GET /api/v1.0/users/shortcuts/available](#/Users/getAvailableShortcuts) → find shortcut to update
2. Modify shortcut: POST this endpoint with updated properties

**Minimal Required Fields**: ShortcutId (path), updated Shortcut object in body

**Notes**: Only shortcuts the user owns or has permission to manage can be updated. The ShortcutId in the path is used; ShortcutId in the body is overwritten with the path value.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `shortcut_id` | `ShortcutId` | `path` | `yes` | `str` | `-` | Shortcut identifier. |
| `body` | `body` | `body` | `yes` | `Shortcut` | `Shortcut` | - |

#### Returns

- Typed call return: `ShortcutUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ShortcutUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_user`

Provenance: Golden OpenAPI contract

Operation ID: `updateUser`

- Sync: `client.users.update_user(user_id=..., api_flags=None, body=..., timeout=None)`
- Async: `await client.users.update_user(user_id=..., api_flags=None, body=..., timeout=None)`
- Raw payload: `client.users.update_user.raw(user_id=..., api_flags=None, body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/users/{UserId}`
- Source controller: `IncidentIQ API`

Update user

Updates an existing user record with new profile information, location, role, or custom field values.

**Partial Update Mode**
By default, fields omitted from the request payload may be overwritten with null or default values. To perform a true partial update where only the fields you specify are modified, include the `ApiFlags: OnlySetMappedProperties` header. This ensures existing field values are preserved when not explicitly included in the payload.

**Prerequisites**
1. **UserId** – Locate the user via [POST /api/v1.0/search](#/Users/searchUsers) and extract `Item.Users[].UserId`.
2. **Related references** – When changing location or role, retrieve valid identifiers from [GET /api/v1.0/locations/all](#/Locations/getAllSiteLocationsV2) or [GET /api/v1.0/roles](#/Roles/listRoles).

**Workflow Example**
1. Search for the user: [POST /api/v1.0/search](#/Search/globalSearch) with user filters → extract `Item.Users[0].UserId`.
2. Build the update payload with the fields to change (e.g., `LocationId`, `RoleId`, `Phone`, `CustomFieldValues`).
3. For partial updates, include the `ApiFlags: OnlySetMappedProperties` header.
4. [POST /api/v1.0/users/{UserId}](#/Users/updateUser) to persist the changes.

**Minimal Required Fields**: UserId (path) plus at least one mutable property in the request body.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | User identifier. |
| `api_flags` | `ApiFlags` | `header` | `no` | `str` | `-` | Optional flag to control update behavior. When set to `OnlySetMappedProperties`, only fields explicitly included in the request payload will be updated; fields omitted from the payload will retain their existing values instead of being overwritten with null or default values. |
| `body` | `body` | `body` | `yes` | `UserUpdateRequest` | `UserUpdateRequest` | User update payload containing the fields to modify. |

#### Returns

- Typed call return: `UserDetailUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UserDetailUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_user_authentication_source`

Provenance: Golden OpenAPI contract

Operation ID: `updateUserAuthenticationSource`

- Sync: `client.users.update_user_authentication_source(user_id=..., body=..., timeout=None)`
- Async: `await client.users.update_user_authentication_source(user_id=..., body=..., timeout=None)`
- Raw payload: `client.users.update_user_authentication_source.raw(user_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/users/{UserId}/authentication-source`
- Source controller: `IncidentIQ API`

Update user authentication source

Updates the authentication source for a specific user, allowing administrators to switch how the user authenticates (for example, local credentials versus external SSO).

**Prerequisites**
1. **UserId** - Use [POST /api/v1.0/users](#/Users/searchUsers) to locate the user. Extract `Items[].UserId`.
2. **AuthenticationSource** - Ensure the target authentication source is configured for the tenant.

**Workflow Example**
1. Review current user auth: [GET /api/v1.0/users/{UserId}](#/Users/getUserById) via [GET /api/v1.0/users/{UserId}](#/Users/getUserById).
2. Decide the new source and optional ExternalId.
3. POST this endpoint with AuthenticationSource (and ExternalId if required).

**Minimal Required Fields**: AuthenticationSource (request body)

**Notes**: Changing auth sources can affect login behavior immediately. Coordinate changes with identity provider settings.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | UUID of the user to update Obtain via [POST /api/v1.0/users](#/Users/searchUsers), extract `Items[].UserId`. |
| `body` | `body` | `body` | `yes` | `UpdateUserAuthenticationSourceRequest` | `UpdateUserAuthenticationSourceRequest` | - |

#### Returns

- Typed call return: `UserDetailUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UserDetailUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_user_view_sort`

Provenance: Golden OpenAPI contract

Operation ID: `updateUserViewSort`

- Sync: `client.users.update_user_view_sort(view_id=..., body=..., timeout=None)`
- Async: `await client.users.update_user_view_sort(view_id=..., body=..., timeout=None)`
- Raw payload: `client.users.update_user_view_sort.raw(view_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/users/views/{viewId}/sort`
- Source controller: `IncidentIQ API`

Update user view sort

Updates the sort configuration for an existing user view. Controls which field is used for ordering results and the sort direction.

**Prerequisites**
1. **viewId** - Use [GET /api/v1.0/users/views](#/Users/listUserViews) to list views. Extract `Items[].ViewId`.

**Workflow Example**
1. List views: [GET /api/v1.0/users/views](#/Users/listUserViews) → find the view to modify
2. Update sort: POST this endpoint with Field, Name, and Direction

**Minimal Required Fields**: Field (field identifier), Name (display name), Direction ('Ascending' or 'Descending')

**Notes**: The Field value must match a valid sortable column for the view type. Common fields include 'LastName', 'Email', 'CreatedDate'. Changes take effect immediately for subsequent queries using this view.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `view_id` | `viewId` | `path` | `yes` | `str` | `-` | Identifier of the user view to update. |
| `body` | `body` | `body` | `yes` | `ViewSort` | `ViewSort` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
