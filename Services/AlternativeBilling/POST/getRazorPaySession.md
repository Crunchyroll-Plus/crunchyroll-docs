getRazorPaySession
===========

#### Gets the razor pay session

```http
POST /v1/razorpaySession

# Request Headers
Content-Type: application/json
Authorization: Bearer ${TOKEN}

# Request Body
{
  "accountId": "${accountId}",
  "accountUuid": "${accountUuid}",
  "customer": {
    "email": "${email}",
    "name": "${name}",
    "phone": "${phone}"
  },
  "maxAmount": ${maxAmount},
  "subscriberCountryCode": ${countryCode}
}
```
