savePlayhead
===========

#### Save a playhead.

```http
POST /content/v2/${account_uuid}/playheads

# Request Headers
Content-Type: application/json
Authorization: Bearer ${TOKEN}

# Request Body
{
  "content_id": "${content_id}",
  "playhead": ${playhead}
}
```