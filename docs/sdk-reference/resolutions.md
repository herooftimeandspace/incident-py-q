# `resolutions` Golden Namespace

Sync client access: `client.resolutions`

Async client access: `client.resolutions` with `await` on method calls.

These methods are Golden because they come from the bundled Incident IQ OpenAPI contract.

## Methods

### `get_close_reason_types`

Provenance: Golden OpenAPI contract

Operation ID: `getCloseReasonTypes`

- Sync: `client.resolutions.get_close_reason_types(timeout=None)`
- Async: `await client.resolutions.get_close_reason_types(timeout=None)`
- Raw payload: `client.resolutions.get_close_reason_types.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/resolutions/close-reason-types`
- Source controller: `IncidentIQ API`

Get close reason types

Retrieves all available close reason types that can be selected when closing a ticket. Close reason types categorize the resolution outcome (e.g., Resolved, Duplicate, Won't Fix).

**Note**: This endpoint is part of the deprecated v1.0 API. The close reason types are used during ticket resolution workflows.

**Workflow Example**:
1. Call [GET /api/v1.0/resolutions/close-reason-types](#/Tickets/getCloseReasonTypes) to list available close reasons
2. Use the `CloseReasonTypeId` when closing a ticket via the ticket resolution endpoint

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `CloseReasonTypeListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CloseReasonTypeListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_resolution_action`

Provenance: Golden OpenAPI contract

Operation ID: `getResolutionAction`

- Sync: `client.resolutions.get_resolution_action(action_id=..., timeout=None)`
- Async: `await client.resolutions.get_resolution_action(action_id=..., timeout=None)`
- Raw payload: `client.resolutions.get_resolution_action.raw(action_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/resolutions/actions/{actionId}`
- Source controller: `IncidentIQ API`

Get resolution action

Retrieves detailed metadata for a single resolution action.

**Prerequisites**
1. **actionId** – Use [GET /api/v1.0/resolutions/actions](#/Resolution%20Actions/listResolutionActions) to list available actions and capture `Items[].ResolutionActionId`.

**Workflow Example**
1. List actions in scope: [GET /api/v1.0/resolutions/actions](#/Tickets/listResolutionActions).
2. Choose the desired action and copy `ResolutionActionId` from the response.
3. Call [GET /api/v1.0/resolutions/actions/{actionId}](#/Tickets/getResolutionAction) with the identifier to view full details.

**Minimal Required Fields**: actionId (path parameter).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `action_id` | `actionId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ResolutionActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ResolutionActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_resolution_actions`

Provenance: Golden OpenAPI contract

Operation ID: `listResolutionActions`

- Sync: `client.resolutions.list_resolution_actions(p=None, s=None, timeout=None)`
- Async: `await client.resolutions.list_resolution_actions(p=None, s=None, timeout=None)`
- Raw payload: `client.resolutions.list_resolution_actions.raw(p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v1.0/resolutions/actions`
- Source controller: `IncidentIQ API`

List resolution actions

Returns resolution actions available to the authenticated user.

**Prerequisites**
None. This endpoint relies on the authenticated session context and optional pagination controls.

**Workflow Example**
1. List available resolution actions: [GET /api/v1.0/resolutions/actions](#/Tickets/listResolutionActions).
2. Inspect a specific action: [GET /api/v1.0/resolutions/actions/{actionId}](#/Resolution%20Actions/getResolutionAction).

**Minimal Required Fields**: None. Use optional `$p` (page index) and `$s` (page size) query parameters to paginate results.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index to retrieve |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of records per page |

#### Returns

- Typed call return: `ResolutionActionListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ResolutionActionListResponse`
- Pagination helper: `client.resolutions.list_resolution_actions.iter_pages(start_page=1, page_size=100, max_pages=None, p=None, s=None, timeout=None)`

---
