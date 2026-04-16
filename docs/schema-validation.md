# Schema and Validation

## Bundled Contracts

Primary contract corpus:
- Incident IQ Stoplight Swagger 2.0 controller specs (`/controllers/*.json`)

Secondary compatibility corpus:
- Incident IQ APIHub Postman collection

Bundled assets live under:
- `src/incident_py_q/data/stoplight/controllers/`
- `src/incident_py_q/data/postman/`
- `src/incident_py_q/data/source_manifest.json`
- `src/incident_py_q/data/app_schemas.json`
- `src/incident_py_q/data/silver_inventory.json`

## Runtime Validation Flow

1. Match operation by HTTP method + rendered path.
2. Choose response schema using status fallback:
   - exact status code
   - status class wildcard (`2xx`)
   - `default`
3. Validate JSON payload with `jsonschema`.
4. Raise `SchemaValidationError` (`ValueError`) on mismatch.

Golden routes under `client.<namespace>.*` validate against Stoplight contracts. Silver routes under `client.silver.*` are intentionally kept separate because Stoplight does not publish contracts for them. The typed app helpers under `client.silver.apps.*` and the legacy alias `client.apps.*` use the bundled app schema set where dedicated Silver schemas exist.

## Schema Sync Workflow

```bash
python scripts/sync_schemas.py
python scripts/update_sdk_inventory.py
python scripts/update_silver_inventory.py demo.incidentiq.com.har
python scripts/extract_har_app_inventory.py demo.incidentiq.com.har
```

`update_sdk_inventory.py` refreshes the Golden Stoplight inventory. `update_silver_inventory.py` classifies HAR traffic into Golden, Silver, and discarded routes, writes the bundled Silver inventory, refreshes the merged SDK inventory snapshot, and updates the legacy app-path fixture used by contract tests.
