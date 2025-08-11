signIn
===========

If you're having trouble finding a working Basic token, try the [dump_basic](../../../Tools/dump_basic.py) script.

#### Sign in with an email and password

```http
POST /auth/v1/token

# Request Headers
Authorization: Basic eHVuaWh2ZWRidDNtYmlzdWhldnQ6MWtJUzVkeVR2akUwX3JxYUEzWWVBaDBiVVhVbXhXMTE=
ETP-Anonymous-ID: ${ETP_ID}
Content-Type: application/x-www-form-urlencoded

# Request Body

"scope=offline_access&device_name=${deviceName}&device_id=${deviceId}&device_type=${deviceType}&grant_type=password&username=${email}&password=${password}"
```
