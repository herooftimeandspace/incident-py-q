# `shortcuts` Golden Namespace

Sync client access: `client.shortcuts`

Async client access: `client.shortcuts` with `await` on method calls.

These methods are Golden because they come from the bundled Incident IQ OpenAPI contract.

## Methods

### `get_shortcut`

Provenance: Golden OpenAPI contract

Operation ID: `getShortcut`

- Sync: `client.shortcuts.get_shortcut(shortcut_id=..., timeout=None)`
- Async: `await client.shortcuts.get_shortcut(shortcut_id=..., timeout=None)`
- Raw payload: `client.shortcuts.get_shortcut.raw(shortcut_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/shortcuts/{ShortcutId}`
- Source controller: `IncidentIQ API`

Get shortcut by ID

Retrieves detailed information about a specific rule-based shortcut by its unique identifier.

**Prerequisites**
1. **ShortcutId** - Use [GET /api/v1.0/users/shortcuts/available](#/Users/getAvailableShortcuts) to list shortcuts. Extract `Items[].ShortcutId`.

**Workflow Example**
1. List shortcuts: [GET /api/v1.0/users/shortcuts/available](#/Users/getAvailableShortcuts) → extract ShortcutId
2. Get details: GET this endpoint with ShortcutId

**Response Fields**: ShortcutId, OwnerId, Name, Scope, RuleId, ForEntityTypeId, Snippet, FilterSetId

**Notes**: Returns 404 if the shortcut doesn't exist or the user doesn't have access.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `shortcut_id` | `ShortcutId` | `path` | `yes` | `str` | `-` | UUID of the shortcut to retrieve |

#### Returns

- Typed call return: `ShortcutGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ShortcutGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
