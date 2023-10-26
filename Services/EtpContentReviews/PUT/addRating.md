addRating
===========

#### Add rating.

```http
PUT /content/v2/user/${account_uuid}/rating/${episode|series|movie_listing}/${content_id}

# Request Headers
Content-Type: application/json
Authorization: Bearer ${TOKEN}

# Request Body
## Rate episode
{
  "rating": "${up|down}",
}
## Rate others
{
  "rating": "${1s|2s|3s|4s|5s}" 
}
```