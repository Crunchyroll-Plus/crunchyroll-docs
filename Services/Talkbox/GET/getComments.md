getComments
===========

#### Get comments from the guestbook_key.

```http
GET /talkbox/guestbooks/${guestbook_key}/comments

# Request Headers
Authorization: Bearer ${TOKEN}
```

| Parameter | Type | Description |
| --- | --- | --- |
| page | `int` | What page to start searching from. |
| page_size | `int` | The size of the page. |
| sort | `date,popular` | What to sort the comments by. |
| order | `desc, asc` | What to order the sort the comments by. |
