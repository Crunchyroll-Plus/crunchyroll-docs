getAuthenticationUrls
===========

#### Get the platform's authorization url.

```http
GET /third-party-oauth/v1/${platform}/authorize_url

# Request Headers
Authorization: Bearer ${TOKEN}
```

| Parameter | Type | Description |
| --- | --- | --- |
| callback_redirect | `string` | Url to redirect to when you're finished |
