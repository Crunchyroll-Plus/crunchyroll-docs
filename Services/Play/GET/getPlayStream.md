getPlayStream
===========

#### Get stream.

```http
GET /v1/${contentId}/${android,web,tv}/${phone,tablet,android_tv,firefox,chrome}/play

# Request Headers
Authorization: Bearer ${TOKEN}
x-cr-stream-limits: ${true|false}
```

| Parameter | Type | Description |
| --- | --- | --- |
| queue | `integer` | queue=0 adds a instance to the playback sessions. queue=1 adds a instance to the queue sessions. Both are limited according to your subscription. |
