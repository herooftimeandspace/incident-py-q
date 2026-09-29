# `subtasks` Golden Namespace

Sync client access: `client.subtasks`

Async client access: `client.subtasks` with `await` on method calls.

These methods are Golden because they come from the bundled Incident IQ OpenAPI contract.

## Aliases

| Alias | Canonical Method | Route |
| --- | --- | --- |
| `create` | `create_subtask_group` | `POST /api/v1.0/subtasks/group/new` |

## Methods

### `assign_subtask`

Provenance: Golden OpenAPI contract

Operation ID: `assignSubtask`

- Sync: `client.subtasks.assign_subtask(subtask_id=..., user_id=..., timeout=None)`
- Async: `await client.subtasks.assign_subtask(subtask_id=..., user_id=..., timeout=None)`
- Raw payload: `client.subtasks.assign_subtask.raw(subtask_id=..., user_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/subtasks/{subtaskId}/assign/{userId}`
- Source controller: `IncidentIQ API`

Assign subtask to user

Assigns a subtask to a specific user, adding it to their personal work queue and triggering assignment notifications. The assignee becomes responsible for completing the subtask.

**Prerequisites**
1. **subtaskId** – Use [GET /api/v1.0/subtasks/{id}](#/Tickets/getSubtasksForTicket) (passing the ticketId) to list subtasks and extract `TicketSubtaskId`.
2. **userId** – Use [POST /api/v1.0/search](#/Users/searchUsers) to find users and extract `Item.Users[].UserId`.

**Workflow Example**
1. List subtasks: [GET /api/v1.0/subtasks/{ticketId}](#/Tickets/getSubtasksForTicket) → identify unassigned subtask
2. Find assignee: [POST /api/v1.0/search](#/Search/globalSearch) with user criteria → extract `UserId`
3. Assign: [POST /api/v1.0/subtasks/{subtaskId}/assign/{userId}](#/Tickets/assignSubtask)
4. Verify: [GET /api/v1.0/subtasks](#/Tickets/getUserSubtasks) as the assignee to confirm in queue

**Notifications**: The assignee receives email/in-app notification based on their notification preferences.

**Related Endpoints**
- [POST /api/v1.0/subtasks/{ticketSubtaskId}/unassign](#/Tickets/unassignSubtask) – Remove assignment
- [POST /api/v1.0/subtasks/{subtaskId}/complete](#/Tickets/completeSubtask) – Complete assigned subtask
- [GET /api/v1.0/subtasks](#/Tickets/getUserSubtasks) – View assigned subtasks

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `subtask_id` | `subtaskId` | `path` | `yes` | `str` | `-` | Unique identifier of the subtask |
| `user_id` | `userId` | `path` | `yes` | `str` | `-` | Unique identifier of the user to assign the subtask to |

#### Returns

- Typed call return: `SubtaskListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `SubtaskListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `assign_subtasks_to_group`

Provenance: Golden OpenAPI contract

Operation ID: `assignSubtasksToGroup`

- Sync: `client.subtasks.assign_subtasks_to_group(body=..., timeout=None)`
- Async: `await client.subtasks.assign_subtasks_to_group(body=..., timeout=None)`
- Raw payload: `client.subtasks.assign_subtasks_to_group.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/subtasks/group/assign`
- Source controller: `IncidentIQ API`

Assign subtasks to group

Assigns multiple subtasks to an existing subtask group, allowing you to organize related work items together for batch management and visibility.

**Prerequisites**
1. **SubtaskGroupId** – Use [POST /api/v1.0/subtasks/group/new](#/Tickets/createSubtaskGroup) to create a group, or [GET /api/v1.0/subtasks/my/groups](#/Tickets/getMySubtaskGroups) to find existing groups.
2. **SubtaskIds** – Use [GET /api/v1.0/subtasks/{id}](#/Tickets/getSubtasksForTicket) to list subtasks for a ticket.

**Workflow Example**
1. Create or identify group: [POST /api/v1.0/subtasks/group/new](#/Tickets/createSubtaskGroup) → extract `Item.SubtaskGroupId`
2. List subtasks: [GET /api/v1.0/subtasks/{ticketId}](#/Tickets/getSubtasksForTicket) → select `TicketSubtaskId` values to group
3. Assign to group: [POST /api/v1.0/subtasks/group/assign](#/Tickets/assignSubtasksToGroup) with group and subtask IDs

**Related Endpoints**
- [POST /api/v1.0/subtasks/group/ungroup/{subtaskGroupId}/{ticketId}](#/Tickets/ungroupSubtaskGroupFromTicket) – Remove from group

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `AssignTicketSubtaskGroupRequest` | `AssignTicketSubtaskGroupRequest` | Assignment request including the group and subtask IDs. |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `complete_subtask`

Provenance: Golden OpenAPI contract

Operation ID: `completeSubtask`

- Sync: `client.subtasks.complete_subtask(subtask_id=..., timeout=None)`
- Async: `await client.subtasks.complete_subtask(subtask_id=..., timeout=None)`
- Raw payload: `client.subtasks.complete_subtask.raw(subtask_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/subtasks/{subtaskId}/complete`
- Source controller: `IncidentIQ API`

Complete subtask

Marks a subtask as complete, updating its status and recording completion time. When all subtasks on a ticket are completed, workflow rules may automatically advance the parent ticket's status.

**Prerequisites**
1. **subtaskId** – Use [GET /api/v1.0/subtasks/{id}](#/Tickets/getSubtasksForTicket) to list subtasks and extract `TicketSubtaskId`.

**Workflow Example**
1. View assigned subtasks: [GET /api/v1.0/subtasks](#/Tickets/getUserSubtasks) → identify subtask to complete
2. Complete work: Perform the required task
3. Mark complete: [POST /api/v1.0/subtasks/{subtaskId}/complete](#/Tickets/completeSubtask)
4. Refresh queue: [GET /api/v1.0/subtasks](#/Tickets/getUserSubtasks) to verify removal from active queue

**Automation Triggers**: Completing subtasks may trigger workflow rules, notifications, or parent ticket status changes based on site configuration.

**Note**: Use [POST /api/v1.0/subtasks/{ticketSubtaskId}/revert](#/Tickets/revertSubtaskCompletion) to undo completion if marked prematurely.

**Related Endpoints**
- [POST /api/v1.0/subtasks/{ticketSubtaskId}/revert](#/Tickets/revertSubtaskCompletion) – Undo completion
- [GET /api/v1.0/subtasks](#/Tickets/getUserSubtasks) – View remaining subtasks

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `subtask_id` | `subtaskId` | `path` | `yes` | `str` | `-` | Unique identifier of the subtask |

#### Returns

- Typed call return: `SubtaskListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `SubtaskListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `convert_subtask_to_ticket`

Provenance: Golden OpenAPI contract

Operation ID: `convertSubtaskToTicket`

- Sync: `client.subtasks.convert_subtask_to_ticket(ticket_subtask_id=..., timeout=None)`
- Async: `await client.subtasks.convert_subtask_to_ticket(ticket_subtask_id=..., timeout=None)`
- Raw payload: `client.subtasks.convert_subtask_to_ticket.raw(ticket_subtask_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/subtasks/{ticketSubtaskId}/convert`
- Source controller: `IncidentIQ API`

Convert subtask to ticket

Converts a subtask into a full standalone ticket, promoting it from a checklist item to a complete work item with its own timeline, activities, and workflow. The original subtask is marked as converted and linked to the new ticket.

**Prerequisites**
1. **ticketSubtaskId** – Use [GET /api/v1.0/subtasks/{id}](#/Tickets/getSubtasksForTicket) to list subtasks and extract `TicketSubtaskId`.

**Workflow Example**
1. Identify subtask: [GET /api/v1.0/subtasks/{ticketId}](#/Tickets/getSubtasksForTicket) → select subtask requiring promotion
2. Convert: [POST /api/v1.0/subtasks/{ticketSubtaskId}/convert](#/Tickets/convertSubtaskToTicket)
3. Access new ticket: Use the returned ticket ID to view, assign, or further configure the new ticket

**Conversion Behavior**: The new ticket inherits the subtask's title and description. The subtask remains visible but marked as converted with a link to the new ticket.

**Use Cases**: When a simple task grows in complexity, requires its own SLA, or needs independent tracking.

**Related Endpoints**
- [GET /api/v1.0/subtasks/{id}](#/Tickets/getSubtasksForTicket) – List subtasks
- [GET /api/v1.0/tickets/{ticketId}](#/Tickets/getTicket) – View converted ticket
- [POST /api/v1.0/tickets/new](#/Tickets/createTicket) – Create ticket directly instead

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_subtask_id` | `ticketSubtaskId` | `path` | `yes` | `str` | `-` | Subtask identifier. |

#### Returns

- Typed call return: `TicketSubtaskItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketSubtaskItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_subtask`

Provenance: Golden OpenAPI contract

Operation ID: `createSubtask`

- Sync: `client.subtasks.create_subtask(body=..., timeout=None)`
- Async: `await client.subtasks.create_subtask(body=..., timeout=None)`
- Raw payload: `client.subtasks.create_subtask.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/subtasks/create`
- Source controller: `IncidentIQ API`

Create subtask

Creates a new subtask within a parent ticket. Subtasks are smaller work items that can be assigned and tracked independently, allowing complex tickets to be broken down into manageable pieces.

**Prerequisites**
1. **TicketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to find the parent ticket and extract `Items[].TicketId`.
2. **AssignedUserId** (optional) – Use [POST /api/v1.0/search](#/Search/globalSearch) to find a user and extract `Item.Users[].UserId`.

**Workflow Example**
1. Find parent ticket: [POST /api/v1.0/tickets](#/Tickets/searchTickets) → extract `TicketId`
2. Create subtask: [POST /api/v1.0/subtasks/create](#/Tickets/createSubtask) with `TicketId` and subtask details
3. (Optional) Assign: Include `AssignedUserId` in request or use [POST /api/v1.0/subtasks/{subtaskId}/assign/{userId}](#/Tickets/assignSubtask)
4. Track progress: [GET /api/v1.0/subtasks/{id}](#/Tickets/getSubtasksForTicket) to monitor subtask status

**Minimal Required Fields**: TicketId, Subject

**Related Endpoints**
- [GET /api/v1.0/subtasks/{id}](#/Tickets/getSubtasksForTicket) – List subtasks for ticket
- [POST /api/v1.0/subtasks/{subtaskId}/complete](#/Tickets/completeSubtask) – Mark subtask complete

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `TicketSubtaskRequest` | `TicketSubtaskRequest` | - |

#### Returns

- Typed call return: `SubtaskListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `SubtaskListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_subtask_group`

Provenance: Golden OpenAPI contract

Operation ID: `createSubtaskGroup`

- Sync: `client.subtasks.create_subtask_group(body=..., timeout=None)`
- Async: `await client.subtasks.create_subtask_group(body=..., timeout=None)`
- Raw payload: `client.subtasks.create_subtask_group.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/subtasks/group/new`
- Source controller: `IncidentIQ API`
- Aliases: `create`

Create subtask group

Creates a new subtask group for organizing related subtasks across one or more tickets. Groups help manage batch operations and provide visual organization for complex workflows.

**Prerequisites**
1. **Authentication** – The authenticated user will own the created group.

**Workflow Example**
1. Create group: [POST /api/v1.0/subtasks/group/new](#/Tickets/createSubtaskGroup) with `Name` and optional metadata
2. Assign subtasks: Use [POST /api/v1.0/subtasks/group/assign](#/Tickets/assignSubtasksToGroup) to add subtasks
3. View groups: [GET /api/v1.0/subtasks/my/groups](#/Tickets/getMySubtaskGroups) to list your groups

**Minimal Required Fields**: Name

**Related Endpoints**
- [DELETE /api/v1.0/subtasks/group/{subtaskGroupId}](#/Tickets/deleteSubtaskGroup) – Delete a group
- [POST /api/v1.0/subtasks/group/{subtaskGroupId}](#/Tickets/updateSubtaskGroup) – Update group properties

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `SubtaskGroup` | `SubtaskGroup` | Subtask group payload. |

#### Returns

- Typed call return: `CreateSubtaskGroupResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CreateSubtaskGroupResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_subtask`

Provenance: Golden OpenAPI contract

Operation ID: `deleteSubtask`

- Sync: `client.subtasks.delete_subtask(id=..., timeout=None)`
- Async: `await client.subtasks.delete_subtask(id=..., timeout=None)`
- Raw payload: `client.subtasks.delete_subtask.raw(id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/subtasks/{id}`
- Source controller: `IncidentIQ API`

Delete subtask

Permanently deletes a subtask from a ticket. The subtask is removed from the parent ticket's work breakdown and cannot be recovered. Consider completing or archiving subtasks instead of deleting if audit trail is important.

**Prerequisites**
1. **id** – Use [GET /api/v1.0/subtasks/{id}](#/Tickets/getSubtasksForTicket) (passing the ticketId) to list subtasks and extract `TicketSubtaskId`.

**Workflow Example**
1. List subtasks: [GET /api/v1.0/subtasks/{ticketId}](#/Tickets/getSubtasksForTicket) → identify `TicketSubtaskId` to delete
2. Delete subtask: [DELETE /api/v1.0/subtasks/{id}](#/Tickets/deleteSubtask)
3. Verify removal: [GET /api/v1.0/subtasks/{ticketId}](#/Tickets/getSubtasksForTicket) to confirm deletion

**Note**: Deletion is permanent. To preserve history, consider using [POST /api/v1.0/subtasks/{subtaskId}/complete](#/Tickets/completeSubtask) instead.

**Related Endpoints**
- [POST /api/v1.0/subtasks/{ticketSubtaskId}/duplicate](#/Tickets/duplicateSubtask) – Create copy before deleting
- [POST /api/v1.0/subtasks/{subtaskId}/complete](#/Tickets/completeSubtask) – Complete instead of delete

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `id` | `path` | `yes` | `str` | `-` | Subtask identifier to delete (DELETE). |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_subtask_group`

Provenance: Golden OpenAPI contract

Operation ID: `deleteSubtaskGroup`

- Sync: `client.subtasks.delete_subtask_group(subtask_group_id=..., timeout=None)`
- Async: `await client.subtasks.delete_subtask_group(subtask_group_id=..., timeout=None)`
- Raw payload: `client.subtasks.delete_subtask_group.raw(subtask_group_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/subtasks/group/{subtaskGroupId}`
- Source controller: `IncidentIQ API`

Delete subtask group

Permanently deletes a subtask group. Subtasks that were members of the group are preserved but become ungrouped. This operation cannot be undone.

**Prerequisites**
1. **subtaskGroupId** – Use [GET /api/v1.0/subtasks/my/groups](#/Tickets/getMySubtaskGroups) to list your groups and extract `SubtaskGroupId`.

**Workflow Example**
1. List groups: [GET /api/v1.0/subtasks/my/groups](#/Tickets/getMySubtaskGroups) → identify `SubtaskGroupId` to delete
2. Delete group: [DELETE /api/v1.0/subtasks/group/{subtaskGroupId}](#/Tickets/deleteSubtaskGroup)
3. Verify removal: [GET /api/v1.0/subtasks/my/groups](#/Tickets/getMySubtaskGroups) to confirm deletion

**Note**: Only the group owner or administrators can delete a group.

**Related Endpoints**
- [POST /api/v1.0/subtasks/group/new](#/Tickets/createSubtaskGroup) – Create a new group
- [POST /api/v1.0/subtasks/group/{subtaskGroupId}](#/Tickets/updateSubtaskGroup) – Update group properties

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `subtask_group_id` | `subtaskGroupId` | `path` | `yes` | `str` | `-` | Subtask group identifier. |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `duplicate_subtask`

Provenance: Golden OpenAPI contract

Operation ID: `duplicateSubtask`

- Sync: `client.subtasks.duplicate_subtask(ticket_subtask_id=..., timeout=None)`
- Async: `await client.subtasks.duplicate_subtask(ticket_subtask_id=..., timeout=None)`
- Raw payload: `client.subtasks.duplicate_subtask.raw(ticket_subtask_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/subtasks/{ticketSubtaskId}/duplicate`
- Source controller: `IncidentIQ API`

Duplicate subtask

Creates an exact copy of an existing subtask on the same parent ticket. The duplicated subtask inherits the original's title, description, and settings but starts with a fresh completion status and no assignment.

**Prerequisites**
1. **ticketSubtaskId** – Use [GET /api/v1.0/subtasks/{id}](#/Tickets/getSubtasksForTicket) (passing the ticketId) to list subtasks and extract `TicketSubtaskId`.

**Workflow Example**
1. List subtasks: [GET /api/v1.0/subtasks/{ticketId}](#/Tickets/getSubtasksForTicket) → identify `TicketSubtaskId` to duplicate
2. Duplicate: [POST /api/v1.0/subtasks/{ticketSubtaskId}/duplicate](#/Tickets/duplicateSubtask)
3. (Optional) Assign duplicate: Use [POST /api/v1.0/subtasks/{subtaskId}/assign/{userId}](#/Tickets/assignSubtask)

**Use Cases**: Useful for recurring tasks, template creation, or when multiple similar work items are needed.

**Related Endpoints**
- [POST /api/v1.0/subtasks/{subtaskId}/assign/{userId}](#/Tickets/assignSubtask) – Assign the new copy
- [POST /api/v1.0/tickets/{ticketId}/subtasks/new](#/Tickets/createSubtask) – Create from scratch instead

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_subtask_id` | `ticketSubtaskId` | `path` | `yes` | `str` | `-` | Subtask identifier. |

#### Returns

- Typed call return: `TicketSubtaskItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketSubtaskItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_my_subtask_groups`

Provenance: Golden OpenAPI contract

Operation ID: `getMySubtaskGroups`

- Sync: `client.subtasks.get_my_subtask_groups(timeout=None)`
- Async: `await client.subtasks.get_my_subtask_groups(timeout=None)`
- Raw payload: `client.subtasks.get_my_subtask_groups.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/subtasks/my/groups`
- Source controller: `IncidentIQ API`

Get my subtask groups

Retrieves all subtask groups owned by the authenticated user. Groups organize related subtasks for better visibility and batch management across multiple tickets.

**Response Contents**
- Lists all groups where the current user is the owner
- Includes group metadata (name, creation date, member count)
- Groups can span multiple tickets for cross-ticket organization

**Workflow Example**
1. List your groups: [GET /api/v1.0/subtasks/my/groups](#/Tickets/getMySubtaskGroups)
2. View group subtasks: For each group, call [GET /api/v1.0/subtasks/{id}](#/Tickets/getSubtasksForTicket) on associated tickets
3. Manage group: Use [POST /api/v1.0/subtasks/group/{subtaskGroupId}](#/Tickets/updateSubtaskGroup) to update properties

**Use Cases**: Batch work tracking, project-level subtask organization, cross-ticket task management.

**Related Endpoints**
- [POST /api/v1.0/subtasks/group/new](#/Tickets/createSubtaskGroup) – Create new group
- [POST /api/v1.0/subtasks/group/assign](#/Tickets/assignSubtasksToGroup) – Add subtasks to group
- [GET /api/v1.0/subtasks/{userId}/groups](#/Tickets/getUserSubtaskGroups) – View another user's groups

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `SubtaskGroupListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `SubtaskGroupListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_subtask_source_ticket`

Provenance: Golden OpenAPI contract

Operation ID: `getSubtaskSourceTicket`

- Sync: `client.subtasks.get_subtask_source_ticket(ticket_id=..., timeout=None)`
- Async: `await client.subtasks.get_subtask_source_ticket(ticket_id=..., timeout=None)`
- Raw payload: `client.subtasks.get_subtask_source_ticket.raw(ticket_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/subtasks/{ticketId}/sourceTicket`
- Source controller: `IncidentIQ API`

Get source ticket for a subtask

Retrieves the source ticket that originated a change management subtask. When tickets are created through change management workflows, subtasks may be linked back to the original request ticket.

**Prerequisites**
1. **ticketId** – Use [GET /api/v1.0/subtasks/{id}](#/Tickets/getSubtasksForTicket) to list subtasks and identify those created via change management.

**Workflow Example**
1. List subtasks: [GET /api/v1.0/subtasks/{ticketId}](#/Tickets/getSubtasksForTicket) → identify change management subtasks
2. Get source ticket: [GET /api/v1.0/subtasks/{ticketId}/sourceTicket](#/Tickets/getSubtaskSourceTicket)
3. Navigate to source: Use the returned ticket ID to access the originating request

**Response Contents**: Returns the source ticket's basic information including TicketId, Subject, and Status for context.

**Use Cases**: Audit trails, change management tracking, linking related work items.

**Related Endpoints**
- [GET /api/v1.0/subtasks/{id}](#/Tickets/getSubtasksForTicket) – List subtasks for a ticket
- [GET /api/v1.0/tickets/{ticketId}](#/Tickets/getTicket) – View full source ticket details
- [POST /api/v1.0/subtasks/{ticketSubtaskId}/convert](#/Tickets/convertSubtaskToTicket) – Convert subtask to full ticket

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | Ticket identifier. |

#### Returns

- Typed call return: `SubtaskSourceTicketResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `SubtaskSourceTicketResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_subtasks_for_ticket`

Provenance: Golden OpenAPI contract

Operation ID: `getSubtasksForTicket`

- Sync: `client.subtasks.get_subtasks_for_ticket(id=..., p=None, s=None, timeout=None)`
- Async: `await client.subtasks.get_subtasks_for_ticket(id=..., p=None, s=None, timeout=None)`
- Raw payload: `client.subtasks.get_subtasks_for_ticket.raw(id=..., p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v1.0/subtasks/{id}`
- Source controller: `IncidentIQ API`

Get subtasks for a ticket

Retrieves all subtasks associated with a specific ticket. Returns a paginated list of subtasks including their status, assignee, and completion state.

**Prerequisites**
1. **id** (TicketId) – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to find tickets and extract `Items[].TicketId`.

**Workflow Example**
1. Find ticket: [POST /api/v1.0/tickets](#/Tickets/searchTickets) → extract `TicketId`
2. List subtasks: [GET /api/v1.0/subtasks/{id}](#/Tickets/getSubtasksForTicket) with `TicketId`
3. Work subtask: Complete the work item
4. Mark complete: [POST /api/v1.0/subtasks/{subtaskId}/complete](#/Tickets/completeSubtask)

**Response Fields**: Each subtask includes `TicketSubtaskId`, `Subject`, `Description`, `IsComplete`, `AssignedUserId`, `AssignedUser` details, and `SortOrder`.

**Query Parameters**: Supports pagination with `$p` (page index) and `$s` (page size).

**Related Endpoints**
- [POST /api/v1.0/subtasks/create](#/Tickets/createSubtask) – Create new subtask
- [POST /api/v1.0/subtasks/{subtaskId}/complete](#/Tickets/completeSubtask) – Complete subtask
- [POST /api/v1.0/subtasks/{subtaskId}/assign/{userId}](#/Tickets/assignSubtask) – Assign subtask

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `id` | `path` | `yes` | `str` | `-` | Ticket identifier used to fetch subtasks (GET). |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index to retrieve |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of records per page |

#### Returns

- Typed call return: `SubtaskResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `SubtaskResponse`
- Pagination helper: `client.subtasks.get_subtasks_for_ticket.iter_pages(start_page=1, page_size=100, max_pages=None, id=..., p=None, s=None, timeout=None)`

---

### `get_user_subtask_groups`

Provenance: Golden OpenAPI contract

Operation ID: `getUserSubtaskGroups`

- Sync: `client.subtasks.get_user_subtask_groups(user_id=..., timeout=None)`
- Async: `await client.subtasks.get_user_subtask_groups(user_id=..., timeout=None)`
- Raw payload: `client.subtasks.get_user_subtask_groups.raw(user_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/subtasks/{userId}/groups`
- Source controller: `IncidentIQ API`

Get subtask groups for a user

Retrieves all subtask groups owned by a specific user. Use this endpoint to view another user's grouped subtasks for management or visibility purposes.

**Prerequisites**
1. **userId** – Use [POST /api/v1.0/search](#/Users/searchUsers) to find users and extract `Item.Users[].UserId`.

**Workflow Example**
1. Find user: [POST /api/v1.0/search](#/Search/globalSearch) with user criteria → extract `Item.Users[0].UserId`
2. Get groups: [GET /api/v1.0/subtasks/{userId}/groups](#/Tickets/getUserSubtaskGroups)
3. View group contents: For each group, use [GET /api/v1.0/subtasks/{id}](#/Tickets/getSubtasksForTicket) to see member subtasks

**Note**: Requires appropriate permissions to view another user's subtask groups. For your own groups, use [GET /api/v1.0/subtasks/my/groups](#/Tickets/getMySubtaskGroups) instead.

**Related Endpoints**
- [GET /api/v1.0/subtasks/my/groups](#/Tickets/getMySubtaskGroups) – View your own groups
- [POST /api/v1.0/subtasks/group/new](#/Tickets/createSubtaskGroup) – Create a new group

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `userId` | `path` | `yes` | `str` | `-` | User identifier. |

#### Returns

- Typed call return: `SubtaskGroupListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `SubtaskGroupListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_user_subtasks`

Provenance: Golden OpenAPI contract

Operation ID: `getUserSubtasks`

- Sync: `client.subtasks.get_user_subtasks(timeout=None)`
- Async: `await client.subtasks.get_user_subtasks(timeout=None)`
- Raw payload: `client.subtasks.get_user_subtasks.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/subtasks`
- Source controller: `IncidentIQ API`

Get my open subtasks

Retrieves all open (incomplete) subtasks assigned to the authenticated user across all tickets. This endpoint provides a unified work queue view for subtask management.

**Response Contents**
- Returns subtasks where `IsComplete: false` and the current user is the assignee
- Includes parent ticket references, due dates, and priority information
- Sorted by creation date (newest first) by default

**Workflow Example**
1. Get your subtasks: [GET /api/v1.0/subtasks](#/Tickets/getUserSubtasks)
2. Work on subtask: Complete the required work
3. Mark complete: [POST /api/v1.0/subtasks/{subtaskId}/complete](#/Tickets/completeSubtask)
4. Refresh queue: [GET /api/v1.0/subtasks](#/Tickets/getUserSubtasks) to see remaining work

**Use Cases**: Personal work queue, dashboard widget, mobile notifications.

**Related Endpoints**
- [GET /api/v1.0/subtasks/my/groups](#/Tickets/getMySubtaskGroups) – View your subtask groups
- [POST /api/v1.0/subtasks/{subtaskId}/complete](#/Tickets/completeSubtask) – Complete a subtask
- [POST /api/v1.0/subtasks/{ticketSubtaskId}/unassign](#/Tickets/unassignSubtask) – Unassign from yourself

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `TicketSubtaskListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketSubtaskListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `remove_subtask_group_from_ticket`

Provenance: Golden OpenAPI contract

Operation ID: `removeSubtaskGroupFromTicket`

- Sync: `client.subtasks.remove_subtask_group_from_ticket(subtask_group_id=..., ticket_id=..., timeout=None)`
- Async: `await client.subtasks.remove_subtask_group_from_ticket(subtask_group_id=..., ticket_id=..., timeout=None)`
- Raw payload: `client.subtasks.remove_subtask_group_from_ticket.raw(subtask_group_id=..., ticket_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/subtasks/group/remove/{subtaskGroupId}/{ticketId}`
- Source controller: `IncidentIQ API`

Remove group from ticket

Removes an entire subtask group from a specific ticket, including all subtask associations within that group. This operation clears the group assignment while preserving the individual subtasks.

**Prerequisites**
1. **subtaskGroupId** – Use [GET /api/v1.0/subtasks/my/groups](#/Tickets/getMySubtaskGroups) or [GET /api/v1.0/subtasks/{userId}/groups](#/Tickets/getUserSubtaskGroups) to find group identifiers.
2. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to locate the parent ticket.

**Workflow Example**
1. Find groups: [GET /api/v1.0/subtasks/my/groups](#/Tickets/getMySubtaskGroups) → identify `SubtaskGroupId`
2. Locate ticket: [POST /api/v1.0/tickets](#/Tickets/searchTickets) → extract `Items[].TicketId`
3. Remove group: [POST /api/v1.0/subtasks/group/remove/{subtaskGroupId}/{ticketId}](#/Tickets/removeSubtaskGroupFromTicket)

**Related Endpoints**
- [POST /api/v1.0/subtasks/group/ungroup/{subtaskGroupId}/{ticketId}](#/Tickets/ungroupSubtaskGroupFromTicket) – Ungroup without removing

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `subtask_group_id` | `subtaskGroupId` | `path` | `yes` | `str` | `-` | - |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `revert_subtask_completion`

Provenance: Golden OpenAPI contract

Operation ID: `revertSubtaskCompletion`

- Sync: `client.subtasks.revert_subtask_completion(ticket_subtask_id=..., timeout=None)`
- Async: `await client.subtasks.revert_subtask_completion(ticket_subtask_id=..., timeout=None)`
- Raw payload: `client.subtasks.revert_subtask_completion.raw(ticket_subtask_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/subtasks/{ticketSubtaskId}/revert`
- Source controller: `IncidentIQ API`

Revert subtask completion

Reverts a completed subtask back to an incomplete state. Use this when a subtask was marked complete prematurely or when additional work is discovered. The subtask returns to the assignee's work queue.

**Prerequisites**
1. **ticketSubtaskId** – Use [GET /api/v1.0/subtasks/{id}](#/Tickets/getSubtasksForTicket) to list subtasks and find completed items by checking `IsComplete: true`.

**Workflow Example**
1. List subtasks: [GET /api/v1.0/subtasks/{ticketId}](#/Tickets/getSubtasksForTicket) → identify completed subtask's `TicketSubtaskId`
2. Revert completion: [POST /api/v1.0/subtasks/{ticketSubtaskId}/revert](#/Tickets/revertSubtaskCompletion)
3. Verify status: [GET /api/v1.0/subtasks/{ticketId}](#/Tickets/getSubtasksForTicket) to confirm `IsComplete: false`

**Note**: Reverting completion may affect parent ticket workflow if subtask completion was a gate condition.

**Related Endpoints**
- [POST /api/v1.0/subtasks/{subtaskId}/complete](#/Tickets/completeSubtask) – Mark complete again
- [GET /api/v1.0/subtasks](#/Tickets/getUserSubtasks) – View your pending subtasks

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_subtask_id` | `ticketSubtaskId` | `path` | `yes` | `str` | `-` | Subtask identifier. |

#### Returns

- Typed call return: `TicketSubtaskItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketSubtaskItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `unassign_subtask`

Provenance: Golden OpenAPI contract

Operation ID: `unassignSubtask`

- Sync: `client.subtasks.unassign_subtask(ticket_subtask_id=..., timeout=None)`
- Async: `await client.subtasks.unassign_subtask(ticket_subtask_id=..., timeout=None)`
- Raw payload: `client.subtasks.unassign_subtask.raw(ticket_subtask_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/subtasks/{ticketSubtaskId}/unassign`
- Source controller: `IncidentIQ API`

Unassign subtask

Removes the current user assignment from a subtask, returning it to an unassigned state. The subtask remains on the parent ticket but will no longer appear in the previous assignee's work queue.

**Prerequisites**
1. **ticketSubtaskId** – Use [GET /api/v1.0/subtasks/{id}](#/Tickets/getSubtasksForTicket) to list subtasks and extract `TicketSubtaskId` for assigned items.

**Workflow Example**
1. List subtasks: [GET /api/v1.0/subtasks/{ticketId}](#/Tickets/getSubtasksForTicket) → identify assigned subtask's `TicketSubtaskId`
2. Unassign: [POST /api/v1.0/subtasks/{ticketSubtaskId}/unassign](#/Tickets/unassignSubtask)
3. (Optional) Reassign: Use [POST /api/v1.0/subtasks/{subtaskId}/assign/{userId}](#/Tickets/assignSubtask) to assign to another user

**Use Cases**: Useful when reassigning work, when the assignee is unavailable, or when the subtask needs to be picked up by the next available team member.

**Related Endpoints**
- [POST /api/v1.0/subtasks/{subtaskId}/assign/{userId}](#/Tickets/assignSubtask) – Assign to a new user
- [GET /api/v1.0/subtasks](#/Tickets/getUserSubtasks) – Check your remaining assignments

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_subtask_id` | `ticketSubtaskId` | `path` | `yes` | `str` | `-` | Subtask identifier. |

#### Returns

- Typed call return: `TicketSubtaskListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketSubtaskListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `ungroup_subtask_group_from_ticket`

Provenance: Golden OpenAPI contract

Operation ID: `ungroupSubtaskGroupFromTicket`

- Sync: `client.subtasks.ungroup_subtask_group_from_ticket(subtask_group_id=..., ticket_id=..., timeout=None)`
- Async: `await client.subtasks.ungroup_subtask_group_from_ticket(subtask_group_id=..., ticket_id=..., timeout=None)`
- Raw payload: `client.subtasks.ungroup_subtask_group_from_ticket.raw(subtask_group_id=..., ticket_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/subtasks/group/ungroup/{subtaskGroupId}/{ticketId}`
- Source controller: `IncidentIQ API`

Ungroup subtasks from group

Disassociates a ticket's subtasks from a subtask group without deleting the group or the subtasks themselves. The subtasks remain on the ticket but are no longer part of the grouped view.

**Prerequisites**
1. **subtaskGroupId** – Use [GET /api/v1.0/subtasks/my/groups](#/Tickets/getMySubtaskGroups) to list your subtask groups and extract `SubtaskGroupId`.
2. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) to find the ticket containing grouped subtasks.

**Workflow Example**
1. List groups: [GET /api/v1.0/subtasks/my/groups](#/Tickets/getMySubtaskGroups) → find the group containing the ticket
2. Locate ticket: [POST /api/v1.0/tickets](#/Tickets/searchTickets) → extract `Items[].TicketId`
3. Ungroup: [POST /api/v1.0/subtasks/group/ungroup/{subtaskGroupId}/{ticketId}](#/Tickets/ungroupSubtaskGroupFromTicket)

**Related Endpoints**
- [POST /api/v1.0/subtasks/group/assign](#/Tickets/assignSubtasksToGroup) – Add subtasks back to a group
- [POST /api/v1.0/subtasks/group/remove/{subtaskGroupId}/{ticketId}](#/Tickets/removeSubtaskGroupFromTicket) – Fully remove group

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `subtask_group_id` | `subtaskGroupId` | `path` | `yes` | `str` | `-` | - |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_subtask_group`

Provenance: Golden OpenAPI contract

Operation ID: `updateSubtaskGroup`

- Sync: `client.subtasks.update_subtask_group(subtask_group_id=..., body=..., timeout=None)`
- Async: `await client.subtasks.update_subtask_group(subtask_group_id=..., body=..., timeout=None)`
- Raw payload: `client.subtasks.update_subtask_group.raw(subtask_group_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/subtasks/group/{subtaskGroupId}`
- Source controller: `IncidentIQ API`

Update subtask group

Updates the properties of an existing subtask group, such as its name, description, or visibility settings. Changes apply immediately to all subtasks within the group.

**Prerequisites**
1. **subtaskGroupId** – Use [GET /api/v1.0/subtasks/my/groups](#/Tickets/getMySubtaskGroups) to list your groups and extract `SubtaskGroupId`.

**Workflow Example**
1. List groups: [GET /api/v1.0/subtasks/my/groups](#/Tickets/getMySubtaskGroups) → identify group to update
2. Update group: [POST /api/v1.0/subtasks/group/{subtaskGroupId}](#/Tickets/updateSubtaskGroup) with new properties
3. Verify: [GET /api/v1.0/subtasks/my/groups](#/Tickets/getMySubtaskGroups) to confirm changes

**Related Endpoints**
- [POST /api/v1.0/subtasks/group/new](#/Tickets/createSubtaskGroup) – Create a new group
- [DELETE /api/v1.0/subtasks/group/{subtaskGroupId}](#/Tickets/deleteSubtaskGroup) – Delete group
- [POST /api/v1.0/subtasks/group/assign](#/Tickets/assignSubtasksToGroup) – Assign subtasks to group

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `subtask_group_id` | `subtaskGroupId` | `path` | `yes` | `str` | `-` | Subtask group identifier. |
| `body` | `body` | `body` | `yes` | `SubtaskGroup` | `SubtaskGroup` | Subtask group payload. |

#### Returns

- Typed call return: `UpdateSubtaskGroupResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UpdateSubtaskGroupResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_subtask_sort_order`

Provenance: Golden OpenAPI contract

Operation ID: `updateSubtaskSortOrder`

- Sync: `client.subtasks.update_subtask_sort_order(body=..., timeout=None)`
- Async: `await client.subtasks.update_subtask_sort_order(body=..., timeout=None)`
- Raw payload: `client.subtasks.update_subtask_sort_order.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/subtasks/update-sort`
- Source controller: `IncidentIQ API`

Update subtask sort order

Updates the display sort order for subtasks within a ticket. Use this endpoint to reorder subtasks when presenting them in a checklist or workflow view. The sort order determines the sequence in which subtasks appear in the UI.

**Prerequisites**
1. **TicketSubtaskId** – Use [GET /api/v1.0/subtasks/{id}](#/Tickets/getSubtasksForTicket) to list subtasks and extract `TicketSubtaskId`.
2. **SortOrder** – Provide the new integer sort position in the request body.

**Workflow Example**
1. List subtasks: [GET /api/v1.0/subtasks/{ticketId}](#/Tickets/getSubtasksForTicket) → view current order and `TicketSubtaskId` values
2. Update order: [POST /api/v1.0/subtasks/update-sort](#/Tickets/updateSubtaskSortOrder) with subtask ID and new `SortOrder` value
3. Refresh list: [GET /api/v1.0/subtasks/{ticketId}](#/Tickets/getSubtasksForTicket) to verify new order

**Related Endpoints**
- [GET /api/v1.0/subtasks/{id}](#/Tickets/getSubtasksForTicket) – List subtasks
- [POST /api/v1.0/tickets/{ticketId}/subtasks/new](#/Tickets/createSubtask) – Create subtask with initial sort order

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `TicketSubtask` | `TicketSubtask` | Subtask payload containing the updated sort order. |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
