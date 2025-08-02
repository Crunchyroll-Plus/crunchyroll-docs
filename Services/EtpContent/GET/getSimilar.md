getSimilar
===========

#### Get series similar to the _id.

```http
GET /content/v2/discover/${account_uuid}/similar_to/${series_id}

# Request Headers
Authorization: Bearer ${TOKEN}
```

| Parameter | Type | Description |
| --- | --- | --- |
| n | `int` | Amount of items to return |
| start | `int` | Where to start searching |
