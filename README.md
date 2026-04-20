# incident-py-q

| Main | Staging | Dev | License |
| --- | --- | --- | --- |
| [![Main coverage](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fherooftimeandspace%2Fincident-py-q%2Fbadges%2Fbranch-coverage%2Fmain%2Fcoverage.json)](https://raw.githubusercontent.com/herooftimeandspace/incident-py-q/badges/branch-coverage/main/coverage.json) | [![Staging coverage](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fherooftimeandspace%2Fincident-py-q%2Fbadges%2Fbranch-coverage%2Fstaging%2Fcoverage.json)](https://raw.githubusercontent.com/herooftimeandspace/incident-py-q/badges/branch-coverage/staging/coverage.json) | [![Dev coverage](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fherooftimeandspace%2Fincident-py-q%2Fbadges%2Fbranch-coverage%2Fdev%2Fcoverage.json)](https://raw.githubusercontent.com/herooftimeandspace/incident-py-q/badges/branch-coverage/dev/coverage.json) | [![License repo](https://img.shields.io/github/license/herooftimeandspace/incident-py-q?label=license%20repo)](LICENSE) |
| [![Main unit](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fherooftimeandspace%2Fincident-py-q%2Fbadges%2Fbranch-status%2Fmain%2Funit.json)](https://github.com/herooftimeandspace/incident-py-q/actions/workflows/quality.yml?query=branch%3Amain) | [![Staging unit](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fherooftimeandspace%2Fincident-py-q%2Fbadges%2Fbranch-status%2Fstaging%2Funit.json)](https://github.com/herooftimeandspace/incident-py-q/actions/workflows/quality.yml?query=branch%3Astaging) | [![Dev unit](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fherooftimeandspace%2Fincident-py-q%2Fbadges%2Fbranch-status%2Fdev%2Funit.json)](https://github.com/herooftimeandspace/incident-py-q/actions/workflows/quality.yml?query=branch%3Adev) |  |
| [![Main integration](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fherooftimeandspace%2Fincident-py-q%2Fbadges%2Fbranch-status%2Fmain%2Fintegration.json)](https://github.com/herooftimeandspace/incident-py-q/actions/workflows/integration.yml?query=branch%3Amain) | [![Staging integration](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fherooftimeandspace%2Fincident-py-q%2Fbadges%2Fbranch-status%2Fstaging%2Fintegration.json)](https://github.com/herooftimeandspace/incident-py-q/actions/workflows/integration.yml?query=branch%3Astaging) |  |  |
| [![Main docs](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fherooftimeandspace%2Fincident-py-q%2Fbadges%2Fbranch-status%2Fmain%2Fdocs.json)](https://github.com/herooftimeandspace/incident-py-q/actions/workflows/docs.yml?query=branch%3Amain) |  |  |  |

Contract-driven Incident IQ Python SDK (distribution: `incident-py-q`, import: `incident_py_q`).

Coverage and phase-status badges are published by CI to a dedicated `badges` branch so protected branches (`main`, `staging`, `dev`) never require bot commits for badge refreshes.

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
- `INCIDENTIQ_APP_HEADERS_JSON` (optional JSON object string for app-path calls)

Security hardening rules:
- `INCIDENTIQ_BASE_URL` must use `https`
- base URLs with embedded credentials, query strings, or fragments are rejected
- `client_header` and `site_id` values cannot contain CR/LF characters
- timeout and retry tuning values must stay within safe positive/non-negative bounds

Integration/smoke environment variables:
- `INCIDENTIQ_TEST_BASE_URL` (required for integration tests)
- `INCIDENTIQ_TEST_API_TOKEN` (required for integration tests)
- `INCIDENTIQ_TEST_SITE_ID` (optional)
- `INCIDENTIQ_TEST_CLIENT_HEADER` (optional, default `ApiClient`)
- `INCIDENTIQ_TEST_AUTH_MODE` (optional, default `bearer`)
- `INCIDENTIQ_TEST_APP_HEADERS_JSON` (optional JSON object string for app-path integration calls)
- optional app lookup smoke identifiers for Intune, Mosyle, and Google Device Data

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

Undocumented app-path APIs:

```python
apps = client.apps.registry.list_apps()
intune_lookup = client.apps.microsoft_intune.lookup_asset(
    asset_id="asset-guid",
    serial_number="SER123",
)
google_actions = client.apps.google_device_data.list_remote_actions()
```

## Validation Strategy

- Runtime uses bundled schemas only, never network fetches during requests.
- Success JSON responses are validated against operation response schema.
- Schema violations raise `ValueError` (`SchemaValidationError` subtype).
- App-path calls under `client.apps.*` are validated against bundled HAR-derived schemas.

## Development Commands

```bash
python scripts/run_local_ci.py --target dev
python scripts/run_local_ci.py --target staging
python scripts/run_local_ci.py --target main
```

Branch targets map directly to the GitHub Actions gates:
- `dev`: audit, Ruff, mypy, non-integration tests with coverage, and wheel build
- `staging`: everything in `dev`, plus live integration tests
- `main`: everything in `staging`, plus docs generation

## Schema Sync

Refresh bundled contracts from official upstream sources:

```bash
python scripts/sync_schemas.py
python scripts/update_sdk_inventory.py
python scripts/extract_har_app_inventory.py <intune.har> <mosyle.har> <google.har>
```

Bundled source tree:
- `src/incident_py_q/data/stoplight/controllers/*.json` (primary)
- `src/incident_py_q/data/postman/collection.json` (secondary)
- `src/incident_py_q/data/source_manifest.json` (source manifest)
- `src/incident_py_q/data/app_schemas.json` (HAR-derived app-path schemas)

## Versioning and Stability

- The package follows semantic versioning.
- `incident_py_q.__version__` matches package metadata version.
- Generated SDK surface is semver-significant and protected by golden tests.
- Promotion into `main` requires exactly one release label: `semver:patch`, `semver:minor`, or `semver:major`.
- Promotion workflows propagate the source PR's semver label when one is present and otherwise default the promotion PR to `semver:patch`.

## Documentation

Project docs are built with MkDocs Material and pdoc:

```bash
python scripts/build_docs.py
```
