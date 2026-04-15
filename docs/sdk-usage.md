# SDK Usage

The SDK surface is generated from bundled operation contracts.

Full generated method and route documentation lives under the SDK reference pages.

## Namespace Pattern

```python
from incident_py_q import Client

client = Client.from_env()
print(client.tickets.list_methods())
```

Common shape:
- `client.<namespace>.<method>(...)` returns typed Pydantic models when representable.
- `client.<namespace>.<method>.raw(...)` returns validated JSON payloads.
- `client.<namespace>.list_methods()` enumerates the generated runtime surface for that namespace.

## Request Signatures

Generated method parameters are snake_case from schema names:
- `ThingId` -> `thing_id`
- `pageSize` -> `page_size`

## Pagination Helper

When paging query parameters are present, `iter_pages(...)` is available:

```python
pages = client.tickets.get_tickets.iter_pages(start_page=1, page_size=100, max_pages=3)
```

## Low-Level Request API

```python
payload = client.request(
    "GET",
    "/users/{UserId}",
    path_params={"UserId": "00000000-0000-0000-0000-000000000000"},
)
```
