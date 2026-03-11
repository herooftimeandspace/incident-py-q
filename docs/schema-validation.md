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

## Runtime Validation Flow

1. Match operation by HTTP method + rendered path.
2. Choose response schema using status fallback:
   - exact status code
   - status class wildcard (`2xx`)
   - `default`
3. Validate JSON payload with `jsonschema`.
4. Raise `SchemaValidationError` (`ValueError`) on mismatch.

## Schema Sync Workflow

```bash
python scripts/sync_schemas.py
python scripts/update_sdk_inventory.py
```

The sync script is manifest-driven and supports continue-on-error with required-source failure exit behavior.
