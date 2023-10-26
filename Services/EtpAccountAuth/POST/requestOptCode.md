requestOptCode
===========

#### Request an opt code.

```http
POST /accounts/v1/phone/verify

# Request Headers
Content-Type: application/json
Authorization: Bearer ${TOKEN}

# Request Body
{
  "phone_number": "${phone_number}"
}
```