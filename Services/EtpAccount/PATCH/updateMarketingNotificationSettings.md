setProfile
===========

#### Change profile settings.

```http
PATCH /accounts/v1/${account_uuid}/notification_setting

# Request Headers
Content-Type: application/json
Authorization: Bearer ${TOKEN}

# Request Body
## Set Subtitle Language
{
    "opt_out_newsletters": false|true,
    "opt_out_promotional_updates": false|true,
    "opt_out_store_deals": false|true
}
```
