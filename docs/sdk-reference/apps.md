# `apps` Namespace

Sync client access: `client.apps`

Async client access: `client.apps` with `await` for async service methods.

These methods cover the HAR-derived app-path APIs that are not part of the schema-driven controller SDK surface.

| Service | Methods | Access Path |
| --- | ---: | --- |
| `registry` | 2 | `client.apps.registry` |
| `microsoft_intune` | 6 | `client.apps.microsoft_intune` |
| `mosyle` | 4 | `client.apps.mosyle` |
| `google_device_data` | 6 | `client.apps.google_device_data` |

## `registry`

App Registry service available at `client.apps.registry`.

### `list_apps`

- Sync: `client.apps.registry.list_apps(include_hidden=False, timeout=None)`
- Async: `await client.apps.registry.list_apps(include_hidden=False, timeout=None)`
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

- Sync: `client.apps.registry.list_apps_raw(include_hidden=False, timeout=None)`
- Async: `await client.apps.registry.list_apps_raw(include_hidden=False, timeout=None)`
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

## `microsoft_intune`

Microsoft Intune service available at `client.apps.microsoft_intune`.

### `lookup_asset`

- Sync: `client.apps.microsoft_intune.lookup_asset(asset_id=..., serial_number=..., asset_tag=None, timeout=None)`
- Async: `await client.apps.microsoft_intune.lookup_asset(asset_id=..., serial_number=..., asset_tag=None, timeout=None)`
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

- Sync: `client.apps.microsoft_intune.lookup_asset_raw(asset_id=..., serial_number=..., asset_tag=None, timeout=None)`
- Async: `await client.apps.microsoft_intune.lookup_asset_raw(asset_id=..., serial_number=..., asset_tag=None, timeout=None)`
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

- Sync: `client.apps.microsoft_intune.list_remote_actions(timeout=None)`
- Async: `await client.apps.microsoft_intune.list_remote_actions(timeout=None)`
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

- Sync: `client.apps.microsoft_intune.list_remote_actions_raw(timeout=None)`
- Async: `await client.apps.microsoft_intune.list_remote_actions_raw(timeout=None)`
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

- Sync: `client.apps.microsoft_intune.classify_owner_type_from_lookup(lookup_response=..., expected_external_id=None)`
- Async: `client.apps.microsoft_intune.classify_owner_type_from_lookup(lookup_response=..., expected_external_id=None)`
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

- Sync: `client.apps.microsoft_intune.partition_assets_by_owner_type(assets=..., timeout=None)`
- Async: `await client.apps.microsoft_intune.partition_assets_by_owner_type(assets=..., timeout=None)`
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

## `mosyle`

Mosyle service available at `client.apps.mosyle`.

### `lookup_asset`

- Sync: `client.apps.mosyle.lookup_asset(asset_id=..., serial_number=..., asset_tag=None, timeout=None)`
- Async: `await client.apps.mosyle.lookup_asset(asset_id=..., serial_number=..., asset_tag=None, timeout=None)`
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

- Sync: `client.apps.mosyle.lookup_asset_raw(asset_id=..., serial_number=..., asset_tag=None, timeout=None)`
- Async: `await client.apps.mosyle.lookup_asset_raw(asset_id=..., serial_number=..., asset_tag=None, timeout=None)`
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

- Sync: `client.apps.mosyle.list_remote_actions(timeout=None)`
- Async: `await client.apps.mosyle.list_remote_actions(timeout=None)`
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

- Sync: `client.apps.mosyle.list_remote_actions_raw(timeout=None)`
- Async: `await client.apps.mosyle.list_remote_actions_raw(timeout=None)`
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

## `google_device_data`

Google Device Data service available at `client.apps.google_device_data`.

### `lookup_asset`

- Sync: `client.apps.google_device_data.lookup_asset(asset_id=..., serial_number=..., asset_tag=None, query=None, skip=0, limit=1, timeout=None)`
- Async: `await client.apps.google_device_data.lookup_asset(asset_id=..., serial_number=..., asset_tag=None, query=None, skip=0, limit=1, timeout=None)`
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

- Sync: `client.apps.google_device_data.lookup_asset_raw(asset_id=..., serial_number=..., asset_tag=None, query=None, skip=0, limit=1, timeout=None)`
- Async: `await client.apps.google_device_data.lookup_asset_raw(asset_id=..., serial_number=..., asset_tag=None, query=None, skip=0, limit=1, timeout=None)`
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

- Sync: `client.apps.google_device_data.list_remote_actions(timeout=None)`
- Async: `await client.apps.google_device_data.list_remote_actions(timeout=None)`
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

- Sync: `client.apps.google_device_data.list_remote_actions_raw(timeout=None)`
- Async: `await client.apps.google_device_data.list_remote_actions_raw(timeout=None)`
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

- Sync: `client.apps.google_device_data.get_sync_options(timeout=None)`
- Async: `await client.apps.google_device_data.get_sync_options(timeout=None)`
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

- Sync: `client.apps.google_device_data.get_sync_options_raw(timeout=None)`
- Async: `await client.apps.google_device_data.get_sync_options_raw(timeout=None)`
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
