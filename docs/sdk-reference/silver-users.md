# `silver.users` Namespace

Sync client access: `client.silver.users`

Async client access: `client.silver.users` with `await` on method calls.

These methods are Silver because the published contract does not document them directly, or because the SDK intentionally wraps a narrower Silver workflow around existing Golden operations. They remain separate so undocumented or convenience behavior never overrides the documented SDK surface.

## Methods

### `post_is_online_list`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.users.post_is_online_list(json_body=..., timeout=None)`
- Async: `await client.silver.users.post_is_online_list(json_body=..., timeout=None)`
- Raw payload: `client.silver.users.post_is_online_list.raw(json_body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/users/is-online/list`
- Observed in: `Chromebook-asset-actions.har`, `apple-asset-actions.har`, `demo.incidentiq.com.har`, `windows-asset-intune-actions.har`

HAR-derived undocumented POST route for `client.silver.users`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `json_body` | `json_body` | `body` | `yes` | `Mapping[str, Any] | list[Any] | str` | Request body observed in HAR traffic. The SDK keeps it as a single payload parameter because the undocumented route did not expose a stable object shape. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `update_user_view`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.users.update_user_view(view_id=..., json_body=..., timeout=None)`
- Async: `await client.silver.users.update_user_view(view_id=..., json_body=..., timeout=None)`
- Raw payload: `client.silver.users.update_user_view.raw(view_id=..., json_body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/users/views/{view_id}`
- Observed in: `migrated_from_golden_stoplight`

Migrated Silver route for POST /users/views/{ViewId}.

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.users.update_user_view` (operationId `View_UpdateUserView`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `view_id` | `ViewId` | `path` | `yes` | `str` | Path parameter migrated from the previous Golden SDK. |
| `json_body` | `UserView` | `body` | `yes` | `dict[str, Any] | list[Any]` | Body parameter migrated from the previous Golden SDK. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---
