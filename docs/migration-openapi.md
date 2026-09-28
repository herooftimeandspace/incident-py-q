# Migrating from the pre-OpenAPI SDK

The Golden contract moved from the retired Stoplight controller specs to the published
[Incident IQ OpenAPI contract](https://scopousiiq.github.io/iiq-docusaurus-docs/docs/api/).
That grew the SDK from 173 to 863 documented operations, renamed most methods, and left a
set of routes undocumented.

## What happened to your code

Nothing breaks on upgrade except one name (see [Requires manual review](#requires-manual-review)).
Every previous method name still resolves: 50 were renamed, 64 moved to
the Silver surface, and the rest were unchanged. The old names are deprecated aliases that
forward to the new location and emit a `DeprecationWarning`, so you can migrate incrementally.

```python
import warnings

warnings.simplefilter("error", DeprecationWarning)  # find every call site to update
```

Aliases are excluded from `client.sdk_inventory()`, which describes the current contract only.

## Requires manual review

One legacy name is now used by a **different** operation, so it could not be aliased without
shadowing a real method. Calling it still works but now reaches a different route. Check these
call sites by hand; `incident_py_q.legacy_alias_conflicts()` returns the same list at runtime.

| Legacy call | Used to call | Now calls | Previous behavior moved to |
| --- | --- | --- | --- |
| `client.tickets.assign_ticket` | `POST /tickets/{TicketId}/sla` | `POST /api/v1.0/tickets/{ticketId}/assign` | `client.tickets.assign_ticket_sla` |

## Routes migrated to the Silver surface

The published contract is a locked allowlist profile and no longer documents these 64
routes. Rather than drop them, they moved to `client.silver.*`. They keep strict response
validation against a pruned copy of the previous contract bundled at
`data/legacy/contract.json`, so behavior is unchanged apart from the namespace.

| Legacy call | New call |
| --- | --- |
| `client.alerts.queue_notification` | `client.silver.alerts.queue_notification` |
| `client.analytics.get_report` | `client.silver.analytics.get_report` |
| `client.analytics.get_report_elements` | `client.silver.analytics.get_report_elements` |
| `client.analytics.get_report_queries` | `client.silver.analytics.get_report_queries` |
| `client.analytics.get_reports` | `client.silver.analytics.get_reports` |
| `client.assets.add_manufacturer_to_site2` | `client.silver.assets.add_manufacturer_to_site2` |
| `client.assets.create_asset_status_type` | `client.silver.assets.create_asset_status_type` |
| `client.assets.delete_asset_funding_type` | `client.silver.assets.delete_asset_funding_type` |
| `client.assets.delete_asset_status_type` | `client.silver.assets.delete_asset_status_type` |
| `client.assets.get_asset_favorites2` | `client.silver.assets.get_asset_favorites2` |
| `client.assets.get_asset_funding_type` | `client.silver.assets.get_asset_funding_type` |
| `client.assets.get_asset_funding_types2` | `client.silver.assets.get_asset_funding_types2` |
| `client.assets.get_assets_by_asset_status_type` | `client.silver.assets.get_assets_by_asset_status_type` |
| `client.assets.get_assets_by_asset_tag` | `client.silver.assets.get_assets_by_asset_tag` |
| `client.assets.get_spare_assets_by_asset_tag` | `client.silver.assets.get_spare_assets_by_asset_tag` |
| `client.assets.get_user_assets2` | `client.silver.assets.get_user_assets2` |
| `client.assets.search_assets_by_asset_tag` | `client.silver.assets.search_assets_by_asset_tag` |
| `client.assets.update_asset_funding_type` | `client.silver.assets.update_asset_funding_type` |
| `client.assets.update_asset_status_type` | `client.silver.assets.update_asset_status_type` |
| `client.custom_fields.delete_custom_fields` | `client.silver.custom_fields.delete_custom_fields` |
| `client.custom_fields.get_custom_fields` | `client.silver.custom_fields.get_custom_fields` |
| `client.forms.submit_form` | `client.silver.forms.submit_form` |
| `client.locations.delete_location` | `client.silver.locations.delete_location` |
| `client.locations.get_all_location_rooms` | `client.silver.locations.get_all_location_rooms` |
| `client.locations.get_location_rooms` | `client.silver.locations.get_location_rooms` |
| `client.locations.get_location_type` | `client.silver.locations.get_location_type` |
| `client.locations.get_location_types` | `client.silver.locations.get_location_types` |
| `client.locations.update_location` | `client.silver.locations.update_location` |
| `client.manufacturers.add_manufacturer_to_site3` | `client.silver.manufacturers.add_manufacturer_to_site3` |
| `client.manufacturers.add_manufacturer_to_site4` | `client.silver.manufacturers.add_manufacturer_to_site4` |
| `client.manufacturers.delete_manufacturer2` | `client.silver.manufacturers.delete_manufacturer2` |
| `client.manufacturers.get_global_manufacturers3` | `client.silver.manufacturers.get_global_manufacturers3` |
| `client.manufacturers.get_global_manufacturers4` | `client.silver.manufacturers.get_global_manufacturers4` |
| `client.manufacturers.get_manufacturer2` | `client.silver.manufacturers.get_manufacturer2` |
| `client.manufacturers.remove_manufacturer_from_site2` | `client.silver.manufacturers.remove_manufacturer_from_site2` |
| `client.manufacturers.update_manufacturer2` | `client.silver.manufacturers.update_manufacturer2` |
| `client.metrics.delete_metric_type` | `client.silver.metrics.delete_metric_type` |
| `client.metrics.get_metric` | `client.silver.metrics.get_metric` |
| `client.metrics.get_metrics_for_sla` | `client.silver.metrics.get_metrics_for_sla` |
| `client.metrics.update_metric` | `client.silver.metrics.update_metric` |
| `client.metrics.update_metric_type` | `client.silver.metrics.update_metric_type` |
| `client.notifications.get_notifications` | `client.silver.notifications.get_notifications` |
| `client.notifications.get_ticket_emails` | `client.silver.notifications.get_ticket_emails` |
| `client.notifications.get_unarchived_notifications` | `client.silver.notifications.get_unarchived_notifications` |
| `client.notifications.get_unread_notifications` | `client.silver.notifications.get_unread_notifications` |
| `client.notifications.mark_all_notifications_archived` | `client.silver.notifications.mark_all_notifications_archived` |
| `client.notifications.mark_all_notifications_read` | `client.silver.notifications.mark_all_notifications_read` |
| `client.notifications.mark_notification_archived` | `client.silver.notifications.mark_notification_archived` |
| `client.notifications.mark_notification_read` | `client.silver.notifications.mark_notification_read` |
| `client.parts.delete_part` | `client.silver.parts.delete_part` |
| `client.parts.delete_part_supplier` | `client.silver.parts.delete_part_supplier` |
| `client.parts.get_part` | `client.silver.parts.get_part` |
| `client.parts.get_part_supplier` | `client.silver.parts.get_part_supplier` |
| `client.parts.get_part_suppliers` | `client.silver.parts.get_part_suppliers` |
| `client.parts.get_parts` | `client.silver.parts.get_parts` |
| `client.parts.update_part` | `client.silver.parts.update_part` |
| `client.parts.update_part_supplier` | `client.silver.parts.update_part_supplier` |
| `client.purchaseorders.delete_purchase_order` | `client.silver.purchaseorders.delete_purchase_order` |
| `client.purchaseorders.get_purchase_order` | `client.silver.purchaseorders.get_purchase_order` |
| `client.purchaseorders.get_purchase_orders` | `client.silver.purchaseorders.get_purchase_orders` |
| `client.purchaseorders.update_purchase_order` | `client.silver.purchaseorders.update_purchase_order` |
| `client.slas.get_sla` | `client.silver.slas.get_sla` |
| `client.slas.update_sla` | `client.silver.slas.update_sla` |
| `client.users.update_user_view` | `client.silver.users.update_user_view` |

## Renamed Golden methods

These 50 routes are still documented, but the new contract renamed their operations.

| Legacy call | New call |
| --- | --- |
| `client.analytics.get_asset_counts_by_verification_location` | `client.analytics.get_asset_verification_counts_by_location` |
| `client.analytics.get_asset_counts_by_verification_type` | `client.analytics.get_asset_verification_counts_by_type` |
| `client.assets.add_user_favorite_asset` | `client.assets.add_asset_favorite` |
| `client.assets.get_asset` | `client.assets.get_asset_by_id` |
| `client.assets.get_asset_favorites` | `client.assets.get_user_favorite_assets` |
| `client.assets.get_asset_funding_types` | `client.assets.list_asset_funding_types` |
| `client.assets.get_asset_status_types` | `client.assets.list_asset_status_types` |
| `client.assets.get_asset_status_types2` | `client.assets.list_asset_status_types_post` |
| `client.assets.get_assets` | `client.assets.search_assets` |
| `client.assets.get_assets_by_location_room` | `client.assets.list_assets_by_room` |
| `client.assets.get_assets_by_serial` | `client.assets.get_asset_by_serial` |
| `client.assets.get_assets_by_storage_unit_number` | `client.assets.list_assets_by_storage_unit` |
| `client.assets.get_assets_count` | `client.assets.count_assets` |
| `client.assets.get_global_manufacturers2` | `client.assets.search_global_manufacturers` |
| `client.assets.get_manufacturer` | `client.assets.get_manufacturer_by_id` |
| `client.assets.get_user_assets` | `client.assets.get_assets_for_user_current` |
| `client.assets.remove_user_favorite_asset` | `client.assets.remove_asset_favorite` |
| `client.custom_fields.get_custom_field` | `client.custom_fields.get_custom_field_by_id` |
| `client.custom_fields.get_custom_field_type` | `client.custom_fields.get_custom_field_type_by_id` |
| `client.custom_fields.get_custom_field_types` | `client.custom_fields.list_custom_field_types` |
| `client.custom_fields.get_custom_field_types2` | `client.custom_fields.search_custom_field_types` |
| `client.custom_fields.get_custom_fields2` | `client.custom_fields.search_custom_fields` |
| `client.issues.get_issue` | `client.issues.get_issue_by_id` |
| `client.issues.get_issue_type` | `client.issues.get_issue_type_by_id` |
| `client.issues.get_issue_types` | `client.issues.search_issue_types` |
| `client.issues.get_issue_types_simple` | `client.issues.list_issue_types` |
| `client.locations.get_location` | `client.locations.get_location_by_id_v2` |
| `client.locations.get_location_room` | `client.locations.get_location_room_by_id` |
| `client.locations.get_locations` | `client.locations.get_all_site_locations_v2` |
| `client.metrics.delete_metric` | `client.metrics.delete_metric_metrics` |
| `client.metrics.get_metric_type` | `client.metrics.get_metric_by_id` |
| `client.metrics.get_metric_types` | `client.metrics.list_metrics` |
| `client.metrics.get_metrics` | `client.metrics.list_metric_metrics` |
| `client.metrics.update_metrics_for_sla` | `client.metrics.create_metric_by_id` |
| `client.slas.delete_sla` | `client.slas.delete_sla_by_id` |
| `client.slas.get_slas` | `client.slas.list_slas` |
| `client.tickets.change_ticket_to_requestor_responded` | `client.tickets.set_ticket_requestor_responded` |
| `client.tickets.change_ticket_to_waiting_on_requestor` | `client.tickets.set_ticket_waiting_on_requestor` |
| `client.tickets.get_ticket_statuses` | `client.tickets.list_ticket_statuses` |
| `client.tickets.un_assign_ticket_from_team` | `client.tickets.unassign_ticket_from_team` |
| `client.tickets.un_assign_ticket_from_user` | `client.tickets.unassign_ticket_from_user` |
| `client.tickets.un_assign_ticket_sla` | `client.tickets.unassign_ticket_sla` |
| `client.tickets.un_confirm_ticket_issue` | `client.tickets.unconfirm_ticket_issue` |
| `client.users.delete_user_view` | `client.users.delete_user_by_id` |
| `client.users.get_agents` | `client.users.search_agents` |
| `client.users.get_agents_legacy` | `client.users.search_agents_legacy_get` |
| `client.users.get_user` | `client.users.get_user_by_id` |
| `client.users.get_user_views` | `client.users.list_user_views` |
| `client.users.get_users` | `client.users.search_users` |
| `client.users.get_users_legacy` | `client.users.search_users_legacy_get` |
