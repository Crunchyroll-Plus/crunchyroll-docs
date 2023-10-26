getDownloadToken
===========

#### Get download token.

```http
GET /v1/${content_id}/android/phone/download

# Request Headers
Content-Type: application/json
Authorization: Bearer ${TOKEN}
```

| Parameter | Type | Description |
| --- | --- | --- |
| resolution | `int` | Resolution for the video. |
| relativeExpiration | `long` | I'm unsure what this is for. |
| playDuration | `long` | Duration for the video token to stay valid for. |
