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
  On the auto-generated promotion PR, `unit` is a proxy check that confirms the already-green
  `dev` push validation for the same head SHA instead of rerunning the full unit workflow.
- GitHub Actions opens a promotion PR from `staging` to `main` after green pushes on `staging`.
- Merge `staging -> main` only after `unit`, `integration`, `docs-build`, and `release-prep` pass.
- `dev` allows the repository owner to bypass the PR gate when necessary. `staging` and `main` do not.

## Quality Gates

Run all required checks before opening a pull request:

```bash
python scripts/run_local_ci.py --target dev
```

Use the branch target that matches the branch you are promoting into:

```bash
python scripts/run_local_ci.py --target dev
python scripts/run_local_ci.py --target staging
python scripts/run_local_ci.py --target main
```

- `dev` mirrors the `unit` workflow gate.
- `staging` mirrors `unit` plus `integration`.
- `main` mirrors `unit`, `integration`, and `docs-build`.
- `staging` and `main` require live integration credentials locally, just like protected-branch CI.

## Release Labels and Mainline Releases

- Every `staging -> main` promotion PR must carry exactly one of:
  - `semver:patch`
  - `semver:minor`
  - `semver:major`
- The `prepare-release-promotion` workflow rewrites the promotion branch with the release version bump before merge.
- The required `release-prep` check is non-mutating and verifies that the final promotion PR head is already prepared.
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
