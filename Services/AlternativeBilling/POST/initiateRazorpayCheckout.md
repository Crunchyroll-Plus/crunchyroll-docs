initiateRazorpayCheckout
===========

#### initiates the razorpay process.

```http
POST /v1/initiateCheckout

# Request Headers
Content-Type: application/json
Authorization: Bearer ${TOKEN}

# Request Body
{
  "account": {
    "billingAddress": "${billingAddress}",
    "email": "${email}"
  },
  "accountId": "${accountId}",
  "accountUuid": "${accountUuid}",
  "checkoutType": "unsure on what this is supposed to be couldn't figure it out. There is no enum for it just a string.",
  "razorpay": {
    "orderId": "${orderId}",
    "paymentId": "${paymentId}",
    "signature": "${signature}"
  },
  "subscription": {
    "amount": ${amount},
    "currencyCode": "${currencyCode}",
    "free_trial_duration": "${duration}",
    "sku": "${sku}"
  },
  "context": {
    "googleExternalTransactionToken": "${googleExternalTransactionToken}"
  },
  "type": "{type}"
}
```