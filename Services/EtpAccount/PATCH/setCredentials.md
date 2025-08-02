setCredentials
===========

#### Change account credentials.

```http
PATCH /accounts/v1/me/credentials

# Request Headers
Content-Type: application/json
Authorization: Bearer ${TOKEN}

# Request Body
## Set Username
{
  "username": "${username}"
}
## Set Password
{
    "current_password": "${current_password}"
    "new_password": "${new_password}"
}
```
