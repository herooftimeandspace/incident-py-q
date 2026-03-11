# Contributing

## Development Setup

1. Use Python `3.14+`.
2. Create and activate a virtual environment.
3. Install project + dev dependencies:

```bash
python -m pip install -e '.[dev]'
```

## Quality Gates

Run all required checks before opening a pull request:

```bash
ruff check .
mypy src tests scripts
pytest -m "not integration"
python -m pip wheel --no-deps --wheel-dir dist .
python scripts/build_docs.py
```

Integration tests are optional locally and require live tenant credentials:

```bash
pytest -m integration
```

## Schema Sync Workflow

The runtime validator and contract tests use bundled schema artifacts only.  
To refresh bundled upstream contracts:

```bash
python scripts/sync_schemas.py
python scripts/update_sdk_inventory.py
pytest -m "not integration"
```

If schema updates change generated SDK method inventory, the golden snapshot file at
`tests/contract/golden_sdk_inventory.json` must be committed in the same change.

## Public API Stability

The public SDK surface (`Client`, `AsyncClient`, generated namespaces/method names, and
request signatures) is semver-governed:

- Backward-compatible additive changes: minor version bump.
- Breaking method/namespace/signature changes: major version bump.
- Bug fixes that preserve public surface: patch version bump.
