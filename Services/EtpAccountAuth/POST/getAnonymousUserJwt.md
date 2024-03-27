getAnonymousUserJwt
===========

#### Get a token used for browsing content.

```http
POST /auth/v1/token

# Request Headers
Authorization: Basic bm9haWhkZXZtXzZpeWcwYThsMHE6
ETP-Anonymous-ID: ${ETP_ID}

# Request Body

"device_name=${deviceName}&device_id=${deviceId}&device_type=${deviceType}&grant_type=client_id"
```
