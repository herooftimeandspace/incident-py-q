# `silver.assets` Namespace

Sync client access: `client.silver.assets`

Async client access: `client.silver.assets` with `await` on method calls.

These methods are Silver because Stoplight does not publish Golden contracts for them. They remain separate so undocumented behavior never overrides the documented SDK surface.

## Methods

### `get_asset_by_serial`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.assets.get_asset_by_serial(serial=..., timeout=None)`
- Async: `await client.silver.assets.get_asset_by_serial(serial=..., timeout=None)`
- Raw payload: `client.silver.assets.get_asset_by_serial.raw(serial=..., timeout=None)`
- HTTP route: `GET /assets/serial/{serial}`
- Observed in: `synthetic_required_route`

Silver path for asset lookup by serial number.

This route is treated as Silver because bundled Stoplight contracts do not define it. The SDK exposes it separately so Golden Stoplight methods remain the authoritative contract whenever they exist.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `serial` | `serial` | `path` | `yes` | `str` | Serial number path segment. This Silver route is added explicitly because it is known to exist even when the HAR does not capture it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_asset_files`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.assets.get_asset_files(asset_id=..., timeout=None)`
- Async: `await client.silver.assets.get_asset_files(asset_id=..., timeout=None)`
- Raw payload: `client.silver.assets.get_asset_files.raw(asset_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/assets/{asset_id}/files`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.assets`.

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

### `get_asset_verifications`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.assets.get_asset_verifications(asset_id=..., s=..., timeout=None)`
- Async: `await client.silver.assets.get_asset_verifications(asset_id=..., s=..., timeout=None)`
- Raw payload: `client.silver.assets.get_asset_verifications.raw(asset_id=..., s=..., timeout=None)`
- HTTP route: `GET /api/v1.0/assets/{asset_id}/verifications`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.assets`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `asset_id` | `asset_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |
| `s` | `$s` | `query` | `yes` | `int` | Query parameter inferred from HAR observations for this undocumented Silver route. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_stats_locations`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.assets.get_stats_locations(timeout=None)`
- Async: `await client.silver.assets.get_stats_locations(timeout=None)`
- Raw payload: `client.silver.assets.get_stats_locations.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/assets/stats/locations`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.assets`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_type`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.assets.get_type(type_id=..., timeout=None)`
- Async: `await client.silver.assets.get_type(type_id=..., timeout=None)`
- Raw payload: `client.silver.assets.get_type.raw(type_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/assets/types/{type_id}`
- Observed in: `apple-asset-actions.har`, `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.assets`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `type_id` | `type_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_checkouts_transactions_query_get`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.assets.post_checkouts_transactions_query_get(json_body=..., timeout=None)`
- Async: `await client.silver.assets.post_checkouts_transactions_query_get(json_body=..., timeout=None)`
- Raw payload: `client.silver.assets.post_checkouts_transactions_query_get.raw(json_body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/assets/checkouts/transactions/query/get`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented POST route for `client.silver.assets`.

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
