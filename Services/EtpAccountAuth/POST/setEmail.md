setEmail
===========

#### Set your email.

```http
POST /accounts/v1/phone/set_email

# Request Headers
Content-Type: application/json
Authorization: Bearer ${TOKEN}

# Request Body
{
  "email": "${email}"
}
```