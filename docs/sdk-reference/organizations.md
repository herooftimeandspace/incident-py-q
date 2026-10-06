# `organizations` Golden Namespace

Sync client access: `client.organizations`

Async client access: `client.organizations` with `await` on method calls.

These methods are Golden because they come from the bundled Incident IQ OpenAPI contract.

## Aliases

| Alias | Canonical Method | Route |
| --- | --- | --- |
| `create` | `create_organization` | `POST /api/v1.0/organizations/new` |

## Methods

### `create_organization`

Provenance: Golden OpenAPI contract

Operation ID: `createOrganization`

- Sync: `client.organizations.create_organization(body=..., timeout=None)`
- Async: `await client.organizations.create_organization(body=..., timeout=None)`
- Raw payload: `client.organizations.create_organization.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/organizations/new`
- Source controller: `IncidentIQ API`
- Aliases: `create`

Create organization

Creates a single organization record. Use this endpoint for individual onboarding flows or when building a new organization with specific contact and metadata fields.

**Workflow Example**
1. Gather organization details (Name, SiteId, optional contact info).
2. If you need an OrganizationTypeId, obtain it from [GET /api/v1.0/organizations/types/query](#/Organizations/getOrganizationTypesByQueryGet).
3. Call [POST /api/v1.0/organizations/new](#/Organizations/createOrganization) with the payload.

**Minimal Required Fields**: Name (SiteId recommended when the organization is site-scoped).

**Notes**: This API version is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `UpdateOrganizationRequest` | `UpdateOrganizationRequest` | - |

#### Returns

- Typed call return: `OrganizationItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `OrganizationItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_organization_type`

Provenance: Golden OpenAPI contract

Operation ID: `createOrganizationType`

- Sync: `client.organizations.create_organization_type(body=..., timeout=None)`
- Async: `await client.organizations.create_organization_type(body=..., timeout=None)`
- Raw payload: `client.organizations.create_organization_type.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/organizations/types`
- Source controller: `IncidentIQ API`

Create organization type

Creates a single organization type record. Use this endpoint to add a new type to the taxonomy before assigning it to organizations.

**Workflow Example**
1. Decide the Name and Scope (Global or Site) for the new type.
2. If Scope is Site, include SiteId for the owning site.
3. Call [POST /api/v1.0/organizations/types](#/Organizations/createOrganizationType) with the new type payload.

**Minimal Required Fields**: Name and Scope (SiteId when Scope is Site).

**Notes**: This API version is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `UpdateOrganizationTypeRequest` | `UpdateOrganizationTypeRequest` | - |

#### Returns

- Typed call return: `OrganizationTypeItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `OrganizationTypeItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_organization_types`

Provenance: Golden OpenAPI contract

Operation ID: `createOrganizationTypes`

- Sync: `client.organizations.create_organization_types(body=..., timeout=None)`
- Async: `await client.organizations.create_organization_types(body=..., timeout=None)`
- Raw payload: `client.organizations.create_organization_types.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/organizations/types/ids`
- Source controller: `IncidentIQ API`

Create multiple organization types

Creates multiple organization types in a single batch. Use this when onboarding a set of standard types or migrating taxonomy from another system.

**Workflow Example**
1. Prepare an array of organization type objects with Name and Scope (and SiteId when Scope is Site).
2. Call [POST /api/v1.0/organizations/types/ids](#/Organizations/createOrganizationTypes) to create the batch.

**Minimal Required Fields**: Name, Scope for each array item (SiteId when Scope is Site).

**Notes**: This API version is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | - |

#### Returns

- Typed call return: `OrganizationTypeBatchCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `OrganizationTypeBatchCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_organization_user`

Provenance: Golden OpenAPI contract

Operation ID: `createOrganizationUser`

- Sync: `client.organizations.create_organization_user(body=..., timeout=None)`
- Async: `await client.organizations.create_organization_user(body=..., timeout=None)`
- Raw payload: `client.organizations.create_organization_user.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/organizations/users`
- Source controller: `IncidentIQ API`

Create organization user

Creates a single organization-user relationship. Use this when onboarding one user to an organization or adding a member ad hoc without batching.

**Prerequisites**
1. **OrganizationId** - Use [GET /api/v1.0/organizations/query](#/Organizations/getOrganizationsByQueryGet) and extract `Items[].OrganizationId`.
2. **UserId** - Use [POST /api/v1.0/search](#/Users/searchUsers) and extract `Item.Users[].UserId`.

**Workflow Example**
1. Find the OrganizationId and UserId for the membership you want to create.
2. Call [POST /api/v1.0/organizations/users](#/Organizations/createOrganizationUser) with OrganizationId and UserId.

**Minimal Required Fields**: OrganizationId, UserId.

**Notes**: This API version is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `UpdateOrganizationUserRequest` | `UpdateOrganizationUserRequest` | - |

#### Returns

- Typed call return: `OrganizationUserItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `OrganizationUserItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_organization_users`

Provenance: Golden OpenAPI contract

Operation ID: `createOrganizationUsers`

- Sync: `client.organizations.create_organization_users(body=..., timeout=None)`
- Async: `await client.organizations.create_organization_users(body=..., timeout=None)`
- Raw payload: `client.organizations.create_organization_users.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/organizations/users/ids`
- Source controller: `IncidentIQ API`

Create multiple organization users

Creates multiple organization-user relationships in a single batch. Use this when you need to enroll many users into organizations or build membership lists from an external roster.

**Prerequisites**
1. **OrganizationId** - Use [GET /api/v1.0/organizations/query](#/Organizations/getOrganizationsByQueryGet) and extract `Items[].OrganizationId`.
2. **UserId** - Use [POST /api/v1.0/search](#/Users/searchUsers) and extract `Item.Users[].UserId`.

**Workflow Example**
1. Gather OrganizationId and UserId values.
2. Build an array of objects with OrganizationId and UserId.
3. Call [POST /api/v1.0/organizations/users/ids](#/Organizations/createOrganizationUsers) to create the relationships.

**Minimal Required Fields**: OrganizationId, UserId for each array item.

**Notes**: This API version is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | - |

#### Returns

- Typed call return: `OrganizationUserBatchCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `OrganizationUserBatchCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_organizations`

Provenance: Golden OpenAPI contract

Operation ID: `createOrganizations`

- Sync: `client.organizations.create_organizations(body=..., timeout=None)`
- Async: `await client.organizations.create_organizations(body=..., timeout=None)`
- Raw payload: `client.organizations.create_organizations.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/organizations/ids`
- Source controller: `IncidentIQ API`

Create multiple organizations

Creates multiple organizations in a single batch. Use this when importing or onboarding a set of organizations from an external system.

**Workflow Example**
1. Prepare an array of organization payloads with the fields you want to set (Name, SiteId, contact details, etc.).
2. Call [POST /api/v1.0/organizations/ids](#/Organizations/createOrganizations) to create the batch.

**Minimal Required Fields**: Name for each item; include SiteId when the organization is site-scoped.

**Notes**: This API version is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | - |

#### Returns

- Typed call return: `OrganizationBatchCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `OrganizationBatchCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_organization`

Provenance: Golden OpenAPI contract

Operation ID: `deleteOrganization`

- Sync: `client.organizations.delete_organization(organization_id=..., timeout=None)`
- Async: `await client.organizations.delete_organization(organization_id=..., timeout=None)`
- Raw payload: `client.organizations.delete_organization.raw(organization_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/organizations/{OrganizationId}`
- Source controller: `IncidentIQ API`

Delete organization by ID

Deletes a single organization by OrganizationId. Use this when you need to retire a specific organization record and you have already confirmed it is safe to remove.

**Prerequisites**
1. **OrganizationId** - Use [GET /api/v1.0/organizations/query](#/Organizations/getOrganizationsByQueryGet) and extract `Items[].OrganizationId`.

**Workflow Example**
1. Confirm the organization details with [GET /api/v1.0/organizations/{OrganizationId}](#/Organizations/getOrganization).
2. Call [DELETE /api/v1.0/organizations/{OrganizationId}](#/Organizations/deleteOrganization) to remove the record.

**Minimal Required Fields**: OrganizationId path parameter.

**Notes**: This API version is deprecated and performs a destructive action.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `organization_id` | `OrganizationId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `OrganizationsDomainDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `OrganizationsDomainDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_organization_type`

Provenance: Golden OpenAPI contract

Operation ID: `deleteOrganizationType`

- Sync: `client.organizations.delete_organization_type(organization_type_id=..., timeout=None)`
- Async: `await client.organizations.delete_organization_type(organization_type_id=..., timeout=None)`
- Raw payload: `client.organizations.delete_organization_type.raw(organization_type_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/organizations/types/{OrganizationTypeId}`
- Source controller: `IncidentIQ API`

Delete organization type by ID

Deletes a single organization type by OrganizationTypeId. Use this when you need to retire a specific type and you have confirmed it is not referenced by active organizations.

**Prerequisites**
1. **OrganizationTypeId** - Use [GET /api/v1.0/organizations/types/query](#/Organizations/getOrganizationTypesByQueryGet) and extract `Items[].OrganizationTypeId`.

**Workflow Example**
1. Review type usage by querying organizations or types.
2. Call [DELETE /api/v1.0/organizations/types/{OrganizationTypeId}](#/Organizations/deleteOrganizationType).

**Minimal Required Fields**: OrganizationTypeId path parameter.

**Notes**: This API version is deprecated and performs a destructive action.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `organization_type_id` | `OrganizationTypeId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `OrganizationsDomainDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `OrganizationsDomainDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_organization_types_by_ids`

Provenance: Golden OpenAPI contract

Operation ID: `deleteOrganizationTypesByIds`

- Sync: `client.organizations.delete_organization_types_by_ids(body=..., timeout=None)`
- Async: `await client.organizations.delete_organization_types_by_ids(body=..., timeout=None)`
- Raw payload: `client.organizations.delete_organization_types_by_ids.raw(body=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/organizations/types/ids`
- Source controller: `IncidentIQ API`

Delete organization types by IDs

Deletes organization types for the provided list of OrganizationTypeId values. Use this when you have a known set of types to remove and want a deterministic bulk delete.

**Prerequisites**
1. **OrganizationTypeId** - Use [GET /api/v1.0/organizations/types/query](#/Organizations/getOrganizationTypesByQueryGet) and extract `Items[].OrganizationTypeId`.

**Workflow Example**
1. Collect the OrganizationTypeId list.
2. Call [DELETE /api/v1.0/organizations/types/ids](#/Organizations/deleteOrganizationTypesByIds) with the ID array in the body.

**Minimal Required Fields**: OrganizationTypeId array in the request body.

**Notes**: This API version is deprecated and performs a destructive bulk action.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | - |

#### Returns

- Typed call return: `OrganizationsDomainBatchDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `OrganizationsDomainBatchDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_organization_types_by_query`

Provenance: Golden OpenAPI contract

Operation ID: `deleteOrganizationTypesByQuery`

- Sync: `client.organizations.delete_organization_types_by_query(timeout=None)`
- Async: `await client.organizations.delete_organization_types_by_query(timeout=None)`
- Raw payload: `client.organizations.delete_organization_types_by_query.raw(timeout=None)`
- HTTP route: `DELETE /api/v1.0/organizations/types/query`
- Source controller: `IncidentIQ API`

Delete organization types by query

Deletes organization types that match the provided query criteria. This is a bulk, destructive operation intended for administrative cleanup after you have validated the target set.

**Workflow Example**
1. Preview matches with [GET /api/v1.0/organizations/types/query](#/Organizations/getOrganizationTypesByQueryGet).
2. Call [DELETE /api/v1.0/organizations/types/query](#/Organizations/deleteOrganizationTypesByQuery) to remove the matched types.

**Minimal Required Fields**: Provide filters or query constraints to scope the deletion.

**Notes**: This API version is deprecated and can remove multiple types at once.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `OrganizationsDomainBatchDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `OrganizationsDomainBatchDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_organization_user`

Provenance: Golden OpenAPI contract

Operation ID: `deleteOrganizationUser`

- Sync: `client.organizations.delete_organization_user(organization_user_id=..., timeout=None)`
- Async: `await client.organizations.delete_organization_user(organization_user_id=..., timeout=None)`
- Raw payload: `client.organizations.delete_organization_user.raw(organization_user_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/organizations/users/{OrganizationUserId}`
- Source controller: `IncidentIQ API`

Delete organization user by ID

Deletes a single organization-user relationship by OrganizationUserId. Use this when you need to remove a specific membership link and you already know the relationship ID.

**Prerequisites**
1. **OrganizationUserId** - Use [GET /api/v1.0/organizations/users/query](#/Organizations/getOrganizationUsersByQueryGet) and extract `Items[].OrganizationUserId`.

**Workflow Example**
1. Identify the relationship ID to remove.
2. Call [DELETE /api/v1.0/organizations/users/{OrganizationUserId}](#/Organizations/deleteOrganizationUser).

**Minimal Required Fields**: OrganizationUserId path parameter.

**Notes**: This API version is deprecated and performs a destructive action.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `organization_user_id` | `OrganizationUserId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `OrganizationsDomainDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `OrganizationsDomainDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_organization_users_by_ids`

Provenance: Golden OpenAPI contract

Operation ID: `deleteOrganizationUsersByIds`

- Sync: `client.organizations.delete_organization_users_by_ids(body=..., timeout=None)`
- Async: `await client.organizations.delete_organization_users_by_ids(body=..., timeout=None)`
- Raw payload: `client.organizations.delete_organization_users_by_ids.raw(body=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/organizations/users/ids`
- Source controller: `IncidentIQ API`

Delete organization users by IDs

Deletes organization-user relationships for the specified OrganizationUserId values. Use this when you already know the relationship IDs and want a deterministic bulk delete without querying by filters.

**Prerequisites**
1. **OrganizationUserId** - Use [GET /api/v1.0/organizations/users/query](#/Organizations/getOrganizationUsersByQueryGet) and extract `Items[].OrganizationUserId`.

**Workflow Example**
1. Query to assemble the list of relationship IDs.
2. Call [DELETE /api/v1.0/organizations/users/ids](#/Organizations/deleteOrganizationUsersByIds) with the ID array in the body.

**Minimal Required Fields**: OrganizationUserId array in the request body.

**Notes**: This API version is deprecated and performs a destructive bulk action.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | - |

#### Returns

- Typed call return: `OrganizationsDomainBatchDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `OrganizationsDomainBatchDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_organization_users_by_query`

Provenance: Golden OpenAPI contract

Operation ID: `deleteOrganizationUsersByQuery`

- Sync: `client.organizations.delete_organization_users_by_query(organization_id=None, timeout=None)`
- Async: `await client.organizations.delete_organization_users_by_query(organization_id=None, timeout=None)`
- Raw payload: `client.organizations.delete_organization_users_by_query.raw(organization_id=None, timeout=None)`
- HTTP route: `DELETE /api/v1.0/organizations/users/query`
- Source controller: `IncidentIQ API`

Delete organization users by query

Deletes organization-user relationships matching the provided query parameters. Use this for bulk cleanup when you can identify the relationships to remove via OrganizationId or other query constraints.

**Workflow Example**
1. Preview matches with [GET /api/v1.0/organizations/users/query](#/Organizations/getOrganizationUsersByQueryGet) and confirm the list.
2. Call [DELETE /api/v1.0/organizations/users/query](#/Organizations/deleteOrganizationUsersByQuery) with OrganizationId to remove matching relationships.

**Minimal Required Fields**: OrganizationId is recommended to scope deletion.

**Notes**: This API version is deprecated and performs a destructive bulk action.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `organization_id` | `OrganizationId` | `query` | `no` | `str` | `-` | - |

#### Returns

- Typed call return: `OrganizationsDomainBatchDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `OrganizationsDomainBatchDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_organizations_by_ids`

Provenance: Golden OpenAPI contract

Operation ID: `deleteOrganizationsByIds`

- Sync: `client.organizations.delete_organizations_by_ids(body=..., timeout=None)`
- Async: `await client.organizations.delete_organizations_by_ids(body=..., timeout=None)`
- Raw payload: `client.organizations.delete_organizations_by_ids.raw(body=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/organizations/ids`
- Source controller: `IncidentIQ API`

Delete organizations by IDs

Deletes organizations for the supplied list of OrganizationId values. Use this when you have a known set of organizations to remove and want a deterministic bulk delete.

**Prerequisites**
1. **OrganizationId** - Use [GET /api/v1.0/organizations/query](#/Organizations/getOrganizationsByQueryGet) and extract `Items[].OrganizationId`.

**Workflow Example**
1. Collect the OrganizationId list from a query.
2. Call [DELETE /api/v1.0/organizations/ids](#/Organizations/deleteOrganizationsByIds) with the ID array in the request body.

**Minimal Required Fields**: OrganizationId array in the request body.

**Notes**: This API version is deprecated and performs a destructive bulk action.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | - |

#### Returns

- Typed call return: `OrganizationsDomainBatchDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `OrganizationsDomainBatchDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_organizations_by_query`

Provenance: Golden OpenAPI contract

Operation ID: `deleteOrganizationsByQuery`

- Sync: `client.organizations.delete_organizations_by_query(timeout=None)`
- Async: `await client.organizations.delete_organizations_by_query(timeout=None)`
- Raw payload: `client.organizations.delete_organizations_by_query.raw(timeout=None)`
- HTTP route: `DELETE /api/v1.0/organizations/query`
- Source controller: `IncidentIQ API`

Delete organizations by query

Deletes organizations that match the supplied query criteria. This is a bulk, destructive operation intended for administrative cleanup after you have verified the target set.

**Workflow Example**
1. Preview matches with [GET /api/v1.0/organizations/query](#/Organizations/getOrganizationsByQueryGet).
2. Call [DELETE /api/v1.0/organizations/query](#/Organizations/deleteOrganizationsByQuery) to remove the matched organizations.

**Minimal Required Fields**: Provide filters or query constraints to scope the deletion.

**Notes**: This API version is deprecated and should be used with caution.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `OrganizationsDomainBatchDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `OrganizationsDomainBatchDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_default_organization`

Provenance: Golden OpenAPI contract

Operation ID: `getDefaultOrganization`

- Sync: `client.organizations.get_default_organization(timeout=None)`
- Async: `await client.organizations.get_default_organization(timeout=None)`
- Raw payload: `client.organizations.get_default_organization.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/organizations/default`
- Source controller: `IncidentIQ API`

Get default organization

Returns the default organization associated with the current tenant or user context. Use this as a quick bootstrap when you need a single organization record for downstream operations and do not want to run a full query.

**Workflow Example**
1. Call [GET /api/v1.0/organizations/default](#/Organizations/getDefaultOrganization) to obtain the default record.
2. Extract `Item.OrganizationId` and use it in follow-up calls like [GET /api/v1.0/organizations/{OrganizationId}](#/Organizations/getOrganization).

**Minimal Required Fields**: None.

**Notes**: This API version is deprecated.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `OrganizationItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `OrganizationItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_my_organizations_get`

Provenance: Golden OpenAPI contract

Operation ID: `getMyOrganizationsGet`

- Sync: `client.organizations.get_my_organizations_get(timeout=None)`
- Async: `await client.organizations.get_my_organizations_get(timeout=None)`
- Raw payload: `client.organizations.get_my_organizations_get.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/organizations/my`
- Source controller: `IncidentIQ API`

Get my organizations (GET)

Returns the list of organizations the current user is a member of. Use this endpoint to populate a user's organization context without providing filters or request bodies.

**Workflow Example**
1. Call [GET /api/v1.0/organizations/my](#/Organizations/getMyOrganizationsGet) to retrieve memberships for the current user.
2. Extract `Items[].OrganizationId` for downstream calls like [GET /api/v1.0/organizations/{OrganizationId}](#/Organizations/getOrganization).

**Minimal Required Fields**: None.

**Notes**: This API version is deprecated.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `OrganizationListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `OrganizationListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_my_organizations_post`

Provenance: Golden OpenAPI contract

Operation ID: `getMyOrganizationsPost`

- Sync: `client.organizations.get_my_organizations_post(body=None, timeout=None)`
- Async: `await client.organizations.get_my_organizations_post(body=None, timeout=None)`
- Raw payload: `client.organizations.get_my_organizations_post.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/organizations/my`
- Source controller: `IncidentIQ API`

Get my organizations (POST)

Returns organizations the current user is a member of using a filter payload. Use POST when you need DataFilter criteria or want to page and sort results beyond the simple GET behavior.

**Workflow Example**
1. Provide Filters in the request body to narrow the membership list.
2. Call [POST /api/v1.0/organizations/my](#/Organizations/getMyOrganizationsPost) to retrieve the filtered results.
3. Use `Items[].OrganizationId` for subsequent detail or update calls.

**Minimal Required Fields**: Filters are optional, but include at least one filter to avoid unbounded queries.

**Notes**: This API version is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `InlineObject` | `InlineObject` | - |

#### Returns

- Typed call return: `OrganizationListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `OrganizationListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_organization`

Provenance: Golden OpenAPI contract

Operation ID: `getOrganization`

- Sync: `client.organizations.get_organization(organization_id=..., timeout=None)`
- Async: `await client.organizations.get_organization(organization_id=..., timeout=None)`
- Raw payload: `client.organizations.get_organization.raw(organization_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/organizations/{OrganizationId}`
- Source controller: `IncidentIQ API`

Get organization by ID

Retrieves a single organization record by OrganizationId. Use this endpoint to fetch full organization details once you have an ID from search, query, or default organization lookup.

**Prerequisites**
1. **OrganizationId** - Use [GET /api/v1.0/organizations/query](#/Organizations/getOrganizationsByQueryGet) or [GET /api/v1.0/organizations/default](#/Organizations/getDefaultOrganization) and extract `Items[].OrganizationId` or `Item.OrganizationId`.

**Workflow Example**
1. Obtain an OrganizationId from a query or default lookup.
2. Call [GET /api/v1.0/organizations/{OrganizationId}](#/Organizations/getOrganization) to retrieve full details.

**Minimal Required Fields**: OrganizationId path parameter.

**Notes**: This API version is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `organization_id` | `OrganizationId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `OrganizationItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `OrganizationItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_organization_attachments`

Provenance: Golden OpenAPI contract

Operation ID: `getOrganizationAttachments`

- Sync: `client.organizations.get_organization_attachments(organization_id=..., timeout=None)`
- Async: `await client.organizations.get_organization_attachments(organization_id=..., timeout=None)`
- Raw payload: `client.organizations.get_organization_attachments.raw(organization_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/organizations/{OrganizationId}/attachments`
- Source controller: `IncidentIQ API`

Get organization attachments

Retrieves file attachments associated with a specific organization, such as documents or images stored as entity files. Use this to list current attachments before updating or replacing them.

**Prerequisites**
1. **OrganizationId** - Use [GET /api/v1.0/organizations/query](#/Organizations/getOrganizationsByQueryGet) and extract `Items[].OrganizationId`.

**Workflow Example**
1. Obtain the OrganizationId.
2. Call [GET /api/v1.0/organizations/{OrganizationId}/attachments](#/Organizations/getOrganizationAttachments) to list current files.

**Minimal Required Fields**: OrganizationId path parameter.

**Notes**: This API version is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `organization_id` | `OrganizationId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `EntityFileDetailListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `EntityFileDetailListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_organization_type`

Provenance: Golden OpenAPI contract

Operation ID: `getOrganizationType`

- Sync: `client.organizations.get_organization_type(organization_type_id=..., timeout=None)`
- Async: `await client.organizations.get_organization_type(organization_type_id=..., timeout=None)`
- Raw payload: `client.organizations.get_organization_type.raw(organization_type_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/organizations/types/{OrganizationTypeId}`
- Source controller: `IncidentIQ API`

Get organization type by ID

Retrieves a single organization type record by OrganizationTypeId. Use this endpoint to fetch full details for a type once you have an ID from a list or query response.

**Prerequisites**
1. **OrganizationTypeId** - Use [GET /api/v1.0/organizations/types/query](#/Organizations/getOrganizationTypesByQueryGet) and extract `Items[].OrganizationTypeId`.

**Workflow Example**
1. Query for organization types to get an ID.
2. Call [GET /api/v1.0/organizations/types/{OrganizationTypeId}](#/Organizations/getOrganizationType) to retrieve the full record.

**Minimal Required Fields**: OrganizationTypeId path parameter.

**Notes**: This API version is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `organization_type_id` | `OrganizationTypeId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `OrganizationTypeItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `OrganizationTypeItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_organization_types_by_ids`

Provenance: Golden OpenAPI contract

Operation ID: `getOrganizationTypesByIds`

- Sync: `client.organizations.get_organization_types_by_ids(body=..., timeout=None)`
- Async: `await client.organizations.get_organization_types_by_ids(body=..., timeout=None)`
- Raw payload: `client.organizations.get_organization_types_by_ids.raw(body=..., timeout=None)`
- HTTP route: `GET /api/v1.0/organizations/types/ids`
- Source controller: `IncidentIQ API`

Get organization types by IDs

Returns organization type records for a supplied list of OrganizationTypeId values. Use this when you already have IDs from a query and want a compact lookup without additional filtering.

**Prerequisites**
1. **OrganizationTypeId** - Use [GET /api/v1.0/organizations/types/query](#/Organizations/getOrganizationTypesByQueryGet) and extract `Items[].OrganizationTypeId`.

**Workflow Example**
1. Gather OrganizationTypeId values from a query response.
2. Call [GET /api/v1.0/organizations/types/ids](#/Organizations/getOrganizationTypesByIds) with the ID array in the request body.

**Minimal Required Fields**: OrganizationTypeId array in the request body.

**Notes**: This API version is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | - |

#### Returns

- Typed call return: `OrganizationTypeListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `OrganizationTypeListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_organization_types_by_query_get`

Provenance: Golden OpenAPI contract

Operation ID: `getOrganizationTypesByQueryGet`

- Sync: `client.organizations.get_organization_types_by_query_get(top=None, skip=None, timeout=None)`
- Async: `await client.organizations.get_organization_types_by_query_get(top=None, skip=None, timeout=None)`
- Raw payload: `client.organizations.get_organization_types_by_query_get.raw(top=None, skip=None, timeout=None)`
- HTTP route: `GET /api/v1.0/organizations/types/query`
- Source controller: `IncidentIQ API`

Query organization types (GET)

Returns organization types using simple query parameters and paging. Use this endpoint to browse all available types or to obtain OrganizationTypeId values for update, delete, or assignment workflows.

**Workflow Example**
1. Call [GET /api/v1.0/organizations/types/query](#/Organizations/getOrganizationTypesByQueryGet) with $top/$skip to page through results.
2. Extract `Items[].OrganizationTypeId` and pass them to [GET /api/v1.0/organizations/types/ids](#/Organizations/getOrganizationTypesByIds) or [PUT /api/v1.0/organizations/types/ids/update](#/Organizations/updateOrganizationTypesByIds).

**Minimal Required Fields**: None.

**Notes**: This API version is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `top` | `$top` | `query` | `no` | `int` | `-` | - |
| `skip` | `$skip` | `query` | `no` | `int` | `-` | - |

#### Returns

- Typed call return: `OrganizationTypeListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `OrganizationTypeListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_organization_types_by_query_post`

Provenance: Golden OpenAPI contract

Operation ID: `getOrganizationTypesByQueryPost`

- Sync: `client.organizations.get_organization_types_by_query_post(body=None, timeout=None)`
- Async: `await client.organizations.get_organization_types_by_query_post(body=None, timeout=None)`
- Raw payload: `client.organizations.get_organization_types_by_query_post.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/organizations/types/query`
- Source controller: `IncidentIQ API`

Query organization types (POST)

Returns organization types using a filter payload for complex searches. Use this POST variant when you need DataFilter criteria beyond basic paging.

**Workflow Example**
1. Submit filters that target Name, Scope, or Site-specific criteria.
2. Extract `Items[].OrganizationTypeId` and use them in follow-up operations like [DELETE /api/v1.0/organizations/types/ids](#/Organizations/deleteOrganizationTypesByIds).

**Minimal Required Fields**: Filters are optional, but provide at least one filter to avoid unbounded queries.

**Notes**: This API version is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `InlineObject` | `InlineObject` | - |

#### Returns

- Typed call return: `OrganizationTypeListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `OrganizationTypeListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_organization_user`

Provenance: Golden OpenAPI contract

Operation ID: `getOrganizationUser`

- Sync: `client.organizations.get_organization_user(organization_user_id=..., timeout=None)`
- Async: `await client.organizations.get_organization_user(organization_user_id=..., timeout=None)`
- Raw payload: `client.organizations.get_organization_user.raw(organization_user_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/organizations/users/{OrganizationUserId}`
- Source controller: `IncidentIQ API`

Get organization user by ID

Retrieves a single organization-user relationship by OrganizationUserId. Use this endpoint to inspect the membership link between a user and an organization once you already have the relationship ID.

**Prerequisites**
1. **OrganizationUserId** - Use [GET /api/v1.0/organizations/users/query](#/Organizations/getOrganizationUsersByQueryGet) and extract `Items[].OrganizationUserId`.

**Workflow Example**
1. Query for organization-user relationships to obtain an ID.
2. Call [GET /api/v1.0/organizations/users/{OrganizationUserId}](#/Organizations/getOrganizationUser) to fetch the full relationship record.

**Minimal Required Fields**: OrganizationUserId path parameter.

**Notes**: This API version is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `organization_user_id` | `OrganizationUserId` | `path` | `yes` | `str` | `-` | UUID of the organization-user relationship. Obtain via [POST /api/v1.0/users](#/Users/searchUsers), extract `Items[].UserId`. |

#### Returns

- Typed call return: `OrganizationUserItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `OrganizationUserItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_organization_users_by_ids`

Provenance: Golden OpenAPI contract

Operation ID: `getOrganizationUsersByIds`

- Sync: `client.organizations.get_organization_users_by_ids(body=..., timeout=None)`
- Async: `await client.organizations.get_organization_users_by_ids(body=..., timeout=None)`
- Raw payload: `client.organizations.get_organization_users_by_ids.raw(body=..., timeout=None)`
- HTTP route: `GET /api/v1.0/organizations/users/ids`
- Source controller: `IncidentIQ API`

Get organization users by IDs

Returns organization-user relationship records for a supplied list of OrganizationUserId values. Use this endpoint when you already have IDs from a query or previous workflow and need the full relationship payloads.

**Prerequisites**
1. **OrganizationUserId** - Use [GET /api/v1.0/organizations/users/query](#/Organizations/getOrganizationUsersByQueryGet) and extract `Items[].OrganizationUserId`.

**Workflow Example**
1. Query for relationships to get IDs.
2. Call [GET /api/v1.0/organizations/users/ids](#/Organizations/getOrganizationUsersByIds) with the ID array in the request body.

**Minimal Required Fields**: OrganizationUserId array in the request body.

**Notes**: This API version is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | - |

#### Returns

- Typed call return: `OrganizationUserListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `OrganizationUserListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_organization_users_by_query_get`

Provenance: Golden OpenAPI contract

Operation ID: `getOrganizationUsersByQueryGet`

- Sync: `client.organizations.get_organization_users_by_query_get(organization_id=None, top=None, skip=None, timeout=None)`
- Async: `await client.organizations.get_organization_users_by_query_get(organization_id=None, top=None, skip=None, timeout=None)`
- Raw payload: `client.organizations.get_organization_users_by_query_get.raw(organization_id=None, top=None, skip=None, timeout=None)`
- HTTP route: `GET /api/v1.0/organizations/users/query`
- Source controller: `IncidentIQ API`

Query organization users (GET)

Returns organization-user relationships using simple query parameters and paging. Use this endpoint when you need a quick list of users for one organization or when you want to build an ID set for bulk updates/deletes.

**Workflow Example**
1. Call [GET /api/v1.0/organizations/users/query](#/Organizations/getOrganizationUsersByQueryGet) with OrganizationId (plus $top/$skip) to scope results.
2. Extract `Items[].OrganizationUserId` and pass them to [PUT /api/v1.0/organizations/users/ids/update](#/Organizations/updateOrganizationUsersByIds) or [DELETE /api/v1.0/organizations/users/ids](#/Organizations/deleteOrganizationUsersByIds).

**Minimal Required Fields**: OrganizationId is strongly recommended to scope the query.

**Notes**: This API version is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `organization_id` | `OrganizationId` | `query` | `no` | `str` | `-` | - |
| `top` | `$top` | `query` | `no` | `int` | `-` | - |
| `skip` | `$skip` | `query` | `no` | `int` | `-` | - |

#### Returns

- Typed call return: `OrganizationUserListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `OrganizationUserListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_organization_users_by_query_post`

Provenance: Golden OpenAPI contract

Operation ID: `getOrganizationUsersByQueryPost`

- Sync: `client.organizations.get_organization_users_by_query_post(body=None, timeout=None)`
- Async: `await client.organizations.get_organization_users_by_query_post(body=None, timeout=None)`
- Raw payload: `client.organizations.get_organization_users_by_query_post.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/organizations/users/query`
- Source controller: `IncidentIQ API`

Query organization users (POST)

Returns organization-user relationships using a filter payload for more complex criteria than query params allow. Use POST when you need server-side filtering (DataFilter) across user or organization attributes, or when your filter set is too large for a URL.

**Workflow Example**
1. Submit filters to narrow the relationship set (include OrganizationId in filters when appropriate).
2. Extract `Items[].OrganizationUserId` for follow-up calls like [PUT /api/v1.0/organizations/users/ids/update](#/Organizations/updateOrganizationUsersByIds).

**Minimal Required Fields**: Filters are optional, but include at least one filter to avoid unbounded queries.

**Notes**: This API version is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `InlineObject` | `InlineObject` | - |

#### Returns

- Typed call return: `OrganizationUserListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `OrganizationUserListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_organizations_by_ids`

Provenance: Golden OpenAPI contract

Operation ID: `getOrganizationsByIds`

- Sync: `client.organizations.get_organizations_by_ids(body=..., timeout=None)`
- Async: `await client.organizations.get_organizations_by_ids(body=..., timeout=None)`
- Raw payload: `client.organizations.get_organizations_by_ids.raw(body=..., timeout=None)`
- HTTP route: `GET /api/v1.0/organizations/ids`
- Source controller: `IncidentIQ API`

Get organizations by IDs

Returns organizations for the supplied list of OrganizationId values. Use this endpoint when you already have IDs from a query or search and need the full organization records.

**Prerequisites**
1. **OrganizationId** - Use [GET /api/v1.0/organizations/query](#/Organizations/getOrganizationsByQueryGet) and extract `Items[].OrganizationId`.

**Workflow Example**
1. Query for organizations to gather IDs.
2. Call [GET /api/v1.0/organizations/ids](#/Organizations/getOrganizationsByIds) with the ID array in the request body.

**Minimal Required Fields**: OrganizationId array in the request body.

**Notes**: This API version is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | - |

#### Returns

- Typed call return: `OrganizationListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `OrganizationListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_organizations_by_query_get`

Provenance: Golden OpenAPI contract

Operation ID: `getOrganizationsByQueryGet`

- Sync: `client.organizations.get_organizations_by_query_get(top=None, skip=None, timeout=None)`
- Async: `await client.organizations.get_organizations_by_query_get(top=None, skip=None, timeout=None)`
- Raw payload: `client.organizations.get_organizations_by_query_get.raw(top=None, skip=None, timeout=None)`
- HTTP route: `GET /api/v1.0/organizations/query`
- Source controller: `IncidentIQ API`

Query organizations (GET)

Returns organizations using simple query parameters and paging. Use this endpoint to browse the organization catalog, fetch IDs for downstream operations, or build a working set for batch updates/deletes.

**Workflow Example**
1. Call [GET /api/v1.0/organizations/query](#/Organizations/getOrganizationsByQueryGet) with $top/$skip to page through results.
2. Extract `Items[].OrganizationId` and use them with [PUT /api/v1.0/organizations/ids/update](#/Organizations/updateOrganizationsByIds) or [DELETE /api/v1.0/organizations/ids](#/Organizations/deleteOrganizationsByIds).

**Minimal Required Fields**: None.

**Notes**: This API version is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `top` | `$top` | `query` | `no` | `int` | `-` | - |
| `skip` | `$skip` | `query` | `no` | `int` | `-` | - |

#### Returns

- Typed call return: `OrganizationListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `OrganizationListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_organizations_by_query_post`

Provenance: Golden OpenAPI contract

Operation ID: `getOrganizationsByQueryPost`

- Sync: `client.organizations.get_organizations_by_query_post(body=None, timeout=None)`
- Async: `await client.organizations.get_organizations_by_query_post(body=None, timeout=None)`
- Raw payload: `client.organizations.get_organizations_by_query_post.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/organizations/query`
- Source controller: `IncidentIQ API`

Query organizations (POST)

Returns organizations using a filter payload for advanced query scenarios. Use POST when you need DataFilter criteria beyond basic paging (for example, filtering by name, type, or status).

**Workflow Example**
1. Submit filters that describe your target organization set.
2. Extract `Items[].OrganizationId` for follow-up calls like [GET /api/v1.0/organizations/ids](#/Organizations/getOrganizationsByIds).

**Minimal Required Fields**: Filters are optional, but include at least one filter to avoid unbounded queries.

**Notes**: This API version is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `InlineObject` | `InlineObject` | - |

#### Returns

- Typed call return: `OrganizationListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `OrganizationListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_organizations_for_contact_email`

Provenance: Golden OpenAPI contract

Operation ID: `getOrganizationsForContactEmail`

- Sync: `client.organizations.get_organizations_for_contact_email(email=..., timeout=None)`
- Async: `await client.organizations.get_organizations_for_contact_email(email=..., timeout=None)`
- Raw payload: `client.organizations.get_organizations_for_contact_email.raw(email=..., timeout=None)`
- HTTP route: `GET /api/v1.0/organizations/for/contact`
- Source controller: `IncidentIQ API`

Get organizations by contact email

Returns organizations where the provided email address appears as a contact. Use this to audit organization contact assignments or to identify the organizations linked to a specific contact email.

**Workflow Example**
1. Provide the contact `email` query parameter.
2. Call [GET /api/v1.0/organizations/for/contact](#/Organizations/getOrganizationsForContactEmail) to retrieve matching organizations.
3. Extract `Items[].OrganizationId` for follow-up actions like [GET /api/v1.0/organizations/{OrganizationId}](#/Organizations/getOrganization).

**Minimal Required Fields**: email query parameter.

**Notes**: This API version is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `email` | `email` | `query` | `yes` | `str` | `-` | Contact email address. |

#### Returns

- Typed call return: `OrganizationListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `OrganizationListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `save_organization_attachments`

Provenance: Golden OpenAPI contract

Operation ID: `saveOrganizationAttachments`

- Sync: `client.organizations.save_organization_attachments(organization_id=..., body=..., timeout=None)`
- Async: `await client.organizations.save_organization_attachments(organization_id=..., body=..., timeout=None)`
- Raw payload: `client.organizations.save_organization_attachments.raw(organization_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/organizations/{OrganizationId}/attachments`
- Source controller: `IncidentIQ API`

Save organization attachments

Replaces the attachment list for an organization with the provided file metadata. Use this endpoint to add or remove organization attachments in bulk by supplying the full desired FileData list.

**Prerequisites**
1. **OrganizationId** - Use [GET /api/v1.0/organizations/query](#/Organizations/getOrganizationsByQueryGet) and extract `Items[].OrganizationId`.
2. **FileData** - Build using file metadata from your upload workflow or existing attachment details.

**Workflow Example**
1. Fetch current attachments with [GET /api/v1.0/organizations/{OrganizationId}/attachments](#/Organizations/getOrganizationAttachments).
2. Build the new FileData array, adding/removing items as needed.
3. Call [POST /api/v1.0/organizations/{OrganizationId}/attachments](#/Organizations/saveOrganizationAttachments) with FileData.

**Minimal Required Fields**: FileData array in the request body.

**Notes**: This API version is deprecated; any files not included in FileData are removed.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `organization_id` | `OrganizationId` | `path` | `yes` | `str` | `-` | - |
| `body` | `body` | `body` | `yes` | `UpdateEntityFileDetailsRequest` | `UpdateEntityFileDetailsRequest` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `search_organizations`

Provenance: Golden OpenAPI contract

Operation ID: `searchOrganizations`

- Sync: `client.organizations.search_organizations(query=..., timeout=None)`
- Async: `await client.organizations.search_organizations(query=..., timeout=None)`
- Raw payload: `client.organizations.search_organizations.raw(query=..., timeout=None)`
- HTTP route: `GET /api/v1.0/organizations/search`
- Source controller: `IncidentIQ API`

Search organizations by keyword

Searches organizations by keyword and returns matches where the current user is not already a member. Use this to discover organizations for membership requests or onboarding workflows.

**Workflow Example**
1. Provide a `query` string (name, partial name, or keyword).
2. Call [GET /api/v1.0/organizations/search](#/Organizations/searchOrganizations) to retrieve matching organizations.
3. Use `Items[].OrganizationId` for follow-up membership creation with [POST /api/v1.0/organizations/users](#/Organizations/createOrganizationUser).

**Minimal Required Fields**: query parameter.

**Notes**: This API version is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `query` | `query` | `query` | `yes` | `str` | `-` | Search keyword. |

#### Returns

- Typed call return: `OrganizationListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `OrganizationListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_organization`

Provenance: Golden OpenAPI contract

Operation ID: `updateOrganization`

- Sync: `client.organizations.update_organization(organization_id=..., body=..., timeout=None)`
- Async: `await client.organizations.update_organization(organization_id=..., body=..., timeout=None)`
- Raw payload: `client.organizations.update_organization.raw(organization_id=..., body=..., timeout=None)`
- HTTP route: `PUT /api/v1.0/organizations/{OrganizationId}/update`
- Source controller: `IncidentIQ API`

Update organization by ID

Updates a single organization record by OrganizationId. Use this when you need to change organization metadata such as name, contact details, or insurance fields for an existing organization.

**Prerequisites**
1. **OrganizationId** - Use [GET /api/v1.0/organizations/query](#/Organizations/getOrganizationsByQueryGet) and extract `Items[].OrganizationId`.

**Workflow Example**
1. Retrieve the current organization record to identify fields to change.
2. Call [PUT /api/v1.0/organizations/{OrganizationId}/update](#/Organizations/updateOrganization) with the updated fields.

**Minimal Required Fields**: OrganizationId path parameter plus the fields you intend to update.

**Notes**: This API version is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `organization_id` | `OrganizationId` | `path` | `yes` | `str` | `-` | - |
| `body` | `body` | `body` | `yes` | `UpdateOrganizationRequest` | `UpdateOrganizationRequest` | - |

#### Returns

- Typed call return: `OrganizationsDomainUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `OrganizationsDomainUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_organization_type`

Provenance: Golden OpenAPI contract

Operation ID: `updateOrganizationType`

- Sync: `client.organizations.update_organization_type(organization_type_id=..., body=..., timeout=None)`
- Async: `await client.organizations.update_organization_type(organization_type_id=..., body=..., timeout=None)`
- Raw payload: `client.organizations.update_organization_type.raw(organization_type_id=..., body=..., timeout=None)`
- HTTP route: `PUT /api/v1.0/organizations/types/{OrganizationTypeId}/update`
- Source controller: `IncidentIQ API`

Update organization type by ID

Updates the name, scope, or site association for a single organization type. Use this when you need to rename a type or adjust its scope (Global vs Site).

**Prerequisites**
1. **OrganizationTypeId** - Use [GET /api/v1.0/organizations/types/query](#/Organizations/getOrganizationTypesByQueryGet) and extract `Items[].OrganizationTypeId`.

**Workflow Example**
1. Identify the OrganizationTypeId to modify.
2. Send [PUT /api/v1.0/organizations/types/{OrganizationTypeId}/update](#/Organizations/updateOrganizationType) with the updated fields.

**Minimal Required Fields**: OrganizationTypeId path parameter; include fields you intend to update (Name, Scope, SiteId).

**Notes**: This API version is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `organization_type_id` | `OrganizationTypeId` | `path` | `yes` | `str` | `-` | - |
| `body` | `body` | `body` | `yes` | `UpdateOrganizationTypeRequest` | `UpdateOrganizationTypeRequest` | - |

#### Returns

- Typed call return: `OrganizationsDomainUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `OrganizationsDomainUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_organization_types_by_ids`

Provenance: Golden OpenAPI contract

Operation ID: `updateOrganizationTypesByIds`

- Sync: `client.organizations.update_organization_types_by_ids(body=..., timeout=None)`
- Async: `await client.organizations.update_organization_types_by_ids(body=..., timeout=None)`
- Raw payload: `client.organizations.update_organization_types_by_ids.raw(body=..., timeout=None)`
- HTTP route: `PUT /api/v1.0/organizations/types/ids/update`
- Source controller: `IncidentIQ API`

Update organization types by IDs

Updates multiple organization types using an array of update objects. Use this when you need to rename or re-scope several types in one request and already know their IDs.

**Prerequisites**
1. **OrganizationTypeId** - Use [GET /api/v1.0/organizations/types/query](#/Organizations/getOrganizationTypesByQueryGet) and extract `Items[].OrganizationTypeId`.

**Workflow Example**
1. Build an array where each item includes OrganizationTypeId and updated fields.
2. Call [PUT /api/v1.0/organizations/types/ids/update](#/Organizations/updateOrganizationTypesByIds).

**Minimal Required Fields**: OrganizationTypeId plus fields to update in each array item.

**Notes**: This API version is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | - |

#### Returns

- Typed call return: `OrganizationsDomainBatchUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `OrganizationsDomainBatchUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_organization_types_by_query`

Provenance: Golden OpenAPI contract

Operation ID: `updateOrganizationTypesByQuery`

- Sync: `client.organizations.update_organization_types_by_query(body=..., timeout=None)`
- Async: `await client.organizations.update_organization_types_by_query(body=..., timeout=None)`
- Raw payload: `client.organizations.update_organization_types_by_query.raw(body=..., timeout=None)`
- HTTP route: `PUT /api/v1.0/organizations/types/query/update`
- Source controller: `IncidentIQ API`

Update organization types by query

Batch-updates organization types that match the supplied filter criteria. Use this when you need to apply the same change (such as renaming or scope adjustments) across multiple types.

**Workflow Example**
1. Build a filter set that targets the types you want to update.
2. Provide the Update payload and call [PUT /api/v1.0/organizations/types/query/update](#/Organizations/updateOrganizationTypesByQuery).

**Minimal Required Fields**: Update payload; Filters recommended to scope the update set.

**Notes**: This API version is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `UpdateOrganizationTypesRequest` | `UpdateOrganizationTypesRequest` | - |

#### Returns

- Typed call return: `OrganizationsDomainBatchUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `OrganizationsDomainBatchUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_organization_user`

Provenance: Golden OpenAPI contract

Operation ID: `updateOrganizationUser`

- Sync: `client.organizations.update_organization_user(organization_user_id=..., body=..., timeout=None)`
- Async: `await client.organizations.update_organization_user(organization_user_id=..., body=..., timeout=None)`
- Raw payload: `client.organizations.update_organization_user.raw(organization_user_id=..., body=..., timeout=None)`
- HTTP route: `PUT /api/v1.0/organizations/users/{OrganizationUserId}/update`
- Source controller: `IncidentIQ API`

Update organization user by ID

Updates a single organization-user relationship by OrganizationUserId. Use this endpoint when you need to change the OrganizationId or UserId on an existing relationship and you have the specific relationship ID.

**Prerequisites**
1. **OrganizationUserId** - Use [GET /api/v1.0/organizations/users/query](#/Organizations/getOrganizationUsersByQueryGet) and extract `Items[].OrganizationUserId`.

**Workflow Example**
1. Query for the relationship and capture OrganizationUserId.
2. Submit [PUT /api/v1.0/organizations/users/{OrganizationUserId}/update](#/Organizations/updateOrganizationUser) with the fields to update.

**Minimal Required Fields**: OrganizationUserId path parameter plus the fields you intend to update (OrganizationId or UserId).

**Notes**: This API version is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `organization_user_id` | `OrganizationUserId` | `path` | `yes` | `str` | `-` | - |
| `body` | `body` | `body` | `yes` | `UpdateOrganizationUserRequest` | `UpdateOrganizationUserRequest` | - |

#### Returns

- Typed call return: `OrganizationsDomainUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `OrganizationsDomainUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_organization_users_by_ids`

Provenance: Golden OpenAPI contract

Operation ID: `updateOrganizationUsersByIds`

- Sync: `client.organizations.update_organization_users_by_ids(body=..., timeout=None)`
- Async: `await client.organizations.update_organization_users_by_ids(body=..., timeout=None)`
- Raw payload: `client.organizations.update_organization_users_by_ids.raw(body=..., timeout=None)`
- HTTP route: `PUT /api/v1.0/organizations/users/ids/update`
- Source controller: `IncidentIQ API`

Update organization users by IDs

Updates organization-user relationships for a list of OrganizationUserId values. Use this when you need to correct or replace the OrganizationId/UserId linkage on existing relationships and you already have the IDs.

**Prerequisites**
1. **OrganizationUserId** - Use [GET /api/v1.0/organizations/users/query](#/Organizations/getOrganizationUsersByQueryGet) and extract `Items[].OrganizationUserId`.

**Workflow Example**
1. Query for relationship IDs that need changes.
2. Build an array of update objects that include OrganizationUserId and the fields to change.
3. Call [PUT /api/v1.0/organizations/users/ids/update](#/Organizations/updateOrganizationUsersByIds).

**Minimal Required Fields**: OrganizationUserId plus the fields you intend to update.

**Notes**: This API version is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | - |

#### Returns

- Typed call return: `OrganizationsDomainBatchUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `OrganizationsDomainBatchUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_organization_users_by_query`

Provenance: Golden OpenAPI contract

Operation ID: `updateOrganizationUsersByQuery`

- Sync: `client.organizations.update_organization_users_by_query(body=..., timeout=None)`
- Async: `await client.organizations.update_organization_users_by_query(body=..., timeout=None)`
- Raw payload: `client.organizations.update_organization_users_by_query.raw(body=..., timeout=None)`
- HTTP route: `PUT /api/v1.0/organizations/users/query/update`
- Source controller: `IncidentIQ API`

Update organization users by query

Batch-updates organization-user relationships that match the provided filter criteria. Use this endpoint when you want to apply the same update across a set of relationships without specifying each OrganizationUserId individually.

**Workflow Example**
1. Build Filters (or provide OrganizationId) to scope the relationship set.
2. Provide the Update object with the fields to change.
3. Call [PUT /api/v1.0/organizations/users/query/update](#/Organizations/updateOrganizationUsersByQuery) to apply the batch update.

**Minimal Required Fields**: Update payload; Filters or OrganizationId recommended to scope the update set.

**Notes**: This API version is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `UpdateOrganizationUsersRequest` | `UpdateOrganizationUsersRequest` | - |

#### Returns

- Typed call return: `OrganizationsDomainBatchUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `OrganizationsDomainBatchUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_organizations_by_ids`

Provenance: Golden OpenAPI contract

Operation ID: `updateOrganizationsByIds`

- Sync: `client.organizations.update_organizations_by_ids(body=..., timeout=None)`
- Async: `await client.organizations.update_organizations_by_ids(body=..., timeout=None)`
- Raw payload: `client.organizations.update_organizations_by_ids.raw(body=..., timeout=None)`
- HTTP route: `PUT /api/v1.0/organizations/ids/update`
- Source controller: `IncidentIQ API`

Update organizations by IDs

Updates multiple organizations using an array of update objects. Use this when you need to change the same fields across several organizations and already know their IDs.

**Prerequisites**
1. **OrganizationId** - Use [GET /api/v1.0/organizations/query](#/Organizations/getOrganizationsByQueryGet) and extract `Items[].OrganizationId`.

**Workflow Example**
1. Build an array where each item includes OrganizationId and the updated fields.
2. Call [PUT /api/v1.0/organizations/ids/update](#/Organizations/updateOrganizationsByIds) to apply changes.

**Minimal Required Fields**: OrganizationId plus the fields you intend to update in each array item.

**Notes**: This API version is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | - |

#### Returns

- Typed call return: `OrganizationsDomainBatchUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `OrganizationsDomainBatchUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_organizations_by_query`

Provenance: Golden OpenAPI contract

Operation ID: `updateOrganizationsByQuery`

- Sync: `client.organizations.update_organizations_by_query(body=..., timeout=None)`
- Async: `await client.organizations.update_organizations_by_query(body=..., timeout=None)`
- Raw payload: `client.organizations.update_organizations_by_query.raw(body=..., timeout=None)`
- HTTP route: `PUT /api/v1.0/organizations/query/update`
- Source controller: `IncidentIQ API`

Update organizations by query

Batch-updates organizations that match the provided filter criteria. Use this endpoint to apply the same field updates across a set of organizations without specifying each ID individually.

**Workflow Example**
1. Build a filter set that targets the organizations you want to update.
2. Provide the Update payload and call [PUT /api/v1.0/organizations/query/update](#/Organizations/updateOrganizationsByQuery).

**Minimal Required Fields**: Update payload; Filters recommended to scope the update set.

**Notes**: This API version is deprecated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `UpdateOrganizationsRequest` | `UpdateOrganizationsRequest` | - |

#### Returns

- Typed call return: `OrganizationsDomainBatchUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `OrganizationsDomainBatchUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
