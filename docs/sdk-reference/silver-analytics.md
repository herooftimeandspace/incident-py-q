# `silver.analytics` Namespace

Sync client access: `client.silver.analytics`

Async client access: `client.silver.analytics` with `await` on method calls.

These methods are Silver because Stoplight does not publish Golden contracts for them. They remain separate so undocumented behavior never overrides the documented SDK surface.

## Methods

### `get_agent_current_stats`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.analytics.get_agent_current_stats(timeout=None)`
- Async: `await client.silver.analytics.get_agent_current_stats(timeout=None)`
- Raw payload: `client.silver.analytics.get_agent_current_stats.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/analytics/agent-current-stats`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.analytics`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_agent_location_stats`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.analytics.get_agent_location_stats(timeout=None)`
- Async: `await client.silver.analytics.get_agent_location_stats(timeout=None)`
- Raw payload: `client.silver.analytics.get_agent_location_stats.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/analytics/agent-location-stats`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.analytics`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_asset_summary_stats`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.analytics.get_asset_summary_stats(asset_id=..., timeout=None)`
- Async: `await client.silver.analytics.get_asset_summary_stats(asset_id=..., timeout=None)`
- Raw payload: `client.silver.analytics.get_asset_summary_stats.raw(asset_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/analytics/asset/{asset_id}/summary-stats`
- Observed in: `Chromebook-asset-actions.har`, `apple-asset-actions.har`, `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.analytics`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `asset_id` | `asset_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_requestor_summary_stats`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.analytics.get_requestor_summary_stats(requestor_id=..., timeout=None)`
- Async: `await client.silver.analytics.get_requestor_summary_stats(requestor_id=..., timeout=None)`
- Raw payload: `client.silver.analytics.get_requestor_summary_stats.raw(requestor_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/analytics/requestor/{requestor_id}/summary-stats`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.analytics`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `requestor_id` | `requestor_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---
