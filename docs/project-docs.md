# Project Docs

Core repository documents:

- `README.md`: user-facing overview and quickstart.
- `CONTRIBUTING.md`: local setup, validation gates, and schema sync workflow.
- `SECURITY.md`: private reporting and secret handling expectations.
- `IMPLEMENTATION_PLAN.md`: committed execution plan for this repository.

These files are maintained in the repository root and versioned with code changes.

## Promotion automation

Promotion PRs (`dev` → `staging` → `main`) and the release-prep version bump are
authored with the built-in `github.token`. There is **no stored credential** — no
personal access token and no GitHub App. An earlier `PROMOTION_PR_TOKEN` PAT
expired silently and broke promotion with `HTTP 401: Bad credentials`; nothing
can expire this way now.

### How the required checks are satisfied

`staging` and `main` require the `unit` and `integration` checks. GitHub
deliberately does not fire `pull_request` workflows for pull requests opened with
`github.token`, to prevent recursive runs, so a promotion PR receives no
`pull_request` check runs at all.

That is fine, because **status checks are scoped to the head commit, not to the
event that produced them**. Both workflows therefore also run on pushes to the
branches that become promotion PR heads:

| Promotion PR | Head branch | Checks come from |
| --- | --- | --- |
| `dev` → `staging` | `dev` | push to `dev` |
| `staging` → `main` | `promote/staging-to-main` | push to that branch (including the version bump) |

### Where the promotion branch is prepared

`promote/staging-to-main` must carry `main` plus `staging` plus the version bump
before `release-prep` will pass. That preparation happens in `promotion.yml`, in
the same `workflow_run` job that opens the PR.

It used to happen in `prepare-release-promotion` (`release-prep.yml`), which is
`pull_request_target`-triggered. A promotion PR opened or updated with
`github.token` does not produce `pull_request_target` runs, so that workflow only
ever fired when a **human** touched the PR. An unattended promotion therefore
pushed the bare `staging` tip, and `release-prep` failed with
`Expected prepared pyproject version X, found Y` while the PR sat `BEHIND` main.

`prepare-release-promotion` is still in place for the case it does cover: a
person changing the `semver:` label after the PR exists, which changes the target
version and needs the branch rebuilt. Both paths produce the same commit shape,
and `release-prep` verifies the result either way.

### Live integration tests are unchanged

`integration.yml` runs live tests only on pushes to `staging` and `main`, on
manual dispatch, and on the weekly schedule. On `dev` and promotion-branch
pushes — exactly as on pull requests before — it records an `integration` check
without calling the tenant. This relocates where the check is produced; it does
not weaken the gate, because the `integration` check on a promotion PR was
already a no-op. Integration badges are published only from runs that actually
executed live tests.

### Consequences to keep in mind

- Adding a branch to the push triggers of `quality.yml` or `integration.yml`
  changes which commits carry required checks. Removing `dev` or
  `promote/staging-to-main` would silently strand promotion PRs with missing
  checks.
- `promotion.yml` is `workflow_run`-triggered and `release-prep.yml` is
  `pull_request_target`-triggered, so GitHub always runs the copy of those files
  on the **default branch**. Changes to them take effect only once merged to
  `main`.
