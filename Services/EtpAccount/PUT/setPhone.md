setPhone
===========

#### Set your phone number.

```http
PUT /accounts/v1/phone

# Request Headers
Content-Type: application/json
Authorization: Bearer ${TOKEN}

# Request Body
{
  "phone_number": "${phone_number}",
  "verification_code": "${verification_code}"
}
```