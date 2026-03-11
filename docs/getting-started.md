# Getting Started

## Requirements

- Python `3.14+`

## Install

```bash
python -m pip install incident-py-q
```

## Environment Variables

Runtime:
- `INCIDENTIQ_BASE_URL`
- `INCIDENTIQ_API_TOKEN`
- `INCIDENTIQ_SITE_ID` (optional)
- `INCIDENTIQ_CLIENT_HEADER` (optional, default `ApiClient`)
- `INCIDENTIQ_AUTH_MODE` (optional, default `bearer`)

Integration smoke tests:
- `INCIDENTIQ_TEST_BASE_URL`
- `INCIDENTIQ_TEST_API_TOKEN`
- `INCIDENTIQ_TEST_SITE_ID` (optional)
- `INCIDENTIQ_TEST_CLIENT_HEADER` (optional)
- `INCIDENTIQ_TEST_AUTH_MODE` (optional)

## Sync Client

```python
from incident_py_q import Client

client = Client.from_env()
users = client.users.get_users_legacy()
client.close()
```

## Async Client

```python
import asyncio
from incident_py_q import AsyncClient

async def main() -> None:
    async with AsyncClient.from_env() as client:
        users = await client.users.get_users_legacy()
        print(users)

asyncio.run(main())
```
