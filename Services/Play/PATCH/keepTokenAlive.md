keepTokenAlive
===========

#### Keeps the token alive.

```http
PATCH /playback/v1/token/${contentId}/${videoToken}/keepAlive

# Request Headers
Authorization: Bearer ${TOKEN}
```

| Parameter | Type | Description |
| --- | --- | --- |
| playhead | `long` | Assuming it's the current time you're watching video at. |