# `slas` Golden Namespace

Sync client access: `client.slas`

Async client access: `client.slas` with `await` on method calls.

These methods are Golden because they come from bundled Stoplight controller contracts.

## Aliases

| Alias | Canonical Method | Route |
| --- | --- | --- |
| `delete` | `delete_sla` | `DELETE /slas/{SlaId}` |
| `get` | `get_sla` | `GET /slas/{SlaId}` |
| `list` | `get_slas` | `GET /slas` |
| `update` | `update_sla` | `POST /slas/{SlaId}` |

## Methods

### `activate_sla`

Provenance: Golden Stoplight contract

Operation ID: `Sla_ActivateSla`

- Sync: `client.slas.activate_sla(sla_id=..., timeout=None)`
- Async: `await client.slas.activate_sla(sla_id=..., timeout=None)`
- Raw payload: `client.slas.activate_sla.raw(sla_id=..., timeout=None)`
- HTTP route: `POST /slas/{SlaId}/activate`
- Source controller: `SLAs`

Activate SLA

#### Activates an SLA
#### Sample request:
```
POST /api/v1.0/slas/bd64e104-4c83-4744-a888-eeb760c03bfe/activate
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `sla_id` | `SlaId` | `path` | `yes` | `str` | `-` | SLA ID to be activated |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `deactivate_sla`

Provenance: Golden Stoplight contract

Operation ID: `Sla_DeactivateSla`

- Sync: `client.slas.deactivate_sla(sla_id=..., timeout=None)`
- Async: `await client.slas.deactivate_sla(sla_id=..., timeout=None)`
- Raw payload: `client.slas.deactivate_sla.raw(sla_id=..., timeout=None)`
- HTTP route: `POST /slas/{SlaId}/deactivate`
- Source controller: `SLAs`

Deactivate SLA

#### Deactivates an SLA
#### Sample request:
```
POST /api/v1.0/slas/bd64e104-4c83-4744-a888-eeb760c03bfe/deactivate
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `sla_id` | `SlaId` | `path` | `yes` | `str` | `-` | SLA ID to be deactivated |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_sla`

Provenance: Golden Stoplight contract

Operation ID: `Sla_DeleteSla`

- Sync: `client.slas.delete_sla(sla_id=..., timeout=None)`
- Async: `await client.slas.delete_sla(sla_id=..., timeout=None)`
- Raw payload: `client.slas.delete_sla.raw(sla_id=..., timeout=None)`
- HTTP route: `DELETE /slas/{SlaId}`
- Source controller: `SLAs`
- Aliases: `delete`

Delete SLA 

#### Delete a specific SLA
#### Sample request:
```
DELETE /api/v1.0/slas/bd64e104-4c83-4744-a888-eeb760c03bfe
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `sla_id` | `SlaId` | `path` | `yes` | `str` | `-` | SLA ID to be activated |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_sla`

Provenance: Golden Stoplight contract

Operation ID: `Sla_GetSla`

- Sync: `client.slas.get_sla(sla_id=..., r=..., timeout=None)`
- Async: `await client.slas.get_sla(sla_id=..., r=..., timeout=None)`
- Raw payload: `client.slas.get_sla.raw(sla_id=..., r=..., timeout=None)`
- HTTP route: `GET /slas/{SlaId}`
- Source controller: `SLAs`
- Aliases: `get`

Get SLA

#### Retrieve a specific SLA  by SlaId
#### Sample request:
```
GET /api/v1.0/slas/{SlaId:guid}
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `sla_id` | `SlaId` | `path` | `yes` | `str` | `-` | SlaId of SLA being requested |
| `r` | `r` | `query` | `yes` | `Any` | `-` | Request Options specified for the SlaId |

#### Returns

- Typed call return: `ItemGetResponseOfSla`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemGetResponseOfSla`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_slas`

Provenance: Golden Stoplight contract

Operation ID: `Sla_GetSlas`

- Sync: `client.slas.get_slas(r=..., timeout=None)`
- Async: `await client.slas.get_slas(r=..., timeout=None)`
- Raw payload: `client.slas.get_slas.raw(r=..., timeout=None)`
- HTTP route: `GET /slas`
- Source controller: `SLAs`
- Aliases: `list`

Get SLAs

#### Retrieves a list of available SLAs to apply to a ticket
#### Sample request:
```
GET /api/v1.0/slas
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `r` | `r` | `query` | `yes` | `Any` | `-` | Request Options specified for the Sla |

#### Returns

- Typed call return: `ListGetResponseOfSla`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfSla`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_sla`

Provenance: Golden Stoplight contract

Operation ID: `Sla_UpdateSla`

- Sync: `client.slas.update_sla(sla_id=..., item=..., timeout=None)`
- Async: `await client.slas.update_sla(sla_id=..., item=..., timeout=None)`
- Raw payload: `client.slas.update_sla.raw(sla_id=..., item=..., timeout=None)`
- HTTP route: `POST /slas/{SlaId}`
- Source controller: `SLAs`
- Aliases: `update`

No contract summary provided.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `sla_id` | `SlaId` | `path` | `yes` | `str` | `-` | - |
| `item` | `Item` | `body` | `yes` | `UpdateSlaRequest` | `UpdateSlaRequest` | - |

#### Returns

- Typed call return: `ItemUpdateResponseOfGuid`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemUpdateResponseOfGuid`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
