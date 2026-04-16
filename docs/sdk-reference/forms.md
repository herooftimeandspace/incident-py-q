# `forms` Namespace

Sync client access: `client.forms`

Async client access: `client.forms` with `await` on method calls.

## Methods

### `submit_form`

Operation ID: `Form_SubmitForm`

- Sync: `client.forms.submit_form(model=..., timeout=None)`
- Async: `await client.forms.submit_form(model=..., timeout=None)`
- Raw payload: `client.forms.submit_form.raw(model=..., timeout=None)`
- HTTP route: `POST /forms/submit`
- Source controller: `Forms`

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

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `model` | `Model` | `body` | `yes` | `FormSubmission` | `FormSubmission` | Form submission infomation / parameters |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
