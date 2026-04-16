# `silver.api` Namespace

Sync client access: `client.silver.api`

Async client access: `client.silver.api` with `await` on method calls.

These methods are Silver because Stoplight does not publish Golden contracts for them. They remain separate so undocumented behavior never overrides the documented SDK surface.

## Methods

### `get_search_v2_expression`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.api.get_search_v2_expression(s=..., timeout=None)`
- Async: `await client.silver.api.get_search_v2_expression(s=..., timeout=None)`
- Raw payload: `client.silver.api.get_search_v2_expression.raw(s=..., timeout=None)`
- HTTP route: `GET /api/search/v2/expression`
- Observed in: `Chromebook-asset-actions.har`, `apple-asset-actions.har`

HAR-derived undocumented GET route for `client.silver.api`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `s` | `s` | `query` | `yes` | `str` | Query parameter inferred from HAR observations for this undocumented Silver route. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_search_v2_recent_user`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.api.post_search_v2_recent_user(search_expression_as_string=..., source=..., source_url=..., source_user_agent=..., user_id=..., timeout=None)`
- Async: `await client.silver.api.post_search_v2_recent_user(search_expression_as_string=..., source=..., source_url=..., source_user_agent=..., user_id=..., timeout=None)`
- Raw payload: `client.silver.api.post_search_v2_recent_user.raw(search_expression_as_string=..., source=..., source_url=..., source_user_agent=..., user_id=..., timeout=None)`
- HTTP route: `POST /api/search/v2/recent/user`
- Observed in: `Chromebook-asset-actions.har`, `apple-asset-actions.har`

HAR-derived undocumented POST route for `client.silver.api`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `search_expression_as_string` | `searchExpressionAsString` | `query` | `yes` | `str` | Query parameter inferred from HAR observations for this undocumented Silver route. |
| `source` | `source` | `query` | `yes` | `str` | Query parameter inferred from HAR observations for this undocumented Silver route. |
| `source_url` | `sourceUrl` | `query` | `yes` | `str` | Query parameter inferred from HAR observations for this undocumented Silver route. |
| `source_user_agent` | `sourceUserAgent` | `query` | `yes` | `str` | Query parameter inferred from HAR observations for this undocumented Silver route. |
| `user_id` | `userId` | `query` | `yes` | `str` | Query parameter inferred from HAR observations for this undocumented Silver route. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---
