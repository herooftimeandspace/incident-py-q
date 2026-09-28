# `tickets` Golden Namespace

Sync client access: `client.tickets`

Async client access: `client.tickets` with `await` on method calls.

These methods are Golden because they come from the bundled Incident IQ OpenAPI contract.

## Methods

### `add_ticket_follower_team`

Provenance: Golden OpenAPI contract

Operation ID: `addTicketFollowerTeam`

- Sync: `client.tickets.add_ticket_follower_team(ticket_id=..., team_id=..., timeout=None)`
- Async: `await client.tickets.add_ticket_follower_team(ticket_id=..., team_id=..., timeout=None)`
- Raw payload: `client.tickets.add_ticket_follower_team.raw(ticket_id=..., team_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/followers/team/{teamId}`
- Source controller: `IncidentIQ API`

Add team as ticket followers

Adds all members of a team as followers to a ticket, enabling the entire team to receive notifications about ticket updates, comments, and status changes. This is efficient for keeping cross-functional teams informed without adding individual followers.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to find the ticket and extract `Items[].TicketId`.
2. **teamId** – Use [GET /api/v1.0/teams](#/Teams/listTeams) to list available teams and extract `TeamId`.

**Workflow Example**
1. Locate ticket: [POST /api/v1.0/tickets](#/Tickets/searchTickets) → extract `TicketId`
2. Find team: [GET /api/v1.0/teams](#/Teams/listTeams) → select `TeamId` for the team needing visibility
3. Add team: [POST /api/v1.0/tickets/{ticketId}/followers/team/{teamId}](#/Tickets/addTicketFollowerTeam)
4. Verify: [GET /api/v1.0/tickets/{ticketId}/followers](#/Tickets/getTicketFollowers) to confirm team members added

**Use Cases**: Keeping support teams informed about escalated issues, notifying project teams about related tickets, ensuring stakeholder groups receive updates.

**Note**: New team members added after this call will not automatically become followers; re-add the team to include them.

**Related Endpoints**
- [DELETE /api/v1.0/tickets/{ticketId}/followers/team/{teamId}](#/Tickets/removeTicketFollowerTeam) – Remove team as followers
- [POST /api/v1.0/tickets/{ticketId}/followers/{userId}](#/Tickets/addTicketFollowerUser) – Add individual follower
- [GET /api/v1.0/teams](#/Teams/listTeams) – List available teams

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | Unique identifier of the ticket |
| `team_id` | `teamId` | `path` | `yes` | `str` | `-` | Unique identifier of the team to add as followers |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `add_ticket_follower_user`

Provenance: Golden OpenAPI contract

Operation ID: `addTicketFollowerUser`

- Sync: `client.tickets.add_ticket_follower_user(ticket_id=..., user_id=..., timeout=None)`
- Async: `await client.tickets.add_ticket_follower_user(ticket_id=..., user_id=..., timeout=None)`
- Raw payload: `client.tickets.add_ticket_follower_user.raw(ticket_id=..., user_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/followers/user/{userId}`
- Source controller: `IncidentIQ API`

Add user as ticket follower

Adds a user as a follower to a ticket. The user will receive email and in-app notifications about ticket updates, allowing them to stay informed without being directly assigned.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to find the ticket and extract `Items[].TicketId`.
2. **userId** – Use [POST /api/v1.0/search](#/Search/globalSearch) or [POST /api/v1.0/users](#/Users/searchUsers) to find the user and extract `Item.Users[].UserId`.

**Workflow Example**
1. Find ticket: [POST /api/v1.0/tickets](#/Tickets/searchTickets) → extract `TicketId`
2. Find user: [POST /api/v1.0/search](#/Search/globalSearch) with user name → extract `UserId`
3. Add follower: [POST /api/v1.0/tickets/{ticketId}/followers/user/{userId}](#/Tickets/addTicketFollowerUser)
4. Verify: [GET /api/v1.0/tickets/{ticketId}/followers](#/Tickets/getTicketFollowers) to confirm addition

**Use Cases**: Keeping managers informed, adding subject matter experts for visibility, notifying stakeholders of progress.

**Related Endpoints**
- [GET /api/v1.0/tickets/{ticketId}/followers](#/Tickets/getTicketFollowers) – List current followers
- [DELETE /api/v1.0/tickets/{ticketId}/followers/user/{userId}](#/Tickets/removeTicketFollowerUser) – Remove follower
- [POST /api/v1.0/tickets/{ticketId}/followers/team/{teamId}](#/Tickets/addTicketFollowerTeam) – Add team as followers

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | Unique identifier of the ticket |
| `user_id` | `userId` | `path` | `yes` | `str` | `-` | Unique identifier of the user to add as follower |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `add_ticket_tag`

Provenance: Golden OpenAPI contract

Operation ID: `addTicketTag`

- Sync: `client.tickets.add_ticket_tag(ticket_id=..., tag_id=..., timeout=None)`
- Async: `await client.tickets.add_ticket_tag(ticket_id=..., tag_id=..., timeout=None)`
- Raw payload: `client.tickets.add_ticket_tag.raw(ticket_id=..., tag_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/tags/{tagId}`
- Source controller: `IncidentIQ API`

Add tag to ticket

Adds a tag to a ticket for categorization and filtering purposes.

**Prerequisites**
- Obtain available tags from tag management endpoints or create new tags as needed

**Related Endpoints**
- [DELETE /api/v1.0/tickets/{ticketId}/tags/{tagId}](#/Tickets/removeTicketTag) – Remove a tag
- [POST /api/v1.0/tickets/{ticketId}/tags](#/Tickets/updateTicketTags) – Bulk update tags

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | Unique identifier of the ticket |
| `tag_id` | `tagId` | `path` | `yes` | `str` | `-` | Unique identifier of the tag to add |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `assign_ticket`

Provenance: Golden OpenAPI contract

Operation ID: `assignTicket`

- Sync: `client.tickets.assign_ticket(ticket_id=..., body=..., timeout=None)`
- Async: `await client.tickets.assign_ticket(ticket_id=..., body=..., timeout=None)`
- Raw payload: `client.tickets.assign_ticket.raw(ticket_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/assign`
- Source controller: `IncidentIQ API`

Assign ticket

Assigns a ticket to a user, team, workpackage, SLA, parent ticket, or related ticket. All assignment targets are optional - specify the ones you want to set. Use `ClearUser` or `ClearTeam` to remove existing assignments without setting new ones.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to locate the ticket and extract `Items[].TicketId`.
2. **AssignToUserId** (optional) – Use [POST /api/v1.0/search](#/Users/searchUsers) to locate the target agent.
3. **AssignToTeamId** (optional) – Use [GET /api/v1.0/teams](#/Teams/listTeams) to locate the target team.
4. **AssignToSlaId** (optional) – Use [GET /api/v1.0/slas](#/SLAs/listSlas) to locate the target SLA.

**Workflow Examples**

*Assign to user:*
1. Locate ticket: [POST /api/v1.0/tickets](#/Tickets/searchTickets) → extract `TicketId`
2. Find agent: [POST /api/v1.0/search](#/Search/globalSearch) → extract `UserId`
3. Submit: `{ "TicketId": "...", "AssignToUserId": "..." }`

*Assign to team:*
1. Locate ticket and team
2. Submit: `{ "TicketId": "...", "AssignToTeamId": "..." }`

*Clear user assignment:*
1. Submit: `{ "TicketId": "...", "ClearUser": true }`

**Minimal Required Fields**: TicketId (plus at least one assignment target or clear flag)

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | UUID of the ticket to assign. Obtain via POST /api/v1.0/tickets and extract `Items[].TicketId`. |
| `body` | `body` | `body` | `yes` | `TicketAssignRequest` | `TicketAssignRequest` | - |

#### Returns

- Typed call return: `TicketAssignResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketAssignResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `assign_ticket_sla`

Provenance: Golden OpenAPI contract

Operation ID: `assignTicketSla`

- Sync: `client.tickets.assign_ticket_sla(ticket_id=..., body=..., timeout=None)`
- Async: `await client.tickets.assign_ticket_sla(ticket_id=..., body=..., timeout=None)`
- Raw payload: `client.tickets.assign_ticket_sla.raw(ticket_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/sla`
- Source controller: `IncidentIQ API`

Assign SLA to ticket

Assigns a Service Level Agreement (SLA) to a ticket. The SLA defines response time and resolution time targets for the ticket.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to find the ticket and extract `Items[].TicketId`.
2. **SlaId** – Use [GET /api/v1.0/slas](#/Slas/listSlas) to list available SLAs and extract `Items[].SlaId`.

**Workflow Example**
1. Search for the ticket: [POST /api/v1.0/tickets](#/Tickets/searchTickets) with appropriate filters.
2. List available SLAs: [GET /api/v1.0/slas](#/Slas/listSlas) to find the appropriate SLA for the ticket type.
3. Assign the SLA: POST /api/v1.0/tickets/{ticketId}/sla with the selected `SlaId`.
4. Verify assignment: [GET /api/v1.0/tickets/{ticketId}/sla](#/Tickets/getTicketSla) to confirm the SLA timers are now active.

**Minimal Required Fields**: SlaId

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | UUID of the ticket to assign the SLA to. Obtain via POST /api/v1.0/tickets and read `Items[].TicketId`. |
| `body` | `body` | `body` | `yes` | `SlaAssignRequest` | `SlaAssignRequest` | SLA to assign to the ticket. Only the SlaId field is required. |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `cancel_ticket`

Provenance: Golden OpenAPI contract

Operation ID: `cancelTicket`

- Sync: `client.tickets.cancel_ticket(ticket_id=..., body=None, timeout=None)`
- Async: `await client.tickets.cancel_ticket(ticket_id=..., body=None, timeout=None)`
- Raw payload: `client.tickets.cancel_ticket.raw(ticket_id=..., body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/cancel`
- Source controller: `IncidentIQ API`

Cancel ticket

Cancels a ticket, moving it to a canceled/closed state. Use this endpoint when a ticket should be terminated without resolution (e.g., duplicate, no longer needed, submitted in error).

**Prerequisites**
- Optionally retrieve close reasons from [GET /api/v1.0/resolutions/close-reason-types](#/Tickets/getCloseReasonTypes) to specify a cancellation reason

**Workflow Example**
1. List close reasons: [GET /api/v1.0/resolutions/close-reason-types](#/Tickets/getCloseReasonTypes) → select appropriate `CloseReasonTypeId`
2. Cancel ticket: [POST /api/v1.0/tickets/{ticketId}/cancel](#/Tickets/cancelTicket) with optional reason and comments

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | Unique identifier of the ticket to cancel |
| `body` | `body` | `body` | `no` | `TicketCancelOptions` | `TicketCancelOptions` | Optional cancel options including close reason identifier. |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `change_ticket_activity_visibility`

Provenance: Golden OpenAPI contract

Operation ID: `changeTicketActivityVisibility`

- Sync: `client.tickets.change_ticket_activity_visibility(ticket_id=..., ticket_activity_id=..., body=..., timeout=None)`
- Async: `await client.tickets.change_ticket_activity_visibility(ticket_id=..., ticket_activity_id=..., body=..., timeout=None)`
- Raw payload: `client.tickets.change_ticket_activity_visibility.raw(ticket_id=..., ticket_activity_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/activities/{ticketActivityId}/visibility`
- Source controller: `IncidentIQ API`

Change activity visibility

Changes the visibility of a ticket activity between public and private, allowing agents to expose a note to the requester or keep it internal. Public activities are visible to the ticket requester; private activities are restricted to agents and administrators.

**Prerequisites**
1. **ticketId** - Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to locate the ticket and extract `Items[].TicketId`.
2. **ticketActivityId** - Use [GET /api/v1.0/tickets/{ticketId}/timeline](#/Tickets/getTicketTimeline) or [GET /api/v1.0/tickets/{ticketId}/activities](#/Tickets/getTicketActivities) to find the activity and extract `TicketActivityId`.

**Workflow Example**
1. Identify the ticket and activity in the timeline.
2. [POST /api/v1.0/tickets/{ticketId}/activities/{ticketActivityId}/visibility](#/Tickets/changeTicketActivityVisibility) with `true` to make the activity public or `false` to keep it private.
3. Refresh the timeline to confirm the visibility change.

**Minimal Required Fields**: ticketId, ticketActivityId (path), and visibility boolean in the request body.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | Unique identifier of the ticket |
| `ticket_activity_id` | `ticketActivityId` | `path` | `yes` | `str` | `-` | Unique identifier of the activity |
| `body` | `body` | `body` | `yes` | `bool` | `-` | Boolean indicating whether the activity should be public (true) or private (false) |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `change_ticket_approver`

Provenance: Golden OpenAPI contract

Operation ID: `changeTicketApprover`

- Sync: `client.tickets.change_ticket_approver(ticket_id=..., body=..., timeout=None)`
- Async: `await client.tickets.change_ticket_approver(ticket_id=..., body=..., timeout=None)`
- Raw payload: `client.tickets.change_ticket_approver.raw(ticket_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/workflow/approval/change`
- Source controller: `IncidentIQ API`

Change ticket approver

Changes the approver assignment for a ticket that is currently in an approval workflow state. Use this to reassign approval responsibility to a different user or team.

**Behavior**
- Only works when ticket is in an approval-pending workflow state
- Can change individual user approver, team approver, or both
- Original approver is removed when new approver is assigned

**Use Cases**
- Reassigning approval when original approver is unavailable
- Escalating to a different approval authority
- Transferring approval responsibility between teams

**Prerequisites**
- Ticket must be in a workflow state awaiting approval
- Obtain user IDs via [POST /api/v1.0/search](#/Users/searchUsers)
- Obtain team IDs via team management endpoints

**Related Endpoints**
- [POST /api/v1.0/tickets/{ticketId}/workflow/approval](#/Tickets/sendTicketForApproval) – Initial approval request
- [DELETE /api/v1.0/tickets/{ticketId}/workflow/delete](#/Tickets/deleteWorkflowApproval) – Cancel pending approval

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | UUID of the ticket with pending approval |
| `body` | `body` | `body` | `yes` | `SendTicketForApprovalRequest` | `SendTicketForApprovalRequest` | Approver change details |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `change_ticket_issue`

Provenance: Golden OpenAPI contract

Operation ID: `changeTicketIssue`

- Sync: `client.tickets.change_ticket_issue(ticket_id=..., body=..., timeout=None)`
- Async: `await client.tickets.change_ticket_issue(ticket_id=..., body=..., timeout=None)`
- Raw payload: `client.tickets.change_ticket_issue.raw(ticket_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/issue`
- Source controller: `IncidentIQ API`

Change ticket issue type

Updates the issue type for a ticket. Use this to re-categorize tickets when the initial issue classification was incorrect or needs refinement.

**Prerequisites**
- Obtain available issues from [POST /api/v1.0/issues](#/Issues/searchIssues) or [GET /api/v1.0/issues](#/Issues/listIssues)
- Extract the `IssueId` for the desired issue type

**Workflow Example**
1. Search issues: [POST /api/v1.0/issues](#/Issues/searchIssues) → select appropriate `IssueId`
2. Update ticket issue: [POST /api/v1.0/tickets/{ticketId}/issue](#/Tickets/changeTicketIssue)

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | Unique identifier of the ticket to update |
| `body` | `body` | `body` | `yes` | `SetTicketIssueRequest` | `SetTicketIssueRequest` | Issue update request containing the new issue identifier |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `close_ticket`

Provenance: Golden OpenAPI contract

Operation ID: `closeTicket`

- Sync: `client.tickets.close_ticket(ticket_id=..., body=None, timeout=None)`
- Async: `await client.tickets.close_ticket(ticket_id=..., body=None, timeout=None)`
- Raw payload: `client.tickets.close_ticket.raw(ticket_id=..., body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/close`
- Source controller: `IncidentIQ API`

Resolve ticket

Resolves a ticket and marks it closed using workflow resolution settings.

**Prerequisites**
1. **ticketId** – Locate the ticket via [POST /api/v1.0/tickets](#/Tickets/searchTickets) and extract `Items[].TicketId`.
2. **CloseReasonTypeId** (optional) – Call [GET /api/v1.0/workflows/steps](#/Workflows/getWorkflowSteps) to review available close reasons and select a `CloseReasonTypeId` if the workflow requires one.

**Workflow Example**
1. Identify ticket to resolve: [POST /api/v1.0/tickets](#/Tickets/searchTickets) with filters for pending resolution → collect `Items[].TicketId`.
2. Review current state: [GET /api/v1.0/tickets/{ticketId}](#/Tickets/getTicket) and [GET /api/v1.0/tickets/{ticketId}/status](#/Tickets/getTicketStatus) to ensure all next steps are completed.
3. (Optional) Load close reasons via [GET /api/v1.0/workflows/steps](#/Workflows/getWorkflowSteps) and choose an appropriate `CloseReasonTypeId`.
4. Submit closure: [POST /api/v1.0/tickets/{ticketId}/close](#/Tickets/closeTicket) with the optional close reason payload to mark the ticket resolved.
5. Refresh ticket context: [GET /api/v1.0/tickets/{ticketId}/next-steps](#/Tickets/getTicketNextSteps) and [POST /api/v1.0/tickets/{ticketId}/timeline](#/Tickets/listTicketTimeline) to verify closure activities are recorded.

**Minimal Required Fields**: ticketId (path). Optional body: CloseReasonTypeId.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | UUID of the ticket to close. Obtain via POST /api/v1.0/tickets and extract `Items[].TicketId`. |
| `body` | `body` | `body` | `no` | `TicketCloseRequest` | `TicketCloseRequest` | Optional closure metadata such as close reason identifiers. |

#### Returns

- Typed call return: `TicketCloseResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketCloseResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `confirm_ticket_issue`

Provenance: Golden OpenAPI contract

Operation ID: `confirmTicketIssue`

- Sync: `client.tickets.confirm_ticket_issue(ticket_id=..., timeout=None)`
- Async: `await client.tickets.confirm_ticket_issue(ticket_id=..., timeout=None)`
- Raw payload: `client.tickets.confirm_ticket_issue.raw(ticket_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/confirm-issue`
- Source controller: `IncidentIQ API`

Confirm ticket issue

Confirms the selected issue (problem category) on a ticket before work begins.

**Prerequisites**
1. **ticketId** – Locate the ticket via [POST /api/v1.0/tickets](#/Tickets/searchTickets) and extract `Items[].TicketId`.
2. **Issue selection** – Ensure the ticket already has the appropriate issue assigned (for example during creation or via the issue picker UI).

**Workflow Example**
1. Search for the ticket: [POST /api/v1.0/tickets](#/Tickets/searchTickets) with queue filters → capture `Items[0].TicketId`.
2. Present the issue confirmation dialog to the technician.
3. Call [POST /api/v1.0/tickets/{ticketId}/confirm-issue](#/Tickets/confirmTicketIssue) to acknowledge the chosen issue.
4. Immediately follow with [POST /api/v1.0/tickets/{ticketId}/start](#/Tickets/startTicket) so timers, permissions, and recommended next steps refresh for the technician.

**Minimal Required Fields**: ticketId

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | UUID of the ticket whose issue should be confirmed. Obtain via POST /api/v1.0/tickets and extract `Items[].TicketId`. |

#### Returns

- Typed call return: `TicketIssueConfirmationResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketIssueConfirmationResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `copy_ticket`

Provenance: Golden OpenAPI contract

Operation ID: `copyTicket`

- Sync: `client.tickets.copy_ticket(ticket_id=..., body=..., timeout=None)`
- Async: `await client.tickets.copy_ticket(ticket_id=..., body=..., timeout=None)`
- Raw payload: `client.tickets.copy_ticket.raw(ticket_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/copy`
- Source controller: `IncidentIQ API`

Copy ticket

Copies an existing ticket to create a new ticket while optionally inheriting select attributes.

**Prerequisites**
1. **ticketId** - Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to locate the source ticket and extract `Items[].TicketId`.

**Workflow Example**
1. Identify the ticket to duplicate: [POST /api/v1.0/tickets](#/Tickets/searchTickets) with relevant filters and capture `Items[0].TicketId`.
2. Decide which fields to carry forward (requestor, priority, assignment) and set the matching booleans in the request body.
3. Submit [POST /api/v1.0/tickets/{ticketId}/copy](#/Tickets/copyTicket) and read `Items[0].TicketId` in the response to reference the new ticket copy.

**Minimal Required Fields**: ticketId

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | UUID of the ticket to duplicate. Obtain via POST /api/v1.0/tickets and extract `Items[].TicketId`. |
| `body` | `body` | `body` | `yes` | `TicketCopyRequest` | `TicketCopyRequest` | - |

#### Returns

- Typed call return: `TicketListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_simple_ticket`

Provenance: Golden OpenAPI contract

Operation ID: `createSimpleTicket`

- Sync: `client.tickets.create_simple_ticket(body=..., timeout=None)`
- Async: `await client.tickets.create_simple_ticket(body=..., timeout=None)`
- Raw payload: `client.tickets.create_simple_ticket.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/simple/new`
- Source controller: `IncidentIQ API`

Create ticket (simplified)

Creates a new ticket using simplified string-based identifiers rather than UUIDs. This endpoint is designed for quick ticket creation when you have human-readable identifiers like usernames, asset tags, and issue names.

**Key Differences from Standard Ticket Creation**
- Uses `ForUsername` (email) instead of `ForId` (UUID)
- Uses `AssetTag` instead of asset UUIDs
- Uses `Issue` name instead of `IssueId`

The system automatically resolves these identifiers to their corresponding UUIDs.

**Use Cases**
- Programmatic ticket creation from external systems
- Batch import scenarios where UUIDs are not readily available
- Integration with systems that track users by email and assets by tag

**Prerequisites**
- The user specified by `ForUsername` must exist in the system
- If provided, the `AssetTag` must match an existing asset
- The `Issue` name must match an existing issue type

**Related Endpoints**
- [POST /api/v1.0/tickets/new](#/Tickets/createTicket) – Standard ticket creation with UUID references

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `SimpleTicketRequest` | `SimpleTicketRequest` | Simplified ticket creation payload using string identifiers |

#### Returns

- Typed call return: `SimpleTicketCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `SimpleTicketCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_ticket`

Provenance: Golden OpenAPI contract

Operation ID: `createTicket`

- Sync: `client.tickets.create_ticket(api_flags=None, body=..., timeout=None)`
- Async: `await client.tickets.create_ticket(api_flags=None, body=..., timeout=None)`
- Raw payload: `client.tickets.create_ticket.raw(api_flags=None, body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/new`
- Source controller: `IncidentIQ API`

Create ticket

Creates a new ticket with subject, requester, location, and issue metadata.

**Prerequisites**
1. **ForId** – Use [POST /api/v1.0/search](#/Users/searchUsers) to locate the requester and extract `Item.Users[].UserId`.
2. **Asset metadata** – Use [GET /api/v1.0/assets/assettag/{tag}](#/Assets/getAssetByTag) or [GET /api/v1.0/assets/for/{userId}/{all}](#/Assets/getUserFavoriteAssets) to obtain `AssetId`, `LocationId`, and `LocationRoomId`.
3. **Model selection** – Call [GET /api/v1.0/assets/types](#/Assets/listAssetTypes) followed by [POST /api/v1.0/issues/for/models](#/Model Issues/getIssuesForModels) to retrieve a Chromebook `ModelId`; optionally verify details with [GET /api/v1.0/issues/for/models/{modelId}](#/Model Issues/getIssuesForModel).
4. **Issue selection** – Call [POST /api/v1.0/issues/for/models/link](#/Model Issues/searchModelIssues) with the chosen `ModelId` to obtain an `IssueId`/`IssueTypeId`.

**Workflow Example**
1. Search requester: [POST /api/v1.0/search](#/Search/globalSearch) → extract `Item.Users[0].UserId` for `ForId`.
2. Identify device: [GET /api/v1.0/assets/assettag/{tag}](#/Assets/getAssetByTag) → record `AssetId`, `LocationId`, `LocationRoomId`.
3. Select model: GET asset types → [POST /api/v1.0/issues/for/models](#/Model Issues/getIssuesForModels) (facet `assettype`) → choose `ModelId`.
4. Retrieve issue: [POST /api/v1.0/issues](#/Issues/searchIssues) with `ModelIds` array → select appropriate `IssueId`.
5. Submit creation request: [POST /api/v1.0/tickets/new](#/Tickets/createTicket) with the collected identifiers plus `Subject` and `IssueDescription`.

**Minimal Required Fields**: Subject, IssueDescription, IssueId, ForId

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `api_flags` | `ApiFlags` | `header` | `no` | `str` | `-` | Optional flag to control field mapping behavior. When set to `OnlySetMappedProperties`, only fields explicitly included in the request payload will be set; other fields will use system defaults rather than being explicitly set to null. |
| `body` | `body` | `body` | `yes` | `TicketCreateRequest` | `TicketCreateRequest` | Ticket creation payload including requester, issue metadata, optional assets, and custom fields. |

#### Returns

- Typed call return: `TicketSingleResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketSingleResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_ticket_activity`

Provenance: Golden OpenAPI contract

Operation ID: `createTicketActivity`

- Sync: `client.tickets.create_ticket_activity(ticket_id=..., body=..., timeout=None)`
- Async: `await client.tickets.create_ticket_activity(ticket_id=..., body=..., timeout=None)`
- Raw payload: `client.tickets.create_ticket_activity.raw(ticket_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/activities/new`
- Source controller: `IncidentIQ API`

Add activity to ticket

Records a new activity entry (comment, internal note, or workflow event) against an existing ticket.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to locate the ticket and extract `Items[].TicketId`.
2. **Activity context** – Call [GET /api/v1.0/tickets/{ticketId}](#/Tickets/getTicket) if you need current assignment, status, or requester details before logging the activity.
3. **ResolutionActionId** (for activity type 8) – Call [GET /api/v1.0/resolutions/actions](#/Resolution%20Actions/listResolutionActions) and extract `Items[].ResolutionActionId` for the workflow resolution to apply.

**Workflow Example**
1. Locate ticket: [POST /api/v1.0/tickets](#/Tickets/searchTickets) with status/site filters → extract `Items[0].TicketId`.
2. (Optional) Inspect ticket: [GET /api/v1.0/tickets/{ticketId}](#/Tickets/getTicket) to confirm recipients or current step.
3. Retrieve resolution actions: [GET /api/v1.0/resolutions/actions](#/Tickets/listResolutionActions) → capture the desired `ResolutionActionId` when logging a workflow resolution.
4. Log update: [POST /api/v1.0/tickets/{ticketId}/activities/new](#/Tickets/createTicketActivity) with activity payload (message text, visibility flags, metadata, and optional resolution action details).

**Notification control**
Append `/true` or `/false` to the path (`/api/v1.0/tickets/{ticketId}/activities/new/{sendActivityEmail}`) when you must explicitly toggle ticket notifications. The default route (or `true`) applies `SendNotifications` and emails requesters/followers; passing `false` keeps notifications suppressed while still running automation rules.

**Automation behavior**
`TicketActivityManager.CreateTicketActivity` always runs workflow rules (RunRules flag). The service clones the top-level `IsPublic` value to every nested `ActivityItem`, so set it once to mark the entry as public or internal. Provide `OwnerId` to post on behalf of a service user; otherwise the authenticated user becomes the activity owner.

`ActivityItems[]` accepts either a comment payload (type 6) or resolution action payload (type 8). Each object must include the JSON.NET `$type` value shown in the schema so the API can deserialize the `ITicketActivityItem` interface.

**Minimal Required Fields**: ticketId (path), at least one TicketActivityCreateItem (comment or resolution action). Include `ResolutionActionId` when submitting a workflow resolution (TicketActivityTypeId 8).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | UUID of the ticket receiving the activity. Obtain via POST /api/v1.0/tickets and extract `Items[].TicketId`. |
| `body` | `body` | `body` | `yes` | `TicketActivityRequest` | `TicketActivityRequest` | - |

#### Returns

- Typed call return: `TicketActivityCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketActivityCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_ticket_activity_batch`

Provenance: Golden OpenAPI contract

Operation ID: `createTicketActivityBatch`

- Sync: `client.tickets.create_ticket_activity_batch(ticket_id=..., send_activity_email=None, body=..., timeout=None)`
- Async: `await client.tickets.create_ticket_activity_batch(ticket_id=..., send_activity_email=None, body=..., timeout=None)`
- Raw payload: `client.tickets.create_ticket_activity_batch.raw(ticket_id=..., send_activity_email=None, body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/activities/new-batch`
- Source controller: `IncidentIQ API`

Add batch of activities to ticket

Logs multiple activity entries (comments, updates, notes) to a ticket in a single request. This is more efficient than individual activity posts when recording multiple related updates, such as importing conversation history or logging a series of actions taken during troubleshooting.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to find the ticket and extract `Items[].TicketId`.

**Workflow Example**
1. Locate ticket: [POST /api/v1.0/tickets](#/Tickets/searchTickets) → extract `TicketId`
2. Prepare activities: Build array of activity objects with type, content, and visibility settings
3. Batch post: [POST /api/v1.0/tickets/{ticketId}/activities/new-batch](#/Tickets/createTicketActivityBatch) with activity array
4. View timeline: [GET /api/v1.0/tickets/{ticketId}/timeline](#/Tickets/getTicketTimeline) to confirm activities are recorded

**Query Parameters**: Set `sendActivityEmail=false` to suppress notifications for the batch (useful for imports or bulk operations).

**Request Body**: Array of activity objects, each specifying type, content, visibility, and optional attachments.

**Related Endpoints**
- [POST /api/v1.0/tickets/{ticketId}/activities/new](#/Tickets/createTicketActivity) – Add single activity
- [GET /api/v1.0/tickets/{ticketId}/timeline](#/Tickets/getTicketTimeline) – View activity history
- [POST /api/v1.0/tickets/{ticketId}/activities/{activityId}/send-notification](#/Tickets/sendTicketActivityNotification) – Send notification for activity

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | UUID of the ticket. |
| `send_activity_email` | `sendActivityEmail` | `query` | `no` | `bool` | `-` | Whether to send notification emails for these activities. |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | - |

#### Returns

- Typed call return: `list[Any]`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_ticket_next_step`

Provenance: Golden OpenAPI contract

Operation ID: `createTicketNextStep`

- Sync: `client.tickets.create_ticket_next_step(ticket_id=..., body=..., timeout=None)`
- Async: `await client.tickets.create_ticket_next_step(ticket_id=..., body=..., timeout=None)`
- Raw payload: `client.tickets.create_ticket_next_step.raw(ticket_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/next-steps/new`
- Source controller: `IncidentIQ API`

Create next step for ticket

Creates a new next step (task) for a ticket to track required work before resolution. Next steps help break down complex tickets into manageable, assignable tasks that can be completed by different team members or tracked against deadlines.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to find the ticket and extract `Items[].TicketId`.
2. **TicketNextStepTypeId** – Use [GET /api/v1.0/tickets/next-step/types](#/Tickets/listTicketNextStepTypes) to list available step types.

**Workflow Example**
1. Locate ticket: [POST /api/v1.0/tickets](#/Tickets/searchTickets) → extract `TicketId`
2. Choose step type: [GET /api/v1.0/tickets/next-step/types](#/Tickets/listTicketNextStepTypes) → select appropriate type
3. Create step: [POST /api/v1.0/tickets/{ticketId}/next-steps/new](#/Tickets/createTicketNextStep) with step details
4. View steps: [GET /api/v1.0/tickets/{ticketId}/next-steps](#/Tickets/getTicketNextSteps) to confirm creation

**Request Body**: Provide `Title`, `Description`, optional `AssignedUserId`, `DueDate`, and `TicketNextStepTypeId`.

**Use Cases**: Creating checklist items for complex troubleshooting, assigning follow-up tasks, tracking multi-step resolution processes.

**Related Endpoints**
- [GET /api/v1.0/tickets/{ticketId}/next-steps](#/Tickets/getTicketNextSteps) – List all next steps
- [POST /api/v1.0/tickets/{ticketId}/next-steps/{nextStepId}](#/Tickets/updateTicketNextStep) – Update a next step
- [GET /api/v1.0/tickets/next-step/types](#/Tickets/listTicketNextStepTypes) – List available step types

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | Unique identifier of the ticket |
| `body` | `body` | `body` | `yes` | `TicketNextStepRequest` | `TicketNextStepRequest` | - |

#### Returns

- Typed call return: `TicketNextStepCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketNextStepCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_ticket_next_step_template`

Provenance: Golden OpenAPI contract

Operation ID: `createTicketNextStepTemplate`

- Sync: `client.tickets.create_ticket_next_step_template(body=..., timeout=None)`
- Async: `await client.tickets.create_ticket_next_step_template(body=..., timeout=None)`
- Raw payload: `client.tickets.create_ticket_next_step_template.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/next-step/templates/new`
- Source controller: `IncidentIQ API`

Create a new ticket next step template

Creates a new ticket next step template. Templates define predefined workflows that can be applied to tickets during the resolution process.

**Prerequisites**
1. **ProductId** - Obtain via [GET /api/v1.0/products/all](#/Products/listProducts), extract `Items[].ProductId`.
2. **SiteId** (optional) - Obtain via [GET /api/v2.0/locations](#/Locations/getMyLocationsV2), extract `Items[].LocationId`.
3. **TicketNextStepTypeId** - Obtain via ticket next step type endpoints.

**Workflow Example**
1. Get product ID: `GET /api/v1.0/products` to select the appropriate product
2. (Optional) Get site ID: `GET /api/v2.0/locations` if creating a site-scoped template
3. Get next step type ID: Query available next step types
4. Create template: `POST /api/v1.0/tickets/next-step/templates/new` with required fields
5. Verify creation by fetching the returned template ID

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `TicketNextStepTemplateRequest` | `TicketNextStepTemplateRequest` | Template configuration for the new next step template. |

#### Returns

- Typed call return: `TicketNextStepTemplateItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketNextStepTemplateItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_ticket_view`

Provenance: Golden OpenAPI contract

Operation ID: `createTicketView`

- Sync: `client.tickets.create_ticket_view(body=..., timeout=None)`
- Async: `await client.tickets.create_ticket_view(body=..., timeout=None)`
- Raw payload: `client.tickets.create_ticket_view.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/views/new`
- Source controller: `IncidentIQ API`

Create ticket view

Creates a new saved ticket view that defines filters, columns, and sort order for the ticket queue. Views allow users to create personalized dashboards for managing their workload.

**Prerequisites**
1. **ProductId** – Use the ticket product ID (`88df910c-91aa-e711-80c2-0004ffa00010` for IncidentIQ Tickets).
2. **Filters** – Build filter criteria using facets from [GET /api/v1.0/filters/for/entitytype/{entityTypeId}](#/Filters/listFiltersForEntityType).

**Workflow Example**
1. Identify filters: Determine the status, assignee, or date criteria for your view
2. Create view: [POST /api/v1.0/tickets/views/new](#/Tickets/createTicketView) with Name, Filters, and column configuration
3. Use view: [POST /api/v1.0/tickets](#/Tickets/searchTickets) with `Schema` set to the view's name

**Minimal Required Fields**: Name, ProductId, ViewTypeId

**Related Endpoints**
- [GET /api/v1.0/tickets/views](#/Tickets/listTicketViews) – List available views
- [POST /api/v1.0/tickets/views/{viewId}](#/Tickets/updateTicketView) – Update existing view
- [DELETE /api/v1.0/tickets/views/{viewId}](#/Tickets/deleteTicketView) – Delete view

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

### `delete_ticket`

Provenance: Golden OpenAPI contract

Operation ID: `deleteTicket`

- Sync: `client.tickets.delete_ticket(ticket_id=..., timeout=None)`
- Async: `await client.tickets.delete_ticket(ticket_id=..., timeout=None)`
- Raw payload: `client.tickets.delete_ticket.raw(ticket_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/tickets/{ticketId}`
- Source controller: `IncidentIQ API`

Delete ticket

Soft-deletes a ticket by setting its `IsDeleted` flag to true. The ticket remains in the database but is excluded from normal search results. Deleted tickets can be restored using [PUT /api/v1.0/tickets/{ticketId}/undelete](#/Tickets/undeleteTicket).

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to locate the ticket and extract `Items[].TicketId`.

**Workflow Example**
1. Search for tickets: [POST /api/v1.0/tickets](#/Tickets/searchTickets) with filters → extract `Items[].TicketId`
2. Delete ticket: [DELETE /api/v1.0/tickets/{ticketId}](#/Tickets/deleteTicket)
3. To restore: [PUT /api/v1.0/tickets/{ticketId}/undelete](#/Tickets/undeleteTicket)

**Note**: This operation requires appropriate permissions. The caller must have rights to delete tickets in the target site.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | UUID of the ticket to delete. Obtain via POST /api/v1.0/tickets and read `Items[].TicketId` from the search response. |

#### Returns

- Typed call return: `TicketDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_ticket_activity`

Provenance: Golden OpenAPI contract

Operation ID: `deleteTicketActivity`

- Sync: `client.tickets.delete_ticket_activity(ticket_activity_id=..., timeout=None)`
- Async: `await client.tickets.delete_ticket_activity(ticket_activity_id=..., timeout=None)`
- Raw payload: `client.tickets.delete_ticket_activity.raw(ticket_activity_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/tickets/activities/{ticketActivityId}`
- Source controller: `IncidentIQ API`

Delete ticket activity

Soft-deletes a ticket activity (comment, update, etc.) from the ticket timeline. The activity is marked as deleted but may be recoverable by administrators using the undelete endpoint.

**Prerequisites**
1. **ticketActivityId** – Use [GET /api/v1.0/tickets/{ticketId}/timeline](#/Tickets/getTicketTimeline) to view the timeline and extract `TicketActivityId`.

**Workflow Example**
1. View timeline: [GET /api/v1.0/tickets/{ticketId}/timeline](#/Tickets/getTicketTimeline) → identify activity to delete
2. Delete activity: [DELETE /api/v1.0/tickets/activities/{ticketActivityId}](#/Tickets/deleteTicketActivity)
3. Verify: [GET /api/v1.0/tickets/{ticketId}/timeline](#/Tickets/getTicketTimeline) to confirm removal

**Permissions**: Typically requires ownership of the activity or administrative privileges. System-generated activities (status changes, assignments) may not be deletable.

**Note**: For comments, consider editing instead of deleting to preserve audit trail.

**Related Endpoints**
- [GET /api/v1.0/tickets/{ticketId}/timeline](#/Tickets/getTicketTimeline) – View timeline
- [POST /api/v1.0/tickets/{ticketId}/activities/{ticketActivityId}](#/Tickets/updateTicketActivity) – Edit instead of delete
- [POST /api/v1.0/tickets/activities/{ticketActivityId}/undelete](#/Tickets/undeleteTicketActivity) – Restore deleted activity

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_activity_id` | `ticketActivityId` | `path` | `yes` | `str` | `-` | Unique identifier of the ticket activity to delete |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_ticket_next_step_template`

Provenance: Golden OpenAPI contract

Operation ID: `deleteTicketNextStepTemplate`

- Sync: `client.tickets.delete_ticket_next_step_template(ticket_next_step_template_id=..., timeout=None)`
- Async: `await client.tickets.delete_ticket_next_step_template(ticket_next_step_template_id=..., timeout=None)`
- Raw payload: `client.tickets.delete_ticket_next_step_template.raw(ticket_next_step_template_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/tickets/next-step/templates/{TicketNextStepTemplateId}`
- Source controller: `IncidentIQ API`

Delete a ticket next step template

Deletes a ticket next step template by its unique identifier. This action is permanent and cannot be undone.

**Prerequisites**
1. **TicketNextStepTemplateId** - Obtain via [GET /api/v1.0/tickets/next-step/templates](#/Tickets/listTicketNextStepTemplates), extract `Items[].TicketNextStepTemplateId`.

**Workflow Example**
1. List templates: `GET /api/v1.0/tickets/next-step/templates` to find the template to delete
2. Delete template: `DELETE /api/v1.0/tickets/next-step/templates/{TicketNextStepTemplateId}`
3. Verify deletion by re-listing templates

**Warning**: Ensure the template is not actively used by any workflows before deletion.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_next_step_template_id` | `TicketNextStepTemplateId` | `path` | `yes` | `str` | `-` | Unique identifier of the ticket next step template to delete. Obtain via [GET /api/v1.0/tickets/next-step/templates](#/Tickets/listTicketNextStepTemplates), extract `Items[].TicketNextStepTemplateId`. |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_ticket_view`

Provenance: Golden OpenAPI contract

Operation ID: `deleteTicketView`

- Sync: `client.tickets.delete_ticket_view(view_id=..., timeout=None)`
- Async: `await client.tickets.delete_ticket_view(view_id=..., timeout=None)`
- Raw payload: `client.tickets.delete_ticket_view.raw(view_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/tickets/views/{viewId}`
- Source controller: `IncidentIQ API`

Delete ticket view

Permanently deletes a saved ticket view from the system. Once deleted, the view cannot be recovered. Users should export or note view configurations before deletion if they may need to recreate them.

**Prerequisites**
1. **viewId** – Use [GET /api/v1.0/tickets/views](#/Tickets/listTicketViews) to list views and extract `Items[].ViewId`.

**Workflow Example**
1. List views: [GET /api/v1.0/tickets/views](#/Tickets/listTicketViews) → identify `ViewId` to delete
2. (Optional) Backup: [GET /api/v1.0/tickets/views/{viewId}](#/Tickets/getTicketView) to save the configuration
3. Delete view: [DELETE /api/v1.0/tickets/views/{viewId}](#/Tickets/deleteTicketView)
4. Verify removal: [GET /api/v1.0/tickets/views](#/Tickets/listTicketViews) to confirm deletion

**Note**: Only the view owner or administrators can delete views. Shared views may be used by other team members.

**Related Endpoints**
- [GET /api/v1.0/tickets/views](#/Tickets/listTicketViews) – List views before deletion
- [POST /api/v1.0/tickets/views/new](#/Tickets/createTicketView) – Create replacement view

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `view_id` | `viewId` | `path` | `yes` | `str` | `-` | Identifier of the ticket view to delete. |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_activities_for_tickets`

Provenance: Golden OpenAPI contract

Operation ID: `getActivitiesForTickets`

- Sync: `client.tickets.get_activities_for_tickets(p=None, s=None, body=..., timeout=None)`
- Async: `await client.tickets.get_activities_for_tickets(p=None, s=None, body=..., timeout=None)`
- Raw payload: `client.tickets.get_activities_for_tickets.raw(p=None, s=None, body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/activities`
- Source controller: `IncidentIQ API`

Get activities for multiple tickets

Retrieves ticket activities for multiple tickets in a single request. This is a batch operation that accepts a list of ticket IDs in the request body and returns activities for all specified tickets.

**Prerequisites**
1. **TicketIds** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to search for tickets and extract `Items[].TicketId`.

**Workflow Example**
1. Search tickets: [POST /api/v1.0/tickets](#/Tickets/searchTickets) with filters → extract multiple `Items[].TicketId` values.
2. Call [POST /api/v1.0/tickets/activities](#/Tickets/getActivitiesForTickets) with the list of ticket IDs.
3. Process the combined activity feed for reporting or display.

**Pagination**: Supports `$p` (page index) and `$s` (page size) query parameters.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index for pagination. |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of activities per page. |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | - |

#### Returns

- Typed call return: `TicketActivityListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketActivityListResponse`
- Pagination helper: `client.tickets.get_activities_for_tickets.iter_pages(start_page=1, page_size=100, max_pages=None, p=None, s=None, body=..., timeout=None)`

---

### `get_all_workflow_statuses`

Provenance: Golden OpenAPI contract

Operation ID: `getAllWorkflowStatuses`

- Sync: `client.tickets.get_all_workflow_statuses(timeout=None)`
- Async: `await client.tickets.get_all_workflow_statuses(timeout=None)`
- Raw payload: `client.tickets.get_all_workflow_statuses.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/tickets/workflows/statuses`
- Source controller: `IncidentIQ API`

Get all workflow statuses

Retrieves all ticket statuses across all workflows configured in the system. This provides a complete inventory of possible ticket states, useful for building universal status dropdowns, cross-workflow reporting, or understanding the full range of ticket lifecycle states.

**Workflow Example**
1. List all statuses: [GET /api/v1.0/tickets/workflows/statuses](#/Tickets/getAllWorkflowStatuses)
2. Use for UI: Populate status filter dropdowns that work across all ticket types
3. Use for reporting: Build dashboards that aggregate tickets by status across workflows

**Response Fields**: Each status includes `WorkflowStepId`, `WorkflowId`, `StepName`, `Color`, `IsClosed`, and `DisplayOrder`.

**Use Cases**: Building cross-workflow status filters, creating universal ticket dashboards, analyzing ticket distribution across all workflow states.

**Note**: For workflow-specific statuses, use [GET /api/v1.0/tickets/{workflowId}/statuses](#/Tickets/getWorkflowStatuses) instead.

**Related Endpoints**
- [GET /api/v1.0/tickets/{workflowId}/statuses](#/Tickets/getWorkflowStatuses) – Statuses for specific workflow
- [GET /api/v1.0/tickets/statuses/{statusId}](#/Tickets/getTicketStatusById) – Single status details
- [GET /api/v1.0/workflows](#/Workflows/listWorkflows) – List available workflows

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `TicketStatusListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketStatusListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_related_tickets`

Provenance: Golden OpenAPI contract

Operation ID: `getRelatedTickets`

- Sync: `client.tickets.get_related_tickets(ticket_id=..., timeout=None)`
- Async: `await client.tickets.get_related_tickets(ticket_id=..., timeout=None)`
- Raw payload: `client.tickets.get_related_tickets.raw(ticket_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/tickets/{ticketId}/related-tickets`
- Source controller: `IncidentIQ API`

Get related tickets

Retrieves tickets that are related to the specified ticket. Related tickets can include duplicates, parent/child relationships (subtickets), manually linked tickets, or tickets automatically associated based on similar attributes like requester, asset, or issue type.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to find the ticket and extract `Items[].TicketId`.

**Workflow Example**
1. Locate ticket: [POST /api/v1.0/tickets](#/Tickets/searchTickets) → extract `TicketId`
2. Get related: [GET /api/v1.0/tickets/{ticketId}/related-tickets](#/Tickets/getRelatedTickets)
3. Review: Examine related tickets for patterns or consolidation opportunities
4. Act: Link, merge, or reference related tickets as needed

**Response Fields**: Returns a list of related tickets with relationship type, ticket details, and status information.

**Use Cases**: Identifying duplicate reports, finding related issues for the same requester, reviewing linked parent/child tickets, consolidating similar problems.

**Note**: The relationship types and discovery rules are configured at the site level.

**Related Endpoints**
- [POST /api/v1.0/tickets/{ticketId}/link](#/Tickets/markTicketAsDuplicate) – Manually link tickets
- [GET /api/v1.0/tickets/get-similar-tickets](#/Tickets/getSimilarTickets) – Find similar tickets by content
- [GET /api/v1.0/tickets/{ticketId}/subtickets](#/Subtasks/getSubtasksForTicket) – View subtickets specifically

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | Unique identifier of the ticket |

#### Returns

- Typed call return: `TicketListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_similar_tickets`

Provenance: Golden OpenAPI contract

Operation ID: `getSimilarTickets`

- Sync: `client.tickets.get_similar_tickets(body=..., timeout=None)`
- Async: `await client.tickets.get_similar_tickets(body=..., timeout=None)`
- Raw payload: `client.tickets.get_similar_tickets.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/get-similar-tickets`
- Source controller: `IncidentIQ API`

Find similar tickets

Searches for tickets similar to a reference ticket based on configurable matching criteria. Use this endpoint to identify potentially related issues, recurring problems, or duplicate tickets.

**Matching Options**
Each boolean flag enables a specific similarity dimension:
- `SameFor` - Tickets for the same requester
- `SameIssue` - Tickets with the same issue type
- `SameModel` - Tickets involving the same device model
- `SameAsset` - Tickets linked to the same asset
- `SameLocation` - Tickets from the same location
- `IsOpen` - Limit results to open tickets only

All flags default to `false`. Enable one or more to narrow the similarity search.

**Use Cases**
- Detecting duplicate submissions before creating a new ticket
- Identifying recurring issues for a specific device or user
- Finding related tickets for knowledge base article creation

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `SimilarTicketOptions` | `SimilarTicketOptions` | Search criteria including the reference ticket and matching options. |

#### Returns

- Typed call return: `TicketListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_ticket`

Provenance: Golden OpenAPI contract

Operation ID: `getTicket`

- Sync: `client.tickets.get_ticket(ticket_id=..., timeout=None)`
- Async: `await client.tickets.get_ticket(ticket_id=..., timeout=None)`
- Raw payload: `client.tickets.get_ticket.raw(ticket_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/tickets/{ticketId}`
- Source controller: `IncidentIQ API`

Get Ticket Details

Retrieves end-to-end ticket details including assignment, workflow status, site context, assets, and permission flags.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) with filters to locate the ticket and extract `Items[].TicketId` (e.g., `Items[0].TicketId`).

**Workflow Example**
1. Filter tickets: [POST /api/v1.0/tickets](#/Tickets/searchTickets) with status, assignee, product, or site filters as needed.
2. Extract the desired ticket identifier from the response at `Items[].TicketId`.
3. Call [GET /api/v1.0/tickets/{ticketId}](#/Tickets/getTicket) to retrieve comprehensive ticket metadata for UI rendering, auditing, or troubleshooting workflows.
4. When technicians click **Start Ticket**, first confirm the issue via [POST /api/v1.0/tickets/{ticketId}/confirm-issue](#/Tickets/confirmTicketIssue) and then call [POST /api/v1.0/tickets/{ticketId}/start](#/Tickets/startTicket); follow with this GET request to refresh status, timers, and owner details now that work has begun.

**Minimal Required Fields**: ticketId

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | UUID of the ticket to retrieve. Obtain via POST /api/v1.0/tickets and read `Items[].TicketId` from the search response. |

#### Returns

- Typed call return: `TicketSingleResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketSingleResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_ticket_activities`

Provenance: Golden OpenAPI contract

Operation ID: `getTicketActivities`

- Sync: `client.tickets.get_ticket_activities(ticket_id=..., p=None, s=None, timeout=None)`
- Async: `await client.tickets.get_ticket_activities(ticket_id=..., p=None, s=None, timeout=None)`
- Raw payload: `client.tickets.get_ticket_activities.raw(ticket_id=..., p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v1.0/tickets/{ticketId}/activities`
- Source controller: `IncidentIQ API`

Get all activities for a ticket

Returns the chronological activity log for a ticket, including user comments, internal notes, workflow transitions, and system-generated events.

**Prerequisites**
1. **ticketId** – Locate the ticket via [POST /api/v1.0/tickets](#/Tickets/searchTickets) and extract `Items[].TicketId`.

**Workflow Example**
1. Search tickets: [POST /api/v1.0/tickets](#/Tickets/searchTickets) with site, status, or requester filters.
2. Extract the ticket identifier from `Items[].TicketId`.
3. Call [GET /api/v1.0/tickets/{ticketId}/activities](#/Tickets/getTicketActivities) to render the activity feed for customer support or auditing.

**Minimal Required Fields**: ticketId

Supports pagination via optional `$p` (page index) and `$s` (page size) query parameters.

This endpoint focuses on agent-authored updates and workflow notes shared with stakeholders. For a full audit trail that includes automation and rule execution entries, use [GET /api/v1.0/tickets/{ticketId}/timeline](#/Tickets/getTicketTimeline).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | UUID of the ticket whose activity feed should be retrieved. Obtain via POST /api/v1.0/tickets and read `Items[].TicketId`. |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index for paginating ticket activities. |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of activity records to return per page. |

#### Returns

- Typed call return: `TicketActivitiesResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketActivitiesResponse`
- Pagination helper: `client.tickets.get_ticket_activities.iter_pages(start_page=1, page_size=100, max_pages=None, ticket_id=..., p=None, s=None, timeout=None)`

---

### `get_ticket_activity_by_id`

Provenance: Golden OpenAPI contract

Operation ID: `getTicketActivityById`

- Sync: `client.tickets.get_ticket_activity_by_id(ticket_activity_id=..., timeout=None)`
- Async: `await client.tickets.get_ticket_activity_by_id(ticket_activity_id=..., timeout=None)`
- Raw payload: `client.tickets.get_ticket_activity_by_id.raw(ticket_activity_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/tickets/activities/{ticketActivityId}`
- Source controller: `IncidentIQ API`

Get ticket activity by ID

Retrieves the complete details of a specific ticket activity by its identifier. Activities include comments, status changes, assignments, attachments, and other timeline events.

**Prerequisites**
1. **ticketActivityId** – Use [GET /api/v1.0/tickets/{ticketId}/timeline](#/Tickets/getTicketTimeline) to view the ticket's activity history and extract `TicketActivityId` from timeline entries.

**Workflow Example**
1. View timeline: [GET /api/v1.0/tickets/{ticketId}/timeline](#/Tickets/getTicketTimeline) → identify activity of interest
2. Get details: [GET /api/v1.0/tickets/activities/{ticketActivityId}](#/Tickets/getTicketActivityById)
3. Process: Use activity data for display, audit, or integration purposes

**Response Contents**: Returns the activity type, creator, timestamp, content (comment text, field changes), visibility settings, and any attachments.

**Use Cases**: Activity detail views, audit logging, activity-triggered integrations.

**Related Endpoints**
- [GET /api/v1.0/tickets/{ticketId}/timeline](#/Tickets/getTicketTimeline) – View full activity history
- [POST /api/v1.0/tickets/{ticketId}/activities/{ticketActivityId}](#/Tickets/updateTicketActivity) – Edit activity
- [DELETE /api/v1.0/tickets/activities/{ticketActivityId}](#/Tickets/deleteTicketActivity) – Delete activity

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_activity_id` | `ticketActivityId` | `path` | `yes` | `str` | `-` | Unique identifier of the ticket activity |

#### Returns

- Typed call return: `TicketActivitySingleResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketActivitySingleResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_ticket_approvals`

Provenance: Golden OpenAPI contract

Operation ID: `getTicketApprovals`

- Sync: `client.tickets.get_ticket_approvals(ticket_id=..., timeout=None)`
- Async: `await client.tickets.get_ticket_approvals(ticket_id=..., timeout=None)`
- Raw payload: `client.tickets.get_ticket_approvals.raw(ticket_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/tickets/{ticketId}/approvals`
- Source controller: `IncidentIQ API`

Get ticket approvals

Retrieves the list of approvals associated with a ticket, including approval status, approvers, and decision history. Used in workflows that require managerial or stakeholder sign-off before proceeding.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to find tickets in approval status and extract `Items[].TicketId`.

**Workflow Example**
1. Find ticket: [POST /api/v1.0/tickets](#/Tickets/searchTickets) with workflow filter → extract `TicketId`
2. Get approvals: [GET /api/v1.0/tickets/{ticketId}/approvals](#/Tickets/getTicketApprovals)
3. Review: Check each approval's `Status`, `ApproverUserId`, `DecisionDate`, and `Comments`
4. Take action: If pending, use [POST /api/v1.0/tickets/{ticketId}/workflow/approval/response](#/Tickets/processTicketApproval) to approve or reject

**Response Fields**: Each approval includes `ApprovalId`, `ApproverUserId`, `ApproverName`, `Status` (Pending/Approved/Rejected), `RequestDate`, `DecisionDate`, and optional `Comments`.

**Use Cases**: Tracking approval progress, building approval dashboards, auditing approval decisions.

**Related Endpoints**
- [POST /api/v1.0/tickets/{ticketId}/workflow/approval](#/Tickets/sendTicketForApproval) – Send for approval
- [POST /api/v1.0/tickets/{ticketId}/workflow/approval/response](#/Tickets/processTicketApproval) – Approve or reject

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | Unique identifier of the ticket |

#### Returns

- Typed call return: `TicketApprovalsResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketApprovalsResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_ticket_asset_groups`

Provenance: Golden OpenAPI contract

Operation ID: `getTicketAssetGroups`

- Sync: `client.tickets.get_ticket_asset_groups(ticket_id=..., p=None, s=None, timeout=None)`
- Async: `await client.tickets.get_ticket_asset_groups(ticket_id=..., p=None, s=None, timeout=None)`
- Raw payload: `client.tickets.get_ticket_asset_groups.raw(ticket_id=..., p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v1.0/tickets/{ticketId}/assetgroups`
- Source controller: `IncidentIQ API`

Get asset groups for ticket

Returns the saved asset views (groups) associated with the specified ticket. Asset groups are saved filter configurations that define collections of assets.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to locate the ticket and extract `Items[].TicketId`.

**Workflow Example**
1. Search tickets: [POST /api/v1.0/tickets](#/Tickets/searchTickets) with filters → extract `Items[].TicketId`.
2. Call [GET /api/v1.0/tickets/{ticketId}/assetgroups](#/Tickets/getTicketAssetGroups) to retrieve associated asset groups.
3. Use asset group information for bulk asset operations or filtering.

**Pagination**: Supports `$p` (page index) and `$s` (page size) query parameters. Default page size is 100.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | UUID of the ticket |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index. |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of asset groups per page. |

#### Returns

- Typed call return: `ViewListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ViewListResponse`
- Pagination helper: `client.tickets.get_ticket_asset_groups.iter_pages(start_page=1, page_size=100, max_pages=None, ticket_id=..., p=None, s=None, timeout=None)`

---

### `get_ticket_assets`

Provenance: Golden OpenAPI contract

Operation ID: `getTicketAssets`

- Sync: `client.tickets.get_ticket_assets(ticket_id=..., timeout=None)`
- Async: `await client.tickets.get_ticket_assets(ticket_id=..., timeout=None)`
- Raw payload: `client.tickets.get_ticket_assets.raw(ticket_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/tickets/{ticketId}/assets`
- Source controller: `IncidentIQ API`

Get ticket assets

Retrieves all assets currently linked to a given ticket. Each asset record includes model metadata, serial number, and asset tag for display in ticket detail views.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to search for tickets and read `Items[].TicketId`.

**Field References**
- **TicketAssetId** is the join record identifier; use it when updating links via [POST /api/v1.0/tickets/{ticketId}/assets](#/Tickets/updateTicketAssets).
- **AssetId** references the device record; fetch full details with [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById).
- **ModelId** and **CategoryId** identify the asset's model and category; lookup metadata via [POST /api/v1.0/issues/for/models](#/Model Issues/getIssuesForModels).

**Workflow Example**
1. Search for the ticket: [POST /api/v1.0/tickets](#/Tickets/searchTickets) with filters → extract `Items[0].TicketId`.
2. Fetch linked assets: [GET /api/v1.0/tickets/{ticketId}/assets](#/Tickets/getTicketAssets) → iterate `Items[]` to display asset tags and models.
3. (Optional) Load full asset details: for each `AssetId`, call [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById) to retrieve owner, location, and custom fields.

**Minimal Required Fields**: ticketId (path parameter)

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | UUID of the ticket whose linked assets should be returned. Obtain via POST /api/v1.0/tickets and read `Items[].TicketId`. |

#### Returns

- Typed call return: `TicketAssetListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketAssetListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_ticket_assets_by_model`

Provenance: Golden OpenAPI contract

Operation ID: `getTicketAssetsByModel`

- Sync: `client.tickets.get_ticket_assets_by_model(body=..., timeout=None)`
- Async: `await client.tickets.get_ticket_assets_by_model(body=..., timeout=None)`
- Raw payload: `client.tickets.get_ticket_assets_by_model.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/assets`
- Source controller: `IncidentIQ API`

Find ticket assets by model/category

Returns ticket asset links for the specified asset models or categories. Use this to see which tickets already reference a device model (or its category) before attaching new assets or issuing bulk updates.

**Prerequisites**
1. **ModelIds/CategoryIds** – Query the catalog via [POST /api/v1.0/issues/for/models](#/Model Issues/getIssuesForModels) and capture `Items[].ModelId` plus `Items[].Category.CategoryId`. Optionally confirm the selection with [GET /api/v1.0/issues/for/models/{modelId}](#/Model Issues/getIssuesForModel).
2. **Product scope (optional)** – Reuse the `ProductId` header from your session or retrieve a product context from [POST /api/v1.0/assets/](#/Assets/searchAssets) (`Items[].ProductId`) when searching across products.
3. **Asset context (optional)** – When reconciling against a specific device, load it with [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById) to pull `AssetId`, `ModelId`, and `CategoryId` for the payload.

**Workflow Example**
1. Discover models: [POST /api/v1.0/issues/for/models](#/Model Issues/getIssuesForModels) with asset type filters → record `ModelId` and `CategoryId` for the devices you want to audit.
2. Build payload: include `ModelIds` (or `CategoryIds`), keep `FilterByProduct: true` to limit to the active product, and supply `ProductId` only when overriding the header context.
3. Call [POST /api/v1.0/tickets/assets](#/Tickets/getTicketAssetsByModel) → inspect returned `TicketAssetId`/`AssetId` pairs for tickets using those models.
4. (Optional) Use the results to drive follow-up updates with [POST /api/v1.0/tickets/{ticketId}/assets](#/Tickets/updateTicketAssets) when adding or pruning links on individual tickets.

**Minimal Required Fields**: at least one of `ModelIds` or `CategoryIds`.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `GetTicketAssetsRequest` | `GetTicketAssetsRequest` | Model and/or category filters that determine which ticket asset links are returned. When `FilterByProduct` is true, results are limited to the product specified in the request headers unless `ProductId` is provided. |

#### Returns

- Typed call return: `GetTicketAssetsResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `GetTicketAssetsResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_ticket_count`

Provenance: Golden OpenAPI contract

Operation ID: `getTicketCount`

- Sync: `client.tickets.get_ticket_count(body=None, timeout=None)`
- Async: `await client.tickets.get_ticket_count(body=None, timeout=None)`
- Raw payload: `client.tickets.get_ticket_count.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/count`
- Source controller: `IncidentIQ API`

Count tickets matching criteria

Returns the count of tickets matching the specified filter criteria without returning full ticket records. Use this to power dashboard KPIs, queue badges, or trend reporting while reusing the same search filters as the full ticket search.

**Prerequisites**
1. **Filters (optional)** - Build filters using the same facet model as [POST /api/v1.0/tickets](#/Tickets/searchTickets) (`TicketSearchRequest.Filters`).

**Workflow Example**
1. Define your filters (status, workflow, requester, date range).
2. [POST /api/v1.0/tickets/count](#/Tickets/getTicketCount) with a `TicketSearchRequest` payload.
3. Use the returned count to drive UI badges or reporting thresholds.

**Minimal Required Fields**: None (request body optional).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `TicketSearchRequest` | `TicketSearchRequest` | - |

#### Returns

- Typed call return: `TicketCountResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketCountResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_ticket_due_date_reminders`

Provenance: Golden OpenAPI contract

Operation ID: `getTicketDueDateReminders`

- Sync: `client.tickets.get_ticket_due_date_reminders(ticket_id=..., timeout=None)`
- Async: `await client.tickets.get_ticket_due_date_reminders(ticket_id=..., timeout=None)`
- Raw payload: `client.tickets.get_ticket_due_date_reminders.raw(ticket_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/tickets/due-dates/reminders/{ticketId}`
- Source controller: `IncidentIQ API`

Get due date reminders for ticket

Retrieves all configured due date reminders for a specific ticket, including whether reminders fire before or after the due date. Use this to display or audit reminder settings before adjusting them.

**Prerequisites**
1. **ticketId** - Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) and extract `Items[].TicketId`.

**Workflow Example**
1. Locate the ticket and capture its `TicketId`.
2. [GET /api/v1.0/tickets/due-dates/reminders/{ticketId}](#/Tickets/getTicketDueDateReminders) to read current reminders.
3. Update reminders with [POST /api/v1.0/tickets/due-dates/reminders](#/Tickets/saveTicketDueDateReminders) if changes are needed.

**Minimal Required Fields**: ticketId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | Unique identifier of the ticket |

#### Returns

- Typed call return: `TicketRemindersResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketRemindersResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_ticket_fields`

Provenance: Golden OpenAPI contract

Operation ID: `getTicketFields`

- Sync: `client.tickets.get_ticket_fields(timeout=None)`
- Async: `await client.tickets.get_ticket_fields(timeout=None)`
- Raw payload: `client.tickets.get_ticket_fields.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/tickets/fields`
- Source controller: `IncidentIQ API`

Get ticket field definitions

Retrieves metadata about all available ticket fields, including built-in and custom fields. Useful for building dynamic forms, validating field inputs, or understanding the ticket data model.

**Workflow Example**
1. Get field definitions: [GET /api/v1.0/tickets/fields](#/Tickets/getTicketFields)
2. Build UI: Use field metadata to construct dynamic ticket creation/edit forms
3. Create ticket: [POST /api/v1.0/tickets/new](#/Tickets/createTicket) with validated field values
4. Update fields: [PUT /api/v1.0/tickets/{ticketId}](#/Tickets/updateTicket) for modifications

**Response Fields**: Each field includes `FieldId`, `FieldName`, `DataType`, `IsRequired`, `IsReadOnly`, `DisplayOrder`, and validation constraints.

**Use Cases**: Building custom ticket submission forms, implementing field validation logic, discovering available custom fields, generating API documentation for ticket payloads.

**Note**: For custom field values on specific tickets, use [GET /api/v1.0/tickets/{ticketId}](#/Tickets/getTicket) and inspect `CustomFieldValues`.

**Related Endpoints**
- [POST /api/v1.0/tickets/new](#/Tickets/createTicket) – Create ticket using field definitions
- [GET /api/v1.0/customfields](#/Custom Fields/searchCustomFields) – Custom field management

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `TicketFieldsResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketFieldsResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_ticket_followers`

Provenance: Golden OpenAPI contract

Operation ID: `getTicketFollowers`

- Sync: `client.tickets.get_ticket_followers(ticket_id=..., timeout=None)`
- Async: `await client.tickets.get_ticket_followers(ticket_id=..., timeout=None)`
- Raw payload: `client.tickets.get_ticket_followers.raw(ticket_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/tickets/{ticketId}/followers`
- Source controller: `IncidentIQ API`

Get ticket followers

Retrieves the list of users following a ticket. Followers receive notifications about ticket updates.

**Related Endpoints**
- [POST /api/v1.0/tickets/{ticketId}/followers/user/{userId}](#/Tickets/addTicketFollowerUser) – Add a user follower
- [DELETE /api/v1.0/tickets/{ticketId}/followers/user/{userId}](#/Tickets/removeTicketFollowerUser) – Remove a user follower
- [POST /api/v1.0/tickets/{ticketId}/followers/team/{teamId}](#/Tickets/addTicketFollowerTeam) – Add a team as followers

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | Unique identifier of the ticket |

#### Returns

- Typed call return: `TicketFollowersResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketFollowersResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_ticket_ids_for_filter_sets`

Provenance: Golden OpenAPI contract

Operation ID: `getTicketIdsForFilterSets`

- Sync: `client.tickets.get_ticket_ids_for_filter_sets(body=..., timeout=None)`
- Async: `await client.tickets.get_ticket_ids_for_filter_sets(body=..., timeout=None)`
- Raw payload: `client.tickets.get_ticket_ids_for_filter_sets.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/ids/for/filtersets`
- Source controller: `IncidentIQ API`

Get ticket IDs for filter sets

Retrieves lists of ticket identifiers that match one or more filter set definitions. Use this to determine which tickets belong to specific saved views or criteria sets without performing a full search.

**Prerequisites**
1. **FilterSetIds** – Use [GET /api/v1.0/filters](#/Filters/listFilters) to obtain identifiers for the filter sets you wish to evaluate.

**Workflow Example**
1. List filters: [GET /api/v1.0/filters](#/Filters/listFilters) → extract `Items[].FilterSetId`.
2. Apply filter sets: [POST /api/v1.0/tickets/ids/for/filtersets](#/Tickets/getTicketIdsForFilterSets) with the collected IDs to find matching tickets.
3. (Optional) Inspect matches: Use the returned `MatchedIds` with breadcrumb or detail APIs to retrieve ticket metadata.

**Minimal Required Fields**: FilterSetIds

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `GetIdsForFilterSetRequest` | `GetIdsForFilterSetRequest` | - |

#### Returns

- Typed call return: `list[Any]`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_ticket_kb_articles`

Provenance: Golden OpenAPI contract

Operation ID: `getTicketKbArticles`

- Sync: `client.tickets.get_ticket_kb_articles(ticket_id=..., p=None, s=None, timeout=None)`
- Async: `await client.tickets.get_ticket_kb_articles(ticket_id=..., p=None, s=None, timeout=None)`
- Raw payload: `client.tickets.get_ticket_kb_articles.raw(ticket_id=..., p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v1.0/tickets/{ticketId}/kb-articles`
- Source controller: `IncidentIQ API`

Get related knowledge base articles

Returns knowledge base articles related to the ticket's issue context so agents can provide quick resolutions. Supports pagination for large result sets.

**Prerequisites**
1. **ticketId** – Locate the ticket via [POST /api/v1.0/tickets](#/Tickets/searchTickets) and extract `Items[].TicketId`.

**Workflow Example**
1. Search tickets: [POST /api/v1.0/tickets](#/Tickets/searchTickets) with filters for the agent's queue.
2. Extract the identifier from `Items[].TicketId`.
3. Call [GET /api/v1.0/tickets/{ticketId}/kb-articles](#/Tickets/getTicketKbArticles) (optionally with `$p`/`$s`) to surface knowledge articles in the support UI.

**Minimal Required Fields**: ticketId (path). Optional pagination: $p, $s.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | UUID of the ticket used to scope knowledge base recommendations. Obtain via POST /api/v1.0/tickets and extract `Items[].TicketId`. |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index for paginating article results. |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of article records per page. |

#### Returns

- Typed call return: `TicketKbArticlesResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketKbArticlesResponse`
- Pagination helper: `client.tickets.get_ticket_kb_articles.iter_pages(start_page=1, page_size=100, max_pages=None, ticket_id=..., p=None, s=None, timeout=None)`

---

### `get_ticket_location_types`

Provenance: Golden OpenAPI contract

Operation ID: `getTicketLocationTypes`

- Sync: `client.tickets.get_ticket_location_types(ticket_id=..., p=None, s=None, timeout=None)`
- Async: `await client.tickets.get_ticket_location_types(ticket_id=..., p=None, s=None, timeout=None)`
- Raw payload: `client.tickets.get_ticket_location_types.raw(ticket_id=..., p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v1.0/tickets/{ticketId}/locationtypes`
- Source controller: `IncidentIQ API`

Get location types for ticket

Returns the location types associated with the specified ticket. This typically includes the location type of the ticket's site and any related locations.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to locate the ticket and extract `Items[].TicketId`.

**Workflow Example**
1. Search tickets: [POST /api/v1.0/tickets](#/Tickets/searchTickets) with filters → extract `Items[].TicketId`.
2. Call [GET /api/v1.0/tickets/{ticketId}/locationtypes](#/Tickets/getTicketLocationTypes) to retrieve location type metadata.
3. Use for filtering, reporting, or understanding the ticket's organizational context.

**Pagination**: Supports `$p` (page index) and `$s` (page size) query parameters. Default page size is 100.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | UUID of the ticket |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index. |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of location types per page. |

#### Returns

- Typed call return: `LocationTypeListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `LocationTypeListResponse`
- Pagination helper: `client.tickets.get_ticket_location_types.iter_pages(start_page=1, page_size=100, max_pages=None, ticket_id=..., p=None, s=None, timeout=None)`

---

### `get_ticket_locations`

Provenance: Golden OpenAPI contract

Operation ID: `getTicketLocations`

- Sync: `client.tickets.get_ticket_locations(ticket_id=..., p=None, s=None, timeout=None)`
- Async: `await client.tickets.get_ticket_locations(ticket_id=..., p=None, s=None, timeout=None)`
- Raw payload: `client.tickets.get_ticket_locations.raw(ticket_id=..., p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v1.0/tickets/{ticketId}/locations`
- Source controller: `IncidentIQ API`

Get locations associated with ticket

Retrieves all locations associated with a ticket, including the primary location and any additional locations linked through assets, users, or manual associations. This information helps agents understand the physical context of the issue and coordinate on-site support.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to find the ticket and extract `Items[].TicketId`.

**Workflow Example**
1. Locate ticket: [POST /api/v1.0/tickets](#/Tickets/searchTickets) → extract `TicketId`
2. Get locations: [GET /api/v1.0/tickets/{ticketId}/locations](#/Tickets/getTicketLocations)
3. Use for routing: Identify nearby technicians or determine site-specific procedures

**Response Fields**: Each location includes `LocationId`, `Name`, `Address`, `SiteId`, and location hierarchy information.

**Query Parameters**: Supports pagination with `$p` (page) and `$s` (page size).

**Use Cases**: Dispatching field technicians, determining local support resources, mapping tickets by geographic area, identifying assets at the same location.

**Related Endpoints**
- [GET /api/v1.0/tickets/{ticketId}](#/Tickets/getTicket) – View primary ticket location
- [GET /api/v1.0/locations](#/Locations/getAllSiteLocationsV2) – List all locations
- [GET /api/v1.0/tickets/{ticketId}/assets](#/Tickets/getTicketAssets) – View associated assets and their locations

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | Unique identifier of the ticket |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index |
| `s` | `$s` | `query` | `no` | `int` | `-` | Page size (default 100) |

#### Returns

- Typed call return: `LocationListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `LocationListResponse`
- Pagination helper: `client.tickets.get_ticket_locations.iter_pages(start_page=1, page_size=100, max_pages=None, ticket_id=..., p=None, s=None, timeout=None)`

---

### `get_ticket_next_step`

Provenance: Golden OpenAPI contract

Operation ID: `getTicketNextStep`

- Sync: `client.tickets.get_ticket_next_step(ticket_id=..., next_step_id=..., timeout=None)`
- Async: `await client.tickets.get_ticket_next_step(ticket_id=..., next_step_id=..., timeout=None)`
- Raw payload: `client.tickets.get_ticket_next_step.raw(ticket_id=..., next_step_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/tickets/{ticketId}/next-steps/{nextStepId}`
- Source controller: `IncidentIQ API`

Get next step details

Retrieves details of a specific next step (task) for a ticket, including assignee, due date, status, description, and completion information. Use this to display step details or verify step configuration before updates.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to find the ticket and extract `Items[].TicketId`.
2. **nextStepId** – Use [GET /api/v1.0/tickets/{ticketId}/next-steps](#/Tickets/getTicketNextSteps) to list steps and extract `TicketNextStepId`.

**Workflow Example**
1. List steps: [GET /api/v1.0/tickets/{ticketId}/next-steps](#/Tickets/getTicketNextSteps) → identify step of interest
2. Get details: [GET /api/v1.0/tickets/{ticketId}/next-steps/{nextStepId}](#/Tickets/getTicketNextStep)
3. Display: Show step details in task management interface

**Response Fields**: Includes `Title`, `Description`, `AssignedUserId`, `AssignedUser` object, `DueDate`, `IsCompleted`, `CompletedDate`, and `TicketNextStepTypeId`.

**Related Endpoints**
- [GET /api/v1.0/tickets/{ticketId}/next-steps](#/Tickets/getTicketNextSteps) – List all next steps
- [POST /api/v1.0/tickets/{ticketId}/next-steps/{nextStepId}](#/Tickets/updateTicketNextStep) – Update this step
- [POST /api/v1.0/tickets/{ticketId}/next-steps/new](#/Tickets/createTicketNextStep) – Create new step

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | Unique identifier of the ticket |
| `next_step_id` | `nextStepId` | `path` | `yes` | `str` | `-` | Unique identifier of the next step |

#### Returns

- Typed call return: `TicketNextStepResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketNextStepResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_ticket_next_step_template`

Provenance: Golden OpenAPI contract

Operation ID: `getTicketNextStepTemplate`

- Sync: `client.tickets.get_ticket_next_step_template(ticket_next_step_template_id=..., timeout=None)`
- Async: `await client.tickets.get_ticket_next_step_template(ticket_next_step_template_id=..., timeout=None)`
- Raw payload: `client.tickets.get_ticket_next_step_template.raw(ticket_next_step_template_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/tickets/next-step/templates/{TicketNextStepTemplateId}`
- Source controller: `IncidentIQ API`

Get a ticket next step template by ID

Retrieves a single ticket next step template by its unique identifier.

**Prerequisites**
1. **TicketNextStepTemplateId** - Obtain via [GET /api/v1.0/tickets/next-step/templates](#/Tickets/listTicketNextStepTemplates), extract `Items[].TicketNextStepTemplateId`.

**Workflow Example**
1. List templates: `GET /api/v1.0/tickets/next-step/templates` to find available templates
2. Get template details: `GET /api/v1.0/tickets/next-step/templates/{TicketNextStepTemplateId}`
3. Use template configuration in ticket workflow operations

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_next_step_template_id` | `TicketNextStepTemplateId` | `path` | `yes` | `str` | `-` | Unique identifier of the ticket next step template. Obtain via [GET /api/v1.0/tickets/next-step/templates](#/Tickets/listTicketNextStepTemplates), extract `Items[].TicketNextStepTemplateId`. |

#### Returns

- Typed call return: `TicketNextStepTemplateItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketNextStepTemplateItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_ticket_next_step_type`

Provenance: Golden OpenAPI contract

Operation ID: `getTicketNextStepType`

- Sync: `client.tickets.get_ticket_next_step_type(ticket_next_step_type_id=..., timeout=None)`
- Async: `await client.tickets.get_ticket_next_step_type(ticket_next_step_type_id=..., timeout=None)`
- Raw payload: `client.tickets.get_ticket_next_step_type.raw(ticket_next_step_type_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/tickets/next-step/types/{ticketNextStepTypeId}`
- Source controller: `IncidentIQ API`

Get next-step type

Retrieves details for a specific next-step type definition. Next-step types define the categories of tasks that can be created within tickets (e.g., 'Follow-up Call', 'Research Issue', 'Order Parts'). Use this to display type metadata or validate type configurations.

**Prerequisites**
1. **ticketNextStepTypeId** – Use [GET /api/v1.0/tickets/next-step/types](#/Tickets/listTicketNextStepTypes) to list available types and extract `TicketNextStepTypeId`.

**Workflow Example**
1. List types: [GET /api/v1.0/tickets/next-step/types](#/Tickets/listTicketNextStepTypes) → identify type of interest
2. Get details: [GET /api/v1.0/tickets/next-step/types/{ticketNextStepTypeId}](#/Tickets/getTicketNextStepType)
3. Use: Apply type metadata when creating or displaying next steps

**Response Fields**: Includes type name, description, default settings, and whether the type is active.

**Related Endpoints**
- [GET /api/v1.0/tickets/next-step/types](#/Tickets/listTicketNextStepTypes) – List all next-step types
- [POST /api/v1.0/tickets/{ticketId}/next-steps/new](#/Tickets/createTicketNextStep) – Create next step using this type
- [GET /api/v1.0/tickets/{ticketId}/next-steps](#/Tickets/getTicketNextSteps) – List next steps on ticket

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_next_step_type_id` | `ticketNextStepTypeId` | `path` | `yes` | `str` | `-` | UUID of the next-step type. |

#### Returns

- Typed call return: `TicketNextStepType`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketNextStepType`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_ticket_next_steps`

Provenance: Golden OpenAPI contract

Operation ID: `getTicketNextSteps`

- Sync: `client.tickets.get_ticket_next_steps(ticket_id=..., p=None, s=None, timeout=None)`
- Async: `await client.tickets.get_ticket_next_steps(ticket_id=..., p=None, s=None, timeout=None)`
- Raw payload: `client.tickets.get_ticket_next_steps.raw(ticket_id=..., p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v1.0/tickets/{ticketId}/next-steps`
- Source controller: `IncidentIQ API`

Get ticket next steps

Provides recommended next actions for a ticket based on workflow configuration, ticket state, and agent permissions. Supports pagination when many recommendations are available.

**Prerequisites**
1. **ticketId** – Locate the ticket via [POST /api/v1.0/tickets](#/Tickets/searchTickets) and extract `Items[].TicketId`.

**Workflow Example**
1. Search tickets: [POST /api/v1.0/tickets](#/Tickets/searchTickets) with filters suited to the agent's queue.
2. Extract the identifier from `Items[].TicketId`.
3. Call [GET /api/v1.0/tickets/{ticketId}/next-steps](#/Tickets/getTicketNextSteps) (optionally paginating with `$p` and `$s`) to surface recommended actions in the UI.

**Minimal Required Fields**: ticketId (path). Optional pagination: $p, $s.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | UUID of the ticket whose next-step guidance should be retrieved. Obtain via POST /api/v1.0/tickets and extract `Items[].TicketId`. |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index for paginating next-step recommendations. |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of recommendation records to return per page. |

#### Returns

- Typed call return: `TicketNextStepsResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketNextStepsResponse`
- Pagination helper: `client.tickets.get_ticket_next_steps.iter_pages(start_page=1, page_size=100, max_pages=None, ticket_id=..., p=None, s=None, timeout=None)`

---

### `get_ticket_roles`

Provenance: Golden OpenAPI contract

Operation ID: `getTicketRoles`

- Sync: `client.tickets.get_ticket_roles(ticket_id=..., p=None, s=None, timeout=None)`
- Async: `await client.tickets.get_ticket_roles(ticket_id=..., p=None, s=None, timeout=None)`
- Raw payload: `client.tickets.get_ticket_roles.raw(ticket_id=..., p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v1.0/tickets/{ticketId}/roles`
- Source controller: `IncidentIQ API`

Get roles associated with ticket

Returns the list of roles that have access to or are associated with the specified ticket. This includes roles assigned through team membership, location-based access, or direct permissions.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to locate the ticket and extract `Items[].TicketId`.

**Workflow Example**
1. Search tickets: [POST /api/v1.0/tickets](#/Tickets/searchTickets) with filters → extract `Items[].TicketId`.
2. Call [GET /api/v1.0/tickets/{ticketId}/roles](#/Tickets/getTicketRoles) to retrieve associated roles.
3. Use role information for permission checks or assignment workflows.

**Pagination**: Supports `$p` (page index) and `$s` (page size) query parameters. Default page size is 100.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | UUID of the ticket |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index. |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of roles per page. |

#### Returns

- Typed call return: `RoleListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `RoleListResponse`
- Pagination helper: `client.tickets.get_ticket_roles.iter_pages(start_page=1, page_size=100, max_pages=None, ticket_id=..., p=None, s=None, timeout=None)`

---

### `get_ticket_sla`

Provenance: Golden OpenAPI contract

Operation ID: `getTicketSla`

- Sync: `client.tickets.get_ticket_sla(ticket_id=..., timeout=None)`
- Async: `await client.tickets.get_ticket_sla(ticket_id=..., timeout=None)`
- Raw payload: `client.tickets.get_ticket_sla.raw(ticket_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/tickets/{ticketId}/sla`
- Source controller: `IncidentIQ API`

Get Ticket SLA

Retrieves the SLA applied to a single ticket, including the linked SLA definition and aggregated metric timers.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to locate the ticket and read `Items[].TicketId`.

**Field References**
- **Sla.SlaId** and `Sla.Metrics[]` are defined by [GET /api/v1.0/slas](#/Slas/listSlas); reuse `Items[].SlaId` and `Items[].Metrics[]` from that response to interpret timer names and thresholds.
- **SlaTimes[]** summarizes log history for each metric (records, running flag, and total minutes) so you can show remaining time against SLA targets.

**Workflow Example**
1. Search for the ticket: [POST /api/v1.0/tickets](#/Tickets/searchTickets) with filters for status, assignee, or site and extract `Items[0].TicketId`.
2. (Optional) Refresh the ticket shell: [GET /api/v1.0/tickets/{ticketId}](#/Tickets/getTicket) to display status and ownership.
3. Fetch SLA timers: [GET /api/v1.0/tickets/{ticketId}/sla](#/Tickets/getTicketSla) to render the applied SLA, metrics, and accumulated time for response/resolution.

**Minimal Required Fields**: ticketId

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | UUID of the ticket whose SLA data should be returned. Obtain via POST /api/v1.0/tickets and read `Items[].TicketId`. |

#### Returns

- Typed call return: `TicketSlaSingleResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketSlaSingleResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_ticket_sources`

Provenance: Golden OpenAPI contract

Operation ID: `getTicketSources`

- Sync: `client.tickets.get_ticket_sources(filter=None, timeout=None)`
- Async: `await client.tickets.get_ticket_sources(filter=None, timeout=None)`
- Raw payload: `client.tickets.get_ticket_sources.raw(filter=None, timeout=None)`
- HTTP route: `GET /api/v1.0/tickets/sources`
- Source controller: `IncidentIQ API`

Get ticket sources

Retrieves all available ticket source types configured for the site. Sources indicate how tickets were created (e.g., web portal, email, phone, API, mobile app) and are useful for analytics, routing rules, and reporting on ticket origin channels.

**Workflow Example**
1. List sources: [GET /api/v1.0/tickets/sources](#/Tickets/getTicketSources) → retrieve available source types
2. Use for filtering: Include `SourceId` in [POST /api/v1.0/tickets](#/Tickets/searchTickets) to filter by origin
3. Use for reporting: Group ticket metrics by source to analyze channel performance

**Response Fields**: Each source includes `SourceId`, `Name`, `Description`, and whether it's the default source.

**Use Cases**: Building source dropdowns for ticket creation, analyzing ticket volume by channel, configuring routing rules based on ticket origin.

**Related Endpoints**
- [POST /api/v1.0/tickets](#/Tickets/searchTickets) – Filter tickets by SourceId
- [POST /api/v1.0/tickets/new](#/Tickets/createTicket) – Create ticket with specific source
- [GET /api/v1.0/tickets/{ticketId}](#/Tickets/getTicket) – View ticket's source

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `filter` | `$filter` | `query` | `no` | `str` | `-` | OData filter expression |

#### Returns

- Typed call return: `TicketSourcesResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketSourcesResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_ticket_status`

Provenance: Golden OpenAPI contract

Operation ID: `getTicketStatus`

- Sync: `client.tickets.get_ticket_status(ticket_id=..., timeout=None)`
- Async: `await client.tickets.get_ticket_status(ticket_id=..., timeout=None)`
- Raw payload: `client.tickets.get_ticket_status.raw(ticket_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/tickets/{ticketId}/status`
- Source controller: `IncidentIQ API`

Get ticket status

Retrieves the latest workflow status information for a ticket, including the active workflow step, approval state, and whether the ticket can be routed for approval. Use this response as the authoritative source for the `WorkflowStepId` needed when advancing or resolving a ticket.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to locate the ticket and extract `Items[].TicketId`.

**Workflow Example**
1. Filter tickets with [POST /api/v1.0/tickets](#/Tickets/searchTickets) (status, product, requester filters) and capture `Items[].TicketId`.
2. Call [GET /api/v1.0/tickets/{ticketId}/status](#/Tickets/getTicketStatus) to read `Item.CurrentWorkflowStep.WorkflowStepId`, approval flags, and approver assignments.
3. Advance the ticket by calling [POST /api/v1.0/tickets/{ticketId}/status/{statusId}](#/Tickets/setTicketStatus) with a valid workflow step identifier obtained from this response.

**Minimal Required Fields**: ticketId

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | UUID of the ticket whose status should be retrieved. Obtain via POST /api/v1.0/tickets and extract `Items[].TicketId`. |

#### Returns

- Typed call return: `TicketStatusResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketStatusResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_ticket_status_by_id`

Provenance: Golden OpenAPI contract

Operation ID: `getTicketStatusById`

- Sync: `client.tickets.get_ticket_status_by_id(status_id=..., timeout=None)`
- Async: `await client.tickets.get_ticket_status_by_id(status_id=..., timeout=None)`
- Raw payload: `client.tickets.get_ticket_status_by_id.raw(status_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/tickets/statuses/{statusId}`
- Source controller: `IncidentIQ API`

Get ticket status by ID

Retrieves details for a specific ticket status (workflow step) by its identifier. Status definitions include display name, color coding, sort order, and whether the status represents a closed state. Use this to display status metadata or validate workflow configurations.

**Prerequisites**
1. **statusId** – Obtain from ticket data (`Item.StatusId`) or from [GET /api/v1.0/tickets/workflows/statuses](#/Tickets/getAllWorkflowStatuses).

**Workflow Example**
1. Get ticket: [GET /api/v1.0/tickets/{ticketId}](#/Tickets/getTicket) → extract `StatusId`
2. Get status details: [GET /api/v1.0/tickets/statuses/{statusId}](#/Tickets/getTicketStatusById)
3. Display: Use status name, color, and IsClosed for UI rendering

**Response Fields**: Includes `WorkflowStepId`, `StepName`, `StatusName`, `Color`, `IsClosed`, `DisplayOrder`, and associated workflow.

**Related Endpoints**
- [GET /api/v1.0/tickets/workflows/statuses](#/Tickets/getAllWorkflowStatuses) – List all statuses across workflows
- [GET /api/v1.0/tickets/{workflowId}/statuses](#/Tickets/getWorkflowStatuses) – List statuses for specific workflow
- [GET /api/v1.0/tickets/{ticketId}/status](#/Tickets/getTicketStatus) – Get ticket's current status

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `status_id` | `statusId` | `path` | `yes` | `str` | `-` | Unique identifier of the workflow step/status to retrieve |

#### Returns

- Typed call return: `TicketStatusSingleResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketStatusSingleResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_ticket_teams`

Provenance: Golden OpenAPI contract

Operation ID: `getTicketTeams`

- Sync: `client.tickets.get_ticket_teams(ticket_id=..., p=None, s=None, timeout=None)`
- Async: `await client.tickets.get_ticket_teams(ticket_id=..., p=None, s=None, timeout=None)`
- Raw payload: `client.tickets.get_ticket_teams.raw(ticket_id=..., p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v1.0/tickets/{ticketId}/teams`
- Source controller: `IncidentIQ API`

Get teams associated with ticket

Retrieves all teams associated with a ticket, including the assigned team, teams with members following the ticket, and teams added for collaboration purposes. Use this to understand team involvement and coordinate cross-team work.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to find the ticket and extract `Items[].TicketId`.

**Workflow Example**
1. Locate ticket: [POST /api/v1.0/tickets](#/Tickets/searchTickets) → extract `TicketId`
2. Get teams: [GET /api/v1.0/tickets/{ticketId}/teams](#/Tickets/getTicketTeams)
3. Review: Identify teams involved and their roles
4. Coordinate: Contact team leads or add additional teams as followers

**Response Fields**: Each team includes `TeamId`, `Name`, `Description`, and member count information.

**Query Parameters**: Supports pagination with `$p` (page) and `$s` (page size).

**Use Cases**: Identifying responsible teams, coordinating handoffs between teams, auditing team involvement, understanding escalation paths.

**Related Endpoints**
- [POST /api/v1.0/tickets/{ticketId}/followers/team/{teamId}](#/Tickets/addTicketFollowerTeam) – Add team as followers
- [GET /api/v1.0/teams](#/Teams/listTeams) – List all teams
- [POST /api/v1.0/tickets/bulk/assign](#/Tickets/bulkAssignTickets) – Assign tickets to teams

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | Unique identifier of the ticket |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index |
| `s` | `$s` | `query` | `no` | `int` | `-` | Page size (default 100) |

#### Returns

- Typed call return: `TeamListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TeamListResponse`
- Pagination helper: `client.tickets.get_ticket_teams.iter_pages(start_page=1, page_size=100, max_pages=None, ticket_id=..., p=None, s=None, timeout=None)`

---

### `get_ticket_timeline`

Provenance: Golden OpenAPI contract

Operation ID: `getTicketTimeline`

- Sync: `client.tickets.get_ticket_timeline(ticket_id=..., p=None, s=None, timeout=None)`
- Async: `await client.tickets.get_ticket_timeline(ticket_id=..., p=None, s=None, timeout=None)`
- Raw payload: `client.tickets.get_ticket_timeline.raw(ticket_id=..., p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v1.0/tickets/{ticketId}/timeline`
- Source controller: `IncidentIQ API`

Get ticket timeline

Retrieves the chronological timeline for a ticket, combining activities, workflow transitions, and automation events with pagination support.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to find the ticket and extract `Items[].TicketId`.

**Workflow Example**
1. Locate ticket: [POST /api/v1.0/tickets](#/Tickets/searchTickets) with filters (status, product, requester).
2. Extract the identifier from `Items[].TicketId`.
3. Call [GET /api/v1.0/tickets/{ticketId}/timeline](#/Tickets/getTicketTimeline), optionally paging with `$p`/`$s`, to render the combined event history.

**Minimal Required Fields**: ticketId (path). Optional pagination: $p, $s.

Timeline results include both user-authored activity entries and automated events generated by workflow rules, ticket status transitions, and background jobs. After workflow transitions such as [POST /api/v1.0/tickets/{ticketId}/start](#/Tickets/startTicket) or inventory operations like [POST /api/v1.0/inventory/actions/ids/new](#/Inventory/createInventoryActionsBatch), reuse this GET (or the equivalent POST form) to refresh the activity stream shown to technicians. Part usage entries surface as `TicketActivityPart` items linked to the underlying inventory action.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | UUID of the ticket whose timeline should be retrieved. Obtain via POST /api/v1.0/tickets and extract `Items[].TicketId`. |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index for paginating timeline events. |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of timeline records to return per page. |

#### Returns

- Typed call return: `TicketTimelineResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketTimelineResponse`
- Pagination helper: `client.tickets.get_ticket_timeline.iter_pages(start_page=1, page_size=100, max_pages=None, ticket_id=..., p=None, s=None, timeout=None)`

---

### `get_ticket_users`

Provenance: Golden OpenAPI contract

Operation ID: `getTicketUsers`

- Sync: `client.tickets.get_ticket_users(ticket_id=..., p=None, s=None, timeout=None)`
- Async: `await client.tickets.get_ticket_users(ticket_id=..., p=None, s=None, timeout=None)`
- Raw payload: `client.tickets.get_ticket_users.raw(ticket_id=..., p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v1.0/tickets/{ticketId}/users`
- Source controller: `IncidentIQ API`

Get users associated with ticket

Retrieves all users associated with a ticket, including the requester, assignees, followers, and other related users. Provides a comprehensive view of everyone involved with a ticket.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to find the ticket and extract `Items[].TicketId`.

**Workflow Example**
1. Find ticket: [POST /api/v1.0/tickets](#/Tickets/searchTickets) → extract `TicketId`
2. Get users: [GET /api/v1.0/tickets/{ticketId}/users](#/Tickets/getTicketUsers)
3. Analyze: Review user roles and involvement
4. Take action: Add followers, reassign, or contact stakeholders as needed

**Response Fields**: Each user includes `UserId`, `Name`, `Email`, `Role` on the ticket (Requester, Owner, Follower, etc.), and user details.

**Query Parameters**: Supports pagination with `$p` (page index, default 0) and `$s` (page size, default 100).

**Use Cases**: Building user involvement reports, sending bulk notifications, auditing ticket access, identifying stakeholders for escalation.

**Related Endpoints**
- [GET /api/v1.0/tickets/{ticketId}/followers](#/Tickets/getTicketFollowers) – Just followers
- [GET /api/v1.0/tickets/{ticketId}/teams](#/Tickets/getTicketTeams) – Teams involved
- [POST /api/v1.0/tickets/{ticketId}/followers/user/{userId}](#/Tickets/addTicketFollowerUser) – Add user

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | Unique identifier of the ticket |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index |
| `s` | `$s` | `query` | `no` | `int` | `-` | Page size (default 100) |

#### Returns

- Typed call return: `UserListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UserListResponse`
- Pagination helper: `client.tickets.get_ticket_users.iter_pages(start_page=1, page_size=100, max_pages=None, ticket_id=..., p=None, s=None, timeout=None)`

---

### `get_ticket_view`

Provenance: Golden OpenAPI contract

Operation ID: `getTicketView`

- Sync: `client.tickets.get_ticket_view(view_id=..., timeout=None)`
- Async: `await client.tickets.get_ticket_view(view_id=..., timeout=None)`
- Raw payload: `client.tickets.get_ticket_view.raw(view_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/tickets/views/{viewId}`
- Source controller: `IncidentIQ API`

Get ticket view

Retrieves the complete definition of a saved ticket view, including its filters, column configuration, sort order, and sharing settings. Use this to inspect or clone an existing view.

**Prerequisites**
1. **viewId** – Use [GET /api/v1.0/tickets/views](#/Tickets/listTicketViews) to list available views and extract `Items[].ViewId`.

**Workflow Example**
1. List views: [GET /api/v1.0/tickets/views](#/Tickets/listTicketViews) → identify `ViewId` of interest
2. Get definition: [GET /api/v1.0/tickets/views/{viewId}](#/Tickets/getTicketView)
3. (Optional) Clone: Modify the returned definition and use [POST /api/v1.0/tickets/views/new](#/Tickets/createTicketView) to create a copy

**Response Fields**: Includes Name, Filters (facet conditions), Columns (visible fields), Sort, and sharing scope (personal or shared).

**Related Endpoints**
- [GET /api/v1.0/tickets/views](#/Tickets/listTicketViews) – List all views
- [POST /api/v1.0/tickets/views/{viewId}](#/Tickets/updateTicketView) – Modify view
- [POST /api/v1.0/tickets](#/Tickets/searchTickets) – Execute view as a search

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `view_id` | `viewId` | `path` | `yes` | `str` | `-` | Identifier of the ticket view to retrieve. |

#### Returns

- Typed call return: `ViewItemGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ViewItemGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_workflow_statuses`

Provenance: Golden OpenAPI contract

Operation ID: `getWorkflowStatuses`

- Sync: `client.tickets.get_workflow_statuses(workflow_id=..., timeout=None)`
- Async: `await client.tickets.get_workflow_statuses(workflow_id=..., timeout=None)`
- Raw payload: `client.tickets.get_workflow_statuses.raw(workflow_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/tickets/{workflowId}/statuses`
- Source controller: `IncidentIQ API`

Get statuses for specific workflow

Retrieves all ticket statuses available within a specific workflow, including the status sequence, display colors, and which statuses represent closed states. Use this to populate workflow-specific status dropdowns and understand valid status transitions.

**Prerequisites**
1. **workflowId** – Use [GET /api/v1.0/workflows](#/Workflows/listWorkflows) to list workflows and extract `WorkflowId`, or get from ticket data via [GET /api/v1.0/tickets/{ticketId}](#/Tickets/getTicket) → `Item.WorkflowId`.

**Workflow Example**
1. Get ticket: [GET /api/v1.0/tickets/{ticketId}](#/Tickets/getTicket) → extract `WorkflowId`
2. List statuses: [GET /api/v1.0/tickets/{workflowId}/statuses](#/Tickets/getWorkflowStatuses)
3. Display: Show valid status options for the ticket's workflow
4. Transition: Use [POST /api/v1.0/tickets/{ticketId}/status/{statusId}](#/Tickets/setTicketStatus) to change status

**Response Fields**: Each status includes `WorkflowStepId`, `StepName`, `Color`, `IsClosed`, `DisplayOrder`, and transition rules.

**Use Cases**: Building workflow-specific status selectors, validating status transitions, displaying available actions for tickets.

**Note**: For all statuses across all workflows, use [GET /api/v1.0/tickets/workflows/statuses](#/Tickets/getAllWorkflowStatuses).

**Related Endpoints**
- [GET /api/v1.0/workflows](#/Workflows/listWorkflows) – List all workflows
- [GET /api/v1.0/tickets/workflows/statuses](#/Tickets/getAllWorkflowStatuses) – All statuses across workflows
- [POST /api/v1.0/tickets/{ticketId}/status/{statusId}](#/Tickets/setTicketStatus) – Change ticket status

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `workflow_id` | `workflowId` | `path` | `yes` | `str` | `-` | Unique identifier of the workflow |

#### Returns

- Typed call return: `TicketStatusListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketStatusListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_workflow_step_status`

Provenance: Golden OpenAPI contract

Operation ID: `getWorkflowStepStatus`

- Sync: `client.tickets.get_workflow_step_status(workflow_step_id=..., timeout=None)`
- Async: `await client.tickets.get_workflow_step_status(workflow_step_id=..., timeout=None)`
- Raw payload: `client.tickets.get_workflow_step_status.raw(workflow_step_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/tickets/workflow/steps/{workflowStepId}`
- Source controller: `IncidentIQ API`

Get workflow step status

Retrieves the ticket status definition associated with a specific workflow step. Returns status metadata including step name, closure state, and workflow configuration.

**Use Cases**
- Looking up status details before changing ticket state
- Validating workflow step configuration
- Building status selection interfaces

**Prerequisites**
- Obtain workflow step IDs via [GET /api/v1.0/workflows/steps](#/Workflows/getWorkflowSteps)
- Or extract from ticket response `WorkflowStep.WorkflowStepId`

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `workflow_step_id` | `workflowStepId` | `path` | `yes` | `str` | `-` | UUID of the workflow step to retrieve |

#### Returns

- Typed call return: `TicketStatusSingleResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketStatusSingleResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `has_active_events`

Provenance: Golden OpenAPI contract

Operation ID: `hasActiveEvents`

- Sync: `client.tickets.has_active_events(ticket_id=..., timeout=None)`
- Async: `await client.tickets.has_active_events(ticket_id=..., timeout=None)`
- Raw payload: `client.tickets.has_active_events.raw(ticket_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/tickets/active-events/{ticketId}`
- Source controller: `IncidentIQ API`

Check for active scheduled events

Checks whether a ticket has any active scheduled events linked to it. Returns a boolean indicating if maintenance windows, recurring tasks, or other scheduled activities are currently associated with the ticket.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to locate the ticket and extract `Items[].TicketId`.

**Workflow Example**
1. Find ticket: [POST /api/v1.0/tickets](#/Tickets/searchTickets) → extract `TicketId`
2. Check events: [GET /api/v1.0/tickets/active-events/{ticketId}](#/Tickets/hasActiveEvents)
3. If `true`: Review events before modifying ticket to avoid conflicts with scheduled work

**Use Cases**:
- Validate before closing a ticket with pending scheduled work
- Check for conflicts before reassigning
- Display event indicator in ticket detail views

**Response**: Returns `true` if active scheduled events exist, `false` otherwise.

**Related Endpoints**
- [GET /api/v1.0/tickets/{ticketId}](#/Tickets/getTicket) – View full ticket details
- [GET /api/v1.0/tickets/{ticketId}/timeline](#/Tickets/getTicketTimeline) – View ticket activity history

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | UUID of the ticket. |

#### Returns

- Typed call return: `bool`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_ticket_next_step_templates`

Provenance: Golden OpenAPI contract

Operation ID: `listTicketNextStepTemplates`

- Sync: `client.tickets.list_ticket_next_step_templates(top=None, skip=None, orderby=None, timeout=None)`
- Async: `await client.tickets.list_ticket_next_step_templates(top=None, skip=None, orderby=None, timeout=None)`
- Raw payload: `client.tickets.list_ticket_next_step_templates.raw(top=None, skip=None, orderby=None, timeout=None)`
- HTTP route: `GET /api/v1.0/tickets/next-step/templates`
- Source controller: `IncidentIQ API`

List ticket next step templates

Retrieves a paginated list of ticket next step templates. Templates define predefined workflows that can be applied to tickets during the resolution process.

**Workflow Example**
1. List templates: `GET /api/v1.0/tickets/next-step/templates`
2. Extract `Items[].TicketNextStepTemplateId` for use with other operations
3. Apply template to ticket using the ticket workflow endpoints

**Paging**: Supports standard paging parameters (`$top`, `$skip`) and custom filters via query string.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `top` | `$top` | `query` | `no` | `int` | `-` | Maximum number of records to return (default: 20). |
| `skip` | `$skip` | `query` | `no` | `int` | `-` | Number of records to skip for pagination. |
| `orderby` | `$orderby` | `query` | `no` | `str` | `-` | Field to sort results by (default: Name ascending). |

#### Returns

- Typed call return: `TicketNextStepTemplateListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketNextStepTemplateListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_ticket_next_step_types`

Provenance: Golden OpenAPI contract

Operation ID: `listTicketNextStepTypes`

- Sync: `client.tickets.list_ticket_next_step_types(timeout=None)`
- Async: `await client.tickets.list_ticket_next_step_types(timeout=None)`
- Raw payload: `client.tickets.list_ticket_next_step_types.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/tickets/next-step/types`
- Source controller: `IncidentIQ API`

List next-step types

Retrieves the collection of available next-step types (e.g., "Verify Asset", "Requestor Acknowledgment") defined for the site. These types categorize and drive ticket workflow recommendations, helping agents understand what actions to take next.

**Workflow Example**
1. Get types: [GET /api/v1.0/tickets/next-step/types](#/Tickets/listTicketNextStepTypes) to list all configured types
2. Select type: Choose appropriate `TicketNextStepTypeId` based on needed action
3. Create next step: [POST /api/v1.0/tickets/{ticketId}/next-steps/new](#/Tickets/createTicketNextStep) with the type ID
4. Monitor: [GET /api/v1.0/tickets/{ticketId}/next-steps](#/Tickets/getTicketNextSteps) to view ticket recommendations

**Response Fields**: Each type includes `TicketNextStepTypeId`, `Name`, `Description`, `IsActive`, and configuration settings.

**Use Cases**: Building next-step creation dialogs, filtering available actions by type, understanding workflow options for ticket resolution.

**Related Endpoints**
- [GET /api/v1.0/tickets/next-step/types/{ticketNextStepTypeId}](#/Tickets/getTicketNextStepType) – Get specific type details
- [POST /api/v1.0/tickets/{ticketId}/next-steps/new](#/Tickets/createTicketNextStep) – Create next step
- [GET /api/v1.0/tickets/{ticketId}/next-steps](#/Tickets/getTicketNextSteps) – List ticket next steps

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `list[Any]`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_ticket_priority_levels`

Provenance: Golden OpenAPI contract

Operation ID: `listTicketPriorityLevels`

- Sync: `client.tickets.list_ticket_priority_levels(timeout=None)`
- Async: `await client.tickets.list_ticket_priority_levels(timeout=None)`
- Raw payload: `client.tickets.list_ticket_priority_levels.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/tickets/priorities`
- Source controller: `IncidentIQ API`

List Ticket Priorities

Retrieves the site-defined priority level metadata, including numeric score ranges, labels, and badge colors. Caller can map the numeric `Priority` and optional `PriorityLevelId` returned by ticket endpoints to the descriptive values used in the UI.

**Workflow Example**
1. Retrieve the ticket: [GET /api/v1.0/tickets/{ticketId}](#/Tickets/getTicket) → read `Item.Priority` and `Item.PriorityLevelId`.
2. Call this endpoint to resolve the matching priority metadata for display in dashboards or escalations.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `TicketPriorityListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketPriorityListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_ticket_slas`

Provenance: Golden OpenAPI contract

Operation ID: `listTicketSlas`

- Sync: `client.tickets.list_ticket_slas(p=None, s=None, o=None, body=None, timeout=None)`
- Async: `await client.tickets.list_ticket_slas(p=None, s=None, o=None, body=None, timeout=None)`
- Raw payload: `client.tickets.list_ticket_slas.raw(p=None, s=None, o=None, body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/slas`
- Source controller: `IncidentIQ API`

List Ticket SLAs

Retrieves the SLA definition and accumulated timer metrics for each ticket that matches the supplied `GetTicketsRequest` filters. The service first runs the same query-engine pipeline as [POST /api/v1.0/tickets](#/Tickets/searchTickets) using the `$p`, `$s`, and `$o` query parameters, then resolves SLA data for every `TicketId` returned on that page. The service overwrites `FieldsToReturn` with `TicketId` so the upstream query only fetches identifiers.

**Prerequisites:**
- **Status/workflow filters** - Call [GET /api/v1.0/workflows/allproducts/site/{siteId}](#/Workflows/listSiteProductWorkflows) and reuse `WorkflowSteps[].WorkflowStepId`/`StatusId` when building `Filters[]` entries
- **Other facet IDs** - Use [GET /api/v1.0/tags/query](#/Tags/getTagsByQuery) for tag filters, [GET /api/v1.0/tickets/priorities](#/Tickets/listTicketPriorityLevels) for priority IDs, and [POST /api/v1.0/search](#/Search/globalSearch) to look up agent/requester UUIDs
- **Ticket preview** - Submit the same body to [POST /api/v1.0/tickets](#/Tickets/searchTickets) to verify that the queue returns the expected tickets before requesting SLA information

**Workflow Example:**
1. **Preview queue:** [POST /api/v1.0/tickets](#/Tickets/searchTickets) with your desired `Filters[]` to confirm `Items[].TicketId` order
2. **Batch SLA lookup:** [POST /api/v1.0/tickets/slas](#/Tickets/listTicketSlas) (with `$s=50&$o=TicketPriority desc`) using the same request body to receive SLA objects for each ticket on that page
3. **Drill down:** [GET /api/v1.0/tickets/{ticketId}/sla](#/Tickets/getTicketSla) to display the detailed timers for a single ticket if needed

**Minimal Required Fields:**
- Provide at least one `Filters[]` facet (status, workflow, agent, ticketId, etc.) or reuse a saved `Schema` to scope the queue
- Leaving the body empty reuses the caller's default ticket view

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index forwarded to the internal ticket search before SLA hydration. |
| `s` | `$s` | `query` | `no` | `int` | `-` | Page size (number of tickets) pulled from the queue before resolving SLA data. Defaults to 20 and typically capped at 100. |
| `o` | `$o` | `query` | `no` | `Any` | `-` | Sort expression: field name followed by optional direction (e.g., `TicketPriority desc`). Direction can be `asc`, `ascending`, `desc`, or `descending`. Default direction is ascending. See [TicketSortField](#/components/schemas/TicketSortField) for valid field names. |
| `body` | `body` | `body` | `no` | `GetTicketsRequest` | `GetTicketsRequest` | Ticket queue payload that mirrors the body accepted by POST /api/v1.0/tickets. The service ignores `FieldsToReturn` and always requests `TicketId` internally. |

#### Returns

- Typed call return: `TicketSlaListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketSlaListResponse`
- Pagination helper: `client.tickets.list_ticket_slas.iter_pages(start_page=1, page_size=100, max_pages=None, p=None, s=None, o=None, body=None, timeout=None)`

---

### `list_ticket_statuses`

Provenance: Golden OpenAPI contract

Operation ID: `listTicketStatuses`

- Sync: `client.tickets.list_ticket_statuses(timeout=None)`
- Async: `await client.tickets.list_ticket_statuses(timeout=None)`
- Raw payload: `client.tickets.list_ticket_statuses.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/tickets/statuses`
- Source controller: `IncidentIQ API`

List all ticket statuses

Retrieves all available ticket statuses (workflow steps) configured for the site. Use this endpoint to build status dropdowns, validate status transitions, or map status IDs to display names.

**Related Endpoints**
- [GET /api/v1.0/tickets/{ticketId}/status](#/Tickets/getTicketStatus) – Get current status for a specific ticket
- [POST /api/v1.0/tickets/{ticketId}/status/{statusId}](#/Tickets/setTicketStatus) – Change ticket status
- [GET /api/v1.0/workflows/allproducts/site/{siteId}](#/Workflows/listWorkflows) – Get workflows with detailed step information

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `TicketStatusListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketStatusListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_ticket_timeline`

Provenance: Golden OpenAPI contract

Operation ID: `listTicketTimeline`

- Sync: `client.tickets.list_ticket_timeline(ticket_id=..., body=None, timeout=None)`
- Async: `await client.tickets.list_ticket_timeline(ticket_id=..., body=None, timeout=None)`
- Raw payload: `client.tickets.list_ticket_timeline.raw(ticket_id=..., body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/timeline`
- Source controller: `IncidentIQ API`

Get ticket timeline (POST)

POST form of the timeline query used by legacy UI components. Returns the same payload as the GET variant without requiring a request body.

**Usage**:
- Call immediately after workflow changes (e.g., confirmation/start flows) when the UI expects to POST to the timeline endpoint.
- Refresh the activity stream after adding parts via [POST /api/v1.0/inventory/actions/ids/new](#/Inventory/createInventoryActionsBatch); the response includes `TicketActivityPart` entries summarizing the inventory action.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | UUID of the ticket whose timeline should be retrieved. Obtain via POST /api/v1.0/tickets and extract `Items[].TicketId`. |
| `body` | `body` | `body` | `no` | `GetTicketTimelineRequest` | `GetTicketTimelineRequest` | Optional filtering options to control which activity types are included in the timeline. When omitted, all activity types are loaded. |

#### Returns

- Typed call return: `TicketTimelineResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketTimelineResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_ticket_views`

Provenance: Golden OpenAPI contract

Operation ID: `listTicketViews`

- Sync: `client.tickets.list_ticket_views(p=None, s=None, timeout=None)`
- Async: `await client.tickets.list_ticket_views(p=None, s=None, timeout=None)`
- Raw payload: `client.tickets.list_ticket_views.raw(p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v1.0/tickets/views`
- Source controller: `IncidentIQ API`

List ticket views

Returns all saved ticket views available to the authenticated user, including personal views and shared views from their team or site. Views define saved search criteria, column layouts, and sort orders for ticket lists.

**Workflow Example**
1. List views: [GET /api/v1.0/tickets/views](#/Tickets/listTicketViews) → retrieve available `ViewId` values
2. Select view: Choose a view to apply or inspect
3. Get details: [GET /api/v1.0/tickets/views/{viewId}](#/Tickets/getTicketView) for full view definition
4. Execute search: Use view filters with [POST /api/v1.0/tickets](#/Tickets/searchTickets)

**Response Fields**: Each view includes `ViewId`, `Name`, `ViewTypeId`, `PageSize`, `UserId` (owner), and sharing metadata.

**Query Parameters**: Supports pagination with `$p` (page) and `$s` (page size).

**Use Cases**: Building view selector dropdowns, discovering shared team views, auditing view configurations, cloning existing views.

**Related Endpoints**
- [GET /api/v1.0/tickets/views/{viewId}](#/Tickets/getTicketView) – Get full view definition
- [POST /api/v1.0/tickets/views/new](#/Tickets/createTicketView) – Create new view
- [POST /api/v1.0/tickets](#/Tickets/searchTickets) – Execute search using view filters

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index. Defaults to 0 when omitted. |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of records per page. Defaults to 100 when omitted. |

#### Returns

- Typed call return: `ViewListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ViewListResponse`
- Pagination helper: `client.tickets.list_ticket_views.iter_pages(start_page=1, page_size=100, max_pages=None, p=None, s=None, timeout=None)`

---

### `list_wizard_categories`

Provenance: Golden OpenAPI contract

Operation ID: `listWizardCategories`

- Sync: `client.tickets.list_wizard_categories(product_filter_type=None, parent_category_id=None, apply_site_visibility=None, timeout=None)`
- Async: `await client.tickets.list_wizard_categories(product_filter_type=None, parent_category_id=None, apply_site_visibility=None, timeout=None)`
- Raw payload: `client.tickets.list_wizard_categories.raw(product_filter_type=None, parent_category_id=None, apply_site_visibility=None, timeout=None)`
- HTTP route: `GET /api/v1.0/tickets/wizards/categories`
- Source controller: `IncidentIQ API`

List ticket wizard categories

Retrieves categories of type 'Ticket_Wizards' that organize ticket creation wizards. These are the top-level groupings shown in the ticket submission wizard interface (e.g., 'Report an Issue', 'Request Something').

**Workflow Example**
1. Call [GET /api/v1.0/tickets/wizards/categories](#/Categories/listWizardCategories) without ParentCategoryId to fetch top-level wizard categories.
2. Pass a returned CategoryId as ParentCategoryId to list child categories or nested wizard steps.
3. Use category IDs to display or configure the ticket submission experience.

**Minimal Required Fields**: none (ParentCategoryId is optional for drilling into sub-categories).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `product_filter_type` | `ProductFilterType` | `query` | `no` | `str` | `-` | Filter by product scope |
| `parent_category_id` | `ParentCategoryId` | `query` | `no` | `str` | `-` | Filter to children of a specific parent category |
| `apply_site_visibility` | `ApplySiteVisibility` | `query` | `no` | `bool` | `-` | Whether to apply site-level visibility rules |

#### Returns

- Typed call return: `CategoryListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CategoryListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `log_support_ticket`

Provenance: Golden OpenAPI contract

Operation ID: `logSupportTicket`

- Sync: `client.tickets.log_support_ticket(ticket_id=..., site_id=..., timeout=None)`
- Async: `await client.tickets.log_support_ticket(ticket_id=..., site_id=..., timeout=None)`
- Raw payload: `client.tickets.log_support_ticket.raw(ticket_id=..., site_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/support/{ticketId}/{siteId}`
- Source controller: `IncidentIQ API`

Log support ticket

Logs a support ticket entry for an existing ticket within a specific site context. This is used to escalate tickets to a support team or create a support record for cross-site coordination, typically when a ticket requires assistance from another site or external support resources.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to find the ticket and extract `Items[].TicketId`.
2. **siteId** – Use obtain from application context (user's site affiliation) or [GET /api/v1.0/sites/{SiteId}/settings](#/Sites/getSiteSettingsById) to verify target site.

**Workflow Example**
1. Identify ticket: [POST /api/v1.0/tickets](#/Tickets/searchTickets) with search criteria → extract `TicketId`
2. Determine support site: use known `SiteId` from application context or configured support site
3. Log support ticket: [POST /api/v1.0/tickets/support/{ticketId}/{siteId}](#/Tickets/logSupportTicket)
4. Track: The ticket's support status is updated for coordination purposes

**Use Cases**: Cross-site support coordination, escalation to central IT, logging support interactions for audit purposes.

**Related Endpoints**
- [POST /api/v1.0/tickets](#/Tickets/searchTickets) – Find tickets to escalate
- [GET /api/v1.0/sites/{SiteId}/settings](#/Sites/getSiteSettingsById) – Get site details

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | UUID of the ticket. |
| `site_id` | `siteId` | `path` | `yes` | `str` | `-` | UUID of the site. |

#### Returns

- Typed call return: `Any`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `mark_ticket_as_duplicate`

Provenance: Golden OpenAPI contract

Operation ID: `markTicketAsDuplicate`

- Sync: `client.tickets.mark_ticket_as_duplicate(ticket_id=..., duplicate_of_ticket_id=..., timeout=None)`
- Async: `await client.tickets.mark_ticket_as_duplicate(ticket_id=..., duplicate_of_ticket_id=..., timeout=None)`
- Raw payload: `client.tickets.mark_ticket_as_duplicate.raw(ticket_id=..., duplicate_of_ticket_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/mark-as-duplicate/{duplicateOfTicketId}`
- Source controller: `IncidentIQ API`

Mark ticket as duplicate

Marks a ticket as a duplicate of another ticket so that work can be consolidated.

**Prerequisites**
1. **ticketId** – The ticket being marked duplicate. Obtain via [POST /api/v1.0/tickets](#/Tickets/searchTickets) and read `Items[].TicketId`.
2. **duplicateOfTicketId** – The primary ticket that will remain open. Also obtain via [POST /api/v1.0/tickets](#/Tickets/searchTickets) or from the ticket detail view `Item.TicketId`.

**Workflow Example**
1. Search for both tickets with [POST /api/v1.0/tickets](#/Tickets/searchTickets) to get their UUIDs.
2. Choose the ticket to close (`ticketId`) and the primary ticket (`duplicateOfTicketId`).
3. Call [POST /api/v1.0/tickets/{ticketId}/mark-as-duplicate/{duplicateOfTicketId}](#/Tickets/markTicketAsDuplicate) to link the records.

**Minimal Required Fields**: ticketId, duplicateOfTicketId

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | UUID of the ticket flagged as duplicate. Obtain via POST /api/v1.0/tickets and extract `Items[].TicketId`. |
| `duplicate_of_ticket_id` | `duplicateOfTicketId` | `path` | `yes` | `str` | `-` | UUID of the original ticket that remains active. Obtain via POST /api/v1.0/tickets or GET /api/v1.0/tickets/{ticketId} and read `Item.TicketId`. |

#### Returns

- Typed call return: `TicketDuplicateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketDuplicateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `mark_ticket_not_sensitive`

Provenance: Golden OpenAPI contract

Operation ID: `markTicketNotSensitive`

- Sync: `client.tickets.mark_ticket_not_sensitive(ticket_id=..., timeout=None)`
- Async: `await client.tickets.mark_ticket_not_sensitive(ticket_id=..., timeout=None)`
- Raw payload: `client.tickets.mark_ticket_not_sensitive.raw(ticket_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/mark-not-sensitive`
- Source controller: `IncidentIQ API`

Remove sensitive flag from ticket

Removes the sensitive information flag from a ticket, restoring normal visibility settings. After removal, the ticket will appear in standard searches and reports without the privacy restrictions that were previously applied.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) with sensitive flag filter to find marked tickets and extract `Items[].TicketId`.

**Workflow Example**
1. Find sensitive tickets: [POST /api/v1.0/tickets](#/Tickets/searchTickets) with `HasSensitiveInformation: true` filter → extract `TicketId`
2. Review: Confirm the sensitive designation is no longer needed
3. Remove flag: [POST /api/v1.0/tickets/{ticketId}/mark-not-sensitive](#/Tickets/markTicketNotSensitive)
4. Verify: [GET /api/v1.0/tickets/{ticketId}](#/Tickets/getTicket) to confirm `HasSensitiveInformation: false`

**Use Cases**: Declassifying tickets after investigation completion, correcting mistakenly flagged tickets, restoring visibility for reporting purposes.

**Note**: Removing the sensitive flag makes the ticket visible to users who may not have seen it previously. Ensure this is appropriate before proceeding.

**Related Endpoints**
- [POST /api/v1.0/tickets/{ticketId}/mark-sensitive](#/Tickets/markTicketSensitive) – Mark ticket as sensitive
- [POST /api/v1.0/tickets](#/Tickets/searchTickets) – Filter by sensitive status
- [GET /api/v1.0/tickets/{ticketId}](#/Tickets/getTicket) – View ticket sensitivity status

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | Unique identifier of the ticket |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `mark_ticket_not_urgent`

Provenance: Golden OpenAPI contract

Operation ID: `markTicketNotUrgent`

- Sync: `client.tickets.mark_ticket_not_urgent(ticket_id=..., timeout=None)`
- Async: `await client.tickets.mark_ticket_not_urgent(ticket_id=..., timeout=None)`
- Raw payload: `client.tickets.mark_ticket_not_urgent.raw(ticket_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/mark-not-urgent`
- Source controller: `IncidentIQ API`

Remove urgent flag from ticket

Removes the urgent flag from a ticket, returning it to normal priority handling in agent queues and workflows. Use this when the urgent situation has been addressed or when a ticket was mistakenly flagged as urgent.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) with urgent filter to find flagged tickets and extract `Items[].TicketId`.

**Workflow Example**
1. Find urgent tickets: [POST /api/v1.0/tickets](#/Tickets/searchTickets) with `IsUrgent: true` filter → extract `TicketId`
2. Review: Confirm the urgent situation has been resolved
3. Remove flag: [POST /api/v1.0/tickets/{ticketId}/mark-not-urgent](#/Tickets/markTicketNotUrgent)
4. Verify: [GET /api/v1.0/tickets/{ticketId}](#/Tickets/getTicket) to confirm `IsUrgent: false`

**Use Cases**: De-escalating tickets after emergency resolution, correcting accidental urgent flags, normalizing queue priority after initial response.

**Note**: Removing the urgent flag may affect the ticket's position in agent queues and stop escalation workflows that were triggered by the urgent status.

**Related Endpoints**
- [POST /api/v1.0/tickets/{ticketId}/mark-urgent](#/Tickets/markTicketUrgent) – Mark ticket as urgent
- [POST /api/v1.0/tickets](#/Tickets/searchTickets) – Filter by urgent status
- [POST /api/v1.0/tickets/bulk/set-priority](#/Tickets/bulkSetTicketPriority) – Adjust priority levels

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | Unique identifier of the ticket |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `mark_ticket_sensitive`

Provenance: Golden OpenAPI contract

Operation ID: `markTicketSensitive`

- Sync: `client.tickets.mark_ticket_sensitive(ticket_id=..., timeout=None)`
- Async: `await client.tickets.mark_ticket_sensitive(ticket_id=..., timeout=None)`
- Raw payload: `client.tickets.mark_ticket_sensitive.raw(ticket_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/mark-sensitive`
- Source controller: `IncidentIQ API`

Mark ticket as sensitive

Marks a ticket as containing sensitive information. Sensitive tickets have restricted visibility and may be hidden from certain users or reports to protect privacy. Use this for tickets involving HR issues, security incidents, or personal data.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to find the ticket and extract `Items[].TicketId`.

**Workflow Example**
1. Find ticket: [POST /api/v1.0/tickets](#/Tickets/searchTickets) → extract `TicketId`
2. Mark sensitive: [POST /api/v1.0/tickets/{ticketId}/mark-sensitive](#/Tickets/markTicketSensitive)
3. Verify: [GET /api/v1.0/tickets/{ticketId}](#/Tickets/getTicket) to confirm `HasSensitiveInformation: true`

**Visibility Impact**: Once marked, the ticket may be hidden from general searches, reports, and users without elevated permissions. Only designated staff can view sensitive tickets.

**Use Cases**: HIPAA-related issues, employee complaints, security breaches, confidential investigations, personal data requests.

**Related Endpoints**
- [POST /api/v1.0/tickets/{ticketId}/mark-not-sensitive](#/Tickets/markTicketNotSensitive) – Remove sensitive flag
- [GET /api/v1.0/tickets/{ticketId}](#/Tickets/getTicket) – Check sensitive status

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | Unique identifier of the ticket |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `mark_ticket_urgent`

Provenance: Golden OpenAPI contract

Operation ID: `markTicketUrgent`

- Sync: `client.tickets.mark_ticket_urgent(ticket_id=..., timeout=None)`
- Async: `await client.tickets.mark_ticket_urgent(ticket_id=..., timeout=None)`
- Raw payload: `client.tickets.mark_ticket_urgent.raw(ticket_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/mark-urgent`
- Source controller: `IncidentIQ API`

Mark ticket as urgent

Marks a ticket as urgent, flagging it for immediate attention. Urgent tickets appear highlighted in agent queues and may trigger escalation workflows or priority notifications to supervisors.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to find the ticket and extract `Items[].TicketId`.

**Workflow Example**
1. Find ticket: [POST /api/v1.0/tickets](#/Tickets/searchTickets) → extract `TicketId`
2. Mark urgent: [POST /api/v1.0/tickets/{ticketId}/mark-urgent](#/Tickets/markTicketUrgent)
3. Verify: [GET /api/v1.0/tickets/{ticketId}](#/Tickets/getTicket) to confirm `IsUrgent: true`
4. Later: Use [POST /api/v1.0/tickets/{ticketId}/mark-not-urgent](#/Tickets/markTicketNotUrgent) when resolved

**Queue Impact**: Urgent tickets typically sort to the top of agent queues and may have different SLA timers applied.

**Use Cases**: VIP user issues, system outages, time-sensitive requests, executive escalations, safety concerns.

**Related Endpoints**
- [POST /api/v1.0/tickets/{ticketId}/mark-not-urgent](#/Tickets/markTicketNotUrgent) – Remove urgent flag
- [GET /api/v1.0/tickets/{ticketId}](#/Tickets/getTicket) – Check urgent status
- [POST /api/v1.0/tickets](#/Tickets/searchTickets) – Filter by `IsUrgent`

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | Unique identifier of the ticket |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `process_ticket_approval`

Provenance: Golden OpenAPI contract

Operation ID: `processTicketApproval`

- Sync: `client.tickets.process_ticket_approval(ticket_id=..., body=..., timeout=None)`
- Async: `await client.tickets.process_ticket_approval(ticket_id=..., body=..., timeout=None)`
- Raw payload: `client.tickets.process_ticket_approval.raw(ticket_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/workflow/approval/response`
- Source controller: `IncidentIQ API`

Respond to approval request

Submits an approval decision (approve or reject) for a ticket that is awaiting workflow approval. This endpoint is used by designated approvers to advance tickets through approval gates in multi-stage workflows, such as budget approvals or change management processes.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) with approval status filter to find tickets awaiting your approval and extract `Items[].TicketId`.
2. The authenticated user must be a designated approver for the ticket's current workflow step.

**Workflow Example**
1. Find pending approvals: [POST /api/v1.0/tickets](#/Tickets/searchTickets) with approval filter → extract `TicketId`
2. Review ticket: [GET /api/v1.0/tickets/{ticketId}](#/Tickets/getTicket) and [GET /api/v1.0/tickets/{ticketId}/approvals](#/Tickets/getTicketApprovals) for context
3. Submit decision: [POST /api/v1.0/tickets/{ticketId}/workflow/approval/response](#/Tickets/processTicketApproval) with approve/reject decision
4. Verify: [GET /api/v1.0/tickets/{ticketId}/status](#/Tickets/getTicketStatus) to confirm workflow advanced

**Request Body**: Provide `IsApproved` (boolean) and optional `Comments` explaining the decision.

**Note**: Rejection may return the ticket to the requester or previous step depending on workflow configuration.

**Related Endpoints**
- [GET /api/v1.0/tickets/{ticketId}/approvals](#/Tickets/getTicketApprovals) – View approval history and status
- [GET /api/v1.0/tickets/{ticketId}/status](#/Tickets/getTicketStatus) – View current workflow status

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | Unique identifier of the ticket |
| `body` | `body` | `body` | `yes` | `TicketApprovalRequest` | `TicketApprovalRequest` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `process_ticket_workflow_approval`

Provenance: Golden OpenAPI contract

Operation ID: `processTicketWorkflowApproval`

- Sync: `client.tickets.process_ticket_workflow_approval(ticket_id=..., workflow_step_id=..., user_id=..., timeout=None)`
- Async: `await client.tickets.process_ticket_workflow_approval(ticket_id=..., workflow_step_id=..., user_id=..., timeout=None)`
- Raw payload: `client.tickets.process_ticket_workflow_approval.raw(ticket_id=..., workflow_step_id=..., user_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/workflow/approval/{workflowStepId}/{userId}`
- Source controller: `IncidentIQ API`

Process workflow approval

Processes an approval action for a ticket workflow step. This endpoint allows approvers to approve or advance a ticket through its workflow.

**Authentication**
- Supports anonymous access for approval link scenarios
- Supports app authorization for automated approvals

**Behavior**
- Validates the user has approval rights for the workflow step
- Advances the ticket to the next workflow state upon approval
- Returns the updated ticket with new status

**Use Cases**
- Processing approvals from email links
- Automated approval workflows via API
- Mobile approval processing

**Prerequisites**
- Ticket must be in the specified workflow step
- User must be an authorized approver for that step

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | UUID of the ticket to approve |
| `workflow_step_id` | `workflowStepId` | `path` | `yes` | `str` | `-` | UUID of the workflow step being approved |
| `user_id` | `userId` | `path` | `yes` | `str` | `-` | UUID of the user performing the approval |

#### Returns

- Typed call return: `TicketSingleResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketSingleResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `remove_ticket_follower_team`

Provenance: Golden OpenAPI contract

Operation ID: `removeTicketFollowerTeam`

- Sync: `client.tickets.remove_ticket_follower_team(ticket_id=..., team_id=..., timeout=None)`
- Async: `await client.tickets.remove_ticket_follower_team(ticket_id=..., team_id=..., timeout=None)`
- Raw payload: `client.tickets.remove_ticket_follower_team.raw(ticket_id=..., team_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/tickets/{ticketId}/followers/team/{teamId}`
- Source controller: `IncidentIQ API`

Remove team as ticket followers

Removes all members of a team from the ticket's follower list. After removal, team members will no longer receive notifications about updates to this ticket unless they're following individually or through another team.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to find the ticket and extract `Items[].TicketId`.
2. **teamId** – Use [GET /api/v1.0/tickets/{ticketId}/teams](#/Tickets/getTicketTeams) or [GET /api/v1.0/teams](#/Teams/listTeams) to identify the team.

**Workflow Example**
1. View current followers: [GET /api/v1.0/tickets/{ticketId}/followers](#/Tickets/getTicketFollowers) → identify team to remove
2. Remove team: [DELETE /api/v1.0/tickets/{ticketId}/followers/team/{teamId}](#/Tickets/removeTicketFollowerTeam)
3. Verify: [GET /api/v1.0/tickets/{ticketId}/followers](#/Tickets/getTicketFollowers) to confirm team members removed

**Use Cases**: Removing stakeholder groups after issue resolution, transferring ticket ownership between teams, reducing unnecessary notifications.

**Note**: This removes team-based following only; individual follows remain intact.

**Related Endpoints**
- [POST /api/v1.0/tickets/{ticketId}/followers/team/{teamId}](#/Tickets/addTicketFollowerTeam) – Add team as followers
- [DELETE /api/v1.0/tickets/{ticketId}/followers/{userId}](#/Tickets/removeTicketFollowerUser) – Remove individual follower
- [GET /api/v1.0/tickets/{ticketId}/followers](#/Tickets/getTicketFollowers) – List current followers

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | Unique identifier of the ticket |
| `team_id` | `teamId` | `path` | `yes` | `str` | `-` | Unique identifier of the team to remove as followers |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `remove_ticket_follower_user`

Provenance: Golden OpenAPI contract

Operation ID: `removeTicketFollowerUser`

- Sync: `client.tickets.remove_ticket_follower_user(ticket_id=..., user_id=..., timeout=None)`
- Async: `await client.tickets.remove_ticket_follower_user(ticket_id=..., user_id=..., timeout=None)`
- Raw payload: `client.tickets.remove_ticket_follower_user.raw(ticket_id=..., user_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/tickets/{ticketId}/followers/user/{userId}`
- Source controller: `IncidentIQ API`

Remove user as ticket follower

Removes a user from the ticket's follower list so they no longer receive notifications about updates. Use this to clean up watchers when a user no longer needs visibility on a ticket.

**Prerequisites**
1. **ticketId** - Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) and extract `Items[].TicketId`.
2. **userId** - Use [GET /api/v1.0/tickets/{ticketId}/followers](#/Tickets/getTicketFollowers) or [POST /api/v1.0/search](#/Users/searchUsers) and extract `Item.Users[].UserId`.

**Workflow Example**
1. Identify the ticket and the follower to remove.
2. [DELETE /api/v1.0/tickets/{ticketId}/followers/user/{userId}](#/Tickets/removeTicketFollowerUser).
3. Verify the follower list using [GET /api/v1.0/tickets/{ticketId}/followers](#/Tickets/getTicketFollowers).

**Minimal Required Fields**: ticketId, userId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | Unique identifier of the ticket |
| `user_id` | `userId` | `path` | `yes` | `str` | `-` | Unique identifier of the user to remove as follower |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `remove_ticket_tag`

Provenance: Golden OpenAPI contract

Operation ID: `removeTicketTag`

- Sync: `client.tickets.remove_ticket_tag(ticket_id=..., tag_id=..., timeout=None)`
- Async: `await client.tickets.remove_ticket_tag(ticket_id=..., tag_id=..., timeout=None)`
- Raw payload: `client.tickets.remove_ticket_tag.raw(ticket_id=..., tag_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/tickets/{ticketId}/tags/{tagId}`
- Source controller: `IncidentIQ API`

Remove tag from ticket

Removes a specific tag from a ticket, updating its categorization. Tags help organize and filter tickets; removing a tag updates search results and any tag-based automation rules.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to locate the ticket and extract `Items[].TicketId`.
2. **tagId** – Use [GET /api/v1.0/tickets/tags](#/Tags/searchTagsByType) to list available tags, or [GET /api/v1.0/tickets/{ticketId}](#/Tickets/getTicket) to see tags currently on the ticket.

**Workflow Example**
1. Find ticket: [POST /api/v1.0/tickets](#/Tickets/searchTickets) → extract `Items[].TicketId`
2. View current tags: [GET /api/v1.0/tickets/{ticketId}](#/Tickets/getTicket) → review `Tags[]` array
3. Remove tag: [DELETE /api/v1.0/tickets/{ticketId}/tags/{tagId}](#/Tickets/removeTicketTag)
4. Verify: [GET /api/v1.0/tickets/{ticketId}](#/Tickets/getTicket) to confirm tag removal

**Related Endpoints**
- [POST /api/v1.0/tickets/{ticketId}/tags/{tagId}](#/Tickets/addTicketTag) – Add a tag
- [POST /api/v1.0/tickets/{ticketId}/tags](#/Tickets/updateTicketTags) – Bulk update all tags

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | Unique identifier of the ticket |
| `tag_id` | `tagId` | `path` | `yes` | `str` | `-` | Unique identifier of the tag to remove |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `resolve_ticket_next_step`

Provenance: Golden OpenAPI contract

Operation ID: `resolveTicketNextStep`

- Sync: `client.tickets.resolve_ticket_next_step(ticket_id=..., ticket_next_step_id=..., timeout=None)`
- Async: `await client.tickets.resolve_ticket_next_step(ticket_id=..., ticket_next_step_id=..., timeout=None)`
- Raw payload: `client.tickets.resolve_ticket_next_step.raw(ticket_id=..., ticket_next_step_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/next-steps/{ticketNextStepId}/resolve`
- Source controller: `IncidentIQ API`

Resolve ticket next step

Marks a workflow recommendation such as "Verify Asset" as complete once the underlying task has been satisfied.

**Prerequisites**
1. **ticketId** – Locate the ticket via [POST /api/v1.0/tickets](#/Tickets/searchTickets) and extract `Items[].TicketId`.
2. **ticketNextStepId** – Call [GET /api/v1.0/tickets/{ticketId}/next-steps](#/Tickets/getTicketNextSteps) and read `Items[].TicketNextStepId` for the recommendation you plan to close.
3. **Asset verification** – When resolving the "Verify Asset" recommendation, first record the device check with [POST /api/v1.0/assets/{assetId}/verifications/new](#/Assets/createAssetVerification).

**Workflow Example**
1. Identify work: [POST /api/v1.0/tickets](#/Tickets/searchTickets) with queue filters → capture `Items[].TicketId`.
2. Load recommendations: [GET /api/v1.0/tickets/{ticketId}/next-steps](#/Tickets/getTicketNextSteps) → select the "Verify Asset" entry and note `TicketNextStepId` plus the related `AssetId`.
3. Confirm the device: [POST /api/v1.0/assets/{assetId}/verifications/new](#/Assets/createAssetVerification) with manual verification details gathered from the modal.
4. Resolve the recommendation: [POST /api/v1.0/tickets/{ticketId}/next-steps/{ticketNextStepId}/resolve](#/Tickets/resolveTicketNextStep) to clear the next step and refresh ticket status.

**Minimal Required Fields**: ticketId (path), ticketNextStepId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | UUID of the ticket whose workflow recommendation is being resolved. Obtain via POST /api/v1.0/tickets and extract `Items[].TicketId`. |
| `ticket_next_step_id` | `ticketNextStepId` | `path` | `yes` | `str` | `-` | UUID of the recommendation to resolve. Obtain via [POST /api/v1.0/tickets/next-steps](#/Tickets/searchTicketNextSteps) or [GET /api/v1.0/tickets/{ticketId}/next-steps](#/Tickets/getTicketNextSteps) and extract `Items[].TicketNextStepId`. |

#### Returns

- Typed call return: `TicketNextStepResolveResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketNextStepResolveResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `save_ticket_due_date_reminders`

Provenance: Golden OpenAPI contract

Operation ID: `saveTicketDueDateReminders`

- Sync: `client.tickets.save_ticket_due_date_reminders(body=..., timeout=None)`
- Async: `await client.tickets.save_ticket_due_date_reminders(body=..., timeout=None)`
- Raw payload: `client.tickets.save_ticket_due_date_reminders.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/due-dates/reminders`
- Source controller: `IncidentIQ API`

Save due date reminders

Creates or updates due date reminders for a ticket. Reminders automatically notify assigned agents, followers, or the requester before or after the due date, helping ensure timely ticket resolution.

**Prerequisites**
1. **TicketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to find the ticket and extract `Items[].TicketId`.
2. **Due Date** – The ticket must have a due date set via [POST /api/v1.0/tickets/{ticketId}/due-dates](#/Tickets/setTicketDueDate).

**Workflow Example**
1. Locate ticket: [POST /api/v1.0/tickets](#/Tickets/searchTickets) → extract `TicketId`
2. Set due date (if not set): [POST /api/v1.0/tickets/{ticketId}/due-dates](#/Tickets/setTicketDueDate)
3. Configure reminders: [POST /api/v1.0/tickets/due-dates/reminders](#/Tickets/saveTicketDueDateReminders) with reminder settings
4. Verify: [GET /api/v1.0/tickets/due-dates/reminders/{ticketId}](#/Tickets/getTicketDueDateReminders) to confirm configuration

**Request Body**: Provide `TicketId`, `ReminderOffsetDays` (negative for before, positive for after due date), and notification recipients.

**Related Endpoints**
- [POST /api/v1.0/tickets/{ticketId}/due-dates](#/Tickets/setTicketDueDate) – Set ticket due date
- [GET /api/v1.0/tickets/due-dates/reminders/{ticketId}](#/Tickets/getTicketDueDateReminders) – View configured reminders
- [POST /api/v1.0/tickets/bulk/set-due-date](#/Tickets/bulkSetTicketDueDate) – Bulk set due dates

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `TicketRemindersRequest` | `TicketRemindersRequest` | - |

#### Returns

- Typed call return: `TicketRemindersUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketRemindersUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `search_ticket_next_steps`

Provenance: Golden OpenAPI contract

Operation ID: `searchTicketNextSteps`

- Sync: `client.tickets.search_ticket_next_steps(p=None, s=None, timeout=None)`
- Async: `await client.tickets.search_ticket_next_steps(p=None, s=None, timeout=None)`
- Raw payload: `client.tickets.search_ticket_next_steps.raw(p=None, s=None, timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/next-steps`
- Source controller: `IncidentIQ API`

Search ticket next steps

Performs a filtered and paginated search across all pending next steps in the system. Use this endpoint to identify bottlenecks or high-priority recommendations across multiple tickets or sites.

**Workflow Example**
1. Monitor workflow: [POST /api/v1.0/tickets/next-steps](#/Tickets/searchTicketNextSteps) with filters for unassigned or overdue steps.
2. Iterate `Items[]` to identify targets for remediation or follow-up.

**Minimal Required Fields**: none (supports optional paging and filters via query parameters)

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index to retrieve |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of records per page |

#### Returns

- Typed call return: `list[Any]`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload
- Pagination helper: `client.tickets.search_ticket_next_steps.iter_pages(start_page=1, page_size=100, max_pages=None, p=None, s=None, timeout=None)`

---

### `search_tickets`

Provenance: Golden OpenAPI contract

Operation ID: `searchTickets`

- Sync: `client.tickets.search_tickets(p=None, s=None, o=None, body=None, timeout=None)`
- Async: `await client.tickets.search_tickets(p=None, s=None, o=None, body=None, timeout=None)`
- Raw payload: `client.tickets.search_tickets.raw(p=None, s=None, o=None, body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/tickets`
- Source controller: `IncidentIQ API`

Search tickets

Searches and filters ticket records based on specified criteria. This endpoint powers the agent portal's ticket queues and supports advanced querying capabilities for IT service requests and incident tracking. It returns a paginated list of matching tickets with their complete details.

**Filter Facet System**

This endpoint uses the universal `FilterMatch` pattern shared across Tickets, Assets, and Users search endpoints. Tickets support **103 filter facets** organized into categories:

- **Assignment**: `agent`, `team`, `unassigned`, `assignedtome`, `assignedtoothers`
- **Status/Workflow**: `status`, `workflow`, `workflowstage`, `workflowstep`, `ticketstate`, `previousstatus`
- **Dates**: `createddate`, `modifieddate`, `closeddate`, `duedate`, `activitydate`, `scheduleddate` (use `DateExpressionSyntax`)
- **Users**: `user`, `for`, `onbehalfof`, `agent` (use UUID in `Id` field)
- **Assets**: `asset`, `assettype`, `assetstatus`, `model`, `modelcategory`
- **SLA**: `sla`, `slaresponsetime`, `slaresolutiontime`
- **Custom Fields**: `ticketcustomfield`, `ticketattribute`

See the `TicketSearchFilter` schema for the complete `x-facet-definitions` reference documenting all 103 facets with their required fields.

**RequestOptions overview**
- `TicketSearchRequest` mirrors the RequestOptions payload captured in the agent portal. Include `ProductId`, `Schema` (saved view such as `OpenWithModify` or `All`), `FilterByProduct`, `ShowChildTickets`, and `OnlyShowDeleted` as needed.
- Populate `Filters[]` with facet entries. Each entry must declare a `Facet` key plus either an `Id` (for entity-based facets such as status, workflow, prioritylevel, tag, user, agent) or a `Value` expression (for keyword/date comparisons). Optional fields such as `Negative`, `Selected`, and `GroupIndex` control exclusion logic and UI grouping.
- Call [GET /api/v1.0/filters/for/entitytype/{entityTypeId}](#/Filters/listFiltersForEntityType) with entity type `888891ac-91aa-e711-80c2-100dffa00001` to enumerate additional ticket filter keys before constructing the payload.

**Filter Expression Syntax**
- **Date facets**: Use `DateExpressionSyntax` - supports comparison operators (`date>=MM/DD/YYYY`, `date<=MM/DD/YYYY`), explicit ranges (`daterange:MM/DD/YYYY-MM/DD/YYYY`), and relative ranges (`range:today`, `range:thisweek`, `range:lastdays:30`, `range:nextweek`).
- **Numeric facets**: Use `NumericExpressionSyntax` - format is `numoperator:<operator>:<value>` where operator is `equals`, `lessthan`, `lessthanequal`, `greaterthan`, or `greaterthanequal`.
- **Keyword/text**: Simple `Value` field (e.g., `"Value": "charging cart"`).
- **Entity references**: Use `Id` field with UUID (status, workflow, priority, tag, user, agent, asset).

**Filters and operators**
- Status/workflow filters require workflow step IDs; retrieve them via [GET /api/v1.0/workflows/allproducts/site/{siteId}](#/Workflows/listWorkflows).
- Priority filters use `Facet: "prioritylevel"` with IDs from [GET /api/v1.0/tickets/priorities](#/Tickets/listTicketPriorityLevels). Tag filters use IDs from [GET /api/v1.0/tags/query](#/Tags/getTagsByQuery). Custom field facets reuse the `CustomFieldId` as the `Id`.
- Set `Negative: true` to exclude specific statuses (for example, remove `Resolved` and `Canceled` while keeping all other results) as demonstrated in the integration guide.

**Pagination and Sorting**

Use query string parameters to control pagination and sorting:

| Parameter | Description | Example |
|-----------|-------------|---------|
| `$p` | Zero-based page index | `$p=0` |
| `$s` | Page size (default 20, max 100) | `$s=25` |
| `$o` | Sort expression: field name followed by direction | `$o=TicketCreatedDate desc` |

**Sort Expression Syntax**: The `$o` parameter accepts a field name followed by an optional direction, separated by a space:
```
$o=FieldName direction
```

**Examples:**
```
POST /api/v1.0/tickets?$p=0&$s=25&$o=TicketCreatedDate desc    (newest first)
POST /api/v1.0/tickets?$p=0&$s=25&$o=TicketNumber asc          (lowest ticket numbers first)
POST /api/v1.0/tickets?$p=0&$s=25&$o=TicketModifiedDate desc   (recently modified first)
```

**Direction values**: `asc`, `ascending`, `desc`, or `descending` (default is ascending if omitted).

**Available Sort Fields**:
- **Dates**: `TicketCreatedDate`, `TicketModifiedDate`, `TicketClosedDate`, `TicketDueDate`
- **Ticket Properties**: `TicketId`, `TicketNumber`, `TicketNumberSort`, `TicketSubject`, `TicketPriority`, `TicketStatusName`
- **Assignment**: `AssignedUserFirstName`, `AssignedTeamName`, `WorkflowStepName`
- **Requester**: `ForFirstName`, `ForName`, `ForLocationName`
- **Location**: `LocationName`, `LocationRoomName`
- **Other**: `IssueCategoryId`, `IssueTypeId`, `IsClosed`, `OverallSurveyRating`, `SiteId`

The response `Paging` object echoes `PageIndex`, `PageSize`, `PageCount`, and `TotalRows` to help you issue subsequent requests.

**Performance considerations**
- Begin every search with a narrow combination of filters (status + workflow + keyword) to avoid scanning the district-wide ticket corpus.
- Cache supporting metadata (statuses, workflow steps, priorities, tags, custom field IDs) rather than issuing lookups per request.
- Disable `ShowChildTickets` unless you specifically need subtickets; excluding them reduces response size.
- Iterate with moderate page sizes (25–50) instead of requesting very large batches, which can lead to longer response times or gateway throttling. Use the `ItemCount`/`Paging` data to detect when you've reached the end.

**Related endpoints**
- [GET /api/v1.0/tickets/priorities](#/Tickets/listTicketPriorityLevels) – resolve numeric priority values to display labels before filtering by `prioritylevel`.
- [GET /api/v1.0/tags/query](#/Tags/getTagsByQuery) – retrieve tag IDs used by the `tag` facet.
- [GET /api/v1.0/workflows/allproducts/site/{siteId}](#/Workflows/listWorkflows) – enumerate workflow steps and status IDs for `status`/`workflow` filters.

**Common Use Case**: Search operations are often used to find IDs needed for other API calls. Extract the relevant ID from the response `Items[]` array before chaining additional workflows (for example, start/assign/copy ticket actions).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index to retrieve |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of records per page |
| `o` | `$o` | `query` | `no` | `Any` | `-` | Sort expression: field name followed by optional direction (e.g., `TicketCreatedDate desc`). Direction can be `asc`, `ascending`, `desc`, or `descending`. Default direction is ascending. See [TicketSortField](#/components/schemas/TicketSortField) for valid field names. |
| `body` | `body` | `body` | `no` | `TicketSearchRequest` | `TicketSearchRequest` | Optional TicketSearchRequest payload (also known as the RequestOptions object) that mirrors the agent portal search dialog. Provide at least one `Filters[]` entry to narrow the result set; omit the body to reuse the caller's default queue. |

#### Returns

- Typed call return: `TicketSearchResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketSearchResponse`
- Pagination helper: `client.tickets.search_tickets.iter_pages(start_page=1, page_size=100, max_pages=None, p=None, s=None, o=None, body=None, timeout=None)`

---

### `send_ticket_activity_notification`

Provenance: Golden OpenAPI contract

Operation ID: `sendTicketActivityNotification`

- Sync: `client.tickets.send_ticket_activity_notification(ticket_id=..., activity_id=..., timeout=None)`
- Async: `await client.tickets.send_ticket_activity_notification(ticket_id=..., activity_id=..., timeout=None)`
- Raw payload: `client.tickets.send_ticket_activity_notification.raw(ticket_id=..., activity_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/activities/{activityId}/send-notification`
- Source controller: `IncidentIQ API`

Resend activity notification

Triggers or re-triggers an email notification for a specific ticket activity. Use this to resend notifications that may not have been delivered, or to send notifications for activities that were originally created with notifications suppressed.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to find the ticket and extract `Items[].TicketId`.
2. **activityId** – Use [GET /api/v1.0/tickets/{ticketId}/timeline](#/Tickets/getTicketTimeline) to find the activity and extract `TicketActivityId`.

**Workflow Example**
1. View timeline: [GET /api/v1.0/tickets/{ticketId}/timeline](#/Tickets/getTicketTimeline) → identify activity needing notification
2. Extract IDs: Note `TicketId` and `TicketActivityId`
3. Send notification: [POST /api/v1.0/tickets/{ticketId}/activities/{activityId}/send-notification](#/Tickets/sendTicketActivityNotification)
4. Verify: Check recipient email or notification logs

**Use Cases**: Resending failed notifications, notifying users added after initial activity, sending reminders about important updates.

**Related Endpoints**
- [GET /api/v1.0/tickets/{ticketId}/timeline](#/Tickets/getTicketTimeline) – View activity history
- [POST /api/v1.0/tickets/{ticketId}/activities/new-batch](#/Tickets/createTicketActivityBatch) – Create activities with notification control
- [GET /api/v1.0/tickets/activities/{ticketActivityId}](#/Tickets/getTicketActivityById) – View activity details

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | UUID of the ticket. |
| `activity_id` | `activityId` | `path` | `yes` | `str` | `-` | UUID of the activity. |

#### Returns

- Typed call return: `Any`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `send_ticket_for_approval`

Provenance: Golden OpenAPI contract

Operation ID: `sendTicketForApproval`

- Sync: `client.tickets.send_ticket_for_approval(ticket_id=..., body=..., timeout=None)`
- Async: `await client.tickets.send_ticket_for_approval(ticket_id=..., body=..., timeout=None)`
- Raw payload: `client.tickets.send_ticket_for_approval.raw(ticket_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/workflow/approval`
- Source controller: `IncidentIQ API`

Send ticket for approval

Submits a ticket into an approval workflow, transitioning it to an awaiting-approval status. Designated approvers will be notified via email and in-app notifications and can approve or reject the request.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to find the ticket and extract `Items[].TicketId`.
2. **ApproverUserIds** (optional) – Use [POST /api/v1.0/search](#/Search/globalSearch) to find approvers, or let workflow rules determine approvers.

**Workflow Example**
1. Complete ticket work: Ensure ticket is ready for approval review
2. Find ticket: [POST /api/v1.0/tickets](#/Tickets/searchTickets) → extract `TicketId`
3. Submit for approval: [POST /api/v1.0/tickets/{ticketId}/workflow/approval](#/Tickets/sendTicketForApproval) with optional approver list
4. Monitor: [GET /api/v1.0/tickets/{ticketId}/approvals](#/Tickets/getTicketApprovals) to track approval status
5. On decision: Ticket advances or returns based on approve/reject outcome

**Use Cases**: Budget approvals, change management requests, equipment purchases, policy exceptions, HR actions requiring management sign-off.

**Request Body**: Optionally specify `ApproverUserIds` array; if omitted, workflow rules determine approvers.

**Related Endpoints**
- [GET /api/v1.0/tickets/{ticketId}/approvals](#/Tickets/getTicketApprovals) – View approval status
- [POST /api/v1.0/tickets/{ticketId}/workflow/approval/response](#/Tickets/processTicketApproval) – Approve or reject

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | Unique identifier of the ticket |
| `body` | `body` | `body` | `yes` | `SendTicketForApprovalRequest` | `SendTicketForApprovalRequest` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `set_ticket_due_date`

Provenance: Golden OpenAPI contract

Operation ID: `setTicketDueDate`

- Sync: `client.tickets.set_ticket_due_date(ticket_id=..., body=..., timeout=None)`
- Async: `await client.tickets.set_ticket_due_date(ticket_id=..., body=..., timeout=None)`
- Raw payload: `client.tickets.set_ticket_due_date.raw(ticket_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/due-dates`
- Source controller: `IncidentIQ API`

Set ticket due date

Sets or updates the due date for a specific ticket. Due dates establish completion targets, drive SLA compliance tracking, and trigger automated reminder notifications to help ensure timely ticket resolution.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to find the ticket and extract `Items[].TicketId`.

**Workflow Example**
1. Locate ticket: [POST /api/v1.0/tickets](#/Tickets/searchTickets) with search criteria → extract `TicketId`
2. Calculate due date: Determine appropriate deadline based on SLA or priority
3. Set due date: [POST /api/v1.0/tickets/{ticketId}/due-dates](#/Tickets/setTicketDueDate) with date
4. Configure reminders: [POST /api/v1.0/tickets/due-dates/reminders](#/Tickets/saveTicketDueDateReminders) to set notifications
5. Verify: [GET /api/v1.0/tickets/{ticketId}](#/Tickets/getTicket) to confirm due date is set

**Request Body**: Provide `DueDate` in ISO 8601 format and optional reminder settings.

**Note**: Setting a due date may trigger workflow rules or automatic priority escalation based on site configuration.

**Related Endpoints**
- [POST /api/v1.0/tickets/due-dates/reminders](#/Tickets/saveTicketDueDateReminders) – Configure due date reminders
- [GET /api/v1.0/tickets/due-dates/reminders/{ticketId}](#/Tickets/getTicketDueDateReminders) – View current reminders
- [POST /api/v1.0/tickets/bulk/set-due-date](#/Tickets/bulkSetTicketDueDate) – Set due dates for multiple tickets

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | Unique identifier of the ticket |
| `body` | `body` | `body` | `yes` | `DueDatePackage` | `DueDatePackage` | - |

#### Returns

- Typed call return: `TicketUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `set_ticket_next_step_resolvable`

Provenance: Golden OpenAPI contract

Operation ID: `setTicketNextStepResolvable`

- Sync: `client.tickets.set_ticket_next_step_resolvable(ticket_id=..., ticket_next_step_id=..., user_resolvable=..., timeout=None)`
- Async: `await client.tickets.set_ticket_next_step_resolvable(ticket_id=..., ticket_next_step_id=..., user_resolvable=..., timeout=None)`
- Raw payload: `client.tickets.set_ticket_next_step_resolvable.raw(ticket_id=..., ticket_next_step_id=..., user_resolvable=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/next-steps/{ticketNextStepId}/resolvable/{userResolvable}`
- Source controller: `IncidentIQ API`

Set next step as user resolvable

Toggles whether a specific next step can be marked complete by the ticket requester (non-agent user) rather than requiring agent completion. User-resolvable steps enable self-service workflows where end users can confirm they've completed recommended actions.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to find the ticket and extract `Items[].TicketId`.
2. **ticketNextStepId** – Use [GET /api/v1.0/tickets/{ticketId}/next-steps](#/Tickets/getTicketNextSteps) to list steps and extract `TicketNextStepId`.

**Workflow Example**
1. List steps: [GET /api/v1.0/tickets/{ticketId}/next-steps](#/Tickets/getTicketNextSteps) → identify step to configure
2. Set resolvable: [POST /api/v1.0/tickets/{ticketId}/next-steps/{ticketNextStepId}/resolvable/{userResolvable}](#/Tickets/setTicketNextStepResolvable) with `userResolvable=true`
3. Requester can now mark the step complete via the user portal
4. To disable: POST .../resolvable/false

**Path Parameters**: `userResolvable` is a boolean (true/false) indicating the desired setting.

**Use Cases**: Self-service troubleshooting steps, user confirmation of instructions followed, delegating simple tasks to requesters.

**Related Endpoints**
- [GET /api/v1.0/tickets/{ticketId}/next-steps](#/Tickets/getTicketNextSteps) – List next steps
- [POST /api/v1.0/tickets/{ticketId}/next-steps/{nextStepId}](#/Tickets/updateTicketNextStep) – Update step details

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | UUID of the ticket. |
| `ticket_next_step_id` | `ticketNextStepId` | `path` | `yes` | `str` | `-` | UUID of the next step recommendation. |
| `user_resolvable` | `userResolvable` | `path` | `yes` | `bool` | `-` | Boolean flag indicating if the step is user resolvable. |

#### Returns

- Typed call return: `Any`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `set_ticket_owner_and_for`

Provenance: Golden OpenAPI contract

Operation ID: `setTicketOwnerAndFor`

- Sync: `client.tickets.set_ticket_owner_and_for(ticket_id=..., owner_user_id=..., for_user_id=..., timeout=None)`
- Async: `await client.tickets.set_ticket_owner_and_for(ticket_id=..., owner_user_id=..., for_user_id=..., timeout=None)`
- Raw payload: `client.tickets.set_ticket_owner_and_for.raw(ticket_id=..., owner_user_id=..., for_user_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/owner/{ownerUserId}/for/{forUserId}`
- Source controller: `IncidentIQ API`

Set ticket owner and requester

Updates both the internal owner and the end-user requester associated with a ticket in a single operation.

**Prerequisites**
1. **ticketId** – Locate via [POST /api/v1.0/tickets](#/Tickets/searchTickets).
2. **ownerUserId** – Technican identifier.
3. **forUserId** – End-user requester identifier.

**Minimal Required Fields**: ticketId, ownerUserId, forUserId

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | UUID of the ticket. |
| `owner_user_id` | `ownerUserId` | `path` | `yes` | `str` | `-` | UUID of the user who will own the ticket. Obtain via [POST /api/v1.0/users](#/Users/searchUsers), extract `Items[].UserId`. |
| `for_user_id` | `forUserId` | `path` | `yes` | `str` | `-` | UUID of the requester (end user) for the ticket. Obtain via [POST /api/v1.0/users](#/Users/searchUsers), extract `Items[].UserId`. |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `set_ticket_priority`

Provenance: Golden OpenAPI contract

Operation ID: `setTicketPriority`

- Sync: `client.tickets.set_ticket_priority(ticket_id=..., body=..., timeout=None)`
- Async: `await client.tickets.set_ticket_priority(ticket_id=..., body=..., timeout=None)`
- Raw payload: `client.tickets.set_ticket_priority.raw(ticket_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/priority`
- Source controller: `IncidentIQ API`

Set ticket priority

Updates the priority level for a ticket. Use this endpoint for automated triage workflows or to escalate/de-escalate tickets programmatically.

**Prerequisites**
- Obtain available priority levels from [GET /api/v1.0/tickets/priorities](#/Tickets/listTicketPriorityLevels)
- Extract the `PriorityLevelId` for the desired priority level

**Workflow Example**
1. List priorities: [GET /api/v1.0/tickets/priorities](#/Tickets/listTicketPriorityLevels) → select desired `PriorityLevelId`
2. Update ticket: [POST /api/v1.0/tickets/{ticketId}/priority](#/Tickets/setTicketPriority) with the selected priority

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | Unique identifier of the ticket to update |
| `body` | `body` | `body` | `yes` | `SetTicketPriorityRequest` | `SetTicketPriorityRequest` | Priority update request containing the new priority level identifier |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `set_ticket_requestor_responded`

Provenance: Golden OpenAPI contract

Operation ID: `setTicketRequestorResponded`

- Sync: `client.tickets.set_ticket_requestor_responded(ticket_id=..., timeout=None)`
- Async: `await client.tickets.set_ticket_requestor_responded(ticket_id=..., timeout=None)`
- Raw payload: `client.tickets.set_ticket_requestor_responded.raw(ticket_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/status/requestor-responded`
- Source controller: `IncidentIQ API`

Mark requestor has responded

Changes the ticket status to indicate the requestor has responded. This is typically used after a ticket was in 'waiting on requestor' status and the customer has provided the requested information.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) with waiting status filter to find tickets and extract `Items[].TicketId`.

**Workflow Example**
1. Find waiting tickets: [POST /api/v1.0/tickets](#/Tickets/searchTickets) with 'waiting on requestor' status filter → extract `TicketId`
2. Review response: Check ticket activities via [GET /api/v1.0/tickets/{ticketId}/activities](#/Tickets/getTicketActivities)
3. Mark responded: [POST /api/v1.0/tickets/{ticketId}/status/requestor-responded](#/Tickets/setTicketRequestorResponded)
4. Continue work: Ticket returns to agent queue for action

**Use Cases**: Customer replied to email, customer provided files or information, automated integration detected response, phone call logged from customer.

**Note**: This endpoint is a workflow shortcut. For full status control, use [POST /api/v1.0/tickets/{ticketId}/status/{statusId}](#/Tickets/setTicketStatus).

**Related Endpoints**
- [POST /api/v1.0/tickets/{ticketId}/status/waiting-on-requestor](#/Tickets/setTicketWaitingOnRequestor) – Set to waiting
- [GET /api/v1.0/tickets/{ticketId}/status](#/Tickets/getTicketStatus) – Check current status

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | Unique identifier of the ticket |

#### Returns

- Typed call return: `TicketSingleResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketSingleResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `set_ticket_status`

Provenance: Golden OpenAPI contract

Operation ID: `setTicketStatus`

- Sync: `client.tickets.set_ticket_status(ticket_id=..., status_id=..., timeout=None)`
- Async: `await client.tickets.set_ticket_status(ticket_id=..., status_id=..., timeout=None)`
- Raw payload: `client.tickets.set_ticket_status.raw(ticket_id=..., status_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/status/{statusId}`
- Source controller: `IncidentIQ API`

Update ticket status

Transitions a single ticket to a new workflow status.

**Prerequisites**
1. **ticketId** – Locate the ticket via [POST /api/v1.0/tickets](#/Tickets/searchTickets) and extract `Items[].TicketId`.
2. **statusId** – Retrieve valid workflow steps via [GET /api/v1.0/tickets/{ticketId}/status](#/Tickets/getTicketStatus) (preferred) or [GET /api/v1.0/workflows/steps](#/Workflows/getWorkflowSteps). Use the `WorkflowStepId` returned by those endpoints.

**Workflow Example**
1. Find target ticket: [POST /api/v1.0/tickets](#/Tickets/searchTickets) with filters → collect `Items[].TicketId`.
2. Inspect status options: [GET /api/v1.0/tickets/{ticketId}/status](#/Tickets/getTicketStatus) to read `Item.CurrentWorkflowStep.WorkflowStepId` and confirm approvals are satisfied.
3. Transition status: [POST /api/v1.0/tickets/{ticketId}/status/{statusId}](#/Tickets/setTicketStatus) with the chosen workflow step to advance the ticket and trigger automation. The response returns the refreshed ticket envelope.

**Minimal Required Fields**: ticketId, statusId

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | UUID of the ticket whose status should be updated. Obtain via POST /api/v1.0/tickets and extract `Items[].TicketId`. |
| `status_id` | `statusId` | `path` | `yes` | `str` | `-` | UUID of the workflow status (workflow step) to apply. Equivalent to the `WorkflowStepId` returned by [GET /api/v1.0/workflows/steps](#/Workflows/getWorkflowSteps); alternatively read `Item.WorkflowStep.WorkflowStepId` from [GET /api/v1.0/tickets/{ticketId}](#/Tickets/getTicket). |

#### Returns

- Typed call return: `TicketSingleResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketSingleResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `set_ticket_waiting_on_requestor`

Provenance: Golden OpenAPI contract

Operation ID: `setTicketWaitingOnRequestor`

- Sync: `client.tickets.set_ticket_waiting_on_requestor(ticket_id=..., timeout=None)`
- Async: `await client.tickets.set_ticket_waiting_on_requestor(ticket_id=..., timeout=None)`
- Raw payload: `client.tickets.set_ticket_waiting_on_requestor.raw(ticket_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/status/waiting-on-requestor`
- Source controller: `IncidentIQ API`

Set ticket to waiting on requestor

Changes the ticket status to indicate the agent is waiting for a response from the requestor. This workflow shortcut puts the ticket in a holding state until the customer responds with requested information.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to find the ticket and extract `Items[].TicketId`.

**Workflow Example**
1. Work ticket: Agent reviews ticket and determines more info is needed
2. Contact customer: Send email or call requesting information
3. Mark waiting: [POST /api/v1.0/tickets/{ticketId}/status/waiting-on-requestor](#/Tickets/setTicketWaitingOnRequestor)
4. When response arrives: [POST /api/v1.0/tickets/{ticketId}/status/requestor-responded](#/Tickets/setTicketRequestorResponded)

**SLA Impact**: Waiting-on-requestor status may pause SLA timers since the delay is outside the agent's control.

**Use Cases**: Requesting clarification from customer, awaiting screenshots or error logs, waiting for access credentials, pending approval from requestor.

**Note**: This endpoint is a workflow shortcut. For full status control, use [POST /api/v1.0/tickets/{ticketId}/status/{statusId}](#/Tickets/setTicketStatus).

**Related Endpoints**
- [POST /api/v1.0/tickets/{ticketId}/status/requestor-responded](#/Tickets/setTicketRequestorResponded) – When customer responds
- [GET /api/v1.0/tickets/{ticketId}/status](#/Tickets/getTicketStatus) – Check current status

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | Unique identifier of the ticket |

#### Returns

- Typed call return: `TicketSingleResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketSingleResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `start_ticket`

Provenance: Golden OpenAPI contract

Operation ID: `startTicket`

- Sync: `client.tickets.start_ticket(ticket_id=..., body=..., timeout=None)`
- Async: `await client.tickets.start_ticket(ticket_id=..., body=..., timeout=None)`
- Raw payload: `client.tickets.start_ticket.raw(ticket_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/start`
- Source controller: `IncidentIQ API`

Start ticket work

Marks a ticket as in progress and assigns the acting technician so timers, workflow rules, and activity streams update.

**Prerequisites**
1. **ticketId** – Locate the ticket via [POST /api/v1.0/tickets](#/Tickets/searchTickets) and extract `Items[].TicketId`.
2. **Issue confirmation** – Call [POST /api/v1.0/tickets/{ticketId}/confirm-issue](#/Tickets/confirmTicketIssue) to acknowledge the selected issue before starting work.
3. **UserId** – Determine the technician beginning work (typically the current agent) via [POST /api/v1.0/search](#/Users/searchUsers) or from the ticket metadata.

**Workflow Example**
1. Confirm the ticket issue with [POST /api/v1.0/tickets/{ticketId}/confirm-issue](#/Tickets/confirmTicketIssue).
2. Start the ticket by POSTing to /api/v1.0/tickets/{ticketId}/start with the acting technician's `UserId`.
3. Refresh ticket data via [GET /api/v1.0/tickets/{ticketId}](#/Tickets/getTicket), [POST /api/v1.0/tickets/{ticketId}/timeline](#/Tickets/listTicketTimeline), and [GET /api/v1.0/tickets/{ticketId}/next-steps](#/Tickets/getTicketNextSteps) to update the UI.

**Minimal Required Fields**: ticketId (path), UserId (body).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | UUID of the ticket to start. Obtain via POST /api/v1.0/tickets and extract `Items[].TicketId`. |
| `body` | `body` | `body` | `yes` | `TicketStartRequest` | `TicketStartRequest` | - |

#### Returns

- Typed call return: `TicketWorkflowTransitionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketWorkflowTransitionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `unassign_ticket_from_related`

Provenance: Golden OpenAPI contract

Operation ID: `unassignTicketFromRelated`

- Sync: `client.tickets.unassign_ticket_from_related(ticket_id=..., related_ticket_id=..., timeout=None)`
- Async: `await client.tickets.unassign_ticket_from_related(ticket_id=..., related_ticket_id=..., timeout=None)`
- Raw payload: `client.tickets.unassign_ticket_from_related.raw(ticket_id=..., related_ticket_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/unassign/related/{relatedTicketId}`
- Source controller: `IncidentIQ API`

Unassign ticket from related ticket

Removes the relationship between two related tickets. This unlinks a ticket from another ticket it was previously associated with.

**Behavior**
- Removes the bidirectional relationship between tickets
- Both tickets remain in the system, just unlinked
- Activity is recorded on both tickets

**Use Cases**
- Removing incorrect ticket relationships
- Unlinking tickets that are no longer related
- Cleaning up ticket associations

**Related Endpoints**
- Use ticket search to find related ticket IDs

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | UUID of the primary ticket |
| `related_ticket_id` | `relatedTicketId` | `path` | `yes` | `str` | `-` | UUID of the related ticket to unlink. Obtain via [POST /api/v1.0/tickets](#/Tickets/searchTickets), extract `Items[].TicketId` from response. |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `unassign_ticket_from_team`

Provenance: Golden OpenAPI contract

Operation ID: `unassignTicketFromTeam`

- Sync: `client.tickets.unassign_ticket_from_team(ticket_id=..., timeout=None)`
- Async: `await client.tickets.unassign_ticket_from_team(ticket_id=..., timeout=None)`
- Raw payload: `client.tickets.unassign_ticket_from_team.raw(ticket_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/unassign/team`
- Source controller: `IncidentIQ API`

Unassign ticket from team

Removes the current team assignment from a ticket. Use this to change team routing or return the ticket to an unassigned state.

**Workflow Example**
1. Unassign from team: [POST /api/v1.0/tickets/{ticketId}/unassign/team](#/Tickets/unassignTicketFromTeam)
2. Optionally reassign to different team: [POST /api/v1.0/tickets/{ticketId}/assign](#/Tickets/assignTicket) with new team details

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | Unique identifier of the ticket to unassign from team |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `unassign_ticket_from_user`

Provenance: Golden OpenAPI contract

Operation ID: `unassignTicketFromUser`

- Sync: `client.tickets.unassign_ticket_from_user(ticket_id=..., timeout=None)`
- Async: `await client.tickets.unassign_ticket_from_user(ticket_id=..., timeout=None)`
- Raw payload: `client.tickets.unassign_ticket_from_user.raw(ticket_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/unassign/user`
- Source controller: `IncidentIQ API`

Unassign ticket from user

Removes the current user assignment from a ticket. Use this before reassigning to a different user or to return the ticket to an unassigned state.

**Workflow Example**
1. Unassign current user: [POST /api/v1.0/tickets/{ticketId}/unassign/user](#/Tickets/unassignTicketFromUser)
2. Optionally reassign: [POST /api/v1.0/tickets/{ticketId}/assign](#/Tickets/assignTicket) with new assignment details

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | Unique identifier of the ticket to unassign |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `unassign_ticket_sla`

Provenance: Golden OpenAPI contract

Operation ID: `unassignTicketSla`

- Sync: `client.tickets.unassign_ticket_sla(ticket_id=..., timeout=None)`
- Async: `await client.tickets.unassign_ticket_sla(ticket_id=..., timeout=None)`
- Raw payload: `client.tickets.unassign_ticket_sla.raw(ticket_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/unassign-sla`
- Source controller: `IncidentIQ API`

Unassign SLA from ticket

Removes the service level agreement (SLA) assignment from a ticket. After this operation, the ticket will no longer be tracked against SLA response and resolution time requirements.

**Behavior**
- Clears the SLA assignment from the ticket
- SLA metrics and timers are stopped
- Does not delete SLA history or past violations

**Use Cases**
- Removing SLA when ticket scope changes
- Clearing incorrectly assigned SLAs
- Exempting specific tickets from SLA tracking

**Related Endpoints**
- [POST /api/v1.0/tickets/{ticketId}/sla](#/Tickets/bulkAssignTicketSla) – Assign an SLA
- [GET /api/v1.0/tickets/{ticketId}/sla](#/Tickets/getTicketSla) – Get current SLA

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | UUID of the ticket to remove SLA from |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `unconfirm_ticket_issue`

Provenance: Golden OpenAPI contract

Operation ID: `unconfirmTicketIssue`

- Sync: `client.tickets.unconfirm_ticket_issue(ticket_id=..., timeout=None)`
- Async: `await client.tickets.unconfirm_ticket_issue(ticket_id=..., timeout=None)`
- Raw payload: `client.tickets.unconfirm_ticket_issue.raw(ticket_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/unconfirm-issue`
- Source controller: `IncidentIQ API`

Unconfirm ticket issue

Marks the ticket issue as unconfirmed. This reverses a previous issue confirmation and indicates that the reported issue needs further verification.

**Behavior**
- Sets the `IsIssueConfirmed` flag to false
- Records the action in ticket activity history
- Does not change ticket status or assignment

**Use Cases**
- Reversing an accidental issue confirmation
- Indicating need for additional troubleshooting
- Resetting issue status when new information becomes available

**Related Endpoints**
- [POST /api/v1.0/tickets/{ticketId}/confirm-issue](#/Tickets/confirmTicketIssue) – Confirm the issue

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | UUID of the ticket to unconfirm |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `undelete_ticket`

Provenance: Golden OpenAPI contract

Operation ID: `undeleteTicket`

- Sync: `client.tickets.undelete_ticket(ticket_id=..., timeout=None)`
- Async: `await client.tickets.undelete_ticket(ticket_id=..., timeout=None)`
- Raw payload: `client.tickets.undelete_ticket.raw(ticket_id=..., timeout=None)`
- HTTP route: `PUT /api/v1.0/tickets/{ticketId}/undelete`
- Source controller: `IncidentIQ API`

Restore deleted ticket

Restores a soft-deleted ticket by setting its `IsDeleted` flag to false. The ticket will appear in normal search results again after restoration.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) with `OnlyShowDeleted: true` filter to find deleted tickets and extract `Items[].TicketId`.

**Workflow Example**
1. Search deleted tickets: [POST /api/v1.0/tickets](#/Tickets/searchTickets) with `OnlyShowDeleted: true` → extract `Items[].TicketId`
2. Restore ticket: [PUT /api/v1.0/tickets/{ticketId}/undelete](#/Tickets/undeleteTicket)

**Note**: This operation requires appropriate permissions. The caller must have rights to restore tickets in the target site.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | UUID of the ticket to restore. Obtain via POST /api/v1.0/tickets with OnlyShowDeleted filter. |

#### Returns

- Typed call return: `TicketUndeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketUndeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `undelete_ticket_activity`

Provenance: Golden OpenAPI contract

Operation ID: `undeleteTicketActivity`

- Sync: `client.tickets.undelete_ticket_activity(ticket_activity_id=..., timeout=None)`
- Async: `await client.tickets.undelete_ticket_activity(ticket_activity_id=..., timeout=None)`
- Raw payload: `client.tickets.undelete_ticket_activity.raw(ticket_activity_id=..., timeout=None)`
- HTTP route: `PUT /api/v1.0/tickets/activities/{ticketActivityId}/undelete`
- Source controller: `IncidentIQ API`

Restore deleted ticket activity

Restores a soft-deleted ticket activity by clearing its `IsDeleted` flag. The activity will appear in the ticket's activity feed again after restoration.

**Prerequisites**
1. **ticketActivityId** – Obtain from the activity feed or audit logs. Deleted activities may need to be queried with special filters.

**Workflow Example**
1. Identify the deleted activity's ID from logs or admin tools.
2. Call [PUT /api/v1.0/tickets/activities/{ticketActivityId}/undelete](#/Tickets/undeleteTicketActivity) to restore it.
3. Verify restoration by fetching the ticket's activities.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_activity_id` | `ticketActivityId` | `path` | `yes` | `str` | `-` | UUID of the ticket activity to restore |

#### Returns

- Typed call return: `TicketActivityItemGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketActivityItemGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_ticket`

Provenance: Golden OpenAPI contract

Operation ID: `updateTicket`

- Sync: `client.tickets.update_ticket(ticket_id=..., api_flags=None, body=..., timeout=None)`
- Async: `await client.tickets.update_ticket(ticket_id=..., api_flags=None, body=..., timeout=None)`
- Raw payload: `client.tickets.update_ticket.raw(ticket_id=..., api_flags=None, body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}`
- Source controller: `IncidentIQ API`

Update ticket

Updates a previously submitted ticket and returns the refreshed record. Use the `Update*` flags to control whether assets, tags, followers, custom fields, or attachments are overwritten; unspecified collections remain unchanged. Automation and notification rules can run asynchronously, so follow up with GET `/api/v1.0/tickets/{ticketId}` if you need the latest state.

**Partial Update Mode**
By default, fields omitted from the request payload may be overwritten with null or default values. To perform a true partial update where only the fields you specify are modified, include the `ApiFlags: OnlySetMappedProperties` header. This ensures existing field values are preserved when not explicitly included in the payload.

**Prerequisites**
1. **ticketId** – Locate the ticket via [POST /api/v1.0/tickets](#/Tickets/searchTickets) or webhook payloads and pass it in the path.
2. **Update scope** – Decide which related collections you want to change (assets, tags, followers, custom fields, attachments) and set the matching `Update*` booleans so the service applies those sections of the payload.

**Workflow Example**
1. Search for the ticket: [POST /api/v1.0/tickets](#/Tickets/searchTickets) with filters → extract `Items[].TicketId`.
2. Build the update payload with the new assignment, asset, and custom field changes; set `UpdateAssets`, `UpdateCustomFields`, and `UpdateTicketFollowers` accordingly.
3. [POST /api/v1.0/tickets/{ticketId}](#/Tickets/updateTicket) (optionally with `ApiFlags: OnlySetMappedProperties` header for partial updates).
4. Refresh UI context via [GET /api/v1.0/tickets/{ticketId}](#/Tickets/getTicket) or [POST /api/v1.0/tickets/{ticketId}/timeline](#/Tickets/listTicketTimeline) to surface rule-driven updates and recent activities.

**Minimal Required Fields**: ticketId (path). Provide only the fields you intend to change; set the appropriate `Update*` flags when modifying collections.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | UUID of the ticket to update. Obtain via POST /api/v1.0/tickets and read `Items[].TicketId` from the search response. |
| `api_flags` | `ApiFlags` | `header` | `no` | `str` | `-` | Optional flag to control update behavior. When set to `OnlySetMappedProperties`, only fields explicitly included in the request payload will be updated; fields omitted from the payload will retain their existing values instead of being overwritten with null or default values. This is useful for partial updates where you want to modify specific fields without affecting others. |
| `body` | `body` | `body` | `yes` | `TicketUpdateRequest` | `TicketUpdateRequest` | Ticket update payload including optional assignment, assets, tags, followers, and custom field changes. Set the related `Update*` flags when modifying collections. |

#### Returns

- Typed call return: `TicketUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_ticket_activity`

Provenance: Golden OpenAPI contract

Operation ID: `updateTicketActivity`

- Sync: `client.tickets.update_ticket_activity(ticket_id=..., ticket_activity_id=..., body=..., timeout=None)`
- Async: `await client.tickets.update_ticket_activity(ticket_id=..., ticket_activity_id=..., body=..., timeout=None)`
- Raw payload: `client.tickets.update_ticket_activity.raw(ticket_id=..., ticket_activity_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/activities/{ticketActivityId}`
- Source controller: `IncidentIQ API`

Update ticket activity

Updates an existing ticket activity, such as editing a comment, correcting information in a note, or modifying activity metadata. Only certain activity types (primarily comments and notes) can be edited; system-generated activities like status changes cannot be modified.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to find the ticket and extract `Items[].TicketId`.
2. **ticketActivityId** – Use [GET /api/v1.0/tickets/{ticketId}/timeline](#/Tickets/getTicketTimeline) to find the activity and extract `TicketActivityId`.

**Workflow Example**
1. View timeline: [GET /api/v1.0/tickets/{ticketId}/timeline](#/Tickets/getTicketTimeline) → identify activity to edit
2. Get details: [GET /api/v1.0/tickets/activities/{ticketActivityId}](#/Tickets/getTicketActivityById)
3. Update: [POST /api/v1.0/tickets/{ticketId}/activities/{ticketActivityId}](#/Tickets/updateTicketActivity) with modified content
4. Verify: [GET /api/v1.0/tickets/{ticketId}/timeline](#/Tickets/getTicketTimeline) to confirm changes

**Request Body**: Provide updated activity data including `Body` (content), `IsPrivate` (visibility), and other editable fields.

**Note**: Editing an activity preserves the original creation timestamp but may record an edit history for audit purposes.

**Related Endpoints**
- [GET /api/v1.0/tickets/activities/{ticketActivityId}](#/Tickets/getTicketActivityById) – View activity details
- [DELETE /api/v1.0/tickets/activities/{ticketActivityId}](#/Tickets/deleteTicketActivity) – Delete activity instead
- [GET /api/v1.0/tickets/{ticketId}/timeline](#/Tickets/getTicketTimeline) – View activity history

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | Unique identifier of the ticket |
| `ticket_activity_id` | `ticketActivityId` | `path` | `yes` | `str` | `-` | Unique identifier of the activity to update |
| `body` | `body` | `body` | `yes` | `TicketActivity` | `TicketActivity` | Updated activity details |

#### Returns

- Typed call return: `TicketActivityUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketActivityUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_ticket_assets`

Provenance: Golden OpenAPI contract

Operation ID: `updateTicketAssets`

- Sync: `client.tickets.update_ticket_assets(ticket_id=..., body=..., timeout=None)`
- Async: `await client.tickets.update_ticket_assets(ticket_id=..., body=..., timeout=None)`
- Raw payload: `client.tickets.update_ticket_assets.raw(ticket_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/assets`
- Source controller: `IncidentIQ API`

Update ticket assets

Replaces the asset list attached to a ticket and returns the refreshed asset collection. The array you submit is treated as the source of truth: omitted assets are removed, matching `TicketAssetId`/`AssetId`/`ModelId`+`CategoryId` entries are updated, and new items are added.

The service enforces update access and, when Permissions V2 is enabled, requires the caller to have rights to work the ticket. Asset update rules and ticket subject automation may run asynchronously after submission, so subsequent GET responses can reflect additional system changes.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) and read `Items[].TicketId`.
2. **assetId** (or model placeholder) – Resolve devices via [GET /api/v1.0/assets/assettag/{tag}](#/Assets/getAssetByTag) or [GET /api/v1.0/assets/for/{userId}/{all}](#/Assets/getUserFavoriteAssets) to capture `AssetId`. When linking a placeholder, pair `ModelId` with `CategoryId` from the same asset metadata.

**Workflow Example**
1. Locate ticket: [POST /api/v1.0/tickets](#/Tickets/searchTickets) with queue filters → capture `Items[0].TicketId`.
2. Find the device: [GET /api/v1.0/assets/assettag/{tag}](#/Assets/getAssetByTag) (or assets/for/{userId}/{all}) → capture `AssetId`, `ModelId`, and `CategoryId`.
3. Attach assets: [POST /api/v1.0/tickets/{ticketId}/assets](#/Tickets/updateTicketAssets) with the full asset list to keep on the ticket. Reuse `TicketAssetId` when retaining an existing link; omit an entry to remove it.

**Minimal Required Fields**: ticketId (path). Each array item must include `AssetId` or a `ModelId`/`CategoryId` placeholder.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | UUID of the ticket whose assets are being updated. Obtain via POST /api/v1.0/tickets and extract `Items[].TicketId`. |
| `body` | `body` | `body` | `yes` | `UpdateTicketAssetsRequest` | `UpdateTicketAssetsRequest` | Authoritative list of assets that should remain linked to the ticket. Entries missing `AssetId`, `ModelId`, and `CategoryId` are ignored; any existing ticket assets not included here are removed. Caller must have update rights and, when Permissions V2 is enabled, permission to work the ticket. |

#### Returns

- Typed call return: `TicketAssetListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketAssetListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_ticket_assets_by_category`

Provenance: Golden OpenAPI contract

Operation ID: `updateTicketAssetsByCategory`

- Sync: `client.tickets.update_ticket_assets_by_category(ticket_id=..., wizard_category_id=..., body=..., timeout=None)`
- Async: `await client.tickets.update_ticket_assets_by_category(ticket_id=..., wizard_category_id=..., body=..., timeout=None)`
- Raw payload: `client.tickets.update_ticket_assets_by_category.raw(ticket_id=..., wizard_category_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/assets/{wizardCategoryId}`
- Source controller: `IncidentIQ API`

Update ticket assets by category

Updates the assets linked to a ticket, filtering by wizard category. This endpoint is useful when working with ticket wizards that categorize assets during submission.

**Behavior**
- Assets are filtered by the specified wizard category before update
- The provided list replaces existing assets in that category
- Other assets outside the category are not affected

**Use Cases**
- Updating device assignments during multi-step ticket wizards
- Replacing assets within a specific category without affecting others

**Prerequisites**
- Obtain ticket ID via [POST /api/v1.0/tickets](#/Tickets/searchTickets)
- Obtain wizard category ID from the ticket creation wizard configuration

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | UUID of the ticket to update |
| `wizard_category_id` | `wizardCategoryId` | `path` | `yes` | `str` | `-` | UUID of the wizard category to filter assets by |
| `body` | `body` | `body` | `yes` | `UpdateTicketAssetsRequest` | `UpdateTicketAssetsRequest` | List of assets to associate with the ticket within the specified category |

#### Returns

- Typed call return: `TicketAssetListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketAssetListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_ticket_custom_fields`

Provenance: Golden OpenAPI contract

Operation ID: `updateTicketCustomFields`

- Sync: `client.tickets.update_ticket_custom_fields(ticket_id=..., body=..., timeout=None)`
- Async: `await client.tickets.update_ticket_custom_fields(ticket_id=..., body=..., timeout=None)`
- Raw payload: `client.tickets.update_ticket_custom_fields.raw(ticket_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/custom-fields`
- Source controller: `IncidentIQ API`

Update ticket custom fields

Updates one or more custom field values on an existing ticket.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) or your webhook payload to capture the target ticket's `TicketId`.
2. **CustomFieldTypeId** – Call [GET /api/v1.0/tickets/{ticketId}](#/Tickets/getTicket) or [GET /api/v1.0/custom-fields/types](#/CustomFields/listCustomFieldTypes) to map the custom field you intend to update and extract `CustomFieldValues[].CustomFieldTypeId`.
3. **Value format** – Match the `EditorTypeId` for the target field (text, numeric, dropdown, multi-select) to ensure the `Value` payload uses the correct casing or serialized array format.

**Workflow Example (WAG Osceola claim integration)**
1. Locate the insurance claim ticket via [POST /api/v1.0/tickets](#/Tickets/searchTickets) (filter by Issue or Workflow step) and capture `Items[0].TicketId`.
2. Inspect current custom fields with [GET /api/v1.0/tickets/{ticketId}](#/Tickets/getTicket) to confirm the `CustomFieldTypeId` that stores the WAG Claim Number.
3. Submit [POST /api/v1.0/tickets/{ticketId}/custom-fields](#/Tickets/updateTicketCustomFields) with an array of `TicketCustomFieldUpdateItem` objects (each containing `TicketId`, `CustomFieldTypeId`, and the new `Value`).
4. (Optional) Follow up with [POST /api/v1.0/tickets/{ticketId}/activities/new](#/Tickets/createTicketActivity) to log the claim approval/denial and include the same claim number in an activity comment.

**Minimal Required Fields**: ticketId, each request item requires `TicketId`, `CustomFieldTypeId`, and either `Value` or `ComplexValue` data, depending on the field editor type.

This endpoint is currently used by the WAG Osceola insurance claim workflow to synchronize claim numbers before submitting workflow actions.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | UUID of the ticket receiving the custom field update. |
| `body` | `body` | `body` | `yes` | `TicketCustomFieldUpdateRequest` | `TicketCustomFieldUpdateRequest` | Array of ticket custom field updates. Each entry should target a single `CustomFieldTypeId` and, when omitted, the client should set `TicketId` to match the `ticketId` path parameter. |

#### Returns

- Typed call return: `TicketCustomFieldUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketCustomFieldUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_ticket_description`

Provenance: Golden OpenAPI contract

Operation ID: `updateTicketDescription`

- Sync: `client.tickets.update_ticket_description(ticket_id=..., body=..., timeout=None)`
- Async: `await client.tickets.update_ticket_description(ticket_id=..., body=..., timeout=None)`
- Raw payload: `client.tickets.update_ticket_description.raw(ticket_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/description`
- Source controller: `IncidentIQ API`

Update ticket description

Updates the issue description text for a ticket. This modifies the detailed description field without affecting other ticket properties.

**Behavior**
- Replaces the existing `IssueDescription` with the new text
- Does not trigger workflow rules or status changes
- Records the change in ticket activity history

**Use Cases**
- Adding additional details after initial ticket creation
- Correcting or clarifying the original issue description
- Appending diagnostic information gathered during troubleshooting

**Prerequisites**
- Obtain ticket ID via [POST /api/v1.0/tickets](#/Tickets/searchTickets)
- Caller must have permission to work on the ticket

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | UUID of the ticket to update |
| `body` | `body` | `body` | `yes` | `UpdateTicketDescriptionRequest` | `UpdateTicketDescriptionRequest` | Updated description payload |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_ticket_next_step`

Provenance: Golden OpenAPI contract

Operation ID: `updateTicketNextStep`

- Sync: `client.tickets.update_ticket_next_step(ticket_id=..., next_step_id=..., body=..., timeout=None)`
- Async: `await client.tickets.update_ticket_next_step(ticket_id=..., next_step_id=..., body=..., timeout=None)`
- Raw payload: `client.tickets.update_ticket_next_step.raw(ticket_id=..., next_step_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/next-steps/{nextStepId}`
- Source controller: `IncidentIQ API`

Update next step

Updates an existing next step (task) for a ticket, including modifying the title, description, assignee, due date, or marking the step complete. Use this to track progress on individual tasks as work proceeds.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to find the ticket and extract `Items[].TicketId`.
2. **nextStepId** – Use [GET /api/v1.0/tickets/{ticketId}/next-steps](#/Tickets/getTicketNextSteps) to list steps and extract `TicketNextStepId`.

**Workflow Example**
1. List steps: [GET /api/v1.0/tickets/{ticketId}/next-steps](#/Tickets/getTicketNextSteps) → identify step to update
2. Get current: [GET /api/v1.0/tickets/{ticketId}/next-steps/{nextStepId}](#/Tickets/getTicketNextStep)
3. Update: [POST /api/v1.0/tickets/{ticketId}/next-steps/{nextStepId}](#/Tickets/updateTicketNextStep) with modified fields
4. Verify: [GET /api/v1.0/tickets/{ticketId}/next-steps/{nextStepId}](#/Tickets/getTicketNextStep) to confirm changes

**Request Body**: Include modified fields such as `Title`, `Description`, `AssignedUserId`, `DueDate`, `IsCompleted`.

**Use Cases**: Reassigning tasks, adjusting deadlines, marking tasks complete, adding notes to step descriptions.

**Related Endpoints**
- [GET /api/v1.0/tickets/{ticketId}/next-steps/{nextStepId}](#/Tickets/getTicketNextStep) – View step details
- [GET /api/v1.0/tickets/{ticketId}/next-steps](#/Tickets/getTicketNextSteps) – List all steps
- [DELETE /api/v1.0/tickets/{ticketId}/next-steps/{nextStepId}](#/Tickets/resolveTicketNextStep) – Remove step

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | Unique identifier of the ticket |
| `next_step_id` | `nextStepId` | `path` | `yes` | `str` | `-` | Unique identifier of the next step |
| `body` | `body` | `body` | `yes` | `TicketNextStepRequest` | `TicketNextStepRequest` | - |

#### Returns

- Typed call return: `TicketNextStepUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketNextStepUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_ticket_next_step_template`

Provenance: Golden OpenAPI contract

Operation ID: `updateTicketNextStepTemplate`

- Sync: `client.tickets.update_ticket_next_step_template(ticket_next_step_template_id=..., body=..., timeout=None)`
- Async: `await client.tickets.update_ticket_next_step_template(ticket_next_step_template_id=..., body=..., timeout=None)`
- Raw payload: `client.tickets.update_ticket_next_step_template.raw(ticket_next_step_template_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/next-step/templates/{TicketNextStepTemplateId}`
- Source controller: `IncidentIQ API`

Update an existing ticket next step template

Updates an existing ticket next step template. The template ID in the path must match an existing template.

**Prerequisites**
1. **TicketNextStepTemplateId** - Obtain via [GET /api/v1.0/tickets/next-step/templates](#/Tickets/listTicketNextStepTemplates), extract `Items[].TicketNextStepTemplateId`.
2. **ProductId** - Obtain via [GET /api/v1.0/products/all](#/Products/listProducts), extract `Items[].ProductId`.
3. **SiteId** (optional) - Obtain via [GET /api/v2.0/locations](#/Locations/getMyLocationsV2), extract `Items[].LocationId`.
4. **TicketNextStepTypeId** - Obtain via ticket next step type endpoints.

**Workflow Example**
1. Get existing template: `GET /api/v1.0/tickets/next-step/templates/{TicketNextStepTemplateId}`
2. Modify desired fields in the response body
3. Update template: `POST /api/v1.0/tickets/next-step/templates/{TicketNextStepTemplateId}` with modified body
4. Verify changes by re-fetching the template

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_next_step_template_id` | `TicketNextStepTemplateId` | `path` | `yes` | `str` | `-` | Unique identifier of the ticket next step template to update. Obtain via [GET /api/v1.0/tickets/next-step/templates](#/Tickets/listTicketNextStepTemplates), extract `Items[].TicketNextStepTemplateId`. |
| `body` | `body` | `body` | `yes` | `TicketNextStepTemplateRequest` | `TicketNextStepTemplateRequest` | Updated template configuration. |

#### Returns

- Typed call return: `TicketNextStepTemplateItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketNextStepTemplateItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_ticket_subject`

Provenance: Golden OpenAPI contract

Operation ID: `updateTicketSubject`

- Sync: `client.tickets.update_ticket_subject(ticket_id=..., body=..., timeout=None)`
- Async: `await client.tickets.update_ticket_subject(ticket_id=..., body=..., timeout=None)`
- Raw payload: `client.tickets.update_ticket_subject.raw(ticket_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/subject`
- Source controller: `IncidentIQ API`

Update ticket subject

Updates the subject line (title) of a ticket. The subject is the primary text displayed in ticket lists, search results, and notifications, making it critical for ticket identification and quick triage by agents.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to find the ticket and extract `Items[].TicketId`.

**Workflow Example**
1. Locate ticket: [POST /api/v1.0/tickets](#/Tickets/searchTickets) → extract `TicketId`
2. Review current subject: [GET /api/v1.0/tickets/{ticketId}](#/Tickets/getTicket) → note current `Subject`
3. Update: [POST /api/v1.0/tickets/{ticketId}/subject](#/Tickets/updateTicketSubject) with new subject text
4. Verify: [GET /api/v1.0/tickets/{ticketId}](#/Tickets/getTicket) to confirm change

**Request Body**: Provide `Subject` field with the new ticket title (typically 5-200 characters).

**Use Cases**: Correcting typos in user-submitted subjects, adding ticket classification prefixes, clarifying vague issue descriptions, standardizing subject formats.

**Note**: Subject changes are recorded in the ticket activity timeline for audit purposes.

**Related Endpoints**
- [GET /api/v1.0/tickets/{ticketId}](#/Tickets/getTicket) – View full ticket including subject
- [POST /api/v1.0/tickets/{ticketId}](#/Tickets/updateTicket) – Update multiple ticket fields
- [GET /api/v1.0/tickets/{ticketId}/timeline](#/Tickets/getTicketTimeline) – View change history

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | Unique identifier of the ticket |
| `body` | `body` | `body` | `yes` | `UpdateTicketSubjectRequest` | `UpdateTicketSubjectRequest` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_ticket_tags`

Provenance: Golden OpenAPI contract

Operation ID: `updateTicketTags`

- Sync: `client.tickets.update_ticket_tags(ticket_id=..., body=..., timeout=None)`
- Async: `await client.tickets.update_ticket_tags(ticket_id=..., body=..., timeout=None)`
- Raw payload: `client.tickets.update_ticket_tags.raw(ticket_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/{ticketId}/tags`
- Source controller: `IncidentIQ API`

Update ticket tags

Bulk updates the tags on a ticket by replacing the current tag set with the provided list. Tags enable flexible categorization and filtering beyond the standard issue type hierarchy, supporting custom workflows and reporting needs.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to find the ticket and extract `Items[].TicketId`.
2. **Tag objects** – Use [GET /api/v1.0/tags/query](#/Tags/getTagsByQuery) to retrieve available tags with their `TagId` values.

**Workflow Example**
1. Locate ticket: [POST /api/v1.0/tickets](#/Tickets/searchTickets) → extract `TicketId`
2. Get current tags: [GET /api/v1.0/tickets/{ticketId}](#/Tickets/getTicket) → note existing tags array
3. List available tags: [GET /api/v1.0/tags/query](#/Tags/getTagsByQuery) → identify tags to add
4. Update tags: [POST /api/v1.0/tickets/{ticketId}/tags](#/Tickets/updateTicketTags) with complete tag array
5. Verify: [GET /api/v1.0/tickets/{ticketId}](#/Tickets/getTicket) to confirm tag changes

**Request Body**: Array of `Tag` objects including `TagId` for each tag to apply. Empty array removes all tags.

**Note**: This is a replacement operation, not additive. Include all desired tags in the request.

**Related Endpoints**
- [POST /api/v1.0/tickets/{ticketId}/tags/{tagId}](#/Tickets/addTicketTag) – Add single tag
- [DELETE /api/v1.0/tickets/{ticketId}/tags/{tagId}](#/Tickets/removeTicketTag) – Remove single tag
- [GET /api/v1.0/tags/query](#/Tags/getTagsByQuery) – List available tags

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | Unique identifier of the ticket |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | Array of tags to apply to the ticket |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_ticket_view`

Provenance: Golden OpenAPI contract

Operation ID: `updateTicketView`

- Sync: `client.tickets.update_ticket_view(view_id=..., body=..., timeout=None)`
- Async: `await client.tickets.update_ticket_view(view_id=..., body=..., timeout=None)`
- Raw payload: `client.tickets.update_ticket_view.raw(view_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/views/{viewId}`
- Source controller: `IncidentIQ API`

Update ticket view

Updates an existing ticket view's configuration, including filters, column layout, sort order, page size, and sharing settings. If the view does not exist, a new view is created with the provided configuration.

**Prerequisites**
1. **viewId** – Use [GET /api/v1.0/tickets/views](#/Tickets/listTicketViews) to list views and extract `Items[].ViewId`.

**Workflow Example**
1. Get current: [GET /api/v1.0/tickets/views/{viewId}](#/Tickets/getTicketView) → retrieve existing configuration
2. Modify: Update filter criteria, columns, sort order, or sharing settings
3. Save: [POST /api/v1.0/tickets/views/{viewId}](#/Tickets/updateTicketView) with updated definition
4. Verify: [GET /api/v1.0/tickets/views/{viewId}](#/Tickets/getTicketView) to confirm changes

**Request Body**: Provide complete `ViewDefinition` including `Name`, `Filters`, `Columns`, `Sort`, `PageSize`, and optionally `IsShared`.

**Use Cases**: Refining search criteria, adding/removing columns, changing default sort, sharing personal views with team.

**Note**: Only the view owner or administrators can update views. Updating shared views affects all users who use that view.

**Related Endpoints**
- [GET /api/v1.0/tickets/views/{viewId}](#/Tickets/getTicketView) – Get current view definition
- [DELETE /api/v1.0/tickets/views/{viewId}](#/Tickets/deleteTicketView) – Delete view
- [POST /api/v1.0/tickets/views/new](#/Tickets/createTicketView) – Create new view instead

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `view_id` | `viewId` | `path` | `yes` | `str` | `-` | Identifier of the ticket view to update. |
| `body` | `body` | `body` | `yes` | `ViewDefinition` | `ViewDefinition` | - |

#### Returns

- Typed call return: `ViewItemUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ViewItemUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_ticket_view_schedules`

Provenance: Golden OpenAPI contract

Operation ID: `updateTicketViewSchedules`

- Sync: `client.tickets.update_ticket_view_schedules(view_id=..., body=..., timeout=None)`
- Async: `await client.tickets.update_ticket_view_schedules(view_id=..., body=..., timeout=None)`
- Raw payload: `client.tickets.update_ticket_view_schedules.raw(view_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/views/{viewId}/schedules`
- Source controller: `IncidentIQ API`

Update ticket view schedules

Replaces the scheduled report/export configuration for a ticket view. Schedules define automated delivery of view results via email at specified intervals, enabling regular reporting without manual execution.

**Prerequisites**
1. **viewId** – Use [GET /api/v1.0/tickets/views](#/Tickets/listTicketViews) to list views and extract `Items[].ViewId`.

**Workflow Example**
1. Get view: [GET /api/v1.0/tickets/views/{viewId}](#/Tickets/getTicketView) to verify view exists
2. Define schedule: Create schedule configuration with frequency, recipients, and export format
3. Update schedules: [POST /api/v1.0/tickets/views/{viewId}/schedules](#/Tickets/updateTicketViewSchedules) with schedule array
4. Verify: The scheduled reports will begin delivery according to the configuration

**Request Body**: Array of `ViewSchedule` objects specifying `IsEnabled`, schedule frequency, recipients, and export options.

**Use Cases**: Setting up daily/weekly ticket reports for management, automating KPI delivery, scheduling team performance summaries.

**Note**: Schedules are replaced entirely; include all desired schedules in each request.

**Related Endpoints**
- [GET /api/v1.0/tickets/views/{viewId}](#/Tickets/getTicketView) – View definition
- [POST /api/v1.0/tickets/views/{viewId}](#/Tickets/updateTicketView) – Update view filters/columns
- [GET /api/v1.0/views/schedules](#/Views/listTicketViews) – List all scheduled views

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `view_id` | `viewId` | `path` | `yes` | `str` | `-` | Identifier of the ticket view to update. |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_ticket_view_sort`

Provenance: Golden OpenAPI contract

Operation ID: `updateTicketViewSort`

- Sync: `client.tickets.update_ticket_view_sort(view_id=..., body=..., timeout=None)`
- Async: `await client.tickets.update_ticket_view_sort(view_id=..., body=..., timeout=None)`
- Raw payload: `client.tickets.update_ticket_view_sort.raw(view_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/tickets/views/{viewId}/sort`
- Source controller: `IncidentIQ API`

Update ticket view sort

Updates the default sort order for a saved ticket view. The sort configuration determines how tickets are ordered when the view is loaded. Common sort fields include `ModifiedDate`, `CreatedDate`, `TicketPriority`, and `DueDate`.

**Prerequisites**
1. **viewId** – Use [GET /api/v1.0/tickets/views](#/Tickets/listTicketViews) to list views and extract `Items[].ViewId`.

**Workflow Example**
1. Identify view: [GET /api/v1.0/tickets/views](#/Tickets/listTicketViews) → select `ViewId` to update
2. Update sort: [POST /api/v1.0/tickets/views/{viewId}/sort](#/Tickets/updateTicketViewSort) with `Field`, `Name`, and `Direction`
3. Test view: [POST /api/v1.0/tickets](#/Tickets/searchTickets) with the view's Schema to verify new order

**Sort Fields**: TicketClosedDate, ModifiedDate, CreatedDate, TicketPriority, DueDate, Subject, TicketNumber
**Directions**: Ascending, Descending

**Related Endpoints**
- [GET /api/v1.0/tickets/views/{viewId}](#/Tickets/getTicketView) – View current sort
- [POST /api/v1.0/tickets/views/{viewId}](#/Tickets/updateTicketView) – Update other view properties

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `view_id` | `viewId` | `path` | `yes` | `str` | `-` | Identifier of the ticket view to update. |
| `body` | `body` | `body` | `yes` | `ViewSort` | `ViewSort` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
