addWatchlistItem
===========

#### Add a series to your watchlist.

```http
PATCH /content/v2/${account_uuid}/watchlist/${content_id}

# Request Headers
Content-Type: application/json
Authorization: Bearer ${TOKEN}

# Request Body
{
  "is_favorite": "${is_favorite}"
}
```