getMusicPlayStream
===========

#### Get music stream.

```http
GET /playback/v1/music/{contentId}/${android,web,tv}/${phone,tablet,android_tv,firefox,chrome}/play
# Request Headers
Authorization: Bearer ${TOKEN}
```

| Parameter | Type | Description |
| --- | --- | --- |
| queue | `boolean` | queue=0 adds a instance to the playback sessions. queue=1 adds a instance to the queue sessions. Both are limited according to your subscription. |
