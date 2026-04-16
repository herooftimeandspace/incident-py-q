# `tickets` Golden Namespace

Sync client access: `client.tickets`

Async client access: `client.tickets` with `await` on method calls.

These methods are Golden because they come from bundled Stoplight controller contracts.

## Aliases

| Alias | Canonical Method | Route |
| --- | --- | --- |
| `create` | `create_ticket` | `POST /tickets/new` |
| `delete` | `delete_ticket` | `DELETE /tickets/{TicketId}` |
| `get` | `get_ticket` | `GET /tickets/{TicketId}` |
| `update` | `update_ticket` | `POST /tickets/{TicketId}` |

## Methods

### `assign_ticket`

Provenance: Golden Stoplight contract

Operation ID: `Ticket_AssignTicket`

- Sync: `client.tickets.assign_ticket(ticket_id=..., sla=..., timeout=None)`
- Async: `await client.tickets.assign_ticket(ticket_id=..., sla=..., timeout=None)`
- Raw payload: `client.tickets.assign_ticket.raw(ticket_id=..., sla=..., timeout=None)`
- HTTP route: `POST /tickets/{TicketId}/sla`
- Source controller: `Tickets`

No contract summary provided.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `TicketId` | `path` | `yes` | `str` | `-` | - |
| `sla` | `Sla` | `body` | `yes` | `Sla` | `Sla` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `cancel_ticket`

Provenance: Golden Stoplight contract

Operation ID: `Ticket_CancelTicket`

- Sync: `client.tickets.cancel_ticket(ticket_id=..., cancel_options=..., timeout=None)`
- Async: `await client.tickets.cancel_ticket(ticket_id=..., cancel_options=..., timeout=None)`
- Raw payload: `client.tickets.cancel_ticket.raw(ticket_id=..., cancel_options=..., timeout=None)`
- HTTP route: `POST /tickets/{TicketId}/cancel`
- Source controller: `Tickets`

Cancel a ticket

#### Takes a CloseReasonTypeId from:

| CloseReasonTypeId  | Name			|
| :------------- | ----------:	|
| C98AE44E-ADA0-4AE7-AE30-817785C00001		| Canceled   |
| C98AE44E-ADA0-4AE7-AE30-817785C00002		| Resolved |
| C98AE44E-ADA0-4AE7-AE30-817785C00003		| Canceled - No Longer Occurring |
| C98AE44E-ADA0-4AE7-AE30-817785C00004		| Canceled - Duplicate Ticket |
| C98AE44E-ADA0-4AE7-AE30-817785C00005		| Resolved - No Issue Found |
| C98AE44E-ADA0-4AE7-AE30-817785C00006		| Resolved - No Response From Requestor |

#### Sample request:
```
POST /api/v1.0/tickets/c8aef633-a009-48b1-9187-15621defbba8/cancel
{
"CloseReasonTypeId":"C98AE44E-ADA0-4AE7-AE30-817785C00001",
}
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `TicketId` | `path` | `yes` | `str` | `-` | Ticket ID that we will be canceling |
| `cancel_options` | `CancelOptions` | `body` | `yes` | `TicketCancelOptions` | `TicketCancelOptions` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `change_ticket_issue`

Provenance: Golden Stoplight contract

Operation ID: `Ticket_ChangeTicketIssue`

- Sync: `client.tickets.change_ticket_issue(ticket_id=..., request=..., timeout=None)`
- Async: `await client.tickets.change_ticket_issue(ticket_id=..., request=..., timeout=None)`
- Raw payload: `client.tickets.change_ticket_issue.raw(ticket_id=..., request=..., timeout=None)`
- HTTP route: `POST /tickets/{TicketId}/issue`
- Source controller: `Tickets`

Change Issue

#### Specify a new Issue for an existing ticket   
#### Sample request:
```
POST /api/v1.0/tickets/EDE88D85-D6E4-E711-80C3-0003FF685BE7/issue
{
"TicketId":"EDE88D85-D6E4-E711-80C3-0003FF685BE7",
"IssueId":"DD66756C-6DA8-E711-80C2-0003FF001002"
}
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `TicketId` | `path` | `yes` | `str` | `-` | Ticket ID that will have the team assigned to it removed |
| `request` | `Request` | `body` | `yes` | `SetTicketIssueRequest` | `SetTicketIssueRequest` | Ticket Issue Request Object |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `change_ticket_to_requestor_responded`

Provenance: Golden Stoplight contract

Operation ID: `Ticket_ChangeTicketToRequestorResponded`

- Sync: `client.tickets.change_ticket_to_requestor_responded(ticket_id=..., timeout=None)`
- Async: `await client.tickets.change_ticket_to_requestor_responded(ticket_id=..., timeout=None)`
- Raw payload: `client.tickets.change_ticket_to_requestor_responded.raw(ticket_id=..., timeout=None)`
- HTTP route: `POST /tickets/{TicketId}/status/requestor-responded`
- Source controller: `Tickets`

Mark as 'requestor responded'

#### Change ticket status to 'requestor responded' and apply any applicable rules.
#### Sample request:
```
POST /api/v1.0/tickets/c8aef633-a009-48b1-9187-15621defbba8/status/requestor-responded
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `TicketId` | `path` | `yes` | `str` | `-` | Ticket ID that we will be changing status of |

#### Returns

- Typed call return: `ItemGetResponseOfTicket`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemGetResponseOfTicket`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `change_ticket_to_waiting_on_requestor`

Provenance: Golden Stoplight contract

Operation ID: `Ticket_ChangeTicketToWaitingOnRequestor`

- Sync: `client.tickets.change_ticket_to_waiting_on_requestor(ticket_id=..., timeout=None)`
- Async: `await client.tickets.change_ticket_to_waiting_on_requestor(ticket_id=..., timeout=None)`
- Raw payload: `client.tickets.change_ticket_to_waiting_on_requestor.raw(ticket_id=..., timeout=None)`
- HTTP route: `POST /tickets/{TicketId}/status/waiting-on-requestor`
- Source controller: `Tickets`

Mark as 'waiting on requestor'

#### Change ticket status to 'waiting on requestor' and apply any applicable rules.
#### Sample request:
```
POST /api/v1.0/tickets/c8aef633-a009-48b1-9187-15621defbba8/status/waiting-on-requestor
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `TicketId` | `path` | `yes` | `str` | `-` | Ticket ID that we will be changing status of |

#### Returns

- Typed call return: `ItemGetResponseOfTicket`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemGetResponseOfTicket`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `close_ticket`

Provenance: Golden Stoplight contract

Operation ID: `Ticket_CloseTicket`

- Sync: `client.tickets.close_ticket(ticket_id=..., close_options=..., timeout=None)`
- Async: `await client.tickets.close_ticket(ticket_id=..., close_options=..., timeout=None)`
- Raw payload: `client.tickets.close_ticket.raw(ticket_id=..., close_options=..., timeout=None)`
- HTTP route: `POST /tickets/{TicketId}/close`
- Source controller: `Tickets`

Close a ticket

#### Takes a CloseReasonTypeId from:

| CloseReasonTypeId  | Name			|
| :------------- | ----------:	|
| C98AE44E-ADA0-4AE7-AE30-817785C00001		| Canceled   |
| C98AE44E-ADA0-4AE7-AE30-817785C00002		| Resolved |
| C98AE44E-ADA0-4AE7-AE30-817785C00003		| Canceled - No Longer Occurring |
| C98AE44E-ADA0-4AE7-AE30-817785C00004		| Canceled - Duplicate Ticket |
| C98AE44E-ADA0-4AE7-AE30-817785C00005		| Resolved - No Issue Found |
| C98AE44E-ADA0-4AE7-AE30-817785C00006		| Resolved - No Response From Requestor |

#### Sample request:
```
POST /api/v1.0/tickets/c8aef633-a009-48b1-9187-15621defbba8/close
{
"CloseReasonTypeId":"C98AE44E-ADA0-4AE7-AE30-817785C00001",
}
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `TicketId` | `path` | `yes` | `str` | `-` | Ticket ID that we will be closing |
| `close_options` | `CloseOptions` | `body` | `yes` | `TicketCloseOptions` | `TicketCloseOptions` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `confirm_ticket_issue`

Provenance: Golden Stoplight contract

Operation ID: `Ticket_ConfirmTicketIssue`

- Sync: `client.tickets.confirm_ticket_issue(ticket_id=..., timeout=None)`
- Async: `await client.tickets.confirm_ticket_issue(ticket_id=..., timeout=None)`
- Raw payload: `client.tickets.confirm_ticket_issue.raw(ticket_id=..., timeout=None)`
- HTTP route: `POST /tickets/{TicketId}/confirm-issue`
- Source controller: `Tickets`

Confirm a tickets issue

#### Sample request:
```
POST /api/v1.0/tickets/c8aef633-a009-48b1-9187-15621defbba8/confirm-issue
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `TicketId` | `path` | `yes` | `str` | `-` | Ticket ID that we will be confirming issue of |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `copy_ticket`

Provenance: Golden Stoplight contract

Operation ID: `Ticket_CopyTicket`

- Sync: `client.tickets.copy_ticket(ticket_id=..., copy_options=..., timeout=None)`
- Async: `await client.tickets.copy_ticket(ticket_id=..., copy_options=..., timeout=None)`
- Raw payload: `client.tickets.copy_ticket.raw(ticket_id=..., copy_options=..., timeout=None)`
- HTTP route: `POST /tickets/{TicketId}/copy`
- Source controller: `Tickets`

Copy Ticket

#### Create a copy of a given ticket.    
#### Sample request:
```
POST /api/v1.0/tickets/c8aef633-a009-48b1-9187-15621defbba8/copy
{
"CopyRequestor":true,
"CopyPriority":true,
"CopyAssignedTo":true,
"CopyCustomFieldValues":true,
"RunRules":false,
"SendEmails":false,
"CreateWorkpackage":false,
"WorkpackageName":"New Name",
"Quantity":1
}
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `TicketId` | `path` | `yes` | `str` | `-` | - |
| `copy_options` | `CopyOptions` | `body` | `yes` | `CopyTicketOptions` | `CopyTicketOptions` | - |

#### Returns

- Typed call return: `ListGetResponseOfTicket`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfTicket`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_ticket`

Provenance: Golden Stoplight contract

Operation ID: `Ticket_CreateTicket`

- Sync: `client.tickets.create_ticket(ticket=..., timeout=None)`
- Async: `await client.tickets.create_ticket(ticket=..., timeout=None)`
- Raw payload: `client.tickets.create_ticket.raw(ticket=..., timeout=None)`
- HTTP route: `POST /tickets/new`
- Source controller: `Tickets`
- Aliases: `create`

Submit a new ticket

#### Creates a newly submitted ticket to the Incident IQ platform.  Based on inputs the new ticket may have additional rules fire which may subsequently update the new ticket.  A ticket ID, as well a complete record of the ticket, is returned for every successful new ticket call made to the API.  Please note that rules fire asynchronously after ticket submission so ticket data initially returned may subquently be updated.  To obtain the latest data using the provided ticket ID, call GET `/api/v1.0/tickets/{TicketId}`. For more flexible searching of tickets in general call POST `/api/v1.0/tickets` and provide filters for your search criteria.
#### Sample request:
```
POST /api/v1.0/tickets/new
{
   "Assets":[
      {
         "AssetId":"c8aef633-a009-48b1-9187-15621defbba8"
      }
   ],
   "IsUrgent":false,
   "TicketFollowers":null,
   "Locations":null,
   "Users":null,
   "Teams":null,
   "Roles":null,
   "AssetGroups":null,
   "IssueDescription":"Issue description",
   "CustomFieldValues":[
      {
         "SiteId":"bb6cece8-e4f4-e511-a789-005056bb000e",
         "CustomFieldId":"4112aa9a-db65-4e49-ad67-a5423010b344",
         "Scope":"Site",
         "CustomFieldTypeId":"e7c8b30d-d899-4193-a70b-21994d2a8089",
         "EntityTypeId":"888891ac-91aa-e711-80c2-100dffa00001",
         "IsRequired":false,
         "IsReadOnly":false,
         "IsHidden":false,
         "Filters":[
            {
               "FilterId":"888861e5-34ff-4fcf-87de-100d6f0e0043",
               "Exclude":false,
               "Value":"d5d91f20-2269-e611-80f1-000c29ab80b0"
            }
         ],
         "DisplayOrder":39,
         "EditorTypeId":12,
         "Value":"",
         "IsValid":true
      }
   ],
   "LocationId":"1fd1574a-2243-e611-a93b-a45e60e682da",
   "Attachments":[
            
   ],
   "LocationDetails":"Room details",
   "HasSensitiveInformation":false,
   "Subject":"Acer R13 CB5-312T - Application / Operating System &gt; Can\\'t access website",
   "TicketWizardCategoryId":"d5d91f20-2269-e611-80f1-000c29ab80b0",
   "ForId":"4dd6574a-2243-e611-a93b-a45e60e682da",
   "LocationRoomId":"d1186c41-7e78-e611-80f1-000c29ab80b0",
   "IssueCategoryId":"3cf36201-f97d-40e0-a713-c6cfac2c0b6e",
   "IssueId":"927f2fbb-4db7-e611-80ff-000c29ab80b0",
   "IssueTypeId":"c8add287-0ca2-4fcc-b027-8d0980a84519",
   "IsTraining":false,
   "ProductId":"88df910c-91aa-e711-80c2-0004ffa00010"
}
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket` | `Ticket` | `body` | `yes` | `UpdateTicketRequest` | `UpdateTicketRequest` | Ticket detail parameters including optional associated entities such as assets or attachments |

#### Returns

- Typed call return: `ItemCreateResponseOfTicket`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemCreateResponseOfTicket`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_ticket`

Provenance: Golden Stoplight contract

Operation ID: `Ticket_DeleteTicket`

- Sync: `client.tickets.delete_ticket(ticket_id=..., timeout=None)`
- Async: `await client.tickets.delete_ticket(ticket_id=..., timeout=None)`
- Raw payload: `client.tickets.delete_ticket.raw(ticket_id=..., timeout=None)`
- HTTP route: `DELETE /tickets/{TicketId}`
- Source controller: `Tickets`
- Aliases: `delete`

Delete a ticket

#### Deletes an existing ticket
#### Sample request:
```
DELETE /api/v1.0/tickets/9F326CEF-8390-4707-BA2F-EBD7A397AD65
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `TicketId` | `path` | `yes` | `str` | `-` | Ticket ID that we will be changing status of |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_ticket`

Provenance: Golden Stoplight contract

Operation ID: `Ticket_GetTicket`

- Sync: `client.tickets.get_ticket(ticket_id=..., timeout=None)`
- Async: `await client.tickets.get_ticket(ticket_id=..., timeout=None)`
- Raw payload: `client.tickets.get_ticket.raw(ticket_id=..., timeout=None)`
- HTTP route: `GET /tickets/{TicketId}`
- Source controller: `Tickets`
- Aliases: `get`

No contract summary provided.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `TicketId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ItemGetResponseOfTicket`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemGetResponseOfTicket`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_ticket_assets`

Provenance: Golden Stoplight contract

Operation ID: `Ticket_GetTicketAssets`

- Sync: `client.tickets.get_ticket_assets(ticket_id=..., timeout=None)`
- Async: `await client.tickets.get_ticket_assets(ticket_id=..., timeout=None)`
- Raw payload: `client.tickets.get_ticket_assets.raw(ticket_id=..., timeout=None)`
- HTTP route: `GET /tickets/{TicketId}/assets`
- Source controller: `Tickets`

Get assets for ticket

#### Get all assets currently linked to a given ticket.  Properties and meta information for each asset is returned.  To obtain the latest high-level ticket data provided a valid ticket ID, call GET `/api/v1.0/tickets/{TicketId}`.
#### Sample request:
```
GET /api/v1.0/tickets/ac6cece8-e4f4-e511-a789-005056bb000e/assets
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `TicketId` | `path` | `yes` | `str` | `-` | Ticket ID of the ticket to update |

#### Returns

- Typed call return: `ListGetResponseOfTicketAsset`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfTicketAsset`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_ticket_sla`

Provenance: Golden Stoplight contract

Operation ID: `Ticket_GetTicketSla`

- Sync: `client.tickets.get_ticket_sla(ticket_id=..., timeout=None)`
- Async: `await client.tickets.get_ticket_sla(ticket_id=..., timeout=None)`
- Raw payload: `client.tickets.get_ticket_sla.raw(ticket_id=..., timeout=None)`
- HTTP route: `GET /tickets/{TicketId}/sla`
- Source controller: `Tickets`

Get SLA for ticket

#### Get the current service level agreement ( SLA ) linked to a given ticket.  Properties and meta information for the SLA is returned.  To obtain the latest high-level ticket data provided a valid ticket ID, call GET `/api/v1.0/tickets/{TicketId}`.
#### Sample request:
```
GET /api/v1.0/tickets/ac6cece8-e4f4-e511-a789-005056bb000e/sla
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `TicketId` | `path` | `yes` | `str` | `-` | Ticket ID of the ticket to update |

#### Returns

- Typed call return: `ItemGetResponseOfTicketSla`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemGetResponseOfTicketSla`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_ticket_statuses`

Provenance: Golden Stoplight contract

Operation ID: `Ticket_GetTicketStatuses`

- Sync: `client.tickets.get_ticket_statuses(timeout=None)`
- Async: `await client.tickets.get_ticket_statuses(timeout=None)`
- Raw payload: `client.tickets.get_ticket_statuses.raw(timeout=None)`
- HTTP route: `GET /tickets/statuses`
- Source controller: `Tickets`

Retrieve list of ticket status

#### Returns a list of all ticket statuses available 
#### Sample request:
```
PUT /api/v1.0/tickets/statuses
```

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `ListGetResponseOfTicketStatus`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfTicketStatus`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `mark_ticket_as_duplicate`

Provenance: Golden Stoplight contract

Operation ID: `Ticket_MarkTicketAsDuplicate`

- Sync: `client.tickets.mark_ticket_as_duplicate(ticket_id=..., original_ticket_id=..., timeout=None)`
- Async: `await client.tickets.mark_ticket_as_duplicate(ticket_id=..., original_ticket_id=..., timeout=None)`
- Raw payload: `client.tickets.mark_ticket_as_duplicate.raw(ticket_id=..., original_ticket_id=..., timeout=None)`
- HTTP route: `POST /tickets/{TicketId}/mark-as-duplicate/{OriginalTicketId}`
- Source controller: `Tickets`

No contract summary provided.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `TicketId` | `path` | `yes` | `str` | `-` | - |
| `original_ticket_id` | `OriginalTicketId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `mark_ticket_not_sensitive`

Provenance: Golden Stoplight contract

Operation ID: `Ticket_MarkTicketNotSensitive`

- Sync: `client.tickets.mark_ticket_not_sensitive(ticket_id=..., timeout=None)`
- Async: `await client.tickets.mark_ticket_not_sensitive(ticket_id=..., timeout=None)`
- Raw payload: `client.tickets.mark_ticket_not_sensitive.raw(ticket_id=..., timeout=None)`
- HTTP route: `POST /tickets/{TicketId}/mark-not-sensitive`
- Source controller: `Tickets`

No contract summary provided.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `TicketId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `mark_ticket_not_urgent`

Provenance: Golden Stoplight contract

Operation ID: `Ticket_MarkTicketNotUrgent`

- Sync: `client.tickets.mark_ticket_not_urgent(ticket_id=..., timeout=None)`
- Async: `await client.tickets.mark_ticket_not_urgent(ticket_id=..., timeout=None)`
- Raw payload: `client.tickets.mark_ticket_not_urgent.raw(ticket_id=..., timeout=None)`
- HTTP route: `POST /tickets/{TicketId}/mark-not-urgent`
- Source controller: `Tickets`

No contract summary provided.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `TicketId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `mark_ticket_sensitive`

Provenance: Golden Stoplight contract

Operation ID: `Ticket_MarkTicketSensitive`

- Sync: `client.tickets.mark_ticket_sensitive(ticket_id=..., timeout=None)`
- Async: `await client.tickets.mark_ticket_sensitive(ticket_id=..., timeout=None)`
- Raw payload: `client.tickets.mark_ticket_sensitive.raw(ticket_id=..., timeout=None)`
- HTTP route: `POST /tickets/{TicketId}/mark-sensitive`
- Source controller: `Tickets`

No contract summary provided.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `TicketId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `mark_ticket_urgent`

Provenance: Golden Stoplight contract

Operation ID: `Ticket_MarkTicketUrgent`

- Sync: `client.tickets.mark_ticket_urgent(ticket_id=..., timeout=None)`
- Async: `await client.tickets.mark_ticket_urgent(ticket_id=..., timeout=None)`
- Raw payload: `client.tickets.mark_ticket_urgent.raw(ticket_id=..., timeout=None)`
- HTTP route: `POST /tickets/{TicketId}/mark-urgent`
- Source controller: `Tickets`

No contract summary provided.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `TicketId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `un_assign_ticket_from_team`

Provenance: Golden Stoplight contract

Operation ID: `Ticket_UnAssignTicketFromTeam`

- Sync: `client.tickets.un_assign_ticket_from_team(ticket_id=..., timeout=None)`
- Async: `await client.tickets.un_assign_ticket_from_team(ticket_id=..., timeout=None)`
- Raw payload: `client.tickets.un_assign_ticket_from_team.raw(ticket_id=..., timeout=None)`
- HTTP route: `POST /tickets/{TicketId}/unassign/team`
- Source controller: `Tickets`

No contract summary provided.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `TicketId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `un_assign_ticket_from_user`

Provenance: Golden Stoplight contract

Operation ID: `Ticket_UnAssignTicketFromUser`

- Sync: `client.tickets.un_assign_ticket_from_user(ticket_id=..., timeout=None)`
- Async: `await client.tickets.un_assign_ticket_from_user(ticket_id=..., timeout=None)`
- Raw payload: `client.tickets.un_assign_ticket_from_user.raw(ticket_id=..., timeout=None)`
- HTTP route: `POST /tickets/{TicketId}/unassign/user`
- Source controller: `Tickets`

No contract summary provided.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `TicketId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `un_assign_ticket_sla`

Provenance: Golden Stoplight contract

Operation ID: `Ticket_UnAssignTicketSla`

- Sync: `client.tickets.un_assign_ticket_sla(ticket_id=..., timeout=None)`
- Async: `await client.tickets.un_assign_ticket_sla(ticket_id=..., timeout=None)`
- Raw payload: `client.tickets.un_assign_ticket_sla.raw(ticket_id=..., timeout=None)`
- HTTP route: `POST /tickets/{TicketId}/unassign-sla`
- Source controller: `Tickets`

Remove SLA

#### Removes the currently assigned SLA from a ticket
#### Sample request:
```
POST /api/v1.0/tickets/c8aef633-a009-48b1-9187-15621defbba8/unassign-sla
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `TicketId` | `path` | `yes` | `str` | `-` | Ticket IDof the ticket that will have the SLA removed |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `un_confirm_ticket_issue`

Provenance: Golden Stoplight contract

Operation ID: `Ticket_UnConfirmTicketIssue`

- Sync: `client.tickets.un_confirm_ticket_issue(ticket_id=..., timeout=None)`
- Async: `await client.tickets.un_confirm_ticket_issue(ticket_id=..., timeout=None)`
- Raw payload: `client.tickets.un_confirm_ticket_issue.raw(ticket_id=..., timeout=None)`
- HTTP route: `POST /tickets/{TicketId}/unconfirm-issue`
- Source controller: `Tickets`

Reverse ticket issue confirmation

#### Will reverse an already confirmed issue on a ticket
#### Sample request:
```
POST /api/v1.0/tickets/c8aef633-a009-48b1-9187-15621defbba8/unconfirm-issue
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `TicketId` | `path` | `yes` | `str` | `-` | Ticket ID that we will be reversing the confirm of |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `undelete_ticket`

Provenance: Golden Stoplight contract

Operation ID: `Ticket_UndeleteTicket`

- Sync: `client.tickets.undelete_ticket(ticket_id=..., timeout=None)`
- Async: `await client.tickets.undelete_ticket(ticket_id=..., timeout=None)`
- Raw payload: `client.tickets.undelete_ticket.raw(ticket_id=..., timeout=None)`
- HTTP route: `PUT /tickets/{TicketId}/undelete`
- Source controller: `Tickets`

Undelete a ticket

#### Undeletes an existing deleted ticket
#### Sample request:
```
PUT /api/v1.0/tickets/c8aef633-a009-48b1-9187-15621defbba8/undelete
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `TicketId` | `path` | `yes` | `str` | `-` | Ticket ID that we will be changing status of |

#### Returns

- Typed call return: `ItemGetResponseOfTicket`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemGetResponseOfTicket`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_ticket`

Provenance: Golden Stoplight contract

Operation ID: `Ticket_UpdateTicket`

- Sync: `client.tickets.update_ticket(ticket_id=..., ticket=..., timeout=None)`
- Async: `await client.tickets.update_ticket(ticket_id=..., ticket=..., timeout=None)`
- Raw payload: `client.tickets.update_ticket.raw(ticket_id=..., ticket=..., timeout=None)`
- HTTP route: `POST /tickets/{TicketId}`
- Source controller: `Tickets`
- Aliases: `update`

Update an existing ticket

#### Updates a previously submitted ticket with provided changes.  Please note that based on inputs the updated ticket may have additional update rules fire which may affect final values.  A ticket ID, as well a complete record of the ticket, is returned for every successful update ticket call made to the API.  Please note that rules fire asynchronously so ticket data initially returned may subquently be updated.  To obtain the latest data using the provided ticket ID, call GET `/api/v1.0/tickets/{TicketId}`. For more flexible searching of tickets in general call POST `/api/v1.0/tickets` and provide filters for your search criteria.
#### Sample request:
```
POST /api/v1.0/tickets/ac6cece8-e4f4-e511-a789-005056bb000e
{
   "Assets":[
      {
         "AssetId":"c8aef633-a009-48b1-9187-15621defbba8"
      }
   ],
   "IsUrgent":false,
   "TicketFollowers":null,
   "Locations":null,
   "Users":null,
   "Teams":null,
   "Roles":null,
   "AssetGroups":null,
   "IssueDescription":"Issue description",
   "CustomFieldValues":[
      {
         "SiteId":"bb6cece8-e4f4-e511-a789-005056bb000e",
         "CustomFieldId":"4112aa9a-db65-4e49-ad67-a5423010b344",
         "Scope":"Site",
         "CustomFieldTypeId":"e7c8b30d-d899-4193-a70b-21994d2a8089",
         "EntityTypeId":"888891ac-91aa-e711-80c2-100dffa00001",
         "IsRequired":false,
         "IsReadOnly":false,
         "IsHidden":false,
         "Filters":[
            {
               "FilterId":"888861e5-34ff-4fcf-87de-100d6f0e0043",
               "Exclude":false,
               "Value":"d5d91f20-2269-e611-80f1-000c29ab80b0"
            }
         ],
         "DisplayOrder":39,
         "EditorTypeId":12,
         "Value":"",
         "IsValid":true
      }
   ],
   "LocationId":"1fd1574a-2243-e611-a93b-a45e60e682da",
   "Attachments":[
            
   ],
   "LocationDetails":"Room details",
   "HasSensitiveInformation":false,
   "Subject":"Acer R13 CB5-312T - Application / Operating System &gt; Can\\'t access website",
   "TicketWizardCategoryId":"d5d91f20-2269-e611-80f1-000c29ab80b0",
   "ForId":"4dd6574a-2243-e611-a93b-a45e60e682da",
   "LocationRoomId":"d1186c41-7e78-e611-80f1-000c29ab80b0",
   "IssueCategoryId":"3cf36201-f97d-40e0-a713-c6cfac2c0b6e",
   "IssueId":"927f2fbb-4db7-e611-80ff-000c29ab80b0",
   "IssueTypeId":"c8add287-0ca2-4fcc-b027-8d0980a84519",
   "IsTraining":false,
   "ProductId":"88df910c-91aa-e711-80c2-0004ffa00010"
}
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `TicketId` | `path` | `yes` | `str` | `-` | Ticket ID of the ticket to update |
| `ticket` | `Ticket` | `body` | `yes` | `UpdateTicketRequest` | `UpdateTicketRequest` | Ticket detail parameters including optional associated entities such as assets or attachments |

#### Returns

- Typed call return: `ItemUpdateResponseOfTicket`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemUpdateResponseOfTicket`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_ticket_assets`

Provenance: Golden Stoplight contract

Operation ID: `Ticket_UpdateTicketAssets`

- Sync: `client.tickets.update_ticket_assets(ticket_id=..., assets=..., timeout=None)`
- Async: `await client.tickets.update_ticket_assets(ticket_id=..., assets=..., timeout=None)`
- Raw payload: `client.tickets.update_ticket_assets.raw(ticket_id=..., assets=..., timeout=None)`
- HTTP route: `POST /tickets/{TicketId}/assets`
- Source controller: `Tickets`

Update assets

#### Updates a previously submitted ticket's assets with provided values.  Please note that based on inputs the updated ticket may have additional update rules fire which may affect final values.  Please note that rules fire asynchronously so ticket data initially returned may subquently be updated.  To obtain the latest data using the provided ticket ID, call GET `/api/v1.0/tickets/{TicketId}`.
#### Sample request:
```
POST /api/v1.0/tickets/ac6cece8-e4f4-e511-a789-005056bb000e
[
   {
      "AssetId":"4112aa9a-db65-4e49-ad67-a5423010b344"
   }
]
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `TicketId` | `path` | `yes` | `str` | `-` | Ticket ID of the ticket to update |
| `assets` | `Assets` | `body` | `yes` | `list[Any]` | `-` | Asset ID values for the ticket being updated |

#### Returns

- Typed call return: `ListGetResponseOfTicketAsset`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfTicketAsset`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_ticket_custom_fields`

Provenance: Golden Stoplight contract

Operation ID: `Ticket_UpdateTicketCustomFields`

- Sync: `client.tickets.update_ticket_custom_fields(ticket_id=..., values=..., timeout=None)`
- Async: `await client.tickets.update_ticket_custom_fields(ticket_id=..., values=..., timeout=None)`
- Raw payload: `client.tickets.update_ticket_custom_fields.raw(ticket_id=..., values=..., timeout=None)`
- HTTP route: `POST /tickets/{TicketId}/custom-fields`
- Source controller: `Tickets`

Update custom fields

#### Updates a previously submitted ticket's custom fields with provided values.  Please note that based on inputs the updated ticket may have additional update rules fire which may affect final values.  Please note that rules fire asynchronously so ticket data initially returned may subquently be updated.  To obtain the latest data using the provided ticket ID, call GET `/api/v1.0/tickets/{TicketId}`.
#### Sample request:
```
POST /api/v1.0/tickets/ac6cece8-e4f4-e511-a789-005056bb000e
[
   {
      "SiteId":"bb6cece8-e4f4-e511-a789-005056bb000e",
      "CustomFieldId":"4112aa9a-db65-4e49-ad67-a5423010b344",
      "Scope":"Site",
      "CustomFieldTypeId":"e7c8b30d-d899-4193-a70b-21994d2a8089",
      "EntityTypeId":"888891ac-91aa-e711-80c2-100dffa00001",
      "IsRequired":false,
      "IsReadOnly":false,
      "IsHidden":false,
      "Filters":[
         {
            "FilterId":"888861e5-34ff-4fcf-87de-100d6f0e0043",
            "Exclude":false,
            "Value":"d5d91f20-2269-e611-80f1-000c29ab80b0"
         }
      ],
      "DisplayOrder":39,
      "EditorTypeId":12,
      "Value":"",
      "IsValid":true
   }
]
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `TicketId` | `path` | `yes` | `str` | `-` | Ticket ID of the ticket to update |
| `values` | `Values` | `body` | `yes` | `list[Any]` | `-` | Custom field values for the ticket being updated |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_ticket_subject`

Provenance: Golden Stoplight contract

Operation ID: `Ticket_UpdateTicketSubject`

- Sync: `client.tickets.update_ticket_subject(ticket_id=..., update=..., timeout=None)`
- Async: `await client.tickets.update_ticket_subject(ticket_id=..., update=..., timeout=None)`
- Raw payload: `client.tickets.update_ticket_subject.raw(ticket_id=..., update=..., timeout=None)`
- HTTP route: `POST /tickets/{TicketId}/subject`
- Source controller: `Tickets`

Update the subject of a ticket

#### Changes the Subject of an existing ticket
#### Sample request:
```
POST /api/v1.0/tickets/{TicketId:guid}/subject
{
   "TicketId":"c8aef633-a009-48b1-9187-15621defbba8",
   "Subject":"Example New Subject",
}
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `TicketId` | `path` | `yes` | `str` | `-` | Ticket ID that we need to update |
| `update` | `Update` | `body` | `yes` | `UpdateTicketSubjectRequest` | `UpdateTicketSubjectRequest` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
