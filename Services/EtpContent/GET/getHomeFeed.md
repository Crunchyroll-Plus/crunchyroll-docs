getHomeFeed
===========

#### Get the home feed for your account.

```http
GET /content/v2/discover/${account_uuid}/home_feed

# Request Headers
Authorization: Bearer ${TOKEN}
```

| Parameter | Type | Description |
| --- | --- | --- |
| n | `int` | Amount of items to return |
| start | `int` | Where to start searching |
