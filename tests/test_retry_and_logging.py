"""Tests for retry policy and logging redaction helpers."""

from __future__ import annotations

from incident_py_q.logging_utils import redact_headers
from incident_py_q.retry import compute_backoff_seconds, method_is_idempotent, should_retry_status


def test_retry_status_and_idempotency_rules() -> None:
    assert should_retry_status(503)
    assert not should_retry_status(404)

    assert method_is_idempotent("GET")
    assert method_is_idempotent("put")
    assert not method_is_idempotent("POST")


def test_backoff_is_non_negative() -> None:
    value = compute_backoff_seconds(attempt=2, base=0.1)
    assert value >= 0.4


def test_header_redaction() -> None:
    headers = {
        "Authorization": "Bearer token",
        "Client": "ApiClient",
        "Cookie": "secret",
    }
    redacted = redact_headers(headers)
    assert redacted["Authorization"] == "***REDACTED***"
    assert redacted["Cookie"] == "***REDACTED***"
    assert redacted["Client"] == "ApiClient"
