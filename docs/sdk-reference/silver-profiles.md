# `silver.profiles` Namespace

Sync client access: `client.silver.profiles`

Async client access: `client.silver.profiles` with `await` on method calls.

These methods are Silver because Stoplight does not publish Golden contracts for them. They remain separate so undocumented behavior never overrides the documented SDK surface.

## Methods

### `post_profile_picture`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.profiles.post_profile_picture(user_id=..., file=..., timeout=None)`
- Async: `await client.silver.profiles.post_profile_picture(user_id=..., file=..., timeout=None)`
- Raw payload: `client.silver.profiles.post_profile_picture.raw(user_id=..., file=..., timeout=None)`
- HTTP route: `POST /api/v1.0/profiles/{user_id}/picture`
- Observed in: `iiq-profile-picture.har`

HAR-derived undocumented POST route for `client.silver.profiles`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `user_id` | `user_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |
| `file` | `File` | `file` | `yes` | `str | PathLike[str]` | Multipart file field inferred from HAR observations for this undocumented Silver route. Pass a local file path and the SDK uploads it as form-data. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---
