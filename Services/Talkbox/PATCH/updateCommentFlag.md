updateCommentFlag
===========

#### Update a comment's flags.

```http
PATCH /talkbox/guestbooks/${guestbook_key}/comments/${comment_id}/flags

# Request Headers
Authorization: Bearer ${TOKEN}

# Request Body
{
    "add": [
        ${like,spoiler,inappropriate,deleted}
    ],
    "remove": [
        ${like,spoiler,inappropriate,deleted}
    ]
}
```