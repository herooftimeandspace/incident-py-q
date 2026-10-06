# `issues` Golden Namespace

Sync client access: `client.issues`

Async client access: `client.issues` with `await` on method calls.

These methods are Golden because they come from the bundled Incident IQ OpenAPI contract.

## Methods

### `add_issue_to_models`

Provenance: Golden OpenAPI contract

Operation ID: `addIssueToModels`

- Sync: `client.issues.add_issue_to_models(body=None, timeout=None)`
- Async: `await client.issues.add_issue_to_models(body=None, timeout=None)`
- Raw payload: `client.issues.add_issue_to_models.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/issues/for/models/link/new`
- Source controller: `IncidentIQ API`

Add issues to models

Creates model-issue association records that control which issues appear for specific models. Use this to add new issue options to a model or to bulk attach an issue to several models.

**Prerequisites**
1. **IssueId** - Use [GET /api/v1.0/issues](#/Issues/listIssues) or [POST /api/v1.0/issues](#/Issues/searchIssues) and extract `Items[].IssueId`.
2. **ModelId** - Obtain from [POST /api/v1.0/assets/search](#/Assets/keywordSearchAssets) or [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById).

**Workflow Example**
1. Choose the issue to link and the target model IDs.
2. Build an array of `ModelIssue` entries with `IssueId`, `ModelId`, and optional `Scope`.
3. [POST /api/v1.0/issues/for/models/link/new](#/Model Issues/addIssueToModels) to create the associations.

**Minimal Required Fields**: IssueId and ModelId for each ModelIssue entry.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `ModelIssueArrayRequest` | `ModelIssueArrayRequest` | - |

#### Returns

- Typed call return: `ModelIssueListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ModelIssueListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_issue`

Provenance: Golden OpenAPI contract

Operation ID: `createIssue`

- Sync: `client.issues.create_issue(body=None, timeout=None)`
- Async: `await client.issues.create_issue(body=None, timeout=None)`
- Raw payload: `client.issues.create_issue.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/issues/new`
- Source controller: `IncidentIQ API`

Create issue

Creates a new issue definition used for ticket categorization (for example, "Broken Screen" or "Software Install"). Use this endpoint when adding new issue options to the catalog.

**Prerequisites**
1. **IssueTypeId** - Use [GET /api/v1.0/issues/types](#/Issue%20Types/listIssueTypes) or [POST /api/v1.0/issues/types](#/Issue%20Types/searchIssueTypes) and extract `Items[].IssueTypeId`.

**Workflow Example**
1. List issue types and choose the appropriate type.
2. Build `CreateIssueRequest` with `Name`, `IssueTypeId`, and any optional category metadata.
3. Create the issue: [POST /api/v1.0/issues/new](#/Issues/createIssue).

**Minimal Required Fields**: `Name`, `IssueTypeId`.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `CreateIssueRequest` | `CreateIssueRequest` | - |

#### Returns

- Typed call return: `CreateIssueResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CreateIssueResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_issue_type`

Provenance: Golden OpenAPI contract

Operation ID: `createIssueType`

- Sync: `client.issues.create_issue_type(body=None, timeout=None)`
- Async: `await client.issues.create_issue_type(body=None, timeout=None)`
- Raw payload: `client.issues.create_issue_type.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/issues/types/new`
- Source controller: `IncidentIQ API`

Create issue type

Creates a new issue type definition. Use this to add a new category of issues (for example, Hardware, Software, Facilities) that can be referenced by issues.

**Workflow Example**
1. Build an `IssueType` payload with `Name` and `Scope` (and optional `SiteId`/`ProductId`).
2. Create the type: [POST /api/v1.0/issues/types/new](#/Issue Types/createIssueType).
3. Use the returned `IssueTypeId` when creating issues via [POST /api/v1.0/issues/new](#/Issues/createIssue).

**Minimal Required Fields**: `Name`, `Scope`.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `IssueType` | `IssueType` | - |

#### Returns

- Typed call return: `CreateIssueTypeResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CreateIssueTypeResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_issue`

Provenance: Golden OpenAPI contract

Operation ID: `deleteIssue`

- Sync: `client.issues.delete_issue(issue_id=..., timeout=None)`
- Async: `await client.issues.delete_issue(issue_id=..., timeout=None)`
- Raw payload: `client.issues.delete_issue.raw(issue_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/issues/{issueId}`
- Source controller: `IncidentIQ API`

Delete issue

Deletes an issue definition by ID. Use this to retire options that should no longer appear during ticket creation.

**Prerequisites**
1. **issueId** - Use [GET /api/v1.0/issues](#/Issues/listIssues) or [POST /api/v1.0/issues](#/Issues/searchIssues) and extract `Items[].IssueId`.

**Workflow Example**
1. Identify the issue to retire.
2. Delete it: [DELETE /api/v1.0/issues/{issueId}](#/Issues/deleteIssue).

**Minimal Required Fields**: issueId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `issue_id` | `issueId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_issue_type`

Provenance: Golden OpenAPI contract

Operation ID: `deleteIssueType`

- Sync: `client.issues.delete_issue_type(issue_type_id=..., timeout=None)`
- Async: `await client.issues.delete_issue_type(issue_type_id=..., timeout=None)`
- Raw payload: `client.issues.delete_issue_type.raw(issue_type_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/issues/types/{issueTypeId}`
- Source controller: `IncidentIQ API`

Delete issue type

Deletes an issue type by ID. Use this to retire a type that should no longer be offered when creating issues.

**Prerequisites**
1. **issueTypeId** - Use [GET /api/v1.0/issues/types](#/Issue%20Types/listIssueTypes) or [POST /api/v1.0/issues/types](#/Issue%20Types/searchIssueTypes) and extract `Items[].IssueTypeId`.

**Workflow Example**
1. Identify the type to delete.
2. Delete it: [DELETE /api/v1.0/issues/types/{issueTypeId}](#/Issue Types/deleteIssueType).

**Minimal Required Fields**: issueTypeId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `issue_type_id` | `issueTypeId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_available_issues`

Provenance: Golden OpenAPI contract

Operation ID: `getAvailableIssues`

- Sync: `client.issues.get_available_issues(timeout=None)`
- Async: `await client.issues.get_available_issues(timeout=None)`
- Raw payload: `client.issues.get_available_issues.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/issues/site`
- Source controller: `IncidentIQ API`

Get available issues

Returns the list of issues available for the current site context. This is commonly used to populate issue dropdowns in ticket creation flows with site-specific visibility applied.

**Workflow Example**
1. Load issues: [GET /api/v1.0/issues/site](#/Issues/getAvailableIssues).
2. Use the returned list to populate the issue selector for the active site.
3. If you need full details for a specific issue, call [GET /api/v1.0/issues/{issueId}](#/Issues/getIssueById).

**Minimal Required Fields**: None.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `AvailableIssuesListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AvailableIssuesListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_issue_by_id`

Provenance: Golden OpenAPI contract

Operation ID: `getIssueById`

- Sync: `client.issues.get_issue_by_id(issue_id=..., timeout=None)`
- Async: `await client.issues.get_issue_by_id(issue_id=..., timeout=None)`
- Raw payload: `client.issues.get_issue_by_id.raw(issue_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/issues/{issueId}`
- Source controller: `IncidentIQ API`

Get issue by ID

Retrieves a single issue definition by ID, including its type, category metadata, and configuration flags. Use this to inspect or edit an issue before updating it.

**Prerequisites**
1. **issueId** - Use [GET /api/v1.0/issues](#/Issues/listIssues) or [POST /api/v1.0/issues](#/Issues/searchIssues) and extract `Items[].IssueId`.

**Workflow Example**
1. List issues and capture the target `IssueId`.
2. Fetch details: [GET /api/v1.0/issues/{issueId}](#/Issues/getIssueById).
3. (Optional) Update using [POST /api/v1.0/issues/{issueId}](#/Issues/updateIssue).

**Minimal Required Fields**: issueId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `issue_id` | `issueId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `IssueItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `IssueItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_issue_roles`

Provenance: Golden OpenAPI contract

Operation ID: `getIssueRoles`

- Sync: `client.issues.get_issue_roles(issue_id=..., timeout=None)`
- Async: `await client.issues.get_issue_roles(issue_id=..., timeout=None)`
- Raw payload: `client.issues.get_issue_roles.raw(issue_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/issues/{issueId}/roles`
- Source controller: `IncidentIQ API`

Get issue roles

Retrieves role configuration for a specific issue, including enabled/disabled role lists. Use this to understand which roles can see or use the issue option.

**Prerequisites**
1. **issueId** - Use [GET /api/v1.0/issues](#/Issues/listIssues) or [POST /api/v1.0/issues](#/Issues/searchIssues) and extract `Items[].IssueId`.

**Workflow Example**
1. Identify the issue to inspect.
2. Fetch roles: [GET /api/v1.0/issues/{issueId}/roles](#/Issues/getIssueRoles).
3. Use the response to drive role visibility settings or audits.

**Minimal Required Fields**: issueId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `issue_id` | `issueId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `IssueRolesItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `IssueRolesItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_issue_type_by_id`

Provenance: Golden OpenAPI contract

Operation ID: `getIssueTypeById`

- Sync: `client.issues.get_issue_type_by_id(issue_type_id=..., timeout=None)`
- Async: `await client.issues.get_issue_type_by_id(issue_type_id=..., timeout=None)`
- Raw payload: `client.issues.get_issue_type_by_id.raw(issue_type_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/issues/types/{issueTypeId}`
- Source controller: `IncidentIQ API`

Get issue type by ID

Retrieves a single issue type definition by ID, including scope and product metadata. Use this when inspecting or editing issue types.

**Prerequisites**
1. **issueTypeId** - Use [GET /api/v1.0/issues/types](#/Issue%20Types/listIssueTypes) or [POST /api/v1.0/issues/types](#/Issue%20Types/searchIssueTypes) and extract `Items[].IssueTypeId`.

**Workflow Example**
1. List issue types and capture the target `IssueTypeId`.
2. Retrieve details: [GET /api/v1.0/issues/types/{issueTypeId}](#/Issue Types/getIssueTypeById).

**Minimal Required Fields**: issueTypeId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `issue_type_id` | `issueTypeId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `IssueTypeItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `IssueTypeItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_issues_for_model`

Provenance: Golden OpenAPI contract

Operation ID: `getIssuesForModel`

- Sync: `client.issues.get_issues_for_model(model_id=..., apply_site_visibility=None, timeout=None)`
- Async: `await client.issues.get_issues_for_model(model_id=..., apply_site_visibility=None, timeout=None)`
- Raw payload: `client.issues.get_issues_for_model.raw(model_id=..., apply_site_visibility=None, timeout=None)`
- HTTP route: `GET /api/v1.0/issues/for/models/{modelId}`
- Source controller: `IncidentIQ API`

Get issues for model

Retrieves the issue catalog associated with a single asset model, optionally applying site visibility rules. Use this to populate issue pickers when a specific model is known or to audit which issues are allowed for that model.

**Prerequisites**
1. **modelId** - Obtain from [POST /api/v1.0/assets/search](#/Assets/keywordSearchAssets) or [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById) and extract `Items[].ModelId` or `Item.ModelId`.

**Workflow Example**
1. Locate the model from an asset search or asset detail.
2. [GET /api/v1.0/issues/for/models/{modelId}](#/Model Issues/getIssuesForModel) (set `ApplySiteVisibility=false` to include all).
3. Use the returned issues to drive UI selections or validation.

**Minimal Required Fields**: modelId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `model_id` | `modelId` | `path` | `yes` | `str` | `-` | - |
| `apply_site_visibility` | `ApplySiteVisibility` | `query` | `no` | `bool` | `-` | - |

#### Returns

- Typed call return: `IssueListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `IssueListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_issues_for_model_categories`

Provenance: Golden OpenAPI contract

Operation ID: `getIssuesForModelCategories`

- Sync: `client.issues.get_issues_for_model_categories(apply_site_visibility=None, body=None, timeout=None)`
- Async: `await client.issues.get_issues_for_model_categories(apply_site_visibility=None, body=None, timeout=None)`
- Raw payload: `client.issues.get_issues_for_model_categories.raw(apply_site_visibility=None, body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/issues/for/model-categories`
- Source controller: `IncidentIQ API`

Get issues for model categories

Retrieves issues for multiple model categories in one request, useful for admin bulk audits or when building cached issue lists per category.

**Prerequisites**
1. **CategoryIds** - Use [GET /api/v1.0/categories/of/models](#/Categories/listModelCategories) and collect `Items[].CategoryId` values.

**Workflow Example**
1. List model categories and choose the ones to evaluate.
2. [POST /api/v1.0/issues/for/model-categories](#/Model Issues/getIssuesForModelCategories) with a `UuidList` of CategoryIds.
3. Use the response to map category IDs to issue lists.

**Minimal Required Fields**: CategoryIds (request body).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `apply_site_visibility` | `ApplySiteVisibility` | `query` | `no` | `bool` | `-` | - |
| `body` | `body` | `body` | `no` | `UuidList` | `UuidList` | - |

#### Returns

- Typed call return: `IssueListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `IssueListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_issues_for_model_category`

Provenance: Golden OpenAPI contract

Operation ID: `getIssuesForModelCategory`

- Sync: `client.issues.get_issues_for_model_category(category_id=..., apply_site_visibility=None, timeout=None)`
- Async: `await client.issues.get_issues_for_model_category(category_id=..., apply_site_visibility=None, timeout=None)`
- Raw payload: `client.issues.get_issues_for_model_category.raw(category_id=..., apply_site_visibility=None, timeout=None)`
- HTTP route: `GET /api/v1.0/issues/for/model-categories/{categoryId}`
- Source controller: `IncidentIQ API`

Get issues for model category

Retrieves the issues configured for a single model category. Use this when a model inherits its issue list from its category and you need to understand the base set before overrides.

**Prerequisites**
1. **categoryId** - Use [GET /api/v1.0/categories/of/models](#/Categories/listModelCategories) and extract `Items[].CategoryId`.

**Workflow Example**
1. List model categories and select the category of interest.
2. [GET /api/v1.0/issues/for/model-categories/{categoryId}](#/Model Issues/getIssuesForModelCategory) to load the issue list.
3. Compare the results with model-specific overrides from [GET /api/v1.0/issues/for/models/{modelId}](#/Model%20Issues/getIssuesForModel).

**Minimal Required Fields**: categoryId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `category_id` | `categoryId` | `path` | `yes` | `str` | `-` | - |
| `apply_site_visibility` | `ApplySiteVisibility` | `query` | `no` | `bool` | `-` | - |

#### Returns

- Typed call return: `IssueListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `IssueListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_issues_for_models`

Provenance: Golden OpenAPI contract

Operation ID: `getIssuesForModels`

- Sync: `client.issues.get_issues_for_models(apply_site_visibility=None, body=None, timeout=None)`
- Async: `await client.issues.get_issues_for_models(apply_site_visibility=None, body=None, timeout=None)`
- Raw payload: `client.issues.get_issues_for_models.raw(apply_site_visibility=None, body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/issues/for/models`
- Source controller: `IncidentIQ API`

Get issues for models

Retrieves issues for multiple models in a single call, useful when rendering issue options for bulk selections or validating multiple models at once.

**Prerequisites**
1. **ModelIds** - Collect model IDs from [POST /api/v1.0/assets/search](#/Assets/keywordSearchAssets) or [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById) and use `Items[].ModelId` values.

**Workflow Example**
1. Search assets and gather a list of model IDs.
2. [POST /api/v1.0/issues/for/models](#/Model Issues/getIssuesForModels) with a `UuidList` payload of ModelIds.
3. Review the response to map each model to its available issues.

**Minimal Required Fields**: ModelIds (request body).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `apply_site_visibility` | `ApplySiteVisibility` | `query` | `no` | `bool` | `-` | - |
| `body` | `body` | `body` | `no` | `UuidList` | `UuidList` | - |

#### Returns

- Typed call return: `IssueListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `IssueListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_models_for_issue`

Provenance: Golden OpenAPI contract

Operation ID: `getModelsForIssue`

- Sync: `client.issues.get_models_for_issue(issue_id=..., timeout=None)`
- Async: `await client.issues.get_models_for_issue(issue_id=..., timeout=None)`
- Raw payload: `client.issues.get_models_for_issue.raw(issue_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/issues/models/{issueId}`
- Source controller: `IncidentIQ API`

Get models for issue

Retrieves all asset models associated with a specific issue. Use this to see which device models expose a given issue during ticket creation.

**Prerequisites**
1. **issueId** - Use [GET /api/v1.0/issues](#/Issues/listIssues) or [POST /api/v1.0/issues](#/Issues/searchIssues) and extract `Items[].IssueId`.

**Workflow Example**
1. Identify the issue you want to inspect.
2. Fetch models: [GET /api/v1.0/issues/models/{issueId}](#/Issues/getModelsForIssue).
3. Use the returned model list to display compatibility or to drive model-specific filters.

**Minimal Required Fields**: issueId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `issue_id` | `issueId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `IssueModelsListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `IssueModelsListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `link_issue_to_app`

Provenance: Golden OpenAPI contract

Operation ID: `linkIssueToApp`

- Sync: `client.issues.link_issue_to_app(issue_id=..., app_id=..., timeout=None)`
- Async: `await client.issues.link_issue_to_app(issue_id=..., app_id=..., timeout=None)`
- Raw payload: `client.issues.link_issue_to_app.raw(issue_id=..., app_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/issues/{issueId}/link/app/{appId}`
- Source controller: `IncidentIQ API`

Link issue to app

Links an issue to an external app so the app can surface or manage the issue in its own workflows. Use this when integrating issue catalogs with third-party applications.

**Prerequisites**
1. **issueId** - Use [GET /api/v1.0/issues](#/Issues/listIssues) or [POST /api/v1.0/issues](#/Issues/searchIssues) and extract `Items[].IssueId`.
2. **appId** - Use the app's registration identifier from your integration settings.

**Workflow Example**
1. Identify the issue to link.
2. Link the app: [POST /api/v1.0/issues/{issueId}/link/app/{appId}](#/Issues/linkIssueToApp).
3. Verify app-specific behavior in the integration UI.

**Minimal Required Fields**: issueId and appId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `issue_id` | `issueId` | `path` | `yes` | `str` | `-` | - |
| `app_id` | `appId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `link_model_issue_to_app`

Provenance: Golden OpenAPI contract

Operation ID: `linkModelIssueToApp`

- Sync: `client.issues.link_model_issue_to_app(model_issue_id=..., app_id=..., timeout=None)`
- Async: `await client.issues.link_model_issue_to_app(model_issue_id=..., app_id=..., timeout=None)`
- Raw payload: `client.issues.link_model_issue_to_app.raw(model_issue_id=..., app_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/issues/for/models/{modelIssueId}/link/app/{appId}`
- Source controller: `IncidentIQ API`

Link model issue to app

Links a model-issue association to an external app so the app can surface or manage the model-specific issue. Use this when an integration needs visibility into model-level issue mappings.

**Prerequisites**
1. **modelIssueId** - Use [POST /api/v1.0/issues/for/models/link](#/Model%20Issues/searchModelIssues) and extract `Items[].ModelIssueId`.
2. **appId** - Use the app's registration identifier from your integration settings.

**Workflow Example**
1. Identify the model-issue association to link.
2. [POST /api/v1.0/issues/for/models/{modelIssueId}/link/app/{appId}](#/Model Issues/linkModelIssueToApp).
3. Verify the app now sees the model issue in its catalog.

**Minimal Required Fields**: modelIssueId and appId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `model_issue_id` | `modelIssueId` | `path` | `yes` | `str` | `-` | - |
| `app_id` | `appId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_global_issue_types`

Provenance: Golden OpenAPI contract

Operation ID: `listGlobalIssueTypes`

- Sync: `client.issues.list_global_issue_types(timeout=None)`
- Async: `await client.issues.list_global_issue_types(timeout=None)`
- Raw payload: `client.issues.list_global_issue_types.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/issues/types/global`
- Source controller: `IncidentIQ API`

List global issue types

Returns only global issue types, excluding site-specific or personal scopes. Use this to build cross-site catalogs or default issue type lists.

**Workflow Example**
1. Retrieve global types: [GET /api/v1.0/issues/types/global](#/Issue Types/listGlobalIssueTypes).
2. Use the returned `IssueTypeId` values as defaults when creating issues.

**Minimal Required Fields**: None.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `IssueTypeListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `IssueTypeListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_issue_types`

Provenance: Golden OpenAPI contract

Operation ID: `listIssueTypes`

- Sync: `client.issues.list_issue_types(apply_site_visibility=None, timeout=None)`
- Async: `await client.issues.list_issue_types(apply_site_visibility=None, timeout=None)`
- Raw payload: `client.issues.list_issue_types.raw(apply_site_visibility=None, timeout=None)`
- HTTP route: `GET /api/v1.0/issues/types`
- Source controller: `IncidentIQ API`

List issue types

Retrieves the list of issue types, optionally filtered by site visibility. Use this endpoint to populate issue type pickers in admin tools or to validate issue type IDs used by issue creation.

**Workflow Example**
1. List issue types: [GET /api/v1.0/issues/types](#/Issue Types/listIssueTypes) (set `ApplySiteVisibility=false` to include all).
2. Select the appropriate type and store `IssueTypeId`.
3. Use the selected type when creating issues via [POST /api/v1.0/issues/new](#/Issues/createIssue).

**Minimal Required Fields**: None. Optional: `ApplySiteVisibility` query parameter.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `apply_site_visibility` | `ApplySiteVisibility` | `query` | `no` | `bool` | `-` | Whether to apply site visibility filters (default: true) |

#### Returns

- Typed call return: `IssueTypeListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `IssueTypeListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_issues`

Provenance: Golden OpenAPI contract

Operation ID: `listIssues`

- Sync: `client.issues.list_issues(apply_site_visibility=None, timeout=None)`
- Async: `await client.issues.list_issues(apply_site_visibility=None, timeout=None)`
- Raw payload: `client.issues.list_issues.raw(apply_site_visibility=None, timeout=None)`
- HTTP route: `GET /api/v1.0/issues`
- Source controller: `IncidentIQ API`

List issues

Retrieves a list of issue definitions. Issues represent problems or topics that can be associated with tickets (e.g., 'Broken Screen', 'Software Installation Request').

**Use Cases**
- Populate dropdown menus for issue selection during ticket creation
- Display available issues for a specific site or product
- Build issue management interfaces

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `apply_site_visibility` | `ApplySiteVisibility` | `query` | `no` | `bool` | `-` | When true, filters results to only include issues visible at the current site. When false, returns all issues regardless of site visibility settings. |

#### Returns

- Typed call return: `IssueListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `IssueListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `remove_issue_from_model`

Provenance: Golden OpenAPI contract

Operation ID: `removeIssueFromModel`

- Sync: `client.issues.remove_issue_from_model(model_issue_id=..., timeout=None)`
- Async: `await client.issues.remove_issue_from_model(model_issue_id=..., timeout=None)`
- Raw payload: `client.issues.remove_issue_from_model.raw(model_issue_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/issues/for/models/link/{modelIssueId}`
- Source controller: `IncidentIQ API`

Remove issue from model

Removes a single model-issue association by its identifier. Use this when you need to detach one issue from one model without affecting other associations.

**Prerequisites**
1. **modelIssueId** - Use [POST /api/v1.0/issues/for/models/link](#/Model%20Issues/searchModelIssues) and extract `Items[].ModelIssueId`.

**Workflow Example**
1. Search for the model-issue link you want to remove.
2. [DELETE /api/v1.0/issues/for/models/link/{modelIssueId}](#/Model Issues/removeIssueFromModel).
3. Re-query model issues to confirm the link is gone.

**Minimal Required Fields**: modelIssueId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `model_issue_id` | `modelIssueId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `remove_issues_from_models`

Provenance: Golden OpenAPI contract

Operation ID: `removeIssuesFromModels`

- Sync: `client.issues.remove_issues_from_models(body=None, timeout=None)`
- Async: `await client.issues.remove_issues_from_models(body=None, timeout=None)`
- Raw payload: `client.issues.remove_issues_from_models.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/issues/for/models/link/remove`
- Source controller: `IncidentIQ API`

Remove issues from models (bulk)

Bulk removes model-issue associations using a list of ModelIssue entries. Use this to clean up many links at once, such as when retiring an issue or deprecating a model.

**Prerequisites**
1. **ModelIssue entries** - Use [POST /api/v1.0/issues/for/models/link](#/Model%20Issues/searchModelIssues) to retrieve the current ModelIssue objects to remove.

**Workflow Example**
1. Search for the links to remove and collect their ModelIssue data.
2. [POST /api/v1.0/issues/for/models/link/remove](#/Model Issues/removeIssuesFromModels) with the array of ModelIssue entries.
3. Re-run the search to confirm the links are removed.

**Minimal Required Fields**: ModelIssueId for each entry.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `ModelIssueArrayRequest` | `ModelIssueArrayRequest` | - |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `save_issue_options_for_site`

Provenance: Golden OpenAPI contract

Operation ID: `saveIssueOptionsForSite`

- Sync: `client.issues.save_issue_options_for_site(issue_id=..., apply_to_all_products=None, body=None, timeout=None)`
- Async: `await client.issues.save_issue_options_for_site(issue_id=..., apply_to_all_products=None, body=None, timeout=None)`
- Raw payload: `client.issues.save_issue_options_for_site.raw(issue_id=..., apply_to_all_products=None, body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/issues/{issueId}/site`
- Source controller: `IncidentIQ API`

Save issue options for site

Updates site-specific options for an issue, such as role visibility or other per-site settings. Use this when configuring which roles can see or select an issue at a specific site.

**Prerequisites**
1. **issueId** - Use [GET /api/v1.0/issues](#/Issues/listIssues) or [POST /api/v1.0/issues](#/Issues/searchIssues) and extract `Items[].IssueId`.

**Workflow Example**
1. Review current role settings: [GET /api/v1.0/issues/{issueId}/roles](#/Issues/getIssueRoles).
2. Build the `EntitySiteOption` array for the desired site settings.
3. Save options: [POST /api/v1.0/issues/{issueId}/site](#/Issues/saveIssueOptionsForSite) (set `applyToAllProducts=true` if needed).

**Minimal Required Fields**: issueId (path) plus a body array of site options.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `issue_id` | `issueId` | `path` | `yes` | `str` | `-` | - |
| `apply_to_all_products` | `applyToAllProducts` | `query` | `no` | `bool` | `-` | - |
| `body` | `body` | `body` | `no` | `SaveIssueOptionsForSiteIssuesByIssueIdSiteRequest` | `SaveIssueOptionsForSiteIssuesByIssueIdSiteRequest` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `search_issue_types`

Provenance: Golden OpenAPI contract

Operation ID: `searchIssueTypes`

- Sync: `client.issues.search_issue_types(body=None, timeout=None)`
- Async: `await client.issues.search_issue_types(body=None, timeout=None)`
- Raw payload: `client.issues.search_issue_types.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/issues/types`
- Source controller: `IncidentIQ API`

Search issue types

Searches issue types using a request-body filter. Use this when you need to constrain the list by scope, site, or other criteria supported by `GetIssueTypesRequest`.

**Workflow Example**
1. Build a `GetIssueTypesRequest` with the desired filters.
2. Submit the search: [POST /api/v1.0/issues/types](#/Issue Types/searchIssueTypes).
3. Use returned `Items[]` to drive issue type selection or validation.

**Minimal Required Fields**: None. Filters are optional.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `GetIssueTypesRequest` | `GetIssueTypesRequest` | - |

#### Returns

- Typed call return: `IssueTypeListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `IssueTypeListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `search_issues`

Provenance: Golden OpenAPI contract

Operation ID: `searchIssues`

- Sync: `client.issues.search_issues(body=..., timeout=None)`
- Async: `await client.issues.search_issues(body=..., timeout=None)`
- Raw payload: `client.issues.search_issues.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/issues`
- Source controller: `IncidentIQ API`

Search issues

Retrieves issues based on comprehensive search criteria. Use this endpoint to find issues filtered by models, categories, tickets, or other attributes.

**Use Cases**
- Find issues available for specific asset models
- Filter issues by category or type
- Get issues relevant to specific tickets
- Build dynamic issue selection interfaces based on context

**Search Strategy Options**
- `AggregateTicket`: Returns issues aggregated from ticket data
- `Explicit`: Returns explicitly defined issues only
- `All`: Returns all issues matching criteria

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `IssueSearchRequest` | `IssueSearchRequest` | - |

#### Returns

- Typed call return: `IssueSearchResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `IssueSearchResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `search_model_issues`

Provenance: Golden OpenAPI contract

Operation ID: `searchModelIssues`

- Sync: `client.issues.search_model_issues(body=None, timeout=None)`
- Async: `await client.issues.search_model_issues(body=None, timeout=None)`
- Raw payload: `client.issues.search_model_issues.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/issues/for/models/link`
- Source controller: `IncidentIQ API`

Search model issues

Searches model issue association records based on model, category, or integration filters. Use this to find ModelIssueId values for later updates or to audit which issues are linked to which models.

**Prerequisites**
1. **ModelIds (optional)** - Obtain from [POST /api/v1.0/assets/search](#/Assets/keywordSearchAssets) or [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById).
2. **ModelCategoryIds (optional)** - Use [GET /api/v1.0/categories/of/models](#/Categories/listModelCategories) and extract `Items[].CategoryId`.
3. **AppIds (optional)** - Use your integration registration IDs.

**Workflow Example**
1. Gather the filter IDs you want to scope by.
2. [POST /api/v1.0/issues/for/models/link](#/Model Issues/searchModelIssues) with `GetModelIssuesRequest` filters.
3. Use returned `Items[].ModelIssueId` values for link, unlink, or app overrides.

**Minimal Required Fields**: None. Provide at least one filter (ModelIds, ModelCategoryIds, or AppIds) to limit results.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `GetModelIssuesRequest` | `GetModelIssuesRequest` | - |

#### Returns

- Typed call return: `ModelIssueListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ModelIssueListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `set_app_model_issue_name_override`

Provenance: Golden OpenAPI contract

Operation ID: `setAppModelIssueNameOverride`

- Sync: `client.issues.set_app_model_issue_name_override(model_issue_id=..., app_id=..., body=None, timeout=None)`
- Async: `await client.issues.set_app_model_issue_name_override(model_issue_id=..., app_id=..., body=None, timeout=None)`
- Raw payload: `client.issues.set_app_model_issue_name_override.raw(model_issue_id=..., app_id=..., body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/issues/for/models/{modelIssueId}/link/app/{appId}/name`
- Source controller: `IncidentIQ API`

Set app model issue name override

Sets or updates the display name override for a model-issue association within a specific app. Use this when an integration needs a custom label different from the global issue name.

**Prerequisites**
1. **modelIssueId** - Use [POST /api/v1.0/issues/for/models/link](#/Model%20Issues/searchModelIssues) and extract `Items[].ModelIssueId`.
2. **appId** - Use the app's registration identifier from your integration settings.
3. Ensure the app is linked using [POST /api/v1.0/issues/for/models/{modelIssueId}/link/app/{appId}](#/Model%20Issues/linkModelIssueToApp).

**Workflow Example**
1. Link the app to the model issue if not already linked.
2. [POST /api/v1.0/issues/for/models/{modelIssueId}/link/app/{appId}/name](#/Model Issues/setAppModelIssueNameOverride) with `NameOverride`.
3. Verify the app displays the override name.

**Minimal Required Fields**: modelIssueId, appId (path) and NameOverride (request body).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `model_issue_id` | `modelIssueId` | `path` | `yes` | `str` | `-` | - |
| `app_id` | `appId` | `path` | `yes` | `str` | `-` | - |
| `body` | `body` | `body` | `no` | `SetAppModelIssueNameRequest` | `SetAppModelIssueNameRequest` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `set_issue_sort_order`

Provenance: Golden OpenAPI contract

Operation ID: `setIssueSortOrder`

- Sync: `client.issues.set_issue_sort_order(issue_id=..., sort_order=..., timeout=None)`
- Async: `await client.issues.set_issue_sort_order(issue_id=..., sort_order=..., timeout=None)`
- Raw payload: `client.issues.set_issue_sort_order.raw(issue_id=..., sort_order=..., timeout=None)`
- HTTP route: `POST /api/v1.0/issues/{issueId}/sortorder/{sortOrder}`
- Source controller: `IncidentIQ API`

Set issue sort order

Updates the display sort order for an issue. Use this to control how issues appear in selection lists within the UI.

**Prerequisites**
1. **issueId** - Use [GET /api/v1.0/issues](#/Issues/listIssues) or [POST /api/v1.0/issues](#/Issues/searchIssues) and extract `Items[].IssueId`.

**Workflow Example**
1. Identify the issue to reorder.
2. Set the desired sort order: [POST /api/v1.0/issues/{issueId}/sortorder/{sortOrder}](#/Issues/setIssueSortOrder).
3. Refresh issue lists to confirm the new ordering.

**Minimal Required Fields**: issueId and sortOrder (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `issue_id` | `issueId` | `path` | `yes` | `str` | `-` | - |
| `sort_order` | `sortOrder` | `path` | `yes` | `int` | `-` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `unlink_issue_from_app`

Provenance: Golden OpenAPI contract

Operation ID: `unlinkIssueFromApp`

- Sync: `client.issues.unlink_issue_from_app(issue_id=..., app_id=..., timeout=None)`
- Async: `await client.issues.unlink_issue_from_app(issue_id=..., app_id=..., timeout=None)`
- Raw payload: `client.issues.unlink_issue_from_app.raw(issue_id=..., app_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/issues/{issueId}/link/app/{appId}`
- Source controller: `IncidentIQ API`

Unlink issue from app

Unlinks an issue from an external app. Use this to remove the app's association so it no longer references the issue.

**Prerequisites**
1. **issueId** - Use [GET /api/v1.0/issues](#/Issues/listIssues) or [POST /api/v1.0/issues](#/Issues/searchIssues) and extract `Items[].IssueId`.
2. **appId** - Use the app's registration identifier from your integration settings.

**Workflow Example**
1. Identify the issue and app to unlink.
2. Unlink: [DELETE /api/v1.0/issues/{issueId}/link/app/{appId}](#/Issues/unlinkIssueFromApp).

**Minimal Required Fields**: issueId and appId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `issue_id` | `issueId` | `path` | `yes` | `str` | `-` | - |
| `app_id` | `appId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `unlink_model_issue_from_app`

Provenance: Golden OpenAPI contract

Operation ID: `unlinkModelIssueFromApp`

- Sync: `client.issues.unlink_model_issue_from_app(model_issue_id=..., app_id=..., timeout=None)`
- Async: `await client.issues.unlink_model_issue_from_app(model_issue_id=..., app_id=..., timeout=None)`
- Raw payload: `client.issues.unlink_model_issue_from_app.raw(model_issue_id=..., app_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/issues/for/models/{modelIssueId}/link/app/{appId}`
- Source controller: `IncidentIQ API`

Unlink model issue from app

Unlinks a model-issue association from an external app. Use this to revoke app visibility for a model issue without removing the underlying model-issue link.

**Prerequisites**
1. **modelIssueId** - Use [POST /api/v1.0/issues/for/models/link](#/Model%20Issues/searchModelIssues) and extract `Items[].ModelIssueId`.
2. **appId** - Use the app's registration identifier from your integration settings.

**Workflow Example**
1. Identify the app-linked model issue.
2. [DELETE /api/v1.0/issues/for/models/{modelIssueId}/link/app/{appId}](#/Model Issues/unlinkModelIssueFromApp).
3. Confirm the app no longer lists the model issue.

**Minimal Required Fields**: modelIssueId and appId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `model_issue_id` | `modelIssueId` | `path` | `yes` | `str` | `-` | - |
| `app_id` | `appId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_issue`

Provenance: Golden OpenAPI contract

Operation ID: `updateIssue`

- Sync: `client.issues.update_issue(issue_id=..., body=None, timeout=None)`
- Async: `await client.issues.update_issue(issue_id=..., body=None, timeout=None)`
- Raw payload: `client.issues.update_issue.raw(issue_id=..., body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/issues/{issueId}`
- Source controller: `IncidentIQ API`

Update issue

Updates an existing issue definition by ID. Use this to rename issues, change their type/category metadata, or adjust visibility settings.

**Prerequisites**
1. **issueId** - Use [GET /api/v1.0/issues](#/Issues/listIssues) or [POST /api/v1.0/issues](#/Issues/searchIssues) and extract `Items[].IssueId`.

**Workflow Example**
1. Load the issue: [GET /api/v1.0/issues/{issueId}](#/Issues/getIssueById).
2. Modify the fields in the `Issue` payload.
3. Save changes: [POST /api/v1.0/issues/{issueId}](#/Issues/updateIssue).

**Minimal Required Fields**: issueId (path) plus at least one field to update (commonly `Name` or `IssueTypeId`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `issue_id` | `issueId` | `path` | `yes` | `str` | `-` | - |
| `body` | `body` | `body` | `no` | `Issue` | `Issue` | - |

#### Returns

- Typed call return: `UpdateIssueResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UpdateIssueResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_issue_type`

Provenance: Golden OpenAPI contract

Operation ID: `updateIssueType`

- Sync: `client.issues.update_issue_type(issue_type_id=..., body=None, timeout=None)`
- Async: `await client.issues.update_issue_type(issue_type_id=..., body=None, timeout=None)`
- Raw payload: `client.issues.update_issue_type.raw(issue_type_id=..., body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/issues/types/{issueTypeId}`
- Source controller: `IncidentIQ API`

Update issue type

Updates an existing issue type definition by ID. Use this to rename a type, change its scope, or update product/site associations.

**Prerequisites**
1. **issueTypeId** - Use [GET /api/v1.0/issues/types](#/Issue%20Types/listIssueTypes) or [POST /api/v1.0/issues/types](#/Issue%20Types/searchIssueTypes) and extract `Items[].IssueTypeId`.

**Workflow Example**
1. Load the current type: [GET /api/v1.0/issues/types/{issueTypeId}](#/Issue Types/getIssueTypeById).
2. Modify fields in the `IssueType` payload.
3. Save changes: [POST /api/v1.0/issues/types/{issueTypeId}](#/Issue Types/updateIssueType).

**Minimal Required Fields**: issueTypeId (path) plus at least one field to update (commonly `Name` or `Scope`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `issue_type_id` | `issueTypeId` | `path` | `yes` | `str` | `-` | - |
| `body` | `body` | `body` | `no` | `IssueType` | `IssueType` | - |

#### Returns

- Typed call return: `UpdateIssueTypeResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UpdateIssueTypeResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_model_issues_to_match_category`

Provenance: Golden OpenAPI contract

Operation ID: `updateModelIssuesToMatchCategory`

- Sync: `client.issues.update_model_issues_to_match_category(model_id=..., timeout=None)`
- Async: `await client.issues.update_model_issues_to_match_category(model_id=..., timeout=None)`
- Raw payload: `client.issues.update_model_issues_to_match_category.raw(model_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/issues/for/models/{modelId}/match/category`
- Source controller: `IncidentIQ API`

Update model to match category issues

Updates a single model so its issue list matches the issues defined on its model category. Use this when only one model needs to be resynced after category updates or to undo manual overrides.

**Prerequisites**
1. **modelId** - Obtain from [POST /api/v1.0/assets/search](#/Assets/keywordSearchAssets) or [GET /api/v1.0/assets/{assetId}](#/Assets/getAssetById).
2. (Optional) Review category issues with [GET /api/v1.0/issues/for/model-categories/{categoryId}](#/Model%20Issues/getIssuesForModelCategory).

**Workflow Example**
1. Identify the target model ID.
2. [POST /api/v1.0/issues/for/models/{modelId}/match/category](#/Model Issues/updateModelIssuesToMatchCategory) to apply category defaults.
3. [GET /api/v1.0/issues/for/models/{modelId}](#/Model Issues/getIssuesForModel) to verify the new issue list.

**Minimal Required Fields**: modelId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `model_id` | `modelId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
