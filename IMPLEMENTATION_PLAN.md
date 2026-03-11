# Incident IQ SDK Build Plan (`incident-py-q`)

## Summary
Build a production-ready Python package (`incident-py-q`, import `incident_py_q`) with sync+async clients, strict schema validation, dynamic SDK generation, contract-driven tests, docs, and CI/CD.  
Primary contract source is Incident IQ Stoplight Swagger 2.0 controller specs; APIHub Postman collection is bundled as a secondary contract corpus.

## Key Constraints and Public Interfaces
- Python target is **3.14+** only.
- Default auth behavior is **Bearer token** (`Authorization: Bearer <token>`).
- Client supports explicit tenant URL configuration for SDK/runtime and integration smoke tests.
- Public entry points:
  - `incident_py_q.Client`
  - `incident_py_q.AsyncClient`
- Unified request method on both:
  - `request(method, path, *, path_params=None, params=None, json=None, headers=None, timeout=None) -> dict | list | None`
- Config surface:
  - `base_url` (tenant-specific, required unless provided by env)
  - `api_token`
  - `site_id` (optional/required depending on endpoint policy)
  - `client_header` (default `ApiClient`)
  - `auth_mode` (default `bearer`; optional `raw` for compatibility)
- Tenant URL env vars:
  - `INCIDENTIQ_BASE_URL` for normal SDK usage
  - `INCIDENTIQ_TEST_BASE_URL` for integration/smoke tests
  - tests fail-fast/skip cleanly with clear messaging if test base URL or creds are missing

## Implementation Changes
- Package layout under `src/incident_py_q`:
  - core transport (sync+async parity, retries, logging redaction)
  - auth/header policy (Bearer default)
  - schema loader/registry/validator
  - dynamic SDK namespace/method generator from operation metadata
- Schema sync tooling:
  - Stoplight GraphQL source (workspace `incidentiq`, project `v1`, default branch, `/controllers/*.json`)
  - APIHub Postman collection source
  - manifest-driven sync script with continue-on-error reporting and required-source failure exit
- Runtime validation:
  - method/path operation matching
  - status-code response schema selection
  - `jsonschema` validation for successful responses
  - `ValueError` on schema validation failure
- SDK ergonomics:
  - snake_case params from schema names
  - typed Pydantic response models by default when possible
  - `.raw(...)` for validated JSON
  - stable inventory snapshot for semver governance

## Test Plan
- Unit tests:
  - auth/header behavior (Bearer default, optional `site_id`/`client` behavior)
  - request construction, retries, timeout, error propagation
  - schema loading/matching/ref resolution/validation
  - SDK generation + signatures + sync/async parity
- Contract tests (schema-driven):
  - coverage across bundled Stoplight operations
  - compatibility checks against bundled Postman corpus
  - golden SDK surface inventory drift detection
- Integration tests (`@pytest.mark.integration`):
  - use `INCIDENTIQ_TEST_BASE_URL` explicitly
  - read-only smoke endpoints only
  - skip cleanly when credentials/base URL are absent
- Packaging/resource tests:
  - verify bundled schemas load from installed wheel/sdist

## Docs, CI/CD, and Artifact
- Docs:
  - `README.md`, `CHANGELOG.md`, `CONTRIBUTING.md`, `SECURITY.md`, `.env.example`
  - MkDocs Material site + pdoc API reference integration
  - explicit section for tenant URL setup (`INCIDENTIQ_BASE_URL`, `INCIDENTIQ_TEST_BASE_URL`)
- CI:
  - quality workflow: Python **3.14+**, ruff, mypy, tests (non-integration), build, docs build
  - integration workflow: secrets + `INCIDENTIQ_TEST_BASE_URL` gated
  - GitHub Pages docs publish workflow
- Plan artifact:
  - `IMPLEMENTATION_PLAN.md` (this document)

## Assumptions and Defaults
- Distribution: `incident-py-q`; import: `incident_py_q`.
- Python 3.14+ required for runtime and CI.
- Bearer token is default auth mode.
- Tenant URL is always configurable per client instance and separately for integration smoke tests.

