# `events` Golden Namespace

Sync client access: `client.events`

Async client access: `client.events` with `await` on method calls.

These methods are Golden because they come from the bundled Incident IQ OpenAPI contract.

## Methods

### `add_event_series_dates`

Provenance: Golden OpenAPI contract

Operation ID: `addEventSeriesDates`

- Sync: `client.events.add_event_series_dates(body=..., timeout=None)`
- Async: `await client.events.add_event_series_dates(body=..., timeout=None)`
- Raw payload: `client.events.add_event_series_dates.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/events/series/add-dates`
- Source controller: `IncidentIQ API`

Add dates to event series

Adds additional schedules to an existing event series. This is used to extend recurring or multi-date events without recreating the series.

**Prerequisites**
1. **ParentEventId** - Use [GET /api/v1.0/events/{EventId}](#/Events/getEvent) to confirm the series parent and extract the `EventId`.

**Workflow Example**
1. Get series parent: [GET /api/v1.0/events/{EventId}](#/Events/getEvent).
2. Build `AdditionalSchedules` entries with new date ranges.
3. Add dates: [POST /api/v1.0/events/series/add-dates](#/Events/addEventSeriesDates).

**Minimal Required Fields**: `ParentEventId`, `AdditionalSchedules` (each with `StartDateTime` and `EndDateTime`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `AddEventSeriesDatesRequest` | `AddEventSeriesDatesRequest` | - |

#### Returns

- Typed call return: `EventUpdateValidationListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `EventUpdateValidationListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `calculate_event_fees`

Provenance: Golden OpenAPI contract

Operation ID: `calculateEventFees`

- Sync: `client.events.calculate_event_fees(event_id=..., timeout=None)`
- Async: `await client.events.calculate_event_fees(event_id=..., timeout=None)`
- Raw payload: `client.events.calculate_event_fees.raw(event_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/events/{EventId}/calculate-fees`
- Source controller: `IncidentIQ API`

Calculate event fees

Triggers fee calculation for a specific event and returns the outcome in an action response. This endpoint is deprecated but still used by legacy workflows that need to recompute fee totals on demand.

**Prerequisites**
1. **EventId** - Use [POST /api/v1.0/events/query](#/Events/getEventsByQueryPost) and extract `Items[].EventId`.

**Workflow Example**
1. Locate event: [POST /api/v1.0/events/query](#/Events/getEventsByQueryPost) -> extract `Items[].EventId`.
2. Trigger fee calc: [POST /api/v1.0/events/{EventId}/calculate-fees](#/Events/calculateEventFees).
3. Review the action response for success or errors.

**Minimal Required Fields**: EventId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `event_id` | `EventId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_event`

Provenance: Golden OpenAPI contract

Operation ID: `createEvent`

- Sync: `client.events.create_event(body=..., timeout=None)`
- Async: `await client.events.create_event(body=..., timeout=None)`
- Raw payload: `client.events.create_event.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/events/new`
- Source controller: `IncidentIQ API`

Create event

Creates a single event record, including schedule, location, and metadata details. Use this endpoint for creating one-off events or as a precursor to building a recurring series.

**Prerequisites**
- If setting **EventTypeId**, use [POST /api/v1.0/events/types/query](#/Events/getEventTypesByQueryPost) to obtain `Items[].EventTypeId`.
- If assigning an **OwnerId**, use [POST /api/v1.0/users](#/Users/searchUsers) and extract `Items[].UserId`.

**Workflow Example**
1. (Optional) Lookup event types and owner user ID.
2. Build an `UpdateEventRequest` with schedule fields and metadata.
3. Create the event: [POST /api/v1.0/events/new](#/Events/createEvent).

**Minimal Required Fields**: `StartDateTime`, `EndDateTime`, plus any tenant-required metadata (commonly `SiteId`, `Title`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `UpdateEventRequest` | `UpdateEventRequest` | - |

#### Returns

- Typed call return: `EventItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `EventItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_event_series`

Provenance: Golden OpenAPI contract

Operation ID: `createEventSeries`

- Sync: `client.events.create_event_series(body=..., timeout=None)`
- Async: `await client.events.create_event_series(body=..., timeout=None)`
- Raw payload: `client.events.create_event_series.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/events/series/new`
- Source controller: `IncidentIQ API`

Create event series

Creates a new event series (recurring or multi-date) in a single request. Use this endpoint to define the shared event metadata once and provide the primary schedule plus any additional schedules that should be generated as part of the series.

**Prerequisites**
- If setting **EventTypeId**, use [POST /api/v1.0/events/types/query](#/Events/getEventTypesByQueryPost) to obtain `Items[].EventTypeId`.
- If assigning an **OwnerId**, use [POST /api/v1.0/users](#/Users/searchUsers) and extract `Items[].UserId`.

**Workflow Example**
1. (Optional) Lookup event types and owner user ID.
2. Build `CreateEventSeriesRequest` with shared fields plus `Series.PrimarySchedule` and any `Series.AdditionalSchedules`.
3. Create series: [POST /api/v1.0/events/series/new](#/Events/createEventSeries).

**Minimal Required Fields**: `SiteId`, `Title`, and `Series.PrimarySchedule` (`StartDateTime`, `EndDateTime`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `CreateEventSeriesRequest` | `CreateEventSeriesRequest` | - |

#### Returns

- Typed call return: `EventItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `EventItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_event_type`

Provenance: Golden OpenAPI contract

Operation ID: `createEventType`

- Sync: `client.events.create_event_type(body=..., timeout=None)`
- Async: `await client.events.create_event_type(body=..., timeout=None)`
- Raw payload: `client.events.create_event_type.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/events/types`
- Source controller: `IncidentIQ API`

Create event type

Creates a single event type category. Use this to add new classifications for events and to control visibility via the scope setting.

**Workflow Example**
1. Build an `UpdateEventTypeRequest` with `Name`, `Scope`, and optional `Icon`/`SiteId`.
2. Create type: [POST /api/v1.0/events/types](#/Events/createEventType).
3. Use the returned `EventTypeId` when creating events.

**Minimal Required Fields**: `Name` and `Scope` (plus optional `SiteId`/`Icon`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `UpdateEventTypeRequest` | `UpdateEventTypeRequest` | - |

#### Returns

- Typed call return: `EventTypeItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `EventTypeItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_event_types`

Provenance: Golden OpenAPI contract

Operation ID: `createEventTypes`

- Sync: `client.events.create_event_types(body=..., timeout=None)`
- Async: `await client.events.create_event_types(body=..., timeout=None)`
- Raw payload: `client.events.create_event_types.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/events/types/ids`
- Source controller: `IncidentIQ API`

Create multiple event types

Creates multiple event types in a single request. Each array entry is an `UpdateEventTypeRequest` payload describing one type.

**Workflow Example**
1. Build an array of event type payloads with `Name`, `Scope`, and optional `Icon` or `SiteId`.
2. Create types: [POST /api/v1.0/events/types/ids](#/Events/createEventTypes).
3. Use the returned identifiers to update event creation workflows.

**Minimal Required Fields**: Each item should include `Name` and `Scope` (plus optional `SiteId`/`Icon`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | - |

#### Returns

- Typed call return: `EventTypeBatchCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `EventTypeBatchCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_events`

Provenance: Golden OpenAPI contract

Operation ID: `createEvents`

- Sync: `client.events.create_events(body=..., timeout=None)`
- Async: `await client.events.create_events(body=..., timeout=None)`
- Raw payload: `client.events.create_events.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/events/ids`
- Source controller: `IncidentIQ API`

Create multiple events

Creates multiple events in a single request. Each array entry is an `UpdateEventRequest` payload representing one event, allowing bulk scheduling when importing or provisioning events in batches.

**Prerequisites**
- If setting **EventTypeId**, use [POST /api/v1.0/events/types/query](#/Events/getEventTypesByQueryPost) to obtain `Items[].EventTypeId`.
- If assigning an **OwnerId**, use [POST /api/v1.0/users](#/Users/searchUsers) and extract `Items[].UserId`.

**Workflow Example**
1. (Optional) Lookup event types and owners.
2. Build an array of `UpdateEventRequest` items with schedule fields and metadata.
3. Create events: [POST /api/v1.0/events/ids](#/Events/createEvents).

**Minimal Required Fields**: Array of `UpdateEventRequest` items. Each item should include scheduling fields (`StartDateTime`, `EndDateTime`) plus any tenant-required metadata (commonly `SiteId`, `Title`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | - |

#### Returns

- Typed call return: `EventBatchCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `EventBatchCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_event`

Provenance: Golden OpenAPI contract

Operation ID: `deleteEvent`

- Sync: `client.events.delete_event(event_id=..., timeout=None)`
- Async: `await client.events.delete_event(event_id=..., timeout=None)`
- Raw payload: `client.events.delete_event.raw(event_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/events/{EventId}`
- Source controller: `IncidentIQ API`

Delete event by ID

Deletes a single event by its identifier. For recurring series, delete a specific instance using [DELETE /api/v1.0/events/{EventId}/{instance}](#/Events/deleteRecurringEvent).

**Prerequisites**
1. **EventId** - Use [POST /api/v1.0/events/query](#/Events/getEventsByQueryPost) and extract `Items[].EventId`.

**Workflow Example**
1. Locate event: [POST /api/v1.0/events/query](#/Events/getEventsByQueryPost) -> extract `Items[].EventId`.
2. Delete event: [DELETE /api/v1.0/events/{EventId}](#/Events/deleteEvent).

**Minimal Required Fields**: EventId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `event_id` | `EventId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `EventsDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `EventsDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_event_type`

Provenance: Golden OpenAPI contract

Operation ID: `deleteEventType`

- Sync: `client.events.delete_event_type(event_type_id=..., timeout=None)`
- Async: `await client.events.delete_event_type(event_type_id=..., timeout=None)`
- Raw payload: `client.events.delete_event_type.raw(event_type_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/events/types/{EventTypeId}`
- Source controller: `IncidentIQ API`

Delete event type by ID

Deletes a single event type by its identifier. Use this to retire a category that should no longer be selectable for new events.

**Prerequisites**
1. **EventTypeId** - Use [POST /api/v1.0/events/types/query](#/Events/getEventTypesByQueryPost) and extract `Items[].EventTypeId`.

**Workflow Example**
1. List event types: [POST /api/v1.0/events/types/query](#/Events/getEventTypesByQueryPost) -> extract `Items[].EventTypeId`.
2. Delete type: [DELETE /api/v1.0/events/types/{EventTypeId}](#/Events/deleteEventType).

**Minimal Required Fields**: EventTypeId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `event_type_id` | `EventTypeId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `EventsDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `EventsDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_event_types_by_ids`

Provenance: Golden OpenAPI contract

Operation ID: `deleteEventTypesByIds`

- Sync: `client.events.delete_event_types_by_ids(body=..., timeout=None)`
- Async: `await client.events.delete_event_types_by_ids(body=..., timeout=None)`
- Raw payload: `client.events.delete_event_types_by_ids.raw(body=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/events/types/ids`
- Source controller: `IncidentIQ API`

Delete event types by IDs

Deletes multiple event types by explicit ID list. Use this for deterministic cleanup when you already know the exact set of types to remove.

**Prerequisites**
1. **EventTypeIds** - Use [POST /api/v1.0/events/types/query](#/Events/getEventTypesByQueryPost) and extract `Items[].EventTypeId`.

**Workflow Example**
1. Query types: [POST /api/v1.0/events/types/query](#/Events/getEventTypesByQueryPost) -> extract `Items[].EventTypeId`.
2. Delete types: [DELETE /api/v1.0/events/types/ids](#/Events/deleteEventTypesByIds) with the ID array.

**Minimal Required Fields**: Array of EventTypeId values.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | - |

#### Returns

- Typed call return: `EventsDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `EventsDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_event_types_by_query`

Provenance: Golden OpenAPI contract

Operation ID: `deleteEventTypesByQuery`

- Sync: `client.events.delete_event_types_by_query(timeout=None)`
- Async: `await client.events.delete_event_types_by_query(timeout=None)`
- Raw payload: `client.events.delete_event_types_by_query.raw(timeout=None)`
- HTTP route: `DELETE /api/v1.0/events/types/query`
- Source controller: `IncidentIQ API`

Delete event types by query

Deletes event types that match the legacy query criteria. Use this only after validating the target set via the query endpoints to avoid unintended deletion.

**Workflow Example**
1. Preview candidates: [GET /api/v1.0/events/types/query](#/Events/getEventTypesByQueryGet) or [POST /api/v1.0/events/types/query](#/Events/getEventTypesByQueryPost).
2. Confirm filters.
3. Delete matches: [DELETE /api/v1.0/events/types/query](#/Events/deleteEventTypesByQuery).

**Minimal Required Fields**: None. Uses the same query criteria supported by the legacy GET endpoint.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `EventsDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `EventsDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_events_by_ids`

Provenance: Golden OpenAPI contract

Operation ID: `deleteEventsByIds`

- Sync: `client.events.delete_events_by_ids(body=..., timeout=None)`
- Async: `await client.events.delete_events_by_ids(body=..., timeout=None)`
- Raw payload: `client.events.delete_events_by_ids.raw(body=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/events/ids`
- Source controller: `IncidentIQ API`

Delete events by IDs

Deletes multiple events by explicit ID list. Use this when you already know the exact set of events to remove and want a deterministic delete action.

**Prerequisites**
1. **EventIds** - Use [POST /api/v1.0/events/query](#/Events/getEventsByQueryPost) and extract `Items[].EventId`.

**Workflow Example**
1. Query events: [POST /api/v1.0/events/query](#/Events/getEventsByQueryPost) -> extract `Items[].EventId`.
2. Delete events: [DELETE /api/v1.0/events/ids](#/Events/deleteEventsByIds) with the ID array.

**Minimal Required Fields**: Array of EventId values.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | - |

#### Returns

- Typed call return: `EventsDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `EventsDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_events_by_query`

Provenance: Golden OpenAPI contract

Operation ID: `deleteEventsByQuery`

- Sync: `client.events.delete_events_by_query(timeout=None)`
- Async: `await client.events.delete_events_by_query(timeout=None)`
- Raw payload: `client.events.delete_events_by_query.raw(timeout=None)`
- HTTP route: `DELETE /api/v1.0/events/query`
- Source controller: `IncidentIQ API`

Delete events by query

Deletes events that match the legacy query criteria. Use this endpoint only after you have confirmed the target set with the corresponding query endpoint.

**Workflow Example**
1. Preview candidates: [GET /api/v1.0/events/query](#/Events/getEventsByQueryGet) or [POST /api/v1.0/events/query](#/Events/getEventsByQueryPost).
2. Confirm the filter criteria.
3. Delete matches: [DELETE /api/v1.0/events/query](#/Events/deleteEventsByQuery).

**Minimal Required Fields**: None. Uses the same query criteria supported by the legacy GET endpoint.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `EventsDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `EventsDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_recurring_event`

Provenance: Golden OpenAPI contract

Operation ID: `deleteRecurringEvent`

- Sync: `client.events.delete_recurring_event(event_id=..., instance=..., timeout=None)`
- Async: `await client.events.delete_recurring_event(event_id=..., instance=..., timeout=None)`
- Raw payload: `client.events.delete_recurring_event.raw(event_id=..., instance=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/events/{EventId}/{instance}`
- Source controller: `IncidentIQ API`

Delete recurring event instance

Deletes a specific instance of a recurring event series by index. Use this to remove one occurrence without deleting the entire series or future instances.

**Prerequisites**
1. **EventId** - Use [POST /api/v1.0/events/query](#/Events/getEventsByQueryPost) and extract `Items[].EventId` for the series parent.

**Workflow Example**
1. Locate the series parent: [POST /api/v1.0/events/query](#/Events/getEventsByQueryPost) -> extract `Items[].EventId`.
2. Choose the instance index from the series schedule.
3. Delete the occurrence: [DELETE /api/v1.0/events/{EventId}/{instance}](#/Events/deleteRecurringEvent).

**Minimal Required Fields**: EventId and instance (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `event_id` | `EventId` | `path` | `yes` | `str` | `-` | - |
| `instance` | `instance` | `path` | `yes` | `int` | `-` | Instance index to delete. |

#### Returns

- Typed call return: `EventsDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `EventsDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_available_rooms`

Provenance: Golden OpenAPI contract

Operation ID: `getAvailableRooms`

- Sync: `client.events.get_available_rooms(timeout=None)`
- Async: `await client.events.get_available_rooms(timeout=None)`
- Raw payload: `client.events.get_available_rooms.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/events/available/rooms`
- Source controller: `IncidentIQ API`

Get available rooms

Returns rooms that are available for the specified time window and scheduling criteria. Use this endpoint to drive room selection UIs or to validate room availability before creating an event.

**Workflow Example**
1. Determine the desired schedule window and (optionally) the target locations.
2. Call [GET /api/v1.0/events/available/rooms](#/Events/getAvailableRooms) with the schedule query parameters supported by the API.
3. Use the returned room list to populate selection controls or validate a request.

**Minimal Required Fields**: None. Provide time window and location criteria via query parameters when available.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `dict[str, Any]`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_available_times`

Provenance: Golden OpenAPI contract

Operation ID: `getAvailableTimes`

- Sync: `client.events.get_available_times(timeout=None)`
- Async: `await client.events.get_available_times(timeout=None)`
- Raw payload: `client.events.get_available_times.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/events/available/times`
- Source controller: `IncidentIQ API`

Get available times

Returns available time slots for event scheduling within the specified criteria. Use this endpoint to suggest valid time ranges when users are selecting dates and times for events.

**Workflow Example**
1. Define the desired date range and any location or room constraints.
2. Call [GET /api/v1.0/events/available/times](#/Events/getAvailableTimes) with the appropriate query parameters.
3. Present the returned time slots to users or use them to validate a proposed schedule.

**Minimal Required Fields**: None. Provide scheduling constraints via query parameters when supported.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `dict[str, Any]`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_event`

Provenance: Golden OpenAPI contract

Operation ID: `getEvent`

- Sync: `client.events.get_event(event_id=..., timeout=None)`
- Async: `await client.events.get_event(event_id=..., timeout=None)`
- Raw payload: `client.events.get_event.raw(event_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/events/{EventId}`
- Source controller: `IncidentIQ API`

Get event by ID

Returns full details for a single event, including schedule, location, status, and related metadata. Use this when navigating from list views or when validating updates before modifying an event.

**Prerequisites**
1. **EventId** - Use [POST /api/v1.0/events/query](#/Events/getEventsByQueryPost) and extract `Items[].EventId`.

**Workflow Example**
1. Query events: [POST /api/v1.0/events/query](#/Events/getEventsByQueryPost) -> extract `Items[].EventId`.
2. Get details: [GET /api/v1.0/events/{EventId}](#/Events/getEvent).
3. (Optional) Update using [PUT /api/v1.0/events/{EventId}/update](#/Events/updateEvent).

**Minimal Required Fields**: EventId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `event_id` | `EventId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `EventItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `EventItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_event_attachments`

Provenance: Golden OpenAPI contract

Operation ID: `getEventAttachments`

- Sync: `client.events.get_event_attachments(event_id=..., timeout=None)`
- Async: `await client.events.get_event_attachments(event_id=..., timeout=None)`
- Raw payload: `client.events.get_event_attachments.raw(event_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/events/{EventId}/attachments`
- Source controller: `IncidentIQ API`

Get event attachments

Returns the list of file attachments associated with an event. Use this to display uploaded documents, images, or approval artifacts tied to the event.

**Prerequisites**
1. **EventId** - Use [POST /api/v1.0/events/query](#/Events/getEventsByQueryPost) and extract `Items[].EventId`.

**Workflow Example**
1. Locate event: [POST /api/v1.0/events/query](#/Events/getEventsByQueryPost) -> extract `Items[].EventId`.
2. Fetch attachments: [GET /api/v1.0/events/{EventId}/attachments](#/Events/getEventAttachments).

**Minimal Required Fields**: EventId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `event_id` | `EventId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `EntityFileDetailListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `EntityFileDetailListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_event_fee_package`

Provenance: Golden OpenAPI contract

Operation ID: `getEventFeePackage`

- Sync: `client.events.get_event_fee_package(event_id=..., timeout=None)`
- Async: `await client.events.get_event_fee_package(event_id=..., timeout=None)`
- Raw payload: `client.events.get_event_fee_package.raw(event_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/events/{EventId}/fee-package`
- Source controller: `IncidentIQ API`

Get event fee package

Retrieves the fee package configuration and totals for a specific event. Use this endpoint to display pricing details, fee rules, or invoice-ready summaries tied to an event.

**Prerequisites**
1. **EventId** - Use [POST /api/v1.0/events/query](#/Events/getEventsByQueryPost) and extract `Items[].EventId`.

**Workflow Example**
1. Locate the event: [POST /api/v1.0/events/query](#/Events/getEventsByQueryPost) -> extract `Items[].EventId`.
2. Fetch fee package: [GET /api/v1.0/events/{EventId}/fee-package](#/Events/getEventFeePackage).
3. Use the returned data to render fee breakdowns or confirm charges.

**Minimal Required Fields**: EventId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `event_id` | `EventId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `FeeSchedulePackageResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `FeeSchedulePackageResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_event_recurrence`

Provenance: Golden OpenAPI contract

Operation ID: `getEventRecurrence`

- Sync: `client.events.get_event_recurrence(body=..., timeout=None)`
- Async: `await client.events.get_event_recurrence(body=..., timeout=None)`
- Raw payload: `client.events.get_event_recurrence.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/events/recurrence`
- Source controller: `IncidentIQ API`

Get active events in series

Returns all active events that belong to a recurring or multi-date series. Use this to display the series instances tied to a parent event or to validate which occurrences are still active.

**Prerequisites**
1. **ParentEventId** - Use [GET /api/v1.0/events/{EventId}](#/Events/getEvent) to confirm the series parent.

**Workflow Example**
1. Get the series parent: [GET /api/v1.0/events/{EventId}](#/Events/getEvent).
2. Submit `UpdateEventRequest` with `ParentEventId` (or series metadata).
3. Review the returned `Items` list to display occurrences.

**Minimal Required Fields**: Provide `ParentEventId` or equivalent series identifiers in the request body.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `UpdateEventRequest` | `UpdateEventRequest` | - |

#### Returns

- Typed call return: `UpdateEventRequestListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UpdateEventRequestListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_event_type`

Provenance: Golden OpenAPI contract

Operation ID: `getEventType`

- Sync: `client.events.get_event_type(event_type_id=..., timeout=None)`
- Async: `await client.events.get_event_type(event_type_id=..., timeout=None)`
- Raw payload: `client.events.get_event_type.raw(event_type_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/events/types/{EventTypeId}`
- Source controller: `IncidentIQ API`

Get event type by ID

Returns a single event type definition by its identifier. Use this when editing event categories or when you need to resolve an event's type metadata in detail.

**Prerequisites**
1. **EventTypeId** - Use [POST /api/v1.0/events/types/query](#/Events/getEventTypesByQueryPost) and extract `Items[].EventTypeId`.

**Workflow Example**
1. List event types: [POST /api/v1.0/events/types/query](#/Events/getEventTypesByQueryPost) -> extract `Items[].EventTypeId`.
2. Get details: [GET /api/v1.0/events/types/{EventTypeId}](#/Events/getEventType).

**Minimal Required Fields**: EventTypeId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `event_type_id` | `EventTypeId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `EventTypeItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `EventTypeItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_event_types_by_ids`

Provenance: Golden OpenAPI contract

Operation ID: `getEventTypesByIds`

- Sync: `client.events.get_event_types_by_ids(body=..., timeout=None)`
- Async: `await client.events.get_event_types_by_ids(body=..., timeout=None)`
- Raw payload: `client.events.get_event_types_by_ids.raw(body=..., timeout=None)`
- HTTP route: `GET /api/v1.0/events/types/ids`
- Source controller: `IncidentIQ API`

Get event types by IDs

Returns event type records for the supplied list of type UUIDs. Use this when you already have identifiers and need to hydrate labels or scope metadata.

**Prerequisites**
1. **EventTypeIds** - Use [POST /api/v1.0/events/types/query](#/Events/getEventTypesByQueryPost) and extract `Items[].EventTypeId`.

**Workflow Example**
1. Query types: [POST /api/v1.0/events/types/query](#/Events/getEventTypesByQueryPost) -> extract `Items[].EventTypeId`.
2. Fetch by IDs: [GET /api/v1.0/events/types/ids](#/Events/getEventTypesByIds) with the ID array.

**Minimal Required Fields**: Array of EventTypeId values in the request body.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | - |

#### Returns

- Typed call return: `EventTypeListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `EventTypeListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_event_types_by_query_get`

Provenance: Golden OpenAPI contract

Operation ID: `getEventTypesByQueryGet`

- Sync: `client.events.get_event_types_by_query_get(top=None, skip=None, timeout=None)`
- Async: `await client.events.get_event_types_by_query_get(top=None, skip=None, timeout=None)`
- Raw payload: `client.events.get_event_types_by_query_get.raw(top=None, skip=None, timeout=None)`
- HTTP route: `GET /api/v1.0/events/types/query`
- Source controller: `IncidentIQ API`

Query event types (GET)

Returns event types using the legacy GET query endpoint with `$top` and `$skip` pagination. This variant is deprecated and intended for simple list retrieval when body-based filters are not required.

**Workflow Example**
1. Request the first page by calling this endpoint with `?$top=50&$skip=0`.
2. Page forward by increasing `$skip`.
3. For advanced filtering, use [POST /api/v1.0/events/types/query](#/Events/getEventTypesByQueryPost).

**Minimal Required Fields**: None. Optional: `$top`, `$skip`.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `top` | `$top` | `query` | `no` | `int` | `-` | - |
| `skip` | `$skip` | `query` | `no` | `int` | `-` | - |

#### Returns

- Typed call return: `EventTypeListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `EventTypeListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_event_types_by_query_post`

Provenance: Golden OpenAPI contract

Operation ID: `getEventTypesByQueryPost`

- Sync: `client.events.get_event_types_by_query_post(body=None, timeout=None)`
- Async: `await client.events.get_event_types_by_query_post(body=None, timeout=None)`
- Raw payload: `client.events.get_event_types_by_query_post.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/events/types/query`
- Source controller: `IncidentIQ API`

Query event types (POST)

Queries event types using request-body filters. Use this to target specific scopes, site-specific types, or naming patterns via the standard filter system.

**Workflow Example**
1. Build `Filters` with desired criteria (scope, name, site).
2. Submit query: [POST /api/v1.0/events/types/query](#/Events/getEventTypesByQueryPost).
3. Use returned `Items[]` to populate type pickers or admin lists.

**Minimal Required Fields**: None. Filters are optional.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `InlineObject` | `InlineObject` | - |

#### Returns

- Typed call return: `EventTypeListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `EventTypeListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_events_by_ids`

Provenance: Golden OpenAPI contract

Operation ID: `getEventsByIds`

- Sync: `client.events.get_events_by_ids(body=..., timeout=None)`
- Async: `await client.events.get_events_by_ids(body=..., timeout=None)`
- Raw payload: `client.events.get_events_by_ids.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/events/ids/get`
- Source controller: `IncidentIQ API`

Get events by IDs

Returns event records for a supplied list of event UUIDs. Use this endpoint when you already have identifiers and want to retrieve a compact set without re-running a full query.

**Prerequisites**
1. **EventIds** - Use [POST /api/v1.0/events/query](#/Events/getEventsByQueryPost) and extract `Items[].EventId`.

**Workflow Example**
1. Query for events: [POST /api/v1.0/events/query](#/Events/getEventsByQueryPost) -> extract `Items[].EventId`.
2. Fetch by IDs: [POST /api/v1.0/events/ids/get](#/Events/getEventsByIds) with the ID array.

**Minimal Required Fields**: Array of EventId values.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | - |

#### Returns

- Typed call return: `EventListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `EventListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_events_by_query_get`

Provenance: Golden OpenAPI contract

Operation ID: `getEventsByQueryGet`

- Sync: `client.events.get_events_by_query_get(top=None, skip=None, timeout=None)`
- Async: `await client.events.get_events_by_query_get(top=None, skip=None, timeout=None)`
- Raw payload: `client.events.get_events_by_query_get.raw(top=None, skip=None, timeout=None)`
- HTTP route: `GET /api/v1.0/events/query`
- Source controller: `IncidentIQ API`

Query events (GET)

Returns events using the legacy GET query endpoint with `$top` and `$skip` paging parameters. This variant is deprecated and best suited for simple list retrieval when no body-based filters are required.

**Workflow Example**
1. Request the first page by calling this endpoint with `?$top=50&$skip=0`.
2. Page forward by incrementing `$skip`.
3. For more advanced filtering, use [POST /api/v1.0/events/query](#/Events/getEventsByQueryPost).

**Minimal Required Fields**: None. Optional: `$top`, `$skip`.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `top` | `$top` | `query` | `no` | `int` | `-` | - |
| `skip` | `$skip` | `query` | `no` | `int` | `-` | - |

#### Returns

- Typed call return: `EventListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `EventListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_events_by_query_post`

Provenance: Golden OpenAPI contract

Operation ID: `getEventsByQueryPost`

- Sync: `client.events.get_events_by_query_post(body=None, timeout=None)`
- Async: `await client.events.get_events_by_query_post(body=None, timeout=None)`
- Raw payload: `client.events.get_events_by_query_post.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/events/query`
- Source controller: `IncidentIQ API`

Query events (POST)

Queries events using structured filters, paging, and sorting. This is the primary endpoint for searching and listing events in the IncidentIQ Events module. It supports advanced filtering by date, location, room, event type, status, organization, and custom fields.

**IMPORTANT: RequestOptions Wrapper**

This endpoint uses the `RequestOptionParameter` pattern — all filters, paging, and sorting MUST be nested inside a `RequestOptions` object in the request body. Placing them at the root level will be silently ignored.

**Filter Facet System**

This endpoint supports event-specific facets via the `RequestOptions.Filters` array. Each filter entry specifies a `Facet` key plus either `Ids` (for UUID-based facets) or `Values` (for expression-based facets):

- **Scheduling**: `EventDate`, `EventDayOfWeek`, `EventTimeOfDay`, `DaysBeforeEvent`, `DaysAfterEvent`, `Upcoming`, `CreatedDate`
- **Classification**: `EventType`, `EventStatus`, `Event`, `EventsInSeries`
- **Location**: `EventLocation`, `EventRoom`, `EventRoomType`
- **People**: `EventOwner`, `EventOrganization`, `EventOrganizationType`, `EventOrganizationStatus`, `ContactEmail`
- **Insurance**: `InsuranceExpired`, `OrgInsuranceExpirationDate`
- **Financial**: `FeeType`, `RateType`, `NumberOfAttendees`
- **Custom Fields**: `EventCustomField` (append subtype: `text`, `number`, `datetime`, `users`, etc.)

See the `EventSearchFilter` schema for the complete `x-facet-definitions` reference documenting all facets with their required fields and value formats.

**Filter Expression Syntax**
- **Date facets** (`EventDate`, `CreatedDate`): Supports relative ranges (`range:year`, `range:today`, `range:tomorrow`) and explicit ranges (`daterange:MM/dd/yyyy-MM/dd/yyyy`). See `EventSearchFilter` for full syntax.
- **Time facets** (`EventTimeOfDay`): Use `timerange:HH:mm-HH:mm` in 24-hour format (e.g., `timerange:06:00-12:00`).
- **Numeric facets** (`NumberOfAttendees`, `DaysBeforeEvent`, `DaysAfterEvent`): Use `numoperator:<operator>:<value>` where operator is `equals`, `lessthan`, `lessthanequal`, `greaterthan`, or `greaterthanequal`.
- **Boolean facets** (`InsuranceExpired`): Use `yes` or `no` as the value.
- **Parameterless facets** (`Upcoming`): Just include the facet with no `Ids` or `Values` — returns future events excluding Canceled/Denied.

**Prerequisites**
- To filter by **EventType**, retrieve type IDs from [POST /api/v1.0/events/types/query](#/Events/getEventTypesByQueryPost) → extract `Items[].EventTypeId`.
- To filter by **EventStatus**, retrieve status IDs from [POST /api/v1.0/events/status-types/query](#/Events/getEventStatusTypesByQueryPost) → extract `Items[].EventStatusTypeId`.
- To filter by **EventLocation**, retrieve location IDs from [GET /api/v2.0/locations/view](#/Locations/getMyLocationsViewV2) → extract `Items[].LocationId`.
- To filter by **EventOwner**, retrieve user IDs from [POST /api/v1.0/users](#/Users/searchUsersByQuery) → extract `Items[].UserId`.

**Pagination and Sorting**

Use `RequestOptions.Paging` to control pagination and sorting:

| Field | Description | Example |
|-------|-------------|---------|
| `PageSize` | Records per page (default 20) | `50` |
| `PageIndex` | Zero-based page index | `0` |
| `SortField` | Field to sort by | `StartDatetime` |
| `SortDirection` | `Ascending` or `Descending` | `Descending` |

The response `Paging` object provides `PageIndex`, `PageSize`, `PageCount`, and `TotalRows` for navigation.

**Available Sort Fields**: `StartDatetime`, `EndDatetime`, `CreatedDate`, `ModifiedDate`, `Title`, `EventTag`

**Workflow Examples**

*Find all approved events this year:*
```json
{
  "RequestOptions": {
    "Paging": { "PageSize": 50 },
    "Filters": [
      { "Facet": "EventDate", "Values": ["range:year"] },
      { "Facet": "EventStatus", "Ids": ["<ApprovedStatusId>"] }
    ]
  }
}
```

*Find upcoming events at a specific location:*
```json
{
  "RequestOptions": {
    "Paging": { "PageSize": 25, "SortField": "StartDatetime", "SortDirection": "Ascending" },
    "Filters": [
      { "Facet": "Upcoming" },
      { "Facet": "EventLocation", "Ids": ["<LocationId>"] }
    ]
  }
}
```

*Find events with 50+ attendees in the next 7 days:*
```json
{
  "RequestOptions": {
    "Filters": [
      { "Facet": "DaysBeforeEvent", "Values": ["numoperator:lessthanequal:7"] },
      { "Facet": "NumberOfAttendees", "Values": ["numoperator:greaterthanequal:50"] }
    ]
  }
}
```

**Performance Considerations**
- Begin with narrow filter combinations (date range + status) to avoid scanning the entire event corpus.
- Cache supporting metadata (event types, status types, locations) rather than issuing lookups per request.
- Use moderate page sizes (25–50) for optimal response times.

**Related endpoints**
- [POST /api/v1.0/events/types/query](#/Events/getEventTypesByQueryPost) — retrieve event type IDs for `EventType` facet.
- [POST /api/v1.0/events/status-types/query](#/Events/getEventStatusTypesByQueryPost) — retrieve status type IDs for `EventStatus` facet.
- [POST /api/v1.0/events/query/withdeleted](#/Events/getEventsByQueryWithDeletedPost) — same query interface including soft-deleted events.
- [POST /api/v1.0/events/for/{UserId}](#/Events/getUserEventsPost) — query events for a specific user.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `GetEventsRequest` | `GetEventsRequest` | - |

#### Returns

- Typed call return: `EventListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `EventListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_events_by_query_with_deleted_get`

Provenance: Golden OpenAPI contract

Operation ID: `getEventsByQueryWithDeletedGet`

- Sync: `client.events.get_events_by_query_with_deleted_get(top=None, skip=None, timeout=None)`
- Async: `await client.events.get_events_by_query_with_deleted_get(top=None, skip=None, timeout=None)`
- Raw payload: `client.events.get_events_by_query_with_deleted_get.raw(top=None, skip=None, timeout=None)`
- HTTP route: `GET /api/v1.0/events/query/withdeleted`
- Source controller: `IncidentIQ API`

Query events including deleted (GET)

Returns events using the legacy GET query endpoint, including soft-deleted records. Use this for audit or recovery workflows when you must see deleted entries.

**Workflow Example**
1. Request the first page by calling this endpoint with `?$top=50&$skip=0`.
2. Page through results as needed.
3. For advanced filtering, use [POST /api/v1.0/events/query/withdeleted](#/Events/getEventsByQueryWithDeletedPost).

**Minimal Required Fields**: None. Optional: `$top`, `$skip`.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `top` | `$top` | `query` | `no` | `int` | `-` | - |
| `skip` | `$skip` | `query` | `no` | `int` | `-` | - |

#### Returns

- Typed call return: `EventListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `EventListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_events_by_query_with_deleted_post`

Provenance: Golden OpenAPI contract

Operation ID: `getEventsByQueryWithDeletedPost`

- Sync: `client.events.get_events_by_query_with_deleted_post(body=None, timeout=None)`
- Async: `await client.events.get_events_by_query_with_deleted_post(body=None, timeout=None)`
- Raw payload: `client.events.get_events_by_query_with_deleted_post.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/events/query/withdeleted`
- Source controller: `IncidentIQ API`

Query events including deleted (POST)

Queries events (including soft-deleted records) using request-body filters. This is the preferred way to audit historical data while still applying the same filter system used for active events.

**Prerequisites**
- If filtering by **EventTypeId**, use [POST /api/v1.0/events/types/query](#/Events/getEventTypesByQueryPost) to retrieve `Items[].EventTypeId`.

**Workflow Example**
1. (Optional) Lookup event types: [POST /api/v1.0/events/types/query](#/Events/getEventTypesByQueryPost) -> extract `Items[].EventTypeId`.
2. Build filters in `GetEventsRequest.Filters`.
3. Submit query: [POST /api/v1.0/events/query/withdeleted](#/Events/getEventsByQueryWithDeletedPost).

**Minimal Required Fields**: None. Filters are optional.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `GetEventsRequest` | `GetEventsRequest` | - |

#### Returns

- Typed call return: `EventListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `EventListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_user_events_get`

Provenance: Golden OpenAPI contract

Operation ID: `getUserEventsGet`

- Sync: `client.events.get_user_events_get(user_id=..., timeout=None)`
- Async: `await client.events.get_user_events_get(user_id=..., timeout=None)`
- Raw payload: `client.events.get_user_events_get.raw(user_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/events/for/{UserId}`
- Source controller: `IncidentIQ API`

Get user events (GET)

Returns events associated with a specific user using the legacy GET variant. This endpoint is deprecated but still useful for simple lookups when you only need the default event list for a user and minimal query parameters.

**Prerequisites**
1. **UserId** - Use [POST /api/v1.0/users](#/Users/searchUsers) and extract `Items[].UserId`.

**Workflow Example**
1. Search for the user: [POST /api/v1.0/users](#/Users/searchUsers) -> extract `Items[].UserId`.
2. Fetch events: [GET /api/v1.0/events/for/{UserId}](#/Events/getUserEventsGet).
3. For full detail on a specific event, call [GET /api/v1.0/events/{EventId}](#/Events/getEvent).

**Minimal Required Fields**: UserId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `EventListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `EventListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_user_events_post`

Provenance: Golden OpenAPI contract

Operation ID: `getUserEventsPost`

- Sync: `client.events.get_user_events_post(user_id=..., body=None, timeout=None)`
- Async: `await client.events.get_user_events_post(user_id=..., body=None, timeout=None)`
- Raw payload: `client.events.get_user_events_post.raw(user_id=..., body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/events/for/{UserId}`
- Source controller: `IncidentIQ API`

Get user events (POST)

Returns events associated with a specific user, with support for request-body filters. Use this POST variant when you need to apply complex filtering beyond the legacy GET query parameters.

**Prerequisites**
1. **UserId** - Use [POST /api/v1.0/users](#/Users/searchUsers) and extract `Items[].UserId`.

**Workflow Example**
1. Search for the user: [POST /api/v1.0/users](#/Users/searchUsers) -> extract `Items[].UserId`.
2. Build a filter body (optional): `GetEventsRequest.Filters`.
3. Fetch events: [POST /api/v1.0/events/for/{UserId}](#/Events/getUserEventsPost).

**Minimal Required Fields**: UserId (path). Filters are optional.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | - |
| `body` | `body` | `body` | `no` | `GetEventsRequest` | `GetEventsRequest` | - |

#### Returns

- Typed call return: `EventListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `EventListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `project_events`

Provenance: Golden OpenAPI contract

Operation ID: `projectEvents`

- Sync: `client.events.project_events(body=..., timeout=None)`
- Async: `await client.events.project_events(body=..., timeout=None)`
- Raw payload: `client.events.project_events.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/events/project-events`
- Source controller: `IncidentIQ API`

Project event occurrences

Projects future occurrences for a recurring or multi-date event based on the supplied schedule information. Use this to preview generated occurrences before committing a series update.

**Prerequisites**
1. **EventId** (if projecting from an existing event) - Use [POST /api/v1.0/events/query](#/Events/getEventsByQueryPost) and extract `Items[].EventId`.

**Workflow Example**
1. Identify the event or series to project.
2. Build an `UpdateEventRequest` with recurrence data and schedule fields.
3. Submit projection: [POST /api/v1.0/events/project-events](#/Events/projectEvents).

**Minimal Required Fields**: Schedule fields in the `UpdateEventRequest` (`StartDateTime`, `EndDateTime`) plus series metadata as needed.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `UpdateEventRequest` | `UpdateEventRequest` | - |

#### Returns

- Typed call return: `UpdateEventRequestListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UpdateEventRequestListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `save_event_attachments`

Provenance: Golden OpenAPI contract

Operation ID: `saveEventAttachments`

- Sync: `client.events.save_event_attachments(event_id=..., body=..., timeout=None)`
- Async: `await client.events.save_event_attachments(event_id=..., body=..., timeout=None)`
- Raw payload: `client.events.save_event_attachments.raw(event_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/events/{EventId}/attachments`
- Source controller: `IncidentIQ API`

Save event attachments

Adds or updates attachment metadata for an event. Use this after uploading files to associate them with the event record and to control visibility or ordering.

**Prerequisites**
1. **EventId** - Use [POST /api/v1.0/events/query](#/Events/getEventsByQueryPost) and extract `Items[].EventId`.

**Workflow Example**
1. Locate event: [POST /api/v1.0/events/query](#/Events/getEventsByQueryPost) -> extract `Items[].EventId`.
2. Prepare `UpdateEventFileDetailsRequest` with file details.
3. Save attachments: [POST /api/v1.0/events/{EventId}/attachments](#/Events/saveEventAttachments).

**Minimal Required Fields**: EventId (path) plus the attachment list in the request body.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `event_id` | `EventId` | `path` | `yes` | `str` | `-` | - |
| `body` | `body` | `body` | `yes` | `UpdateEventFileDetailsRequest` | `UpdateEventFileDetailsRequest` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_event`

Provenance: Golden OpenAPI contract

Operation ID: `updateEvent`

- Sync: `client.events.update_event(event_id=..., body=..., timeout=None)`
- Async: `await client.events.update_event(event_id=..., body=..., timeout=None)`
- Raw payload: `client.events.update_event.raw(event_id=..., body=..., timeout=None)`
- HTTP route: `PUT /api/v1.0/events/{EventId}/update`
- Source controller: `IncidentIQ API`

Update event by ID

Updates a single event by ID, including schedule changes, location updates, and metadata edits. Use the `Instance` field in the request body to control how recurring events are applied.

**Prerequisites**
1. **EventId** - Use [POST /api/v1.0/events/query](#/Events/getEventsByQueryPost) and extract `Items[].EventId`.

**Workflow Example**
1. Load current data: [GET /api/v1.0/events/{EventId}](#/Events/getEvent).
2. Edit fields in `UpdateEventRequest` (for recurring events, set `Instance`).
3. Submit update: [PUT /api/v1.0/events/{EventId}/update](#/Events/updateEvent).

**Minimal Required Fields**: EventId (path) plus at least one field to update in the body.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `event_id` | `EventId` | `path` | `yes` | `str` | `-` | - |
| `body` | `body` | `body` | `yes` | `UpdateEventRequest` | `UpdateEventRequest` | - |

#### Returns

- Typed call return: `EventsUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `EventsUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_event_type`

Provenance: Golden OpenAPI contract

Operation ID: `updateEventType`

- Sync: `client.events.update_event_type(event_type_id=..., body=..., timeout=None)`
- Async: `await client.events.update_event_type(event_type_id=..., body=..., timeout=None)`
- Raw payload: `client.events.update_event_type.raw(event_type_id=..., body=..., timeout=None)`
- HTTP route: `PUT /api/v1.0/events/types/{EventTypeId}/update`
- Source controller: `IncidentIQ API`

Update event type by ID

Updates an existing event type using the supplied ID and payload. Use this to rename categories, adjust scope visibility, or update icon metadata.

**Prerequisites**
1. **EventTypeId** - Use [POST /api/v1.0/events/types/query](#/Events/getEventTypesByQueryPost) and extract `Items[].EventTypeId`.

**Workflow Example**
1. List event types: [POST /api/v1.0/events/types/query](#/Events/getEventTypesByQueryPost) -> extract `Items[].EventTypeId`.
2. Build `UpdateEventTypeRequest` with the fields to change.
3. Update type: [PUT /api/v1.0/events/types/{EventTypeId}/update](#/Events/updateEventType).

**Minimal Required Fields**: EventTypeId (path) plus at least one field to update (commonly `Name` or `Scope`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `event_type_id` | `EventTypeId` | `path` | `yes` | `str` | `-` | - |
| `body` | `body` | `body` | `yes` | `UpdateEventTypeRequest` | `UpdateEventTypeRequest` | - |

#### Returns

- Typed call return: `EventsUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `EventsUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_event_types_by_ids`

Provenance: Golden OpenAPI contract

Operation ID: `updateEventTypesByIds`

- Sync: `client.events.update_event_types_by_ids(body=..., timeout=None)`
- Async: `await client.events.update_event_types_by_ids(body=..., timeout=None)`
- Raw payload: `client.events.update_event_types_by_ids.raw(body=..., timeout=None)`
- HTTP route: `PUT /api/v1.0/events/types/ids/update`
- Source controller: `IncidentIQ API`

Update event types by IDs

Updates multiple event types by explicit ID list. Each item should include the `EventTypeId` and the fields to change, allowing bulk renames or scope adjustments.

**Prerequisites**
1. **EventTypeIds** - Use [POST /api/v1.0/events/types/query](#/Events/getEventTypesByQueryPost) and extract `Items[].EventTypeId`.

**Workflow Example**
1. Query types: [POST /api/v1.0/events/types/query](#/Events/getEventTypesByQueryPost) -> extract `Items[].EventTypeId`.
2. Build `UpdateEventTypeRequest` items with `EventTypeId` and updated fields.
3. Submit update: [PUT /api/v1.0/events/types/ids/update](#/Events/updateEventTypesByIds).

**Minimal Required Fields**: Each item must include `EventTypeId` plus at least one field to update.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | - |

#### Returns

- Typed call return: `EventTypeBatchUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `EventTypeBatchUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_event_types_by_query`

Provenance: Golden OpenAPI contract

Operation ID: `updateEventTypesByQuery`

- Sync: `client.events.update_event_types_by_query(body=..., timeout=None)`
- Async: `await client.events.update_event_types_by_query(body=..., timeout=None)`
- Raw payload: `client.events.update_event_types_by_query.raw(body=..., timeout=None)`
- HTTP route: `PUT /api/v1.0/events/types/query/update`
- Source controller: `IncidentIQ API`

Update event types by query

Applies a batch update to all event types matched by the provided filters. The request includes both the `Filters` list and an `Update` object describing the fields to change.

**Workflow Example**
1. Preview target types: [POST /api/v1.0/events/types/query](#/Events/getEventTypesByQueryPost) with the same filters.
2. Build `UpdateEventTypesRequest` with `Filters` and an `Update` payload.
3. Submit update: [PUT /api/v1.0/events/types/query/update](#/Events/updateEventTypesByQuery).

**Minimal Required Fields**: `Filters` and `Update` in the request body.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `UpdateEventTypesRequest` | `UpdateEventTypesRequest` | - |

#### Returns

- Typed call return: `EventTypeBatchUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `EventTypeBatchUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_events_by_ids`

Provenance: Golden OpenAPI contract

Operation ID: `updateEventsByIds`

- Sync: `client.events.update_events_by_ids(body=..., timeout=None)`
- Async: `await client.events.update_events_by_ids(body=..., timeout=None)`
- Raw payload: `client.events.update_events_by_ids.raw(body=..., timeout=None)`
- HTTP route: `PUT /api/v1.0/events/ids/update`
- Source controller: `IncidentIQ API`

Update events by IDs

Updates multiple events by ID in one request. Each item should include the `EventId` and the fields to change, which allows consistent bulk edits for schedules, titles, or statuses.

**Prerequisites**
1. **EventIds** - Use [POST /api/v1.0/events/query](#/Events/getEventsByQueryPost) and extract `Items[].EventId`.

**Workflow Example**
1. Query events to capture IDs.
2. Build `UpdateEventRequest` items including `EventId` and the fields to update.
3. Submit update: [PUT /api/v1.0/events/ids/update](#/Events/updateEventsByIds).

**Minimal Required Fields**: Each array item must include `EventId` plus at least one field to update.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | - |

#### Returns

- Typed call return: `EventBatchUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `EventBatchUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_events_by_query`

Provenance: Golden OpenAPI contract

Operation ID: `updateEventsByQuery`

- Sync: `client.events.update_events_by_query(body=..., timeout=None)`
- Async: `await client.events.update_events_by_query(body=..., timeout=None)`
- Raw payload: `client.events.update_events_by_query.raw(body=..., timeout=None)`
- HTTP route: `PUT /api/v1.0/events/query/update`
- Source controller: `IncidentIQ API`

Update events by query

Applies a batch update to all events matched by the provided filter set. The request includes both the filter list and a partial `Update` object describing the fields to change.

**Workflow Example**
1. Preview target events: [POST /api/v1.0/events/query](#/Events/getEventsByQueryPost) with the same filters.
2. Build `UpdateEventsRequest` with `Filters` and an `Update` payload.
3. Submit update: [PUT /api/v1.0/events/query/update](#/Events/updateEventsByQuery).

**Minimal Required Fields**: `Filters` and `Update` in the request body.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `UpdateEventsRequest` | `UpdateEventsRequest` | - |

#### Returns

- Typed call return: `EventBatchUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `EventBatchUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `validate_schedule`

Provenance: Golden OpenAPI contract

Operation ID: `validateSchedule`

- Sync: `client.events.validate_schedule(location_room_ids=None, location_ids=None, start_date_time=None, end_date_time=None, setup_minutes=None, breakdown_minutes=None, requested_event_id=None, timeout=None)`
- Async: `await client.events.validate_schedule(location_room_ids=None, location_ids=None, start_date_time=None, end_date_time=None, setup_minutes=None, breakdown_minutes=None, requested_event_id=None, timeout=None)`
- Raw payload: `client.events.validate_schedule.raw(location_room_ids=None, location_ids=None, start_date_time=None, end_date_time=None, setup_minutes=None, breakdown_minutes=None, requested_event_id=None, timeout=None)`
- HTTP route: `GET /api/v1.0/events/validate-schedule`
- Source controller: `IncidentIQ API`

Validate schedule

Validates a proposed schedule against conflicts and availability using query parameters. Use this endpoint to quickly check a single schedule window before creating or updating an event.

**Prerequisites**
- If using **LocationRoomIds** or **LocationIds**, obtain them from your location directory APIs or from existing event data.

**Workflow Example**
1. Gather the target rooms or locations and the proposed start/end times.
2. Call [GET /api/v1.0/events/validate-schedule](#/Events/validateSchedule) with the query parameters.
3. Review the response to confirm availability before saving the event.

**Minimal Required Fields**: `StartDateTime`, `EndDateTime`, and at least one of `LocationRoomIds` or `LocationIds`.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `location_room_ids` | `LocationRoomIds` | `query` | `no` | `Any` | `-` | - |
| `location_ids` | `LocationIds` | `query` | `no` | `Any` | `-` | - |
| `start_date_time` | `StartDateTime` | `query` | `no` | `str` | `-` | - |
| `end_date_time` | `EndDateTime` | `query` | `no` | `str` | `-` | - |
| `setup_minutes` | `SetupMinutes` | `query` | `no` | `int` | `-` | - |
| `breakdown_minutes` | `BreakdownMinutes` | `query` | `no` | `int` | `-` | - |
| `requested_event_id` | `RequestedEventId` | `query` | `no` | `str` | `-` | - |

#### Returns

- Typed call return: `ScheduleValidationListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ScheduleValidationListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `validate_schedules_all`

Provenance: Golden OpenAPI contract

Operation ID: `validateSchedulesAll`

- Sync: `client.events.validate_schedules_all(body=..., timeout=None)`
- Async: `await client.events.validate_schedules_all(body=..., timeout=None)`
- Raw payload: `client.events.validate_schedules_all.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/events/validate-schedules-all`
- Source controller: `IncidentIQ API`

Validate all schedules

Validates multiple schedules against all conflict types in one request. Use this when validating a batch of candidate schedules, such as a series of recurring dates or multiple rooms.

**Prerequisites**
- If using **LocationRoomIds** or **LocationIds**, obtain them from your location directory APIs or from existing event data.

**Workflow Example**
1. Build an array of `ScheduleValidationRequest` items with times and locations.
2. Submit the batch: [POST /api/v1.0/events/validate-schedules-all](#/Events/validateSchedulesAll).
3. Review `ValidationMessages` and `ConflictingEvents` for each item.

**Minimal Required Fields**: Each request item should include `StartDateTime`, `EndDateTime`, and at least one of `LocationRoomIds` or `LocationIds`.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | - |

#### Returns

- Typed call return: `ScheduleValidationListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ScheduleValidationListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `validate_schedules_calendar_conflicts`

Provenance: Golden OpenAPI contract

Operation ID: `validateSchedulesCalendarConflicts`

- Sync: `client.events.validate_schedules_calendar_conflicts(body=..., timeout=None)`
- Async: `await client.events.validate_schedules_calendar_conflicts(body=..., timeout=None)`
- Raw payload: `client.events.validate_schedules_calendar_conflicts.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/events/validate-schedules-calendar-conflicts`
- Source controller: `IncidentIQ API`

Validate calendar conflicts

Validates schedules against calendar conflicts only. This is useful when you want to check overlap with other events without enforcing room or location availability.

**Prerequisites**
- If using **LocationRoomIds** or **LocationIds**, obtain them from your location directory APIs or from existing event data.

**Workflow Example**
1. Build an array of `ScheduleValidationRequest` items.
2. Submit the batch: [POST /api/v1.0/events/validate-schedules-calendar-conflicts](#/Events/validateSchedulesCalendarConflicts).
3. Review the conflict messages and the `ConflictingEvents` list.

**Minimal Required Fields**: Each request item should include `StartDateTime`, `EndDateTime`, and at least one of `LocationRoomIds` or `LocationIds`.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | - |

#### Returns

- Typed call return: `ScheduleValidationListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ScheduleValidationListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `validate_schedules_conflicting_events`

Provenance: Golden OpenAPI contract

Operation ID: `validateSchedulesConflictingEvents`

- Sync: `client.events.validate_schedules_conflicting_events(body=..., timeout=None)`
- Async: `await client.events.validate_schedules_conflicting_events(body=..., timeout=None)`
- Raw payload: `client.events.validate_schedules_conflicting_events.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/events/validate-schedules-conflicting-events`
- Source controller: `IncidentIQ API`

Validate conflicting events

Validates proposed schedules against existing events to detect conflicts. This variant focuses exclusively on event-to-event collisions, excluding other availability checks.

**Prerequisites**
- If using **LocationRoomIds** or **LocationIds**, obtain them from your location directory APIs.

**Workflow Example**
1. Collect the room/location IDs and proposed start/end times.
2. Build an array of `ScheduleValidationRequest` items.
3. Submit validation: [POST /api/v1.0/events/validate-schedules-conflicting-events](#/Events/validateSchedulesConflictingEvents) and review `ValidationMessages` and `ConflictingEvents`.

**Minimal Required Fields**: For each request item, include `StartDateTime`, `EndDateTime`, and at least one of `LocationRoomIds` or `LocationIds`.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | - |

#### Returns

- Typed call return: `ScheduleValidationListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ScheduleValidationListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `validate_schedules_place_reservations`

Provenance: Golden OpenAPI contract

Operation ID: `validateSchedulesPlaceReservations`

- Sync: `client.events.validate_schedules_place_reservations(body=..., timeout=None)`
- Async: `await client.events.validate_schedules_place_reservations(body=..., timeout=None)`
- Raw payload: `client.events.validate_schedules_place_reservations.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/events/validate-schedules-place-reservations`
- Source controller: `IncidentIQ API`

Validate place reservations

Validates schedules against location and room availability only. Use this when you need to check room conflicts without considering other event overlaps.

**Prerequisites**
- If using **LocationRoomIds** or **LocationIds**, obtain them from your location directory APIs or from existing event data.

**Workflow Example**
1. Build an array of `ScheduleValidationRequest` items with rooms/locations and times.
2. Submit the batch: [POST /api/v1.0/events/validate-schedules-place-reservations](#/Events/validateSchedulesPlaceReservations).
3. Review the response to confirm room availability.

**Minimal Required Fields**: Each request item should include `StartDateTime`, `EndDateTime`, and at least one of `LocationRoomIds` or `LocationIds`.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | - |

#### Returns

- Typed call return: `ScheduleValidationListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ScheduleValidationListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
