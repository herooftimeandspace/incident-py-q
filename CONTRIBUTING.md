# Contributing

## Development Setup

1. Use Python `3.14+`.
2. Create and activate a virtual environment.
3. Install project + dev dependencies:

```bash
python -m pip install -e '.[dev]'
```

## Branch Promotion Flow

- Branch feature, bugfix, and chore work from `dev`.
- Merge reviewed work into `dev` after the `unit` check passes.
- GitHub Actions opens a promotion PR from `dev` to `staging` after green pushes on `dev`.
- Merge `dev -> staging` only after `unit` and `integration` both pass.
- GitHub Actions opens a promotion PR from `staging` to `main` after green pushes on `staging`.
- Merge `staging -> main` only after `unit`, `integration`, `docs-build`, and `release-prep` pass.
- `dev` allows the repository owner to bypass the PR gate when necessary. `staging` and `main` do not.

## Quality Gates

Run all required checks before opening a pull request:

```bash
ruff check .
mypy src tests scripts
pytest --cov=incident_py_q --cov-report=xml -m "not integration"
python -m pip wheel --no-deps --no-build-isolation --wheel-dir dist .
python scripts/build_docs.py
```

Integration tests are optional locally and require live tenant credentials:

```bash
pytest -m integration
```

## Release Labels and Mainline Releases

- Every `staging -> main` promotion PR must carry exactly one of:
  - `semver:patch`
  - `semver:minor`
  - `semver:major`
- The `release-prep` workflow applies the version bump on the promotion branch before the PR is merged into `main`.
- After the PR merges into `main`, GitHub Actions:
  - tags the release as `vX.Y.Z`
  - creates a GitHub Release
  - attaches the wheel, sdist, and versioned SDK zip asset
- PyPI publication is intentionally out of scope for this repository flow today.

## Schema Sync Workflow

The runtime validator and contract tests use bundled schema artifacts only.  
To refresh bundled upstream contracts:

```bash
python scripts/sync_schemas.py
python scripts/update_sdk_inventory.py
pytest --cov=incident_py_q --cov-report=xml -m "not integration"
```

If schema updates change generated SDK method inventory, the golden snapshot file at
`tests/contract/golden_sdk_inventory.json` must be committed in the same change.

## Public API Stability

The public SDK surface (`Client`, `AsyncClient`, generated namespaces/method names, and
request signatures) is semver-governed:

- Backward-compatible additive changes: minor version bump.
- Breaking method/namespace/signature changes: major version bump.
- Bug fixes that preserve public surface: patch version bump.
