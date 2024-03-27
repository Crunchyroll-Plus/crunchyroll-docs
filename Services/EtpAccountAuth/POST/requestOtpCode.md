requestOtpCode
===========

#### Request an otp code.

```http
POST /accounts/v1/phone/verify

# Request Headers
Content-Type: application/json
Authorization: Basic bm9haWhkZXZtXzZpeWcwYThsMHE6

# Request Body
{
  "phone_number": "${phone_number}",
  "channel": "${sms|whatsapp}"
}
```
