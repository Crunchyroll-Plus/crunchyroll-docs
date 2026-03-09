getDownloadToken
===========

#### Get download token.

```http
GET /playback/v2/{contentId}/android/phone/download

# Request Headers
Authorization: Bearer ${TOKEN}
```

| Parameter | Type | Description |
| --- | --- | --- |
| resolution | `int` | Resolution for the video. |
| relativeExpiration | `long` | I'm unsure what this is for. |
| playDuration | `long` | Duration for the video token to stay valid for. |
