# `silver.notifications` Namespace

Sync client access: `client.silver.notifications`

Async client access: `client.silver.notifications` with `await` on method calls.

These methods are Silver because the published contract does not document them directly, or because the SDK intentionally wraps a narrower Silver workflow around existing Golden operations. They remain separate so undocumented or convenience behavior never overrides the documented SDK surface.

## Methods

### `get_notifications`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.notifications.get_notifications(json_body=..., timeout=None)`
- Async: `await client.silver.notifications.get_notifications(json_body=..., timeout=None)`
- Raw payload: `client.silver.notifications.get_notifications.raw(json_body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/notifications`
- Observed in: `migrated_from_golden_stoplight`

Query notifications

#### Queries the system for any notifications based on submitted request parameters
#### Sample request:
```
POST /api/v1.0/notifications
{
  "IncludeRead": true,
  "IncludeArchived": true,
  "IncludeUnarchived": true
}
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.notifications.get_notifications` (operationId `Notification_GetNotifications`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `json_body` | `RequestInfo` | `body` | `yes` | `dict[str, Any] | list[Any]` | Body parameter migrated from the previous Golden SDK. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_ticket_emails`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.notifications.get_ticket_emails(ticket_id=..., timeout=None)`
- Async: `await client.silver.notifications.get_ticket_emails(ticket_id=..., timeout=None)`
- Raw payload: `client.silver.notifications.get_ticket_emails.raw(ticket_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/notifications/emails/for/ticket/{ticket_id}`
- Observed in: `migrated_from_golden_stoplight`

Get emails for ticket

#### For a specific, single ticket query the system for all related emails
#### Sample request:
```
GET /api/v1.0/notifications/emails/for/ticket/ac6cece8-e4f4-e511-a789-005056bb000e
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.notifications.get_ticket_emails` (operationId `Notification_GetTicketEmails`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `ticket_id` | `TicketId` | `path` | `yes` | `str` | Ticket ID of the record to query |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_unarchived_notifications`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.notifications.get_unarchived_notifications(timeout=None)`
- Async: `await client.silver.notifications.get_unarchived_notifications(timeout=None)`
- Raw payload: `client.silver.notifications.get_unarchived_notifications.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/notifications/unarchived`
- Observed in: `migrated_from_golden_stoplight`

Get unarchived

#### Queries the system for any unarchived notifications
#### Sample request:
```
GET /api/v1.0/notifications/unarchived
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.notifications.get_unarchived_notifications` (operationId `Notification_GetUnarchivedNotifications`).

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `get_unread_notifications`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.notifications.get_unread_notifications(timeout=None)`
- Async: `await client.silver.notifications.get_unread_notifications(timeout=None)`
- Raw payload: `client.silver.notifications.get_unread_notifications.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/notifications/unread`
- Observed in: `migrated_from_golden_stoplight`

Get unread

#### Queries the system for any unread notifications
#### Sample request:
```
GET /api/v1.0/notifications/unread
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.notifications.get_unread_notifications` (operationId `Notification_GetUnreadNotifications`).

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `mark_all_notifications_archived`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.notifications.mark_all_notifications_archived(timeout=None)`
- Async: `await client.silver.notifications.mark_all_notifications_archived(timeout=None)`
- Raw payload: `client.silver.notifications.mark_all_notifications_archived.raw(timeout=None)`
- HTTP route: `POST /api/v1.0/notifications/all-archive`
- Observed in: `migrated_from_golden_stoplight`

Mark all notification as archived

#### Marks all notifications that are not yet marked "archived" as "archived"
#### Sample request:
```
POST /api/v1.0/notifications/all-archive
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.notifications.mark_all_notifications_archived` (operationId `Notification_MarkAllNotificationsArchived`).

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `mark_all_notifications_read`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.notifications.mark_all_notifications_read(timeout=None)`
- Async: `await client.silver.notifications.mark_all_notifications_read(timeout=None)`
- Raw payload: `client.silver.notifications.mark_all_notifications_read.raw(timeout=None)`
- HTTP route: `POST /api/v1.0/notifications/all-read`
- Observed in: `migrated_from_golden_stoplight`

Mark all notification as read

#### Marks all notifications that are not yet marked "read" as "read"
#### Sample request:
```
POST /api/v1.0/notifications/all-read
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.notifications.mark_all_notifications_read` (operationId `Notification_MarkAllNotificationsRead`).

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `mark_notification_archived`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.notifications.mark_notification_archived(notification_id=..., timeout=None)`
- Async: `await client.silver.notifications.mark_notification_archived(notification_id=..., timeout=None)`
- Raw payload: `client.silver.notifications.mark_notification_archived.raw(notification_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/notifications/{notification_id}/archive`
- Observed in: `migrated_from_golden_stoplight`

Mark notification as archived

#### Marks a provided single notification as "archived"
#### Sample request:
```
POST /api/v1.0/notifications/ac6cece8-e4f4-e511-a789-005056bb000e/archive
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.notifications.mark_notification_archived` (operationId `Notification_MarkNotificationArchived`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `notification_id` | `NotificationId` | `path` | `yes` | `str` | Notification ID of the record to modify |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---

### `mark_notification_read`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.notifications.mark_notification_read(notification_id=..., timeout=None)`
- Async: `await client.silver.notifications.mark_notification_read(notification_id=..., timeout=None)`
- Raw payload: `client.silver.notifications.mark_notification_read.raw(notification_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/notifications/{notification_id}/read`
- Observed in: `migrated_from_golden_stoplight`

Mark notification as read

#### Marks a provided single notification as "read"
#### Sample request:
```
POST /api/v1.0/notifications/ac6cece8-e4f4-e511-a789-005056bb000e/read
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.notifications.mark_notification_read` (operationId `Notification_MarkNotificationRead`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `notification_id` | `NotificationId` | `path` | `yes` | `str` | Notification ID of the record to modify |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---
