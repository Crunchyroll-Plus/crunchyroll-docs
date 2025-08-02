addWatchlistItem
===========

#### Add a series to your watchlist.

```http
POST /content/v2/${account_uuid}/watchlist

# Request Headers
Content-Type: application/json
Authorization: Bearer ${TOKEN}

# Request Body
{
  "content_id": "${SERIES_ID}"
}
```