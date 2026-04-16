# API Reference

Static package API pages are generated with `pdoc`.

Runtime-generated namespace methods such as `client.tickets.get_ticket(...)` are
documented separately under the generated SDK reference pages.

Golden Stoplight methods are documented under the generated Golden namespace pages.
Silver HAR-derived methods are documented under the generated [`silver` overview](sdk-reference/silver.md).
The legacy app alias under `client.apps.*` is documented on the generated
[`apps` Silver namespace page](sdk-reference/apps.md).

Build locally:

```bash
python scripts/generate_api_docs.py
python scripts/generate_sdk_reference.py
```

Then open:
- [`incident_py_q` module](api/incident_py_q.html)
- [SDK reference index](sdk-reference/index.md)
- [Silver overview](sdk-reference/silver.md)
