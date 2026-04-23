# `silver.resolutions` Namespace

Sync client access: `client.silver.resolutions`

Async client access: `client.silver.resolutions` with `await` on method calls.

These methods are Silver because Stoplight does not publish direct Golden contracts for them, or because the SDK intentionally wraps a narrower Silver workflow around existing Golden operations. They remain separate so undocumented or convenience behavior never overrides the documented SDK surface.

## Methods

### `post_actions`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.resolutions.post_actions(s=..., site_scope=..., timeout=None)`
- Async: `await client.silver.resolutions.post_actions(s=..., site_scope=..., timeout=None)`
- Raw payload: `client.silver.resolutions.post_actions.raw(s=..., site_scope=..., timeout=None)`
- HTTP route: `POST /api/v1.0/resolutions/actions`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented POST route for `client.silver.resolutions`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic. The SDK normalizes the supplied image to PNG and downscales it as needed so the uploaded PNG payload stays at or below 1 MB.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `s` | `$s` | `query` | `yes` | `int` | Query parameter inferred from HAR observations for this undocumented Silver route. |
| `site_scope` | `SiteScope` | `body` | `yes` | `str` | Body field inferred from HAR observations for this undocumented Silver route. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_actions_for__issue_link`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.resolutions.post_actions_for__issue_link(s=..., json_body=..., timeout=None)`
- Async: `await client.silver.resolutions.post_actions_for__issue_link(s=..., json_body=..., timeout=None)`
- Raw payload: `client.silver.resolutions.post_actions_for__issue_link.raw(s=..., json_body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/resolutions/actions/for/issue/link`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented POST route for `client.silver.resolutions`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `s` | `$s` | `query` | `yes` | `int` | Query parameter inferred from HAR observations for this undocumented Silver route. |
| `json_body` | `json_body` | `body` | `yes` | `Mapping[str, Any]` | Request body observed in HAR traffic. The SDK uses a single `json_body` payload because the Silver route carries a complex undocumented schema. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---
