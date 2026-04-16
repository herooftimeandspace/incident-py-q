# `silver.app_registry` Namespace

Sync client access: `client.silver.app_registry`

Async client access: `client.silver.app_registry` with `await` on method calls.

These methods are Silver because Stoplight does not publish Golden contracts for them. They remain separate so undocumented behavior never overrides the documented SDK surface.

## Methods

### `get_app`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.app_registry.get_app(app_key=..., timeout=None)`
- Async: `await client.silver.app_registry.get_app(app_key=..., timeout=None)`
- Raw payload: `client.silver.app_registry.get_app.raw(app_key=..., timeout=None)`
- HTTP route: `GET /api/v1.0/app-registry/app/{app_key}`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.app_registry`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `app_key` | `app_key` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_site_app`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.app_registry.get_site_app(site_app_id=..., timeout=None)`
- Async: `await client.silver.app_registry.get_site_app(site_app_id=..., timeout=None)`
- Raw payload: `client.silver.app_registry.get_site_app.raw(site_app_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/app-registry/site-app/{site_app_id}`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.app_registry`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `site_app_id` | `site_app_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_installed`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.app_registry.post_installed(include_hidden_apps=..., timeout=None)`
- Async: `await client.silver.app_registry.post_installed(include_hidden_apps=..., timeout=None)`
- Raw payload: `client.silver.app_registry.post_installed.raw(include_hidden_apps=..., timeout=None)`
- HTTP route: `POST /api/v1.0/app-registry/installed`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented POST route for `client.silver.app_registry`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `include_hidden_apps` | `IncludeHiddenApps` | `body` | `yes` | `bool` | Body field inferred from HAR observations for this undocumented Silver route. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---
