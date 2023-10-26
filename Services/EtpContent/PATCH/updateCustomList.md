updateCustomList
===========

#### Update a custom list.

```http
PATCH /content/v2/${account_uuid}/custom-lists/${list_id}

# Request Headers
Content-Type: application/json
Authorization: Bearer ${TOKEN}

# Request Body
{
  "title": "${TITLE}"
}
```