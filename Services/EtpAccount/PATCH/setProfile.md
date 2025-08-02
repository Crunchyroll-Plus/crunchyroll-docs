setProfile
===========

#### Change profile settings, I don't remember testing this so the request body may be somewhat wrong.

```http
PATCH /accounts/v1/me/multiprofile/{profile_uuid}

# Request Headers
Content-Type: application/json
Authorization: Bearer ${TOKEN}

# Request Body
{
  "username": "${username}",
  "profile_name": "${profile_name}",
  "email": "${email}",
  "avatar": "${avatar}",
  "wallpaper": "${wallpaper}",
  "age_consent": "${true|false}",
  "password": "${password}",
  "verification_code": "${verification_code}"
  "maturity_rating": "${maturity_rating}",
  "preferred_content_audio_language": "${preferred_content_audio_language}",
  "preferred_content_subtitle_language": "${preferred_content_subtitle_language}"
}
```
