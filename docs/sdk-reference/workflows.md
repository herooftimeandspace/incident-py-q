# `workflows` Golden Namespace

Sync client access: `client.workflows`

Async client access: `client.workflows` with `await` on method calls.

These methods are Golden because they come from the bundled Incident IQ OpenAPI contract.

## Methods

### `create_workflow`

Provenance: Golden OpenAPI contract

Operation ID: `createWorkflow`

- Sync: `client.workflows.create_workflow(body=..., timeout=None)`
- Async: `await client.workflows.create_workflow(body=..., timeout=None)`
- Raw payload: `client.workflows.create_workflow.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/workflows/new`
- Source controller: `IncidentIQ API`

Create workflow

Creates a new workflow definition.

**Note**: This endpoint is part of API version 1.0 which is marked as deprecated.

**Authentication**: Requires authenticated user with workflow management permissions.

**Required Fields**:
- `Name` - Display name for the workflow
- `ProductId` - Product this workflow applies to
- `InitialStepId` - Starting step for new tickets (create step first or use existing)
- `PromptLocations`, `PromptUsers`, `PromptSystems` - Workflow behavior flags

**Workflow Example**:
1. Create initial step: [POST /api/v1.0/workflows/steps/new](#/Workflows/createWorkflowStep) → get `WorkflowStepId`.
2. Create workflow: [POST /api/v1.0/workflows/new](#/Workflows/createWorkflow) with the step ID as `InitialStepId`.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `Workflow` | `Workflow` | - |

#### Returns

- Typed call return: `WorkflowCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `WorkflowCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_workflow_step`

Provenance: Golden OpenAPI contract

Operation ID: `createWorkflowStep`

- Sync: `client.workflows.create_workflow_step(body=..., timeout=None)`
- Async: `await client.workflows.create_workflow_step(body=..., timeout=None)`
- Raw payload: `client.workflows.create_workflow_step.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/workflows/steps/new`
- Source controller: `IncidentIQ API`

Create workflow step

Creates a new workflow step (status) that can be used in workflow transitions.

**Note**: This endpoint is part of API version 1.0 which is marked as deprecated.

**Authentication**: Requires authenticated user with workflow management permissions.

**Required Fields**:
- `WorkflowId` - Parent workflow this step belongs to
- `StepName` - Display name for the step
- `StatusId` - Associated status identifier
- `IsClosed` - Whether tickets in this step are considered closed
- `DisplayOrder` - Ordering position in UI

**Workflow Example**:
1. Create workflow: [POST /api/v1.0/workflows/new](#/Workflows/createWorkflow) → get `WorkflowId`.
2. Create step: [POST /api/v1.0/workflows/steps/new](#/Workflows/createWorkflowStep) with `WorkflowId`.
3. Configure next-step mappings for transitions.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `WorkflowStepFull` | `WorkflowStepFull` | - |

#### Returns

- Typed call return: `WorkflowStepCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `WorkflowStepCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_workflow`

Provenance: Golden OpenAPI contract

Operation ID: `deleteWorkflow`

- Sync: `client.workflows.delete_workflow(workflow_id=..., timeout=None)`
- Async: `await client.workflows.delete_workflow(workflow_id=..., timeout=None)`
- Raw payload: `client.workflows.delete_workflow.raw(workflow_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/workflows/{workflowId}`
- Source controller: `IncidentIQ API`

Delete workflow

Deletes a workflow. This is a destructive operation that cannot be undone.

**Note**: This endpoint is part of API version 1.0 which is marked as deprecated.

**Warning**: Deleting a workflow may affect existing tickets that reference it. Ensure no tickets are using this workflow before deletion.

**Authentication**: Requires authenticated user with workflow management permissions.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `workflow_id` | `workflowId` | `path` | `yes` | `str` | `-` | UUID of the workflow to retrieve, update, or delete. Obtain by calling GET /api/v1.0/workflows. |

#### Returns

- Typed call return: `WorkflowDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `WorkflowDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_workflow_step`

Provenance: Golden OpenAPI contract

Operation ID: `deleteWorkflowStep`

- Sync: `client.workflows.delete_workflow_step(workflow_step_id=..., timeout=None)`
- Async: `await client.workflows.delete_workflow_step(workflow_step_id=..., timeout=None)`
- Raw payload: `client.workflows.delete_workflow_step.raw(workflow_step_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/workflows/steps/{workflowStepId}`
- Source controller: `IncidentIQ API`

Delete workflow step

Deletes a workflow step. This is a destructive operation.

**Note**: This endpoint is part of API version 1.0 which is marked as deprecated.

**Warning**: Ensure no tickets are currently in this step and no next-step mappings reference it.

**Authentication**: Requires authenticated user with workflow management permissions.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `workflow_step_id` | `workflowStepId` | `path` | `yes` | `str` | `-` | UUID of the workflow step to retrieve, update, or delete. |

#### Returns

- Typed call return: `WorkflowStepDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `WorkflowStepDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_workflow`

Provenance: Golden OpenAPI contract

Operation ID: `getWorkflow`

- Sync: `client.workflows.get_workflow(workflow_id=..., timeout=None)`
- Async: `await client.workflows.get_workflow(workflow_id=..., timeout=None)`
- Raw payload: `client.workflows.get_workflow.raw(workflow_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/workflows/{workflowId}`
- Source controller: `IncidentIQ API`

Get workflow by ID

Retrieves a single workflow definition by its UUID, including all configured steps.

**Note**: This endpoint is part of API version 1.0 which is marked as deprecated.

**Authentication**: Allows anonymous access and app authorization.

**Prerequisites**:
1. **workflowId** - Obtain by calling [GET /api/v1.0/workflows](#/Workflows/listWorkflows) or from a ticket's `WorkflowId` property.

**Workflow Example**:
1. List workflows: [GET /api/v1.0/workflows](#/Workflows/listWorkflows) → extract desired `WorkflowId`.
2. Get details: [GET /api/v1.0/workflows/{workflowId}](#/Workflows/getWorkflow).
3. Use `Steps[]` array to understand available transitions.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `workflow_id` | `workflowId` | `path` | `yes` | `str` | `-` | UUID of the workflow to retrieve, update, or delete. Obtain by calling GET /api/v1.0/workflows. |

#### Returns

- Typed call return: `WorkflowItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `WorkflowItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_workflow_action_types`

Provenance: Golden OpenAPI contract

Operation ID: `getWorkflowActionTypes`

- Sync: `client.workflows.get_workflow_action_types(timeout=None)`
- Async: `await client.workflows.get_workflow_action_types(timeout=None)`
- Raw payload: `client.workflows.get_workflow_action_types.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/workflows/actiontypes`
- Source controller: `IncidentIQ API`

List action types

Returns the available workflow action types that can be configured on workflow steps. Action types define the types of automated actions available.

**Note**: This endpoint is part of API version 1.0 which is marked as deprecated.

**Authentication**: Requires authenticated user.

**Use Case**: Get available action types when configuring automated actions for workflow steps.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `WorkflowActionTypeListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `WorkflowActionTypeListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_workflow_actions`

Provenance: Golden OpenAPI contract

Operation ID: `getWorkflowActions`

- Sync: `client.workflows.get_workflow_actions(workflow_step_id=..., timeout=None)`
- Async: `await client.workflows.get_workflow_actions(workflow_step_id=..., timeout=None)`
- Raw payload: `client.workflows.get_workflow_actions.raw(workflow_step_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/workflows/steps/{workflowStepId}/actions`
- Source controller: `IncidentIQ API`

List actions for a step

Returns the automated actions configured for a workflow step. Actions execute when tickets transition into this step.

**Note**: This endpoint is part of API version 1.0 which is marked as deprecated.

**Authentication**: Requires authenticated user.

**Use Case**: Understand what automation will trigger when a ticket enters a specific status.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `workflow_step_id` | `workflowStepId` | `path` | `yes` | `str` | `-` | UUID of the workflow step whose actions should be listed. |

#### Returns

- Typed call return: `WorkflowStepActionListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `WorkflowStepActionListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_workflow_approval_types`

Provenance: Golden OpenAPI contract

Operation ID: `getWorkflowApprovalTypes`

- Sync: `client.workflows.get_workflow_approval_types(timeout=None)`
- Async: `await client.workflows.get_workflow_approval_types(timeout=None)`
- Raw payload: `client.workflows.get_workflow_approval_types.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/workflows/approvaltypes`
- Source controller: `IncidentIQ API`

List approval types

Returns the available workflow approval types that can be configured on workflow steps. Approval types define the approval process required for certain transitions.

**Note**: This endpoint is part of API version 1.0 which is marked as deprecated.

**Authentication**: Requires authenticated user.

**Use Case**: Get available approval types when configuring workflow steps that require approval.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `WorkflowApprovalTypeListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `WorkflowApprovalTypeListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_workflow_custom_fields`

Provenance: Golden OpenAPI contract

Operation ID: `getWorkflowCustomFields`

- Sync: `client.workflows.get_workflow_custom_fields(workflow_id=..., timeout=None)`
- Async: `await client.workflows.get_workflow_custom_fields(workflow_id=..., timeout=None)`
- Raw payload: `client.workflows.get_workflow_custom_fields.raw(workflow_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/workflows/{workflowId}/fields`
- Source controller: `IncidentIQ API`

List custom fields for workflow

Returns the custom fields that are configured for tickets using this workflow. Custom fields extend the standard ticket data model.

**Note**: This endpoint is part of API version 1.0 which is marked as deprecated. This is an async operation.

**Authentication**: Requires authenticated user.

**Use Case**: Determine which custom fields should be displayed when creating or editing tickets in this workflow.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `workflow_id` | `workflowId` | `path` | `yes` | `str` | `-` | UUID of the workflow whose custom fields should be listed. |

#### Returns

- Typed call return: `WorkflowCustomFieldListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `WorkflowCustomFieldListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_workflow_linked_issues`

Provenance: Golden OpenAPI contract

Operation ID: `getWorkflowLinkedIssues`

- Sync: `client.workflows.get_workflow_linked_issues(workflow_id=..., timeout=None)`
- Async: `await client.workflows.get_workflow_linked_issues(workflow_id=..., timeout=None)`
- Raw payload: `client.workflows.get_workflow_linked_issues.raw(workflow_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/workflows/{workflowId}/issues`
- Source controller: `IncidentIQ API`

List issues linked to workflow

Returns the issue types (ticket categories) that are linked to a specific workflow. Issues determine the initial categorization of tickets.

**Note**: This endpoint is part of API version 1.0 which is marked as deprecated.

**Authentication**: Requires authenticated user.

**Use Case**: Understand which issue types will use this workflow when tickets are created.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `workflow_id` | `workflowId` | `path` | `yes` | `str` | `-` | UUID of the workflow whose linked issues should be listed. |

#### Returns

- Typed call return: `WorkflowIssueListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `WorkflowIssueListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_workflow_next_steps`

Provenance: Golden OpenAPI contract

Operation ID: `getWorkflowNextSteps`

- Sync: `client.workflows.get_workflow_next_steps(workflow_step_id=..., timeout=None)`
- Async: `await client.workflows.get_workflow_next_steps(workflow_step_id=..., timeout=None)`
- Raw payload: `client.workflows.get_workflow_next_steps.raw(workflow_step_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/workflows/steps/{workflowStepId}/nextsteps`
- Source controller: `IncidentIQ API`

List next-step mappings

Returns the allowed next-step transition mappings for a workflow step. These mappings define which status transitions are valid from the current step.

**Note**: This endpoint is part of API version 1.0 which is marked as deprecated.

**Authentication**: Requires authenticated user.

**Use Case**: Determine valid status transitions when updating a ticket.

**Workflow Example**:
1. Get ticket: [GET /api/v1.0/tickets/{ticketId}](#/Tickets/getTicket) → extract `WorkflowStep.WorkflowStepId`.
2. Get allowed transitions: [GET /api/v1.0/workflows/steps/{workflowStepId}/nextsteps](#/Workflows/getWorkflowNextSteps).
3. Use `AllowedNextWorkflowStepId` values when changing ticket status.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `workflow_step_id` | `workflowStepId` | `path` | `yes` | `str` | `-` | UUID of the workflow step whose next-step mappings should be listed. |

#### Returns

- Typed call return: `WorkflowNextStepListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `WorkflowNextStepListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_workflow_next_steps_as_steps`

Provenance: Golden OpenAPI contract

Operation ID: `getWorkflowNextStepsAsSteps`

- Sync: `client.workflows.get_workflow_next_steps_as_steps(workflow_step_id=..., timeout=None)`
- Async: `await client.workflows.get_workflow_next_steps_as_steps(workflow_step_id=..., timeout=None)`
- Raw payload: `client.workflows.get_workflow_next_steps_as_steps.raw(workflow_step_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/workflows/steps/{workflowStepId}/nextsteps/steps`
- Source controller: `IncidentIQ API`

List next steps as full step objects

Returns the allowed next steps as full `WorkflowStep` objects rather than just mapping references. Useful when you need complete step details for UI rendering.

**Note**: This endpoint is part of API version 1.0 which is marked as deprecated.

**Authentication**: Requires authenticated user.

**Use Case**: Get full step details for building status transition dropdowns or menus.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `workflow_step_id` | `workflowStepId` | `path` | `yes` | `str` | `-` | UUID of the workflow step whose next steps should be listed as full step objects. |

#### Returns

- Typed call return: `WorkflowStepListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `WorkflowStepListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_workflow_step`

Provenance: Golden OpenAPI contract

Operation ID: `getWorkflowStep`

- Sync: `client.workflows.get_workflow_step(workflow_step_id=..., timeout=None)`
- Async: `await client.workflows.get_workflow_step(workflow_step_id=..., timeout=None)`
- Raw payload: `client.workflows.get_workflow_step.raw(workflow_step_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/workflows/steps/{workflowStepId}`
- Source controller: `IncidentIQ API`

Get workflow step by ID

Retrieves a single workflow step by its UUID.

**Note**: This endpoint is part of API version 1.0 which is marked as deprecated.

**Authentication**: Requires authenticated user.

**Prerequisites**:
1. **workflowStepId** - Obtain from [GET /api/v1.0/workflows/steps](#/Workflows/getWorkflowSteps) or from ticket's `WorkflowStep.WorkflowStepId`.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `workflow_step_id` | `workflowStepId` | `path` | `yes` | `str` | `-` | UUID of the workflow step to retrieve, update, or delete. |

#### Returns

- Typed call return: `WorkflowStepItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `WorkflowStepItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_workflow_steps`

Provenance: Golden OpenAPI contract

Operation ID: `getWorkflowSteps`

- Sync: `client.workflows.get_workflow_steps(p=None, s=None, filter=None, timeout=None)`
- Async: `await client.workflows.get_workflow_steps(p=None, s=None, filter=None, timeout=None)`
- Raw payload: `client.workflows.get_workflow_steps.raw(p=None, s=None, filter=None, timeout=None)`
- HTTP route: `GET /api/v1.0/workflows/steps`
- Source controller: `IncidentIQ API`

List all workflow steps

Lists workflow steps (ticket statuses) available to the authenticated tenant with paging and filter support.

**Note**: This endpoint is part of API version 1.0 which is marked as deprecated.

**Default Paging**: Returns up to 100 records per page, sorted by `Name` ascending.

**Prerequisites**:
1. **Workflow context** - Use [GET /api/v1.0/tickets/{ticketId}](#/Tickets/getTicket) to read `Item.WorkflowStep.WorkflowId`, or call workflow endpoints to determine the workflow.
2. **Filtering** - Prepare optional OData-style filters such as `$filter=WorkflowId eq {workflowId}` to narrow results.

**Workflow Example**:
1. Identify a ticket: [POST /api/v1.0/tickets](#/Tickets/searchTickets) with filters → extract `Items[0].WorkflowStep.WorkflowId`.
2. Call [GET /api/v1.0/workflows/steps](#/Workflows/getWorkflowSteps) with `$filter=WorkflowId eq {workflowId}` to fetch valid transitions.
3. Use `Items[].WorkflowStepId` when updating tickets.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `p` | `$p` | `query` | `no` | `int` | `-` | Zero-based page index to retrieve. |
| `s` | `$s` | `query` | `no` | `int` | `-` | Number of records per page. |
| `filter` | `$filter` | `query` | `no` | `str` | `-` | Filter expression applied to the result set (e.g., `(WorkflowId eq {workflowId})` or `(StepName contains 'Resolved')`). |

#### Returns

- Typed call return: `WorkflowStepsResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `WorkflowStepsResponse`
- Pagination helper: `client.workflows.get_workflow_steps.iter_pages(start_page=1, page_size=100, max_pages=None, p=None, s=None, filter=None, timeout=None)`

---

### `get_workflow_steps_by_workflow`

Provenance: Golden OpenAPI contract

Operation ID: `getWorkflowStepsByWorkflow`

- Sync: `client.workflows.get_workflow_steps_by_workflow(workflow_id=..., timeout=None)`
- Async: `await client.workflows.get_workflow_steps_by_workflow(workflow_id=..., timeout=None)`
- Raw payload: `client.workflows.get_workflow_steps_by_workflow.raw(workflow_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/workflows/{workflowId}/steps`
- Source controller: `IncidentIQ API`

List steps for a workflow

Returns all workflow steps (statuses) configured for a specific workflow.

**Note**: This endpoint is part of API version 1.0 which is marked as deprecated.

**Authentication**: Requires authenticated user.

**Prerequisites**:
1. **workflowId** - Obtain from [GET /api/v1.0/workflows](#/Workflows/listWorkflows).

**Workflow Example**:
1. Get workflow: [GET /api/v1.0/workflows](#/Workflows/listWorkflows) → extract `WorkflowId`.
2. List steps: [GET /api/v1.0/workflows/{workflowId}/steps](#/Workflows/getWorkflowStepsByWorkflow).
3. Use `WorkflowStepId` values when updating ticket status.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `workflow_id` | `workflowId` | `path` | `yes` | `str` | `-` | UUID of the workflow whose steps should be listed. |

#### Returns

- Typed call return: `WorkflowStepListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `WorkflowStepListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_workflows`

Provenance: Golden OpenAPI contract

Operation ID: `listWorkflows`

- Sync: `client.workflows.list_workflows(timeout=None)`
- Async: `await client.workflows.list_workflows(timeout=None)`
- Raw payload: `client.workflows.list_workflows.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/workflows`
- Source controller: `IncidentIQ API`

List workflows

Returns all workflows available to the authenticated tenant for the current product context.

**Note**: This endpoint is part of API version 1.0 which is marked as deprecated. Consider using newer versioned endpoints when available.

**Authentication**: Requires a valid bearer token or session cookie.

**Workflow Example**:
1. Call [GET /api/v1.0/workflows](#/Workflows/listWorkflows) to retrieve all workflows for your product.
2. Use the `WorkflowId` from the response when creating tickets or querying workflow steps.
3. Use `InitialStepId` to understand the starting status for new tickets.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `WorkflowListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `WorkflowListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_workflows_all_products`

Provenance: Golden OpenAPI contract

Operation ID: `listWorkflowsAllProducts`

- Sync: `client.workflows.list_workflows_all_products(timeout=None)`
- Async: `await client.workflows.list_workflows_all_products(timeout=None)`
- Raw payload: `client.workflows.list_workflows_all_products.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/workflows/allproducts`
- Source controller: `IncidentIQ API`

List workflows across all products

Returns workflows for all licensed products at the authenticated tenant's site. Useful for applications that need to display or manage workflows across multiple product lines.

**Note**: This endpoint is part of API version 1.0 which is marked as deprecated.

**Authentication**: Supports both XSRF public authorization and app authorization. No user session required when using app keys.

**Workflow Example**:
1. Call [GET /api/v1.0/workflows/allproducts](#/Workflows/listWorkflowsAllProducts) to see all workflows across products.
2. Group by `ProductId` to organize workflows by product.
3. Use when building cross-product dashboards or administrative tools.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `WorkflowListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `WorkflowListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_workflows_by_site_and_product`

Provenance: Golden OpenAPI contract

Operation ID: `listWorkflowsBySiteAndProduct`

- Sync: `client.workflows.list_workflows_by_site_and_product(site_id=..., product_id=..., timeout=None)`
- Async: `await client.workflows.list_workflows_by_site_and_product(site_id=..., product_id=..., timeout=None)`
- Raw payload: `client.workflows.list_workflows_by_site_and_product.raw(site_id=..., product_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/workflows/site/{siteId}/product/{productId}`
- Source controller: `IncidentIQ API`

List workflows by site and product

Returns workflows configured for a specific site and product combination. Use this endpoint when you need workflows filtered to a particular product context.

**Note**: This endpoint is part of API version 1.0 which is marked as deprecated.

**Authentication**: Allows anonymous access and app authorization.

**Prerequisites**:
1. **siteId** - Call [GET /api/v1.0/sites/{siteUrl}](#/Sites/getSiteByUrl) and extract `Item.SiteId`.
2. **productId** - Obtain from site's `LicensedProducts[]` or use the ProductId header value.

**Workflow Example**:
1. Identify site: [GET /api/v1.0/sites/{siteUrl}](#/Sites/getSiteByUrl) → extract `Item.SiteId` and `Item.LicensedProducts[].ProductId`.
2. Get workflows: [GET /api/v1.0/workflows/site/{siteId}/product/{productId}](#/Workflows/listWorkflowsBySiteAndProduct).
3. Use `WorkflowId` for ticket operations.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `site_id` | `siteId` | `path` | `yes` | `str` | `-` | UUID of the site. Obtain by calling GET /api/v1.0/sites/{siteUrl} and reading `Item.SiteId`. |
| `product_id` | `productId` | `path` | `yes` | `str` | `-` | UUID of the product. Obtain from site's licensed products list or from ProductId header. |

#### Returns

- Typed call return: `WorkflowListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `WorkflowListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_workflow`

Provenance: Golden OpenAPI contract

Operation ID: `updateWorkflow`

- Sync: `client.workflows.update_workflow(workflow_id=..., body=..., timeout=None)`
- Async: `await client.workflows.update_workflow(workflow_id=..., body=..., timeout=None)`
- Raw payload: `client.workflows.update_workflow.raw(workflow_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/workflows/{workflowId}`
- Source controller: `IncidentIQ API`

Update workflow

Updates an existing workflow or creates it if it doesn't exist (upsert behavior).

**Note**: This endpoint is part of API version 1.0 which is marked as deprecated.

**Authentication**: Requires authenticated user with workflow management permissions.

**Prerequisites**:
1. **workflowId** - The UUID of the workflow to update.
2. **Workflow body** - Complete workflow object with updated properties.

**Request Body**: Submit a `Workflow` object. The `WorkflowId` in the path takes precedence over the body.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `workflow_id` | `workflowId` | `path` | `yes` | `str` | `-` | UUID of the workflow to retrieve, update, or delete. Obtain by calling GET /api/v1.0/workflows. |
| `body` | `body` | `body` | `yes` | `Workflow` | `Workflow` | - |

#### Returns

- Typed call return: `WorkflowUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `WorkflowUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_workflow_step`

Provenance: Golden OpenAPI contract

Operation ID: `updateWorkflowStep`

- Sync: `client.workflows.update_workflow_step(workflow_step_id=..., body=..., timeout=None)`
- Async: `await client.workflows.update_workflow_step(workflow_step_id=..., body=..., timeout=None)`
- Raw payload: `client.workflows.update_workflow_step.raw(workflow_step_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/workflows/steps/{workflowStepId}`
- Source controller: `IncidentIQ API`

Update workflow step

Updates an existing workflow step or creates it if it doesn't exist (upsert behavior).

**Note**: This endpoint is part of API version 1.0 which is marked as deprecated.

**Authentication**: Requires authenticated user with workflow management permissions.

**Request Body**: Submit a `WorkflowStep` object. The `WorkflowStepId` in the path takes precedence.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `workflow_step_id` | `workflowStepId` | `path` | `yes` | `str` | `-` | UUID of the workflow step to retrieve, update, or delete. |
| `body` | `body` | `body` | `yes` | `WorkflowStepFull` | `WorkflowStepFull` | - |

#### Returns

- Typed call return: `WorkflowStepUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `WorkflowStepUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
