requestOptCode
===========

#### Request an opt code.

```http
POST /accounts/v1/phone/verify

# Request Headers
Content-Type: application/json
# I'm quite unsure which one to use so try Basic then Bearer
Authorization: Basic ${CLIENT_ID}

# Request Body
{
  "phone_number": "${phone_number}"
}
```
