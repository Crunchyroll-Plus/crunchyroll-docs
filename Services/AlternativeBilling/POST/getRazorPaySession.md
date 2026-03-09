getRazorPaySession
===========

#### Gets the razor pay session

```http
POST /accounts/v1/device

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