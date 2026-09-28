# `silver.forms` Namespace

Sync client access: `client.silver.forms`

Async client access: `client.silver.forms` with `await` on method calls.

These methods are Silver because the published contract does not document them directly, or because the SDK intentionally wraps a narrower Silver workflow around existing Golden operations. They remain separate so undocumented or convenience behavior never overrides the documented SDK surface.

## Methods

### `submit_form`

Provenance: Silver (HAR-derived undocumented route)

- Sync: `client.silver.forms.submit_form(json_body=..., timeout=None)`
- Async: `await client.silver.forms.submit_form(json_body=..., timeout=None)`
- Raw payload: `client.silver.forms.submit_form.raw(json_body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/forms/submit`
- Observed in: `migrated_from_golden_stoplight`

Submit new record to a form

#### Supports form submissions to Incident IQ using pre-configured forms that trigger actions upon submission
#### Sample request:
```
POST /api/v1.0/forms/submit
{
  "FormKey": "test-form-1",
  "SiteId": "ac6cece8-e4f4-e511-a789-005056bb000e",
  "Data": [ {
    "CustomFieldTypeId": "ac6cece8-e4f4-e511-a789-005056bb000e",
    "Value": "Test form submission",
  } ]
}
```

Migrated from the previous Golden SDK. The published Golden OpenAPI contract no longer documents this route, so it moved to the Silver surface to preserve access. Previously `client.forms.submit_form` (operationId `Form_SubmitForm`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- | --- |
| `json_body` | `Model` | `body` | `yes` | `dict[str, Any] | list[Any]` | Form submission infomation / parameters |

#### Returns

- Typed call return: `dict[str, Any] | list[Any] | None`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload only; this Silver route has no Golden schema contract.

---
