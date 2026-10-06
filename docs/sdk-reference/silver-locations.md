# `silver.locations` Namespace

Sync client access: `client.silver.locations`

Async client access: `client.silver.locations` with `await` on method calls.

These methods are Silver because the published contract does not document them directly, or because the SDK intentionally wraps a narrower Silver workflow around existing Golden operations. They remain separate so undocumented or convenience behavior never overrides the documented SDK surface.

## Methods

### `delete_location`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.locations.delete_location(location_id=..., timeout=None)`
- Async: `await client.silver.locations.delete_location(location_id=..., timeout=None)`
- Raw payload: `client.silver.locations.delete_location.raw(location_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/locations/{location_id}`
- Observed in: `migrated_from_golden_stoplight`

Delete location

#### Delete a specific location
#### Sample request:
```
DELETE /api/v1.0/locations/d344d88d-d201-4c52-8d23-4371fa7179bb
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.locations.delete_location` (operationId `Location_DeleteLocation`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `location_id` | `LocationId` | `path` | `yes` | `str` | Path parameter migrated from the previous Golden SDK. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_all_location_rooms`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.locations.get_all_location_rooms(timeout=None)`
- Async: `await client.silver.locations.get_all_location_rooms(timeout=None)`
- Raw payload: `client.silver.locations.get_all_location_rooms.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/locations/rooms`
- Observed in: `migrated_from_golden_stoplight`

Get All Location Rooms

#### Retrieve a list of rooms for all locations
#### Sample request:
```
GET /api/v1.0/locations/rooms
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.locations.get_all_location_rooms` (operationId `Location_GetAllLocationRooms`).

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_location_rooms`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.locations.get_location_rooms(location_id=..., timeout=None)`
- Async: `await client.silver.locations.get_location_rooms(location_id=..., timeout=None)`
- Raw payload: `client.silver.locations.get_location_rooms.raw(location_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/locations/{location_id}/rooms`
- Observed in: `migrated_from_golden_stoplight`

Get Location Room for Location

#### Retrieve a list of Location Rooms for a specific Location ID
#### Sample request:
```
GET /api/v1.0/locations/4fc0dc90-c40a-4012-b4e2-224ca02bdfb7/rooms
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.locations.get_location_rooms` (operationId `Location_GetLocationRooms`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `location_id` | `LocationId` | `path` | `yes` | `str` | Path parameter migrated from the previous Golden SDK. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_location_type`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.locations.get_location_type(location_type_id=..., timeout=None)`
- Async: `await client.silver.locations.get_location_type(location_type_id=..., timeout=None)`
- Raw payload: `client.silver.locations.get_location_type.raw(location_type_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/locations/types/{location_type_id}`
- Observed in: `migrated_from_golden_stoplight`

Get Location Type

#### Retrieve a specific Location Type via LocationTypeID
#### Sample request:
```
GET /api/v1.0/locations/types/27c81cbe-fdc4-4d7f-9c1c-e0311de5f882
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.locations.get_location_type` (operationId `Location_GetLocationType`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `location_type_id` | `LocationTypeId` | `path` | `yes` | `str` | Path parameter migrated from the previous Golden SDK. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_location_types`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.locations.get_location_types(timeout=None)`
- Async: `await client.silver.locations.get_location_types(timeout=None)`
- Raw payload: `client.silver.locations.get_location_types.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/locations/types`
- Observed in: `migrated_from_golden_stoplight`

Get Location Types

#### Retrieves a list of location types that can then be used to retrieve a specific location type via GET `api/locations/types/{LocationTypeId:guid}`.
#### Sample request:
```
GET /api/v1.0/locations/types
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.locations.get_location_types` (operationId `Location_GetLocationTypes`).

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `update_location`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.locations.update_location(location_id=..., json_body=..., timeout=None)`
- Async: `await client.silver.locations.update_location(location_id=..., json_body=..., timeout=None)`
- Raw payload: `client.silver.locations.update_location.raw(location_id=..., json_body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/locations/{location_id}`
- Observed in: `migrated_from_golden_stoplight`

Migrated Silver route for POST /locations/{LocationId}.

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.locations.update_location` (operationId `Location_UpdateLocation`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `location_id` | `LocationId` | `path` | `yes` | `str` | Path parameter migrated from the previous Golden SDK. |
| `json_body` | `Location` | `body` | `yes` | `dict[str, Any] | list[Any]` | Body parameter migrated from the previous Golden SDK. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---
