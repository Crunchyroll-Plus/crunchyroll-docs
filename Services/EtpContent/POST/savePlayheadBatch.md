savePlayheadBatch
===========

#### Save multiple playheads.

```http
POST /content/v2/${account_uuid}/playheads/batch

# Request Headers
Content-Type: application/json
Authorization: Bearer ${TOKEN}

# Request Body
{
  "batch": {
    "${content_id_1}": {
      "playhead": ${playhead_1},
      "date_watched": ${ISO_DATE_FORMAT_1}
    },
    "${content_id_2}": {
      "playhead": ${playhead_2},
      "date_watched": ${ISO_DATE_FORMAT_2}
    }
  }
}
```