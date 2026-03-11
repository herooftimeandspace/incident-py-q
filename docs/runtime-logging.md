# Logging and Runtime Behavior

## Logging

The SDK uses standard-library `logging` and does not install handlers.

- Logger name: `incident_py_q.client`
- Structured `extra` fields include method/path/status.
- Sensitive headers (Authorization, cookies, API keys) are redacted.

Configure logging in your application as needed:

```python
import logging

logging.basicConfig(level=logging.INFO)
```

## Retry Policy

Conservative retry defaults:
- Retryable statuses: `408`, `429`, `500`, `502`, `503`, `504`
- Retry methods: idempotent methods only (`GET`, `HEAD`, `OPTIONS`, `DELETE`, `PUT`)
- Backoff: exponential with bounded jitter

Non-idempotent writes are not retried by default.

## Auth Behavior

Default auth mode is bearer:
- token `abc` -> `Authorization: Bearer abc`
- pre-prefixed token `Bearer abc` is preserved

Optional raw mode is available for compatibility.
