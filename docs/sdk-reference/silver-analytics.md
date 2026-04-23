# `silver.analytics` Namespace

Sync client access: `client.silver.analytics`

Async client access: `client.silver.analytics` with `await` on method calls.

These methods are Silver because Stoplight does not publish direct Golden contracts for them, or because the SDK intentionally wraps a narrower Silver workflow around existing Golden operations. They remain separate so undocumented or convenience behavior never overrides the documented SDK surface.

## Methods

### `get_agent_current_stats`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.analytics.get_agent_current_stats(timeout=None)`
- Async: `await client.silver.analytics.get_agent_current_stats(timeout=None)`
- Raw payload: `client.silver.analytics.get_agent_current_stats.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/analytics/agent-current-stats`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.analytics`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic. The April 22, 2026 resize HAR showed the upload plus a later `GET /img/...?...w=150&h=150`, but no separate persisted crop endpoint, so the SDK applies the avatar framing locally. It accepts common local raster image formats including JPG/JPEG, PNG, GIF, WEBP, and BMP. For non-square inputs it uses the largest centered square crop, then converts the result inside `client.silver.profiles.post_profile_picture(...)` to PNG and downscales it until the uploaded PNG payload stays at or below 1 MB.

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

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic. The April 22, 2026 resize HAR showed the upload plus a later `GET /img/...?...w=150&h=150`, but no separate persisted crop endpoint, so the SDK applies the avatar framing locally. For non-square inputs it uses the largest centered square crop, then converts the result inside `client.silver.profiles.post_profile_picture(...)` to PNG and downscales it until the uploaded PNG payload stays at or below 1 MB.

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
