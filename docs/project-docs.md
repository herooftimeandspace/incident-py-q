# Project Docs

Core repository documents:

- `README.md`: user-facing overview and quickstart.
- `CONTRIBUTING.md`: local setup, validation gates, and schema sync workflow.
- `SECURITY.md`: private reporting and secret handling expectations.
- `IMPLEMENTATION_PLAN.md`: committed execution plan for this repository.

These files are maintained in the repository root and versioned with code changes.

## Promotion automation credentials

Promotion PRs (`dev` → `staging` → `main`) and the release-prep version bump are
authored by a **GitHub App installation token**, minted per workflow run by
`actions/create-github-app-token`. This replaces the former
`PROMOTION_PR_TOKEN` personal access token, which expired silently and broke
promotion with `HTTP 401: Bad credentials`.

### Why not `github.token`?

`staging` and `main` require the `unit` and `integration` status checks. Work
pushed to `dev` already produces `unit` on the promotion PR's head commit, but
`integration` only runs on pull requests targeting `staging`/`main` — and GitHub
deliberately does not fire `pull_request` workflows for pull requests opened with
`github.token`, to prevent recursive runs. A promotion PR opened that way would
never receive `integration` and could never merge. An App installation token is a
distinct actor, so downstream validation runs normally.

The same constraint applies to release-prep: pushing the version bump with
`github.token` would not re-trigger the promotion PR's own checks.

### Required secrets

| Secret | Value |
| --- | --- |
| `PROMOTION_APP_ID` | The GitHub App's App ID |
| `PROMOTION_APP_PRIVATE_KEY` | A generated private key for that App (full PEM contents) |

### App setup

Create a GitHub App in the organization, install it on this repository, and grant
these **repository** permissions:

| Permission | Level | Needed for |
| --- | --- | --- |
| Metadata | Read-only | Required baseline |
| Contents | Read and write | Pushing the `promote/staging-to-main` ref and the version bump |
| Pull requests | Read and write | Creating, editing, and labelling promotion PRs |
| Workflows | Read and write | Promoting commits that modify files under `.github/workflows/` |

Installation tokens are short-lived and minted fresh on each run, so there is no
credential to rotate and no silent expiry. If either secret is missing, the
workflows fail early with an explicit message rather than a `401` deep in a run.
