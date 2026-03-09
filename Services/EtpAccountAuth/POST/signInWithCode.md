signInWithCode
===========

#### sign in with a code.

```http
POST /auth/v1/token

# Request Headers
Authorization: Basic eHVuaWh2ZWRidDNtYmlzdWhldnQ6MWtJUzVkeVR2akUwX3JxYUEzWWVBaDBiVVhVbXhXMTE=
ETP-Anonymous-ID: ${ETP_ID}
CrPassToken: ${PASS_TOKEN} # Required if the account has a pin

# Request Body

"grant_type=authorization_code&device_name=${deviceName}&device_id=${deviceId}&device_type=${deviceType}&code=${code}&code_verifier=${code_verifier}&scope=offline_access"
```
