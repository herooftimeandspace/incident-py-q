# `notifications` Namespace

Sync client access: `client.notifications`

Async client access: `client.notifications` with `await` on method calls.

## Aliases

| Alias | Canonical Method | Route |
| --- | --- | --- |
| `create` | `get_notifications` | `POST /notifications` |

## Methods

### `get_notifications`

Operation ID: `Notification_GetNotifications`

- Sync: `client.notifications.get_notifications(request_info=..., timeout=None)`
- Async: `await client.notifications.get_notifications(request_info=..., timeout=None)`
- Raw payload: `client.notifications.get_notifications.raw(request_info=..., timeout=None)`
- HTTP route: `POST /notifications`
- Source controller: `Emails & Notifications`
- Aliases: `create`

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

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `request_info` | `RequestInfo` | `body` | `yes` | `GetNotificationsRequest` | `GetNotificationsRequest` | - |

#### Returns

- Typed call return: `ListGetResponseOfNotification`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfNotification`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_ticket_emails`

Operation ID: `Notification_GetTicketEmails`

- Sync: `client.notifications.get_ticket_emails(ticket_id=..., timeout=None)`
- Async: `await client.notifications.get_ticket_emails(ticket_id=..., timeout=None)`
- Raw payload: `client.notifications.get_ticket_emails.raw(ticket_id=..., timeout=None)`
- HTTP route: `GET /notifications/emails/for/ticket/{TicketId}`
- Source controller: `Emails & Notifications`

Get emails for ticket

#### For a specific, single ticket query the system for all related emails
#### Sample request:
```
GET /api/v1.0/notifications/emails/for/ticket/ac6cece8-e4f4-e511-a789-005056bb000e
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `TicketId` | `path` | `yes` | `str` | `-` | Ticket ID of the record to query |

#### Returns

- Typed call return: `ListGetResponseOfEmail`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfEmail`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_unarchived_notifications`

Operation ID: `Notification_GetUnarchivedNotifications`

- Sync: `client.notifications.get_unarchived_notifications(timeout=None)`
- Async: `await client.notifications.get_unarchived_notifications(timeout=None)`
- Raw payload: `client.notifications.get_unarchived_notifications.raw(timeout=None)`
- HTTP route: `GET /notifications/unarchived`
- Source controller: `Emails & Notifications`

Get unarchived

#### Queries the system for any unarchived notifications
#### Sample request:
```
GET /api/v1.0/notifications/unarchived
```

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `ListGetResponseOfNotification`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfNotification`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_unread_notifications`

Operation ID: `Notification_GetUnreadNotifications`

- Sync: `client.notifications.get_unread_notifications(timeout=None)`
- Async: `await client.notifications.get_unread_notifications(timeout=None)`
- Raw payload: `client.notifications.get_unread_notifications.raw(timeout=None)`
- HTTP route: `GET /notifications/unread`
- Source controller: `Emails & Notifications`

Get unread

#### Queries the system for any unread notifications
#### Sample request:
```
GET /api/v1.0/notifications/unread
```

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `ListGetResponseOfNotification`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfNotification`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `mark_all_notifications_archived`

Operation ID: `Notification_MarkAllNotificationsArchived`

- Sync: `client.notifications.mark_all_notifications_archived(timeout=None)`
- Async: `await client.notifications.mark_all_notifications_archived(timeout=None)`
- Raw payload: `client.notifications.mark_all_notifications_archived.raw(timeout=None)`
- HTTP route: `POST /notifications/all-archive`
- Source controller: `Emails & Notifications`

Mark all notification as archived

#### Marks all notifications that are not yet marked "archived" as "archived"
#### Sample request:
```
POST /api/v1.0/notifications/all-archive
```

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `mark_all_notifications_read`

Operation ID: `Notification_MarkAllNotificationsRead`

- Sync: `client.notifications.mark_all_notifications_read(timeout=None)`
- Async: `await client.notifications.mark_all_notifications_read(timeout=None)`
- Raw payload: `client.notifications.mark_all_notifications_read.raw(timeout=None)`
- HTTP route: `POST /notifications/all-read`
- Source controller: `Emails & Notifications`

Mark all notification as read

#### Marks all notifications that are not yet marked "read" as "read"
#### Sample request:
```
POST /api/v1.0/notifications/all-read
```

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `mark_notification_archived`

Operation ID: `Notification_MarkNotificationArchived`

- Sync: `client.notifications.mark_notification_archived(notification_id=..., timeout=None)`
- Async: `await client.notifications.mark_notification_archived(notification_id=..., timeout=None)`
- Raw payload: `client.notifications.mark_notification_archived.raw(notification_id=..., timeout=None)`
- HTTP route: `POST /notifications/{NotificationId}/archive`
- Source controller: `Emails & Notifications`

Mark notification as archived

#### Marks a provided single notification as "archived"
#### Sample request:
```
POST /api/v1.0/notifications/ac6cece8-e4f4-e511-a789-005056bb000e/archive
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `notification_id` | `NotificationId` | `path` | `yes` | `str` | `-` | Notification ID of the record to modify |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `mark_notification_read`

Operation ID: `Notification_MarkNotificationRead`

- Sync: `client.notifications.mark_notification_read(notification_id=..., timeout=None)`
- Async: `await client.notifications.mark_notification_read(notification_id=..., timeout=None)`
- Raw payload: `client.notifications.mark_notification_read.raw(notification_id=..., timeout=None)`
- HTTP route: `POST /notifications/{NotificationId}/read`
- Source controller: `Emails & Notifications`

Mark notification as read

#### Marks a provided single notification as "read"
#### Sample request:
```
POST /api/v1.0/notifications/ac6cece8-e4f4-e511-a789-005056bb000e/read
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `notification_id` | `NotificationId` | `path` | `yes` | `str` | `-` | Notification ID of the record to modify |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
