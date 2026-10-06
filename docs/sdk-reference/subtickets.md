# `subtickets` Golden Namespace

Sync client access: `client.subtickets`

Async client access: `client.subtickets` with `await` on method calls.

These methods are Golden because they come from the bundled Incident IQ OpenAPI contract.

## Methods

### `delete_subticket`

Provenance: Golden OpenAPI contract

Operation ID: `deleteSubticket`

- Sync: `client.subtickets.delete_subticket(ticket_id=..., timeout=None)`
- Async: `await client.subtickets.delete_subticket(ticket_id=..., timeout=None)`
- Raw payload: `client.subtickets.delete_subticket.raw(ticket_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/subtickets/{ticketId}`
- Source controller: `IncidentIQ API`

Delete subticket

Permanently deletes a subticket (child ticket) from its parent ticket. Subtickets are full tickets linked to a parent for hierarchical work tracking. This operation removes the link and soft-deletes the subticket.

**Prerequisites**
1. **ticketId** – Use [POST /api/v1.0/tickets](#/Tickets/searchTickets) with `ShowChildTickets: true` to find subtickets. Extract `Items[].TicketId` from child tickets.

**Workflow Example**
1. Find subtickets: [POST /api/v1.0/tickets](#/Tickets/searchTickets) with `ShowChildTickets: true` → identify subticket's `TicketId`
2. Delete subticket: [DELETE /api/v1.0/subtickets/{ticketId}](#/Tickets/deleteSubticket)
3. Verify removal: [GET /api/v1.0/tickets/{parentTicketId}](#/Tickets/getTicket) to confirm child is removed

**Note**: Unlike subtasks, subtickets are full tickets with their own timeline and activities. Deletion is a soft-delete; administrators may be able to restore.

**Related Endpoints**
- [POST /api/v1.0/tickets](#/Tickets/searchTickets) – Search with ShowChildTickets filter
- [POST /api/v1.0/tickets/new](#/Tickets/createTicket) – Create tickets (including subtickets)

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticketId` | `path` | `yes` | `str` | `-` | Ticket identifier for the subticket to delete. |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
