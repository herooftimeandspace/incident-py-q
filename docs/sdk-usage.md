# SDK Usage

The SDK surface is split into Golden and Silver paths:
- Golden: generated from bundled Stoplight controller contracts.
- Silver: generated from HAR-observed undocumented routes and exposed explicitly under `client.silver`.

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
- `client.silver.<namespace>.*` exposes undocumented Silver routes.
- `client.apps.<service>.*` is the legacy alias for `client.silver.apps.<service>.*`.

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

## Silver Examples

```python
registry = client.silver.apps.registry.list_apps()
actions = client.silver.apps.microsoft_intune.list_remote_actions()
lookup = client.silver.apps.google_device_data.lookup_asset(
    asset_id="asset-guid",
    serial_number="SER123",
)
stats = client.silver.analytics.get_agent_current_stats()
assigned = client.silver.tickets.list_current_user_assigned_tickets()
agent_assigned = client.silver.tickets.list_assigned_tickets_for_agent(
    agent_user_id="agent-guid",
    schema="Open",
)
```

`list_current_user_assigned_tickets(...)` uses the UI-observed read-only `AssignedToMe_Unassigned` queue route. That queue can include current-user assigned rows and unassigned rows; use `client.silver.analytics.get_agent_current_stats(...)` for the tenant's authoritative assigned-to-me and unassigned counts.

Use `list_assigned_tickets_for_agent(...)` when automation authenticates as a service account but needs tickets for a specific human agent. The helper sends `POST /services/tickets` with `Schema` set to `Open` or `All`, an explicit `agent` facet filter, and the UI-style `Client: WebBrowser` header. In live validation for issue #87, `schema="Open"` matched the target agent's expected open-ticket UI count; `schema="All"` returned one more row than the stated UI/history total, so the checked-in docs treat `All` as the API's all-schema result until the UI exclusion rule is known.
