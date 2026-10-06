# `sites` Golden Namespace

Sync client access: `client.sites`

Async client access: `client.sites` with `await` on method calls.

These methods are Golden because they come from the bundled Incident IQ OpenAPI contract.

## Methods

### `get_my_site_settings`

Provenance: Golden OpenAPI contract

Operation ID: `getMySiteSettings`

- Sync: `client.sites.get_my_site_settings(timeout=None)`
- Async: `await client.sites.get_my_site_settings(timeout=None)`
- Raw payload: `client.sites.get_my_site_settings.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/sites/my/settings`
- Source controller: `IncidentIQ API`

Get current site settings

Retrieves configuration settings for the authenticated user's current site context. This endpoint returns site-wide settings including workflow types, entity types, priority levels, and other configuration data needed by client applications.

**Use Cases**
- Bootstrap client applications with site-specific configuration on startup
- Cache site settings locally to reduce API calls during session
- Retrieve entity type UUIDs needed for creating tickets, assets, and other records
- Look up priority level mappings for ticket prioritization logic

**Key Response Fields**
- `SiteId` - UUID for the current site, used in cross-site operations
- `ProductId` - Licensed product identifier
- `FileTypes` - Map of file type names to IDs for attachment uploads
- `WorkflowApprovalTypes` - UUIDs for workflow approval actions (Approve, RequestInfo)
- `EntityTypes` - Map of entity names (Assets, Tickets) to their UUIDs
- `PriorityLevels[]` - Array of priority configurations with min/max score ranges

**Workflow Example**
1. Call this endpoint on application startup to initialize configuration
2. Cache `EntityTypes.Tickets` UUID for use in [POST /api/v1.0/tickets/new](#/Tickets/createTicket)
3. Use `PriorityLevels[]` to display appropriate priority options in forms

**Related Endpoints**: Use [GET /api/v1.0/sites/{SiteId}/settings](#/Sites/getSiteSettingsById) to retrieve settings for a specific site by ID.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `ItemGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_role_by_id`

Provenance: Golden OpenAPI contract

Operation ID: `getRoleById`

- Sync: `client.sites.get_role_by_id(role_id=..., timeout=None)`
- Async: `await client.sites.get_role_by_id(role_id=..., timeout=None)`
- Raw payload: `client.sites.get_role_by_id.raw(role_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/sites/roles/{RoleId}`
- Source controller: `IncidentIQ API`

Get role by ID

Retrieves detailed information about a specific security role identified by its UUID, including metadata about user assignments and editability.

**Prerequisites**
1. **RoleId** - Use [GET /api/v1.0/sites/roles](#/Sites/listRoles) to list all roles. Extract `Items[].RoleId` from the response.

**Use Cases**
- Display role details in a role management interface
- Verify role configuration before assigning to users
- Check user counts and editability constraints for a specific role

**Response Fields**
- `RoleId`, `RoleName` - Role identifier and display name
- `Portal` - Portal access: 1=Requestor, 2=Agent, 3=iiQAdmin
- `IsEditable` - Whether the role's permissions can be modified
- `CanBeDeleted` - Whether the role can be removed (system roles cannot)
- `Users` - Count of users currently assigned to this role
- `CreatedDate`, `ModifiedDate` - Audit timestamps

**Workflow Example**
1. List all roles: [GET /api/v1.0/sites/roles](#/Sites/listRoles) → find target `RoleId`
2. Get role details: [GET /api/v1.0/sites/roles/{RoleId}](#/Sites/getRoleById)

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `role_id` | `RoleId` | `path` | `yes` | `str` | `-` | Unique identifier for the role. |

#### Returns

- Typed call return: `ItemGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_site_by_url`

Provenance: Golden OpenAPI contract

Operation ID: `getSiteByUrl`

- Sync: `client.sites.get_site_by_url(site_url=..., timeout=None)`
- Async: `await client.sites.get_site_by_url(site_url=..., timeout=None)`
- Raw payload: `client.sites.get_site_by_url.raw(site_url=..., timeout=None)`
- HTTP route: `GET /api/v1.0/sites/{siteUrl}`
- Source controller: `IncidentIQ API`

Get site configuration

Retrieves full configuration details for a district site identified by its hostname (e.g., `demo.incidentiq.com`). Use this endpoint to inspect licensed products, installed apps, and global settings that drive the tenant experience.

**Use Cases**
- Bootstrap applications by discovering tenant configuration from hostname
- Audit licensed products and installed integrations for a district
- Retrieve system user IDs and time zone settings for automation scripts
- Build multi-tenant applications that adapt behavior based on site configuration

**Key Response Fields**
- `SiteId` - UUID for the site, used in subsequent API calls
- `Domain`, `DomainWithProtocol` - Hostname and full URL for the tenant
- `TimeZone`, `IanaTimeZone` - Time zone configuration (e.g., "Eastern Standard Time", "America/New_York")
- `LicensedProducts[]` - Array of licensed modules (Ticketing, Facilities, etc.) with tier information
- `InstalledApps[]` - Third-party integrations (SSO providers, MDM connectors) with install dates
- `Status` - Current site lifecycle status (Testing, Production, Onboarding)
- `Settings` - Nested configuration object with entity types, portals, and custom settings

**Workflow Example**
1. Look up site by hostname: [GET /api/v1.0/sites/{siteUrl}](#/Sites/getSiteByUrl) → extract `SiteId`
2. Use `SiteId` for site-specific operations like [GET /api/v1.0/sites/{SiteId}/settings](#/Sites/getSiteSettingsById)
3. Check `LicensedProducts[]` to enable/disable features based on licensing

**Notes**: The `siteUrl` parameter is the hostname only, without protocol (e.g., `demo.incidentiq.com`, not `https://demo.incidentiq.com`).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `site_url` | `siteUrl` | `path` | `yes` | `str` | `-` | Hostname for the district environment, without the protocol (for example, `demo.incidentiq.com`). |

#### Returns

- Typed call return: `SiteDetailsResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `SiteDetailsResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_site_settings_by_id`

Provenance: Golden OpenAPI contract

Operation ID: `getSiteSettingsById`

- Sync: `client.sites.get_site_settings_by_id(site_id=..., timeout=None)`
- Async: `await client.sites.get_site_settings_by_id(site_id=..., timeout=None)`
- Raw payload: `client.sites.get_site_settings_by_id.raw(site_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/sites/{SiteId}/settings`
- Source controller: `IncidentIQ API`

Get site settings by ID

Retrieves configuration settings for a specific site identified by its UUID. Returns site-wide configuration data including workflow types, entity types, portal mappings, and custom settings.

**Prerequisites**
1. **SiteId** - Obtain from [GET /api/v1.0/sites/my/settings](#/Sites/getMySiteSettings) (extract `Item.SiteId`) or from [GET /api/v1.0/sites/{siteUrl}](#/Sites/getSiteByUrl) (extract `Item.SiteId`).

**Use Cases**
- Retrieve settings for a site other than the user's current context
- Build multi-site administration dashboards that compare configurations
- Cache site settings for cross-site operations in integrations
- Validate site configuration before performing bulk updates

**Key Response Fields**
- `SiteId`, `ProductId` - Site and product identifiers
- `Name` - District display name
- `FileTypes` - Map of file type names to numeric IDs
- `WorkflowApprovalTypes` - UUIDs for workflow approval actions
- `Portals` - Map of portal names to numeric IDs (Requestor=1, Agent=2, iiQAdmin=3)
- `EntityTypes` - Map of entity names to their UUIDs for Assets, Tickets, etc.

**Workflow Example**
1. Get current site: [GET /api/v1.0/sites/my/settings](#/Sites/getMySiteSettings) → extract `SiteId`
2. Retrieve settings by ID: [GET /api/v1.0/sites/{SiteId}/settings](#/Sites/getSiteSettingsById)

**Related Endpoints**: For current site settings without specifying ID, use [GET /api/v1.0/sites/my/settings](#/Sites/getMySiteSettings).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `site_id` | `SiteId` | `path` | `yes` | `str` | `-` | Unique identifier for the site. |

#### Returns

- Typed call return: `ItemGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_roles`

Provenance: Golden OpenAPI contract

Operation ID: `listRoles`

- Sync: `client.sites.list_roles(top=None, skip=None, orderby=None, timeout=None)`
- Async: `await client.sites.list_roles(top=None, skip=None, orderby=None, timeout=None)`
- Raw payload: `client.sites.list_roles.raw(top=None, skip=None, orderby=None, timeout=None)`
- HTTP route: `GET /api/v1.0/sites/roles`
- Source controller: `IncidentIQ API`

List roles

Retrieves all security roles defined for the current site. Roles control user permissions and determine which portal (Requestor, Agent, iiQAdmin) users can access.

**Use Cases**
- Populate role selection dropdowns when creating or updating users
- Audit role assignments and user counts across your organization
- Build permission management interfaces for administrators

**Response Fields**
- `RoleId` - UUID used when assigning roles to users via [POST /api/v1.0/users/{UserId}](#/Users/updateUser)
- `RoleName` - Display name (e.g., "Administrator", "Agent", "Requestor")
- `Portal` - Portal access level: 1=Requestor, 2=Agent, 3=iiQAdmin
- `Visibility` - Role visibility scope: 0=Hidden, 1=Visible
- `Users` - Count of users currently assigned to this role

**Workflow Example**
1. List roles: [GET /api/v1.0/sites/roles](#/Sites/listRoles) → extract `RoleId` values
2. Assign role to user: [POST /api/v1.0/users/{UserId}](#/Users/updateUser) with `RoleId` in request body

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `top` | `$top` | `query` | `no` | `int` | `-` | Maximum number of roles to return. Defaults to 1000. |
| `skip` | `$skip` | `query` | `no` | `int` | `-` | Number of roles to skip for pagination. |
| `orderby` | `$orderby` | `query` | `no` | `str` | `-` | Field to sort results by. Defaults to RoleName ascending. |

#### Returns

- Typed call return: `ListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_roles_filtered`

Provenance: Golden OpenAPI contract

Operation ID: `listRolesFiltered`

- Sync: `client.sites.list_roles_filtered(body=None, timeout=None)`
- Async: `await client.sites.list_roles_filtered(body=None, timeout=None)`
- Raw payload: `client.sites.list_roles_filtered.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/sites/roles`
- Source controller: `IncidentIQ API`

List roles with filters

Retrieves security roles with advanced filtering capabilities. The POST method allows complex filter criteria and pagination options to be passed in the request body.

**Use Cases**
- Search for roles by name or portal type with specific criteria
- Implement server-side filtering for role management interfaces
- Retrieve roles matching multiple conditions in a single request

**Request Body Options**
- `Filters` - Array of filter conditions (field, operator, value)
- `Paging` - Pagination settings (`PageIndex`, `PageSize`)
- `Sorts` - Sorting criteria (field name, direction)

**Common Filters**
- Filter by portal: `{ "Field": "Portal", "Operator": "=", "Value": 2 }` for Agent roles
- Filter by active status: `{ "Field": "IsActive", "Operator": "=", "Value": true }`

**Related Endpoints**: Use [GET /api/v1.0/sites/roles](#/Sites/listRoles) for simple listing without filters, or [GET /api/v1.0/sites/roles/with-permission-policies](#/Sites/listRolesWithPermissionPolicies) to include permission details.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `RequestOptions` | `RequestOptions` | Optional filtering and pagination options. |

#### Returns

- Typed call return: `ListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_roles_with_permission_policies`

Provenance: Golden OpenAPI contract

Operation ID: `listRolesWithPermissionPolicies`

- Sync: `client.sites.list_roles_with_permission_policies(top=None, skip=None, timeout=None)`
- Async: `await client.sites.list_roles_with_permission_policies(top=None, skip=None, timeout=None)`
- Raw payload: `client.sites.list_roles_with_permission_policies.raw(top=None, skip=None, timeout=None)`
- HTTP route: `GET /api/v1.0/sites/roles/with-permission-policies`
- Source controller: `IncidentIQ API`

List roles with permission policies

Retrieves all roles along with their associated permission policy definitions, returning each role's metadata plus the full policy list that drives authorization behavior. Use this for permission audits, admin role management screens, or when you need to map which actions are allowed for a given role without making separate policy calls.

**Workflow Example**
1. Call [GET /api/v1.0/sites/roles/with-permission-policies](#/Sites/listRolesWithPermissionPolicies) to load every role and its policies.
2. Page results with `$top`/`$skip` when your tenant has a large role catalog.
3. Use the returned `RoleId` and `PermissionPolicies[]` data to populate admin UI or export audit reports.

**Minimal Required Fields**: none.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `top` | `$top` | `query` | `no` | `int` | `-` | Maximum number of roles to return. |
| `skip` | `$skip` | `query` | `no` | `int` | `-` | Number of roles to skip for pagination. |

#### Returns

- Typed call return: `ListGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_sites`

Provenance: Golden OpenAPI contract

Operation ID: `listSites`

- Sync: `client.sites.list_sites(timeout=None)`
- Async: `await client.sites.list_sites(timeout=None)`
- Raw payload: `client.sites.list_sites.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/sites`
- Source controller: `IncidentIQ API`

List all sites

Retrieves all tenant sites in the IncidentIQ platform. This endpoint is restricted to Global Administrators and returns a paginated list of Site objects.

**Authentication Requirements:**
- Requires Global Administrator privileges (`GlobalAdminOnly: true`)
- Standard user authentication will return 403 Forbidden

**Use Cases:**
- Build multi-tenant administration dashboards
- Populate site selection dropdowns for cross-site operations
- Audit site configurations across your organization
- Obtain SiteIds for use in site-specific API calls

**Response Fields:**
- `SiteId` - Unique identifier for the site
- `Name` - Display name of the site (e.g., "IncidentIQ Demo District")
- `SiteUrl` - URL slug used in site-specific endpoints
- `IsActive` - Whether the site is currently active
- `Created` / `Modified` - Timestamp metadata

**Supports:**
- Custom filters via query parameters
- Pagination (default: 1000 items, sorted by Name ascending)

**Related Endpoints:**
- [GET /api/v1.0/sites/{siteUrl}](#/Sites/getSiteByUrl) - Get specific site by URL
- [GET /api/v1.0/sites/{SiteId}/settings](#/Sites/getSiteSettingsById) - Get site settings

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `SiteListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `SiteListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
