createProfile
===========

#### Create a new profile.

```http
POST /accounts/v1/me/multiprofile

# Request Headers
Authorization: Bearer ${TOKEN}
Content-Type: application/json

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
