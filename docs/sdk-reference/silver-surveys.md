# `silver.surveys` Namespace

Sync client access: `client.silver.surveys`

Async client access: `client.silver.surveys` with `await` on method calls.

These methods are Silver because Stoplight does not publish Golden contracts for them. They remain separate so undocumented behavior never overrides the documented SDK surface.

## Methods

### `get_responses_ticket`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.surveys.get_responses_ticket(ticket_id=..., timeout=None)`
- Async: `await client.silver.surveys.get_responses_ticket(ticket_id=..., timeout=None)`
- Raw payload: `client.silver.surveys.get_responses_ticket.raw(ticket_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/surveys/responses/ticket/{ticket_id}`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.surveys`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `ticket_id` | `ticket_id` | `path` | `yes` | `str` | Path parameter inferred from HAR observations. This route remains on the Silver surface because Stoplight does not publish a Golden contract for it. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---
