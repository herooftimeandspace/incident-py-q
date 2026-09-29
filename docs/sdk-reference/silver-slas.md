# `silver.slas` Namespace

Sync client access: `client.silver.slas`

Async client access: `client.silver.slas` with `await` on method calls.

These methods are Silver because the published contract does not document them directly, or because the SDK intentionally wraps a narrower Silver workflow around existing Golden operations. They remain separate so undocumented or convenience behavior never overrides the documented SDK surface.

## Methods

### `get_sla`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.slas.get_sla(sla_id=..., r=..., timeout=None)`
- Async: `await client.silver.slas.get_sla(sla_id=..., r=..., timeout=None)`
- Raw payload: `client.silver.slas.get_sla.raw(sla_id=..., r=..., timeout=None)`
- HTTP route: `GET /api/v1.0/slas/{sla_id}`
- Observed in: `migrated_from_golden_stoplight`

Get SLA

#### Retrieve a specific SLA  by SlaId
#### Sample request:
```
GET /api/v1.0/slas/{SlaId:guid}
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.slas.get_sla` (operationId `Sla_GetSla`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `sla_id` | `SlaId` | `path` | `yes` | `str` | SlaId of SLA being requested |
| `r` | `r` | `query` | `yes` | `Any` | Request Options specified for the SlaId |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `update_sla`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.slas.update_sla(sla_id=..., json_body=..., timeout=None)`
- Async: `await client.silver.slas.update_sla(sla_id=..., json_body=..., timeout=None)`
- Raw payload: `client.silver.slas.update_sla.raw(sla_id=..., json_body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/slas/{sla_id}`
- Observed in: `migrated_from_golden_stoplight`

Migrated Silver route for POST /slas/{SlaId}.

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.slas.update_sla` (operationId `Sla_UpdateSla`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `sla_id` | `SlaId` | `path` | `yes` | `str` | Path parameter migrated from the previous Golden SDK. |
| `json_body` | `Item` | `body` | `yes` | `dict[str, Any] | list[Any]` | Body parameter migrated from the previous Golden SDK. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---
