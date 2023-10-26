migrateWatchData
===========

#### Migrate funimation watch data.

```http
POST /fun-migrator/v1/watch-data/${account_uuid}/migrate/${not_migrated|in_progress|skip|merge|overwrite}

# Request Headers
Authorization: Bearer ${TOKEN}
```