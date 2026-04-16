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
- `INCIDENTIQ_APP_HEADERS_JSON` (optional JSON object string for app-path calls)

Integration smoke tests:
- `INCIDENTIQ_TEST_BASE_URL`
- `INCIDENTIQ_TEST_API_TOKEN`
- `INCIDENTIQ_TEST_SITE_ID` (optional)
- `INCIDENTIQ_TEST_CLIENT_HEADER` (optional)
- `INCIDENTIQ_TEST_AUTH_MODE` (optional)
- `INCIDENTIQ_TEST_APP_HEADERS_JSON` (optional JSON object string)
- Optional app lookup smoke identifiers:
  - `INCIDENTIQ_TEST_INTUNE_ASSET_ID` / `INCIDENTIQ_TEST_INTUNE_ASSET_SERIAL` / `INCIDENTIQ_TEST_INTUNE_ASSET_TAG`
  - `INCIDENTIQ_TEST_MOSYLE_ASSET_ID` / `INCIDENTIQ_TEST_MOSYLE_ASSET_SERIAL` / `INCIDENTIQ_TEST_MOSYLE_ASSET_TAG`
  - `INCIDENTIQ_TEST_GOOGLE_DEVICE_ASSET_ID` / `INCIDENTIQ_TEST_GOOGLE_DEVICE_ASSET_SERIAL` / `INCIDENTIQ_TEST_GOOGLE_DEVICE_ASSET_TAG`

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

## Silver Namespace

Golden methods stay on `client.<namespace>.*`. Undocumented supplementary routes are exposed under `client.silver.*`.

The legacy app-path alias still exists on `client.apps`, but the preferred explicit path is `client.silver.apps`:

```python
apps = client.silver.apps.registry.list_apps()
intune = client.silver.apps.microsoft_intune.lookup_asset(
    asset_id="asset-guid",
    serial_number="SER123",
)
serial_lookup = client.silver.assets.get_asset_by_serial(serial="SER123")
```
