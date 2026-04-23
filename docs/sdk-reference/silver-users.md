# `silver.users` Namespace

Sync client access: `client.silver.users`

Async client access: `client.silver.users` with `await` on method calls.

These methods are Silver because Stoplight does not publish direct Golden contracts for them, or because the SDK intentionally wraps a narrower Silver workflow around existing Golden operations. They remain separate so undocumented or convenience behavior never overrides the documented SDK surface.

## Methods

### `get_my_shortcuts`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.users.get_my_shortcuts(timeout=None)`
- Async: `await client.silver.users.get_my_shortcuts(timeout=None)`
- Raw payload: `client.silver.users.get_my_shortcuts.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/users/my/shortcuts`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.users`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_shortcuts_available`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.users.get_shortcuts_available(timeout=None)`
- Async: `await client.silver.users.get_shortcuts_available(timeout=None)`
- Raw payload: `client.silver.users.get_shortcuts_available.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/users/shortcuts/available`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.users`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_simple`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.users.get_simple(simple_id=..., timeout=None)`
- Async: `await client.silver.users.get_simple(simple_id=..., timeout=None)`
- Raw payload: `client.silver.users.get_simple.raw(simple_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/users/simple/{simple_id}`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.users`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `simple_id` | `simple_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_user_options`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.users.get_user_options(user_id=..., timeout=None)`
- Async: `await client.silver.users.get_user_options(user_id=..., timeout=None)`
- Raw payload: `client.silver.users.get_user_options.raw(user_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/users/{user_id}/options`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.users`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `user_id` | `user_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_user_relationships`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.users.get_user_relationships(user_id=..., timeout=None)`
- Async: `await client.silver.users.get_user_relationships(user_id=..., timeout=None)`
- Raw payload: `client.silver.users.get_user_relationships.raw(user_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/users/{user_id}/relationships`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.users`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `user_id` | `user_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_user_rooms`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.users.get_user_rooms(user_id=..., s=..., timeout=None)`
- Async: `await client.silver.users.get_user_rooms(user_id=..., s=..., timeout=None)`
- Raw payload: `client.silver.users.get_user_rooms.raw(user_id=..., s=..., timeout=None)`
- HTTP route: `GET /api/v1.0/users/{user_id}/rooms`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.users`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `user_id` | `user_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |
| `s` | `$s` | `query` | `yes` | `int` | Query parameter inferred from HAR observations for this undocumented Silver route. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

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
