# `locations` Namespace

Sync client access: `client.locations`

Async client access: `client.locations` with `await` on method calls.

## Aliases

| Alias | Canonical Method | Route |
| --- | --- | --- |
| `delete` | `delete_location` | `DELETE /locations/{LocationId}` |
| `get` | `get_location` | `GET /locations/{LocationId}` |
| `update` | `update_location` | `POST /locations/{LocationId}` |

## Methods

### `delete_location`

Operation ID: `Location_DeleteLocation`

- Sync: `client.locations.delete_location(location_id=..., timeout=None)`
- Async: `await client.locations.delete_location(location_id=..., timeout=None)`
- Raw payload: `client.locations.delete_location.raw(location_id=..., timeout=None)`
- HTTP route: `DELETE /locations/{LocationId}`
- Source controller: `Locations`
- Aliases: `delete`

Delete location

#### Delete a specific location
#### Sample request:
```
DELETE /api/v1.0/locations/d344d88d-d201-4c52-8d23-4371fa7179bb
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `location_id` | `LocationId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_location_room`

Operation ID: `Location_DeleteLocationRoom`

- Sync: `client.locations.delete_location_room(location_room_id=..., timeout=None)`
- Async: `await client.locations.delete_location_room(location_room_id=..., timeout=None)`
- Raw payload: `client.locations.delete_location_room.raw(location_room_id=..., timeout=None)`
- HTTP route: `DELETE /locations/rooms/{LocationRoomId}`
- Source controller: `Locations`

Delete location room

#### Delete a specific location room
#### Sample request:
```
DELETE /api/v1.0/locations/rooms/dba9553e-c473-4863-b99f-2c5c54c73a1b
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `location_room_id` | `LocationRoomId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_all_location_rooms`

Operation ID: `Location_GetAllLocationRooms`

- Sync: `client.locations.get_all_location_rooms(timeout=None)`
- Async: `await client.locations.get_all_location_rooms(timeout=None)`
- Raw payload: `client.locations.get_all_location_rooms.raw(timeout=None)`
- HTTP route: `GET /locations/rooms`
- Source controller: `Locations`

Get All Location Rooms

#### Retrieve a list of rooms for all locations
#### Sample request:
```
GET /api/v1.0/locations/rooms
```

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `ListGetResponseOfLocationRoom`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfLocationRoom`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_location`

Operation ID: `Location_GetLocation`

- Sync: `client.locations.get_location(location_id=..., timeout=None)`
- Async: `await client.locations.get_location(location_id=..., timeout=None)`
- Raw payload: `client.locations.get_location.raw(location_id=..., timeout=None)`
- HTTP route: `GET /locations/{LocationId}`
- Source controller: `Locations`
- Aliases: `get`

Get Location

#### Retrieve a specific Location via Location ID
#### Sample request:
```
GET /api/v1.0/locations/4fc0dc90-c40a-4012-b4e2-224ca02bdfb7
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `location_id` | `LocationId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ItemGetResponseOfLocation`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemGetResponseOfLocation`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_location_room`

Operation ID: `Location_GetLocationRoom`

- Sync: `client.locations.get_location_room(location_room_id=..., timeout=None)`
- Async: `await client.locations.get_location_room(location_room_id=..., timeout=None)`
- Raw payload: `client.locations.get_location_room.raw(location_room_id=..., timeout=None)`
- HTTP route: `GET /locations/rooms/{LocationRoomId}`
- Source controller: `Locations`

Get Location Room

#### Retrieve a specific Location Room via that Room's ID
#### Sample request:
```
GET /api/v1.0/locations/rooms/6983376d-8906-4c3b-95de-f252a11d9164
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `location_room_id` | `LocationRoomId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ItemGetResponseOfLocationRoom`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemGetResponseOfLocationRoom`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_location_rooms`

Operation ID: `Location_GetLocationRooms`

- Sync: `client.locations.get_location_rooms(location_id=..., timeout=None)`
- Async: `await client.locations.get_location_rooms(location_id=..., timeout=None)`
- Raw payload: `client.locations.get_location_rooms.raw(location_id=..., timeout=None)`
- HTTP route: `GET /locations/{LocationId}/rooms`
- Source controller: `Locations`

Get Location Room for Location

#### Retrieve a list of Location Rooms for a specific Location ID
#### Sample request:
```
GET /api/v1.0/locations/4fc0dc90-c40a-4012-b4e2-224ca02bdfb7/rooms
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `location_id` | `LocationId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ListGetResponseOfLocationRoom`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfLocationRoom`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_location_type`

Operation ID: `Location_GetLocationType`

- Sync: `client.locations.get_location_type(location_type_id=..., timeout=None)`
- Async: `await client.locations.get_location_type(location_type_id=..., timeout=None)`
- Raw payload: `client.locations.get_location_type.raw(location_type_id=..., timeout=None)`
- HTTP route: `GET /locations/types/{LocationTypeId}`
- Source controller: `Locations`

Get Location Type

#### Retrieve a specific Location Type via LocationTypeID
#### Sample request:
```
GET /api/v1.0/locations/types/27c81cbe-fdc4-4d7f-9c1c-e0311de5f882
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `location_type_id` | `LocationTypeId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ItemGetResponseOfLocationType`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemGetResponseOfLocationType`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_location_types`

Operation ID: `Location_GetLocationTypes`

- Sync: `client.locations.get_location_types(timeout=None)`
- Async: `await client.locations.get_location_types(timeout=None)`
- Raw payload: `client.locations.get_location_types.raw(timeout=None)`
- HTTP route: `GET /locations/types`
- Source controller: `Locations`

Get Location Types

#### Retrieves a list of location types that can then be used to retrieve a specific location type via GET `api/locations/types/{LocationTypeId:guid}`.
#### Sample request:
```
GET /api/v1.0/locations/types
```

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `ListGetResponseOfLocationType`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfLocationType`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_locations`

Operation ID: `Location_GetLocations`

- Sync: `client.locations.get_locations(timeout=None)`
- Async: `await client.locations.get_locations(timeout=None)`
- Raw payload: `client.locations.get_locations.raw(timeout=None)`
- HTTP route: `GET /locations/all`
- Source controller: `Locations`

Get All Locations

#### Retrieve a list of all locations
#### Sample request:
```
GET /api/v1.0/locations/all
```

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `ListGetResponseOfLocation`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfLocation`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_location`

Operation ID: `Location_UpdateLocation`

- Sync: `client.locations.update_location(location_id=..., location=..., timeout=None)`
- Async: `await client.locations.update_location(location_id=..., location=..., timeout=None)`
- Raw payload: `client.locations.update_location.raw(location_id=..., location=..., timeout=None)`
- HTTP route: `POST /locations/{LocationId}`
- Source controller: `Locations`
- Aliases: `update`

No contract summary provided.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `location_id` | `LocationId` | `path` | `yes` | `str` | `-` | - |
| `location` | `Location` | `body` | `yes` | `Location` | `Location` | - |

#### Returns

- Typed call return: `ItemUpdateResponseOfLocation`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemUpdateResponseOfLocation`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_location_room`

Operation ID: `Location_UpdateLocationRoom`

- Sync: `client.locations.update_location_room(location_room_id=..., location_room=..., timeout=None)`
- Async: `await client.locations.update_location_room(location_room_id=..., location_room=..., timeout=None)`
- Raw payload: `client.locations.update_location_room.raw(location_room_id=..., location_room=..., timeout=None)`
- HTTP route: `POST /locations/rooms/{LocationRoomId}`
- Source controller: `Locations`

No contract summary provided.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `location_room_id` | `LocationRoomId` | `path` | `yes` | `str` | `-` | - |
| `location_room` | `LocationRoom` | `body` | `yes` | `LocationRoom` | `LocationRoom` | - |

#### Returns

- Typed call return: `ItemUpdateResponseOfLocationRoom`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemUpdateResponseOfLocationRoom`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
