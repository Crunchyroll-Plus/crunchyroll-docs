validateProvidedCredentials
===========

#### Validates the provided credentials.

```http
POST /auth/v1/{account_uuid}/passtoken

# Request Headers
Content-Type: application/json
Authorization: Bearer ${TOKEN}
exclude_from_auth_retry: true

# Request Body
{
  "credential_type": "password | verification_code | profile_pin",
  "profile_id": "${profile_id}",
  "value": "${password | otp_code | profile_pin}"
}
```