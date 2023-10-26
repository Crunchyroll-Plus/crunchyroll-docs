voteComment
===========

#### Vote on a comment.

```http
POST /talkbox/guestbooks/${guestbook_key}/votes

# Request Headers
Authorization: Bearer ${TOKEN}

# Request Body
{
    "vote_type": "${like,spoiler,inappropriate}"
}
```
