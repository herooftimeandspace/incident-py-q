"""Logging helpers with secret redaction."""

from __future__ import annotations

from collections.abc import Mapping

SENSITIVE_HEADER_NAMES = {
    "authorization",
    "x-api-key",
    "cookie",
    "set-cookie",
    "app-token",
    "apptoken",
    "usertoken",
    "sessionid",
    "x-app-token",
    "x-client-id",
    "x-client-secret",
    "x-xsrf-token",
}


def redact_headers(headers: Mapping[str, str] | None) -> dict[str, str]:
    """Return a redacted copy of headers suitable for structured logs."""
    if not headers:
        return {}
    redacted: dict[str, str] = {}
    for key, value in headers.items():
        if key.lower() in SENSITIVE_HEADER_NAMES:
            redacted[key] = "***REDACTED***"
        else:
            redacted[key] = value
    return redacted
