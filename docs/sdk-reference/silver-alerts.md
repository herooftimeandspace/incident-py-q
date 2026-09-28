# `silver.alerts` Namespace

Sync client access: `client.silver.alerts`

Async client access: `client.silver.alerts` with `await` on method calls.

These methods are Silver because the published contract does not document them directly, or because the SDK intentionally wraps a narrower Silver workflow around existing Golden operations. They remain separate so undocumented or convenience behavior never overrides the documented SDK surface.

## Methods

### `queue_notification`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.alerts.queue_notification(json_body=..., timeout=None)`
- Async: `await client.silver.alerts.queue_notification(json_body=..., timeout=None)`
- Raw payload: `client.silver.alerts.queue_notification.raw(json_body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/alerts/new`
- Observed in: `migrated_from_golden_stoplight`

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

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.alerts.queue_notification` (operationId `Alerts_QueueNotification`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `json_body` | `notification` | `body` | `yes` | `dict[str, Any] | list[Any]` | Notification details / parameters |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---
