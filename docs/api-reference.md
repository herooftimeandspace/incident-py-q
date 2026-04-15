# API Reference

Static package API pages are generated with `pdoc`.

Runtime-generated namespace methods such as `client.tickets.get_ticket(...)` are
documented separately under the generated SDK reference pages.

Build locally:

```bash
python scripts/generate_api_docs.py
python scripts/generate_sdk_reference.py
```

Then open:
- [`incident_py_q` module](api/incident_py_q.html)
- [SDK reference index](sdk-reference/index.md)
