getAnonymousUserJwt
===========

#### Get a token used for browsing content.

```http
POST /auth/v1/token

# Request Headers
Authorization: Basic eHVuaWh2ZWRidDNtYmlzdWhldnQ6MWtJUzVkeVR2akUwX3JxYUEzWWVBaDBiVVhVbXhXMTE=
ETP-Anonymous-ID: ${ETP_ID}
Content-Type: application/x-www-form-urlencoded

# Request Body

"grant_type=client_id"
```
