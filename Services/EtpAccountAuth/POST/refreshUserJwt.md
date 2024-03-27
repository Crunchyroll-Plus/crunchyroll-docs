refreshUserJwt
===========

#### Get a new token using the refresh_token

```http
POST /auth/v1/token

# Request Headers
Authorization: Basic bm9haWhkZXZtXzZpeWcwYThsMHE6
ETP-Anonymous-ID: ${ETP_ID}

# Request Body

"scope=offline_access&device_name=${deviceName}&device_id=${deviceId}&device_type=${deviceType}&grant_type=refresh_token&refresh_token=${refresh_token}"
```
