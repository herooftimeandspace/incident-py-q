# Changelog

All notable changes to `incident-py-q` are documented in this file.

The format is based on Keep a Changelog and this project follows Semantic Versioning.

## [Unreleased]

### Changed
- **Breaking:** The Golden contract source is now the published Incident IQ OpenAPI 3.0
  document behind the [API reference](https://scopousiiq.github.io/iiq-docusaurus-docs/docs/api/).
  It replaces the Stoplight GraphQL controller sync and the APIHub Postman collection.
- `scripts/sync_schemas.py` fetches and validates that single OpenAPI document instead of
  querying Stoplight's GraphQL API and APIHub.
- `scripts/update_sdk_inventory.py` now regenerates the Golden, Silver, and merged
  inventory snapshots together.
- The generated SDK surface grew from 173 to 863 operations across 37 namespaces.
  Operation ids and method names follow the new contract, so many Golden methods were
  renamed (for example `tickets.get_ticket_statuses` is now `tickets.list_ticket_statuses`).
- Golden paths are now tenant-absolute (`/api/v1.0/...`).
- Silver no longer exposes routes the Golden contract documents; 45 HAR-derived routes
  were retired in favor of their documented Golden equivalents.
- The 64 routes the published contract stopped documenting moved to `client.silver.*`
  rather than being dropped. They keep strict response validation against a pruned copy
  of the previous contract.

### Deprecated
- Every pre-migration method name still resolves, as a deprecated alias that forwards to
  its new location and emits a `DeprecationWarning`: 50 renamed Golden methods and 64
  routes migrated to Silver. Aliases are excluded from `sdk_inventory()` and will be
  removed in a future release. See `docs/migration-openapi.md`.
- Namespaces the new contract dropped (`alerts`, `forms`, `manufacturers`, `notifications`,
  `parts`, `purchaseorders`) still exist on the client and hold only deprecated aliases.

### Breaking
- `client.tickets.assign_ticket` could not be aliased: the new contract gives that name to a
  different operation. It used to call `POST /tickets/{TicketId}/sla` and now calls
  `POST /api/v1.0/tickets/{ticketId}/assign`. The previous behavior is at
  `client.tickets.assign_ticket_sla`. `incident_py_q.legacy_alias_conflicts()` reports this
  at runtime. This is the only legacy name that changed meaning.

### Added
- `incident_py_q.schema.openapi` converts the published OpenAPI 3.0 contract into the
  SDK's internal Swagger-shaped document.
- `scripts/reconcile_silver_inventory.py` prunes bundled Silver routes that the Golden
  contract now documents, without needing HAR captures.
- `scripts/build_legacy_compat.py` rebuilds the migration bundle (legacy contract, Silver
  entries, and alias map) from the pre-migration commit.
- `incident_py_q.compat` with `legacy_alias_conflicts()`, exported at package level.
- `docs/migration-openapi.md` with the full old-to-new method mapping.
- Narrow contract normalization for live-optional `AssetCustomFieldValue.AssetId`.

### Removed
- Bundled Stoplight controller specs and the APIHub Postman collection, along with the
  Postman contract tests and the Silver-only asset-serial response override that the
  documented contract and normalization now cover.

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
