postComment
===========

#### Post a comment.

```http
POST /talkbox/guestbooks/${guestbook_key}/comments

# Request Headers
Authorization: Bearer ${TOKEN}

# Request Body
{
    flags: [
        ${like,spoiler,inappropriate,deleted}
    ],
    locale: ${locale},
    message: ${message},
    parent_id: ${parent_id}
}
```
