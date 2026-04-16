# `silver.rules` Namespace

Sync client access: `client.silver.rules`

Async client access: `client.silver.rules` with `await` on method calls.

These methods are Silver because Stoplight does not publish Golden contracts for them. They remain separate so undocumented behavior never overrides the documented SDK surface.

## Methods

### `get_log`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.rules.get_log(log_id=..., n_888891ac_91aa_e711_80c2_100dffa00003_id=..., s=..., timeout=None)`
- Async: `await client.silver.rules.get_log(log_id=..., n_888891ac_91aa_e711_80c2_100dffa00003_id=..., s=..., timeout=None)`
- Raw payload: `client.silver.rules.get_log.raw(log_id=..., n_888891ac_91aa_e711_80c2_100dffa00003_id=..., s=..., timeout=None)`
- HTTP route: `GET /api/v1.0/rules/logs/{log_id}/{n_888891ac_91aa_e711_80c2_100dffa00003_id}`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.rules`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `log_id` | `log_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |
| `n_888891ac_91aa_e711_80c2_100dffa00003_id` | `n_888891ac_91aa_e711_80c2_100dffa00003_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |
| `s` | `$s` | `query` | `yes` | `int` | Query parameter inferred from HAR observations for this undocumented Silver route. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_ids`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.rules.post_ids(json_body=..., timeout=None)`
- Async: `await client.silver.rules.post_ids(json_body=..., timeout=None)`
- Raw payload: `client.silver.rules.post_ids.raw(json_body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/rules/ids`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented POST route for `client.silver.rules`.

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
