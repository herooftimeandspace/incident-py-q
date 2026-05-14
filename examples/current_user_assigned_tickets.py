"""Read-only current-user assigned ticket report example.

This example uses only SDK read paths:
- `client.silver.tickets.list_current_user_assigned_tickets(...)` reads the
  UI-observed `AssignedToMe_Unassigned` ticket queue.
- `client.tickets.get_ticket_statuses.raw()` reads the Golden ticket status
  catalog. `.raw()` is used because the live status payload is JSON data that
  the runtime validator now accepts even when Incident IQ omits `WorkflowId`.
- `client.silver.tickets.get_ticket_activities.raw(...)` reads recent ticket
  activity so a report can include recent actions and comments.

Set `INCIDENTIQ_BASE_URL` and `INCIDENTIQ_API_TOKEN` before running. A bare
tenant root such as `https://example.incidentiq.com` is normalized to the
Golden `/api/v1.0` prefix by the SDK.
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from typing import Any

from incident_py_q import Client


def _items(payload: Any) -> list[dict[str, Any]]:
    """Return the common Incident IQ `Items` list from a JSON-compatible payload."""
    if isinstance(payload, Mapping):
        items = payload.get("Items")
        if isinstance(items, list):
            return [dict(item) for item in items if isinstance(item, Mapping)]
    if isinstance(payload, list):
        return [dict(item) for item in payload if isinstance(item, Mapping)]
    return []


def _first_present(row: Mapping[str, Any], names: Iterable[str]) -> Any:
    """Return the first non-empty value from several possible Incident IQ field names."""
    for name in names:
        value = row.get(name)
        if value is not None and value != "":
            return value
    return None


def _status_lookup(status_payload: Any) -> dict[str, str]:
    """Build a best-effort ticket status ID to display-name lookup."""
    lookup: dict[str, str] = {}
    for status in _items(status_payload):
        status_id = _first_present(status, ("TicketStatusTypeId", "WorkflowStepId"))
        status_name = _first_present(status, ("StatusName", "StepName"))
        if status_id is not None and status_name is not None:
            lookup[str(status_id)] = str(status_name)
    return lookup


def _activity_items(activity_payload: Any) -> list[dict[str, Any]]:
    """Flatten common ticket activity response shapes into activity item dictionaries."""
    flattened: list[dict[str, Any]] = []
    for activity in _items(activity_payload):
        nested_items = activity.get("ActivityItems")
        if isinstance(nested_items, list):
            flattened.extend(dict(item) for item in nested_items if isinstance(item, Mapping))
        else:
            flattened.append(activity)
    return flattened


def _recent_comments(activity_payload: Any, *, limit: int = 3) -> list[str]:
    """Extract recent comment text from a ticket activity payload."""
    comments: list[str] = []
    for item in _activity_items(activity_payload):
        comment = _first_present(item, ("Comments", "Comment", "Body", "Text"))
        if comment is not None:
            comments.append(str(comment))
        if len(comments) >= limit:
            break
    return comments


def _recent_actions(activity_payload: Any, *, limit: int = 3) -> list[str]:
    """Extract recent action labels or notes from a ticket activity payload."""
    actions: list[str] = []
    for item in _activity_items(activity_payload):
        action = _first_present(
            item,
            (
                "ResolutionActionName",
                "ActionName",
                "TicketActivityTypeName",
                "Notes",
                "Subject",
            ),
        )
        if action is not None:
            actions.append(str(action))
        if len(actions) >= limit:
            break
    return actions


def build_current_user_ticket_report(client: Client, *, page_size: int = 100) -> list[dict[str, Any]]:
    """Fetch assigned tickets plus status, urgency, recent actions, and recent comments."""
    statuses = _status_lookup(client.tickets.get_ticket_statuses.raw())
    tickets_payload = client.silver.tickets.list_current_user_assigned_tickets(
        page_size=page_size,
        sort_by="TicketModifiedDate",
        sort_direction="Descending",
    )

    report_rows: list[dict[str, Any]] = []
    for ticket in _items(tickets_payload):
        ticket_id = _first_present(ticket, ("TicketId", "Id"))
        if ticket_id is None:
            continue
        activities = client.silver.tickets.get_ticket_activities.raw(ticket_id=str(ticket_id))
        status_id = _first_present(ticket, ("TicketStatusTypeId", "WorkflowStepId", "StatusId"))
        report_rows.append(
            {
                "ticket_id": str(ticket_id),
                "ticket_number": _first_present(ticket, ("TicketNumber", "Number")),
                "subject": _first_present(ticket, ("TicketSubject", "Subject")),
                "status": (
                    _first_present(ticket, ("TicketStatusName", "StatusName"))
                    or statuses.get(str(status_id))
                ),
                "priority": _first_present(ticket, ("TicketPriority", "Priority", "PriorityName")),
                "is_urgent": bool(_first_present(ticket, ("IsUrgent", "Urgent"))),
                "recent_actions": _recent_actions(activities),
                "recent_comments": _recent_comments(activities),
            }
        )
    return report_rows


def main() -> None:
    """Print a compact report for the current authenticated user's assigned tickets."""
    with Client.from_env() as client:
        for row in build_current_user_ticket_report(client):
            print(row)


if __name__ == "__main__":
    main()
