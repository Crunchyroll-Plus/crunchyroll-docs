signIn
===========

#### Sign in with an email and password

```http
POST /auth/v1/token

# Request Headers
Authorization: Basic ${KEY}
ETP-Anonymous-ID: ${ETP_ID}

# Request Body

scope=offline_access&device_name=${deviceName}&device_id=${deviceId}&device_type$={deviceType}&grant_type=password&username=${email}&password=${password}
```
