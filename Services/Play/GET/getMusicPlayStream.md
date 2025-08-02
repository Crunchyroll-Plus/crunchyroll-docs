getMusicPlayStream
===========

#### Get music stream.

```http
GET /v1/music/{contentId}/${android,web}/${phone,firefox}/play
# Request Headers
Authorization: Bearer ${TOKEN}
x-cr-stream-limits: ${true|false}
```

| Parameter | Type | Description |
| --- | --- | --- |
| queue | `boolean` | Not sure. |
| ttloverride | `long` | Not sure. |