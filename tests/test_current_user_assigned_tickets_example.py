"""Tests for the current-user assigned tickets example helpers."""

from __future__ import annotations

from typing import Any, cast

from examples.current_user_assigned_tickets import build_current_user_ticket_report


class _RawEndpoint:
    """Minimal endpoint double for SDK methods that expose a `.raw()` call."""

    def __init__(self, payload: Any = None) -> None:
        self.payload = payload
        self.calls: list[dict[str, Any]] = []

    def raw(self, **kwargs: Any) -> Any:
        """Record the raw call and return the configured payload."""
        self.calls.append(kwargs)
        return self.payload


class _TicketStatusNamespace:
    """Fake Golden tickets namespace containing only status lookup support."""

    def __init__(self, status_payload: Any) -> None:
        self.get_ticket_statuses = _RawEndpoint(status_payload)


class _SilverTicketsNamespace:
    """Fake Silver tickets namespace containing queue and activity methods."""

    def __init__(self, queue_payload: Any, activity_payload: Any) -> None:
        self._queue_payload = queue_payload
        self.list_current_user_assigned_tickets_calls: list[dict[str, Any]] = []
        self.get_ticket_activities = _RawEndpoint(activity_payload)

    def list_current_user_assigned_tickets(self, **kwargs: Any) -> Any:
        """Record the queue call and return assigned ticket rows."""
        self.list_current_user_assigned_tickets_calls.append(kwargs)
        return self._queue_payload


class _SilverNamespace:
    """Fake Silver namespace exposing ticket queue helpers."""

    def __init__(self, tickets: _SilverTicketsNamespace) -> None:
        self.tickets = tickets


class _Client:
    """Fake SDK client with only the namespaces used by the example."""

    def __init__(self, *, status_payload: Any, queue_payload: Any, activity_payload: Any) -> None:
        self.tickets = _TicketStatusNamespace(status_payload)
        self.silver = _SilverNamespace(_SilverTicketsNamespace(queue_payload, activity_payload))


def test_current_user_ticket_report_reads_nested_workflow_step_status() -> None:
    """Queue rows with nested `WorkflowStep` status data produce non-empty statuses."""
    client = _Client(
        status_payload={"Items": []},
        queue_payload={
            "Items": [
                {
                    "TicketId": "ticket-1",
                    "TicketNumber": "T-1",
                    "TicketSubject": "Printer issue",
                    "WorkflowStepId": "workflow-step-1",
                    "WorkflowStep": {
                        "WorkflowStepId": "workflow-step-1",
                        "StatusName": "Submitted",
                        "StepName": "Submitted",
                    },
                }
            ]
        },
        activity_payload={"Items": []},
    )

    report = build_current_user_ticket_report(cast(Any, client))

    assert report[0]["status"] == "Submitted"
