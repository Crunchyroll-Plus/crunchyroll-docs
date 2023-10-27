search
===========

#### Search the Crunchyroll's database based on queries.

```http
GET /content/v2/discover/search

# Request Headers
Authorization: Bearer ${TOKEN}
```

| Parameter | Type | Description |
| --- | --- | --- |
| n | `int` | Amount of items to return |
| start | `int` | Where to start searching |
| categories | `array` | Array of categories |
| type | `music,series,episode,top_results,movie_listing` | Type of item to search |
| q | `string` | Query to search for |
| seasonal_tag | `string` | The seasonal tag to search |
