# `silver.custom_fields` Namespace

Sync client access: `client.silver.custom_fields`

Async client access: `client.silver.custom_fields` with `await` on method calls.

These methods are Silver because Stoplight does not publish Golden contracts for them. They remain separate so undocumented behavior never overrides the documented SDK surface.

## Methods

### `post_for__asset`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.custom_fields.post_for__asset(s=..., json_body=..., timeout=None)`
- Async: `await client.silver.custom_fields.post_for__asset(s=..., json_body=..., timeout=None)`
- Raw payload: `client.silver.custom_fields.post_for__asset.raw(s=..., json_body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/custom-fields/for/asset`
- Observed in: `Chromebook-asset-actions.har`, `apple-asset-actions.har`, `demo.incidentiq.com.har`

HAR-derived undocumented POST route for `client.silver.custom_fields`.

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

### `post_for__ticket`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.custom_fields.post_for__ticket(s=..., json_body=..., timeout=None)`
- Async: `await client.silver.custom_fields.post_for__ticket(s=..., json_body=..., timeout=None)`
- Raw payload: `client.silver.custom_fields.post_for__ticket.raw(s=..., json_body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/custom-fields/for/ticket`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented POST route for `client.silver.custom_fields`.

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

### `post_for__user`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.custom_fields.post_for__user(s=..., json_body=..., timeout=None)`
- Async: `await client.silver.custom_fields.post_for__user(s=..., json_body=..., timeout=None)`
- Raw payload: `client.silver.custom_fields.post_for__user.raw(s=..., json_body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/custom-fields/for/user`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented POST route for `client.silver.custom_fields`.

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
