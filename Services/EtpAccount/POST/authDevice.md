authDevice
===========

#### Authenticate a device code.

```http
POST /accounts/v1/device

# Request Headers
Content-Type: application/json
Authorization: Bearer ${TOKEN}

# Request Body
{
  "user_code": "${user_code}"
}
```