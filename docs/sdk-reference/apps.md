# `apps` Silver Namespace

Primary sync access: `client.silver.apps`

Legacy sync alias: `client.apps`

Primary async access: `client.silver.apps` with `await` for async service methods.

These methods are Silver because Stoplight does not publish Golden contracts for them. The legacy `client.apps` alias remains available so existing integrations keep working while the undocumented nature of these routes is made explicit.

| Service | Manual Helpers | Generic Silver Methods | Access Path |
| --- | ---: | ---: | --- |
| `aeries_sis` | 0 | 7 | `client.silver.apps.aeries_sis` |
| `file_wave` | 0 | 2 | `client.silver.apps.file_wave` |
| `google_device_data` | 6 | 11 | `client.silver.apps.google_device_data` |
| `infinite_campus` | 0 | 1 | `client.silver.apps.infinite_campus` |
| `jamf` | 0 | 1 | `client.silver.apps.jamf` |
| `jamf_school` | 0 | 1 | `client.silver.apps.jamf_school` |
| `local_asset_manager` | 0 | 1 | `client.silver.apps.local_asset_manager` |
| `lock_n_charge2` | 0 | 3 | `client.silver.apps.lock_n_charge2` |
| `meraki_mdm` | 0 | 1 | `client.silver.apps.meraki_mdm` |
| `microsoft_intune` | 6 | 23 | `client.silver.apps.microsoft_intune` |
| `mosyle` | 4 | 0 | `client.silver.apps.mosyle` |
| `mosyle_manager` | 0 | 4 | `client.silver.apps.mosyle_manager` |
| `password_reset` | 0 | 1 | `client.silver.apps.password_reset` |
| `payments_fee_tracker` | 0 | 3 | `client.silver.apps.payments_fee_tracker` |
| `payments_in_touch` | 0 | 3 | `client.silver.apps.payments_in_touch` |
| `payments_my_school_bucks` | 0 | 3 | `client.silver.apps.payments_my_school_bucks` |
| `payments_square` | 0 | 3 | `client.silver.apps.payments_square` |
| `payments_stripe` | 0 | 3 | `client.silver.apps.payments_stripe` |
| `payments_vanco` | 0 | 3 | `client.silver.apps.payments_vanco` |
| `policy_agreements` | 0 | 1 | `client.silver.apps.policy_agreements` |
| `registry` | 2 | 0 | `client.silver.apps.registry` |
| `remote_beyond_trust` | 0 | 1 | `client.silver.apps.remote_beyond_trust` |
| `remote_chrome` | 0 | 1 | `client.silver.apps.remote_chrome` |
| `remote_team_viewer` | 0 | 1 | `client.silver.apps.remote_team_viewer` |
| `spare_pool_management` | 0 | 4 | `client.silver.apps.spare_pool_management` |
| `trafera` | 0 | 2 | `client.silver.apps.trafera` |
| `widgets` | 0 | 1 | `client.silver.apps.widgets` |
| `workspace_one` | 0 | 1 | `client.silver.apps.workspace_one` |

## `aeries_sis`

Aeries Sis service available at `client.silver.apps.aeries_sis`.

### `get_auth_oneroster_validate`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.aeries_sis.get_auth_oneroster_validate(timeout=None)`
- Async: `await client.silver.apps.aeries_sis.get_auth_oneroster_validate(timeout=None)`
- Raw payload: `client.silver.apps.aeries_sis.get_auth_oneroster_validate.raw(timeout=None)`
- HTTP route: `GET /apps/aeriesSis/api/aeriesSis/auth/oneroster/validate`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.apps.aeries_sis`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_settings_options`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.aeries_sis.get_settings_options(timeout=None)`
- Async: `await client.silver.apps.aeries_sis.get_settings_options(timeout=None)`
- Raw payload: `client.silver.apps.aeries_sis.get_settings_options.raw(timeout=None)`
- HTTP route: `GET /apps/aeriesSis/api/aeriesSis/settings/options`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.apps.aeries_sis`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_settings_options_sync`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.aeries_sis.get_settings_options_sync(timeout=None)`
- Async: `await client.silver.apps.aeries_sis.get_settings_options_sync(timeout=None)`
- Raw payload: `client.silver.apps.aeries_sis.get_settings_options_sync.raw(timeout=None)`
- HTTP route: `GET /apps/aeriesSis/api/aeriesSis/settings/options/sync`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.apps.aeries_sis`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_sync_history`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.aeries_sis.get_sync_history(timeout=None)`
- Async: `await client.silver.apps.aeries_sis.get_sync_history(timeout=None)`
- Raw payload: `client.silver.apps.aeries_sis.get_sync_history.raw(timeout=None)`
- HTTP route: `GET /apps/aeriesSis/api/aeriesSis/data/sync/history`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.apps.aeries_sis`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_sync_locations`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.aeries_sis.get_sync_locations(timeout=None)`
- Async: `await client.silver.apps.aeries_sis.get_sync_locations(timeout=None)`
- Raw payload: `client.silver.apps.aeries_sis.get_sync_locations.raw(timeout=None)`
- HTTP route: `GET /apps/aeriesSis/api/aeriesSis/sync/data/locations`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.apps.aeries_sis`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_sync_status_last`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.aeries_sis.get_sync_status_last(timeout=None)`
- Async: `await client.silver.apps.aeries_sis.get_sync_status_last(timeout=None)`
- Raw payload: `client.silver.apps.aeries_sis.get_sync_status_last.raw(timeout=None)`
- HTTP route: `GET /apps/aeriesSis/api/aeriesSis/sync/status/last`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.apps.aeries_sis`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_users_search`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.aeries_sis.post_users_search(limit=..., skip=..., sort=..., timeout=None)`
- Async: `await client.silver.apps.aeries_sis.post_users_search(limit=..., skip=..., sort=..., timeout=None)`
- Raw payload: `client.silver.apps.aeries_sis.post_users_search.raw(limit=..., skip=..., sort=..., timeout=None)`
- HTTP route: `POST /apps/aeriesSis/api/aeriesSis/data/users/search`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented POST route for `client.silver.apps.aeries_sis`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `limit` | `Limit` | `body` | `yes` | `int` | Body field inferred from HAR observations for this undocumented Silver route. |
| `skip` | `Skip` | `body` | `yes` | `int` | Body field inferred from HAR observations for this undocumented Silver route. |
| `sort` | `Sort` | `body` | `yes` | `str` | Body field inferred from HAR observations for this undocumented Silver route. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

## `file_wave`

File Wave service available at `client.silver.apps.file_wave`.

### `get_assets_usage`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.file_wave.get_assets_usage(usage_id=..., n_883d10f1_e4a0_4268_a319_3d36d1948030_id=..., timeout=None)`
- Async: `await client.silver.apps.file_wave.get_assets_usage(usage_id=..., n_883d10f1_e4a0_4268_a319_3d36d1948030_id=..., timeout=None)`
- Raw payload: `client.silver.apps.file_wave.get_assets_usage.raw(usage_id=..., n_883d10f1_e4a0_4268_a319_3d36d1948030_id=..., timeout=None)`
- HTTP route: `GET /apps/fileWave/api/fileWave/data/assets/usage/{usage_id}/{n_883d10f1_e4a0_4268_a319_3d36d1948030_id}`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.apps.file_wave`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `usage_id` | `usage_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |
| `n_883d10f1_e4a0_4268_a319_3d36d1948030_id` | `n_883d10f1_e4a0_4268_a319_3d36d1948030_id` | `path` | `yes` | `int` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_assets_lookup`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.file_wave.post_assets_lookup(asset_id=..., asset_tag=..., serial_number=..., timeout=None)`
- Async: `await client.silver.apps.file_wave.post_assets_lookup(asset_id=..., asset_tag=..., serial_number=..., timeout=None)`
- Raw payload: `client.silver.apps.file_wave.post_assets_lookup.raw(asset_id=..., asset_tag=..., serial_number=..., timeout=None)`
- HTTP route: `POST /apps/fileWave/api/fileWave/data/assets/lookup`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented POST route for `client.silver.apps.file_wave`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `asset_id` | `AssetId` | `body` | `yes` | `str` | Body field inferred from HAR observations for this undocumented Silver route. |
| `asset_tag` | `AssetTag` | `body` | `yes` | `str` | Body field inferred from HAR observations for this undocumented Silver route. |
| `serial_number` | `SerialNumber` | `body` | `yes` | `str` | Body field inferred from HAR observations for this undocumented Silver route. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

## `google_device_data`

Google Device Data service available at `client.silver.apps.google_device_data`.

### `lookup_asset`

Provenance: Silver manual helper

- Sync: `client.silver.apps.google_device_data.lookup_asset(asset_id=..., serial_number=..., asset_tag=None, query=None, skip=0, limit=1, timeout=None)`
- Async: `await client.silver.apps.google_device_data.lookup_asset(asset_id=..., serial_number=..., asset_tag=None, query=None, skip=0, limit=1, timeout=None)`
- Legacy alias: replace `client.silver.apps` with `client.apps` if you need the old access path.
- HTTP route: `POST /apps/googleDeviceData/api/googleDeviceData/data/assets/get-google-device`

Look up an Incident IQ asset against Google Device Data.

Posts the asset lookup payload to the Google Device Data endpoint.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `asset_id` | `AssetId` | `body` | `yes` | `str` | Incident IQ asset identifier. |
| `serial_number` | `SerialNumber` | `body` | `yes` | `str` | Serial number. |
| `asset_tag` | `AssetTag` | `body` | `no` | `str | None` | Optional asset tag. |
| `query` | `Query` | `body` | `no` | `str | None` | Optional search query. |
| `skip` | `Skip` | `body` | `no` | `int` | Result offset for the Google endpoint. |
| `limit` | `Limit` | `body` | `no` | `int` | Maximum results requested. |

#### Returns

- Typed call return: `AppLookupResponse | None`
- Raw payload return: `dict[str, Any] | None`
- Response model: `AppLookupResponse`

---

### `lookup_asset_raw`

Provenance: Silver manual helper

- Sync: `client.silver.apps.google_device_data.lookup_asset_raw(asset_id=..., serial_number=..., asset_tag=None, query=None, skip=0, limit=1, timeout=None)`
- Async: `await client.silver.apps.google_device_data.lookup_asset_raw(asset_id=..., serial_number=..., asset_tag=None, query=None, skip=0, limit=1, timeout=None)`
- Legacy alias: replace `client.silver.apps` with `client.apps` if you need the old access path.
- HTTP route: `POST /apps/googleDeviceData/api/googleDeviceData/data/assets/get-google-device`

Look up an asset against Google Device Data and return raw JSON.

Same request as `lookup_asset`, but returns validated raw JSON.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `asset_id` | `AssetId` | `body` | `yes` | `str` | Incident IQ asset identifier. |
| `serial_number` | `SerialNumber` | `body` | `yes` | `str` | Serial number. |
| `asset_tag` | `AssetTag` | `body` | `no` | `str | None` | Optional asset tag. |
| `query` | `Query` | `body` | `no` | `str | None` | Optional search query. |
| `skip` | `Skip` | `body` | `no` | `int` | Result offset for the Google endpoint. |
| `limit` | `Limit` | `body` | `no` | `int` | Maximum results requested. |

#### Returns

- Typed call return: `dict[str, Any] | None`
- Raw payload return: `dict[str, Any] | None`
- Response schema: `lookup_response`

---

### `list_remote_actions`

Provenance: Silver manual helper

- Sync: `client.silver.apps.google_device_data.list_remote_actions(timeout=None)`
- Async: `await client.silver.apps.google_device_data.list_remote_actions(timeout=None)`
- Legacy alias: replace `client.silver.apps` with `client.apps` if you need the old access path.
- HTTP route: `GET /apps/googleDeviceData/api/googleDeviceData/remoteactions`

List available Google Device Data remote actions.

Calls the Google Device Data remote actions endpoint and returns typed action records.

#### Parameters

This method does not define parameters.

#### Returns

- Typed call return: `list[AppRemoteAction]`
- Raw payload return: `list[dict[str, Any]]`
- Response model: `AppRemoteAction`

---

### `list_remote_actions_raw`

Provenance: Silver manual helper

- Sync: `client.silver.apps.google_device_data.list_remote_actions_raw(timeout=None)`
- Async: `await client.silver.apps.google_device_data.list_remote_actions_raw(timeout=None)`
- Legacy alias: replace `client.silver.apps` with `client.apps` if you need the old access path.
- HTTP route: `GET /apps/googleDeviceData/api/googleDeviceData/remoteactions`

List available Google Device Data remote actions and return raw JSON.

Same request as `list_remote_actions`, but returns validated raw JSON.

#### Parameters

This method does not define parameters.

#### Returns

- Typed call return: `list[dict[str, Any]]`
- Raw payload return: `list[dict[str, Any]]`
- Response schema: `remote_actions_response`

---

### `get_sync_options`

Provenance: Silver manual helper

- Sync: `client.silver.apps.google_device_data.get_sync_options(timeout=None)`
- Async: `await client.silver.apps.google_device_data.get_sync_options(timeout=None)`
- Legacy alias: replace `client.silver.apps` with `client.apps` if you need the old access path.
- HTTP route: `GET /apps/googleDeviceData/api/googleDeviceData/sync/options`

Fetch Google Device Data sync options.

Calls the sync options endpoint and returns the typed options model.

#### Parameters

This method does not define parameters.

#### Returns

- Typed call return: `GoogleSyncOptionsResponse`
- Raw payload return: `dict[str, Any] | None`
- Response model: `GoogleSyncOptionsResponse`

---

### `get_sync_options_raw`

Provenance: Silver manual helper

- Sync: `client.silver.apps.google_device_data.get_sync_options_raw(timeout=None)`
- Async: `await client.silver.apps.google_device_data.get_sync_options_raw(timeout=None)`
- Legacy alias: replace `client.silver.apps` with `client.apps` if you need the old access path.
- HTTP route: `GET /apps/googleDeviceData/api/googleDeviceData/sync/options`

Fetch Google Device Data sync options and return raw JSON.

Same request as `get_sync_options`, but returns validated raw JSON.

#### Parameters

This method does not define parameters.

#### Returns

- Typed call return: `dict[str, Any] | None`
- Raw payload return: `dict[str, Any] | None`
- Response schema: `google_sync_options_response`

---

### `get_assets_usage`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.google_device_data.get_assets_usage(usage_id=..., n_883d10f1_e4a0_4268_a319_3d36d1948030_id=..., timeout=None)`
- Async: `await client.silver.apps.google_device_data.get_assets_usage(usage_id=..., n_883d10f1_e4a0_4268_a319_3d36d1948030_id=..., timeout=None)`
- Raw payload: `client.silver.apps.google_device_data.get_assets_usage.raw(usage_id=..., n_883d10f1_e4a0_4268_a319_3d36d1948030_id=..., timeout=None)`
- HTTP route: `GET /apps/googleDeviceData/api/googleDeviceData/data/assets/usage/{usage_id}/{n_883d10f1_e4a0_4268_a319_3d36d1948030_id}`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.apps.google_device_data`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `usage_id` | `usage_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |
| `n_883d10f1_e4a0_4268_a319_3d36d1948030_id` | `n_883d10f1_e4a0_4268_a319_3d36d1948030_id` | `path` | `yes` | `int` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_assignment_suggestions`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.google_device_data.get_assignment_suggestions(timeout=None)`
- Async: `await client.silver.apps.google_device_data.get_assignment_suggestions(timeout=None)`
- Raw payload: `client.silver.apps.google_device_data.get_assignment_suggestions.raw(timeout=None)`
- HTTP route: `GET /apps/googleDeviceData/api/googleDeviceData/data/assignment/suggestions`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.apps.google_device_data`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_auth_token_check`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.google_device_data.get_auth_token_check(timeout=None)`
- Async: `await client.silver.apps.google_device_data.get_auth_token_check(timeout=None)`
- Raw payload: `client.silver.apps.google_device_data.get_auth_token_check.raw(timeout=None)`
- HTTP route: `GET /apps/googleDeviceData/api/auth/token-check`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.apps.google_device_data`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_models_distinct`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.google_device_data.get_models_distinct(timeout=None)`
- Async: `await client.silver.apps.google_device_data.get_models_distinct(timeout=None)`
- Raw payload: `client.silver.apps.google_device_data.get_models_distinct.raw(timeout=None)`
- HTTP route: `GET /apps/googleDeviceData/api/googleDeviceData/data/models/distinct`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.apps.google_device_data`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_status_last`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.google_device_data.get_status_last(google_device_data_key=..., timeout=None)`
- Async: `await client.silver.apps.google_device_data.get_status_last(google_device_data_key=..., timeout=None)`
- Raw payload: `client.silver.apps.google_device_data.get_status_last.raw(google_device_data_key=..., timeout=None)`
- HTTP route: `GET /apps/googleDeviceData/api/googleDeviceData/{google_device_data_key}/status/last`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.apps.google_device_data`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `google_device_data_key` | `google_device_data_key` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_sync_history`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.google_device_data.get_sync_history(timeout=None)`
- Async: `await client.silver.apps.google_device_data.get_sync_history(timeout=None)`
- Raw payload: `client.silver.apps.google_device_data.get_sync_history.raw(timeout=None)`
- HTTP route: `GET /apps/googleDeviceData/api/googleDeviceData/data/sync/history`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.apps.google_device_data`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_device_sync_push_schedule`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.google_device_data.post_device_sync_push_schedule(schedule_id=..., timeout=None)`
- Async: `await client.silver.apps.google_device_data.post_device_sync_push_schedule(schedule_id=..., timeout=None)`
- Raw payload: `client.silver.apps.google_device_data.post_device_sync_push_schedule.raw(schedule_id=..., timeout=None)`
- HTTP route: `POST /apps/googleDeviceData/api/googleDeviceData/device/sync/push/schedule/{schedule_id}`
- Observed in: `Chromebook-asset-actions.har`, `apple-asset-actions.har`

HAR-derived undocumented POST route for `client.silver.apps.google_device_data`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `schedule_id` | `schedule_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_jobs_logs`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.google_device_data.post_jobs_logs(job_id=..., limit=..., timeout=None)`
- Async: `await client.silver.apps.google_device_data.post_jobs_logs(job_id=..., limit=..., timeout=None)`
- Raw payload: `client.silver.apps.google_device_data.post_jobs_logs.raw(job_id=..., limit=..., timeout=None)`
- HTTP route: `POST /apps/googleDeviceData/api/googleDeviceData/data/jobs/{job_id}/logs`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented POST route for `client.silver.apps.google_device_data`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `job_id` | `job_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |
| `limit` | `Limit` | `body` | `yes` | `int` | Body field inferred from HAR observations for this undocumented Silver route. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_remoteactions_deprovision_device_execute`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.google_device_data.post_remoteactions_deprovision_device_execute(execute_id=..., json_body=..., timeout=None)`
- Async: `await client.silver.apps.google_device_data.post_remoteactions_deprovision_device_execute(execute_id=..., json_body=..., timeout=None)`
- Raw payload: `client.silver.apps.google_device_data.post_remoteactions_deprovision_device_execute.raw(execute_id=..., json_body=..., timeout=None)`
- HTTP route: `POST /apps/googleDeviceData/api/googleDeviceData/remoteactions/DeprovisionDevice/execute/{execute_id}`
- Observed in: `Chromebook-asset-actions.har`, `apple-asset-actions.har`

HAR-derived undocumented POST route for `client.silver.apps.google_device_data`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `execute_id` | `execute_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |
| `json_body` | `json_body` | `body` | `yes` | `Mapping[str, Any]` | Request body observed in HAR traffic. The SDK uses a single `json_body` payload because the Silver route carries a complex undocumented schema. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_remoteactions_disable_device_execute`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.google_device_data.post_remoteactions_disable_device_execute(execute_id=..., timeout=None)`
- Async: `await client.silver.apps.google_device_data.post_remoteactions_disable_device_execute(execute_id=..., timeout=None)`
- Raw payload: `client.silver.apps.google_device_data.post_remoteactions_disable_device_execute.raw(execute_id=..., timeout=None)`
- HTTP route: `POST /apps/googleDeviceData/api/googleDeviceData/remoteactions/DisableDevice/execute/{execute_id}`
- Observed in: `Chromebook-asset-actions.har`, `apple-asset-actions.har`

HAR-derived undocumented POST route for `client.silver.apps.google_device_data`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `execute_id` | `execute_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_remoteactions_wipe_device_execute`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.google_device_data.post_remoteactions_wipe_device_execute(execute_id=..., timeout=None)`
- Async: `await client.silver.apps.google_device_data.post_remoteactions_wipe_device_execute(execute_id=..., timeout=None)`
- Raw payload: `client.silver.apps.google_device_data.post_remoteactions_wipe_device_execute.raw(execute_id=..., timeout=None)`
- HTTP route: `POST /apps/googleDeviceData/api/googleDeviceData/remoteactions/WipeDevice/execute/{execute_id}`
- Observed in: `Chromebook-asset-actions.har`, `apple-asset-actions.har`

HAR-derived undocumented POST route for `client.silver.apps.google_device_data`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `execute_id` | `execute_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

## `infinite_campus`

Infinite Campus service available at `client.silver.apps.infinite_campus`.

### `get_settings_options_sync`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.infinite_campus.get_settings_options_sync(timeout=None)`
- Async: `await client.silver.apps.infinite_campus.get_settings_options_sync(timeout=None)`
- Raw payload: `client.silver.apps.infinite_campus.get_settings_options_sync.raw(timeout=None)`
- HTTP route: `GET /apps/infiniteCampus/api/infiniteCampus/settings/options/sync`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.apps.infinite_campus`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

## `jamf`

Jamf service available at `client.silver.apps.jamf`.

### `post_assets_lookup`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.jamf.post_assets_lookup(asset_id=..., asset_tag=..., serial_number=..., timeout=None)`
- Async: `await client.silver.apps.jamf.post_assets_lookup(asset_id=..., asset_tag=..., serial_number=..., timeout=None)`
- Raw payload: `client.silver.apps.jamf.post_assets_lookup.raw(asset_id=..., asset_tag=..., serial_number=..., timeout=None)`
- HTTP route: `POST /apps/jamf/api/jamf/data/assets/lookup`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented POST route for `client.silver.apps.jamf`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `asset_id` | `AssetId` | `body` | `yes` | `str` | Body field inferred from HAR observations for this undocumented Silver route. |
| `asset_tag` | `AssetTag` | `body` | `yes` | `str` | Body field inferred from HAR observations for this undocumented Silver route. |
| `serial_number` | `SerialNumber` | `body` | `yes` | `str` | Body field inferred from HAR observations for this undocumented Silver route. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

## `jamf_school`

Jamf School service available at `client.silver.apps.jamf_school`.

### `post_assets_lookup`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.jamf_school.post_assets_lookup(asset_tag=..., serial_number=..., timeout=None)`
- Async: `await client.silver.apps.jamf_school.post_assets_lookup(asset_tag=..., serial_number=..., timeout=None)`
- Raw payload: `client.silver.apps.jamf_school.post_assets_lookup.raw(asset_tag=..., serial_number=..., timeout=None)`
- HTTP route: `POST /apps/jamfSchool/api/jamfSchool/data/assets/lookup`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented POST route for `client.silver.apps.jamf_school`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `asset_tag` | `AssetTag` | `body` | `yes` | `str` | Body field inferred from HAR observations for this undocumented Silver route. |
| `serial_number` | `SerialNumber` | `body` | `yes` | `str` | Body field inferred from HAR observations for this undocumented Silver route. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

## `local_asset_manager`

Local Asset Manager service available at `client.silver.apps.local_asset_manager`.

### `post_microsoft_sccm_assets_lookup`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.local_asset_manager.post_microsoft_sccm_assets_lookup(asset_id=..., asset_tag=..., serial_number=..., timeout=None)`
- Async: `await client.silver.apps.local_asset_manager.post_microsoft_sccm_assets_lookup(asset_id=..., asset_tag=..., serial_number=..., timeout=None)`
- Raw payload: `client.silver.apps.local_asset_manager.post_microsoft_sccm_assets_lookup.raw(asset_id=..., asset_tag=..., serial_number=..., timeout=None)`
- HTTP route: `POST /apps/localAssetManager/api/microsoftSccm/data/assets/lookup`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented POST route for `client.silver.apps.local_asset_manager`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `asset_id` | `AssetId` | `body` | `yes` | `str` | Body field inferred from HAR observations for this undocumented Silver route. |
| `asset_tag` | `AssetTag` | `body` | `yes` | `str` | Body field inferred from HAR observations for this undocumented Silver route. |
| `serial_number` | `SerialNumber` | `body` | `yes` | `str` | Body field inferred from HAR observations for this undocumented Silver route. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

## `lock_n_charge2`

Lock N Charge2 service available at `client.silver.apps.lock_n_charge2`.

### `get_bays`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.lock_n_charge2.get_bays(refresh=..., timeout=None)`
- Async: `await client.silver.apps.lock_n_charge2.get_bays(refresh=..., timeout=None)`
- Raw payload: `client.silver.apps.lock_n_charge2.get_bays.raw(refresh=..., timeout=None)`
- HTTP route: `GET /apps/lockNCharge2/api/bays`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.apps.lock_n_charge2`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `refresh` | `refresh` | `query` | `yes` | `bool` | Query parameter inferred from HAR observations for this undocumented Silver route. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_stations`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.lock_n_charge2.get_stations(timeout=None)`
- Async: `await client.silver.apps.lock_n_charge2.get_stations(timeout=None)`
- Raw payload: `client.silver.apps.lock_n_charge2.get_stations.raw(timeout=None)`
- HTTP route: `GET /apps/lockNCharge2/api/stations`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.apps.lock_n_charge2`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_stations_licensed`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.lock_n_charge2.get_stations_licensed(timeout=None)`
- Async: `await client.silver.apps.lock_n_charge2.get_stations_licensed(timeout=None)`
- Raw payload: `client.silver.apps.lock_n_charge2.get_stations_licensed.raw(timeout=None)`
- HTTP route: `GET /apps/lockNCharge2/api/stations/licensed`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.apps.lock_n_charge2`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

## `meraki_mdm`

Meraki Mdm service available at `client.silver.apps.meraki_mdm`.

### `post_assets_lookup`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.meraki_mdm.post_assets_lookup(asset_id=..., asset_tag=..., serial_number=..., timeout=None)`
- Async: `await client.silver.apps.meraki_mdm.post_assets_lookup(asset_id=..., asset_tag=..., serial_number=..., timeout=None)`
- Raw payload: `client.silver.apps.meraki_mdm.post_assets_lookup.raw(asset_id=..., asset_tag=..., serial_number=..., timeout=None)`
- HTTP route: `POST /apps/merakiMdm/api/merakiMdm/data/assets/lookup`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented POST route for `client.silver.apps.meraki_mdm`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `asset_id` | `AssetId` | `body` | `yes` | `str` | Body field inferred from HAR observations for this undocumented Silver route. |
| `asset_tag` | `AssetTag` | `body` | `yes` | `str` | Body field inferred from HAR observations for this undocumented Silver route. |
| `serial_number` | `SerialNumber` | `body` | `yes` | `str` | Body field inferred from HAR observations for this undocumented Silver route. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

## `microsoft_intune`

Microsoft Intune service available at `client.silver.apps.microsoft_intune`.

### `lookup_asset`

Provenance: Silver manual helper

- Sync: `client.silver.apps.microsoft_intune.lookup_asset(asset_id=..., serial_number=..., asset_tag=None, timeout=None)`
- Async: `await client.silver.apps.microsoft_intune.lookup_asset(asset_id=..., serial_number=..., asset_tag=None, timeout=None)`
- Legacy alias: replace `client.silver.apps` with `client.apps` if you need the old access path.
- HTTP route: `POST /apps/microsoftIntune/api/microsoftIntune/data/assets/lookup`

Look up an Incident IQ asset against Microsoft Intune.

Posts the asset lookup payload to the Intune app endpoint and returns the typed lookup response when available.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `asset_id` | `AssetId` | `body` | `yes` | `str` | Incident IQ asset identifier. |
| `serial_number` | `SerialNumber` | `body` | `yes` | `str` | Serial number sent to the Intune lookup endpoint. |
| `asset_tag` | `AssetTag` | `body` | `no` | `str | None` | Optional asset tag. |

#### Returns

- Typed call return: `AppLookupResponse | None`
- Raw payload return: `dict[str, Any] | None`
- Response model: `AppLookupResponse`

---

### `lookup_asset_raw`

Provenance: Silver manual helper

- Sync: `client.silver.apps.microsoft_intune.lookup_asset_raw(asset_id=..., serial_number=..., asset_tag=None, timeout=None)`
- Async: `await client.silver.apps.microsoft_intune.lookup_asset_raw(asset_id=..., serial_number=..., asset_tag=None, timeout=None)`
- Legacy alias: replace `client.silver.apps` with `client.apps` if you need the old access path.
- HTTP route: `POST /apps/microsoftIntune/api/microsoftIntune/data/assets/lookup`

Look up an asset against Microsoft Intune and return raw JSON.

Same request as `lookup_asset`, but returns validated raw JSON.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `asset_id` | `AssetId` | `body` | `yes` | `str` | Incident IQ asset identifier. |
| `serial_number` | `SerialNumber` | `body` | `yes` | `str` | Serial number sent to the Intune lookup endpoint. |
| `asset_tag` | `AssetTag` | `body` | `no` | `str | None` | Optional asset tag. |

#### Returns

- Typed call return: `dict[str, Any] | None`
- Raw payload return: `dict[str, Any] | None`
- Response schema: `lookup_response`

---

### `list_remote_actions`

Provenance: Silver manual helper

- Sync: `client.silver.apps.microsoft_intune.list_remote_actions(timeout=None)`
- Async: `await client.silver.apps.microsoft_intune.list_remote_actions(timeout=None)`
- Legacy alias: replace `client.silver.apps` with `client.apps` if you need the old access path.
- HTTP route: `GET /apps/microsoftIntune/api/microsoftIntune/remoteactions`

List available Intune remote actions.

Calls the Intune remote actions endpoint and returns typed action records.

#### Parameters

This method does not define parameters.

#### Returns

- Typed call return: `list[AppRemoteAction]`
- Raw payload return: `list[dict[str, Any]]`
- Response model: `AppRemoteAction`

---

### `list_remote_actions_raw`

Provenance: Silver manual helper

- Sync: `client.silver.apps.microsoft_intune.list_remote_actions_raw(timeout=None)`
- Async: `await client.silver.apps.microsoft_intune.list_remote_actions_raw(timeout=None)`
- Legacy alias: replace `client.silver.apps` with `client.apps` if you need the old access path.
- HTTP route: `GET /apps/microsoftIntune/api/microsoftIntune/remoteactions`

List available Intune remote actions and return raw JSON.

Same request as `list_remote_actions`, but returns validated raw JSON.

#### Parameters

This method does not define parameters.

#### Returns

- Typed call return: `list[dict[str, Any]]`
- Raw payload return: `list[dict[str, Any]]`
- Response schema: `remote_actions_response`

---

### `classify_owner_type_from_lookup`

Provenance: Silver manual helper

- Sync: `client.silver.apps.microsoft_intune.classify_owner_type_from_lookup(lookup_response=..., expected_external_id=None)`
- Async: `client.silver.apps.microsoft_intune.classify_owner_type_from_lookup(lookup_response=..., expected_external_id=None)`
- Legacy alias: replace `client.silver.apps` with `client.apps` if you need the old access path.
- HTTP route: Utility helper (no HTTP request)

Classify Intune owner type from a lookup payload.

Utility helper that derives owner type and optional external-id match state from a lookup response; no HTTP request is made.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `lookup_response` | `lookup_response` | `python` | `yes` | `AppLookupResponse | Mapping[str, Any]` | Lookup payload or model to classify. |
| `expected_external_id` | `expected_external_id` | `python` | `no` | `str | None` | Optional external id used to flag mismatches. |

#### Returns

- Typed call return: `IntuneOwnerClassification`
- Raw payload return: `IntuneOwnerClassification`
- Response model: `IntuneOwnerClassification`

---

### `partition_assets_by_owner_type`

Provenance: Silver manual helper

- Sync: `client.silver.apps.microsoft_intune.partition_assets_by_owner_type(assets=..., timeout=None)`
- Async: `await client.silver.apps.microsoft_intune.partition_assets_by_owner_type(assets=..., timeout=None)`
- Legacy alias: replace `client.silver.apps` with `client.apps` if you need the old access path.
- HTTP route: Utility helper (no HTTP request)

Partition Intune-linked assets by owner type.

Utility helper that performs lookups as needed and groups assets into company, personal, and unknown partitions.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `assets` | `assets` | `python` | `yes` | `Sequence[Mapping[str, Any]]` | Asset payloads containing Intune app mapping data. |

#### Returns

- Typed call return: `IntuneOwnershipPartition`
- Raw payload return: `IntuneOwnershipPartition`
- Response model: `IntuneOwnershipPartition`

---

### `get_assets_usage`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.microsoft_intune.get_assets_usage(usage_id=..., n_883d10f1_e4a0_4268_a319_3d36d1948030_id=..., timeout=None)`
- Async: `await client.silver.apps.microsoft_intune.get_assets_usage(usage_id=..., n_883d10f1_e4a0_4268_a319_3d36d1948030_id=..., timeout=None)`
- Raw payload: `client.silver.apps.microsoft_intune.get_assets_usage.raw(usage_id=..., n_883d10f1_e4a0_4268_a319_3d36d1948030_id=..., timeout=None)`
- HTTP route: `GET /apps/microsoftIntune/api/microsoftIntune/data/assets/usage/{usage_id}/{n_883d10f1_e4a0_4268_a319_3d36d1948030_id}`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.apps.microsoft_intune`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `usage_id` | `usage_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |
| `n_883d10f1_e4a0_4268_a319_3d36d1948030_id` | `n_883d10f1_e4a0_4268_a319_3d36d1948030_id` | `path` | `yes` | `int` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_auth_token_check`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.microsoft_intune.get_auth_token_check(timeout=None)`
- Async: `await client.silver.apps.microsoft_intune.get_auth_token_check(timeout=None)`
- Raw payload: `client.silver.apps.microsoft_intune.get_auth_token_check.raw(timeout=None)`
- HTTP route: `GET /apps/microsoftIntune/api/microsoftIntune/auth/token-check`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.apps.microsoft_intune`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_sync_history`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.microsoft_intune.get_sync_history(timeout=None)`
- Async: `await client.silver.apps.microsoft_intune.get_sync_history(timeout=None)`
- Raw payload: `client.silver.apps.microsoft_intune.get_sync_history.raw(timeout=None)`
- HTTP route: `GET /apps/microsoftIntune/api/microsoftIntune/data/sync/history`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.apps.microsoft_intune`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_sync_options`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.microsoft_intune.get_sync_options(timeout=None)`
- Async: `await client.silver.apps.microsoft_intune.get_sync_options(timeout=None)`
- Raw payload: `client.silver.apps.microsoft_intune.get_sync_options.raw(timeout=None)`
- HTTP route: `GET /apps/microsoftIntune/api/microsoftIntune/sync/options`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.apps.microsoft_intune`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_sync_status_last`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.microsoft_intune.get_sync_status_last(timeout=None)`
- Async: `await client.silver.apps.microsoft_intune.get_sync_status_last(timeout=None)`
- Raw payload: `client.silver.apps.microsoft_intune.get_sync_status_last.raw(timeout=None)`
- HTTP route: `GET /apps/microsoftIntune/api/microsoftIntune/sync/status/last`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.apps.microsoft_intune`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_jobs_logs`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.microsoft_intune.post_jobs_logs(job_id=..., limit=..., timeout=None)`
- Async: `await client.silver.apps.microsoft_intune.post_jobs_logs(job_id=..., limit=..., timeout=None)`
- Raw payload: `client.silver.apps.microsoft_intune.post_jobs_logs.raw(job_id=..., limit=..., timeout=None)`
- HTTP route: `POST /apps/microsoftIntune/api/microsoftIntune/data/jobs/{job_id}/logs`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented POST route for `client.silver.apps.microsoft_intune`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `job_id` | `job_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |
| `limit` | `Limit` | `body` | `yes` | `int` | Body field inferred from HAR observations for this undocumented Silver route. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_remoteactions_clean_windows_device_execute`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.microsoft_intune.post_remoteactions_clean_windows_device_execute(execute_id=..., keep_user_data=..., timeout=None)`
- Async: `await client.silver.apps.microsoft_intune.post_remoteactions_clean_windows_device_execute(execute_id=..., keep_user_data=..., timeout=None)`
- Raw payload: `client.silver.apps.microsoft_intune.post_remoteactions_clean_windows_device_execute.raw(execute_id=..., keep_user_data=..., timeout=None)`
- HTTP route: `POST /apps/microsoftIntune/api/microsoftIntune/remoteactions/CleanWindowsDevice/execute/{execute_id}`
- Observed in: `Chromebook-asset-actions.har`, `apple-asset-actions.har`, `windows-asset-intune-actions.har`

HAR-derived undocumented POST route for `client.silver.apps.microsoft_intune`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `execute_id` | `execute_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |
| `keep_user_data` | `KeepUserData` | `body` | `yes` | `str` | Body field inferred from HAR observations for this undocumented Silver route. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_remoteactions_delete_user_from_shared_apple_device_execute`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.microsoft_intune.post_remoteactions_delete_user_from_shared_apple_device_execute(execute_id=..., user_principal_name=..., timeout=None)`
- Async: `await client.silver.apps.microsoft_intune.post_remoteactions_delete_user_from_shared_apple_device_execute(execute_id=..., user_principal_name=..., timeout=None)`
- Raw payload: `client.silver.apps.microsoft_intune.post_remoteactions_delete_user_from_shared_apple_device_execute.raw(execute_id=..., user_principal_name=..., timeout=None)`
- HTTP route: `POST /apps/microsoftIntune/api/microsoftIntune/remoteactions/DeleteUserFromSharedAppleDevice/execute/{execute_id}`
- Observed in: `Chromebook-asset-actions.har`, `apple-asset-actions.har`, `windows-asset-intune-actions.har`

HAR-derived undocumented POST route for `client.silver.apps.microsoft_intune`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `execute_id` | `execute_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |
| `user_principal_name` | `UserPrincipalName` | `body` | `yes` | `str` | Body field inferred from HAR observations for this undocumented Silver route. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_remoteactions_disable_lost_mode_execute`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.microsoft_intune.post_remoteactions_disable_lost_mode_execute(execute_id=..., timeout=None)`
- Async: `await client.silver.apps.microsoft_intune.post_remoteactions_disable_lost_mode_execute(execute_id=..., timeout=None)`
- Raw payload: `client.silver.apps.microsoft_intune.post_remoteactions_disable_lost_mode_execute.raw(execute_id=..., timeout=None)`
- HTTP route: `POST /apps/microsoftIntune/api/microsoftIntune/remoteactions/DisableLostMode/execute/{execute_id}`
- Observed in: `Chromebook-asset-actions.har`, `apple-asset-actions.har`, `windows-asset-intune-actions.har`

HAR-derived undocumented POST route for `client.silver.apps.microsoft_intune`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `execute_id` | `execute_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_remoteactions_locate_device_execute`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.microsoft_intune.post_remoteactions_locate_device_execute(execute_id=..., timeout=None)`
- Async: `await client.silver.apps.microsoft_intune.post_remoteactions_locate_device_execute(execute_id=..., timeout=None)`
- Raw payload: `client.silver.apps.microsoft_intune.post_remoteactions_locate_device_execute.raw(execute_id=..., timeout=None)`
- HTTP route: `POST /apps/microsoftIntune/api/microsoftIntune/remoteactions/LocateDevice/execute/{execute_id}`
- Observed in: `Chromebook-asset-actions.har`, `apple-asset-actions.har`, `windows-asset-intune-actions.har`

HAR-derived undocumented POST route for `client.silver.apps.microsoft_intune`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `execute_id` | `execute_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_remoteactions_logout_shared_apple_device_active_user_execute`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.microsoft_intune.post_remoteactions_logout_shared_apple_device_active_user_execute(execute_id=..., timeout=None)`
- Async: `await client.silver.apps.microsoft_intune.post_remoteactions_logout_shared_apple_device_active_user_execute(execute_id=..., timeout=None)`
- Raw payload: `client.silver.apps.microsoft_intune.post_remoteactions_logout_shared_apple_device_active_user_execute.raw(execute_id=..., timeout=None)`
- HTTP route: `POST /apps/microsoftIntune/api/microsoftIntune/remoteactions/LogoutSharedAppleDeviceActiveUser/execute/{execute_id}`
- Observed in: `Chromebook-asset-actions.har`, `apple-asset-actions.har`, `windows-asset-intune-actions.har`

HAR-derived undocumented POST route for `client.silver.apps.microsoft_intune`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `execute_id` | `execute_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_remoteactions_reboot_device_execute`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.microsoft_intune.post_remoteactions_reboot_device_execute(execute_id=..., timeout=None)`
- Async: `await client.silver.apps.microsoft_intune.post_remoteactions_reboot_device_execute(execute_id=..., timeout=None)`
- Raw payload: `client.silver.apps.microsoft_intune.post_remoteactions_reboot_device_execute.raw(execute_id=..., timeout=None)`
- HTTP route: `POST /apps/microsoftIntune/api/microsoftIntune/remoteactions/RebootDevice/execute/{execute_id}`
- Observed in: `Chromebook-asset-actions.har`, `apple-asset-actions.har`, `windows-asset-intune-actions.har`

HAR-derived undocumented POST route for `client.silver.apps.microsoft_intune`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `execute_id` | `execute_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_remoteactions_recover_passcode_execute`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.microsoft_intune.post_remoteactions_recover_passcode_execute(execute_id=..., timeout=None)`
- Async: `await client.silver.apps.microsoft_intune.post_remoteactions_recover_passcode_execute(execute_id=..., timeout=None)`
- Raw payload: `client.silver.apps.microsoft_intune.post_remoteactions_recover_passcode_execute.raw(execute_id=..., timeout=None)`
- HTTP route: `POST /apps/microsoftIntune/api/microsoftIntune/remoteactions/RecoverPasscode/execute/{execute_id}`
- Observed in: `Chromebook-asset-actions.har`, `apple-asset-actions.har`, `windows-asset-intune-actions.har`

HAR-derived undocumented POST route for `client.silver.apps.microsoft_intune`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `execute_id` | `execute_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_remoteactions_remote_lock_execute`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.microsoft_intune.post_remoteactions_remote_lock_execute(execute_id=..., timeout=None)`
- Async: `await client.silver.apps.microsoft_intune.post_remoteactions_remote_lock_execute(execute_id=..., timeout=None)`
- Raw payload: `client.silver.apps.microsoft_intune.post_remoteactions_remote_lock_execute.raw(execute_id=..., timeout=None)`
- HTTP route: `POST /apps/microsoftIntune/api/microsoftIntune/remoteactions/RemoteLock/execute/{execute_id}`
- Observed in: `Chromebook-asset-actions.har`, `apple-asset-actions.har`, `windows-asset-intune-actions.har`

HAR-derived undocumented POST route for `client.silver.apps.microsoft_intune`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `execute_id` | `execute_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_remoteactions_request_remote_assistance_execute`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.microsoft_intune.post_remoteactions_request_remote_assistance_execute(execute_id=..., timeout=None)`
- Async: `await client.silver.apps.microsoft_intune.post_remoteactions_request_remote_assistance_execute(execute_id=..., timeout=None)`
- Raw payload: `client.silver.apps.microsoft_intune.post_remoteactions_request_remote_assistance_execute.raw(execute_id=..., timeout=None)`
- HTTP route: `POST /apps/microsoftIntune/api/microsoftIntune/remoteactions/RequestRemoteAssistance/execute/{execute_id}`
- Observed in: `Chromebook-asset-actions.har`, `apple-asset-actions.har`, `windows-asset-intune-actions.har`

HAR-derived undocumented POST route for `client.silver.apps.microsoft_intune`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `execute_id` | `execute_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_remoteactions_reset_passcode_execute`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.microsoft_intune.post_remoteactions_reset_passcode_execute(execute_id=..., timeout=None)`
- Async: `await client.silver.apps.microsoft_intune.post_remoteactions_reset_passcode_execute(execute_id=..., timeout=None)`
- Raw payload: `client.silver.apps.microsoft_intune.post_remoteactions_reset_passcode_execute.raw(execute_id=..., timeout=None)`
- HTTP route: `POST /apps/microsoftIntune/api/microsoftIntune/remoteactions/ResetPasscode/execute/{execute_id}`
- Observed in: `Chromebook-asset-actions.har`, `apple-asset-actions.har`, `windows-asset-intune-actions.har`

HAR-derived undocumented POST route for `client.silver.apps.microsoft_intune`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `execute_id` | `execute_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_remoteactions_retire_device_execute`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.microsoft_intune.post_remoteactions_retire_device_execute(execute_id=..., timeout=None)`
- Async: `await client.silver.apps.microsoft_intune.post_remoteactions_retire_device_execute(execute_id=..., timeout=None)`
- Raw payload: `client.silver.apps.microsoft_intune.post_remoteactions_retire_device_execute.raw(execute_id=..., timeout=None)`
- HTTP route: `POST /apps/microsoftIntune/api/microsoftIntune/remoteactions/RetireDevice/execute/{execute_id}`
- Observed in: `Chromebook-asset-actions.har`, `apple-asset-actions.har`, `windows-asset-intune-actions.har`

HAR-derived undocumented POST route for `client.silver.apps.microsoft_intune`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `execute_id` | `execute_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_remoteactions_shut_down_execute`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.microsoft_intune.post_remoteactions_shut_down_execute(execute_id=..., timeout=None)`
- Async: `await client.silver.apps.microsoft_intune.post_remoteactions_shut_down_execute(execute_id=..., timeout=None)`
- Raw payload: `client.silver.apps.microsoft_intune.post_remoteactions_shut_down_execute.raw(execute_id=..., timeout=None)`
- HTTP route: `POST /apps/microsoftIntune/api/microsoftIntune/remoteactions/ShutDown/execute/{execute_id}`
- Observed in: `Chromebook-asset-actions.har`, `apple-asset-actions.har`, `windows-asset-intune-actions.har`

HAR-derived undocumented POST route for `client.silver.apps.microsoft_intune`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `execute_id` | `execute_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_remoteactions_sync_device_execute`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.microsoft_intune.post_remoteactions_sync_device_execute(execute_id=..., timeout=None)`
- Async: `await client.silver.apps.microsoft_intune.post_remoteactions_sync_device_execute(execute_id=..., timeout=None)`
- Raw payload: `client.silver.apps.microsoft_intune.post_remoteactions_sync_device_execute.raw(execute_id=..., timeout=None)`
- HTTP route: `POST /apps/microsoftIntune/api/microsoftIntune/remoteactions/SyncDevice/execute/{execute_id}`
- Observed in: `Chromebook-asset-actions.har`, `apple-asset-actions.har`, `windows-asset-intune-actions.har`

HAR-derived undocumented POST route for `client.silver.apps.microsoft_intune`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `execute_id` | `execute_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_remoteactions_update_windows_device_account_execute`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.microsoft_intune.post_remoteactions_update_windows_device_account_execute(execute_id=..., timeout=None)`
- Async: `await client.silver.apps.microsoft_intune.post_remoteactions_update_windows_device_account_execute(execute_id=..., timeout=None)`
- Raw payload: `client.silver.apps.microsoft_intune.post_remoteactions_update_windows_device_account_execute.raw(execute_id=..., timeout=None)`
- HTTP route: `POST /apps/microsoftIntune/api/microsoftIntune/remoteactions/UpdateWindowsDeviceAccount/execute/{execute_id}`
- Observed in: `Chromebook-asset-actions.har`, `apple-asset-actions.har`, `windows-asset-intune-actions.har`

HAR-derived undocumented POST route for `client.silver.apps.microsoft_intune`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `execute_id` | `execute_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_remoteactions_windows_defender_scan_execute`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.microsoft_intune.post_remoteactions_windows_defender_scan_execute(execute_id=..., quick_scan=..., timeout=None)`
- Async: `await client.silver.apps.microsoft_intune.post_remoteactions_windows_defender_scan_execute(execute_id=..., quick_scan=..., timeout=None)`
- Raw payload: `client.silver.apps.microsoft_intune.post_remoteactions_windows_defender_scan_execute.raw(execute_id=..., quick_scan=..., timeout=None)`
- HTTP route: `POST /apps/microsoftIntune/api/microsoftIntune/remoteactions/WindowsDefenderScan/execute/{execute_id}`
- Observed in: `Chromebook-asset-actions.har`, `apple-asset-actions.har`, `windows-asset-intune-actions.har`

HAR-derived undocumented POST route for `client.silver.apps.microsoft_intune`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `execute_id` | `execute_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |
| `quick_scan` | `QuickScan` | `body` | `yes` | `str` | Body field inferred from HAR observations for this undocumented Silver route. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_remoteactions_windows_defender_update_signatures_execute`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.microsoft_intune.post_remoteactions_windows_defender_update_signatures_execute(execute_id=..., timeout=None)`
- Async: `await client.silver.apps.microsoft_intune.post_remoteactions_windows_defender_update_signatures_execute(execute_id=..., timeout=None)`
- Raw payload: `client.silver.apps.microsoft_intune.post_remoteactions_windows_defender_update_signatures_execute.raw(execute_id=..., timeout=None)`
- HTTP route: `POST /apps/microsoftIntune/api/microsoftIntune/remoteactions/WindowsDefenderUpdateSignatures/execute/{execute_id}`
- Observed in: `Chromebook-asset-actions.har`, `apple-asset-actions.har`, `windows-asset-intune-actions.har`

HAR-derived undocumented POST route for `client.silver.apps.microsoft_intune`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `execute_id` | `execute_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_remoteactions_wipe_execute`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.microsoft_intune.post_remoteactions_wipe_execute(execute_id=..., keep_enrollment_data=..., keep_user_data=..., mac_os_unlock_code=..., timeout=None)`
- Async: `await client.silver.apps.microsoft_intune.post_remoteactions_wipe_execute(execute_id=..., keep_enrollment_data=..., keep_user_data=..., mac_os_unlock_code=..., timeout=None)`
- Raw payload: `client.silver.apps.microsoft_intune.post_remoteactions_wipe_execute.raw(execute_id=..., keep_enrollment_data=..., keep_user_data=..., mac_os_unlock_code=..., timeout=None)`
- HTTP route: `POST /apps/microsoftIntune/api/microsoftIntune/remoteactions/Wipe/execute/{execute_id}`
- Observed in: `Chromebook-asset-actions.har`, `apple-asset-actions.har`, `windows-asset-intune-actions.har`

HAR-derived undocumented POST route for `client.silver.apps.microsoft_intune`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `execute_id` | `execute_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |
| `keep_enrollment_data` | `KeepEnrollmentData` | `body` | `yes` | `str` | Body field inferred from HAR observations for this undocumented Silver route. |
| `keep_user_data` | `KeepUserData` | `body` | `yes` | `str` | Body field inferred from HAR observations for this undocumented Silver route. |
| `mac_os_unlock_code` | `MacOsUnlockCode` | `body` | `yes` | `int` | Body field inferred from HAR observations for this undocumented Silver route. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

## `mosyle`

Mosyle service available at `client.silver.apps.mosyle`.

### `lookup_asset`

Provenance: Silver manual helper

- Sync: `client.silver.apps.mosyle.lookup_asset(asset_id=..., serial_number=..., asset_tag=None, timeout=None)`
- Async: `await client.silver.apps.mosyle.lookup_asset(asset_id=..., serial_number=..., asset_tag=None, timeout=None)`
- Legacy alias: replace `client.silver.apps` with `client.apps` if you need the old access path.
- HTTP route: `POST /apps/mosyleManager/api/mosyleManager/data/assets/lookup`

Look up an Incident IQ asset against Mosyle.

Posts the asset lookup payload to the Mosyle app endpoint.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `asset_id` | `AssetId` | `body` | `yes` | `str` | Incident IQ asset identifier. |
| `serial_number` | `SerialNumber` | `body` | `yes` | `str` | Serial number. |
| `asset_tag` | `AssetTag` | `body` | `no` | `str | None` | Optional asset tag. |

#### Returns

- Typed call return: `AppLookupResponse | None`
- Raw payload return: `dict[str, Any] | None`
- Response model: `AppLookupResponse`

---

### `lookup_asset_raw`

Provenance: Silver manual helper

- Sync: `client.silver.apps.mosyle.lookup_asset_raw(asset_id=..., serial_number=..., asset_tag=None, timeout=None)`
- Async: `await client.silver.apps.mosyle.lookup_asset_raw(asset_id=..., serial_number=..., asset_tag=None, timeout=None)`
- Legacy alias: replace `client.silver.apps` with `client.apps` if you need the old access path.
- HTTP route: `POST /apps/mosyleManager/api/mosyleManager/data/assets/lookup`

Look up an asset against Mosyle and return raw JSON.

Same request as `lookup_asset`, but returns validated raw JSON.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `asset_id` | `AssetId` | `body` | `yes` | `str` | Incident IQ asset identifier. |
| `serial_number` | `SerialNumber` | `body` | `yes` | `str` | Serial number. |
| `asset_tag` | `AssetTag` | `body` | `no` | `str | None` | Optional asset tag. |

#### Returns

- Typed call return: `dict[str, Any] | None`
- Raw payload return: `dict[str, Any] | None`
- Response schema: `lookup_response`

---

### `list_remote_actions`

Provenance: Silver manual helper

- Sync: `client.silver.apps.mosyle.list_remote_actions(timeout=None)`
- Async: `await client.silver.apps.mosyle.list_remote_actions(timeout=None)`
- Legacy alias: replace `client.silver.apps` with `client.apps` if you need the old access path.
- HTTP route: `GET /apps/mosyleManager/api/mosyleManager/remoteactions`

List available Mosyle remote actions.

Calls the Mosyle remote actions endpoint and returns typed action records.

#### Parameters

This method does not define parameters.

#### Returns

- Typed call return: `list[AppRemoteAction]`
- Raw payload return: `list[dict[str, Any]]`
- Response model: `AppRemoteAction`

---

### `list_remote_actions_raw`

Provenance: Silver manual helper

- Sync: `client.silver.apps.mosyle.list_remote_actions_raw(timeout=None)`
- Async: `await client.silver.apps.mosyle.list_remote_actions_raw(timeout=None)`
- Legacy alias: replace `client.silver.apps` with `client.apps` if you need the old access path.
- HTTP route: `GET /apps/mosyleManager/api/mosyleManager/remoteactions`

List available Mosyle remote actions and return raw JSON.

Same request as `list_remote_actions`, but returns validated raw JSON.

#### Parameters

This method does not define parameters.

#### Returns

- Typed call return: `list[dict[str, Any]]`
- Raw payload return: `list[dict[str, Any]]`
- Response schema: `remote_actions_response`

---

## `mosyle_manager`

Mosyle Manager service available at `client.silver.apps.mosyle_manager`.

### `post_remoteactions_clear_commands_execute_mac268d3c3f_7745_5eb1_9299_a92e984d642d`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.mosyle_manager.post_remoteactions_clear_commands_execute_mac268d3c3f_7745_5eb1_9299_a92e984d642d(timeout=None)`
- Async: `await client.silver.apps.mosyle_manager.post_remoteactions_clear_commands_execute_mac268d3c3f_7745_5eb1_9299_a92e984d642d(timeout=None)`
- Raw payload: `client.silver.apps.mosyle_manager.post_remoteactions_clear_commands_execute_mac268d3c3f_7745_5eb1_9299_a92e984d642d.raw(timeout=None)`
- HTTP route: `POST /apps/mosyleManager/api/mosyleManager/remoteactions/ClearCommands/execute/mac268D3C3F-7745-5EB1-9299-A92E984D642D`
- Observed in: `apple-asset-actions.har`

HAR-derived undocumented POST route for `client.silver.apps.mosyle_manager`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_remoteactions_restart_device_execute_mac268d3c3f_7745_5eb1_9299_a92e984d642d`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.mosyle_manager.post_remoteactions_restart_device_execute_mac268d3c3f_7745_5eb1_9299_a92e984d642d(timeout=None)`
- Async: `await client.silver.apps.mosyle_manager.post_remoteactions_restart_device_execute_mac268d3c3f_7745_5eb1_9299_a92e984d642d(timeout=None)`
- Raw payload: `client.silver.apps.mosyle_manager.post_remoteactions_restart_device_execute_mac268d3c3f_7745_5eb1_9299_a92e984d642d.raw(timeout=None)`
- HTTP route: `POST /apps/mosyleManager/api/mosyleManager/remoteactions/RestartDevice/execute/mac268D3C3F-7745-5EB1-9299-A92E984D642D`
- Observed in: `apple-asset-actions.har`

HAR-derived undocumented POST route for `client.silver.apps.mosyle_manager`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_remoteactions_shutdown_device_execute_mac268d3c3f_7745_5eb1_9299_a92e984d642d`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.mosyle_manager.post_remoteactions_shutdown_device_execute_mac268d3c3f_7745_5eb1_9299_a92e984d642d(timeout=None)`
- Async: `await client.silver.apps.mosyle_manager.post_remoteactions_shutdown_device_execute_mac268d3c3f_7745_5eb1_9299_a92e984d642d(timeout=None)`
- Raw payload: `client.silver.apps.mosyle_manager.post_remoteactions_shutdown_device_execute_mac268d3c3f_7745_5eb1_9299_a92e984d642d.raw(timeout=None)`
- HTTP route: `POST /apps/mosyleManager/api/mosyleManager/remoteactions/ShutdownDevice/execute/mac268D3C3F-7745-5EB1-9299-A92E984D642D`
- Observed in: `apple-asset-actions.har`

HAR-derived undocumented POST route for `client.silver.apps.mosyle_manager`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_remoteactions_wipe_device_execute_mac268d3c3f_7745_5eb1_9299_a92e984d642d`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.mosyle_manager.post_remoteactions_wipe_device_execute_mac268d3c3f_7745_5eb1_9299_a92e984d642d(pin_code=..., timeout=None)`
- Async: `await client.silver.apps.mosyle_manager.post_remoteactions_wipe_device_execute_mac268d3c3f_7745_5eb1_9299_a92e984d642d(pin_code=..., timeout=None)`
- Raw payload: `client.silver.apps.mosyle_manager.post_remoteactions_wipe_device_execute_mac268d3c3f_7745_5eb1_9299_a92e984d642d.raw(pin_code=..., timeout=None)`
- HTTP route: `POST /apps/mosyleManager/api/mosyleManager/remoteactions/WipeDevice/execute/mac268D3C3F-7745-5EB1-9299-A92E984D642D`
- Observed in: `apple-asset-actions.har`

HAR-derived undocumented POST route for `client.silver.apps.mosyle_manager`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `pin_code` | `pin_code` | `body` | `yes` | `int` | Body field inferred from HAR observations for this undocumented Silver route. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

## `password_reset`

Password Reset service available at `client.silver.apps.password_reset`.

### `get_user_setup`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.password_reset.get_user_setup(user_id=..., timeout=None)`
- Async: `await client.silver.apps.password_reset.get_user_setup(user_id=..., timeout=None)`
- Raw payload: `client.silver.apps.password_reset.get_user_setup.raw(user_id=..., timeout=None)`
- HTTP route: `GET /apps/passwordReset/api/user/{user_id}/setup`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.apps.password_reset`.

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

## `payments_fee_tracker`

Payments Fee Tracker service available at `client.silver.apps.payments_fee_tracker`.

### `get_sync_options`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.payments_fee_tracker.get_sync_options(timeout=None)`
- Async: `await client.silver.apps.payments_fee_tracker.get_sync_options(timeout=None)`
- Raw payload: `client.silver.apps.payments_fee_tracker.get_sync_options.raw(timeout=None)`
- HTTP route: `GET /apps/paymentsFeeTracker/api/sync/options`
- Observed in: `Chromebook-asset-actions.har`, `apple-asset-actions.har`, `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.apps.payments_fee_tracker`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_line_item_types_search`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.payments_fee_tracker.post_line_item_types_search(timeout=None)`
- Async: `await client.silver.apps.payments_fee_tracker.post_line_item_types_search(timeout=None)`
- Raw payload: `client.silver.apps.payments_fee_tracker.post_line_item_types_search.raw(timeout=None)`
- HTTP route: `POST /apps/paymentsFeeTracker/api/data/line-item-types/search`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented POST route for `client.silver.apps.payments_fee_tracker`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_line_items_search`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.payments_fee_tracker.post_line_items_search(json_body=..., timeout=None)`
- Async: `await client.silver.apps.payments_fee_tracker.post_line_items_search(json_body=..., timeout=None)`
- Raw payload: `client.silver.apps.payments_fee_tracker.post_line_items_search.raw(json_body=..., timeout=None)`
- HTTP route: `POST /apps/paymentsFeeTracker/api/data/line-items/search`
- Observed in: `Chromebook-asset-actions.har`, `apple-asset-actions.har`, `demo.incidentiq.com.har`

HAR-derived undocumented POST route for `client.silver.apps.payments_fee_tracker`.

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

## `payments_in_touch`

Payments In Touch service available at `client.silver.apps.payments_in_touch`.

### `get_sync_options`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.payments_in_touch.get_sync_options(timeout=None)`
- Async: `await client.silver.apps.payments_in_touch.get_sync_options(timeout=None)`
- Raw payload: `client.silver.apps.payments_in_touch.get_sync_options.raw(timeout=None)`
- HTTP route: `GET /apps/paymentsInTouch/api/sync/options`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.apps.payments_in_touch`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_line_item_types_search`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.payments_in_touch.post_line_item_types_search(timeout=None)`
- Async: `await client.silver.apps.payments_in_touch.post_line_item_types_search(timeout=None)`
- Raw payload: `client.silver.apps.payments_in_touch.post_line_item_types_search.raw(timeout=None)`
- HTTP route: `POST /apps/paymentsInTouch/api/data/line-item-types/search`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented POST route for `client.silver.apps.payments_in_touch`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_line_items_search`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.payments_in_touch.post_line_items_search(json_body=..., timeout=None)`
- Async: `await client.silver.apps.payments_in_touch.post_line_items_search(json_body=..., timeout=None)`
- Raw payload: `client.silver.apps.payments_in_touch.post_line_items_search.raw(json_body=..., timeout=None)`
- HTTP route: `POST /apps/paymentsInTouch/api/data/line-items/search`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented POST route for `client.silver.apps.payments_in_touch`.

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

## `payments_my_school_bucks`

Payments My School Bucks service available at `client.silver.apps.payments_my_school_bucks`.

### `get_sync_options`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.payments_my_school_bucks.get_sync_options(timeout=None)`
- Async: `await client.silver.apps.payments_my_school_bucks.get_sync_options(timeout=None)`
- Raw payload: `client.silver.apps.payments_my_school_bucks.get_sync_options.raw(timeout=None)`
- HTTP route: `GET /apps/paymentsMySchoolBucks/api/sync/options`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.apps.payments_my_school_bucks`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_line_item_types_search`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.payments_my_school_bucks.post_line_item_types_search(timeout=None)`
- Async: `await client.silver.apps.payments_my_school_bucks.post_line_item_types_search(timeout=None)`
- Raw payload: `client.silver.apps.payments_my_school_bucks.post_line_item_types_search.raw(timeout=None)`
- HTTP route: `POST /apps/paymentsMySchoolBucks/api/data/line-item-types/search`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented POST route for `client.silver.apps.payments_my_school_bucks`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_line_items_search`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.payments_my_school_bucks.post_line_items_search(json_body=..., timeout=None)`
- Async: `await client.silver.apps.payments_my_school_bucks.post_line_items_search(json_body=..., timeout=None)`
- Raw payload: `client.silver.apps.payments_my_school_bucks.post_line_items_search.raw(json_body=..., timeout=None)`
- HTTP route: `POST /apps/paymentsMySchoolBucks/api/data/line-items/search`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented POST route for `client.silver.apps.payments_my_school_bucks`.

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

## `payments_square`

Payments Square service available at `client.silver.apps.payments_square`.

### `get_sync_options`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.payments_square.get_sync_options(timeout=None)`
- Async: `await client.silver.apps.payments_square.get_sync_options(timeout=None)`
- Raw payload: `client.silver.apps.payments_square.get_sync_options.raw(timeout=None)`
- HTTP route: `GET /apps/paymentsSquare/api/sync/options`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.apps.payments_square`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_line_item_types_search`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.payments_square.post_line_item_types_search(timeout=None)`
- Async: `await client.silver.apps.payments_square.post_line_item_types_search(timeout=None)`
- Raw payload: `client.silver.apps.payments_square.post_line_item_types_search.raw(timeout=None)`
- HTTP route: `POST /apps/paymentsSquare/api/data/line-item-types/search`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented POST route for `client.silver.apps.payments_square`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_line_items_search`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.payments_square.post_line_items_search(json_body=..., timeout=None)`
- Async: `await client.silver.apps.payments_square.post_line_items_search(json_body=..., timeout=None)`
- Raw payload: `client.silver.apps.payments_square.post_line_items_search.raw(json_body=..., timeout=None)`
- HTTP route: `POST /apps/paymentsSquare/api/data/line-items/search`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented POST route for `client.silver.apps.payments_square`.

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

## `payments_stripe`

Payments Stripe service available at `client.silver.apps.payments_stripe`.

### `get_sync_options`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.payments_stripe.get_sync_options(timeout=None)`
- Async: `await client.silver.apps.payments_stripe.get_sync_options(timeout=None)`
- Raw payload: `client.silver.apps.payments_stripe.get_sync_options.raw(timeout=None)`
- HTTP route: `GET /apps/paymentsStripe/api/sync/options`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.apps.payments_stripe`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_line_item_types_search`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.payments_stripe.post_line_item_types_search(timeout=None)`
- Async: `await client.silver.apps.payments_stripe.post_line_item_types_search(timeout=None)`
- Raw payload: `client.silver.apps.payments_stripe.post_line_item_types_search.raw(timeout=None)`
- HTTP route: `POST /apps/paymentsStripe/api/data/line-item-types/search`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented POST route for `client.silver.apps.payments_stripe`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_line_items_search`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.payments_stripe.post_line_items_search(json_body=..., timeout=None)`
- Async: `await client.silver.apps.payments_stripe.post_line_items_search(json_body=..., timeout=None)`
- Raw payload: `client.silver.apps.payments_stripe.post_line_items_search.raw(json_body=..., timeout=None)`
- HTTP route: `POST /apps/paymentsStripe/api/data/line-items/search`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented POST route for `client.silver.apps.payments_stripe`.

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

## `payments_vanco`

Payments Vanco service available at `client.silver.apps.payments_vanco`.

### `get_sync_options`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.payments_vanco.get_sync_options(timeout=None)`
- Async: `await client.silver.apps.payments_vanco.get_sync_options(timeout=None)`
- Raw payload: `client.silver.apps.payments_vanco.get_sync_options.raw(timeout=None)`
- HTTP route: `GET /apps/paymentsVanco/api/sync/options`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.apps.payments_vanco`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_line_item_types_search`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.payments_vanco.post_line_item_types_search(timeout=None)`
- Async: `await client.silver.apps.payments_vanco.post_line_item_types_search(timeout=None)`
- Raw payload: `client.silver.apps.payments_vanco.post_line_item_types_search.raw(timeout=None)`
- HTTP route: `POST /apps/paymentsVanco/api/data/line-item-types/search`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented POST route for `client.silver.apps.payments_vanco`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_line_items_search`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.payments_vanco.post_line_items_search(json_body=..., timeout=None)`
- Async: `await client.silver.apps.payments_vanco.post_line_items_search(json_body=..., timeout=None)`
- Raw payload: `client.silver.apps.payments_vanco.post_line_items_search.raw(json_body=..., timeout=None)`
- HTTP route: `POST /apps/paymentsVanco/api/data/line-items/search`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented POST route for `client.silver.apps.payments_vanco`.

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

## `policy_agreements`

Policy Agreements service available at `client.silver.apps.policy_agreements`.

### `get_users_acceptances_including_cleared`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.policy_agreements.get_users_acceptances_including_cleared(user_id=..., timeout=None)`
- Async: `await client.silver.apps.policy_agreements.get_users_acceptances_including_cleared(user_id=..., timeout=None)`
- Raw payload: `client.silver.apps.policy_agreements.get_users_acceptances_including_cleared.raw(user_id=..., timeout=None)`
- HTTP route: `GET /apps/policyAgreements/api/users/{user_id}/acceptances/including-cleared`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.apps.policy_agreements`.

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

## `registry`

App Registry service available at `client.silver.apps.registry`.

### `list_apps`

Provenance: Silver manual helper

- Sync: `client.silver.apps.registry.list_apps(include_hidden=False, timeout=None)`
- Async: `await client.silver.apps.registry.list_apps(include_hidden=False, timeout=None)`
- Legacy alias: replace `client.silver.apps` with `client.apps` if you need the old access path.
- HTTP route: `GET /api/v1.0/app-registry/apps/{include_hidden}`

List registered tenant apps.

Calls the tenant app registry endpoint and returns the typed registry response envelope.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `include_hidden` | `include_hidden` | `path` | `no` | `bool` | Whether to include hidden app registrations. |

#### Returns

- Typed call return: `AppRegistryResponse`
- Raw payload return: `dict[str, Any] | None`
- Response model: `AppRegistryResponse`

---

### `list_apps_raw`

Provenance: Silver manual helper

- Sync: `client.silver.apps.registry.list_apps_raw(include_hidden=False, timeout=None)`
- Async: `await client.silver.apps.registry.list_apps_raw(include_hidden=False, timeout=None)`
- Legacy alias: replace `client.silver.apps` with `client.apps` if you need the old access path.
- HTTP route: `GET /api/v1.0/app-registry/apps/{include_hidden}`

List registered tenant apps and return raw JSON.

Same request as `list_apps`, but returns validated raw JSON.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `include_hidden` | `include_hidden` | `path` | `no` | `bool` | Whether to include hidden app registrations. |

#### Returns

- Typed call return: `dict[str, Any] | None`
- Raw payload return: `dict[str, Any] | None`
- Response schema: `registry_response`

---

## `remote_beyond_trust`

Remote Beyond Trust service available at `client.silver.apps.remote_beyond_trust`.

### `get_db_bb6cece8_e4f4_e511_a789_005056bb000e_statu`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.remote_beyond_trust.get_db_bb6cece8_e4f4_e511_a789_005056bb000e_statu(bb6cece8_e4f4_e511_a789_005056bb000e_statu_id=..., timeout=None)`
- Async: `await client.silver.apps.remote_beyond_trust.get_db_bb6cece8_e4f4_e511_a789_005056bb000e_statu(bb6cece8_e4f4_e511_a789_005056bb000e_statu_id=..., timeout=None)`
- Raw payload: `client.silver.apps.remote_beyond_trust.get_db_bb6cece8_e4f4_e511_a789_005056bb000e_statu.raw(bb6cece8_e4f4_e511_a789_005056bb000e_statu_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/apps/remoteBeyondTrust/db/bb6cece8-e4f4-e511-a789-005056bb000e-Status/{bb6cece8_e4f4_e511_a789_005056bb000e_statu_id}`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.apps.remote_beyond_trust`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `bb6cece8_e4f4_e511_a789_005056bb000e_statu_id` | `bb6cece8_e4f4_e511_a789_005056bb000e_statu_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

## `remote_chrome`

Remote Chrome service available at `client.silver.apps.remote_chrome`.

### `get_db_bb6cece8_e4f4_e511_a789_005056bb000e_statu`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.remote_chrome.get_db_bb6cece8_e4f4_e511_a789_005056bb000e_statu(bb6cece8_e4f4_e511_a789_005056bb000e_statu_id=..., timeout=None)`
- Async: `await client.silver.apps.remote_chrome.get_db_bb6cece8_e4f4_e511_a789_005056bb000e_statu(bb6cece8_e4f4_e511_a789_005056bb000e_statu_id=..., timeout=None)`
- Raw payload: `client.silver.apps.remote_chrome.get_db_bb6cece8_e4f4_e511_a789_005056bb000e_statu.raw(bb6cece8_e4f4_e511_a789_005056bb000e_statu_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/apps/remoteChrome/db/bb6cece8-e4f4-e511-a789-005056bb000e-Status/{bb6cece8_e4f4_e511_a789_005056bb000e_statu_id}`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.apps.remote_chrome`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `bb6cece8_e4f4_e511_a789_005056bb000e_statu_id` | `bb6cece8_e4f4_e511_a789_005056bb000e_statu_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

## `remote_team_viewer`

Remote Team Viewer service available at `client.silver.apps.remote_team_viewer`.

### `get_db_bb6cece8_e4f4_e511_a789_005056bb000e_statu`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.remote_team_viewer.get_db_bb6cece8_e4f4_e511_a789_005056bb000e_statu(bb6cece8_e4f4_e511_a789_005056bb000e_statu_id=..., timeout=None)`
- Async: `await client.silver.apps.remote_team_viewer.get_db_bb6cece8_e4f4_e511_a789_005056bb000e_statu(bb6cece8_e4f4_e511_a789_005056bb000e_statu_id=..., timeout=None)`
- Raw payload: `client.silver.apps.remote_team_viewer.get_db_bb6cece8_e4f4_e511_a789_005056bb000e_statu.raw(bb6cece8_e4f4_e511_a789_005056bb000e_statu_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/apps/remoteTeamViewer/db/bb6cece8-e4f4-e511-a789-005056bb000e-Status/{bb6cece8_e4f4_e511_a789_005056bb000e_statu_id}`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.apps.remote_team_viewer`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `bb6cece8_e4f4_e511_a789_005056bb000e_statu_id` | `bb6cece8_e4f4_e511_a789_005056bb000e_statu_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

## `spare_pool_management`

Spare Pool Management service available at `client.silver.apps.spare_pool_management`.

### `get_pool_stats_today`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.spare_pool_management.get_pool_stats_today(timeout=None)`
- Async: `await client.silver.apps.spare_pool_management.get_pool_stats_today(timeout=None)`
- Raw payload: `client.silver.apps.spare_pool_management.get_pool_stats_today.raw(timeout=None)`
- HTTP route: `GET /apps/sparePoolManagement/api/pool/stats/today`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.apps.spare_pool_management`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_ticket_pool`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.spare_pool_management.get_ticket_pool(ticket_id=..., pool_id=..., timeout=None)`
- Async: `await client.silver.apps.spare_pool_management.get_ticket_pool(ticket_id=..., pool_id=..., timeout=None)`
- Raw payload: `client.silver.apps.spare_pool_management.get_ticket_pool.raw(ticket_id=..., pool_id=..., timeout=None)`
- HTTP route: `GET /apps/sparePoolManagement/api/ticket/{ticket_id}/pools/{pool_id}`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.apps.spare_pool_management`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticket_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |
| `pool_id` | `pool_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_assets_deployments`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.spare_pool_management.post_assets_deployments(json_body=..., timeout=None)`
- Async: `await client.silver.apps.spare_pool_management.post_assets_deployments(json_body=..., timeout=None)`
- Raw payload: `client.silver.apps.spare_pool_management.post_assets_deployments.raw(json_body=..., timeout=None)`
- HTTP route: `POST /apps/sparePoolManagement/api/assets/deployments`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented POST route for `client.silver.apps.spare_pool_management`.

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

### `post_groups`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.spare_pool_management.post_groups(timeout=None)`
- Async: `await client.silver.apps.spare_pool_management.post_groups(timeout=None)`
- Raw payload: `client.silver.apps.spare_pool_management.post_groups.raw(timeout=None)`
- HTTP route: `POST /apps/sparePoolManagement/api/groups`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented POST route for `client.silver.apps.spare_pool_management`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

## `trafera`

Trafera service available at `client.silver.apps.trafera`.

### `get_parts`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.trafera.get_parts(timeout=None)`
- Async: `await client.silver.apps.trafera.get_parts(timeout=None)`
- Raw payload: `client.silver.apps.trafera.get_parts.raw(timeout=None)`
- HTTP route: `GET /apps/trafera/api/parts`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.apps.trafera`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_settings_options`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.trafera.get_settings_options(timeout=None)`
- Async: `await client.silver.apps.trafera.get_settings_options(timeout=None)`
- Raw payload: `client.silver.apps.trafera.get_settings_options.raw(timeout=None)`
- HTTP route: `GET /apps/trafera/api/settings/options`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.apps.trafera`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

## `widgets`

Widgets service available at `client.silver.apps.widgets`.

### `get_endpoint`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.widgets.get_endpoint(widget_id=..., timeout=None)`
- Async: `await client.silver.apps.widgets.get_endpoint(widget_id=..., timeout=None)`
- Raw payload: `client.silver.apps.widgets.get_endpoint.raw(widget_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/apps/widgets/{widget_id}`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.apps.widgets`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `widget_id` | `widget_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

## `workspace_one`

Workspace One service available at `client.silver.apps.workspace_one`.

### `post_assets_lookup`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.apps.workspace_one.post_assets_lookup(asset_id=..., asset_tag=..., serial_number=..., timeout=None)`
- Async: `await client.silver.apps.workspace_one.post_assets_lookup(asset_id=..., asset_tag=..., serial_number=..., timeout=None)`
- Raw payload: `client.silver.apps.workspace_one.post_assets_lookup.raw(asset_id=..., asset_tag=..., serial_number=..., timeout=None)`
- HTTP route: `POST /apps/workspaceOne/api/workspaceOne/data/assets/lookup`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented POST route for `client.silver.apps.workspace_one`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `asset_id` | `AssetId` | `body` | `yes` | `str` | Body field inferred from HAR observations for this undocumented Silver route. |
| `asset_tag` | `AssetTag` | `body` | `yes` | `str` | Body field inferred from HAR observations for this undocumented Silver route. |
| `serial_number` | `SerialNumber` | `body` | `yes` | `str` | Body field inferred from HAR observations for this undocumented Silver route. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---
