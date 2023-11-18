setProfile
===========

#### Change profile settings.

```http
PATCH /accounts/v1/me/multiprofile/{profile_uuid}

# Request Headers
Content-Type: application/json
Authorization: Bearer ${TOKEN}

# Request Body
## Set Subtitle Language
{
    "preferred_content_subtitle_language": "${preferred_content_subtitle_language}"
}

## Set Audio Language
{
    "preferred_content_audio_language": "${preferred_content_audio_language}"
}

## Set Display Language
{
    "preferred_communication_language": "${preferred_communication_language}"
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
