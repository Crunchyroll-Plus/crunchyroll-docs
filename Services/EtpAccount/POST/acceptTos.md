acceptTos
===========

#### Accepts the TOS (this one doesn't really make sense it doesn't have a body so I'm assuming no content-type heaer is needed.)

```http
POST /accounts/v1/consent/${account_uuid}/tos

# Request Headers
Authorization: Bearer ${TOKEN}

```