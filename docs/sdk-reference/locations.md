# `locations` Golden Namespace

Sync client access: `client.locations`

Async client access: `client.locations` with `await` on method calls.

These methods are Golden because they come from the bundled Incident IQ OpenAPI contract.

## Aliases

| Alias | Canonical Method | Route |
| --- | --- | --- |
| `create` | `create_location_v2` | `POST /api/v2.0/locations/new` |

## Methods

### `create_location_room`

Provenance: Golden OpenAPI contract

Operation ID: `createLocationRoom`

- Sync: `client.locations.create_location_room(site_id=None, body=..., timeout=None)`
- Async: `await client.locations.create_location_room(site_id=None, body=..., timeout=None)`
- Raw payload: `client.locations.create_location_room.raw(site_id=None, body=..., timeout=None)`
- HTTP route: `POST /api/v2.0/locations/rooms`
- Source controller: `IncidentIQ API`

Create a room

Creates a single room within a location. The room will be associated with the specified location and room type.

**Required Fields:**
- `LocationId` - Parent location (building/school)
- `Name` - Room name or number
- `LocationRoomTypeId` - Room type classification
- `LocationRoomStatusTypeId` - Room status

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |
| `body` | `body` | `body` | `yes` | `UpdateLocationRoomRequest` | `UpdateLocationRoomRequest` | - |

#### Returns

- Typed call return: `LocationRoomItemCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `LocationRoomItemCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_location_rooms_batch`

Provenance: Golden OpenAPI contract

Operation ID: `createLocationRoomsBatch`

- Sync: `client.locations.create_location_rooms_batch(site_id=None, body=..., timeout=None)`
- Async: `await client.locations.create_location_rooms_batch(site_id=None, body=..., timeout=None)`
- Raw payload: `client.locations.create_location_rooms_batch.raw(site_id=None, body=..., timeout=None)`
- HTTP route: `POST /api/v2.0/locations/rooms/new/batch`
- Source controller: `IncidentIQ API`

Create multiple rooms

Creates multiple rooms in a single batch operation. Each room entry is created independently, making this useful for initial setup or bulk imports.

**Prerequisites**
1. **LocationId** - Use [GET /api/v2.0/locations](#/Locations/getMyLocationsV2) or [POST /api/v2.0/locations/view](#/Locations/getMyLocationsViewFilteredV2) and extract `Items[].LocationId`.
2. **LocationRoomTypeId/LocationRoomStatusTypeId** - Use existing room data or [GET /api/v2.0/locations/rooms/status-types](#/Locations/getAllLocationRoomStatusTypes) for status types.

**Workflow Example**
1. Build an array of `UpdateLocationRoomRequest` objects for each room.
2. Submit: [POST /api/v2.0/locations/rooms/new/batch](#/Locations/createLocationRoomsBatch).
3. Review the response for created room IDs.

**Minimal Required Fields**: For each room, `LocationId`, `Name`, `LocationRoomTypeId`, `LocationRoomStatusTypeId`.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | - |

#### Returns

- Typed call return: `LocationRoomListCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `LocationRoomListCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_location_v2`

Provenance: Golden OpenAPI contract

Operation ID: `createLocationV2`

- Sync: `client.locations.create_location_v2(site_id=None, product_id=None, body=..., timeout=None)`
- Async: `await client.locations.create_location_v2(site_id=None, product_id=None, body=..., timeout=None)`
- Raw payload: `client.locations.create_location_v2.raw(site_id=None, product_id=None, body=..., timeout=None)`
- HTTP route: `POST /api/v2.0/locations/new`
- Source controller: `IncidentIQ API`
- Aliases: `create`

Create location

Creates a new location within the current site. The location will be associated with the site specified in the request headers.

**Required Fields:**
- `Name` - Display name for the location
- `LocationTypeId` - Reference to a valid location type

**Address Handling:** If address fields (Street1, City, State, Zip) are provided, an address record will be automatically created and linked to the location.

**Custom Fields:** To set custom field values during creation, set `UpdateCustomFields: true` and include the `CustomFieldValues` array.

**Workflow:**
1. Obtain a valid `LocationTypeId` from location type endpoints
2. Optionally obtain a `LocationStatusTypeId` for the initial status
3. Call this endpoint with required fields
4. Use the returned `LocationId` for subsequent operations

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context - the location will be created in this site |
| `product_id` | `ProductId` | `header` | `no` | `str` | `-` | Product context for the request |
| `body` | `body` | `body` | `yes` | `UpdateLocationRequest` | `UpdateLocationRequest` | - |

#### Returns

- Typed call return: `LocationCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `LocationCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_location_room`

Provenance: Golden OpenAPI contract

Operation ID: `deleteLocationRoom`

- Sync: `client.locations.delete_location_room(room_id=..., site_id=None, timeout=None)`
- Async: `await client.locations.delete_location_room(room_id=..., site_id=None, timeout=None)`
- Raw payload: `client.locations.delete_location_room.raw(room_id=..., site_id=None, timeout=None)`
- HTTP route: `DELETE /api/v2.0/locations/rooms/{roomId}`
- Source controller: `IncidentIQ API`

Delete a room

Soft-deletes a room, removing it from active lists while preserving data for restoration. Use the undelete endpoint to restore if needed.

**Prerequisites**
1. **roomId** - Use [POST /api/v2.0/locations/rooms/query](#/Locations/queryLocationRooms) and extract `Items[].LocationRoomId`.

**Workflow Example**
1. Identify the room to delete.
2. Delete: [DELETE /api/v2.0/locations/rooms/{roomId}](#/Locations/deleteLocationRoom).
3. If needed, restore with [POST /api/v2.0/locations/rooms/{roomId}/undelete](#/Locations/undeleteLocationRoom).

**Minimal Required Fields**: roomId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `room_id` | `roomId` | `path` | `yes` | `str` | `-` | The unique identifier of the room to delete |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_location_rooms_batch`

Provenance: Golden OpenAPI contract

Operation ID: `deleteLocationRoomsBatch`

- Sync: `client.locations.delete_location_rooms_batch(site_id=None, body=..., timeout=None)`
- Async: `await client.locations.delete_location_rooms_batch(site_id=None, body=..., timeout=None)`
- Raw payload: `client.locations.delete_location_rooms_batch.raw(site_id=None, body=..., timeout=None)`
- HTTP route: `DELETE /api/v2.0/locations/rooms/delete/batch`
- Source controller: `IncidentIQ API`

Delete multiple rooms

Soft-deletes multiple rooms in a single batch operation. Use this to remove rooms from active use without permanently deleting their records.

**Prerequisites**
1. **Room IDs** - Use [POST /api/v2.0/locations/rooms/query](#/Locations/queryLocationRooms) and extract `Items[].LocationRoomId`.

**Workflow Example**
1. Query rooms to determine the list of IDs to delete.
2. Submit: [DELETE /api/v2.0/locations/rooms/delete/batch](#/Locations/deleteLocationRoomsBatch) with the ID array.
3. Restore later using [POST /api/v2.0/locations/rooms/{roomId}/undelete](#/Locations/undeleteLocationRoom) if needed.

**Minimal Required Fields**: Array of room IDs.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | - |

#### Returns

- Typed call return: `ListDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_location_v2`

Provenance: Golden OpenAPI contract

Operation ID: `deleteLocationV2`

- Sync: `client.locations.delete_location_v2(location_id=..., site_id=None, timeout=None)`
- Async: `await client.locations.delete_location_v2(location_id=..., site_id=None, timeout=None)`
- Raw payload: `client.locations.delete_location_v2.raw(location_id=..., site_id=None, timeout=None)`
- HTTP route: `DELETE /api/v2.0/locations/{LocationId}/delete`
- Source controller: `IncidentIQ API`

Delete location

Soft-deletes a location. The location record is marked as deleted but not permanently removed from the database. Deleted locations can be restored using the undelete endpoint.

**Important Considerations:**
- Assets, tickets, and users associated with this location may need to be migrated first
- Use the [POST /api/v2.0/locations/migrate](#/Locations/updateLocationV2) endpoint to move associated entities before deletion
- Deleted locations will no longer appear in standard location lists

**Related Endpoints:**
- [PUT /api/v2.0/locations/{LocationId}/undelete](#/Locations/updateLocationV2) - Restore a deleted location

**Prerequisites**
1. **LocationId** - Use [GET /api/v2.0/locations](#/Locations/getMyLocationsV2) to obtain. Extract `Items[].LocationId` from response.

**Workflow Example**
1. Obtain LocationId: [GET /api/v2.0/locations](#/Locations/getMyLocationsV2) → extract `Items[].LocationId`
2. Call this endpoint: [DELETE /api/v2.0/locations/{LocationId}/delete](#/Locations/deleteLocationV2)

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `location_id` | `LocationId` | `path` | `yes` | `str` | `-` | Unique identifier of the location to delete |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |

#### Returns

- Typed call return: `LocationDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `LocationDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_address_by_id_v2`

Provenance: Golden OpenAPI contract

Operation ID: `getAddressByIdV2`

- Sync: `client.locations.get_address_by_id_v2(address_id=..., site_id=None, timeout=None)`
- Async: `await client.locations.get_address_by_id_v2(address_id=..., site_id=None, timeout=None)`
- Raw payload: `client.locations.get_address_by_id_v2.raw(address_id=..., site_id=None, timeout=None)`
- HTTP route: `GET /api/v2.0/locations/address/{AddressId}`
- Source controller: `IncidentIQ API`

Get address by ID

Retrieves an address record by its unique identifier. Returns the complete address including street, city, state, ZIP code, country, and geographic coordinates.

**Prerequisites**
1. **AddressId** - Obtain via [GET /api/v2.0/locations/{LocationId}](#/Locations/getLocationByIdV2) and extract `Item.AddressId`, or from [GET /api/v2.0/locations/{LocationId}/address](#/Locations/getLocationAddressV2) response.

**Workflow Example**
1. List locations: [GET /api/v2.0/locations](#/Locations/getMyLocationsV2) → extract `Item.AddressId`
2. Call this endpoint: [GET /api/v2.0/locations/address/{AddressId}](#/Locations/getAddressByIdV2)

**Authentication:** Requires valid bearer token.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `address_id` | `AddressId` | `path` | `yes` | `str` | `-` | Unique identifier of the address to retrieve |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |

#### Returns

- Typed call return: `AddressItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AddressItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_all_location_room_status_types`

Provenance: Golden OpenAPI contract

Operation ID: `getAllLocationRoomStatusTypes`

- Sync: `client.locations.get_all_location_room_status_types(site_id=None, timeout=None)`
- Async: `await client.locations.get_all_location_room_status_types(site_id=None, timeout=None)`
- Raw payload: `client.locations.get_all_location_room_status_types.raw(site_id=None, timeout=None)`
- HTTP route: `GET /api/v2.0/locations/rooms/status-types`
- Source controller: `IncidentIQ API`

Get all room status types

Returns all available room status types (for example, Active, Inactive, Under Maintenance). Use this when configuring room creation or when displaying status selectors.

**Workflow Example**
1. Fetch status types: [GET /api/v2.0/locations/rooms/status-types](#/Locations/getAllLocationRoomStatusTypes).
2. Use the returned IDs in room create/update requests.

**Minimal Required Fields**: None.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |

#### Returns

- Typed call return: `LocationRoomStatusTypeListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `LocationRoomStatusTypeListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_all_site_locations_filtered_v2`

Provenance: Golden OpenAPI contract

Operation ID: `getAllSiteLocationsFilteredV2`

- Sync: `client.locations.get_all_site_locations_filtered_v2(site_id=None, product_id=None, body=None, timeout=None)`
- Async: `await client.locations.get_all_site_locations_filtered_v2(site_id=None, product_id=None, body=None, timeout=None)`
- Raw payload: `client.locations.get_all_site_locations_filtered_v2.raw(site_id=None, product_id=None, body=None, timeout=None)`
- HTTP route: `POST /api/v2.0/locations/all`
- Source controller: `IncidentIQ API`

Get all site locations (filtered)

Returns all locations for the current site with advanced filtering capabilities via request body. Unlike the basic endpoints, this provides full query control over location type, status, and pagination.

**Permission Note:** Requires site-level access to view all locations.

**Workflow Example**
1. Build a `GetUserLocationsRequest` with filters (location type, status, paging).
2. Call this endpoint: [POST /api/v2.0/locations/all](#/Locations/getAllSiteLocationsFilteredV2) with the request body.
3. Process paginated results using `Paging.PageIndex` and `Paging.TotalRows`.

**Related Endpoints:**
- [GET /api/v2.0/locations/all](#/Locations/getAllSiteLocationsV2) - Same endpoint with query string filters
- [GET /api/v2.0/locations/all/{siteId}](#/Locations/getSiteLocationsBySiteIdV2) - Get locations for a specific site

**Minimal Required Fields**: None (filters are optional).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |
| `product_id` | `ProductId` | `header` | `no` | `str` | `-` | Product context for the request |
| `body` | `body` | `body` | `no` | `GetUserLocationsRequest` | `GetUserLocationsRequest` | - |

#### Returns

- Typed call return: `LocationListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `LocationListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_all_site_locations_v2`

Provenance: Golden OpenAPI contract

Operation ID: `getAllSiteLocationsV2`

- Sync: `client.locations.get_all_site_locations_v2(site_id=None, product_id=None, p=None, s=None, timeout=None)`
- Async: `await client.locations.get_all_site_locations_v2(site_id=None, product_id=None, p=None, s=None, timeout=None)`
- Raw payload: `client.locations.get_all_site_locations_v2.raw(site_id=None, product_id=None, p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v2.0/locations/all`
- Source controller: `IncidentIQ API`

Get all site locations

Returns all locations for the current site, regardless of the caller's individual location permissions. This endpoint is useful for administrative views and reports that need to see all locations.

**Supports Custom Filters:** This endpoint accepts filter parameters in query string format.

**Permission Note:** Requires site-level access. The caller must have permission to view all locations in the site.

**Related Endpoints:**
- [POST /api/v2.0/locations/all](#/Locations/getAllSiteLocationsFilteredV2) - Same endpoint with request body filters
- [GET /api/v2.0/locations/all/{siteId}](#/Locations/getSiteLocationsBySiteIdV2) - Get locations for a specific site

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request. If not specified, uses the user's default site. |
| `product_id` | `ProductId` | `header` | `no` | `str` | `-` | Product context for the request |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index |
| `s` | `$s` | `query` | `no` | `int` | `-` | Page size (number of records per page) |

#### Returns

- Typed call return: `LocationListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `LocationListResponse`
- Pagination helper: `client.locations.get_all_site_locations_v2.iter_pages(start_page=1, page_size=100, max_pages=None, site_id=None, product_id=None, p=None, s=None, timeout=None)`

---

### `get_location_address_v2`

Provenance: Golden OpenAPI contract

Operation ID: `getLocationAddressV2`

- Sync: `client.locations.get_location_address_v2(location_id=..., site_id=None, timeout=None)`
- Async: `await client.locations.get_location_address_v2(location_id=..., site_id=None, timeout=None)`
- Raw payload: `client.locations.get_location_address_v2.raw(location_id=..., site_id=None, timeout=None)`
- HTTP route: `GET /api/v2.0/locations/{LocationId}/address`
- Source controller: `IncidentIQ API`

Get location address

Retrieves the physical address associated with a specific location. Returns street address, city, state, ZIP code, country, and geographic coordinates (latitude/longitude).

**Prerequisites**
1. **LocationId** - Obtain via [GET /api/v2.0/locations](#/Locations/getMyLocationsV2) and extract `Items[].LocationId`.

**Workflow Example**
1. List locations: [GET /api/v2.0/locations](#/Locations/getMyLocationsV2) → extract target `LocationId`.
2. Call this endpoint: [GET /api/v2.0/locations/{LocationId}/address](#/Locations/getLocationAddressV2).
3. Use returned coordinates for mapping integration or address display.

**Related Endpoints:**
- [GET /api/v2.0/locations/{LocationId}](#/Locations/getLocationByIdV2) - Get complete location record with address included
- [GET /api/v2.0/locations/address/{AddressId}](#/Locations/getAddressByIdV2) - Get address directly by AddressId

**Authentication:** Requires valid bearer token.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `location_id` | `LocationId` | `path` | `yes` | `str` | `-` | Unique identifier of the location |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |

#### Returns

- Typed call return: `AddressItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AddressItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_location_by_id_v2`

Provenance: Golden OpenAPI contract

Operation ID: `getLocationByIdV2`

- Sync: `client.locations.get_location_by_id_v2(location_id=..., site_id=None, product_id=None, timeout=None)`
- Async: `await client.locations.get_location_by_id_v2(location_id=..., site_id=None, product_id=None, timeout=None)`
- Raw payload: `client.locations.get_location_by_id_v2.raw(location_id=..., site_id=None, product_id=None, timeout=None)`
- HTTP route: `GET /api/v2.0/locations/{LocationId}`
- Source controller: `IncidentIQ API`

Get location by ID

Retrieves a single location by its unique identifier. Returns the complete location record including address, type, status, custom field values, and room count.

**Prerequisites**
1. **LocationId** - Obtain via [GET /api/v2.0/locations](#/Locations/getMyLocationsV2) and extract `Items[].LocationId`, or from ticket/asset/user records.

**Workflow Example**
1. List accessible locations: [GET /api/v2.0/locations](#/Locations/getMyLocationsV2) → identify target location.
2. Call this endpoint: [GET /api/v2.0/locations/{LocationId}](#/Locations/getLocationByIdV2) with the target `LocationId`.
3. Use returned data to display location details including address, type, and status.

**Related Endpoints:**
- [GET /api/v2.0/locations/{LocationId}/address](#/Locations/getLocationAddressV2) - Get only the address
- [PUT /api/v2.0/locations/{LocationId}](#/Locations/updateLocationV2) - Update the location

**Authentication:** Requires valid bearer token.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `location_id` | `LocationId` | `path` | `yes` | `str` | `-` | Unique identifier of the location to retrieve |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |
| `product_id` | `ProductId` | `header` | `no` | `str` | `-` | Product context for the request |

#### Returns

- Typed call return: `LocationItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `LocationItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_location_floorplans_v2`

Provenance: Golden OpenAPI contract

Operation ID: `getLocationFloorplansV2`

- Sync: `client.locations.get_location_floorplans_v2(location_id=..., site_id=None, timeout=None)`
- Async: `await client.locations.get_location_floorplans_v2(location_id=..., site_id=None, timeout=None)`
- Raw payload: `client.locations.get_location_floorplans_v2.raw(location_id=..., site_id=None, timeout=None)`
- HTTP route: `GET /api/v2.0/locations/{locationId}/floorplans`
- Source controller: `IncidentIQ API`

Get location floorplans

Retrieves all floorplan files associated with a location. Floorplans are visual floor layouts that can be used for asset placement and room mapping within the location.

**Prerequisites**
1. **locationId** - Obtain via [GET /api/v2.0/locations](#/Locations/getMyLocationsV2) and extract `Items[].LocationId`.

**Workflow Example**
1. List locations: [GET /api/v2.0/locations](#/Locations/getMyLocationsV2) → extract target `LocationId`.
2. Call this endpoint: [GET /api/v2.0/locations/{locationId}/floorplans](#/Locations/getLocationFloorplansV2).
3. For each floorplan, use [GET /api/v1.0/files/{FileId}](#/Files/downloadFile) to download the actual file.

**Related Endpoints:**
- [POST /api/v2.0/locations/{locationId}/floorplans](#/Locations/updateLocationFloorplansV2) - Update floorplan associations
- [GET /api/v2.0/locations/{locationId}/images](#/Locations/getLocationImagesV2) - Get location images
- [POST /api/v1.0/files/upload](#/Files/uploadFile) - Upload a new floorplan file

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `location_id` | `locationId` | `path` | `yes` | `str` | `-` | Unique identifier of the location |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |

#### Returns

- Typed call return: `EntityFileDetailListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `EntityFileDetailListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_location_ids_for_filter_sets_v2`

Provenance: Golden OpenAPI contract

Operation ID: `getLocationIdsForFilterSetsV2`

- Sync: `client.locations.get_location_ids_for_filter_sets_v2(site_id=None, body=..., timeout=None)`
- Async: `await client.locations.get_location_ids_for_filter_sets_v2(site_id=None, body=..., timeout=None)`
- Raw payload: `client.locations.get_location_ids_for_filter_sets_v2.raw(site_id=None, body=..., timeout=None)`
- HTTP route: `POST /api/v2.0/locations/ids/for/filtersets`
- Source controller: `IncidentIQ API`

Get location IDs for filter sets

Evaluates specified filter sets against locations and returns the IDs of locations that match each filter set. This is useful for determining which locations would be affected by filter-based rules or workflows.

**Use Cases:**
- Preview which locations match a filter set before applying it
- Validate filter set configurations
- Build dynamic location lists based on filter criteria

**Performance Considerations:**
- Processing many filter sets or locations can be resource-intensive
- Use `OnlyReturnFirstMatch` when you only need to know if any locations match
- Use `IdsToProcess` to limit evaluation to specific locations

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |
| `body` | `body` | `body` | `yes` | `GetIdsForFilterSetRequest` | `GetIdsForFilterSetRequest` | - |

#### Returns

- Typed call return: `IdsForFilterSetsListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `IdsForFilterSetsListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_location_images_v2`

Provenance: Golden OpenAPI contract

Operation ID: `getLocationImagesV2`

- Sync: `client.locations.get_location_images_v2(location_id=..., site_id=None, timeout=None)`
- Async: `await client.locations.get_location_images_v2(location_id=..., site_id=None, timeout=None)`
- Raw payload: `client.locations.get_location_images_v2.raw(location_id=..., site_id=None, timeout=None)`
- HTTP route: `GET /api/v2.0/locations/{locationId}/images`
- Source controller: `IncidentIQ API`

Get location images

Retrieves all image files associated with a location. Images can include exterior/interior photos, site maps, parking diagrams, or other visual documentation for the location.

**Prerequisites**
1. **locationId** - Obtain via [GET /api/v2.0/locations](#/Locations/getMyLocationsV2) and extract `Items[].LocationId`.

**Workflow Example**
1. List locations: [GET /api/v2.0/locations](#/Locations/getMyLocationsV2) → extract target `LocationId`.
2. Call this endpoint: [GET /api/v2.0/locations/{locationId}/images](#/Locations/getLocationImagesV2).
3. For each image, use [GET /api/v1.0/files/{FileId}](#/Files/downloadFile) to download the actual file.

**Related Endpoints:**
- [POST /api/v2.0/locations/{locationId}/images](#/Locations/updateLocationImagesV2) - Update image associations
- [GET /api/v2.0/locations/{locationId}/floorplans](#/Locations/getLocationFloorplansV2) - Get location floorplans
- [POST /api/v1.0/files/upload](#/Files/uploadFile) - Upload a new image file

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `location_id` | `locationId` | `path` | `yes` | `str` | `-` | Unique identifier of the location |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |

#### Returns

- Typed call return: `EntityFileDetailListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `EntityFileDetailListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_location_room_available_times`

Provenance: Golden OpenAPI contract

Operation ID: `getLocationRoomAvailableTimes`

- Sync: `client.locations.get_location_room_available_times(location_room_id=..., site_id=None, timeout=None)`
- Async: `await client.locations.get_location_room_available_times(location_room_id=..., site_id=None, timeout=None)`
- Raw payload: `client.locations.get_location_room_available_times.raw(location_room_id=..., site_id=None, timeout=None)`
- HTTP route: `GET /api/v2.0/locations/rooms/{locationRoomId}/available-times`
- Source controller: `IncidentIQ API`

Get room available times

Retrieves the weekly availability schedule for a room. Use this to show open/closed hours when scheduling events.

**Prerequisites**
1. **locationRoomId** - Use [POST /api/v2.0/locations/rooms/query](#/Locations/queryLocationRooms) and extract `Items[].LocationRoomId`.

**Workflow Example**
1. Identify the room ID.
2. Fetch availability: [GET /api/v2.0/locations/rooms/{locationRoomId}/available-times](#/Locations/getLocationRoomAvailableTimes).
3. Use the returned weekly schedule to validate bookings.

**Minimal Required Fields**: locationRoomId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `location_room_id` | `locationRoomId` | `path` | `yes` | `str` | `-` | The unique identifier of the room |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |

#### Returns

- Typed call return: `LocationRoomAvailableTimeListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `LocationRoomAvailableTimeListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_location_room_by_id`

Provenance: Golden OpenAPI contract

Operation ID: `getLocationRoomById`

- Sync: `client.locations.get_location_room_by_id(room_id=..., site_id=None, timeout=None)`
- Async: `await client.locations.get_location_room_by_id(room_id=..., site_id=None, timeout=None)`
- Raw payload: `client.locations.get_location_room_by_id.raw(room_id=..., site_id=None, timeout=None)`
- HTTP route: `GET /api/v2.0/locations/rooms/{roomId}`
- Source controller: `IncidentIQ API`

Get room by ID

Retrieves a single room by its unique identifier, including type, status, capacity, and availability flags. Use this when editing a room or displaying detailed room metadata.

**Prerequisites**
1. **roomId** - Use [POST /api/v2.0/locations/rooms/query](#/Locations/queryLocationRooms) or [POST /api/v2.0/locations/{locationId}/rooms](#/Locations/queryLocationRoomsByLocationId) and extract `Items[].LocationRoomId`.

**Workflow Example**
1. Query rooms to locate the target room.
2. Fetch details: [GET /api/v2.0/locations/rooms/{roomId}](#/Locations/getLocationRoomById).

**Minimal Required Fields**: roomId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `room_id` | `roomId` | `path` | `yes` | `str` | `-` | The unique identifier of the room |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |

#### Returns

- Typed call return: `LocationRoomItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `LocationRoomItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_location_room_images`

Provenance: Golden OpenAPI contract

Operation ID: `getLocationRoomImages`

- Sync: `client.locations.get_location_room_images(location_room_id=..., site_id=None, timeout=None)`
- Async: `await client.locations.get_location_room_images(location_room_id=..., site_id=None, timeout=None)`
- Raw payload: `client.locations.get_location_room_images.raw(location_room_id=..., site_id=None, timeout=None)`
- HTTP route: `GET /api/v2.0/locations/rooms/{locationRoomId}/images`
- Source controller: `IncidentIQ API`

Get room images

Retrieves all image files associated with a room. Use this to display room photos in booking or facilities interfaces.

**Prerequisites**
1. **locationRoomId** - Use [POST /api/v2.0/locations/rooms/query](#/Locations/queryLocationRooms) and extract `Items[].LocationRoomId`.

**Workflow Example**
1. Identify the room ID.
2. Fetch images: [GET /api/v2.0/locations/rooms/{locationRoomId}/images](#/Locations/getLocationRoomImages).
3. Render the returned file metadata as thumbnails or links.

**Minimal Required Fields**: locationRoomId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `location_room_id` | `locationRoomId` | `path` | `yes` | `str` | `-` | The unique identifier of the room |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |

#### Returns

- Typed call return: `EntityFileDetailListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `EntityFileDetailListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_location_room_layouts`

Provenance: Golden OpenAPI contract

Operation ID: `getLocationRoomLayouts`

- Sync: `client.locations.get_location_room_layouts(location_room_id=..., site_id=None, timeout=None)`
- Async: `await client.locations.get_location_room_layouts(location_room_id=..., site_id=None, timeout=None)`
- Raw payload: `client.locations.get_location_room_layouts.raw(location_room_id=..., site_id=None, timeout=None)`
- HTTP route: `GET /api/v2.0/locations/rooms/{locationRoomId}/layouts`
- Source controller: `IncidentIQ API`

Get room layouts

Retrieves all floorplan/layout files associated with a room. Use this to display room diagrams in scheduling or facilities views.

**Prerequisites**
1. **locationRoomId** - Use [POST /api/v2.0/locations/rooms/query](#/Locations/queryLocationRooms) and extract `Items[].LocationRoomId`.

**Workflow Example**
1. Identify the room ID.
2. Fetch layouts: [GET /api/v2.0/locations/rooms/{locationRoomId}/layouts](#/Locations/getLocationRoomLayouts).
3. Render the returned file metadata as links or previews.

**Minimal Required Fields**: locationRoomId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `location_room_id` | `locationRoomId` | `path` | `yes` | `str` | `-` | The unique identifier of the room |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |

#### Returns

- Typed call return: `EntityFileDetailListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `EntityFileDetailListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_location_room_status_type_by_id`

Provenance: Golden OpenAPI contract

Operation ID: `getLocationRoomStatusTypeById`

- Sync: `client.locations.get_location_room_status_type_by_id(status_type_id=..., site_id=None, timeout=None)`
- Async: `await client.locations.get_location_room_status_type_by_id(status_type_id=..., site_id=None, timeout=None)`
- Raw payload: `client.locations.get_location_room_status_type_by_id.raw(status_type_id=..., site_id=None, timeout=None)`
- HTTP route: `GET /api/v2.0/locations/rooms/status-types/{statusTypeId}`
- Source controller: `IncidentIQ API`

Get room status type by ID

Retrieves a single room status type by ID (for example, Active or Under Maintenance). Use this when you need to resolve a status type reference to a display name.

**Prerequisites**
1. **statusTypeId** - Use [GET /api/v2.0/locations/rooms/status-types](#/Locations/getAllLocationRoomStatusTypes) and extract `Items[].LocationRoomStatusTypeId`.

**Workflow Example**
1. List status types and capture the ID.
2. Get the specific type: [GET /api/v2.0/locations/rooms/status-types/{statusTypeId}](#/Locations/getLocationRoomStatusTypeById).

**Minimal Required Fields**: statusTypeId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `status_type_id` | `statusTypeId` | `path` | `yes` | `str` | `-` | The unique identifier of the status type |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |

#### Returns

- Typed call return: `LocationRoomStatusTypeItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `LocationRoomStatusTypeItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_my_locations_filtered_v2`

Provenance: Golden OpenAPI contract

Operation ID: `getMyLocationsFilteredV2`

- Sync: `client.locations.get_my_locations_filtered_v2(site_id=None, product_id=None, body=None, timeout=None)`
- Async: `await client.locations.get_my_locations_filtered_v2(site_id=None, product_id=None, body=None, timeout=None)`
- Raw payload: `client.locations.get_my_locations_filtered_v2.raw(site_id=None, product_id=None, body=None, timeout=None)`
- HTTP route: `POST /api/v2.0/locations`
- Source controller: `IncidentIQ API`

Get my locations (filtered)

Returns locations accessible to the currently authenticated user with advanced filtering capabilities via request body. Supports custom filters and pagination.

**Supports Custom Filters:** Pass filter criteria in the request body for complex queries.

**Related Endpoints:**
- [GET /api/v2.0/locations](#/Locations/getMyLocationsV2) - Same endpoint with query parameters only

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |
| `product_id` | `ProductId` | `header` | `no` | `str` | `-` | Product context for the request |
| `body` | `body` | `body` | `no` | `GetUserLocationsRequest` | `GetUserLocationsRequest` | - |

#### Returns

- Typed call return: `LocationWithPermissionListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `LocationWithPermissionListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_my_locations_manage_filtered_v2`

Provenance: Golden OpenAPI contract

Operation ID: `getMyLocationsManageFilteredV2`

- Sync: `client.locations.get_my_locations_manage_filtered_v2(site_id=None, body=None, timeout=None)`
- Async: `await client.locations.get_my_locations_manage_filtered_v2(site_id=None, body=None, timeout=None)`
- Raw payload: `client.locations.get_my_locations_manage_filtered_v2.raw(site_id=None, body=None, timeout=None)`
- HTTP route: `POST /api/v2.0/locations/manage`
- Source controller: `IncidentIQ API`

Get my locations with manage permission (filtered)

Returns locations where the current user has ticket resolution permissions, with advanced filtering via request body. Use this endpoint to populate location dropdowns for ticket assignment and resolution interfaces.

**Permission Filter:** Automatically includes `HasResolveTicketsPermission: true` in the query.

**Workflow Example**
1. Build a `GetUserLocationsRequest` with optional filters (location type, paging).
2. Call this endpoint: [POST /api/v2.0/locations/manage](#/Locations/getMyLocationsManageFilteredV2) with the request body.
3. Use the returned locations to populate UI controls for ticket routing.

**Related Endpoints:**
- [GET /api/v2.0/locations/manage](#/Locations/getMyLocationsManageV2) - Same endpoint with query string filters
- [GET /api/v2.0/locations](#/Locations/getMyLocationsV2) - All accessible locations regardless of permission level

**Minimal Required Fields**: None (filters are optional).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |
| `body` | `body` | `body` | `no` | `GetUserLocationsRequest` | `GetUserLocationsRequest` | - |

#### Returns

- Typed call return: `LocationWithPermissionListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `LocationWithPermissionListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_my_locations_manage_v2`

Provenance: Golden OpenAPI contract

Operation ID: `getMyLocationsManageV2`

- Sync: `client.locations.get_my_locations_manage_v2(site_id=None, p=None, s=None, timeout=None)`
- Async: `await client.locations.get_my_locations_manage_v2(site_id=None, p=None, s=None, timeout=None)`
- Raw payload: `client.locations.get_my_locations_manage_v2.raw(site_id=None, p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v2.0/locations/manage`
- Source controller: `IncidentIQ API`

Get my locations with manage permission

Returns locations where the current user has ticket resolution (manage) permissions. This is a filtered view specifically for users who need to manage tickets at locations.

**Permission Filter:** Only returns locations where the user has `tickets.resolve` permission.

**Use Case:** Typically used to populate location dropdowns for ticket management interfaces.

**Related Endpoints:**
- [GET /api/v2.0/locations](#/Locations/getMyLocationsV2) - All accessible locations
- [POST /api/v2.0/locations/manage](#/Locations/getMyLocationsManageFilteredV2) - Same with request body filters

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index |
| `s` | `$s` | `query` | `no` | `int` | `-` | Page size |

#### Returns

- Typed call return: `LocationWithPermissionListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `LocationWithPermissionListResponse`
- Pagination helper: `client.locations.get_my_locations_manage_v2.iter_pages(start_page=1, page_size=100, max_pages=None, site_id=None, p=None, s=None, timeout=None)`

---

### `get_my_locations_v2`

Provenance: Golden OpenAPI contract

Operation ID: `getMyLocationsV2`

- Sync: `client.locations.get_my_locations_v2(site_id=None, product_id=None, p=None, s=None, timeout=None)`
- Async: `await client.locations.get_my_locations_v2(site_id=None, product_id=None, p=None, s=None, timeout=None)`
- Raw payload: `client.locations.get_my_locations_v2.raw(site_id=None, product_id=None, p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v2.0/locations`
- Source controller: `IncidentIQ API`

Get my locations

Returns locations accessible to the currently authenticated user, including their effective permissions for each location. Results include permission flags indicating what actions the user can perform at each location.

**Supports Custom Filters:** This endpoint accepts filter parameters in query string format.

**Related Endpoints:**
- [POST /api/v2.0/locations](#/Locations/getMyLocationsFilteredV2) - Same endpoint with request body filters
- [GET /api/v2.0/locations/view](#/Locations/getMyLocationsViewV2) - Alias endpoint

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |
| `product_id` | `ProductId` | `header` | `no` | `str` | `-` | Product context for the request |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index |
| `s` | `$s` | `query` | `no` | `int` | `-` | Page size (number of records per page) |

#### Returns

- Typed call return: `LocationWithPermissionListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `LocationWithPermissionListResponse`
- Pagination helper: `client.locations.get_my_locations_v2.iter_pages(start_page=1, page_size=100, max_pages=None, site_id=None, product_id=None, p=None, s=None, timeout=None)`

---

### `get_my_locations_view_filtered_v2`

Provenance: Golden OpenAPI contract

Operation ID: `getMyLocationsViewFilteredV2`

- Sync: `client.locations.get_my_locations_view_filtered_v2(site_id=None, body=None, timeout=None)`
- Async: `await client.locations.get_my_locations_view_filtered_v2(site_id=None, body=None, timeout=None)`
- Raw payload: `client.locations.get_my_locations_view_filtered_v2.raw(site_id=None, body=None, timeout=None)`
- HTTP route: `POST /api/v2.0/locations/view`
- Source controller: `IncidentIQ API`

Get my locations (view, filtered)

Returns locations accessible to the current user with advanced filtering via request body. This is the view alias of [POST /api/v2.0/locations](#/Locations/getMyLocationsFilteredV2) and includes permission metadata for each location.

**Workflow Example**
1. Build a `GetUserLocationsRequest` with filter criteria (location type, permissions, paging).
2. Submit: [POST /api/v2.0/locations/view](#/Locations/getMyLocationsViewFilteredV2).
3. Use the returned list to populate location pickers with permission flags.

**Minimal Required Fields**: None. Filters are optional.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |
| `body` | `body` | `body` | `no` | `GetUserLocationsRequest` | `GetUserLocationsRequest` | - |

#### Returns

- Typed call return: `LocationWithPermissionListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `LocationWithPermissionListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_my_locations_view_v2`

Provenance: Golden OpenAPI contract

Operation ID: `getMyLocationsViewV2`

- Sync: `client.locations.get_my_locations_view_v2(site_id=None, p=None, s=None, timeout=None)`
- Async: `await client.locations.get_my_locations_view_v2(site_id=None, p=None, s=None, timeout=None)`
- Raw payload: `client.locations.get_my_locations_view_v2.raw(site_id=None, p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v2.0/locations/view`
- Source controller: `IncidentIQ API`

Get my locations (view)

Alias for [GET /api/v2.0/locations](#/Locations/getMyLocationsV2). Returns locations accessible to the currently authenticated user with permission information. Results include permission flags indicating what actions the user can perform at each location.

**Note:** This endpoint is functionally identical to `/api/v2.0/locations` and exists for backward compatibility with older integrations.

**Workflow Example**
1. Call this endpoint: [GET /api/v2.0/locations/view](#/Locations/getMyLocationsViewV2) with optional paging parameters.
2. Process results using permission flags (`CanView`, `CanManage`, etc.) to filter UI options.
3. Use `LocationId` values from response for subsequent location-specific API calls.

**Related Endpoints:**
- [POST /api/v2.0/locations/view](#/Locations/getMyLocationsViewFilteredV2) - Same endpoint with request body filters
- [GET /api/v2.0/locations](#/Locations/getMyLocationsV2) - Primary endpoint (this is an alias)

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index |
| `s` | `$s` | `query` | `no` | `int` | `-` | Page size |

#### Returns

- Typed call return: `LocationWithPermissionListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `LocationWithPermissionListResponse`
- Pagination helper: `client.locations.get_my_locations_view_v2.iter_pages(start_page=1, page_size=100, max_pages=None, site_id=None, p=None, s=None, timeout=None)`

---

### `get_site_locations_by_site_id_filtered_v2`

Provenance: Golden OpenAPI contract

Operation ID: `getSiteLocationsBySiteIdFilteredV2`

- Sync: `client.locations.get_site_locations_by_site_id_filtered_v2(site_id=..., body=None, timeout=None)`
- Async: `await client.locations.get_site_locations_by_site_id_filtered_v2(site_id=..., body=None, timeout=None)`
- Raw payload: `client.locations.get_site_locations_by_site_id_filtered_v2.raw(site_id=..., body=None, timeout=None)`
- HTTP route: `POST /api/v2.0/locations/all/{siteId}`
- Source controller: `IncidentIQ API`

Get locations by site ID (filtered)

Returns locations for a specific site with advanced filtering via request body. Useful for cross-site location lookups or integration scenarios.

**Anonymous Access:** This endpoint allows anonymous requests when the site is configured to permit it. When anonymous, only basic location information is returned.

**Prerequisites**
1. **siteId** - Use [GET /api/v1.0/sites](#/Sites/getSiteByUrl) to retrieve available sites and extract `Item.SiteId`.

**Workflow Example**
1. List sites: [GET /api/v1.0/sites](#/Sites/getSiteByUrl) → extract `Item.SiteId`
2. Build filter request with optional `LocationTypeId` and paging.
3. Call this endpoint: [POST /api/v2.0/locations/all/{siteId}](#/Locations/getSiteLocationsBySiteIdFilteredV2) with request body.

**Related Endpoints:**
- [GET /api/v2.0/locations/all/{siteId}](#/Locations/getSiteLocationsBySiteIdV2) - Same endpoint with query string filters

**Minimal Required Fields**: None (filters are optional).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `site_id` | `siteId` | `path` | `yes` | `str` | `-` | Unique identifier of the site whose locations to retrieve |
| `body` | `body` | `body` | `no` | `GetUserLocationsRequest` | `GetUserLocationsRequest` | - |

#### Returns

- Typed call return: `LocationListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `LocationListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_site_locations_by_site_id_v2`

Provenance: Golden OpenAPI contract

Operation ID: `getSiteLocationsBySiteIdV2`

- Sync: `client.locations.get_site_locations_by_site_id_v2(site_id=..., p=None, s=None, timeout=None)`
- Async: `await client.locations.get_site_locations_by_site_id_v2(site_id=..., p=None, s=None, timeout=None)`
- Raw payload: `client.locations.get_site_locations_by_site_id_v2.raw(site_id=..., p=None, s=None, timeout=None)`
- HTTP route: `GET /api/v2.0/locations/all/{siteId}`
- Source controller: `IncidentIQ API`

Get locations by site ID

Returns all locations for a specific site identified by its SiteId. This endpoint allows anonymous access for certain public-facing scenarios (e.g., location selectors on login pages).

**Anonymous Access:** This endpoint allows anonymous requests when the site is configured to permit it. When anonymous, only basic location information is returned.

**Supports Custom Filters:** This endpoint accepts filter parameters.

**Use Cases:**
- Populating location dropdowns on public forms
- Cross-site location lookups by administrators
- Integration scenarios requiring location data without user context

**Related Endpoints:**
- [GET /api/v2.0/locations/all](#/Locations/getAllSiteLocationsV2) - Get locations for current site context

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `site_id` | `siteId` | `path` | `yes` | `str` | `-` | Unique identifier of the site whose locations to retrieve |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index |
| `s` | `$s` | `query` | `no` | `int` | `-` | Page size (number of records per page) |

#### Returns

- Typed call return: `LocationListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `LocationListResponse`
- Pagination helper: `client.locations.get_site_locations_by_site_id_v2.iter_pages(start_page=1, page_size=100, max_pages=None, site_id=..., p=None, s=None, timeout=None)`

---

### `migrate_location_v2`

Provenance: Golden OpenAPI contract

Operation ID: `migrateLocationV2`

- Sync: `client.locations.migrate_location_v2(site_id=None, body=..., timeout=None)`
- Async: `await client.locations.migrate_location_v2(site_id=None, body=..., timeout=None)`
- Raw payload: `client.locations.migrate_location_v2.raw(site_id=None, body=..., timeout=None)`
- HTTP route: `POST /api/v2.0/locations/migrate`
- Source controller: `IncidentIQ API`

Migrate location entities

Migrates assets, tickets, users, and/or parts from one location to other locations. Use this before deleting or decommissioning a location to reassign associated entities.

**Migration Behavior:**
- Each entity type (assets, tickets, users, parts) can be migrated to a different destination location
- Only include destination fields for entity types you want to migrate
- Omitted or null destination fields mean those entities will not be migrated

**Workflow:**
1. Identify the source location to decommission
2. Select destination locations for each entity type
3. Call this endpoint to perform the migration
4. Verify migration success
5. Delete the source location if desired

**Related Endpoints:**
- [DELETE /api/v2.0/locations/{LocationId}/delete](#/Locations/deleteLocationV2) - Delete location after migration

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |
| `body` | `body` | `body` | `yes` | `MigrateLocationRequest` | `MigrateLocationRequest` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `query_location_rooms`

Provenance: Golden OpenAPI contract

Operation ID: `queryLocationRooms`

- Sync: `client.locations.query_location_rooms(site_id=None, body=None, timeout=None)`
- Async: `await client.locations.query_location_rooms(site_id=None, body=None, timeout=None)`
- Raw payload: `client.locations.query_location_rooms.raw(site_id=None, body=None, timeout=None)`
- HTTP route: `POST /api/v2.0/locations/rooms/query`
- Source controller: `IncidentIQ API`

Query rooms

Retrieves all rooms for the current site with optional filtering, sorting, and pagination. Rooms are spaces within locations that can be reserved or assigned.

**Filtering Options:**
- `LocationId` - Filter by parent location UUID
- `StartDatetime` / `EndDatetime` - Filter by availability window for reservations
- `MaximumOccupancy` - Filter by minimum seating capacity

**Workflow Example**
1. Get available locations: [GET /api/v2.0/locations](#/Locations/getMyLocationsV2) → extract `LocationId`.
2. Build request with optional filters (`LocationId`, `MaximumOccupancy`, paging).
3. Call this endpoint: [POST /api/v2.0/locations/rooms/query](#/Locations/queryLocationRooms) with request body.
4. Use returned `LocationRoomId` values for room-specific operations.

**Related Endpoints:**
- [POST /api/v2.0/locations/rooms/for/user](#/Locations/queryLocationRoomsForUser) - Query rooms for current user
- [GET /api/v2.0/locations/rooms/{LocationRoomId}](#/Locations/getLocationRoomById) - Get specific room details

**Minimal Required Fields**: None (all filters are optional).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |
| `body` | `body` | `body` | `no` | `GetLocationRoomsRequest` | `GetLocationRoomsRequest` | - |

#### Returns

- Typed call return: `LocationRoomListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `LocationRoomListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `query_location_rooms_by_location_id`

Provenance: Golden OpenAPI contract

Operation ID: `queryLocationRoomsByLocationId`

- Sync: `client.locations.query_location_rooms_by_location_id(location_id=..., site_id=None, body=None, timeout=None)`
- Async: `await client.locations.query_location_rooms_by_location_id(location_id=..., site_id=None, body=None, timeout=None)`
- Raw payload: `client.locations.query_location_rooms_by_location_id.raw(location_id=..., site_id=None, body=None, timeout=None)`
- HTTP route: `POST /api/v2.0/locations/{locationId}/rooms`
- Source controller: `IncidentIQ API`

Query rooms by location

Returns rooms for a specific location (building/school), with optional filters for availability or capacity. Use this when scoping room selection to a single location.

**Prerequisites**
1. **locationId** - Use [GET /api/v2.0/locations](#/Locations/getMyLocationsV2) or [POST /api/v2.0/locations/view](#/Locations/getMyLocationsViewFilteredV2) and extract `Items[].LocationId`.

**Workflow Example**
1. Identify the location the user selected.
2. (Optional) Build `GetLocationRoomsRequest` with filters such as `StartDatetime`/`EndDatetime`.
3. Submit: [POST /api/v2.0/locations/{locationId}/rooms](#/Locations/queryLocationRoomsByLocationId).

**Minimal Required Fields**: locationId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `location_id` | `locationId` | `path` | `yes` | `str` | `-` | The location ID to retrieve rooms for |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |
| `body` | `body` | `body` | `no` | `GetLocationRoomsRequest` | `GetLocationRoomsRequest` | - |

#### Returns

- Typed call return: `LocationRoomListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `LocationRoomListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `query_location_rooms_for_user`

Provenance: Golden OpenAPI contract

Operation ID: `queryLocationRoomsForUser`

- Sync: `client.locations.query_location_rooms_for_user(site_id=None, body=None, timeout=None)`
- Async: `await client.locations.query_location_rooms_for_user(site_id=None, body=None, timeout=None)`
- Raw payload: `client.locations.query_location_rooms_for_user.raw(site_id=None, body=None, timeout=None)`
- HTTP route: `POST /api/v2.0/locations/rooms/for/user`
- Source controller: `IncidentIQ API`

Query rooms for current user

Returns rooms the current user can access, using permission rules and optional request-body filters. Use this for room pickers where visibility must respect the user's site/location access.

**Workflow Example**
1. (Optional) Build a `GetLocationRoomsRequest` with filters such as `LocationId` or availability window.
2. Submit: [POST /api/v2.0/locations/rooms/for/user](#/Locations/queryLocationRoomsForUser).
3. Use the returned list to populate UI selectors or availability checks.

**Minimal Required Fields**: None. Filters are optional.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |
| `body` | `body` | `body` | `no` | `GetLocationRoomsRequest` | `GetLocationRoomsRequest` | - |

#### Returns

- Typed call return: `LocationRoomListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `LocationRoomListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `undelete_location_room`

Provenance: Golden OpenAPI contract

Operation ID: `undeleteLocationRoom`

- Sync: `client.locations.undelete_location_room(room_id=..., site_id=None, timeout=None)`
- Async: `await client.locations.undelete_location_room(room_id=..., site_id=None, timeout=None)`
- Raw payload: `client.locations.undelete_location_room.raw(room_id=..., site_id=None, timeout=None)`
- HTTP route: `POST /api/v2.0/locations/rooms/{roomId}/undelete`
- Source controller: `IncidentIQ API`

Undelete a room

Restores a previously soft-deleted room so it appears in active room lists again. Use this when a room was removed in error or when a room becomes available again.

**Prerequisites**
1. **roomId** - Use [POST /api/v2.0/locations/rooms/query](#/Locations/queryLocationRooms) with filters that include deleted rooms (if supported) to identify the room ID.

**Workflow Example**
1. Identify the deleted room ID.
2. Restore: [POST /api/v2.0/locations/rooms/{roomId}/undelete](#/Locations/undeleteLocationRoom).
3. Verify the room appears in standard queries.

**Minimal Required Fields**: roomId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `room_id` | `roomId` | `path` | `yes` | `str` | `-` | The unique identifier of the room to restore |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `undelete_location_v2`

Provenance: Golden OpenAPI contract

Operation ID: `undeleteLocationV2`

- Sync: `client.locations.undelete_location_v2(location_id=..., site_id=None, timeout=None)`
- Async: `await client.locations.undelete_location_v2(location_id=..., site_id=None, timeout=None)`
- Raw payload: `client.locations.undelete_location_v2.raw(location_id=..., site_id=None, timeout=None)`
- HTTP route: `PUT /api/v2.0/locations/{LocationId}/undelete`
- Source controller: `IncidentIQ API`

Restore deleted location

Restores a previously soft-deleted location. The location will be returned to active status and will appear in standard location lists again.

**Note:** This operation only works on soft-deleted locations. Permanently deleted locations cannot be restored.

**Related Endpoints:**
- [DELETE /api/v2.0/locations/{LocationId}/delete](#/Locations/deleteLocationV2) - Soft-delete a location

**Prerequisites**
1. **LocationId** - Use [GET /api/v2.0/locations](#/Locations/getMyLocationsV2) to obtain. Extract `Items[].LocationId` from response.

**Workflow Example**
1. Obtain LocationId: [GET /api/v2.0/locations](#/Locations/getMyLocationsV2) → extract `Items[].LocationId`
2. Call this endpoint: [PUT /api/v2.0/locations/{LocationId}/undelete](#/Locations/undeleteLocationV2)

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `location_id` | `LocationId` | `path` | `yes` | `str` | `-` | Unique identifier of the location to restore |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |

#### Returns

- Typed call return: `LocationItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `LocationItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_location_floorplans_v2`

Provenance: Golden OpenAPI contract

Operation ID: `updateLocationFloorplansV2`

- Sync: `client.locations.update_location_floorplans_v2(location_id=..., site_id=None, body=..., timeout=None)`
- Async: `await client.locations.update_location_floorplans_v2(location_id=..., site_id=None, body=..., timeout=None)`
- Raw payload: `client.locations.update_location_floorplans_v2.raw(location_id=..., site_id=None, body=..., timeout=None)`
- HTTP route: `POST /api/v2.0/locations/{locationId}/floorplans`
- Source controller: `IncidentIQ API`

Update location floorplans

Updates the floorplan files associated with a location. This operation replaces the existing floorplan associations - files not included in the request will be disassociated.

**Workflow:**
1. Upload files using the file upload endpoints first
2. Obtain FileIds from the upload responses
3. Call this endpoint with the FileIds and optional descriptions

**Note:** This endpoint manages the association between files and the location. The files themselves must be uploaded separately.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `location_id` | `locationId` | `path` | `yes` | `str` | `-` | Unique identifier of the location |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |
| `body` | `body` | `body` | `yes` | `UpdateEntityFileDetailsRequest` | `UpdateEntityFileDetailsRequest` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_location_images_v2`

Provenance: Golden OpenAPI contract

Operation ID: `updateLocationImagesV2`

- Sync: `client.locations.update_location_images_v2(location_id=..., site_id=None, body=..., timeout=None)`
- Async: `await client.locations.update_location_images_v2(location_id=..., site_id=None, body=..., timeout=None)`
- Raw payload: `client.locations.update_location_images_v2.raw(location_id=..., site_id=None, body=..., timeout=None)`
- HTTP route: `POST /api/v2.0/locations/{locationId}/images`
- Source controller: `IncidentIQ API`

Update location images

Updates the image files associated with a location. This operation replaces the existing image associations - files not included in the request will be disassociated.

**Workflow:**
1. Upload image files using the file upload endpoints first
2. Obtain FileIds from the upload responses
3. Call this endpoint with the FileIds and optional descriptions

**Note:** This endpoint manages the association between files and the location. The files themselves must be uploaded separately.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `location_id` | `locationId` | `path` | `yes` | `str` | `-` | Unique identifier of the location |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |
| `body` | `body` | `body` | `yes` | `UpdateEntityFileDetailsRequest` | `UpdateEntityFileDetailsRequest` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_location_room`

Provenance: Golden OpenAPI contract

Operation ID: `updateLocationRoom`

- Sync: `client.locations.update_location_room(room_id=..., site_id=None, body=..., timeout=None)`
- Async: `await client.locations.update_location_room(room_id=..., site_id=None, body=..., timeout=None)`
- Raw payload: `client.locations.update_location_room.raw(room_id=..., site_id=None, body=..., timeout=None)`
- HTTP route: `POST /api/v2.0/locations/rooms/{roomId}`
- Source controller: `IncidentIQ API`

Update a room

Updates an existing room's properties such as name, capacity, type, or status. Use this to keep room metadata aligned with real-world changes.

**Prerequisites**
1. **roomId** - Use [POST /api/v2.0/locations/rooms/query](#/Locations/queryLocationRooms) and extract `Items[].LocationRoomId`.

**Workflow Example**
1. Load current room details: [GET /api/v2.0/locations/rooms/{roomId}](#/Locations/getLocationRoomById).
2. Modify fields in `UpdateLocationRoomRequest`.
3. Save changes: [POST /api/v2.0/locations/rooms/{roomId}](#/Locations/updateLocationRoom).

**Minimal Required Fields**: roomId (path) plus at least one field to update.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `room_id` | `roomId` | `path` | `yes` | `str` | `-` | The unique identifier of the room to update |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |
| `body` | `body` | `body` | `yes` | `UpdateLocationRoomRequest` | `UpdateLocationRoomRequest` | - |

#### Returns

- Typed call return: `LocationRoomItemUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `LocationRoomItemUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_location_room_available_times`

Provenance: Golden OpenAPI contract

Operation ID: `updateLocationRoomAvailableTimes`

- Sync: `client.locations.update_location_room_available_times(location_room_id=..., site_id=None, body=..., timeout=None)`
- Async: `await client.locations.update_location_room_available_times(location_room_id=..., site_id=None, body=..., timeout=None)`
- Raw payload: `client.locations.update_location_room_available_times.raw(location_room_id=..., site_id=None, body=..., timeout=None)`
- HTTP route: `POST /api/v2.0/locations/rooms/{locationRoomId}/available-times`
- Source controller: `IncidentIQ API`

Update room available times

Updates the weekly availability schedule for a room. Use this to set open/closed hours or to adjust booking windows.

**Prerequisites**
1. **locationRoomId** - Use [POST /api/v2.0/locations/rooms/query](#/Locations/queryLocationRooms) and extract `Items[].LocationRoomId`.

**Workflow Example**
1. Build an array of `UpdateLocationRoomAvailableTimeRequest` entries.
2. Submit: [POST /api/v2.0/locations/rooms/{locationRoomId}/available-times](#/Locations/updateLocationRoomAvailableTimes).
3. Re-fetch the schedule to confirm updates.

**Minimal Required Fields**: locationRoomId (path) and an availability array in the body.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `location_room_id` | `locationRoomId` | `path` | `yes` | `str` | `-` | The unique identifier of the room |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | - |

#### Returns

- Typed call return: `LocationRoomAvailableTimeListUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `LocationRoomAvailableTimeListUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_location_room_images`

Provenance: Golden OpenAPI contract

Operation ID: `updateLocationRoomImages`

- Sync: `client.locations.update_location_room_images(location_room_id=..., site_id=None, body=..., timeout=None)`
- Async: `await client.locations.update_location_room_images(location_room_id=..., site_id=None, body=..., timeout=None)`
- Raw payload: `client.locations.update_location_room_images.raw(location_room_id=..., site_id=None, body=..., timeout=None)`
- HTTP route: `POST /api/v2.0/locations/rooms/{locationRoomId}/images`
- Source controller: `IncidentIQ API`

Update room images

Updates the image files associated with a room, replacing the existing image list. Use this after uploading new room photos.

**Prerequisites**
1. **locationRoomId** - Use [POST /api/v2.0/locations/rooms/query](#/Locations/queryLocationRooms) and extract `Items[].LocationRoomId`.
2. **FileId list** - Upload image files and capture the `FileId` values.

**Workflow Example**
1. Upload new images and capture their IDs.
2. Build `UpdateEntityFileDetailsRequest` with `FileData` entries.
3. Submit: [POST /api/v2.0/locations/rooms/{locationRoomId}/images](#/Locations/updateLocationRoomImages).

**Minimal Required Fields**: locationRoomId (path) and `FileData` in the body.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `location_room_id` | `locationRoomId` | `path` | `yes` | `str` | `-` | The unique identifier of the room |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |
| `body` | `body` | `body` | `yes` | `UpdateEntityFileDetailsRequest` | `UpdateEntityFileDetailsRequest` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_location_room_layouts`

Provenance: Golden OpenAPI contract

Operation ID: `updateLocationRoomLayouts`

- Sync: `client.locations.update_location_room_layouts(location_room_id=..., site_id=None, body=..., timeout=None)`
- Async: `await client.locations.update_location_room_layouts(location_room_id=..., site_id=None, body=..., timeout=None)`
- Raw payload: `client.locations.update_location_room_layouts.raw(location_room_id=..., site_id=None, body=..., timeout=None)`
- HTTP route: `POST /api/v2.0/locations/rooms/{locationRoomId}/layouts`
- Source controller: `IncidentIQ API`

Update room layouts

Updates the floorplan/layout files associated with a room, replacing the existing layout list. Use this after uploading new layout files to keep room diagrams current.

**Prerequisites**
1. **locationRoomId** - Use [POST /api/v2.0/locations/rooms/query](#/Locations/queryLocationRooms) and extract `Items[].LocationRoomId`.
2. **FileId list** - Upload files using your file upload workflow and capture the `FileId` values.

**Workflow Example**
1. Upload new layout files and capture their IDs.
2. Build `UpdateEntityFileDetailsRequest` with `FileData` entries.
3. Submit: [POST /api/v2.0/locations/rooms/{locationRoomId}/layouts](#/Locations/updateLocationRoomLayouts).

**Minimal Required Fields**: locationRoomId (path) and `FileData` in the body.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `location_room_id` | `locationRoomId` | `path` | `yes` | `str` | `-` | The unique identifier of the room |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |
| `body` | `body` | `body` | `yes` | `UpdateEntityFileDetailsRequest` | `UpdateEntityFileDetailsRequest` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_location_rooms_batch`

Provenance: Golden OpenAPI contract

Operation ID: `updateLocationRoomsBatch`

- Sync: `client.locations.update_location_rooms_batch(site_id=None, body=..., timeout=None)`
- Async: `await client.locations.update_location_rooms_batch(site_id=None, body=..., timeout=None)`
- Raw payload: `client.locations.update_location_rooms_batch.raw(site_id=None, body=..., timeout=None)`
- HTTP route: `POST /api/v2.0/locations/rooms/update/batch`
- Source controller: `IncidentIQ API`

Update multiple rooms

Updates multiple rooms in a single batch operation. Each entry must include `LocationRoomId`, allowing bulk updates for capacity, status, or naming changes.

**Prerequisites**
1. **LocationRoomId list** - Use [POST /api/v2.0/locations/rooms/query](#/Locations/queryLocationRooms) and extract `Items[].LocationRoomId`.

**Workflow Example**
1. Query rooms to collect IDs.
2. Build an array of `UpdateLocationRoomRequest` objects with updated fields.
3. Submit: [POST /api/v2.0/locations/rooms/update/batch](#/Locations/updateLocationRoomsBatch).

**Minimal Required Fields**: Each item must include `LocationRoomId` plus at least one field to update.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | - |

#### Returns

- Typed call return: `GuidListUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `GuidListUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_location_v2`

Provenance: Golden OpenAPI contract

Operation ID: `updateLocationV2`

- Sync: `client.locations.update_location_v2(location_id=..., site_id=None, product_id=None, body=..., timeout=None)`
- Async: `await client.locations.update_location_v2(location_id=..., site_id=None, product_id=None, body=..., timeout=None)`
- Raw payload: `client.locations.update_location_v2.raw(location_id=..., site_id=None, product_id=None, body=..., timeout=None)`
- HTTP route: `POST /api/v2.0/locations/{LocationId}/update`
- Source controller: `IncidentIQ API`

Update location

Updates an existing location. Only include fields you want to modify - omitted fields will retain their current values.

**Address Handling:** If address fields are provided, the location's address will be updated. If the location doesn't have an address, one will be created.

**Custom Fields:** To update custom field values, set `UpdateCustomFields: true` and include the `CustomFieldValues` array with the fields to update.

**Note:** This endpoint uses POST method (not PUT/PATCH) following the IncidentIQ API convention.

**Prerequisites**
1. **LocationId** - Use [GET /api/v2.0/locations](#/Locations/getMyLocationsV2) to obtain. Extract `Items[].LocationId` from response.

**Workflow Example**
1. Obtain LocationId: [GET /api/v2.0/locations](#/Locations/getMyLocationsV2) → extract `Items[].LocationId`
2. Call this endpoint: [POST /api/v2.0/locations/{LocationId}/update](#/Locations/updateLocationV2)

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `location_id` | `LocationId` | `path` | `yes` | `str` | `-` | Unique identifier of the location to update |
| `site_id` | `SiteId` | `header` | `no` | `str` | `-` | Site context for the request |
| `product_id` | `ProductId` | `header` | `no` | `str` | `-` | Product context for the request |
| `body` | `body` | `body` | `yes` | `UpdateLocationRequest` | `UpdateLocationRequest` | - |

#### Returns

- Typed call return: `LocationUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `LocationUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
