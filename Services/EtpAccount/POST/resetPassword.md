resetPassword
===========

#### Reset your password.

```http
POST /accounts/v1/password_forgot

# Request Headers
Content-Type: application/json
Authorization: Bearer ${TOKEN}

# Request Body
{
  "email": "${email}"
}
```