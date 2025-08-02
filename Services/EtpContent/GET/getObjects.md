getObjects
===========

#### Get objects from content_ids.

```http
GET /content/v2/cms/${account_uuid}/objects/${content_ids}

# Request Headers
Authorization: Bearer ${TOKEN}
```

| Parameter | Type | Description |
| --- | --- | --- |
| fields | `array<id,images>` | Fields to return |
