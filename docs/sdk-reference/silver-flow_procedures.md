# `silver.flow_procedures` Namespace

Sync client access: `client.silver.flow_procedures`

Async client access: `client.silver.flow_procedures` with `await` on method calls.

These methods are Silver because Stoplight does not publish Golden contracts for them. They remain separate so undocumented behavior never overrides the documented SDK surface.

## Methods

### `post_available_cards`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.flow_procedures.post_available_cards(json_body=..., timeout=None)`
- Async: `await client.silver.flow_procedures.post_available_cards(json_body=..., timeout=None)`
- Raw payload: `client.silver.flow_procedures.post_available_cards.raw(json_body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/flow-procedures/available/cards`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented POST route for `client.silver.flow_procedures`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `json_body` | `json_body` | `body` | `yes` | `Mapping[str, Any]` | Request body observed in HAR traffic. The SDK uses a single `json_body` payload because the Silver route carries a complex undocumented schema. |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---
