setProfilePin
===========

#### Set a pin for a profile.
- See [validateProvidedCredentials](../POST//validateProvidedCredentials.md) for the CrPassToken header.

```http
PUT /accounts/v1/{account_uuid}/pin/{profile_id}

# Request Headers
Content-Type: application/json
Authorization: Bearer ${TOKEN}
CrPassToken: ${PASS_TOKEN}

# Request Body
{
  "pin": "${pin}"
}
```