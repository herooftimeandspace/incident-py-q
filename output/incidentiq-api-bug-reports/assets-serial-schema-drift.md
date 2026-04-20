# IncidentIQ API Bug Report: Asset Serial Response Schema Drift

## Summary

`GET /assets/serial/{Serial}` returns `200 OK` in live tenant traffic and in Postman, but the published Stoplight contract for `Asset_GetAssetsBySerial` marks several fields as required even though the live response omits them.

## Affected Route

- Route: `GET /assets/serial/{Serial}`
- Published operation: `Asset_GetAssetsBySerial`
- Published response model: `ListGetResponseOfAsset`

## Observed SDK Failure

The Golden SDK path `client.assets.get_assets_by_serial(...)` raises `SchemaValidationError` when response validation is enabled because the live payload does not satisfy the published required-field list.

## Exact Required-Field Mismatches

The live response omits these fields that the published schema currently requires:

- `Asset`: `IsTraining`
- `Asset`: `IsReadOnly`
- `Asset`: `IsExternallyManaged`
- `AssetCustomFieldValue`: `AssetId`
- `Site`: `DefaultWorkflowId`
- `Site`: `DefaultWorkflowInitialStepId`
- `Site`: `EnableAnalytics`
- `Site`: `EnableUsersnap`

## Reproduction Notes

- Postman call to `GET {{BaseURL}}/assets/serial/<serial>` returns `200 OK`.
- The response shape includes a populated `Items` array and standard envelope metadata.
- The failure is not the route itself. The failure occurs during schema validation against the published Stoplight contract.

## Impact

- Golden SDK callers see a validation failure for a route that works in practice.
- A Silver-only workaround was added locally so `client.silver.assets.get_asset_by_serial(...)` can be used as a tactical compatibility path without weakening the Golden contract.

## Requested Upstream Action

- Align the published Stoplight schema for `Asset_GetAssetsBySerial` with the live response shape, or
- Update the live service to return the fields that the published schema marks as required.

Until that alignment happens, published-contract consumers cannot reliably validate successful serial-lookup responses from this route.
