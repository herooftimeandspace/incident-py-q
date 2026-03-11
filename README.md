# incident-py-q

Contract-driven Incident IQ Python SDK (distribution: `incident-py-q`, import: `incident_py_q`).

The package ships:
- sync and async clients (`Client`, `AsyncClient`)
- strict runtime response validation against bundled Incident IQ contracts
- dynamic SDK namespaces generated from schema operations
- schema sync tooling for Stoplight controller specs and APIHub Postman artifacts
- contract/unit/integration tests, docs site tooling, and CI workflows

## Requirements

- Python `3.14+`

## Install

```bash
python -m pip install incident-py-q
```

Development install:

```bash
python -m pip install -e '.[dev]'
```

## Authentication and Tenant URL

Default auth mode is bearer token:

```text
Authorization: Bearer <token>
```

Each client requires a tenant-specific base URL (typically including your API path prefix, such as `/api/v1`).

Runtime environment variables:
- `INCIDENTIQ_BASE_URL` (required unless passed explicitly)
- `INCIDENTIQ_API_TOKEN` (required unless passed explicitly)
- `INCIDENTIQ_SITE_ID` (optional)
- `INCIDENTIQ_CLIENT_HEADER` (optional, default `ApiClient`)
- `INCIDENTIQ_AUTH_MODE` (optional, default `bearer`, supported: `bearer`, `raw`)

Integration/smoke environment variables:
- `INCIDENTIQ_TEST_BASE_URL` (required for integration tests)
- `INCIDENTIQ_TEST_API_TOKEN` (required for integration tests)
- `INCIDENTIQ_TEST_SITE_ID` (optional)
- `INCIDENTIQ_TEST_CLIENT_HEADER` (optional, default `ApiClient`)
- `INCIDENTIQ_TEST_AUTH_MODE` (optional, default `bearer`)

## SDK-First Quick Start

```python
from incident_py_q import Client

client = Client(
    base_url="https://your-tenant.incidentiq.com/api/v1",
    api_token="your-token",
)

users = client.users.get_users_legacy()
users_raw = client.users.get_users_legacy.raw()
```

Async:

```python
import asyncio
from incident_py_q import AsyncClient

async def main() -> None:
    async with AsyncClient(
        base_url="https://your-tenant.incidentiq.com/api/v1",
        api_token="your-token",
    ) as client:
        payload = await client.users.get_users_legacy.raw()
        print(type(payload))

asyncio.run(main())
```

Low-level request API:

```python
payload = client.request(
    "GET",
    "/users/{UserId}",
    path_params={"UserId": "00000000-0000-0000-0000-000000000000"},
)
```

## Validation Strategy

- Runtime uses bundled schemas only, never network fetches during requests.
- Success JSON responses are validated against operation response schema.
- Schema violations raise `ValueError` (`SchemaValidationError` subtype).

## Development Commands

```bash
ruff check .
mypy src tests scripts
pytest -m "not integration"
pytest -m integration
python -m pip wheel --no-deps --wheel-dir dist .
python scripts/build_docs.py
```

## Schema Sync

Refresh bundled contracts from official upstream sources:

```bash
python scripts/sync_schemas.py
python scripts/update_sdk_inventory.py
```

Bundled source tree:
- `src/incident_py_q/data/stoplight/controllers/*.json` (primary)
- `src/incident_py_q/data/postman/collection.json` (secondary)
- `src/incident_py_q/data/source_manifest.json` (source manifest)

## Versioning and Stability

- The package follows semantic versioning.
- `incident_py_q.__version__` matches package metadata version.
- Generated SDK surface is semver-significant and protected by golden tests.

## Documentation

Project docs are built with MkDocs Material and pdoc:

```bash
python scripts/build_docs.py
```
