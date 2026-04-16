# `alerts` Golden Namespace

Sync client access: `client.alerts`

Async client access: `client.alerts` with `await` on method calls.

These methods are Golden because they come from bundled Stoplight controller contracts.

## Aliases

| Alias | Canonical Method | Route |
| --- | --- | --- |
| `create` | `queue_notification` | `POST /alerts/new` |

## Methods

### `queue_notification`

Provenance: Golden Stoplight contract

Operation ID: `Alerts_QueueNotification`

- Sync: `client.alerts.queue_notification(notification=..., timeout=None)`
- Async: `await client.alerts.queue_notification(notification=..., timeout=None)`
- Raw payload: `client.alerts.queue_notification.raw(notification=..., timeout=None)`
- HTTP route: `POST /alerts/new`
- Source controller: `Emails & Notifications`
- Aliases: `create`

Send a new notification

#### Allows creation / sending of notifications within Incident IQ.  Notifications can be directed at users with varying severity.  Content may include rich HTML and links to other resources.
#### Sample request:
```
POST /api/v1.0/alerts/new
{
  "AlertKey": "Custom-Notification-1",
  "EntityTypeId": "ac6cece8-e4f4-e511-a789-005056bb000e",
  "EntityId": "ac6cece8-e4f4-e511-a789-005056bb000e",
  "Severity": 20,
  "Subject": "Test notification 1",
  "Details": "New notification content - click &lt;a href="#"&gt;here&lt;/a&gt;"
}
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `notification` | `notification` | `body` | `yes` | `Alert` | `Alert` | Notification details / parameters |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
