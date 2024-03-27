signInOtp
===========

#### Sign in with an otp code

```http
POST /auth/v1/token

# Request Headers
Authorization: Basic bm9haWhkZXZtXzZpeWcwYThsMHE6
ETP-Anonymous-ID: ${ETP_ID}

# Request Body

"scope=offline_access&device_name=${deviceName}&device_id=${deviceId}&device_type=${deviceType}&grant_type=phone&phone_number=${phone_number}&verification_code=${verification_code}"
```
