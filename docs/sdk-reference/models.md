# `models` Golden Namespace

Sync client access: `client.models`

Async client access: `client.models` with `await` on method calls.

These methods are Golden because they come from the bundled Incident IQ OpenAPI contract.

## Aliases

| Alias | Canonical Method | Route |
| --- | --- | --- |
| `create` | `create_model` | `POST /api/v1.0/models/new` |

## Methods

### `create_model`

Provenance: Golden OpenAPI contract

Operation ID: `createModel`

- Sync: `client.models.create_model(body=..., timeout=None)`
- Async: `await client.models.create_model(body=..., timeout=None)`
- Raw payload: `client.models.create_model.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/models/new`
- Source controller: `IncidentIQ API`
- Aliases: `create`

Create model

Creates a new asset model definition.

**Prerequisites**
- **ManufacturerId** (required) - Use [POST /api/v1.0/assets/manufacturers](#/Manufacturers/searchManufacturers) to find or create a manufacturer
- **CategoryId** (required) - Use [POST /api/v1.0/categories/v2](#/Categories/searchCategoriesV2) to find a category
- **AssetTypeId** (required) - Use [GET /api/v1.0/assets/types](#/Assets/listAssetTypes) to get the asset type

**Workflow Example**
1. Get manufacturer: [POST /api/v1.0/assets/manufacturers](#/Manufacturers/searchManufacturers) → extract `ManufacturerId`
2. Get category: [POST /api/v1.0/categories/v2](#/Categories/searchCategoriesV2) → extract `CategoryId`
3. Get asset type: [GET /api/v1.0/assets/types](#/Assets/listAssetTypes) → extract `AssetTypeId`
4. Call this endpoint: POST /api/v1.0/models/new with required fields
5. Extract `Item.ModelId` from response for use in asset creation

**Required Fields**: Name, ManufacturerId, CategoryId, AssetTypeId, Scope

**Related Endpoints**
- [POST /api/v1.0/models](#/Models/searchModels) - Search existing models
- [POST /api/v1.0/models/{ModelId}](#/Models/updateModel) - Update a model

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `UpdateModelRequest` | `UpdateModelRequest` | - |

#### Returns

- Typed call return: `ModelCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ModelCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_model`

Provenance: Golden OpenAPI contract

Operation ID: `deleteModel`

- Sync: `client.models.delete_model(model_id=..., timeout=None)`
- Async: `await client.models.delete_model(model_id=..., timeout=None)`
- Raw payload: `client.models.delete_model.raw(model_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/models/{ModelId}`
- Source controller: `IncidentIQ API`

Delete model

Deletes a model from the system.

**Prerequisites**
- **ModelId** - Use [POST /api/v1.0/models](#/Models/searchModels) to find the model to delete

**Warning**: Deleting a model may affect assets that reference it. Ensure no assets are using this model before deletion.

**Workflow Example**
1. Search models: [POST /api/v1.0/models](#/Models/searchModels) → find model to delete
2. Verify no assets use this model
3. Call this endpoint: DELETE /api/v1.0/models/{ModelId}

**Related Endpoints**
- [POST /api/v1.0/models/bulk/delete](#/Models/bulkDeleteModels) - Delete multiple models at once

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `model_id` | `ModelId` | `path` | `yes` | `str` | `-` | UUID of the model to delete. Obtain via [POST /api/v1.0/models](#/Models/searchModels). |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_app_model_details`

Provenance: Golden OpenAPI contract

Operation ID: `getAppModelDetails`

- Sync: `client.models.get_app_model_details(model_id=..., app_id=..., timeout=None)`
- Async: `await client.models.get_app_model_details(model_id=..., app_id=..., timeout=None)`
- Raw payload: `client.models.get_app_model_details.raw(model_id=..., app_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/models/{ModelId}/link/app/{AppId}/details`
- Source controller: `IncidentIQ API`

Get app model details

Retrieves the configuration details for a model-app link.

**Prerequisites**
- **ModelId** - Use [POST /api/v1.0/models](#/Models/searchModels)
- **AppId** - Application identifier string

**Response Structure**
Returns AppModel with configuration like InheritIssues flag.

**Related Endpoints**
- [POST /api/v1.0/models/{ModelId}/link/app/{AppId}/details](#/Models/updateAppModelDetails) - Update details

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `model_id` | `ModelId` | `path` | `yes` | `str` | `-` | UUID of the model. |
| `app_id` | `AppId` | `path` | `yes` | `str` | `-` | Application identifier string. |

#### Returns

- Typed call return: `AppModelItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `AppModelItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_global_models_by_manufacturer`

Provenance: Golden OpenAPI contract

Operation ID: `getGlobalModelsByManufacturer`

- Sync: `client.models.get_global_models_by_manufacturer(manufacturer_id=..., body=None, timeout=None)`
- Async: `await client.models.get_global_models_by_manufacturer(manufacturer_id=..., body=None, timeout=None)`
- Raw payload: `client.models.get_global_models_by_manufacturer.raw(manufacturer_id=..., body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/models/global/for/manufacturer/{ManufacturerId}`
- Source controller: `IncidentIQ API`

Search global models by manufacturer

Searches global-scoped models belonging to a specific manufacturer with advanced filtering.

**Prerequisites**
- **ManufacturerId** - Use [POST /api/v1.0/assets/manufacturers](#/Manufacturers/searchManufacturers)

**Related Endpoints**
- [GET /api/v1.0/models/global/for/manufacturer/{ManufacturerId}](#/Models/getGlobalModelsByManufacturerGet) - Simple GET version

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `manufacturer_id` | `ManufacturerId` | `path` | `yes` | `str` | `-` | UUID of the manufacturer. |
| `body` | `body` | `body` | `no` | `ModelSearchRequest` | `ModelSearchRequest` | - |

#### Returns

- Typed call return: `ModelListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ModelListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_global_models_by_manufacturer_get`

Provenance: Golden OpenAPI contract

Operation ID: `getGlobalModelsByManufacturerGet`

- Sync: `client.models.get_global_models_by_manufacturer_get(manufacturer_id=..., timeout=None)`
- Async: `await client.models.get_global_models_by_manufacturer_get(manufacturer_id=..., timeout=None)`
- Raw payload: `client.models.get_global_models_by_manufacturer_get.raw(manufacturer_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/models/global/for/manufacturer/{ManufacturerId}`
- Source controller: `IncidentIQ API`

Get global models by manufacturer

Retrieves global-scoped models belonging to a specific manufacturer.

**Prerequisites**
- **ManufacturerId** - Use [POST /api/v1.0/assets/manufacturers](#/Manufacturers/searchManufacturers)

**Use Cases**
- Global model catalog by manufacturer
- Cross-site manufacturer model management
- Standard model definitions

**Related Endpoints**
- [POST /api/v1.0/models/global/for/manufacturer/{ManufacturerId}](#/Models/getGlobalModelsByManufacturer) - Same with POST filtering

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `manufacturer_id` | `ManufacturerId` | `path` | `yes` | `str` | `-` | UUID of the manufacturer. |

#### Returns

- Typed call return: `ModelListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ModelListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_model_by_id`

Provenance: Golden OpenAPI contract

Operation ID: `getModelById`

- Sync: `client.models.get_model_by_id(model_id=..., timeout=None)`
- Async: `await client.models.get_model_by_id(model_id=..., timeout=None)`
- Raw payload: `client.models.get_model_by_id.raw(model_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/models/{ModelId}`
- Source controller: `IncidentIQ API`

Get model by ID

Retrieves a specific model record by its unique identifier.

**Prerequisites**
- **ModelId** - Use [POST /api/v1.0/models](#/Models/searchModels) to search for models, extract `Items[].ModelId`

**Workflow Example**
1. Search models: [POST /api/v1.0/models](#/Models/searchModels) → get `ModelId`
2. Call this endpoint: GET /api/v1.0/models/{ModelId}
3. View complete model details including manufacturer, category, and metadata

**Related Endpoints**
- [POST /api/v1.0/models](#/Models/searchModels) - Search for models
- [POST /api/v1.0/models/{ModelId}](#/Models/updateModel) - Update this model
- [DELETE /api/v1.0/models/{ModelId}](#/Models/deleteModel) - Delete this model

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `model_id` | `ModelId` | `path` | `yes` | `str` | `-` | UUID of the model. Obtain via [POST /api/v1.0/models](#/Models/searchModels), extract `Items[].ModelId`. |

#### Returns

- Typed call return: `ModelItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ModelItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_model_counts`

Provenance: Golden OpenAPI contract

Operation ID: `getModelCounts`

- Sync: `client.models.get_model_counts(body=None, timeout=None)`
- Async: `await client.models.get_model_counts(body=None, timeout=None)`
- Raw payload: `client.models.get_model_counts.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/models/counts`
- Source controller: `IncidentIQ API`

Get model counts

Retrieves model counts grouped by category, location, role, or manufacturer based on filter criteria.

**Use Cases**
- Dashboard metrics for model distribution
- Capacity planning and reporting
- Asset inventory analysis

**Request Options**
- `CategoryId` - Filter counts by category
- `LocationId` - Filter counts by location
- `RoleId` - Filter counts by role visibility

**Response Structure**
Returns array of ModelCount objects with asset counts per model.

**Related Endpoints**
- [POST /api/v1.0/models/for/category/{CategoryId}/counts](#/Models/getModelCountsByCategory) - Category-specific counts

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `GetModelCountRequest` | `GetModelCountRequest` | - |

#### Returns

- Typed call return: `ModelCountListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ModelCountListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_model_counts_by_category`

Provenance: Golden OpenAPI contract

Operation ID: `getModelCountsByCategory`

- Sync: `client.models.get_model_counts_by_category(category_id=..., timeout=None)`
- Async: `await client.models.get_model_counts_by_category(category_id=..., timeout=None)`
- Raw payload: `client.models.get_model_counts_by_category.raw(category_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/models/for/category/{CategoryId}/counts`
- Source controller: `IncidentIQ API`

Get model counts by category with filters

Retrieves model counts grouped by various dimensions for a specific category with optional filtering.

**Prerequisites**
- **CategoryId** - Use [POST /api/v1.0/categories/v2](#/Categories/searchCategoriesV2)

**Related Endpoints**
- [GET /api/v1.0/models/for/category/{CategoryId}/counts](#/Models/getModelCountsByCategoryGet) - Simple GET version

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `category_id` | `CategoryId` | `path` | `yes` | `str` | `-` | UUID of the category. |

#### Returns

- Typed call return: `ModelCountListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ModelCountListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_model_counts_by_category_get`

Provenance: Golden OpenAPI contract

Operation ID: `getModelCountsByCategoryGet`

- Sync: `client.models.get_model_counts_by_category_get(category_id=..., timeout=None)`
- Async: `await client.models.get_model_counts_by_category_get(category_id=..., timeout=None)`
- Raw payload: `client.models.get_model_counts_by_category_get.raw(category_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/models/for/category/{CategoryId}/counts`
- Source controller: `IncidentIQ API`

Get model counts by category

Retrieves model counts grouped by various dimensions for a specific category.

**Prerequisites**
- **CategoryId** - Use [POST /api/v1.0/categories/v2](#/Categories/searchCategoriesV2)

**Use Cases**
- Category-based model statistics
- Dashboard metrics for model distribution
- Capacity planning by category

**Response Structure**
Returns counts grouped by model, with optional location, role, and manufacturer breakdowns.

**Related Endpoints**
- [POST /api/v1.0/models/for/category/{CategoryId}/counts](#/Models/getModelCountsByCategory) - Same with POST filtering
- [POST /api/v1.0/models/counts](#/Models/getModelCounts) - General model counts

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `category_id` | `CategoryId` | `path` | `yes` | `str` | `-` | UUID of the category. |

#### Returns

- Typed call return: `ModelCountListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ModelCountListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_model_mappings`

Provenance: Golden OpenAPI contract

Operation ID: `getModelMappings`

- Sync: `client.models.get_model_mappings(body=..., timeout=None)`
- Async: `await client.models.get_model_mappings(body=..., timeout=None)`
- Raw payload: `client.models.get_model_mappings.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/models/alias-mapping`
- Source controller: `IncidentIQ API`

Get model mappings

Resolves model alias strings to their corresponding ModelId values. Used for import operations and external system integrations.

**Use Cases**
- Resolve model names during data import
- Map external system model identifiers
- Validate model aliases exist

**Request Format**
Array of ModelMapping objects with Alias property set.

**Response Format**
Same array with ModelId populated for resolved aliases.

**Related Endpoints**
- [POST /api/v1.0/models](#/Models/searchModels) - Search models by name

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `list[Any]` | `-` | - |

#### Returns

- Typed call return: `ModelMappingListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ModelMappingListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_models_available_to_site`

Provenance: Golden OpenAPI contract

Operation ID: `getModelsAvailableToSite`

- Sync: `client.models.get_models_available_to_site(body=None, timeout=None)`
- Async: `await client.models.get_models_available_to_site(body=None, timeout=None)`
- Raw payload: `client.models.get_models_available_to_site.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/models/available/to/site`
- Source controller: `IncidentIQ API`

Get models available to site

Retrieves models that can be added to the current site, including their role visibility settings.

**Use Cases**
- Site model catalog configuration
- Add available models to site
- Review global models for site adoption

**Response Structure**
Returns ModelRoles objects showing which roles have the model enabled/disabled.

**Related Endpoints**
- [POST /api/v1.0/models/available/to/siteV2](#/Models/getModelsAvailableToSiteV2) - V2 with enhanced filtering
- [POST /api/v1.0/models/{ModelId}/site](#/Models/setModelSiteVisibility) - Add model to site

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `GetAvailableModelsRequest` | `GetAvailableModelsRequest` | - |

#### Returns

- Typed call return: `ModelRolesListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ModelRolesListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_models_available_to_site_v2`

Provenance: Golden OpenAPI contract

Operation ID: `getModelsAvailableToSiteV2`

- Sync: `client.models.get_models_available_to_site_v2(body=None, timeout=None)`
- Async: `await client.models.get_models_available_to_site_v2(body=None, timeout=None)`
- Raw payload: `client.models.get_models_available_to_site_v2.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/models/available/to/siteV2`
- Source controller: `IncidentIQ API`

Get models available to site (V2)

Enhanced version of the available models endpoint with improved filtering and performance.

**Use Cases**
- Site model catalog configuration with advanced filtering
- Large-scale model catalog management
- Performance-optimized model availability queries

**Related Endpoints**
- [POST /api/v1.0/models/available/to/site](#/Models/getModelsAvailableToSite) - V1 endpoint

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `GetAvailableModelsRequest` | `GetAvailableModelsRequest` | - |

#### Returns

- Typed call return: `ModelRolesListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ModelRolesListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_models_by_category`

Provenance: Golden OpenAPI contract

Operation ID: `getModelsByCategory`

- Sync: `client.models.get_models_by_category(category_id=..., body=None, timeout=None)`
- Async: `await client.models.get_models_by_category(category_id=..., body=None, timeout=None)`
- Raw payload: `client.models.get_models_by_category.raw(category_id=..., body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/models/for/category/{CategoryId}`
- Source controller: `IncidentIQ API`

Search models by category

Searches models belonging to a specific category with advanced filtering.

**Prerequisites**
- **CategoryId** - Use [POST /api/v1.0/categories/v2](#/Categories/searchCategoriesV2) to find category IDs

**Workflow Example**
1. Get categories: [POST /api/v1.0/categories/v2](#/Categories/searchCategoriesV2) → extract `CategoryId`
2. Call this endpoint: POST /api/v1.0/models/for/category/{CategoryId}
3. View models in that category

**Related Endpoints**
- [GET /api/v1.0/models/for/category/{CategoryId}](#/Models/getModelsByCategoryGet) - Simple GET version

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `category_id` | `CategoryId` | `path` | `yes` | `str` | `-` | UUID of the category. |
| `body` | `body` | `body` | `no` | `ModelSearchRequest` | `ModelSearchRequest` | - |

#### Returns

- Typed call return: `ModelListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ModelListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_models_by_category_for_my_role`

Provenance: Golden OpenAPI contract

Operation ID: `getModelsByCategoryForMyRole`

- Sync: `client.models.get_models_by_category_for_my_role(category_id=..., body=None, timeout=None)`
- Async: `await client.models.get_models_by_category_for_my_role(category_id=..., body=None, timeout=None)`
- Raw payload: `client.models.get_models_by_category_for_my_role.raw(category_id=..., body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/models/for/category/{CategoryId}/for/role`
- Source controller: `IncidentIQ API`

Search models by category for current user's role

Searches models in a specific category that are visible to the current user's role. Supports public/app authorization.

**Prerequisites**
- **CategoryId** - Use [POST /api/v1.0/categories/v2](#/Categories/searchCategoriesV2) to find category IDs

**Related Endpoints**
- [GET /api/v1.0/models/for/category/{CategoryId}/for/role](#/Models/getModelsByCategoryForMyRoleGet) - Simple GET version

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `category_id` | `CategoryId` | `path` | `yes` | `str` | `-` | UUID of the category. |
| `body` | `body` | `body` | `no` | `ModelSearchRequest` | `ModelSearchRequest` | - |

#### Returns

- Typed call return: `ModelListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ModelListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_models_by_category_for_my_role_get`

Provenance: Golden OpenAPI contract

Operation ID: `getModelsByCategoryForMyRoleGet`

- Sync: `client.models.get_models_by_category_for_my_role_get(category_id=..., timeout=None)`
- Async: `await client.models.get_models_by_category_for_my_role_get(category_id=..., timeout=None)`
- Raw payload: `client.models.get_models_by_category_for_my_role_get.raw(category_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/models/for/category/{CategoryId}/for/role`
- Source controller: `IncidentIQ API`

Get models by category for current user's role

Retrieves models in a specific category that are visible to the current user's role. Supports public/app authorization.

**Prerequisites**
- **CategoryId** - Use [POST /api/v1.0/categories/v2](#/Categories/searchCategoriesV2) to find category IDs

**Use Cases**
- Self-service portal category browsing
- Role-restricted category-based model selection
- Public-facing model catalogs

**Related Endpoints**
- [POST /api/v1.0/models/for/category/{CategoryId}/for/role](#/Models/getModelsByCategoryForMyRole) - Same with POST filtering

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `category_id` | `CategoryId` | `path` | `yes` | `str` | `-` | UUID of the category. |

#### Returns

- Typed call return: `ModelListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ModelListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_models_by_category_for_role`

Provenance: Golden OpenAPI contract

Operation ID: `getModelsByCategoryForRole`

- Sync: `client.models.get_models_by_category_for_role(category_id=..., role_id=..., body=None, timeout=None)`
- Async: `await client.models.get_models_by_category_for_role(category_id=..., role_id=..., body=None, timeout=None)`
- Raw payload: `client.models.get_models_by_category_for_role.raw(category_id=..., role_id=..., body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/models/for/category/{CategoryId}/for/role/{RoleId}`
- Source controller: `IncidentIQ API`

Search models by category for specific role

Searches models in a specific category that are visible to a specific role.

**Prerequisites**
- **CategoryId** - Use [POST /api/v1.0/categories/v2](#/Categories/searchCategoriesV2)
- **RoleId** - Use [GET /api/v1.0/sites/roles](#/Sites/listRoles)

**Related Endpoints**
- [GET /api/v1.0/models/for/category/{CategoryId}/for/role/{RoleId}](#/Models/getModelsByCategoryForRoleGet) - Simple GET version

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `category_id` | `CategoryId` | `path` | `yes` | `str` | `-` | UUID of the category. |
| `role_id` | `RoleId` | `path` | `yes` | `str` | `-` | UUID of the role. |
| `body` | `body` | `body` | `no` | `ModelSearchRequest` | `ModelSearchRequest` | - |

#### Returns

- Typed call return: `ModelListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ModelListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_models_by_category_for_role_get`

Provenance: Golden OpenAPI contract

Operation ID: `getModelsByCategoryForRoleGet`

- Sync: `client.models.get_models_by_category_for_role_get(category_id=..., role_id=..., timeout=None)`
- Async: `await client.models.get_models_by_category_for_role_get(category_id=..., role_id=..., timeout=None)`
- Raw payload: `client.models.get_models_by_category_for_role_get.raw(category_id=..., role_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/models/for/category/{CategoryId}/for/role/{RoleId}`
- Source controller: `IncidentIQ API`

Get models by category for specific role

Retrieves models in a specific category that are visible to a specific role.

**Prerequisites**
- **CategoryId** - Use [POST /api/v1.0/categories/v2](#/Categories/searchCategoriesV2)
- **RoleId** - Use [GET /api/v1.0/sites/roles](#/Sites/listRoles)

**Use Cases**
- Role-based category access testing
- Administrative visibility configuration
- Cross-role model visibility comparison

**Related Endpoints**
- [POST /api/v1.0/models/for/category/{CategoryId}/for/role/{RoleId}](#/Models/getModelsByCategoryForRole) - Same with POST filtering

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `category_id` | `CategoryId` | `path` | `yes` | `str` | `-` | UUID of the category. |
| `role_id` | `RoleId` | `path` | `yes` | `str` | `-` | UUID of the role. |

#### Returns

- Typed call return: `ModelListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ModelListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_models_by_category_get`

Provenance: Golden OpenAPI contract

Operation ID: `getModelsByCategoryGet`

- Sync: `client.models.get_models_by_category_get(category_id=..., timeout=None)`
- Async: `await client.models.get_models_by_category_get(category_id=..., timeout=None)`
- Raw payload: `client.models.get_models_by_category_get.raw(category_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/models/for/category/{CategoryId}`
- Source controller: `IncidentIQ API`

Get models by category

Retrieves models belonging to a specific category.

**Prerequisites**
- **CategoryId** - Use [POST /api/v1.0/categories/v2](#/Categories/searchCategoriesV2) to find category IDs

**Use Cases**
- Category-specific model selection
- Filtered model dropdowns by category
- Category-based asset creation workflows

**Related Endpoints**
- [POST /api/v1.0/models/for/category/{CategoryId}](#/Models/getModelsByCategory) - Same with POST filtering
- [POST /api/v1.0/models/for/category/{CategoryId}/for/role](#/Models/getModelsByCategoryForMyRole) - With role filtering

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `category_id` | `CategoryId` | `path` | `yes` | `str` | `-` | UUID of the category. Obtain via [POST /api/v1.0/categories/v2](#/Categories/searchCategoriesV2). |

#### Returns

- Typed call return: `ModelListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ModelListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_models_by_manufacturer`

Provenance: Golden OpenAPI contract

Operation ID: `getModelsByManufacturer`

- Sync: `client.models.get_models_by_manufacturer(manufacturer_id=..., body=None, timeout=None)`
- Async: `await client.models.get_models_by_manufacturer(manufacturer_id=..., body=None, timeout=None)`
- Raw payload: `client.models.get_models_by_manufacturer.raw(manufacturer_id=..., body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/models/for/manufacturer/{ManufacturerId}`
- Source controller: `IncidentIQ API`

Search models by manufacturer

Searches models belonging to a specific manufacturer with advanced filtering.

**Prerequisites**
- **ManufacturerId** - Use [POST /api/v1.0/assets/manufacturers](#/Manufacturers/searchManufacturers)

**Related Endpoints**
- [GET /api/v1.0/models/for/manufacturer/{ManufacturerId}](#/Models/getModelsByManufacturerGet) - Simple GET version

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `manufacturer_id` | `ManufacturerId` | `path` | `yes` | `str` | `-` | UUID of the manufacturer. |
| `body` | `body` | `body` | `no` | `ModelSearchRequest` | `ModelSearchRequest` | - |

#### Returns

- Typed call return: `ModelListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ModelListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_models_by_manufacturer_get`

Provenance: Golden OpenAPI contract

Operation ID: `getModelsByManufacturerGet`

- Sync: `client.models.get_models_by_manufacturer_get(manufacturer_id=..., timeout=None)`
- Async: `await client.models.get_models_by_manufacturer_get(manufacturer_id=..., timeout=None)`
- Raw payload: `client.models.get_models_by_manufacturer_get.raw(manufacturer_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/models/for/manufacturer/{ManufacturerId}`
- Source controller: `IncidentIQ API`

Get models by manufacturer

Retrieves models belonging to a specific manufacturer.

**Prerequisites**
- **ManufacturerId** - Use [POST /api/v1.0/assets/manufacturers](#/Manufacturers/searchManufacturers)

**Use Cases**
- Manufacturer-specific model browsing
- Vendor catalog exploration
- Manufacturer-based asset workflows

**Related Endpoints**
- [POST /api/v1.0/models/for/manufacturer/{ManufacturerId}](#/Models/getModelsByManufacturer) - Same with POST filtering
- [POST /api/v1.0/models/global/for/manufacturer/{ManufacturerId}](#/Models/getGlobalModelsByManufacturer) - Global models only

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `manufacturer_id` | `ManufacturerId` | `path` | `yes` | `str` | `-` | UUID of the manufacturer. Obtain via [POST /api/v1.0/assets/manufacturers](#/Manufacturers/searchManufacturers). |

#### Returns

- Typed call return: `ModelListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ModelListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_models_for_app`

Provenance: Golden OpenAPI contract

Operation ID: `getModelsForApp`

- Sync: `client.models.get_models_for_app(app_id=..., body=None, timeout=None)`
- Async: `await client.models.get_models_for_app(app_id=..., body=None, timeout=None)`
- Raw payload: `client.models.get_models_for_app.raw(app_id=..., body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/models/apps/{AppId}`
- Source controller: `IncidentIQ API`

Search models for app

Searches models linked to a specific application integration with advanced filtering.

**Prerequisites**
- **AppId** - Application identifier string

**Related Endpoints**
- [GET /api/v1.0/models/apps/{AppId}](#/Models/getModelsForAppGet) - Simple GET version

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `app_id` | `AppId` | `path` | `yes` | `str` | `-` | Application identifier string. |
| `body` | `body` | `body` | `no` | `ModelSearchRequest` | `ModelSearchRequest` | - |

#### Returns

- Typed call return: `ModelListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ModelListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_models_for_app_get`

Provenance: Golden OpenAPI contract

Operation ID: `getModelsForAppGet`

- Sync: `client.models.get_models_for_app_get(app_id=..., timeout=None)`
- Async: `await client.models.get_models_for_app_get(app_id=..., timeout=None)`
- Raw payload: `client.models.get_models_for_app_get.raw(app_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/models/apps/{AppId}`
- Source controller: `IncidentIQ API`

Get models for app

Retrieves models linked to a specific application integration.

**Prerequisites**
- **AppId** - Application identifier string (not a GUID)

**Use Cases**
- View models associated with an app integration
- App-specific model catalog
- Integration-based model filtering

**Related Endpoints**
- [POST /api/v1.0/models/apps/{AppId}](#/Models/getModelsForApp) - Same with POST filtering
- [POST /api/v1.0/models/{ModelId}/link/app/{AppId}](#/Models/linkModelToApp) - Link model to app

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `app_id` | `AppId` | `path` | `yes` | `str` | `-` | Application identifier string. |

#### Returns

- Typed call return: `ModelListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ModelListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_models_for_my_role`

Provenance: Golden OpenAPI contract

Operation ID: `getModelsForMyRole`

- Sync: `client.models.get_models_for_my_role(body=None, timeout=None)`
- Async: `await client.models.get_models_for_my_role(body=None, timeout=None)`
- Raw payload: `client.models.get_models_for_my_role.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/models/for/role`
- Source controller: `IncidentIQ API`

Search models for current user's role

Searches models visible to the current authenticated user based on their role permissions with advanced filtering.

**Use Cases**
- Self-service portal with complex filtering
- Role-restricted asset creation with category filters
- User-facing model search

**Filtering**
Supports all standard filter facets plus automatic role-based visibility filtering.

**Related Endpoints**
- [GET /api/v1.0/models/for/role](#/Models/getModelsForMyRoleGet) - Simple GET version
- [POST /api/v1.0/models/for/role/{RoleId}](#/Models/getModelsForRole) - Specify a different role

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `ModelSearchRequest` | `ModelSearchRequest` | - |

#### Returns

- Typed call return: `ModelListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ModelListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_models_for_my_role_get`

Provenance: Golden OpenAPI contract

Operation ID: `getModelsForMyRoleGet`

- Sync: `client.models.get_models_for_my_role_get(top=None, skip=None, timeout=None)`
- Async: `await client.models.get_models_for_my_role_get(top=None, skip=None, timeout=None)`
- Raw payload: `client.models.get_models_for_my_role_get.raw(top=None, skip=None, timeout=None)`
- HTTP route: `GET /api/v1.0/models/for/role`
- Source controller: `IncidentIQ API`

Get models for current user's role

Retrieves models visible to the current authenticated user based on their role permissions.

**Use Cases**
- Self-service portal model selection
- Role-restricted asset creation workflows
- User-facing model catalog

**Filtering**
Supports standard pagination and filtering. Models are automatically filtered based on the current user's role visibility settings.

**Related Endpoints**
- [POST /api/v1.0/models/for/role](#/Models/getModelsForMyRole) - Same endpoint with POST for complex filters
- [POST /api/v1.0/models/for/role/{RoleId}](#/Models/getModelsForRole) - Get models for a specific role

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `top` | `$top` | `query` | `no` | `int` | `-` | Maximum number of records to return |
| `skip` | `$skip` | `query` | `no` | `int` | `-` | Number of records to skip |

#### Returns

- Typed call return: `ModelListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ModelListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_models_for_role`

Provenance: Golden OpenAPI contract

Operation ID: `getModelsForRole`

- Sync: `client.models.get_models_for_role(role_id=..., body=None, timeout=None)`
- Async: `await client.models.get_models_for_role(role_id=..., body=None, timeout=None)`
- Raw payload: `client.models.get_models_for_role.raw(role_id=..., body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/models/for/role/{RoleId}`
- Source controller: `IncidentIQ API`

Search models for specific role

Searches models visible to a specific role with advanced filtering.

**Prerequisites**
- **RoleId** - Use [GET /api/v1.0/sites/roles](#/Sites/listRoles) to get available role IDs

**Workflow Example**
1. Get roles: [GET /api/v1.0/sites/roles](#/Sites/listRoles) → extract `RoleId`
2. Call this endpoint: POST /api/v1.0/models/for/role/{RoleId}
3. View models visible to that role

**Related Endpoints**
- [GET /api/v1.0/models/for/role/{RoleId}](#/Models/getModelsForRoleGet) - Simple GET version

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `role_id` | `RoleId` | `path` | `yes` | `str` | `-` | UUID of the role. |
| `body` | `body` | `body` | `no` | `ModelSearchRequest` | `ModelSearchRequest` | - |

#### Returns

- Typed call return: `ModelListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ModelListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_models_for_role_get`

Provenance: Golden OpenAPI contract

Operation ID: `getModelsForRoleGet`

- Sync: `client.models.get_models_for_role_get(role_id=..., timeout=None)`
- Async: `await client.models.get_models_for_role_get(role_id=..., timeout=None)`
- Raw payload: `client.models.get_models_for_role_get.raw(role_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/models/for/role/{RoleId}`
- Source controller: `IncidentIQ API`

Get models for specific role

Retrieves models visible to a specific role.

**Prerequisites**
- **RoleId** - Use [GET /api/v1.0/sites/roles](#/Sites/listRoles) to get available role IDs

**Use Cases**
- Preview model visibility for a specific role
- Administrative role configuration testing
- Role-based access control validation

**Related Endpoints**
- [POST /api/v1.0/models/for/role/{RoleId}](#/Models/getModelsForRole) - Same endpoint with POST for complex filters
- [GET /api/v1.0/models/for/role](#/Models/getModelsForMyRoleGet) - Get models for current user's role

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `role_id` | `RoleId` | `path` | `yes` | `str` | `-` | UUID of the role. Obtain via [GET /api/v1.0/sites/roles](#/Sites/listRoles). |

#### Returns

- Typed call return: `ModelListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ModelListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_popular_models`

Provenance: Golden OpenAPI contract

Operation ID: `getPopularModels`

- Sync: `client.models.get_popular_models(top=None, timeout=None)`
- Async: `await client.models.get_popular_models(top=None, timeout=None)`
- Raw payload: `client.models.get_popular_models.raw(top=None, timeout=None)`
- HTTP route: `GET /api/v1.0/models/popular`
- Source controller: `IncidentIQ API`

Get popular models

Retrieves models ordered by popularity based on ticket and asset usage. Supports public/app authorization.

**Use Cases**
- Self-service portal "suggested models" section
- Quick model selection based on common usage
- User-facing model recommendations

**Response Structure**
Returns PopularModel objects containing the full Model plus ticket count metrics.

**Related Endpoints**
- [POST /api/v1.0/models](#/Models/searchModels) - Full model search
- [POST /api/v1.0/models/for/role](#/Models/getModelsForMyRole) - Role-filtered models

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `top` | `$top` | `query` | `no` | `int` | `-` | Maximum number of models to return |

#### Returns

- Typed call return: `PopularModelListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `PopularModelListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `link_model_to_app`

Provenance: Golden OpenAPI contract

Operation ID: `linkModelToApp`

- Sync: `client.models.link_model_to_app(model_id=..., app_id=..., timeout=None)`
- Async: `await client.models.link_model_to_app(model_id=..., app_id=..., timeout=None)`
- Raw payload: `client.models.link_model_to_app.raw(model_id=..., app_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/models/{ModelId}/link/app/{AppId}`
- Source controller: `IncidentIQ API`

Link model to app

Creates a link between a model and an application integration.

**Prerequisites**
- **ModelId** - Use [POST /api/v1.0/models](#/Models/searchModels) to find the model
- **AppId** - Application identifier string

**Use Cases**
- Associate models with app integrations
- Enable app-specific model features
- Configure model behavior for integrations

**Related Endpoints**
- [DELETE /api/v1.0/models/{ModelId}/link/app/{AppId}](#/Models/unlinkModelFromApp) - Remove link
- [GET /api/v1.0/models/{ModelId}/link/app/{AppId}/details](#/Models/getAppModelDetails) - View link details

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `model_id` | `ModelId` | `path` | `yes` | `str` | `-` | UUID of the model. |
| `app_id` | `AppId` | `path` | `yes` | `str` | `-` | Application identifier string. |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_all_global_models`

Provenance: Golden OpenAPI contract

Operation ID: `listAllGlobalModels`

- Sync: `client.models.list_all_global_models(body=None, timeout=None)`
- Async: `await client.models.list_all_global_models(body=None, timeout=None)`
- Raw payload: `client.models.list_all_global_models.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/models/all/global`
- Source controller: `IncidentIQ API`

Search all global-scoped models

Searches all models with Global scope, bypassing visibility rules.

**Use Cases**
- Administrative global model searches
- Global model catalog filtering
- Cross-site model analysis

**Related Endpoints**
- [GET /api/v1.0/models/all/global](#/Models/listAllGlobalModelsGet) - Simple GET version

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `ModelSearchRequest` | `ModelSearchRequest` | - |

#### Returns

- Typed call return: `ModelListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ModelListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_all_global_models_get`

Provenance: Golden OpenAPI contract

Operation ID: `listAllGlobalModelsGet`

- Sync: `client.models.list_all_global_models_get(timeout=None)`
- Async: `await client.models.list_all_global_models_get(timeout=None)`
- Raw payload: `client.models.list_all_global_models_get.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/models/all/global`
- Source controller: `IncidentIQ API`

List all global-scoped models

Retrieves all models with Global scope, bypassing visibility rules.

**Use Cases**
- Global model catalog management
- System-wide model standardization
- Cross-site model configuration

**Related Endpoints**
- [POST /api/v1.0/models/all/global](#/Models/listAllGlobalModels) - Same with POST filtering
- [POST /api/v1.0/models/all/sites](#/Models/listAllSiteModels) - Site-scoped models

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `ModelListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ModelListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_all_models`

Provenance: Golden OpenAPI contract

Operation ID: `listAllModels`

- Sync: `client.models.list_all_models(body=None, timeout=None)`
- Async: `await client.models.list_all_models(body=None, timeout=None)`
- Raw payload: `client.models.list_all_models.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/models/all`
- Source controller: `IncidentIQ API`

Search all models (no visibility filter)

Searches all models without visibility filtering. Bypasses role-based and site-based visibility rules.

**Use Cases**
- Administrative model searches
- Visibility configuration auditing
- Cross-site model analysis

**Note**: This endpoint bypasses standard visibility rules.

**Related Endpoints**
- [GET /api/v1.0/models/all](#/Models/listAllModelsGet) - Simple GET version
- [POST /api/v1.0/models/all/global](#/Models/listAllGlobalModels) - Global models only

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `ModelSearchRequest` | `ModelSearchRequest` | - |

#### Returns

- Typed call return: `ModelListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ModelListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_all_models_get`

Provenance: Golden OpenAPI contract

Operation ID: `listAllModelsGet`

- Sync: `client.models.list_all_models_get(timeout=None)`
- Async: `await client.models.list_all_models_get(timeout=None)`
- Raw payload: `client.models.list_all_models_get.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/models/all`
- Source controller: `IncidentIQ API`

List all models (no visibility filter)

Retrieves all models without visibility filtering. Bypasses role-based and site-based visibility rules.

**Use Cases**
- Administrative model management
- System-wide model auditing
- Visibility configuration setup

**Note**: This endpoint bypasses standard visibility rules. Use with caution in production environments.

**Related Endpoints**
- [POST /api/v1.0/models/all](#/Models/listAllModels) - Same endpoint with POST for filtering
- [POST /api/v1.0/models](#/Models/searchModels) - Search with visibility rules applied

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `ModelListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ModelListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_all_site_models`

Provenance: Golden OpenAPI contract

Operation ID: `listAllSiteModels`

- Sync: `client.models.list_all_site_models(body=None, timeout=None)`
- Async: `await client.models.list_all_site_models(body=None, timeout=None)`
- Raw payload: `client.models.list_all_site_models.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/models/all/sites`
- Source controller: `IncidentIQ API`

Search all site-scoped models

Searches all models with Site scope, bypassing visibility rules.

**Use Cases**
- Site-specific model searches
- Site model catalog filtering
- Multi-site model management

**Related Endpoints**
- [GET /api/v1.0/models/all/sites](#/Models/listAllSiteModelsGet) - Simple GET version

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `ModelSearchRequest` | `ModelSearchRequest` | - |

#### Returns

- Typed call return: `ModelListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ModelListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_all_site_models_get`

Provenance: Golden OpenAPI contract

Operation ID: `listAllSiteModelsGet`

- Sync: `client.models.list_all_site_models_get(timeout=None)`
- Async: `await client.models.list_all_site_models_get(timeout=None)`
- Raw payload: `client.models.list_all_site_models_get.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/models/all/sites`
- Source controller: `IncidentIQ API`

List all site-scoped models

Retrieves all models with Site scope, bypassing visibility rules.

**Use Cases**
- Site-specific model management
- Site model visibility auditing
- Multi-site model comparison

**Related Endpoints**
- [POST /api/v1.0/models/all/sites](#/Models/listAllSiteModels) - Same with POST filtering
- [POST /api/v1.0/models/all/global](#/Models/listAllGlobalModels) - Global-scoped models

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `ModelListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ModelListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_models`

Provenance: Golden OpenAPI contract

Operation ID: `listModels`

- Sync: `client.models.list_models(top=None, skip=None, orderby=None, orderby_direction=None, timeout=None)`
- Async: `await client.models.list_models(top=None, skip=None, orderby=None, orderby_direction=None, timeout=None)`
- Raw payload: `client.models.list_models.raw(top=None, skip=None, orderby=None, orderby_direction=None, timeout=None)`
- HTTP route: `GET /api/v1.0/models`
- Source controller: `IncidentIQ API`

List models

Retrieves a paginated list of asset models visible to the current user.

**Use Cases**
- Populate model dropdown when creating or editing assets
- Display model catalog for administrators
- Get `ModelId` values for asset creation workflows

**Response Structure**
Returns models with their associated manufacturer, category, and visibility settings.

**Filtering**
Supports standard pagination (`$top`, `$skip`) and sorting. Use [POST /api/v1.0/models](#/Models/searchModels) for complex filter criteria.

**Related Endpoints**
- [POST /api/v1.0/models](#/Models/searchModels) - Search with filters
- [GET /api/v1.0/models/{ModelId}](#/Models/getModelById) - Get single model
- [POST /api/v1.0/models/new](#/Models/createModel) - Create new model

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `top` | `$top` | `query` | `no` | `int` | `-` | Maximum number of records to return (page size) |
| `skip` | `$skip` | `query` | `no` | `int` | `-` | Number of records to skip for pagination |
| `orderby` | `$orderby` | `query` | `no` | `str` | `-` | Field name to sort by |
| `orderby_direction` | `$orderbyDirection` | `query` | `no` | `str` | `-` | Sort direction |

#### Returns

- Typed call return: `ModelListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ModelListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `remove_model_from_site`

Provenance: Golden OpenAPI contract

Operation ID: `removeModelFromSite`

- Sync: `client.models.remove_model_from_site(model_id=..., timeout=None)`
- Async: `await client.models.remove_model_from_site(model_id=..., timeout=None)`
- Raw payload: `client.models.remove_model_from_site.raw(model_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/models/{ModelId}/site`
- Source controller: `IncidentIQ API`

Remove model from site

Removes a model from the current site's visibility.

**Prerequisites**
- **ModelId** - Use [POST /api/v1.0/models](#/Models/searchModels) to find the model

**Use Cases**
- Hide models from site users
- Site-specific model catalog curation
- Cleanup after model consolidation

**Related Endpoints**
- [POST /api/v1.0/models/{ModelId}/site](#/Models/setModelSiteVisibility) - Add model to site

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `model_id` | `ModelId` | `path` | `yes` | `str` | `-` | UUID of the model to remove. |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `search_models`

Provenance: Golden OpenAPI contract

Operation ID: `searchModels`

- Sync: `client.models.search_models(body=..., timeout=None)`
- Async: `await client.models.search_models(body=..., timeout=None)`
- Raw payload: `client.models.search_models.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/models`
- Source controller: `IncidentIQ API`

Search models

Searches the model catalog using filter criteria. This is the primary endpoint for obtaining `ModelId` values.

**Prerequisites**
- **CategoryId** (optional) - Use [POST /api/v1.0/categories/v2](#/Categories/searchCategoriesV2) to find category IDs
- **ManufacturerId** (optional) - Use [POST /api/v1.0/assets/manufacturers](#/Manufacturers/searchManufacturers) to find manufacturer IDs
- **AssetTypeId** (optional) - Use [GET /api/v1.0/assets/types](#/Assets/listAssetTypes) to find asset type IDs

**Workflow Example**
1. (Optional) Get asset types: [GET /api/v1.0/assets/types](#/Assets/listAssetTypes) → extract `AssetTypeId`
2. Build filter request with `Filters` array using facet `assettype`
3. Call this endpoint: POST /api/v1.0/models
4. Extract `Items[].ModelId` from response

**Supported Facets**
- `assettype` - Filter by asset type ID
- `manufacturer` - Filter by manufacturer ID
- `modelcategory` - Filter by category ID
- `scope` - Filter by scope (Global, Site, Product)

**Related Endpoints**
- [GET /api/v1.0/models](#/Models/listModels) - Simple list with query parameters
- [POST /api/v1.0/models/for/role](#/Models/getModelsForMyRole) - Models filtered by current user's role

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `ModelSearchRequest` | `ModelSearchRequest` | - |

#### Returns

- Typed call return: `ModelListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ModelListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `set_model_site_visibility`

Provenance: Golden OpenAPI contract

Operation ID: `setModelSiteVisibility`

- Sync: `client.models.set_model_site_visibility(model_id=..., body=None, timeout=None)`
- Async: `await client.models.set_model_site_visibility(model_id=..., body=None, timeout=None)`
- Raw payload: `client.models.set_model_site_visibility.raw(model_id=..., body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/models/{ModelId}/site`
- Source controller: `IncidentIQ API`

Set model site visibility

Adds or removes a model from the current site. Supports app authorization.

**Behavior**
- No body or null: Adds model to current site
- Empty array `[]`: Removes model from current site
- Array of EntitySiteOption: Bulk update site options

**Prerequisites**
- **ModelId** - Use [POST /api/v1.0/models](#/Models/searchModels) to find the model

**Related Endpoints**
- [DELETE /api/v1.0/models/{ModelId}/site](#/Models/removeModelFromSite) - Explicit remove
- [POST /api/v1.0/models/site](#/Models/updateModelSiteLinking) - Bulk updates

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `model_id` | `ModelId` | `path` | `yes` | `str` | `-` | UUID of the model. |
| `body` | `body` | `body` | `no` | `list[Any] | None` | `-` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `unlink_model_from_app`

Provenance: Golden OpenAPI contract

Operation ID: `unlinkModelFromApp`

- Sync: `client.models.unlink_model_from_app(model_id=..., app_id=..., timeout=None)`
- Async: `await client.models.unlink_model_from_app(model_id=..., app_id=..., timeout=None)`
- Raw payload: `client.models.unlink_model_from_app.raw(model_id=..., app_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/models/{ModelId}/link/app/{AppId}`
- Source controller: `IncidentIQ API`

Unlink model from app

Removes the link between a model and an application integration.

**Prerequisites**
- **ModelId** - Use [POST /api/v1.0/models](#/Models/searchModels)
- **AppId** - Application identifier string

**Related Endpoints**
- [POST /api/v1.0/models/{ModelId}/link/app/{AppId}](#/Models/linkModelToApp) - Create link

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `model_id` | `ModelId` | `path` | `yes` | `str` | `-` | UUID of the model. |
| `app_id` | `AppId` | `path` | `yes` | `str` | `-` | Application identifier string. |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_app_model_details`

Provenance: Golden OpenAPI contract

Operation ID: `updateAppModelDetails`

- Sync: `client.models.update_app_model_details(model_id=..., app_id=..., body=..., timeout=None)`
- Async: `await client.models.update_app_model_details(model_id=..., app_id=..., body=..., timeout=None)`
- Raw payload: `client.models.update_app_model_details.raw(model_id=..., app_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/models/{ModelId}/link/app/{AppId}/details`
- Source controller: `IncidentIQ API`

Update app model details

Updates the configuration details for a model-app link.

**Prerequisites**
- **ModelId** - Use [POST /api/v1.0/models](#/Models/searchModels)
- **AppId** - Application identifier string

**Configurable Options**
- `InheritIssues` - Whether the model inherits issues from the app

**Related Endpoints**
- [GET /api/v1.0/models/{ModelId}/link/app/{AppId}/details](#/Models/getAppModelDetails) - View current details

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `model_id` | `ModelId` | `path` | `yes` | `str` | `-` | UUID of the model. |
| `app_id` | `AppId` | `path` | `yes` | `str` | `-` | Application identifier string. |
| `body` | `body` | `body` | `yes` | `AppModel` | `AppModel` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_model`

Provenance: Golden OpenAPI contract

Operation ID: `updateModel`

- Sync: `client.models.update_model(model_id=..., body=..., timeout=None)`
- Async: `await client.models.update_model(model_id=..., body=..., timeout=None)`
- Raw payload: `client.models.update_model.raw(model_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/models/{ModelId}`
- Source controller: `IncidentIQ API`

Update model

Updates an existing model's properties.

**Prerequisites**
- **ModelId** - Use [POST /api/v1.0/models](#/Models/searchModels) to find the model
- **ManufacturerId** (required) - Use [POST /api/v1.0/assets/manufacturers](#/Manufacturers/searchManufacturers)
- **CategoryId** (required) - Use [POST /api/v1.0/categories/v2](#/Categories/searchCategoriesV2)
- **AssetTypeId** (required) - Use [GET /api/v1.0/assets/types](#/Assets/listAssetTypes)

**Workflow Example**
1. Get current model: [GET /api/v1.0/models/{ModelId}](#/Models/getModelById)
2. Modify desired fields in the response
3. Call this endpoint: POST /api/v1.0/models/{ModelId} with updated data

**Required Fields**: Name, ManufacturerId, CategoryId, AssetTypeId

**Related Endpoints**
- [GET /api/v1.0/models/{ModelId}](#/Models/getModelById) - Get current model data
- [DELETE /api/v1.0/models/{ModelId}](#/Models/deleteModel) - Delete this model

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `model_id` | `ModelId` | `path` | `yes` | `str` | `-` | UUID of the model to update. Obtain via [POST /api/v1.0/models](#/Models/searchModels). |
| `body` | `body` | `body` | `yes` | `UpdateModelRequest` | `UpdateModelRequest` | - |

#### Returns

- Typed call return: `GuidUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `GuidUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_model_site_linking`

Provenance: Golden OpenAPI contract

Operation ID: `updateModelSiteLinking`

- Sync: `client.models.update_model_site_linking(body=..., timeout=None)`
- Async: `await client.models.update_model_site_linking(body=..., timeout=None)`
- Raw payload: `client.models.update_model_site_linking.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/models/site`
- Source controller: `IncidentIQ API`

Update model-to-site linking (bulk)

Updates visibility of multiple models at the current site in a single operation.

**Use Cases**
- Bulk enable/disable models for a site
- Site model catalog management
- Mass visibility updates

**Request Format**
Send a dictionary mapping ModelId (GUID) to enabled state (boolean).

**Example**
```json
{
  "model-id-1": true,
  "model-id-2": false
}
```

**Related Endpoints**
- [POST /api/v1.0/models/{ModelId}/site](#/Models/setModelSiteVisibility) - Single model visibility
- [POST /api/v1.0/models/bulk/site](#/Models/bulkAddModelsToSite) - Bulk add with site options

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `dict[str, Any]` | `-` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
