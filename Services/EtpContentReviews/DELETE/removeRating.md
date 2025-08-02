deleteRating
===========

#### Delete rating.

```http
DELETE /content/v2/user/${account_uuid}/rating/${episode|series|movie_listing}/${content_id}

# Request Headers
Authorization: Bearer ${TOKEN}
```

```http
DELETE /content-reviews/v3/user/${account_uuid}/rating/${episode|series|movie_listing|season|musicVideo|musicConcert|game}/${content_id}

# Request Headers
Authorization: Bearer ${TOKEN}
```