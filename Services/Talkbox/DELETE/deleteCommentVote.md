deleteCommentVote
===========

#### Delete a comment vote.

```http
DELETE /talkbox/guestbooks/${guestbook_key}/comments/${comment_id}/votes

# Request Headers
Authorization: Bearer ${TOKEN}
```

| Parameter | Type | Description |
| --- | --- | --- |
| vote_type | `like,spoiler,inappropriate` | What page to start searching from. |
