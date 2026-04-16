# `silver.filters` Namespace

Sync client access: `client.silver.filters`

Async client access: `client.silver.filters` with `await` on method calls.

These methods are Silver because Stoplight does not publish Golden contracts for them. They remain separate so undocumented behavior never overrides the documented SDK surface.

## Methods

### `get_for__entitytype`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.filters.get_for__entitytype(entitytype_id=..., timeout=None)`
- Async: `await client.silver.filters.get_for__entitytype(entitytype_id=..., timeout=None)`
- Raw payload: `client.silver.filters.get_for__entitytype.raw(entitytype_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/filters/for/entitytype/{entitytype_id}`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.filters`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `entitytype_id` | `entitytype_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_set`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.filters.get_set(set_id=..., timeout=None)`
- Async: `await client.silver.filters.get_set(set_id=..., timeout=None)`
- Raw payload: `client.silver.filters.get_set.raw(set_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/filters/sets/{set_id}`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.filters`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `set_id` | `set_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_endpoint`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.filters.post_endpoint(json_body=..., timeout=None)`
- Async: `await client.silver.filters.post_endpoint(json_body=..., timeout=None)`
- Raw payload: `client.silver.filters.post_endpoint.raw(json_body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/filters`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented POST route for `client.silver.filters`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `json_body` | `json_body` | `body` | `yes` | `Mapping[str, Any]` | Request body observed in HAR traffic. The SDK uses a single `json_body` payload because the Silver route carries a complex undocumented schema. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---
