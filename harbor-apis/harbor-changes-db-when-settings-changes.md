<!-- Space: RD -->
<!-- Title: When a settings changed in Harbor, what changes will be made to DB? -->
# When a settings changed in Harbor, what changes will be made to DB?
Tried to update default project quota settings to 1GB:
If value is divisible to 1024, you can see output to suitable unit instead of bytes 
- properties (INSERT)
```json
{
  "id": 12,
  "k": "storage_per_project",
  "v": "1073741824"
}
```

