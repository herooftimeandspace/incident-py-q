# `silver.s` Namespace

Sync client access: `client.silver.s`

Async client access: `client.silver.s` with `await` on method calls.

These methods are Silver because Stoplight does not publish direct Golden contracts for them, or because the SDK intentionally wraps a narrower Silver workflow around existing Golden operations. They remain separate so undocumented or convenience behavior never overrides the documented SDK surface.

## Methods

### `get_opensans_v44_memsyags126mizpba_uvwbx2vvnxbbobj2ovzyoosr4dvjwugsjz0b4gaviuwaeqbja_woff2`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.s.get_opensans_v44_memsyags126mizpba_uvwbx2vvnxbbobj2ovzyoosr4dvjwugsjz0b4gaviuwaeqbja_woff2(timeout=None)`
- Async: `await client.silver.s.get_opensans_v44_memsyags126mizpba_uvwbx2vvnxbbobj2ovzyoosr4dvjwugsjz0b4gaviuwaeqbja_woff2(timeout=None)`
- Raw payload: `client.silver.s.get_opensans_v44_memsyags126mizpba_uvwbx2vvnxbbobj2ovzyoosr4dvjwugsjz0b4gaviuwaeqbja_woff2.raw(timeout=None)`
- HTTP route: `GET /s/opensans/v44/memSYaGs126MiZpBA-UvWbX2vVnXBbObj2OVZyOOSr4dVJWUgsjZ0B4gaVIUwaEQbjA.woff2`
- Observed in: `demo.incidentiq.com.har`

HAR-derived undocumented GET route for `client.silver.s`.

This method is intentionally kept on the Silver surface because bundled Stoplight controller contracts do not define this route. Golden Stoplight operations remain the preferred contract source whenever they exist, so Silver only supplements gaps observed in tenant HAR traffic.

#### Parameters

This Silver route does not define inferred parameters.

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---
