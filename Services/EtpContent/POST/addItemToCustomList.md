addItemToCustomList
===========

#### Add a series to a custom list.

```http
POST /content/v2/${account_uuid}/custom-lists/${list_id}

# Request Headers
Content-Type: application/json
Authorization: Bearer ${TOKEN}

# Request Body
{
  "content_id": "${SERIES_ID}"
}
```