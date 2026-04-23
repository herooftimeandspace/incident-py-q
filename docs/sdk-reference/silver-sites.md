# `silver.sites` Namespace

Sync client access: `client.silver.sites`

Async client access: `client.silver.sites` with `await` on method calls.

These methods are Silver because Stoplight does not publish direct Golden contracts for them, or because the SDK intentionally wraps a narrower Silver workflow around existing Golden operations. They remain separate so undocumented or convenience behavior never overrides the documented SDK surface.

## Methods

### `get_deployments`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.sites.get_deployments(timeout=None)`
- Async: `await client.silver.sites.get_deployments(timeout=None)`
- Raw payload: `client.silver.sites.get_deployments.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/sites/deployments`
- Observed in: `Chromebook-asset-actions.har`, `apple-asset-actions.har`, `demo.incidentiq.com.har`, `windows-asset-intune-actions.har`

HAR-derived undocumented GET route for `client.silver.sites`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `post_roles`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.sites.post_roles(filter=None, s=None, v=None, timeout=None)`
- Async: `await client.silver.sites.post_roles(filter=None, s=None, v=None, timeout=None)`
- Raw payload: `client.silver.sites.post_roles.raw(filter=None, s=None, v=None, timeout=None)`
- HTTP route: `POST /api/v1.0/sites/roles`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented POST route for `client.silver.sites`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `filter` | `$filter` | `query` | `no` | `str` | Query parameter inferred from HAR observations for this undocumented Silver route. |
| `s` | `$s` | `query` | `no` | `int` | Query parameter inferred from HAR observations for this undocumented Silver route. |
| `v` | `$v` | `query` | `no` | `int` | Query parameter inferred from HAR observations for this undocumented Silver route. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---
