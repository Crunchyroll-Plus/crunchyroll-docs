setPrimaryLanguages
===========

#### Change languages (this might be wrong this is just an assumption).

```http
PATCH /accounts/v1/me/profile

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
```
