# `teams` Golden Namespace

Sync client access: `client.teams`

Async client access: `client.teams` with `await` on method calls.

These methods are Golden because they come from the bundled Incident IQ OpenAPI contract.

## Aliases

| Alias | Canonical Method | Route |
| --- | --- | --- |
| `create` | `create_team` | `POST /api/v1.0/teams/new` |

## Methods

### `add_team_member`

Provenance: Golden OpenAPI contract

Operation ID: `addTeamMember`

- Sync: `client.teams.add_team_member(team_id=..., user_id=..., timeout=None)`
- Async: `await client.teams.add_team_member(team_id=..., user_id=..., timeout=None)`
- Raw payload: `client.teams.add_team_member.raw(team_id=..., user_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/teams/{teamId}/members/{userId}`
- Source controller: `IncidentIQ API`

Add team member

Adds a specific user to a team. Use this for individual onboarding or when granting access without a batch update.

**Prerequisites**
1. **teamId** - Use [GET /api/v1.0/teams](#/Teams/listTeams) or [GET /api/v1.0/teams/all](#/Teams/listAllTeams) to list teams and extract `Items[].TeamId`.
2. **userId** - Use [POST /api/v1.0/search](#/Users/searchUsers) to find the user and extract `Item.Users[].UserId`.

**Workflow Example**
1. Identify the teamId and userId.
2. [POST /api/v1.0/teams/{teamId}/members/{userId}](#/Teams/addTeamMember) to add the user.
3. Verify membership with [GET /api/v1.0/teams/{teamId}/members](#/Teams/listTeamMembers).

**Minimal Required Fields**: `teamId` (path), `userId` (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `team_id` | `teamId` | `path` | `yes` | `str` | `-` | - |
| `user_id` | `userId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `add_team_members`

Provenance: Golden OpenAPI contract

Operation ID: `addTeamMembers`

- Sync: `client.teams.add_team_members(body=None, timeout=None)`
- Async: `await client.teams.add_team_members(body=None, timeout=None)`
- Raw payload: `client.teams.add_team_members.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/teams/members`
- Source controller: `IncidentIQ API`

Add members to teams

Adds one or more users to one or more teams in a single batch request. Use this to bulk-assign teams during onboarding or to sync memberships from an external source.

**Prerequisites**
1. **TeamId** - Use [GET /api/v1.0/teams](#/Teams/listTeams) or [GET /api/v1.0/teams/all](#/Teams/listAllTeams) to list teams and extract `Items[].TeamId`.
2. **UserId** - Use [POST /api/v1.0/search](#/Users/searchUsers) to find users and extract `Item.Users[].UserId`.

**Workflow Example**
1. Gather TeamId and UserId pairs.
2. POST the TeamMember array to /api/v1.0/teams/members.
3. Confirm the additions with [GET /api/v1.0/teams/{teamId}/members](#/Teams/listTeamMembers).

**Minimal Required Fields**: for each array item include `TeamId` and `UserId`.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `TeamMemberListRequest` | `TeamMemberListRequest` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `clear_team_members`

Provenance: Golden OpenAPI contract

Operation ID: `clearTeamMembers`

- Sync: `client.teams.clear_team_members(team_id=..., timeout=None)`
- Async: `await client.teams.clear_team_members(team_id=..., timeout=None)`
- Raw payload: `client.teams.clear_team_members.raw(team_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/teams/{teamId}/clear-members`
- Source controller: `IncidentIQ API`

Clear team members

Removes all members from a team in a single action. Use this for seasonal resets or before decommissioning a team.

**Prerequisites**
1. **teamId** - Use [GET /api/v1.0/teams](#/Teams/listTeams) or [GET /api/v1.0/teams/all](#/Teams/listAllTeams) to list teams and extract `Items[].TeamId`.

**Workflow Example**
1. Review current membership: [GET /api/v1.0/teams/{teamId}/members](#/Teams/listTeamMembers).
2. [POST /api/v1.0/teams/{teamId}/clear-members](#/Teams/clearTeamMembers).
3. Confirm the team is empty with a follow-up GET.

**Minimal Required Fields**: `teamId` (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `team_id` | `teamId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_team`

Provenance: Golden OpenAPI contract

Operation ID: `createTeam`

- Sync: `client.teams.create_team(body=None, timeout=None)`
- Async: `await client.teams.create_team(body=None, timeout=None)`
- Raw payload: `client.teams.create_team.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/teams/new`
- Source controller: `IncidentIQ API`
- Aliases: `create`

Create team

Creates a new team definition that can be used for ticket routing, access control, and membership assignments.

**Prerequisites**
- None.

**Workflow Example**
1. Choose a team name and optional description.
2. [POST /api/v1.0/teams/new](#/Teams/createTeam) with `TeamName` (and optional `Description`).
3. Use the returned TeamId to add members via /api/v1.0/teams/{teamId}/members/{userId}.

**Minimal Required Fields**: `TeamName`.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `TeamRequest` | `TeamRequest` | - |

#### Returns

- Typed call return: `TeamDetailResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TeamDetailResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_team`

Provenance: Golden OpenAPI contract

Operation ID: `deleteTeam`

- Sync: `client.teams.delete_team(team_id=..., timeout=None)`
- Async: `await client.teams.delete_team(team_id=..., timeout=None)`
- Raw payload: `client.teams.delete_team.raw(team_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/teams/{teamId}`
- Source controller: `IncidentIQ API`

Delete team

Soft-deletes a team so it no longer appears in team lists or selection UI, without permanently removing its history.

**Prerequisites**
1. **teamId** - Use [GET /api/v1.0/teams](#/Teams/listTeams) or [GET /api/v1.0/teams/all](#/Teams/listAllTeams) to list teams and extract `Items[].TeamId`.

**Workflow Example**
1. List teams and choose the teamId to delete.
2. [DELETE /api/v1.0/teams/{teamId}](#/Teams/deleteTeam).
3. Confirm removal by listing teams again.

**Minimal Required Fields**: `teamId` (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `team_id` | `teamId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_team_members`

Provenance: Golden OpenAPI contract

Operation ID: `deleteTeamMembers`

- Sync: `client.teams.delete_team_members(body=None, timeout=None)`
- Async: `await client.teams.delete_team_members(body=None, timeout=None)`
- Raw payload: `client.teams.delete_team_members.raw(body=None, timeout=None)`
- HTTP route: `DELETE /api/v1.0/teams/members`
- Source controller: `IncidentIQ API`

Remove members from teams

Removes one or more users from one or more teams in a single batch request. Use this when offboarding staff, removing temporary access, or syncing memberships from an external roster.

**Prerequisites**
1. **TeamId** - Use [GET /api/v1.0/teams](#/Teams/listTeams) or [GET /api/v1.0/teams/all](#/Teams/listAllTeams) to list teams and extract `Items[].TeamId`.
2. **UserId** - Use [POST /api/v1.0/search](#/Users/searchUsers) to find users and extract `Item.Users[].UserId`.

**Workflow Example**
1. Identify the team and user IDs to remove.
2. POST a TeamMember list to [DELETE /api/v1.0/teams/members](#/Teams/deleteTeamMembers).
3. Verify membership with [GET /api/v1.0/teams/{teamId}/members](#/Teams/listTeamMembers).

**Minimal Required Fields**: for each array item include `TeamId` and `UserId`.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `TeamMemberListRequest` | `TeamMemberListRequest` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_team`

Provenance: Golden OpenAPI contract

Operation ID: `getTeam`

- Sync: `client.teams.get_team(team_id=..., timeout=None)`
- Async: `await client.teams.get_team(team_id=..., timeout=None)`
- Raw payload: `client.teams.get_team.raw(team_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/teams/{teamId}`
- Source controller: `IncidentIQ API`

Get team

Retrieves details for a specific team, including name, description, and status fields needed for configuration and display.

**Prerequisites**
1. **teamId** - Use [GET /api/v1.0/teams](#/Teams/listTeams) or [GET /api/v1.0/teams/all](#/Teams/listAllTeams) to list teams and extract `Items[].TeamId`.

**Workflow Example**
1. List teams to get a teamId.
2. [GET /api/v1.0/teams/{teamId}](#/Teams/getTeam) to retrieve details.

**Minimal Required Fields**: `teamId` (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `team_id` | `teamId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `TeamDetailResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TeamDetailResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_all_teams`

Provenance: Golden OpenAPI contract

Operation ID: `listAllTeams`

- Sync: `client.teams.list_all_teams(timeout=None)`
- Async: `await client.teams.list_all_teams(timeout=None)`
- Raw payload: `client.teams.list_all_teams.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/teams/all`
- Source controller: `IncidentIQ API`

List all teams

Retrieves all teams without pagination. Use this when you need a complete team catalog for selection or synchronization jobs.

**Prerequisites**
- None. Authentication scopes which teams appear.

**Workflow Example**
1. Call [GET /api/v1.0/teams/all](#/Teams/listAllTeams) to load the full list.
2. Use `Items[].TeamId` to fetch details or manage membership.

**Minimal Required Fields**: none.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `TeamListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TeamListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_my_teams`

Provenance: Golden OpenAPI contract

Operation ID: `listMyTeams`

- Sync: `client.teams.list_my_teams(timeout=None)`
- Async: `await client.teams.list_my_teams(timeout=None)`
- Raw payload: `client.teams.list_my_teams.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/teams/my`
- Source controller: `IncidentIQ API`

List my teams

Retrieves the teams the authenticated user belongs to. Use this for user profile views, access scoping, or to determine which team queues should be visible.

**Prerequisites**
- None. The authenticated user is implied.

**Workflow Example**
1. Call [GET /api/v1.0/teams/my](#/Teams/listMyTeams) to retrieve memberships.
2. Use `Items[].TeamId` to view details or manage team resources.

**Minimal Required Fields**: none.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `TeamListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TeamListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_paged_team_members`

Provenance: Golden OpenAPI contract

Operation ID: `listPagedTeamMembers`

- Sync: `client.teams.list_paged_team_members(team_id=..., p=None, s=None, timeout=None)`
- Async: `await client.teams.list_paged_team_members(team_id=..., p=None, s=None, timeout=None)`
- Raw payload: `client.teams.list_paged_team_members.raw(team_id=..., p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v1.0/teams/{teamId}/paged-members`
- Source controller: `IncidentIQ API`

List team members (paged)

Retrieves team members with pagination. Use this when teams are large and you need consistent paging for UI or exports.

**Prerequisites**
1. **teamId** - Use [GET /api/v1.0/teams](#/Teams/listTeams) or [GET /api/v1.0/teams/all](#/Teams/listAllTeams) to list teams and extract `Items[].TeamId`.

**Workflow Example**
1. Choose a teamId.
2. [GET /api/v1.0/teams/{teamId}/paged-members](#/Teams/listPagedTeamMembers) with `$p` and `$s`.
3. Page through results to retrieve all members.

**Minimal Required Fields**: `teamId` (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `team_id` | `teamId` | `path` | `yes` | `str` | `-` | - |
| `p` | `$p` | `query` | `no` | `int` | `-` | Page index (0-based) |
| `s` | `$s` | `query` | `no` | `int` | `-` | Page size |

#### Returns

- Typed call return: `TeamMembersResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TeamMembersResponse`
- Pagination helper: `client.teams.list_paged_team_members.iter_pages(start_page=1, page_size=100, max_pages=None, team_id=..., p=None, s=None, timeout=None)`

---

### `list_team_members`

Provenance: Golden OpenAPI contract

Operation ID: `listTeamMembers`

- Sync: `client.teams.list_team_members(team_id=..., timeout=None)`
- Async: `await client.teams.list_team_members(team_id=..., timeout=None)`
- Raw payload: `client.teams.list_team_members.raw(team_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/teams/{teamId}/members`
- Source controller: `IncidentIQ API`

List team members

Retrieves all members of a team. Use this to audit membership, drive UI lists, or gather UserId values for removal.

**Prerequisites**
1. **teamId** - Use [GET /api/v1.0/teams](#/Teams/listTeams) or [GET /api/v1.0/teams/all](#/Teams/listAllTeams) to list teams and extract `Items[].TeamId`.

**Workflow Example**
1. Select a teamId from the team list.
2. [GET /api/v1.0/teams/{teamId}/members](#/Teams/listTeamMembers) to retrieve members.

**Minimal Required Fields**: `teamId` (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `team_id` | `teamId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `TeamMembersResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TeamMembersResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_team_product_ids`

Provenance: Golden OpenAPI contract

Operation ID: `listTeamProductIds`

- Sync: `client.teams.list_team_product_ids(timeout=None)`
- Async: `await client.teams.list_team_product_ids(timeout=None)`
- Raw payload: `client.teams.list_team_product_ids.raw(timeout=None)`
- HTTP route: `POST /api/v1.0/teams/products/all/ids`
- Source controller: `IncidentIQ API`

List team product IDs

Retrieves the raw list of product IDs associated with teams. This is a compact form of the product listing used for syncing or authorization checks.

**Prerequisites**
- None.

**Workflow Example**
1. Call [POST /api/v1.0/teams/products/all/ids](#/Teams/listTeamProductIds).
2. Use the returned IDs to filter product-scoped operations.

**Minimal Required Fields**: none.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `ListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_team_products`

Provenance: Golden OpenAPI contract

Operation ID: `listTeamProducts`

- Sync: `client.teams.list_team_products(timeout=None)`
- Async: `await client.teams.list_team_products(timeout=None)`
- Raw payload: `client.teams.list_team_products.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/teams/products/all`
- Source controller: `IncidentIQ API`

List team products

Retrieves all product IDs associated with team functionality. Use this to understand which product contexts support team routing or to cache product identifiers for filtering.

**Prerequisites**
- None.

**Workflow Example**
1. Call [GET /api/v1.0/teams/products/all](#/Teams/listTeamProducts) to retrieve product IDs.
2. Store the results for filtering or UI labeling.

**Minimal Required Fields**: none.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `TeamProductListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TeamProductListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_teams`

Provenance: Golden OpenAPI contract

Operation ID: `listTeams`

- Sync: `client.teams.list_teams(p=None, s=None, timeout=None)`
- Async: `await client.teams.list_teams(p=None, s=None, timeout=None)`
- Raw payload: `client.teams.list_teams.raw(p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v1.0/teams`
- Source controller: `IncidentIQ API`

List teams

Retrieves a paginated list of teams available to the authenticated user. Use this endpoint to discover TeamId values for membership management, team detail lookups, or updates.

**Prerequisites**
- None. Authentication scopes which teams appear.

**Workflow Example**
1. List teams: [GET /api/v1.0/teams](#/Teams/listTeams) with `$p` and `$s` for paging.
2. Capture `Items[].TeamId` to use with [GET /api/v1.0/teams/{teamId}](#/Teams/getTeam) or membership endpoints.

**Minimal Required Fields**: none.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `p` | `$p` | `query` | `no` | `int` | `-` | Page index (0-based) |
| `s` | `$s` | `query` | `no` | `int` | `-` | Page size |

#### Returns

- Typed call return: `TeamListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TeamListResponse`
- Pagination helper: `client.teams.list_teams.iter_pages(start_page=1, page_size=100, max_pages=None, p=None, s=None, timeout=None)`

---

### `remove_team_member`

Provenance: Golden OpenAPI contract

Operation ID: `removeTeamMember`

- Sync: `client.teams.remove_team_member(team_id=..., user_id=..., timeout=None)`
- Async: `await client.teams.remove_team_member(team_id=..., user_id=..., timeout=None)`
- Raw payload: `client.teams.remove_team_member.raw(team_id=..., user_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/teams/{teamId}/members/{userId}`
- Source controller: `IncidentIQ API`

Remove team member

Removes a specific user from a team. Use this to revoke access or update team rosters one user at a time.

**Prerequisites**
1. **teamId** - Use [GET /api/v1.0/teams](#/Teams/listTeams) or [GET /api/v1.0/teams/all](#/Teams/listAllTeams) to list teams and extract `Items[].TeamId`.
2. **userId** - Use [GET /api/v1.0/teams/{teamId}/members](#/Teams/listTeamMembers) to list members or [POST /api/v1.0/search](#/Users/searchUsers) to find users.

**Workflow Example**
1. Identify the teamId and userId.
2. [DELETE /api/v1.0/teams/{teamId}/members/{userId}](#/Teams/removeTeamMember).
3. Confirm removal by listing team members.

**Minimal Required Fields**: `teamId` (path), `userId` (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `team_id` | `teamId` | `path` | `yes` | `str` | `-` | - |
| `user_id` | `userId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `undelete_team`

Provenance: Golden OpenAPI contract

Operation ID: `undeleteTeam`

- Sync: `client.teams.undelete_team(team_id=..., timeout=None)`
- Async: `await client.teams.undelete_team(team_id=..., timeout=None)`
- Raw payload: `client.teams.undelete_team.raw(team_id=..., timeout=None)`
- HTTP route: `PUT /api/v1.0/teams/{teamId}/undelete`
- Source controller: `IncidentIQ API`

Undelete team

Restores a previously soft-deleted team so it becomes visible in lists and can accept memberships again.

**Prerequisites**
1. **teamId** - Use [GET /api/v1.0/teams](#/Teams/listTeams) or [GET /api/v1.0/teams/all](#/Teams/listAllTeams) to find the teamId, including deleted teams if available.

**Workflow Example**
1. Delete a team: [DELETE /api/v1.0/teams/{teamId}](#/Teams/deleteTeam).
2. Restore it: [PUT /api/v1.0/teams/{teamId}/undelete](#/Teams/undeleteTeam).
3. Verify by fetching team details.

**Minimal Required Fields**: `teamId` (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `team_id` | `teamId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `TeamDetailResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TeamDetailResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_team`

Provenance: Golden OpenAPI contract

Operation ID: `updateTeam`

- Sync: `client.teams.update_team(team_id=..., body=None, timeout=None)`
- Async: `await client.teams.update_team(team_id=..., body=None, timeout=None)`
- Raw payload: `client.teams.update_team.raw(team_id=..., body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/teams/{teamId}`
- Source controller: `IncidentIQ API`

Update team

Updates an existing team's name or description. Use this to keep team metadata in sync with HR or organizational changes.

**Prerequisites**
1. **teamId** - Use [GET /api/v1.0/teams](#/Teams/listTeams) or [GET /api/v1.0/teams/all](#/Teams/listAllTeams) to list teams and extract `Items[].TeamId`.

**Workflow Example**
1. Fetch team details: [GET /api/v1.0/teams/{teamId}](#/Teams/getTeam).
2. Update `TeamName` or `Description` in the request body.
3. [POST /api/v1.0/teams/{teamId}](#/Teams/updateTeam) to save the changes.

**Minimal Required Fields**: `teamId` (path), `TeamName`.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `team_id` | `teamId` | `path` | `yes` | `str` | `-` | - |
| `body` | `body` | `body` | `no` | `TeamRequest` | `TeamRequest` | - |

#### Returns

- Typed call return: `TeamDetailResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TeamDetailResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_team_members`

Provenance: Golden OpenAPI contract

Operation ID: `updateTeamMembers`

- Sync: `client.teams.update_team_members(body=None, timeout=None)`
- Async: `await client.teams.update_team_members(body=None, timeout=None)`
- Raw payload: `client.teams.update_team_members.raw(body=None, timeout=None)`
- HTTP route: `PUT /api/v1.0/teams/members`
- Source controller: `IncidentIQ API`

Update team members

Updates team membership relationships for the supplied user/team pairs. Use this to reconcile membership state in bulk after a roster sync or when applying policy-driven changes.

**Prerequisites**
1. **TeamId** - Use [GET /api/v1.0/teams](#/Teams/listTeams) or [GET /api/v1.0/teams/all](#/Teams/listAllTeams) to list teams and extract `Items[].TeamId`.
2. **UserId** - Use [POST /api/v1.0/search](#/Users/searchUsers) to find users and extract `Item.Users[].UserId`.

**Workflow Example**
1. Build the desired TeamId/UserId pairs.
2. [PUT /api/v1.0/teams/members](#/Teams/updateTeamMembers) with the TeamMember list.
3. Validate results with [GET /api/v1.0/teams/{teamId}/members](#/Teams/listTeamMembers).

**Minimal Required Fields**: for each array item include `TeamId` and `UserId`.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `TeamMemberListRequest` | `TeamMemberListRequest` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
