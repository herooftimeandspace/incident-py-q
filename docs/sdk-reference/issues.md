# `issues` Golden Namespace

Sync client access: `client.issues`

Async client access: `client.issues` with `await` on method calls.

These methods are Golden because they come from bundled Stoplight controller contracts.

## Aliases

| Alias | Canonical Method | Route |
| --- | --- | --- |
| `delete` | `delete_issue` | `DELETE /issues/{IssueId}` |
| `get` | `get_issue` | `GET /issues/{IssueId}` |
| `update` | `update_issue` | `POST /issues/{IssueId}` |

## Methods

### `delete_issue`

Provenance: Golden Stoplight contract

Operation ID: `Issue_DeleteIssue`

- Sync: `client.issues.delete_issue(issue_id=..., timeout=None)`
- Async: `await client.issues.delete_issue(issue_id=..., timeout=None)`
- Raw payload: `client.issues.delete_issue.raw(issue_id=..., timeout=None)`
- HTTP route: `DELETE /issues/{IssueId}`
- Source controller: `Issues`
- Aliases: `delete`

No contract summary provided.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `issue_id` | `IssueId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_issue_type`

Provenance: Golden Stoplight contract

Operation ID: `Issue_DeleteIssueType`

- Sync: `client.issues.delete_issue_type(issue_type_id=..., timeout=None)`
- Async: `await client.issues.delete_issue_type(issue_type_id=..., timeout=None)`
- Raw payload: `client.issues.delete_issue_type.raw(issue_type_id=..., timeout=None)`
- HTTP route: `DELETE /issues/types/{IssueTypeId}`
- Source controller: `Issues`

Delete Issue Type

#### Delete a specific Issue Type
#### Sample request:
```
DELETE /api/v1.0/issues/types/{IssueTypeId:guid}
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `issue_type_id` | `IssueTypeId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_available_issues`

Provenance: Golden Stoplight contract

Operation ID: `Issue_GetAvailableIssues`

- Sync: `client.issues.get_available_issues(timeout=None)`
- Async: `await client.issues.get_available_issues(timeout=None)`
- Raw payload: `client.issues.get_available_issues.raw(timeout=None)`
- HTTP route: `GET /issues/site`
- Source controller: `Issues`

Get Available Issues

#### Retrieve all available issues for the given Site
#### Sample request:
```
GET /api/v1.0/issues/site
```

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `ListGetResponseOfIssueRoles`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfIssueRoles`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_issue`

Provenance: Golden Stoplight contract

Operation ID: `Issue_GetIssue`

- Sync: `client.issues.get_issue(issue_id=..., timeout=None)`
- Async: `await client.issues.get_issue(issue_id=..., timeout=None)`
- Raw payload: `client.issues.get_issue.raw(issue_id=..., timeout=None)`
- HTTP route: `GET /issues/{IssueId}`
- Source controller: `Issues`
- Aliases: `get`

Get Issue 

#### Retrieve a specific Issue via Issue ID
#### Sample request:
```
GET /api/v1.0/issues/53bf1b92-a533-4a0e-8894-059f05b38f41
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `issue_id` | `IssueId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ItemGetResponseOfIssue`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemGetResponseOfIssue`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_issue_type`

Provenance: Golden Stoplight contract

Operation ID: `Issue_GetIssueType`

- Sync: `client.issues.get_issue_type(issue_type_id=..., timeout=None)`
- Async: `await client.issues.get_issue_type(issue_type_id=..., timeout=None)`
- Raw payload: `client.issues.get_issue_type.raw(issue_type_id=..., timeout=None)`
- HTTP route: `GET /issues/types/{IssueTypeId}`
- Source controller: `Issues`

Get Issue Type

#### Retrieve a specific Issue Type via Issue Type Id
#### Sample request:
```
GET /api/v1.0/issues/types/fb08be5e-0876-4204-acf1-8f6aad44797c
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `issue_type_id` | `IssueTypeId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ItemGetResponseOfIssueType`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemGetResponseOfIssueType`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_issue_types`

Provenance: Golden Stoplight contract

Operation ID: `Issue_GetIssueTypes`

- Sync: `client.issues.get_issue_types(request=..., timeout=None)`
- Async: `await client.issues.get_issue_types(request=..., timeout=None)`
- Raw payload: `client.issues.get_issue_types.raw(request=..., timeout=None)`
- HTTP route: `POST /issues/types`
- Source controller: `Issues`

Get Issue Types

#### Retrieves a list of issue types that can then be used to retrieve a specific custom field via _GetIssueType_ via ID
#### Sample request:
```
POST /api/v1.0/issues/types
```

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `request` | `request` | `body` | `yes` | `GetIssueTypesRequest` | `GetIssueTypesRequest` | - |

#### Returns

- Typed call return: `ListGetResponseOfIssueType`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfIssueType`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_issue_types_simple`

Provenance: Golden Stoplight contract

Operation ID: `Issue_GetIssueTypesSimple`

- Sync: `client.issues.get_issue_types_simple(apply_site_visibility=None, timeout=None)`
- Async: `await client.issues.get_issue_types_simple(apply_site_visibility=None, timeout=None)`
- Raw payload: `client.issues.get_issue_types_simple.raw(apply_site_visibility=None, timeout=None)`
- HTTP route: `GET /issues/types`
- Source controller: `Issues`

No contract summary provided.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `apply_site_visibility` | `ApplySiteVisibility` | `query` | `no` | `bool` | `-` | - |

#### Returns

- Typed call return: `ListGetResponseOfIssueType`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponseOfIssueType`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_issue`

Provenance: Golden Stoplight contract

Operation ID: `Issue_UpdateIssue`

- Sync: `client.issues.update_issue(issue_id=..., model=..., timeout=None)`
- Async: `await client.issues.update_issue(issue_id=..., model=..., timeout=None)`
- Raw payload: `client.issues.update_issue.raw(issue_id=..., model=..., timeout=None)`
- HTTP route: `POST /issues/{IssueId}`
- Source controller: `Issues`
- Aliases: `update`

No contract summary provided.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `issue_id` | `IssueId` | `path` | `yes` | `str` | `-` | - |
| `model` | `Model` | `body` | `yes` | `Issue` | `Issue` | - |

#### Returns

- Typed call return: `ItemUpdateResponseOfIssue`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemUpdateResponseOfIssue`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_issue_type`

Provenance: Golden Stoplight contract

Operation ID: `Issue_UpdateIssueType`

- Sync: `client.issues.update_issue_type(issue_type_id=..., model=..., timeout=None)`
- Async: `await client.issues.update_issue_type(issue_type_id=..., model=..., timeout=None)`
- Raw payload: `client.issues.update_issue_type.raw(issue_type_id=..., model=..., timeout=None)`
- HTTP route: `POST /issues/types/{IssueTypeId}`
- Source controller: `Issues`

No contract summary provided.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `issue_type_id` | `IssueTypeId` | `path` | `yes` | `str` | `-` | - |
| `model` | `Model` | `body` | `yes` | `IssueType` | `IssueType` | - |

#### Returns

- Typed call return: `ItemUpdateResponseOfIssueType`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemUpdateResponseOfIssueType`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
