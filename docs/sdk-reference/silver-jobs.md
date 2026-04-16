# `silver.jobs` Namespace

Sync client access: `client.silver.jobs`

Async client access: `client.silver.jobs` with `await` on method calls.

These methods are Silver because Stoplight does not publish Golden contracts for them. They remain separate so undocumented behavior never overrides the documented SDK surface.

## Methods

### `get_job`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.jobs.get_job(job_id=..., timeout=None)`
- Async: `await client.silver.jobs.get_job(job_id=..., timeout=None)`
- Raw payload: `client.silver.jobs.get_job.raw(job_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/jobs/{job_id}`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.jobs`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `job_id` | `job_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---
