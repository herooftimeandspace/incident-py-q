# `silver.settings` Namespace

Sync client access: `client.silver.settings`

Async client access: `client.silver.settings` with `await` on method calls.

These methods are Silver because Stoplight does not publish direct Golden contracts for them, or because the SDK intentionally wraps a narrower Silver workflow around existing Golden operations. They remain separate so undocumented or convenience behavior never overrides the documented SDK surface.

## Methods

### `get_apps__remote_beyond_trust__remote_connection_url`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.settings.get_apps__remote_beyond_trust__remote_connection_url(timeout=None)`
- Async: `await client.silver.settings.get_apps__remote_beyond_trust__remote_connection_url(timeout=None)`
- Raw payload: `client.silver.settings.get_apps__remote_beyond_trust__remote_connection_url.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/settings/Apps.RemoteBeyondTrust.RemoteConnectionUrl`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.settings`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_apps__remote_team_viewer__api_token`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.settings.get_apps__remote_team_viewer__api_token(timeout=None)`
- Async: `await client.silver.settings.get_apps__remote_team_viewer__api_token(timeout=None)`
- Raw payload: `client.silver.settings.get_apps__remote_team_viewer__api_token.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/settings/Apps.RemoteTeamViewer.ApiToken`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.settings`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_apps__remote_team_viewer__download_link`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.settings.get_apps__remote_team_viewer__download_link(timeout=None)`
- Async: `await client.silver.settings.get_apps__remote_team_viewer__download_link(timeout=None)`
- Raw payload: `client.silver.settings.get_apps__remote_team_viewer__download_link.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/settings/Apps.RemoteTeamViewer.DownloadLink`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.settings`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_apps__remote_team_viewer__primary_group_id`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.settings.get_apps__remote_team_viewer__primary_group_id(timeout=None)`
- Async: `await client.silver.settings.get_apps__remote_team_viewer__primary_group_id(timeout=None)`
- Raw payload: `client.silver.settings.get_apps__remote_team_viewer__primary_group_id.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/settings/Apps.RemoteTeamViewer.PrimaryGroupId`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.settings`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_apps__sis__custom_field_mapping__enabled`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.settings.get_apps__sis__custom_field_mapping__enabled(timeout=None)`
- Async: `await client.silver.settings.get_apps__sis__custom_field_mapping__enabled(timeout=None)`
- Raw payload: `client.silver.settings.get_apps__sis__custom_field_mapping__enabled.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/settings/Apps.Sis.CustomFieldMapping.Enabled`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.settings`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_grids__user_options`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.settings.get_grids__user_options(timeout=None)`
- Async: `await client.silver.settings.get_grids__user_options(timeout=None)`
- Raw payload: `client.silver.settings.get_grids__user_options.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/settings/Grids.UserOptions`
- Observed in: `Chromebook-asset-actions.har`, `apple-asset-actions.har`, `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.settings`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_preferred_mappings`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.settings.get_preferred_mappings(timeout=None)`
- Async: `await client.silver.settings.get_preferred_mappings(timeout=None)`
- Raw payload: `client.silver.settings.get_preferred_mappings.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/settings/preferred-mappings`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.settings`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_shortcuts__recent_ids`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.settings.get_shortcuts__recent_ids(timeout=None)`
- Async: `await client.silver.settings.get_shortcuts__recent_ids(timeout=None)`
- Raw payload: `client.silver.settings.get_shortcuts__recent_ids.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/settings/Shortcuts.RecentIds`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.settings`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_tickets__status_lock`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.settings.get_tickets__status_lock(timeout=None)`
- Async: `await client.silver.settings.get_tickets__status_lock(timeout=None)`
- Raw payload: `client.silver.settings.get_tickets__status_lock.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/settings/Tickets.StatusLock`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.settings`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_undefined`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.settings.get_undefined(timeout=None)`
- Async: `await client.silver.settings.get_undefined(timeout=None)`
- Raw payload: `client.silver.settings.get_undefined.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/settings/undefined`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.settings`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_search__recent_user_searches`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.settings.post_search__recent_user_searches(product_id=..., scope=..., setting_type_id=..., site_id=..., user_id=..., value=..., timeout=None)`
- Async: `await client.silver.settings.post_search__recent_user_searches(product_id=..., scope=..., setting_type_id=..., site_id=..., user_id=..., value=..., timeout=None)`
- Raw payload: `client.silver.settings.post_search__recent_user_searches.raw(product_id=..., scope=..., setting_type_id=..., site_id=..., user_id=..., value=..., timeout=None)`
- HTTP route: `POST /api/v1.0/settings/Search.RecentUserSearches`
- Observed in: `Chromebook-asset-actions.har`, `apple-asset-actions.har`

HAR-derived undocumented POST route for `client.silver.settings`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `product_id` | `ProductId` | `body` | `yes` | `Any | None` | Body field inferred from HAR observations for this undocumented Silver route. |
| `scope` | `Scope` | `body` | `yes` | `str` | Body field inferred from HAR observations for this undocumented Silver route. |
| `setting_type_id` | `SettingTypeId` | `body` | `yes` | `str` | Body field inferred from HAR observations for this undocumented Silver route. |
| `site_id` | `SiteId` | `body` | `yes` | `str` | Body field inferred from HAR observations for this undocumented Silver route. |
| `user_id` | `UserId` | `body` | `yes` | `str` | Body field inferred from HAR observations for this undocumented Silver route. |
| `value` | `Value` | `body` | `yes` | `str` | Body field inferred from HAR observations for this undocumented Silver route. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---
