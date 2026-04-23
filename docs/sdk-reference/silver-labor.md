# `silver.labor` Namespace

Sync client access: `client.silver.labor`

Async client access: `client.silver.labor` with `await` on method calls.

These methods are Silver because Stoplight does not publish direct Golden contracts for them, or because the SDK intentionally wraps a narrower Silver workflow around existing Golden operations. They remain separate so undocumented or convenience behavior never overrides the documented SDK surface.

## Methods

### `get_rates_user`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.labor.get_rates_user(user_id=..., n_61757b5f_dd31_f111_8ef2_000d3a7cb1a2_id=..., n_88df910c_91aa_e711_80c2_0004ffa00010_id=..., timeout=None)`
- Async: `await client.silver.labor.get_rates_user(user_id=..., n_61757b5f_dd31_f111_8ef2_000d3a7cb1a2_id=..., n_88df910c_91aa_e711_80c2_0004ffa00010_id=..., timeout=None)`
- Raw payload: `client.silver.labor.get_rates_user.raw(user_id=..., n_61757b5f_dd31_f111_8ef2_000d3a7cb1a2_id=..., n_88df910c_91aa_e711_80c2_0004ffa00010_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/labor/rates/user/{user_id}/{n_61757b5f_dd31_f111_8ef2_000d3a7cb1a2_id}/{n_88df910c_91aa_e711_80c2_0004ffa00010_id}`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.labor`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `user_id` | `user_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |
| `n_61757b5f_dd31_f111_8ef2_000d3a7cb1a2_id` | `n_61757b5f_dd31_f111_8ef2_000d3a7cb1a2_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |
| `n_88df910c_91aa_e711_80c2_0004ffa00010_id` | `n_88df910c_91aa_e711_80c2_0004ffa00010_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_rates_user_2`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.labor.get_rates_user_2(user_id=..., timeout=None)`
- Async: `await client.silver.labor.get_rates_user_2(user_id=..., timeout=None)`
- Raw payload: `client.silver.labor.get_rates_user_2.raw(user_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/labor/rates/user/{user_id}`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.labor`.

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

### `post_types`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.labor.post_types(timeout=None)`
- Async: `await client.silver.labor.post_types(timeout=None)`
- Raw payload: `client.silver.labor.post_types.raw(timeout=None)`
- HTTP route: `POST /api/v1.0/labor/types`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented POST route for `client.silver.labor`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---
