"""Retry/backoff policy for Incident IQ HTTP calls."""

from __future__ import annotations

import random

RETRYABLE_STATUSES = {408, 429, 500, 502, 503, 504}
IDEMPOTENT_METHODS = {"GET", "HEAD", "OPTIONS", "DELETE", "PUT"}


def should_retry_status(status_code: int) -> bool:
    """Return whether an HTTP status should be retried."""
    return status_code in RETRYABLE_STATUSES


def method_is_idempotent(method: str) -> bool:
    """Return whether a method is treated as safely retryable by default."""
    return method.upper() in IDEMPOTENT_METHODS


def compute_backoff_seconds(attempt: int, base: float) -> float:
    """Compute exponential backoff with bounded jitter.

    Attempt is zero-based.
    """
    jitter = float(random.uniform(0.0, base))
    return float((base * (2**attempt)) + jitter)
