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
| type | `array<episode,series,movie_listing,music,music_video>` | Type of item to search |
| q | `string` | Query to search for |
| seasonal_tag | `string` | The seasonal tag to search |
| is_dubbed | `boolean` | Whether the item is dubbed |
| is_subbed | `boolean` | Whether the item is subbed |
| is_mature | `boolean` | Whether the item is mature |
| is_simulcast | `boolean` | Whether the item is simulcast |