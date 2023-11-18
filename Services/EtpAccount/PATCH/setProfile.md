setProfile
===========

#### Change profile settings.

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
