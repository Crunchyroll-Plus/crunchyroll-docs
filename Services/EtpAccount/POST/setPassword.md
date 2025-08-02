setPassword
===========

#### Set your password (if you forgot to??).

```http
POST /accounts/v1/me/set_password

# Request Headers
Content-Type: application/json
Authorization: Bearer ${TOKEN}

# Request Body
{
  "password": "${password}"
}
```