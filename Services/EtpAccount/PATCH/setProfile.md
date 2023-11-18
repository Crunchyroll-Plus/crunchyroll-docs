setProfile
===========

#### Change profile settings, I don't remember testing this so the request body may be somewhat wrong.

```http
PATCH /accounts/v1/me/multiprofile/{profile_uuid}

# Request Headers
Content-Type: application/json
Authorization: Bearer ${TOKEN}

# Request Body
## Set username
{
    "username": "${username}"
}

## Set Avatar
{
    "avatar": "${avatar}"
}

## Set extended maturity rating
{
    "extended_maturity_rating": "${extended_maturity_rating}"
}

## Set maturity rating
{
    "maturity_rating": "${maturity_rating}"
}
```
