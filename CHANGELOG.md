# Changelog

All notable changes to `incident-py-q` are documented in this file.

The format is based on Keep a Changelog and this project follows Semantic Versioning.

## [0.1.0] - 2026-03-11

### Added
- Initial `incident_py_q` package with sync and async clients.
- Bearer-token auth by default, with optional raw mode.
- Tenant base URL support for runtime and integration tests.
- Schema runtime (`loader`, `registry`, `validator`) using bundled Stoplight and Postman artifacts.
- Dynamic SDK namespace and method generation from bundled controller contracts.
- Schema sync tooling via `scripts/sync_schemas.py`.
- Unit, contract, integration, and packaging/resource tests.
- Golden SDK inventory test for semver-governed public surface drift.
- MkDocs Material documentation + pdoc API docs generation scripts.
- GitHub Actions workflows for quality gates, integration tests, and docs publishing.
