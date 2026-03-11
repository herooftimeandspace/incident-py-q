# Incident IQ SDK

`incident-py-q` is a schema-driven Incident IQ client/SDK for Python 3.14+.

It combines:
- low-level request client (sync + async)
- contract-backed response validation
- dynamic namespace SDK generated from bundled schema operations
- contract and golden-surface testing to prevent accidental API drift

## Design Highlights

- Bearer token auth by default.
- Tenant base URL is explicit and configurable per client instance.
- Runtime never downloads schema documents.
- Integration tests use separate `INCIDENTIQ_TEST_*` variables for smoke usage.

## Quick Example

```python
from incident_py_q import Client

client = Client(
    base_url="https://your-tenant.incidentiq.com/api/v1",
    api_token="your-token",
)

payload = client.users.get_users_legacy.raw()
print(type(payload))
client.close()
```
