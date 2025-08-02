changeCustomListItemPosition
===========

#### Change the position of a series in a custom list.

```http
POST /content/v2/${account_uuid}/custom-lists/${list_id}/${series_id}/position

# Request Headers
Content-Type: application/json
Authorization: Bearer ${TOKEN}

# Request Body
{
  "location": ${LOCATION}
}
```