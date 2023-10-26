getWatchlist
===========

#### Get items from your watchlist.

```http
GET /content/v2/discover/browse

# Request Headers
Authorization: Bearer ${TOKEN}
```

| Parameter | Type | Description |
| --- | --- | --- |
| n | `int` | Amount of items to return |
| start | `int` | Where to start searching |
| order | `desc,asc` | Which order to sort by |
| type | `series,movie_listing` | The item type to sort by |
| sort_by | `date_updated,date_watched,date_added,alphabetical` | What to sort by |
| is_favorite | `boolean` | Filter if the item is favorited |
| is_dubbed | `boolean` | Whether the item is dubbed |
| is_subbed | `boolean` | Whether the item is subbed |
