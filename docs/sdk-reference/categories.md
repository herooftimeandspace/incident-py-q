# `categories` Golden Namespace

Sync client access: `client.categories`

Async client access: `client.categories` with `await` on method calls.

These methods are Golden because they come from the bundled Incident IQ OpenAPI contract.

## Methods

### `create_asset_category`

Provenance: Golden OpenAPI contract

Operation ID: `createAssetCategory`

- Sync: `client.categories.create_asset_category(body=..., timeout=None)`
- Async: `await client.categories.create_asset_category(body=..., timeout=None)`
- Raw payload: `client.categories.create_asset_category.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/categories/for/assets/new`
- Source controller: `IncidentIQ API`

Create an asset category

Creates a new category in the Assets taxonomy for classifying physical assets. The CategoryTypeId is set automatically for asset categories, so you only provide the name and any optional description, parent, or ordering metadata.

**Prerequisites (optional)**
1. **ParentCategoryId** - Use [GET /api/v1.0/categories/of/assets](#/Categories/listAssetCategories) to find a parent; extract `Items[].CategoryId`.

**Workflow Example**
1. (Optional) list asset categories to choose a parent.
2. [POST /api/v1.0/categories/for/assets/new](#/Categories/createAssetCategory) with category details.

**Minimal Required Fields**: Name.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `CategoryCreateRequest` | `CategoryCreateRequest` | - |

#### Returns

- Typed call return: `CategoryItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CategoryItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_category`

Provenance: Golden OpenAPI contract

Operation ID: `createCategory`

- Sync: `client.categories.create_category(body=..., timeout=None)`
- Async: `await client.categories.create_category(body=..., timeout=None)`
- Raw payload: `client.categories.create_category.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/categories/new`
- Source controller: `IncidentIQ API`

Create a new category

Creates a new category. The CategoryTypeId in the request body determines what type of category is created (Asset, Issue, Model, Kb, etc.). Use the type-specific endpoints like [POST /api/v1.0/categories/for/issue/new](#/Categories/createIssueCategory) when you want the server to assign the CategoryTypeId automatically.

**Prerequisites**
1. **CategoryTypeId** - Use [POST /api/v1.0/categories/v2](#/Categories/searchCategoriesV2) to list existing categories and capture a valid `Items[].CategoryTypeId`.
2. **ParentCategoryId** (optional) - To create a child category, extract a parent's `Items[].CategoryId` from the search.

**Workflow Example**
1. Discover category types from existing categories.
2. [POST /api/v1.0/categories/new](#/Categories/createCategory) with Name, CategoryTypeId, and optional ParentCategoryId.

**Minimal Required Fields**: Name, CategoryTypeId.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `Category` | `Category` | - |

#### Returns

- Typed call return: `CreateCategoryResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CreateCategoryResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_issue_category`

Provenance: Golden OpenAPI contract

Operation ID: `createIssueCategory`

- Sync: `client.categories.create_issue_category(body=..., timeout=None)`
- Async: `await client.categories.create_issue_category(body=..., timeout=None)`
- Raw payload: `client.categories.create_issue_category.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/categories/for/issue/new`
- Source controller: `IncidentIQ API`

Create an issue category

Creates a new category in the Issues taxonomy for grouping and organizing issue types. The server assigns the correct CategoryTypeId for Issues automatically, so you only need to supply the category name and optional hierarchy metadata.

**Prerequisites (optional)**
1. **ParentCategoryId** - Use [GET /api/v1.0/categories/of/issues](#/Categories/listIssueCategories) to find a parent; extract `Items[].CategoryId`.

**Workflow Example**
1. (Optional) List issue categories to select a parent.
2. [POST /api/v1.0/categories/for/issue/new](#/Categories/createIssueCategory) with category details.

**Minimal Required Fields**: Name.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `CategoryCreateRequest` | `CategoryCreateRequest` | - |

#### Returns

- Typed call return: `CategoryItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CategoryItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_kb_category`

Provenance: Golden OpenAPI contract

Operation ID: `createKbCategory`

- Sync: `client.categories.create_kb_category(body=..., timeout=None)`
- Async: `await client.categories.create_kb_category(body=..., timeout=None)`
- Raw payload: `client.categories.create_kb_category.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/categories/for/kb/new`
- Source controller: `IncidentIQ API`

Create a knowledge base category

Creates a new category in the Knowledge Base (Kb) taxonomy for organizing KB articles. The server assigns the correct CategoryTypeId for Kb automatically, so you only need to supply the category name and optional hierarchy metadata.

**Prerequisites (optional)**
1. **ParentCategoryId** - Use [GET /api/v1.0/categories/of/kb](#/Categories/listKbCategories) to find a parent; extract `Items[].CategoryId`.

**Workflow Example**
1. (Optional) List KB categories to select a parent.
2. [POST /api/v1.0/categories/for/kb/new](#/Categories/createKbCategory) with category details.

**Minimal Required Fields**: Name.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `CategoryCreateRequest` | `CategoryCreateRequest` | - |

#### Returns

- Typed call return: `CategoryItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CategoryItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_model_category`

Provenance: Golden OpenAPI contract

Operation ID: `createModelCategory`

- Sync: `client.categories.create_model_category(body=..., timeout=None)`
- Async: `await client.categories.create_model_category(body=..., timeout=None)`
- Raw payload: `client.categories.create_model_category.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/categories/for/model/new`
- Source controller: `IncidentIQ API`

Create a model category

Creates a new category in the Models taxonomy for organizing asset models. The server assigns the correct CategoryTypeId for Models, so you only provide the category metadata and optional hierarchy information.

**Prerequisites (optional)**
1. **ParentCategoryId** - Use [GET /api/v1.0/categories/of/models](#/Categories/listModelCategories) to find a parent; extract `Items[].CategoryId`.

**Workflow Example**
1. (Optional) list model categories to select a parent.
2. [POST /api/v1.0/categories/for/model/new](#/Categories/createModelCategory) with the category details.

**Minimal Required Fields**: Name.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `CategoryCreateRequest` | `CategoryCreateRequest` | - |

#### Returns

- Typed call return: `CategoryItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CategoryItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_role_category`

Provenance: Golden OpenAPI contract

Operation ID: `createRoleCategory`

- Sync: `client.categories.create_role_category(body=..., timeout=None)`
- Async: `await client.categories.create_role_category(body=..., timeout=None)`
- Raw payload: `client.categories.create_role_category.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/categories/for/roles/new`
- Source controller: `IncidentIQ API`

Create a role category

Creates a new category in the Roles taxonomy for grouping role records and permission sets. The server applies the Roles CategoryTypeId automatically, leaving you to supply the category details and optional hierarchy.

**Prerequisites (optional)**
1. **ParentCategoryId** - Use [GET /api/v1.0/categories/of/roles](#/Categories/listRoleCategories) to find a parent; extract `Items[].CategoryId`.

**Workflow Example**
1. (Optional) list role categories to choose a parent.
2. [POST /api/v1.0/categories/for/roles/new](#/Categories/createRoleCategory) with category details.

**Minimal Required Fields**: Name.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `CategoryCreateRequest` | `CategoryCreateRequest` | - |

#### Returns

- Typed call return: `CategoryItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CategoryItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_category`

Provenance: Golden OpenAPI contract

Operation ID: `deleteCategory`

- Sync: `client.categories.delete_category(category_id=..., timeout=None)`
- Async: `await client.categories.delete_category(category_id=..., timeout=None)`
- Raw payload: `client.categories.delete_category.raw(category_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/categories/{CategoryId}`
- Source controller: `IncidentIQ API`

Delete a category

Soft-deletes a category so it no longer appears in active lists while preserving history. Use this to remove a category from selection lists; you can restore it later with the undelete endpoint if needed.

**Prerequisites**
1. **CategoryId** - Use [POST /api/v1.0/categories/v2](#/Categories/searchCategoriesV2) to find the category and extract `Items[].CategoryId`.

**Workflow Example**
1. Search categories to confirm the target CategoryId.
2. [DELETE /api/v1.0/categories/{CategoryId}](#/Categories/deleteCategory) to deactivate it.

**Minimal Required Fields**: CategoryId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `category_id` | `CategoryId` | `path` | `yes` | `str` | `-` | Unique identifier of the category to delete |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_category_by_id`

Provenance: Golden OpenAPI contract

Operation ID: `getCategoryById`

- Sync: `client.categories.get_category_by_id(category_id=..., timeout=None)`
- Async: `await client.categories.get_category_by_id(category_id=..., timeout=None)`
- Raw payload: `client.categories.get_category_by_id.raw(category_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/categories/{CategoryId}`
- Source controller: `IncidentIQ API`

Get category by ID

Retrieves a single category by its unique identifier. Returns the full category object including hierarchy information, scope, parent references, and associated metadata.

**Prerequisites**
1. **CategoryId** - Use [POST /api/v1.0/categories/v2](#/Categories/searchCategoriesV2) to search categories and extract `Items[].CategoryId`.

**Workflow Example**
1. Search categories: [POST /api/v1.0/categories/v2](#/Categories/searchCategoriesV2) → capture `Items[].CategoryId`.
2. Retrieve details: [GET /api/v1.0/categories/{CategoryId}](#/Categories/getCategoryById) with the captured ID.

**Minimal Required Fields**: CategoryId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `category_id` | `CategoryId` | `path` | `yes` | `str` | `-` | Unique identifier of the category to retrieve |

#### Returns

- Typed call return: `CategoryItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CategoryItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_category_by_id_and_type`

Provenance: Golden OpenAPI contract

Operation ID: `getCategoryByIdAndType`

- Sync: `client.categories.get_category_by_id_and_type(category_id=..., category_type_id=..., timeout=None)`
- Async: `await client.categories.get_category_by_id_and_type(category_id=..., category_type_id=..., timeout=None)`
- Raw payload: `client.categories.get_category_by_id_and_type.raw(category_id=..., category_type_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/categories/v2/{CategoryId}/{CategoryTypeId}`
- Source controller: `IncidentIQ API`

Get category by ID and type

Retrieves a category by both CategoryId and CategoryTypeId. Use this endpoint when you need to ensure the category belongs to a specific type, such as when working with Model categories in the M&I V2 interface.

**Prerequisites**
1. **CategoryId** - Use [POST /api/v1.0/categories/v2](#/Categories/searchCategoriesV2) to search categories and extract `Items[].CategoryId`.
2. **CategoryTypeId** - From the same response, capture `Items[].CategoryTypeId`.

**Workflow Example**
1. Search categories: [POST /api/v1.0/categories/v2](#/Categories/searchCategoriesV2) → capture both IDs.
2. Retrieve by type: [GET /api/v1.0/categories/v2/{CategoryId}/{CategoryTypeId}](#/Categories/getCategoryByIdAndType).

**Minimal Required Fields**: CategoryId (path), CategoryTypeId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `category_id` | `CategoryId` | `path` | `yes` | `str` | `-` | Unique identifier of the category |
| `category_type_id` | `CategoryTypeId` | `path` | `yes` | `str` | `-` | Category type identifier to filter by |

#### Returns

- Typed call return: `CategoryItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CategoryItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_category_entity_type_links`

Provenance: Golden OpenAPI contract

Operation ID: `getCategoryEntityTypeLinks`

- Sync: `client.categories.get_category_entity_type_links(category_type_id=..., entity_type_id=..., timeout=None)`
- Async: `await client.categories.get_category_entity_type_links(category_type_id=..., entity_type_id=..., timeout=None)`
- Raw payload: `client.categories.get_category_entity_type_links.raw(category_type_id=..., entity_type_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/categories/{CategoryTypeId}/link/{EntityTypeId}`
- Source controller: `IncidentIQ API`

Get category-entity type links

Retrieves the associations between a category type and an entity type. Use this to understand which categories are linked to specific entity types in the system, such as mapping asset categories to asset type entities.

**Prerequisites**
1. **CategoryTypeId** - Use [POST /api/v1.0/categories/v2](#/Categories/searchCategoriesV2) and extract `Items[].CategoryTypeId`.
2. **EntityTypeId** - Obtain from system entity type configuration or related endpoints.

**Workflow Example**
1. Identify the CategoryTypeId for your target category taxonomy.
2. Identify the EntityTypeId for the entity you want to link.
3. [GET /api/v1.0/categories/{CategoryTypeId}/link/{EntityTypeId}](#/Categories/getCategoryEntityTypeLinks) to retrieve existing associations.

**Minimal Required Fields**: CategoryTypeId (path), EntityTypeId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `category_type_id` | `CategoryTypeId` | `path` | `yes` | `str` | `-` | Category type identifier |
| `entity_type_id` | `EntityTypeId` | `path` | `yes` | `str` | `-` | Entity type identifier |

#### Returns

- Typed call return: `GetCategoryEntityTypeLinksResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `GetCategoryEntityTypeLinksResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `link_category_to_app`

Provenance: Golden OpenAPI contract

Operation ID: `linkCategoryToApp`

- Sync: `client.categories.link_category_to_app(category_id=..., app_id=..., timeout=None)`
- Async: `await client.categories.link_category_to_app(category_id=..., app_id=..., timeout=None)`
- Raw payload: `client.categories.link_category_to_app.raw(category_id=..., app_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/categories/{CategoryId}/link/app/{AppId}`
- Source controller: `IncidentIQ API`

Link category to app

Creates a link between a category and an application so the category is available in that app's context. Use this to expose shared category taxonomies in app-specific workflows.

**Prerequisites**
1. **CategoryId** - Use [POST /api/v1.0/categories/v2](#/Categories/searchCategoriesV2) to find categories and extract `Items[].CategoryId`.
2. **AppId** - Use [GET /api/v1.0/categories/app-links](#/Categories/listAppCategoryLinks) to discover app identifiers; extract `Items[].AppId`.

**Workflow Example**
1. Identify the CategoryId and AppId.
2. [POST /api/v1.0/categories/{CategoryId}/link/app/{AppId}](#/Categories/linkCategoryToApp) to create the association.

**Minimal Required Fields**: CategoryId (path), AppId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `category_id` | `CategoryId` | `path` | `yes` | `str` | `-` | Unique identifier of the category |
| `app_id` | `AppId` | `path` | `yes` | `str` | `-` | Application identifier (e.g., 'sparepool', 'feetracker') |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_app_categories`

Provenance: Golden OpenAPI contract

Operation ID: `listAppCategories`

- Sync: `client.categories.list_app_categories(product_filter_type=None, parent_category_id=None, apply_site_visibility=None, timeout=None)`
- Async: `await client.categories.list_app_categories(product_filter_type=None, parent_category_id=None, apply_site_visibility=None, timeout=None)`
- Raw payload: `client.categories.list_app_categories.raw(product_filter_type=None, parent_category_id=None, apply_site_visibility=None, timeout=None)`
- HTTP route: `GET /api/v1.0/categories/of/apps`
- Source controller: `IncidentIQ API`

List app categories

Retrieves categories of type Apps, which can be used to group application-related items and UI navigation. Use optional ParentCategoryId to traverse the hierarchy and ApplySiteVisibility to honor site-scoped visibility.

**Workflow Example**
1. Request top-level app categories with no ParentCategoryId.
2. Use a returned CategoryId as ParentCategoryId to list children.

**Minimal Required Fields**: none (ParentCategoryId is optional).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `product_filter_type` | `ProductFilterType` | `query` | `no` | `str` | `-` | Filter by product scope |
| `parent_category_id` | `ParentCategoryId` | `query` | `no` | `str` | `-` | Filter to children of a specific parent category |
| `apply_site_visibility` | `ApplySiteVisibility` | `query` | `no` | `bool` | `-` | Whether to apply site-level visibility rules |

#### Returns

- Typed call return: `ModelCategoryListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ModelCategoryListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_app_category_links`

Provenance: Golden OpenAPI contract

Operation ID: `listAppCategoryLinks`

- Sync: `client.categories.list_app_category_links(timeout=None)`
- Async: `await client.categories.list_app_category_links(timeout=None)`
- Raw payload: `client.categories.list_app_category_links.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/categories/app-links`
- Source controller: `IncidentIQ API`

List app-category links

Lists all category-to-application associations, showing which categories are currently linked to which app keys. Use this as an inventory view before adding or removing links and to discover valid AppId values used by link/unlink operations.

**Workflow Example**
1. Call [GET /api/v1.0/categories/app-links](#/Categories/listAppCategoryLinks) to review existing associations.
2. Use the AppId and CategoryId values with the link or unlink endpoints as needed.

**Minimal Required Fields**: none.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `ListAppCategoryLinksResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListAppCategoryLinksResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_asset_categories`

Provenance: Golden OpenAPI contract

Operation ID: `listAssetCategories`

- Sync: `client.categories.list_asset_categories(product_filter_type=None, parent_category_id=None, apply_site_visibility=None, timeout=None)`
- Async: `await client.categories.list_asset_categories(product_filter_type=None, parent_category_id=None, apply_site_visibility=None, timeout=None)`
- Raw payload: `client.categories.list_asset_categories.raw(product_filter_type=None, parent_category_id=None, apply_site_visibility=None, timeout=None)`
- HTTP route: `GET /api/v1.0/categories/of/assets`
- Source controller: `IncidentIQ API`

List asset categories

Retrieves categories of type 'Assets' used for organizing and classifying physical assets. These categories can be assigned to assets for grouping and filtering in asset lists and reports.

**Workflow Example**
1. Call [GET /api/v1.0/categories/of/assets](#/Categories/listAssetCategories) without ParentCategoryId to fetch top-level categories.
2. Pass a returned CategoryId as ParentCategoryId to list child categories in the hierarchy.
3. Use category IDs when creating or updating assets via [POST /api/v1.0/assets/new](#/Assets/createAsset).

**Minimal Required Fields**: none (ParentCategoryId is optional for filtering).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `product_filter_type` | `ProductFilterType` | `query` | `no` | `str` | `-` | Filter by product scope |
| `parent_category_id` | `ParentCategoryId` | `query` | `no` | `str` | `-` | Filter to children of a specific parent category |
| `apply_site_visibility` | `ApplySiteVisibility` | `query` | `no` | `bool` | `-` | Whether to apply site-level visibility rules |

#### Returns

- Typed call return: `CategoryListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CategoryListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_categories_for_app`

Provenance: Golden OpenAPI contract

Operation ID: `listCategoriesForApp`

- Sync: `client.categories.list_categories_for_app(app_id=..., timeout=None)`
- Async: `await client.categories.list_categories_for_app(app_id=..., timeout=None)`
- Raw payload: `client.categories.list_categories_for_app.raw(app_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/categories/app/{AppId}`
- Source controller: `IncidentIQ API`

List categories for an app

Retrieves categories that are linked to a specific application, returning the categories that should appear inside that app's experience. Use this when building app-specific pickers or when you need to validate whether a category is already linked.

**Prerequisites**
1. **AppId** - Use [GET /api/v1.0/categories/app-links](#/Categories/listAppCategoryLinks) to discover app keys; extract `Items[].AppId`.

**Workflow Example**
1. List app links: [GET /api/v1.0/categories/app-links](#/Categories/listAppCategoryLinks) -> capture the AppId you care about.
2. Call [GET /api/v1.0/categories/app/{AppId}](#/Categories/listCategoriesForApp) to retrieve the linked categories.

**Minimal Required Fields**: AppId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `app_id` | `AppId` | `path` | `yes` | `str` | `-` | Application identifier (e.g., 'sparepool', 'feetracker') |

#### Returns

- Typed call return: `CategoryListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CategoryListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_categories_v2`

Provenance: Golden OpenAPI contract

Operation ID: `listCategoriesV2`

- Sync: `client.categories.list_categories_v2(filter=None, top=None, skip=None, timeout=None)`
- Async: `await client.categories.list_categories_v2(filter=None, top=None, skip=None, timeout=None)`
- Raw payload: `client.categories.list_categories_v2.raw(filter=None, top=None, skip=None, timeout=None)`
- HTTP route: `GET /api/v1.0/categories/v2`
- Source controller: `IncidentIQ API`

List categories (V2)

Lists categories using the V2 query-style parameters for lightweight filtering and paging. Use this endpoint to quickly retrieve a page of categories (for example, recent or top-level results), and switch to [POST /api/v1.0/categories/v2](#/Categories/searchCategoriesV2) when you need complex filters or request options.

**Workflow Example**
1. [GET /api/v1.0/categories/v2](#/Categories/listCategoriesV2) with $filter/$top/$skip to fetch a page of categories.
2. Use returned CategoryId values in update, delete, or linking operations.

**Minimal Required Fields**: none.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `filter` | `$filter` | `query` | `no` | `str` | `-` | OData-style filter expression |
| `top` | `$top` | `query` | `no` | `int` | `-` | Number of records to return |
| `skip` | `$skip` | `query` | `no` | `int` | `-` | Number of records to skip |

#### Returns

- Typed call return: `CategoryListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CategoryListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_filter_categories`

Provenance: Golden OpenAPI contract

Operation ID: `listFilterCategories`

- Sync: `client.categories.list_filter_categories(product_filter_type=None, parent_category_id=None, apply_site_visibility=None, timeout=None)`
- Async: `await client.categories.list_filter_categories(product_filter_type=None, parent_category_id=None, apply_site_visibility=None, timeout=None)`
- Raw payload: `client.categories.list_filter_categories.raw(product_filter_type=None, parent_category_id=None, apply_site_visibility=None, timeout=None)`
- HTTP route: `GET /api/v1.0/categories/of/filters`
- Source controller: `IncidentIQ API`

List filter categories

Returns the catalog of filter categories that organize available search facets. These categories mirror the groupings shown in the IncidentIQ UI (for example, Asset filters, General, and Timeline filters). Use this endpoint before retrieving individual facets to understand how filters are grouped.

**Workflow Example**
1. Call [GET /api/v1.0/categories/of/filters](#/Categories/listFilterCategories) to fetch the filter taxonomy.
2. Use returned CategoryId values to scope searches or build custom filter UIs that align with system-defined groupings.

**Minimal Required Fields**: none (ParentCategoryId is optional for drilling into sub-categories).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `product_filter_type` | `ProductFilterType` | `query` | `no` | `str` | `-` | Filter by product scope |
| `parent_category_id` | `ParentCategoryId` | `query` | `no` | `str` | `-` | Filter to children of a specific parent category |
| `apply_site_visibility` | `ApplySiteVisibility` | `query` | `no` | `bool` | `-` | Whether to apply site-level visibility rules |

#### Returns

- Typed call return: `FilterCategoryListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `FilterCategoryListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_issue_categories`

Provenance: Golden OpenAPI contract

Operation ID: `listIssueCategories`

- Sync: `client.categories.list_issue_categories(product_filter_type=None, parent_category_id=None, apply_site_visibility=None, timeout=None)`
- Async: `await client.categories.list_issue_categories(product_filter_type=None, parent_category_id=None, apply_site_visibility=None, timeout=None)`
- Raw payload: `client.categories.list_issue_categories.raw(product_filter_type=None, parent_category_id=None, apply_site_visibility=None, timeout=None)`
- HTTP route: `GET /api/v1.0/categories/of/issues`
- Source controller: `IncidentIQ API`

List issue categories

Retrieves categories of type 'Issues' used for grouping and organizing issue types in the ticketing system. These categories help organize the issue hierarchy displayed when creating tickets.

**Workflow Example**
1. Call [GET /api/v1.0/categories/of/issues](#/Categories/listIssueCategories) without ParentCategoryId to fetch top-level issue categories.
2. Pass a returned CategoryId as ParentCategoryId to list child categories in the hierarchy.
3. Use category IDs when configuring issue types or displaying issue pickers in ticket creation flows.

**Minimal Required Fields**: none (ParentCategoryId is optional for hierarchical drilling).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `product_filter_type` | `ProductFilterType` | `query` | `no` | `str` | `-` | Filter by product scope |
| `parent_category_id` | `ParentCategoryId` | `query` | `no` | `str` | `-` | Filter to children of a specific parent category |
| `apply_site_visibility` | `ApplySiteVisibility` | `query` | `no` | `bool` | `-` | Whether to apply site-level visibility rules |

#### Returns

- Typed call return: `CategoryListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CategoryListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_kb_categories`

Provenance: Golden OpenAPI contract

Operation ID: `listKbCategories`

- Sync: `client.categories.list_kb_categories(product_filter_type=None, parent_category_id=None, apply_site_visibility=None, timeout=None)`
- Async: `await client.categories.list_kb_categories(product_filter_type=None, parent_category_id=None, apply_site_visibility=None, timeout=None)`
- Raw payload: `client.categories.list_kb_categories.raw(product_filter_type=None, parent_category_id=None, apply_site_visibility=None, timeout=None)`
- HTTP route: `GET /api/v1.0/categories/of/kb`
- Source controller: `IncidentIQ API`

List knowledge base categories

Retrieves knowledge base categories (Kb) with article counts for each category. Use this list to drive KB navigation, show counts, or validate category selections when creating or tagging articles.

**Workflow Example**
1. Call [GET /api/v1.0/categories/of/kb](#/Categories/listKbCategories) to get root categories and counts.
2. Pass ParentCategoryId to list child categories in the hierarchy.

**Minimal Required Fields**: none (ParentCategoryId is optional).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `product_filter_type` | `ProductFilterType` | `query` | `no` | `str` | `-` | Filter by product scope |
| `parent_category_id` | `ParentCategoryId` | `query` | `no` | `str` | `-` | Filter to children of a specific parent category |
| `apply_site_visibility` | `ApplySiteVisibility` | `query` | `no` | `bool` | `-` | Whether to apply site-level visibility rules |

#### Returns

- Typed call return: `ListKbCategoriesResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ListKbCategoriesResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_model_categories`

Provenance: Golden OpenAPI contract

Operation ID: `listModelCategories`

- Sync: `client.categories.list_model_categories(product_filter_type=None, parent_category_id=None, apply_site_visibility=None, timeout=None)`
- Async: `await client.categories.list_model_categories(product_filter_type=None, parent_category_id=None, apply_site_visibility=None, timeout=None)`
- Raw payload: `client.categories.list_model_categories.raw(product_filter_type=None, parent_category_id=None, apply_site_visibility=None, timeout=None)`
- HTTP route: `GET /api/v1.0/categories/of/models`
- Source controller: `IncidentIQ API`

List model categories

Retrieves model categories used to organize asset models, optionally filtered by product scope, site visibility, or a parent category. This is the primary list for building model category pickers and for drilling into the hierarchy.

**Workflow Example**
1. Call [GET /api/v1.0/categories/of/models](#/Categories/listModelCategories) without ParentCategoryId to fetch top-level categories.
2. Re-call the same endpoint with ParentCategoryId to retrieve child categories.

**Minimal Required Fields**: none (ParentCategoryId is optional).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `product_filter_type` | `ProductFilterType` | `query` | `no` | `str` | `-` | Filter by product scope: 'current' for active product only, 'all' for all products |
| `parent_category_id` | `ParentCategoryId` | `query` | `no` | `str` | `-` | Filter to children of a specific parent category |
| `apply_site_visibility` | `ApplySiteVisibility` | `query` | `no` | `bool` | `-` | Whether to apply site-level visibility rules |

#### Returns

- Typed call return: `ModelCategoryListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ModelCategoryListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `list_role_categories`

Provenance: Golden OpenAPI contract

Operation ID: `listRoleCategories`

- Sync: `client.categories.list_role_categories(product_filter_type=None, parent_category_id=None, apply_site_visibility=None, timeout=None)`
- Async: `await client.categories.list_role_categories(product_filter_type=None, parent_category_id=None, apply_site_visibility=None, timeout=None)`
- Raw payload: `client.categories.list_role_categories.raw(product_filter_type=None, parent_category_id=None, apply_site_visibility=None, timeout=None)`
- HTTP route: `GET /api/v1.0/categories/of/roles`
- Source controller: `IncidentIQ API`

List role categories

Retrieves categories used to group roles and permission sets. This is useful for building role selection UIs that follow the same hierarchy visible in the IncidentIQ admin screens.

**Workflow Example**
1. Request top-level role categories with no ParentCategoryId.
2. Use a returned CategoryId as ParentCategoryId to drill into subcategories.

**Minimal Required Fields**: none (ParentCategoryId is optional).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `product_filter_type` | `ProductFilterType` | `query` | `no` | `str` | `-` | Filter by product scope |
| `parent_category_id` | `ParentCategoryId` | `query` | `no` | `str` | `-` | Filter to children of a specific parent category |
| `apply_site_visibility` | `ApplySiteVisibility` | `query` | `no` | `bool` | `-` | Whether to apply site-level visibility rules |

#### Returns

- Typed call return: `CategoryListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CategoryListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `search_categories_v1`

Provenance: Golden OpenAPI contract

Operation ID: `searchCategoriesV1`

- Sync: `client.categories.search_categories_v1(body=..., timeout=None)`
- Async: `await client.categories.search_categories_v1(body=..., timeout=None)`
- Raw payload: `client.categories.search_categories_v1.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/categories`
- Source controller: `IncidentIQ API`

Search categories (V1)

**Deprecated**: Use [POST /api/v1.0/categories/v2](#/Categories/searchCategoriesV2) instead.

Searches for categories with flexible filtering options. Supports filtering by category type, site scope, product, and parent category hierarchy.

**Workflow Example**
1. Build your filter criteria including CategoryTypeIds, SiteScope, and product options.
2. [POST /api/v1.0/categories](#/Categories/searchCategoriesV1) with the request body to retrieve matching categories.
3. Extract `Items[].CategoryId` for downstream operations.

**Minimal Required Fields**: none (empty body returns all categories); add CategoryTypeIds or ParentCategoryId to filter results.

**Note**: Prefer the V2 endpoint [POST /api/v1.0/categories/v2](#/Categories/searchCategoriesV2) for new integrations as it offers enhanced filtering via RequestOptions.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `GetCategoriesRequestV1` | `GetCategoriesRequestV1` | - |

#### Returns

- Typed call return: `CategoryListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CategoryListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `search_categories_v2`

Provenance: Golden OpenAPI contract

Operation ID: `searchCategoriesV2`

- Sync: `client.categories.search_categories_v2(body=..., timeout=None)`
- Async: `await client.categories.search_categories_v2(body=..., timeout=None)`
- Raw payload: `client.categories.search_categories_v2.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/categories/v2`
- Source controller: `IncidentIQ API`

Search categories (V2)

Searches categories using a JSON body with RequestOptions filters and paging. This is the preferred method when you need facet-style filters, product scoping, or custom visibility logic beyond the simple query parameters of the GET variant.

**Workflow Example**
1. Build filters in RequestOptions.Filters and optional paging in RequestOptions.Paging.
2. [POST /api/v1.0/categories/v2](#/Categories/searchCategoriesV2) and extract matching CategoryId values for downstream operations.

**Minimal Required Fields**: none (an empty object is allowed); add RequestOptions.Filters for targeted searches.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `GetCategoriesRequest` | `GetCategoriesRequest` | - |

#### Returns

- Typed call return: `CategoryListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CategoryListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `set_category_sort_order`

Provenance: Golden OpenAPI contract

Operation ID: `setCategorySortOrder`

- Sync: `client.categories.set_category_sort_order(category_id=..., sort_order=..., timeout=None)`
- Async: `await client.categories.set_category_sort_order(category_id=..., sort_order=..., timeout=None)`
- Raw payload: `client.categories.set_category_sort_order.raw(category_id=..., sort_order=..., timeout=None)`
- HTTP route: `POST /api/v1.0/categories/{CategoryId}/sortorder/{SortOrder}`
- Source controller: `IncidentIQ API`

Set category sort order

Updates the display sort order for a category within its type and parent scope. Lower numbers appear earlier in lists, so use this to tune UI ordering without changing names or hierarchy.

**Prerequisites**
1. **CategoryId** - Use [POST /api/v1.0/categories/v2](#/Categories/searchCategoriesV2) to locate the category and extract `Items[].CategoryId`.

**Workflow Example**
1. Search for the category you want to reorder.
2. [POST /api/v1.0/categories/{CategoryId}/sortorder/{SortOrder}](#/Categories/setCategorySortOrder) with the new order value.

**Minimal Required Fields**: CategoryId (path), SortOrder (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `category_id` | `CategoryId` | `path` | `yes` | `str` | `-` | Unique identifier of the category |
| `sort_order` | `SortOrder` | `path` | `yes` | `int` | `-` | New sort order value (lower numbers appear first) |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `undelete_category`

Provenance: Golden OpenAPI contract

Operation ID: `undeleteCategory`

- Sync: `client.categories.undelete_category(category_id=..., timeout=None)`
- Async: `await client.categories.undelete_category(category_id=..., timeout=None)`
- Raw payload: `client.categories.undelete_category.raw(category_id=..., timeout=None)`
- HTTP route: `PUT /api/v1.0/categories/{CategoryId}/undelete`
- Source controller: `IncidentIQ API`

Restore a deleted category

Restores a previously deleted category so it becomes active and visible again in category lists and pickers. Use this after an accidental deletion or when you need to re-enable a retired category.

**Prerequisites**
1. **CategoryId** - Capture the ID before deletion (for example, from [POST /api/v1.0/categories/v2](#/Categories/searchCategoriesV2)) and store it for restore operations.

**Workflow Example**
1. Identify the deleted CategoryId to restore.
2. [PUT /api/v1.0/categories/{CategoryId}/undelete](#/Categories/undeleteCategory) to reactivate it.

**Minimal Required Fields**: CategoryId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `category_id` | `CategoryId` | `path` | `yes` | `str` | `-` | Unique identifier of the category to restore |

#### Returns

- Typed call return: `CategoryItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `CategoryItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `unlink_category_from_app`

Provenance: Golden OpenAPI contract

Operation ID: `unlinkCategoryFromApp`

- Sync: `client.categories.unlink_category_from_app(category_id=..., app_id=..., timeout=None)`
- Async: `await client.categories.unlink_category_from_app(category_id=..., app_id=..., timeout=None)`
- Raw payload: `client.categories.unlink_category_from_app.raw(category_id=..., app_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/categories/{CategoryId}/link/app/{AppId}`
- Source controller: `IncidentIQ API`

Unlink category from app

Removes an existing link between a category and an application so the category no longer appears under that app. Use this when an app should stop exposing a category.

**Prerequisites**
1. **CategoryId** - Use [POST /api/v1.0/categories/v2](#/Categories/searchCategoriesV2) to find categories and extract `Items[].CategoryId`.
2. **AppId** - Use [GET /api/v1.0/categories/app-links](#/Categories/listAppCategoryLinks) to discover app identifiers; extract `Items[].AppId`.

**Workflow Example**
1. Review existing links with [GET /api/v1.0/categories/app-links](#/Categories/listAppCategoryLinks).
2. [DELETE /api/v1.0/categories/{CategoryId}/link/app/{AppId}](#/Categories/unlinkCategoryFromApp) to remove the link.

**Minimal Required Fields**: CategoryId (path), AppId (path).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `category_id` | `CategoryId` | `path` | `yes` | `str` | `-` | Unique identifier of the category |
| `app_id` | `AppId` | `path` | `yes` | `str` | `-` | Application identifier |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_category`

Provenance: Golden OpenAPI contract

Operation ID: `updateCategory`

- Sync: `client.categories.update_category(category_id=..., body=..., timeout=None)`
- Async: `await client.categories.update_category(category_id=..., body=..., timeout=None)`
- Raw payload: `client.categories.update_category.raw(category_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/categories/{CategoryId}`
- Source controller: `IncidentIQ API`

Update a category

Updates an existing category's name, description, hierarchy, or display metadata. The CategoryId in the path is authoritative and overrides any CategoryId in the body, so use the path to target the record and send only the fields you intend to change.

**Prerequisites**
1. **CategoryId** - Use [POST /api/v1.0/categories/v2](#/Categories/searchCategoriesV2) to locate categories and extract `Items[].CategoryId`.
2. **CategoryTypeId** - From the same response, capture `Items[].CategoryTypeId` for the category you are updating.

**Workflow Example**
1. Search categories with [POST /api/v1.0/categories/v2](#/Categories/searchCategoriesV2) and identify the category.
2. [POST /api/v1.0/categories/{CategoryId}](#/Categories/updateCategory) with the updated fields.

**Minimal Required Fields**: CategoryId (path) plus request body fields CategoryId, CategoryTypeId, Name.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `category_id` | `CategoryId` | `path` | `yes` | `str` | `-` | Unique identifier of the category to update |
| `body` | `body` | `body` | `yes` | `Category` | `Category` | - |

#### Returns

- Typed call return: `UpdateCategoryResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UpdateCategoryResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
