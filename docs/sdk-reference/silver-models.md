# `silver.models` Namespace

Sync client access: `client.silver.models`

Async client access: `client.silver.models` with `await` on method calls.

These methods are Silver because Stoplight does not publish Golden contracts for them. They remain separate so undocumented behavior never overrides the documented SDK surface.

## Methods

### `get_all`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.models.get_all(filter=..., o=..., s=..., timeout=None)`
- Async: `await client.silver.models.get_all(filter=..., o=..., s=..., timeout=None)`
- Raw payload: `client.silver.models.get_all.raw(filter=..., o=..., s=..., timeout=None)`
- HTTP route: `GET /api/v1.0/models/all`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.models`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `filter` | `$filter` | `query` | `yes` | `str` | Query parameter inferred from HAR observations for this undocumented Silver route. |
| `o` | `$o` | `query` | `yes` | `str` | Query parameter inferred from HAR observations for this undocumented Silver route. |
| `s` | `$s` | `query` | `yes` | `int` | Query parameter inferred from HAR observations for this undocumented Silver route. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_apps_aeries_sis`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.models.get_apps_aeries_sis(timeout=None)`
- Async: `await client.silver.models.get_apps_aeries_sis(timeout=None)`
- Raw payload: `client.silver.models.get_apps_aeries_sis.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/models/apps/aeriesSis`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.models`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_apps_google_device_data`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.models.get_apps_google_device_data(timeout=None)`
- Async: `await client.silver.models.get_apps_google_device_data(timeout=None)`
- Raw payload: `client.silver.models.get_apps_google_device_data.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/models/apps/googleDeviceData`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.models`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_apps_microsoft_intune`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.models.get_apps_microsoft_intune(timeout=None)`
- Async: `await client.silver.models.get_apps_microsoft_intune(timeout=None)`
- Raw payload: `client.silver.models.get_apps_microsoft_intune.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/models/apps/microsoftIntune`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.models`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_apps_subtickets_for_i_t`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.models.get_apps_subtickets_for_i_t(timeout=None)`
- Async: `await client.silver.models.get_apps_subtickets_for_i_t(timeout=None)`
- Raw payload: `client.silver.models.get_apps_subtickets_for_i_t.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/models/apps/subticketsForIT`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.models`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_available_to_site`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.models.post_available_to_site(s=..., json_body=..., timeout=None)`
- Async: `await client.silver.models.post_available_to_site(s=..., json_body=..., timeout=None)`
- Raw payload: `client.silver.models.post_available_to_site.raw(s=..., json_body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/models/available/to/site`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented POST route for `client.silver.models`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `s` | `$s` | `query` | `yes` | `int` | Query parameter inferred from HAR observations for this undocumented Silver route. |
| `json_body` | `json_body` | `body` | `yes` | `Mapping[str, Any]` | Request body observed in HAR traffic. The SDK uses a single `json_body` payload because the Silver route carries a complex undocumented schema. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_endpoint`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.models.post_endpoint(filter=None, s=None, v=None, json_body=..., timeout=None)`
- Async: `await client.silver.models.post_endpoint(filter=None, s=None, v=None, json_body=..., timeout=None)`
- Raw payload: `client.silver.models.post_endpoint.raw(filter=None, s=None, v=None, json_body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/models`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented POST route for `client.silver.models`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `filter` | `$filter` | `query` | `no` | `str` | Query parameter inferred from HAR observations for this undocumented Silver route. |
| `s` | `$s` | `query` | `no` | `int` | Query parameter inferred from HAR observations for this undocumented Silver route. |
| `v` | `$v` | `query` | `no` | `int` | Query parameter inferred from HAR observations for this undocumented Silver route. |
| `json_body` | `json_body` | `body` | `yes` | `Mapping[str, Any]` | Request body observed in HAR traffic. The SDK uses a single `json_body` payload because the Silver route carries a complex undocumented schema. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---
