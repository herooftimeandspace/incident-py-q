# `files` Golden Namespace

Sync client access: `client.files`

Async client access: `client.files` with `await` on method calls.

These methods are Golden because they come from the bundled Incident IQ OpenAPI contract.

## Methods

### `add_file_to_entity`

Provenance: Golden OpenAPI contract

Operation ID: `addFileToEntity`

- Sync: `client.files.add_file_to_entity(file_id=..., entity_type_id=..., entity_id=..., timeout=None)`
- Async: `await client.files.add_file_to_entity(file_id=..., entity_type_id=..., entity_id=..., timeout=None)`
- Raw payload: `client.files.add_file_to_entity.raw(file_id=..., entity_type_id=..., entity_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/files/{FileId}/entity/{EntityTypeId}/{EntityId}`
- Source controller: `IncidentIQ API`

Link file to entity

Creates an association between an uploaded file and a specific entity (ticket, asset, user, etc.). This links the file to the entity so it appears in that entity's attachments.

**Prerequisites**
1. **FileId** - Upload a file first using [POST /api/v1.0/files](#/Files/uploadFile) to obtain the FileId
2. **EntityTypeId** - Get entity type UUIDs from [GET /api/v1.0/entity-types](#/Custom Fields/getCustomFieldEntityMappingEntityTypes)
3. **EntityId** - The UUID of the specific entity (ticket, asset, user) to link the file to

**Workflow Example**
1. Upload file: [POST /api/v1.0/files](#/Files/uploadFile) → extract `Item.FileId`
2. Get entity type ID for 'Ticket' from entity types list
3. Link file to ticket: POST to this endpoint with FileId, EntityTypeId, and TicketId
4. File now appears in ticket's attachments

**Common Entity Types**: Ticket, Asset, User, Location, Room

**Notes**: A single file can be linked to multiple entities. Unlinking a file from all entities does not delete the file itself. Use [DELETE /api/v1.0/files/{FileId}](#/Files/deleteFile) to remove the file.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `file_id` | `FileId` | `path` | `yes` | `str` | `-` | - |
| `entity_type_id` | `EntityTypeId` | `path` | `yes` | `str` | `-` | - |
| `entity_id` | `EntityId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `convert_to_excel`

Provenance: Golden OpenAPI contract

Operation ID: `convertToExcel`

- Sync: `client.files.convert_to_excel(body=..., timeout=None)`
- Async: `await client.files.convert_to_excel(body=..., timeout=None)`
- Raw payload: `client.files.convert_to_excel.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/files/convert-to-excel`
- Source controller: `IncidentIQ API`

Convert data to Excel file

Converts a JSON data structure into an Excel (.xlsx) file and returns a temporary download URL. Use this to generate Excel exports from structured data without client-side Excel libraries.

**Workflow Example**
1. Prepare column definitions with headers and data types
2. Prepare row data as arrays matching the column structure
3. POST the data structure to this endpoint
4. Receive a temporary download URL in the response
5. Download the Excel file using [GET /api/v1.0/files/excel/{FileId}](#/Files/getExcelFile)

**Request Structure**:
- `Columns`: Array of column definitions with Name, DisplayName, and optional formatting
- `Rows`: Array of row arrays containing cell values matching column order

**Use Cases**:
- Exporting search results to Excel
- Generating custom reports
- Creating data exports for offline analysis

**Notes**: The generated file URL is temporary and expires after a period. Download promptly or store the file permanently using the standard upload endpoints.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `ExcelConversionRequest` | `ExcelConversionRequest` | - |

#### Returns

- Typed call return: `ExcelConversionUrlResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ExcelConversionUrlResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_file`

Provenance: Golden OpenAPI contract

Operation ID: `deleteFile`

- Sync: `client.files.delete_file(file_id=..., timeout=None)`
- Async: `await client.files.delete_file(file_id=..., timeout=None)`
- Raw payload: `client.files.delete_file.raw(file_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/files/{FileId}`
- Source controller: `IncidentIQ API`

Delete a file

Soft-delete a file from the system. The file record is marked as deleted but may be retained for a period before permanent removal.

**Prerequisites**
1. **FileId** - Obtain from file listings on entities, or from [POST /api/v1.0/files](#/Files/uploadFile) upload response.

**Workflow Example**
1. Identify file to delete from entity attachments or file listings.
2. Call this endpoint: [DELETE /api/v1.0/files/{FileId}](#/Files/deleteFile).
3. The file is marked as deleted and no longer accessible.

**Important Notes**:
- Deleting a file does not automatically update references in tickets, custom fields, or other entities.
- File content may be retained for a period before permanent purging.
- This action may be irreversible depending on system configuration.

**Related Endpoints:**
- [GET /api/v1.0/files/{FileId}/details](#/Files/getFileDetails) - Get file metadata before deletion

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `file_id` | `FileId` | `path` | `yes` | `str` | `-` | Unique identifier of the file to delete |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `download_file`

Provenance: Golden OpenAPI contract

Operation ID: `downloadFile`

- Sync: `client.files.download_file(file_id=..., file_name=None, timeout=None)`
- Async: `await client.files.download_file(file_id=..., file_name=None, timeout=None)`
- Raw payload: `client.files.download_file.raw(file_id=..., file_name=None, timeout=None)`
- HTTP route: `GET /api/v1.0/files/{FileId}`
- Source controller: `IncidentIQ API`

Download a file

Download the raw binary content of a file. The response includes appropriate Content-Type and Content-Disposition headers based on the file's MIME type and filename.

**Workflow**: Use [GET /api/v1.0/files/{FileId}/details](#/Files/getFileDetails) first to retrieve file metadata if needed before downloading.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `file_id` | `FileId` | `path` | `yes` | `str` | `-` | Unique identifier of the file to download |
| `file_name` | `FileName` | `query` | `no` | `str` | `-` | Optional filename override for Content-Disposition header. If not provided, the original filename is used. |

#### Returns

- Typed call return: `UnauthorizedError`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `UnauthorizedError`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_excel_file`

Provenance: Golden OpenAPI contract

Operation ID: `getExcelFile`

- Sync: `client.files.get_excel_file(file_id=..., timeout=None)`
- Async: `await client.files.get_excel_file(file_id=..., timeout=None)`
- Raw payload: `client.files.get_excel_file.raw(file_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/files/excel/{FileId}`
- Source controller: `IncidentIQ API`

Download temporary Excel file

Downloads a temporary Excel file that was generated by the system. These files are typically created by export operations or data conversion endpoints.

**Prerequisites**
1. **FileId** - Obtain from [POST /api/v1.0/files/convert-to-excel](#/Files/convertToExcel) response or from export job completion notifications.

**Workflow Example**
1. Request an Excel export or conversion using [POST /api/v1.0/files/convert-to-excel](#/Files/convertToExcel)
2. Extract the FileId from the response URL
3. Download the Excel file using this endpoint
4. Save or process the .xlsx file client-side

**Response Headers**:
- `Content-Type`: `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`
- `Content-Disposition`: `attachment; filename="export.xlsx"`

**Notes**: Temporary Excel files are automatically cleaned up after a period (typically 24 hours). Download and save important exports promptly. For permanent file storage, upload using [POST /api/v1.0/files](#/Files/uploadFile).

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `file_id` | `FileId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `Any`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_file_attachment_content_types`

Provenance: Golden OpenAPI contract

Operation ID: `getFileAttachmentContentTypes`

- Sync: `client.files.get_file_attachment_content_types(timeout=None)`
- Async: `await client.files.get_file_attachment_content_types(timeout=None)`
- Raw payload: `client.files.get_file_attachment_content_types.raw(timeout=None)`
- HTTP route: `GET /api/v1.0/files/file-attachment-content-types`
- Source controller: `IncidentIQ API`

Get allowed file content types

Retrieves the list of allowed file content types for attachments. Use this endpoint to determine which file formats are permitted for upload before attempting to upload a file.

**Use Cases**:
- Validate file type client-side before upload
- Display allowed file types to users in upload dialogs
- Filter file picker by supported extensions
- Map MIME types to display icons

**Authentication**: This endpoint supports both user authentication and app authorization tokens.

#### Parameters

This operation does not define request parameters.

#### Returns

- Typed call return: `FileContentTypeListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `FileContentTypeListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_file_base64`

Provenance: Golden OpenAPI contract

Operation ID: `getFileBase64`

- Sync: `client.files.get_file_base64(file_id=..., timeout=None)`
- Async: `await client.files.get_file_base64(file_id=..., timeout=None)`
- Raw payload: `client.files.get_file_base64.raw(file_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/files/base64/{FileId}`
- Source controller: `IncidentIQ API`

Get file content as Base64

Retrieves file content as a Base64-encoded string within a JSON response. This is useful when working with JSON-only clients or when you need to embed file content directly in data structures.

**Prerequisites**
1. **FileId** - Obtain from [POST /api/v1.0/files](#/Files/uploadFile) when uploading, or from file listings on entities.

**Workflow Example**
1. Get file ID from an entity's attachments or upload response
2. Call this endpoint to retrieve Base64-encoded content
3. Decode the Base64 string client-side to reconstruct the file
4. Display inline (for images) or save to disk

**Use Cases**:
- Embedding images in HTML data URIs: `data:image/png;base64,{Content}`
- Transferring files through JSON-only APIs
- Storing file content in JSON documents

**Notes**: Base64 encoding increases data size by ~33%. For large files, prefer [GET /api/v1.0/files/{FileId}](#/Files/downloadFile) for binary download.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `file_id` | `FileId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `Base64FileResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `Base64FileResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_file_details`

Provenance: Golden OpenAPI contract

Operation ID: `getFileDetails`

- Sync: `client.files.get_file_details(file_id=..., timeout=None)`
- Async: `await client.files.get_file_details(file_id=..., timeout=None)`
- Raw payload: `client.files.get_file_details.raw(file_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/files/{FileId}/details`
- Source controller: `IncidentIQ API`

Get file details

Retrieve metadata about a file without downloading its content. Use this endpoint to get information like file size, MIME type, creation date, and upload user before deciding to download.

**Use cases**:
- Preview file information before downloading
- Verify file exists and is accessible
- Get file size for progress indicators
- Check who uploaded a file

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `file_id` | `FileId` | `path` | `yes` | `str` | `-` | Unique identifier of the file |

#### Returns

- Typed call return: `FileGetResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `FileGetResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_file_inline`

Provenance: Golden OpenAPI contract

Operation ID: `getFileInline`

- Sync: `client.files.get_file_inline(file_id=..., timeout=None)`
- Async: `await client.files.get_file_inline(file_id=..., timeout=None)`
- Raw payload: `client.files.get_file_inline.raw(file_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/files/{FileId}/inline`
- Source controller: `IncidentIQ API`

View file inline

Retrieves the file content with `Content-Disposition: inline` header, enabling direct browser display instead of download. Ideal for images, PDFs, and other browser-viewable content.

**Prerequisites**
1. **FileId** - Obtain from file listings on entities, or from [POST /api/v1.0/files](#/Files/uploadFile) upload response.

**Workflow Example**
1. Get file ID from entity attachments (ticket, asset, user profile).
2. Embed URL in `<img>` tag or iframe: `/api/v1.0/files/{FileId}/inline`.
3. Browser displays content directly without download prompt.

**Use Cases**:
- Displaying profile pictures in user interfaces
- Embedding document previews in ticket views
- Showing asset images in inventory screens

**Comparison**:
- This endpoint: `Content-Disposition: inline` for browser display
- [GET /api/v1.0/files/{FileId}](#/Files/downloadFile): `Content-Disposition: attachment` for download

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `file_id` | `FileId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `Any`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_files_for_entity`

Provenance: Golden OpenAPI contract

Operation ID: `getFilesForEntity`

- Sync: `client.files.get_files_for_entity(entity_type_id=..., entity_id=..., timeout=None)`
- Async: `await client.files.get_files_for_entity(entity_type_id=..., entity_id=..., timeout=None)`
- Raw payload: `client.files.get_files_for_entity.raw(entity_type_id=..., entity_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/files/entity/{EntityTypeId}/{EntityId}`
- Source controller: `IncidentIQ API`

Get files for an entity

Retrieves all files associated with a specific entity. This endpoint is commonly used to get files attached to users, assets, tickets, or other entity types.

**Permission Notes**:
- Private files (marked as internal) are only returned if the user has the `USERS_FILES_VIEW_PRIVATE` permission.
- Without this permission, only non-private files are returned.

**Common Entity Types**:
- Users: `EntityTypeId` = User entity type UUID
- Assets: `EntityTypeId` = Asset entity type UUID
- Tickets: `EntityTypeId` = Ticket entity type UUID

**Workflow Example**:
1. Get entity type ID from [GET /api/v1.0/entity-types](#/Custom Fields/getCustomFieldEntityMappingEntityTypes)
2. Call this endpoint with the entity type and specific entity ID
3. Iterate through returned files to display or download

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `entity_type_id` | `EntityTypeId` | `path` | `yes` | `str` | `-` | UUID identifying the type of entity (e.g., User, Asset, Ticket) |
| `entity_id` | `EntityId` | `path` | `yes` | `str` | `-` | UUID of the specific entity to retrieve files for |

#### Returns

- Typed call return: `FileListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `FileListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `parse_barcode`

Provenance: Golden OpenAPI contract

Operation ID: `parseBarcode`

- Sync: `client.files.parse_barcode(body=None, timeout=None)`
- Async: `await client.files.parse_barcode(body=None, timeout=None)`
- Raw payload: `client.files.parse_barcode.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/files/barcode/parse`
- Source controller: `IncidentIQ API`

Parse barcode from image

Uploads an image containing a barcode and extracts the encoded data. Supports common barcode formats including QR codes, Code 128, Code 39, UPC, EAN, and Data Matrix.

**Prerequisites**
1. **Image file** - Prepare an image file (PNG, JPG, GIF) containing a visible barcode. The barcode should be clearly visible and not obscured.

**Workflow Example**
1. Capture or obtain an image containing a barcode (e.g., asset tag photo)
2. Upload the image to this endpoint using multipart/form-data
3. Receive parsed barcode text and format type in response
4. Use the extracted value to search for assets: [POST /api/v1.0/assets/search](#/Assets/searchAssets) with the barcode as AssetTag filter

**Supported Formats**: QR Code, Code 128, Code 39, UPC-A, UPC-E, EAN-13, EAN-8, Data Matrix, PDF417

**Notes**: For best results, ensure the barcode is well-lit, in focus, and occupies a significant portion of the image. Returns empty result if no barcode is detected.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `InlineObject` | `InlineObject` | - |

#### Returns

- Typed call return: `BarcodeResultResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `BarcodeResultResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `parse_excel_column_unique_values`

Provenance: Golden OpenAPI contract

Operation ID: `parseExcelColumnUniqueValues`

- Sync: `client.files.parse_excel_column_unique_values(file_id=..., worksheet_index=..., column_index=..., timeout=None)`
- Async: `await client.files.parse_excel_column_unique_values(file_id=..., worksheet_index=..., column_index=..., timeout=None)`
- Raw payload: `client.files.parse_excel_column_unique_values.raw(file_id=..., worksheet_index=..., column_index=..., timeout=None)`
- HTTP route: `POST /api/v1.0/files/{FileId}/parse-excel/worksheet/{WorksheetIndex}/column/{ColumnIndex}/values`
- Source controller: `IncidentIQ API`

Get unique values from Excel column

Extracts distinct unique values from a specific column in an Excel worksheet. This is useful for building dropdown options, validating data, or understanding the range of values in a column before import.

**Prerequisites**
1. **FileId** - Upload an Excel file using [POST /api/v1.0/files](#/Files/uploadFile) first
2. **WorksheetIndex** - Zero-based index of the worksheet (0 = first sheet)
3. **ColumnIndex** - Zero-based index of the column to extract values from

**Workflow Example**
1. Upload Excel file: [POST /api/v1.0/files](#/Files/uploadFile) → extract `Item.FileId`
2. Preview file structure: [POST /api/v1.0/files/{FileId}/parse-excel/{MaxRows}](#/Files/parseFileAsExcel) to see columns
3. Extract unique values from a column (e.g., column 2): POST to this endpoint
4. Use the values to populate a mapping dropdown or validate import data

**Use Cases**:
- Building field mapping UI for data imports
- Validating column contains expected values before processing
- Generating autocomplete suggestions from spreadsheet data

**Notes**: Empty cells are typically excluded from the unique values list. Very large columns may be truncated.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `file_id` | `FileId` | `path` | `yes` | `str` | `-` | - |
| `worksheet_index` | `WorksheetIndex` | `path` | `yes` | `int` | `-` | - |
| `column_index` | `ColumnIndex` | `path` | `yes` | `int` | `-` | - |

#### Returns

- Typed call return: `ExcelColumnValuesResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ExcelColumnValuesResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `parse_file_as_excel`

Provenance: Golden OpenAPI contract

Operation ID: `parseFileAsExcel`

- Sync: `client.files.parse_file_as_excel(file_id=..., max_rows=..., timeout=None)`
- Async: `await client.files.parse_file_as_excel(file_id=..., max_rows=..., timeout=None)`
- Raw payload: `client.files.parse_file_as_excel.raw(file_id=..., max_rows=..., timeout=None)`
- HTTP route: `POST /api/v1.0/files/{FileId}/parse-excel/{MaxRows}`
- Source controller: `IncidentIQ API`

Parse Excel file content

Parses an uploaded Excel file and returns its content as structured JSON data. Use MaxRows to limit the preview size for large files.

**Prerequisites**
1. **FileId** - Upload an Excel file using [POST /api/v1.0/files](#/Files/uploadFile) to obtain the FileId
2. **MaxRows** - Number of rows to parse (use 10-50 for previews, higher for full processing)

**Workflow Example**
1. Upload Excel file: [POST /api/v1.0/files](#/Files/uploadFile) → extract `Item.FileId`
2. Preview first 10 rows: POST to this endpoint with MaxRows=10
3. Review column headers and data structure in the response
4. For full import, parse with higher MaxRows or process in batches

**Response Structure**:
- `Worksheets`: Array of worksheet data
- Each worksheet contains `Name`, `Columns` (headers), and `Rows` (data arrays)

**Use Cases**:
- Previewing uploaded spreadsheets before import
- Building column mapping interfaces
- Validating file format before bulk processing
- Extracting data for asset or user imports

**Notes**: First row is typically treated as headers. For files without headers, client-side adjustment may be needed.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `file_id` | `FileId` | `path` | `yes` | `str` | `-` | - |
| `max_rows` | `MaxRows` | `path` | `yes` | `int` | `-` | Maximum number of rows to parse from the Excel file |

#### Returns

- Typed call return: `ExcelFileResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ExcelFileResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `remove_file_from_entity`

Provenance: Golden OpenAPI contract

Operation ID: `removeFileFromEntity`

- Sync: `client.files.remove_file_from_entity(file_id=..., entity_type_id=..., entity_id=..., timeout=None)`
- Async: `await client.files.remove_file_from_entity(file_id=..., entity_type_id=..., entity_id=..., timeout=None)`
- Raw payload: `client.files.remove_file_from_entity.raw(file_id=..., entity_type_id=..., entity_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/files/{FileId}/entity/{EntityTypeId}/{EntityId}`
- Source controller: `IncidentIQ API`

Unlink file from entity

Removes the association between a file and a specific entity without deleting the file itself. After unlinking, the file will no longer appear in that entity's attachments.

**Prerequisites**
1. **FileId** - The UUID of the file to unlink
2. **EntityTypeId** - Get entity type UUIDs from [GET /api/v1.0/entity-types](#/Custom Fields/getCustomFieldEntityMappingEntityTypes)
3. **EntityId** - The UUID of the entity to unlink the file from

**Workflow Example**
1. List files for an entity: [GET /api/v1.0/files/entity/{EntityTypeId}/{EntityId}](#/Files/getFilesForEntity)
2. Identify the file to remove from the response
3. Call this endpoint with the FileId, EntityTypeId, and EntityId
4. File is removed from entity's attachments but still exists in the system

**Notes**: 
- Unlinking does not delete the file—it remains accessible via its FileId
- A file linked to multiple entities can be unlinked from one without affecting others
- To permanently delete a file, use [DELETE /api/v1.0/files/{FileId}](#/Files/deleteFile) after unlinking from all entities

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `file_id` | `FileId` | `path` | `yes` | `str` | `-` | - |
| `entity_type_id` | `EntityTypeId` | `path` | `yes` | `str` | `-` | - |
| `entity_id` | `EntityId` | `path` | `yes` | `str` | `-` | - |

#### Returns

- Typed call return: `ItemDeleteResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ItemDeleteResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `upload_file`

Provenance: Golden OpenAPI contract

Operation ID: `uploadFile`

- Sync: `client.files.upload_file(body=..., timeout=None)`
- Async: `await client.files.upload_file(body=..., timeout=None)`
- Raw payload: `client.files.upload_file.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/files`
- Source controller: `IncidentIQ API`

Upload a file

Upload a file using multipart/form-data encoding. The uploaded file is stored in the system and a FileId is returned which can be used to associate the file with tickets, assets, custom fields, or other entities.

**Workflow Example**:
1. Upload file using this endpoint → receive `FileId` in response
2. Associate with ticket custom field: [POST /api/v1.0/tickets/{TicketId}/custom-fields](#/Tickets/updateTicketCustomFields)
3. Or link to any entity: [POST /api/v1.0/files/{FileId}/entity/{EntityTypeId}/{EntityId}](#/Files/addFileToEntity)

**Supported file types**: Images (PNG, JPG, GIF), Documents (PDF, DOC, DOCX, XLS, XLSX), Text files, and other common formats. Maximum file size is typically 25MB but may vary by site configuration.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `UploadFileFilesRequestMultipartFormData` | `UploadFileFilesRequestMultipartFormData` | - |

#### Returns

- Typed call return: `FileUploadResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `FileUploadResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `upload_file_base64`

Provenance: Golden OpenAPI contract

Operation ID: `uploadFileBase64`

- Sync: `client.files.upload_file_base64(body=..., timeout=None)`
- Async: `await client.files.upload_file_base64(body=..., timeout=None)`
- Raw payload: `client.files.upload_file_base64.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/files/base64/save`
- Source controller: `IncidentIQ API`

Upload a file as Base64

Upload a file by providing the content as a Base64-encoded string. This method is useful when:
- Working with JSON-only clients that cannot handle multipart uploads
- Uploading files from base64 data URIs (strip the `data:...;base64,` prefix first)
- Programmatically generating file content

**Workflow Example**:
1. Convert file to Base64 string
2. POST to this endpoint with FileName, Content, and optional FileType
3. Receive `FileId` in response
4. Use FileId to associate with ticket custom fields or attachments

**Note**: Base64 encoding increases payload size by approximately 33%. For large files, prefer the multipart upload endpoint.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `Base64FileUploadRequest` | `Base64FileUploadRequest` | - |

#### Returns

- Typed call return: `FileUploadResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `FileUploadResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `upload_file_return_url`

Provenance: Golden OpenAPI contract

Operation ID: `uploadFileReturnUrl`

- Sync: `client.files.upload_file_return_url(body=None, timeout=None)`
- Async: `await client.files.upload_file_return_url(body=None, timeout=None)`
- Raw payload: `client.files.upload_file_return_url.raw(body=None, timeout=None)`
- HTTP route: `POST /api/v1.0/files/return-as-url`
- Source controller: `IncidentIQ API`

Upload file and return public URL

Uploads a file and immediately returns a publicly accessible URL. This endpoint is optimized for scenarios where you need a shareable link without additional API calls.

**Workflow Example**
1. Select a file to upload (image, document, etc.)
2. POST the file using multipart/form-data
3. Receive the public URL directly in the response body (plain text)
4. Use the URL in emails, notifications, or external integrations

**Use Cases**:
- Embedding images in email notifications
- Sharing screenshots in ticket comments
- Generating preview thumbnails for external systems
- Quick file sharing without managing FileIds

**Comparison with Standard Upload**:
- Standard [POST /api/v1.0/files](#/Files/uploadFile): Returns FileId, requires separate call for URL
- This endpoint: Returns URL directly, simpler for immediate use

**Notes**: The returned URL is publicly accessible. Do not use for sensitive or private files. For controlled access, use the standard upload endpoint and manage permissions via entity associations.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `no` | `InlineObject` | `InlineObject` | - |

#### Returns

- Typed call return: `Any`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: Raw JSON payload
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
