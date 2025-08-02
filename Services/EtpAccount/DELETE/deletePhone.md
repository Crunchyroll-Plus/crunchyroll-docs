deleteProfile
===========

#### Delete profile by the id.

```http
DELETE /accounts/v1/me/multiprofile/{profile_uuid}

# Request Headers
Content-Type: application/json
Authorization: Bearer ${TOKEN}

# Request Body
{
    "password": "${password}"
}
```
