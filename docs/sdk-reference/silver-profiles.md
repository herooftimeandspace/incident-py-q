# `silver.profiles` Namespace

Sync client access: `client.silver.profiles`

Async client access: `client.silver.profiles` with `await` on method calls.

These methods are Silver because Stoplight does not publish direct Golden contracts for them, or because the SDK intentionally wraps a narrower Silver workflow around existing Golden operations. They remain separate so undocumented or convenience behavior never overrides the documented SDK surface.

## Methods

### `post_profile_picture`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.profiles.post_profile_picture(user_id=..., file=..., wait_for_consistency=False, consistency_timeout=10.0, consistency_poll_interval=1.0, timeout=None)`
- Async: `await client.silver.profiles.post_profile_picture(user_id=..., file=..., wait_for_consistency=False, consistency_timeout=10.0, consistency_poll_interval=1.0, timeout=None)`
- Raw payload: `client.silver.profiles.post_profile_picture.raw(user_id=..., file=..., wait_for_consistency=False, consistency_timeout=10.0, consistency_poll_interval=1.0, timeout=None)`
- HTTP route: `POST /api/v1.0/profiles/{user_id}/picture`
- Observed in: `iiq-profile-picture.har`

HAR-derived undocumented POST route for `client.silver.profiles`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic. The April 22, 2026 resize HAR showed the upload plus a later `GET /img/...?...w=150&h=150`, but no separate persisted crop endpoint, so the SDK applies the avatar framing locally. For non-square inputs it uses the largest centered square crop, then converts the result inside `client.silver.profiles.post_profile_picture(...)` to PNG and downscales it until the uploaded PNG payload stays at or below 1 MB.

The SDK prepares the avatar locally before upload because the HAR showed the file upload and a later rendered image fetch, but not a separate persisted crop API. That is why `post_profile_picture(...)` center-crops non-square images, converts the image to PNG inside the method, and enforces the 1 MB size cap before any bytes are sent.

The upload call can optionally validate tenant readback with `wait_for_consistency=True`. This is opt-in because some tenants accept the write first and update `PhotoId` a moment later. Use the validation knobs when your workflow needs confirmation that the new picture is visible through user readback before you continue.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `user_id` | `user_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |
| `file` | `File` | `file` | `yes` | `str | PathLike[str]` | Multipart image field inferred from HAR observations for this undocumented Silver route. Pass a local image path in a common raster format such as JPG/JPEG, PNG, GIF, WEBP, or BMP and the SDK uses the largest centered square crop for non-square inputs, converts it inside `client.silver.profiles.post_profile_picture(...)` to PNG, downscales it if needed, and uploads a PNG no larger than 1 MB. |

#### Examples

- Fast path: `client.silver.profiles.post_profile_picture(user_id=..., file=..., timeout=None)`
- Validated path: `client.silver.profiles.post_profile_picture(user_id=..., file=..., wait_for_consistency=True, consistency_timeout=10.0, consistency_poll_interval=1.0, timeout=None)`
- Async validated path: `await client.silver.profiles.post_profile_picture(user_id=..., file=..., wait_for_consistency=True, consistency_timeout=10.0, consistency_poll_interval=1.0, timeout=None)`

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `remove_profile_picture`

Provenance: Silver manual helper

- Sync: `client.silver.profiles.remove_profile_picture(user_id=..., wait_for_consistency=False, consistency_timeout=10.0, consistency_poll_interval=1.0, timeout=None)`
- Async: `await client.silver.profiles.remove_profile_picture(user_id=..., wait_for_consistency=False, consistency_timeout=10.0, consistency_poll_interval=1.0, timeout=None)`
- Raw payload: No public `.raw(...)`; `.raw(...)` is used only as an internal fallback if the typed Golden route path cannot carry the required payload shape.
- Backing routes: `GET /api/v1.0/users/{user_id}`, `POST /api/v1.0/users/{user_id}`

Remove a user's profile picture by clearing `PhotoId` through the documented Golden user update route.

This helper exists on the Silver surface because Incident IQ exposes profile-picture removal as a user update workflow rather than as its own published profile route. The helper first tries the typed Golden `users.get_user(...)` method, then falls back to the explicit `/api/v1.0/users/{user_id}` JSON route if the tenant does not return usable user JSON through the Golden path. It builds the smallest proven-safe `UpdateUserRequest`: the required update fields copied exactly from the fetched user plus `PhotoId = None`. It intentionally does not repost the full user object, so unrelated user fields are not cleared by omission. Validation is opt-in because some tenants reflect `PhotoId` changes a moment after the write call returns. `.raw(...)` stays an internal fallback of last resort, not the normal compatibility path.

#### Examples

- Fast path: `client.silver.profiles.remove_profile_picture(user_id=..., timeout=None)`
- Validated path: `client.silver.profiles.remove_profile_picture(user_id=..., wait_for_consistency=True, consistency_timeout=10.0, consistency_poll_interval=1.0, timeout=None)`
- Async validated path: `await client.silver.profiles.remove_profile_picture(user_id=..., wait_for_consistency=True, consistency_timeout=10.0, consistency_poll_interval=1.0, timeout=None)`

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `user_id` | `user_id` | `path` | `yes` | `str` | User identifier whose profile picture should be removed. |
| `wait_for_consistency` | `wait_for_consistency` | `client` | `no` | `bool` | When `True`, poll user readback until `PhotoId` becomes `None` or raise `TimeoutError` if the tenant does not converge in time. |
| `consistency_timeout` | `consistency_timeout` | `client` | `no` | `float` | Maximum number of seconds to wait for readback convergence when `wait_for_consistency=True`. |
| `consistency_poll_interval` | `consistency_poll_interval` | `client` | `no` | `float` | Polling interval in seconds between user readback checks when `wait_for_consistency=True`. |

#### Returns

- Typed call return: `ItemUpdateResponseOfUser`
- Internal raw fallback return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemUpdateResponseOfUser`

---
