createPrivateCustomList
===========

#### Create a Custom List.

```http
POST /content/v2/${account_uuid}/custom-lists

# Request Headers
Content-Type: application/json
Authorization: Bearer ${TOKEN}

# Request Body
{
  "title": "${TITLE}"
}
```