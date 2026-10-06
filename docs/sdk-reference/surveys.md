# `surveys` Golden Namespace

Sync client access: `client.surveys`

Async client access: `client.surveys` with `await` on method calls.

These methods are Golden because they come from the bundled Incident IQ OpenAPI contract.

## Aliases

| Alias | Canonical Method | Route |
| --- | --- | --- |
| `create` | `create_survey` | `POST /api/v1.0/surveys/new` |

## Methods

### `activate_survey`

Provenance: Golden OpenAPI contract

Operation ID: `activateSurvey`

- Sync: `client.surveys.activate_survey(survey_id=..., timeout=None)`
- Async: `await client.surveys.activate_survey(survey_id=..., timeout=None)`
- Raw payload: `client.surveys.activate_survey.raw(survey_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/surveys/{SurveyId}/activate`
- Source controller: `IncidentIQ API`

Activate a survey

Activates a survey and its linked business rules, allowing it to be assigned to tickets.

**Prerequisites**
1. **SurveyId** - Use [GET /api/v1.0/surveys](#/Surveys/getSurveys) to find the survey. Extract `Item[].SurveyId`.

**Workflow Example**
1. Create survey: [POST /api/v1.0/surveys/new](#/Surveys/createSurvey)
2. Configure questions and settings via [POST /api/v1.0/surveys/{SurveyId}](#/Surveys/updateSurvey)
3. Create rules to assign survey (via Rules API)
4. Activate: GET /api/v1.0/surveys/{SurveyId}/activate

**Effects**:
- Sets `IsActive = true` on the survey
- Activates all linked business rules
- Survey can now be assigned to tickets when rules trigger

**Notes**: Use [GET /api/v1.0/surveys/{SurveyId}/deactivate](#/Surveys/deactivateSurvey) to pause survey assignments.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `survey_id` | `SurveyId` | `path` | `yes` | `str` | `-` | Unique identifier of the survey to activate. |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `create_survey`

Provenance: Golden OpenAPI contract

Operation ID: `createSurvey`

- Sync: `client.surveys.create_survey(body=..., timeout=None)`
- Async: `await client.surveys.create_survey(body=..., timeout=None)`
- Raw payload: `client.surveys.create_survey.raw(body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/surveys/new`
- Source controller: `IncidentIQ API`
- Aliases: `create`

Create a new survey

Creates a new satisfaction survey with questions and configuration settings.

**Workflow Example**
1. Create survey: POST /api/v1.0/surveys/new with survey definition
2. Extract `ItemId` (SurveyId) from response
3. Activate when ready: [GET /api/v1.0/surveys/{SurveyId}/activate](#/Surveys/activateSurvey)
4. Create rule to assign survey to tickets (via Rules API)

**Configuration Options**:
- `ExpirationInDays`: Days before survey expires (null = never)
- `RemindOnDays`: Array of days to send reminders (e.g., [1, 3, 7])
- `Questions`: Array of question definitions with types and required flags

**Notes**: New surveys are created inactive by default. Use activate endpoint when ready to start collecting responses.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `body` | `body` | `yes` | `Survey` | `Survey` | - |

#### Returns

- Typed call return: `SurveyCreateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `SurveyCreateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `deactivate_survey`

Provenance: Golden OpenAPI contract

Operation ID: `deactivateSurvey`

- Sync: `client.surveys.deactivate_survey(survey_id=..., timeout=None)`
- Async: `await client.surveys.deactivate_survey(survey_id=..., timeout=None)`
- Raw payload: `client.surveys.deactivate_survey.raw(survey_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/surveys/{SurveyId}/deactivate`
- Source controller: `IncidentIQ API`

Deactivate a survey

Deactivates a survey and its linked business rules, stopping new assignments.

**Prerequisites**
1. **SurveyId** - Use [GET /api/v1.0/surveys](#/Surveys/getSurveys) to find the survey. Extract `Item[].SurveyId`.

**Workflow Example**
1. Find survey: [GET /api/v1.0/surveys](#/Surveys/getSurveys) -> extract `SurveyId`
2. Deactivate: GET /api/v1.0/surveys/{SurveyId}/deactivate
3. Verify status: [GET /api/v1.0/surveys/{SurveyId}](#/Surveys/getSurvey) -> check `IsActive = false`

**Effects**:
- Sets `IsActive = false` on the survey
- Deactivates all linked business rules
- No new survey assignments will occur
- Existing pending surveys can still be completed

**Notes**: Use [GET /api/v1.0/surveys/{SurveyId}/activate](#/Surveys/activateSurvey) to resume survey assignments.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `survey_id` | `SurveyId` | `path` | `yes` | `str` | `-` | Unique identifier of the survey to deactivate. |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `delete_survey`

Provenance: Golden OpenAPI contract

Operation ID: `deleteSurvey`

- Sync: `client.surveys.delete_survey(survey_id=..., timeout=None)`
- Async: `await client.surveys.delete_survey(survey_id=..., timeout=None)`
- Raw payload: `client.surveys.delete_survey.raw(survey_id=..., timeout=None)`
- HTTP route: `DELETE /api/v1.0/surveys/{SurveyId}`
- Source controller: `IncidentIQ API`

Delete a survey

Permanently deletes a survey and unlinks any associated business rules.

**Prerequisites**
1. **SurveyId** - Use [GET /api/v1.0/surveys](#/Surveys/getSurveys) to find the survey. Extract `Item[].SurveyId`.

**Workflow Example**
1. List surveys: [GET /api/v1.0/surveys](#/Surveys/getSurveys) -> find survey to delete
2. Check linked rules: [GET /api/v1.0/surveys/{SurveyId}/rules](#/Surveys/getSurveyRules)
3. Delete survey: DELETE /api/v1.0/surveys/{SurveyId}

**Warning**: This permanently removes the survey. Linked rules will be updated to remove the survey reference. Historical responses are preserved but orphaned.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `survey_id` | `SurveyId` | `path` | `yes` | `str` | `-` | Unique identifier of the survey to delete. |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `dismiss_survey_for_ticket`

Provenance: Golden OpenAPI contract

Operation ID: `dismissSurveyForTicket`

- Sync: `client.surveys.dismiss_survey_for_ticket(survey_id=..., ticket_id=..., timeout=None)`
- Async: `await client.surveys.dismiss_survey_for_ticket(survey_id=..., ticket_id=..., timeout=None)`
- Raw payload: `client.surveys.dismiss_survey_for_ticket.raw(survey_id=..., ticket_id=..., timeout=None)`
- HTTP route: `POST /api/v1.0/surveys/{SurveyId}/dismiss/ticket/{TicketId}`
- Source controller: `IncidentIQ API`

Dismiss survey for a ticket

Dismisses a pending survey assignment for a ticket without submitting a response.

**Prerequisites**
1. **SurveyId** - Get from pending surveys: [GET /api/v1.0/surveys/{UserId}/pending](#/Surveys/getPendingSurveys). Extract `SurveyId`.
2. **TicketId** - Get from pending surveys. Extract `TicketId`.

**Workflow Example**
1. Get pending surveys: [GET /api/v1.0/surveys/my/pending](#/Surveys/getPendingSurveys)
2. Find survey to dismiss -> extract `SurveyId` and `TicketId`
3. Dismiss: POST /api/v1.0/surveys/{SurveyId}/dismiss/ticket/{TicketId}

**Use Cases**:
- User declines to provide feedback
- Survey no longer relevant
- Clear pending survey notifications

**Notes**: Dismissed surveys won't appear in pending list and won't send further reminders.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `survey_id` | `SurveyId` | `path` | `yes` | `str` | `-` | Unique identifier of the survey. |
| `ticket_id` | `TicketId` | `path` | `yes` | `str` | `-` | Unique identifier of the ticket. |

#### Returns

- Typed call return: `ActionResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `ActionResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_my_pending_surveys`

Provenance: Golden OpenAPI contract

Operation ID: `getMyPendingSurveys`

- Sync: `client.surveys.get_my_pending_surveys(p=None, s=None, o=None, timeout=None)`
- Async: `await client.surveys.get_my_pending_surveys(p=None, s=None, o=None, timeout=None)`
- Raw payload: `client.surveys.get_my_pending_surveys.raw(p=None, s=None, o=None, timeout=None)`
- HTTP route: `GET /api/v1.0/surveys/my/pending`
- Source controller: `IncidentIQ API`

Get my pending surveys

Retrieves pending survey assignments for the currently authenticated user.

**Workflow Example**
1. Get my pending surveys: GET /api/v1.0/surveys/my/pending
2. For each survey, extract `TicketId` and `SurveyId`
3. Get survey details: [GET /api/v1.0/surveys/{SurveyId}](#/Surveys/getSurvey) to see questions
4. Submit response: [POST /api/v1.0/surveys/responses/ticket/{TicketId}](#/Surveys/saveSurveyResponseForTicket)
5. Or dismiss: [POST /api/v1.0/surveys/{SurveyId}/dismiss/ticket/{TicketId}](#/Surveys/dismissSurveyForTicket)

**Use Cases**:
- Show pending survey count in user dashboard
- Build survey completion workflow for end users
- Display survey notifications

**Notes**: This is an alias for [GET /api/v1.0/surveys/{UserId}/pending](#/Surveys/getPendingSurveys) using the current user's ID.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `p` | `$p` | `query` | `no` | `int` | `-` | Page index (zero-based). Use with `$s` for pagination. |
| `s` | `$s` | `query` | `no` | `int` | `-` | Page size (number of records per page). |
| `o` | `$o` | `query` | `no` | `str` | `-` | Sort expression: field name followed by optional direction (e.g., `CreatedDate desc`). Direction can be `asc`, `ascending`, `desc`, or `descending`. Default direction is ascending. Valid sort fields include `CreatedDate`, `ModifiedDate`. |

#### Returns

- Typed call return: `TicketSurveyListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketSurveyListResponse`
- Pagination helper: `client.surveys.get_my_pending_surveys.iter_pages(start_page=1, page_size=100, max_pages=None, p=None, s=None, o=None, timeout=None)`

---

### `get_pending_surveys`

Provenance: Golden OpenAPI contract

Operation ID: `getPendingSurveys`

- Sync: `client.surveys.get_pending_surveys(user_id=..., p=None, s=None, o=None, timeout=None)`
- Async: `await client.surveys.get_pending_surveys(user_id=..., p=None, s=None, o=None, timeout=None)`
- Raw payload: `client.surveys.get_pending_surveys.raw(user_id=..., p=None, s=None, o=None, timeout=None)`
- HTTP route: `GET /api/v1.0/surveys/{UserId}/pending`
- Source controller: `IncidentIQ API`

Get pending surveys for user

Retrieves a list of pending survey assignments for a specific user or the current user.

**Prerequisites**
1. **UserId** - User to check. Use `my` alias for current user: `/api/v1.0/surveys/my/pending`

**Workflow Example**
1. Get pending surveys: GET /api/v1.0/surveys/my/pending (or with UserId)
2. For each pending survey, extract `TicketId` and `SurveyId`
3. Get survey questions: [GET /api/v1.0/surveys/{SurveyId}](#/Surveys/getSurvey)
4. Submit response: [POST /api/v1.0/surveys/responses/ticket/{TicketId}](#/Surveys/saveSurveyResponseForTicket)
5. Or dismiss: [POST /api/v1.0/surveys/{SurveyId}/dismiss/ticket/{TicketId}](#/Surveys/dismissSurveyForTicket)

**Use Cases**:
- Show pending survey notification badge
- Build survey completion UI
- Check if user has outstanding surveys

**Alternate Route**: Use `/api/v1.0/surveys/my/pending` to get pending surveys for the authenticated user.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `user_id` | `UserId` | `path` | `yes` | `str` | `-` | User ID to check pending surveys for. Use the `/surveys/my/pending` route for current user. |
| `p` | `$p` | `query` | `no` | `int` | `-` | Page index (zero-based). Use with `$s` for pagination. |
| `s` | `$s` | `query` | `no` | `int` | `-` | Page size (number of records per page). |
| `o` | `$o` | `query` | `no` | `str` | `-` | Sort expression: field name followed by optional direction (e.g., `CreatedDate desc`). Direction can be `asc`, `ascending`, `desc`, or `descending`. Default direction is ascending. Valid sort fields include `CreatedDate`, `ModifiedDate`. |

#### Returns

- Typed call return: `TicketSurveyListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `TicketSurveyListResponse`
- Pagination helper: `client.surveys.get_pending_surveys.iter_pages(start_page=1, page_size=100, max_pages=None, user_id=..., p=None, s=None, o=None, timeout=None)`

---

### `get_survey`

Provenance: Golden OpenAPI contract

Operation ID: `getSurvey`

- Sync: `client.surveys.get_survey(survey_id=..., timeout=None)`
- Async: `await client.surveys.get_survey(survey_id=..., timeout=None)`
- Raw payload: `client.surveys.get_survey.raw(survey_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/surveys/{SurveyId}`
- Source controller: `IncidentIQ API`

Get survey details

Retrieves a single survey by ID, including all configured questions.

**Prerequisites**
1. **SurveyId** - Use [GET /api/v1.0/surveys](#/Surveys/getSurveys) to list available surveys. Extract `Item[].SurveyId`.

**Workflow Example**
1. List surveys: [GET /api/v1.0/surveys](#/Surveys/getSurveys) -> extract `SurveyId`
2. Get details: GET /api/v1.0/surveys/{SurveyId}
3. Review questions in `Questions[]` array
4. Check linked rules: [GET /api/v1.0/surveys/{SurveyId}/rules](#/Surveys/getSurveyRules)

**Response includes**: Survey metadata, introduction text, expiration settings, reminder schedule, and all question definitions.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `survey_id` | `SurveyId` | `path` | `yes` | `str` | `-` | Unique identifier of the survey to retrieve. |

#### Returns

- Typed call return: `SurveyItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `SurveyItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_survey_response_for_ticket`

Provenance: Golden OpenAPI contract

Operation ID: `getSurveyResponseForTicket`

- Sync: `client.surveys.get_survey_response_for_ticket(ticket_id=..., timeout=None)`
- Async: `await client.surveys.get_survey_response_for_ticket(ticket_id=..., timeout=None)`
- Raw payload: `client.surveys.get_survey_response_for_ticket.raw(ticket_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/surveys/responses/ticket/{TicketId}`
- Source controller: `IncidentIQ API`

Get survey response for a ticket

Retrieves the survey response submitted for a specific ticket, if one exists.

**Prerequisites**
1. **TicketId** - The ticket must have had a survey assigned and completed.

**Workflow Example**
1. Get ticket details (via Tickets API) to confirm ticket ID
2. Check for response: GET /api/v1.0/surveys/responses/ticket/{TicketId}
3. If response exists, review `OverallSatisfaction` and individual `Responses`
4. If no response, check pending: [GET /api/v1.0/surveys/{UserId}/pending](#/Surveys/getPendingSurveys)

**Use Cases**:
- Display satisfaction rating on ticket detail page
- Include survey feedback in ticket reports
- Verify survey was completed before closing follow-up

**Notes**: Returns null `Item` if no survey response exists for the ticket.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `TicketId` | `path` | `yes` | `str` | `-` | Unique identifier of the ticket. |

#### Returns

- Typed call return: `SurveyResponseItemResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `SurveyResponseItemResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_survey_responses`

Provenance: Golden OpenAPI contract

Operation ID: `getSurveyResponses`

- Sync: `client.surveys.get_survey_responses(survey_id=..., p=None, s=None, o=None, timeout=None)`
- Async: `await client.surveys.get_survey_responses(survey_id=..., p=None, s=None, o=None, timeout=None)`
- Raw payload: `client.surveys.get_survey_responses.raw(survey_id=..., p=None, s=None, o=None, timeout=None)`
- HTTP route: `GET /api/v1.0/surveys/responses/{SurveyId}`
- Source controller: `IncidentIQ API`

Get responses for a survey

Retrieves a paginated list of all responses submitted for a specific survey.

**Prerequisites**
1. **SurveyId** - Use [GET /api/v1.0/surveys](#/Surveys/getSurveys) to find the survey. Extract `Item[].SurveyId`.

**Workflow Example**
1. Find survey: [GET /api/v1.0/surveys](#/Surveys/getSurveys) -> extract `SurveyId`
2. Get responses: GET /api/v1.0/surveys/responses/{SurveyId}
3. Analyze `OverallSatisfaction` scores and individual `Responses`
4. For ticket context: Use `TicketId` to look up ticket details

**Use Cases**:
- Generate satisfaction reports
- Identify trends in customer feedback
- Export data for analytics

**Supports**: Pagination (`$p`, `$s`), sorting (`$o`, `$d`), filtering.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `survey_id` | `SurveyId` | `path` | `yes` | `str` | `-` | Unique identifier of the survey. |
| `p` | `$p` | `query` | `no` | `int` | `-` | Page index (zero-based). Use with `$s` for pagination. |
| `s` | `$s` | `query` | `no` | `int` | `-` | Page size (number of records per page). |
| `o` | `$o` | `query` | `no` | `str` | `-` | Sort expression: field name followed by optional direction (e.g., `CreatedDate desc`). Direction can be `asc`, `ascending`, `desc`, or `descending`. Default direction is ascending. Valid sort fields include `CreatedDate`, `ModifiedDate`. |

#### Returns

- Typed call return: `SurveyResponseListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `SurveyResponseListResponse`
- Pagination helper: `client.surveys.get_survey_responses.iter_pages(start_page=1, page_size=100, max_pages=None, survey_id=..., p=None, s=None, o=None, timeout=None)`

---

### `get_survey_rules`

Provenance: Golden OpenAPI contract

Operation ID: `getSurveyRules`

- Sync: `client.surveys.get_survey_rules(survey_id=..., timeout=None)`
- Async: `await client.surveys.get_survey_rules(survey_id=..., timeout=None)`
- Raw payload: `client.surveys.get_survey_rules.raw(survey_id=..., timeout=None)`
- HTTP route: `GET /api/v1.0/surveys/{SurveyId}/rules`
- Source controller: `IncidentIQ API`

Get rules linked to a survey

Retrieves the list of business rules that assign this survey to tickets.

**Prerequisites**
1. **SurveyId** - Use [GET /api/v1.0/surveys](#/Surveys/getSurveys) to find the survey. Extract `Item[].SurveyId`.

**Workflow Example**
1. List surveys: [GET /api/v1.0/surveys](#/Surveys/getSurveys) -> extract `SurveyId`
2. Get linked rules: GET /api/v1.0/surveys/{SurveyId}/rules
3. Review which rules trigger this survey assignment

**Use Cases**:
- Audit which workflows trigger survey assignments
- Verify survey is properly linked before activation
- Troubleshoot why surveys aren't being assigned

**Notes**: Rules use the 'Assign Satisfaction Survey' action type to link surveys to ticket resolution events.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `survey_id` | `SurveyId` | `path` | `yes` | `str` | `-` | Unique identifier of the survey. |

#### Returns

- Typed call return: `SurveyRulesListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `SurveyRulesListResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `get_surveys`

Provenance: Golden OpenAPI contract

Operation ID: `getSurveys`

- Sync: `client.surveys.get_surveys(p=None, s=None, o=None, timeout=None)`
- Async: `await client.surveys.get_surveys(p=None, s=None, o=None, timeout=None)`
- Raw payload: `client.surveys.get_surveys.raw(p=None, s=None, o=None, timeout=None)`
- HTTP route: `GET /api/v1.0/surveys`
- Source controller: `IncidentIQ API`

List all surveys

Retrieves a paginated list of satisfaction surveys configured for the current site.

**Use Cases**
- Display available surveys in admin interface
- Find surveys to assign via rules
- Audit survey configuration across sites

**Workflow Example**
1. List surveys: GET /api/v1.0/surveys
2. Extract `Item[].SurveyId` for surveys you want to manage
3. View details: [GET /api/v1.0/surveys/{SurveyId}](#/Surveys/getSurvey)
4. Check responses: [GET /api/v1.0/surveys/responses/{SurveyId}](#/Surveys/getSurveyResponses)

**Supports**: Pagination (`$p`, `$s`), sorting (`$o`, `$d`), filtering.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `p` | `$p` | `query` | `no` | `int` | `-` | Page index (zero-based). Use with `$s` for pagination. |
| `s` | `$s` | `query` | `no` | `int` | `-` | Page size (number of records per page). |
| `o` | `$o` | `query` | `no` | `str` | `-` | Sort expression: field name followed by optional direction (e.g., `CreatedDate desc`). Direction can be `asc`, `ascending`, `desc`, or `descending`. Default direction is ascending. Valid sort fields include `CreatedDate`, `ModifiedDate`, `Name`. |

#### Returns

- Typed call return: `SurveyListResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `SurveyListResponse`
- Pagination helper: `client.surveys.get_surveys.iter_pages(start_page=1, page_size=100, max_pages=None, p=None, s=None, o=None, timeout=None)`

---

### `save_survey_response_for_ticket`

Provenance: Golden OpenAPI contract

Operation ID: `saveSurveyResponseForTicket`

- Sync: `client.surveys.save_survey_response_for_ticket(ticket_id=..., body=..., timeout=None)`
- Async: `await client.surveys.save_survey_response_for_ticket(ticket_id=..., body=..., timeout=None)`
- Raw payload: `client.surveys.save_survey_response_for_ticket.raw(ticket_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/surveys/responses/ticket/{TicketId}`
- Source controller: `IncidentIQ API`

Save survey response for a ticket

Submits or updates a survey response for a specific ticket.

**Prerequisites**
1. **TicketId** - The ticket must have a pending survey assignment.
2. **SurveyId** - Get from pending surveys: [GET /api/v1.0/surveys/{UserId}/pending](#/Surveys/getPendingSurveys)

**Workflow Example**
1. Get pending surveys: [GET /api/v1.0/surveys/my/pending](#/Surveys/getPendingSurveys) -> find `TicketId` and `SurveyId`
2. Get survey questions: [GET /api/v1.0/surveys/{SurveyId}](#/Surveys/getSurvey) -> review `Questions[]`
3. Submit response: POST /api/v1.0/surveys/responses/ticket/{TicketId}

**Required Fields**: `SurveyId`, `OverallSatisfaction` (1-5)

**Notes**: `OverallSatisfaction` must be between 1-5. Include `Responses` array with answers to each question.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket_id` | `TicketId` | `path` | `yes` | `str` | `-` | Unique identifier of the ticket. |
| `body` | `body` | `body` | `yes` | `SurveyResponse` | `SurveyResponse` | - |

#### Returns

- Typed call return: `SurveyResponseUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `SurveyResponseUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---

### `update_survey`

Provenance: Golden OpenAPI contract

Operation ID: `updateSurvey`

- Sync: `client.surveys.update_survey(survey_id=..., body=..., timeout=None)`
- Async: `await client.surveys.update_survey(survey_id=..., body=..., timeout=None)`
- Raw payload: `client.surveys.update_survey.raw(survey_id=..., body=..., timeout=None)`
- HTTP route: `POST /api/v1.0/surveys/{SurveyId}`
- Source controller: `IncidentIQ API`

Update a survey

Updates an existing survey's configuration, including name, introduction, questions, and settings. Creates the survey if it doesn't exist.

**Prerequisites**
1. **SurveyId** - Use [GET /api/v1.0/surveys](#/Surveys/getSurveys) to find the survey. Extract `Item[].SurveyId`.

**Workflow Example**
1. Get current survey: [GET /api/v1.0/surveys/{SurveyId}](#/Surveys/getSurvey)
2. Modify fields as needed (Name, Intro, Questions, etc.)
3. Update survey: POST /api/v1.0/surveys/{SurveyId} with modified payload
4. If changing activation: Use [GET /api/v1.0/surveys/{SurveyId}/activate](#/Surveys/activateSurvey) or [deactivate](#/Surveys/deactivateSurvey)

**Notes**: Questions are replaced entirely - include all questions in the update, not just changes.

#### Parameters

| Python Arg | API Name | In | Required | Type | Schema / Model | Description |
| --- | --- | --- | --- | --- | --- | --- |
| `survey_id` | `SurveyId` | `path` | `yes` | `str` | `-` | Unique identifier of the survey to update. |
| `body` | `body` | `body` | `yes` | `Survey` | `Survey` | - |

#### Returns

- Typed call return: `SurveyUpdateResponse`
- Raw payload return: `dict[str, Any] | list[Any] | None`
- Response model: `SurveyUpdateResponse`
- Pagination helper: No paging query parameters detected; `iter_pages(...)` returns a single raw response.

---
