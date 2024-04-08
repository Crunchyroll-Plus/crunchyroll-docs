getWatchHistory
===========

#### Get items from your watch history.

```http
GET content/v2/${account_id}/watch-history

# Request Headers
Authorization: Bearer ${TOKEN}
```

| Parameter | Type | Description |
| --- | --- | --- |
| page_size | `int` | Amount of items to return |
| page | `int` | What page to start searching |

