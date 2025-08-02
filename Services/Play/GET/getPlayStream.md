getPlayStream
===========

#### Get stream.

```http
GET /v1/${contentId}/${android,web}/${phone,firefox,chrome}/play

# Request Headers
Authorization: Bearer ${TOKEN}
x-cr-stream-limits: ${true|false}
```

| Parameter | Type | Description |
| --- | --- | --- |
| queue | `boolean` | Not sure. |
| ttloverride | `long` | Not sure. |