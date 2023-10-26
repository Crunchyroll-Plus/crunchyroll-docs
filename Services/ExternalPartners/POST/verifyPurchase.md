verifyPurchase
===========

#### Verify a purchase from google play.

```http
POST /partners/v2/google-play/verify-purchase

# Request Headers
Content-Type: application/json
Authorization: Bearer ${TOKEN}

# Request Body
package_name=${package_name}&sku=${sku}&purchase_token=${purchase_token}
```