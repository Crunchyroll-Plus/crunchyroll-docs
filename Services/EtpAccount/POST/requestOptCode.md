requestOptCode
===========

#### Request a phone verification id.

```http
POST /accounts/v1/phone/verify

# Request Headers
Content-Type: application/json

# Request Body
{
  "phone_number": "${phone_number}"
}
```