<!-- Space: RD -->
<!-- Title: When a project is created in Harbor, what changes will be made to DB? -->
### When a project is created in Harbor, what changes will be made to DB?
- project (INSERT)
```json
{
  "project_id": 20,
  "owner_id": 15,
  "name": "temp_proj",
  "creation_time": "2022-03-07T05:11:30.311753",
  "update_time": "2022-03-07T05:11:30.311753",
  "deleted": false,
  "registry_id": 0
}
```
- project_member (INSERT)
```json
{
  "id": 29,
  "project_id": 20,
  "entity_id": 15,
  "entity_type": "u",
  "role": 1,
  "creation_time": "2022-03-07T05:11:30.311753",
  "update_time": "2022-03-07T05:11:30.311753"
}
```
- cve_allowlist (INSERT)
```json
{
  "id": 21,
  "project_id": 20,
  "creation_time": "2022-03-07T05:11:30.320627",
  "update_time": "2022-03-07T05:11:30.320627",
  "expires_at": null,
  "items": "[]"
}
```
- project_metadata (INSERT)
```json
{
  "id": 30,
  "project_id": 20,
  "name": "public",
  "value": "false",
  "creation_time": "2022-03-07T05:11:30.325184",
  "update_time": "2022-03-07T05:11:30.325184"
}
```
- quota (INSERT)
```json
{
  "id": 20,
  "reference": "project",
  "reference_id": "20",
  "hard": {
    "storage": -1
  },
  "creation_time": "2022-03-07T05:11:30.330528",
  "update_time": "2022-03-07T05:11:30.330528",
  "version": 0
}
```
- quota_usage (INSERT)
```json
{
  "id": 20,
  "reference": "project",
  "reference_id": "20",
  "used": {
    "storage": 0
  },
  "creation_time": "2022-03-07T05:11:30.330528",
  "update_time": "2022-03-07T05:11:30.330528",
  "version": 0
}
```
- audit_log (INSERT)
```json
{
  "id": 323220,
  "project_id": 20,
  "operation": "create",
  "resource_type": "project",
  "resource": "temp_proj",
  "username": "ehsan",
  "op_time": "2022-03-07T05:11:30.348954"
}
```