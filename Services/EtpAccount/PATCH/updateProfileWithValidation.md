updateProfileWithValidation
===========

#### Same as setProfile just for profiles with pins I'm assuming.

- See [validateProvidedCredentials](../POST/validateProvidedCredentials.md) for the CrPassToken header.


```http
PATCH accounts/v2/{account_uuid}/multiprofile/{profile_id}

# Request Headers
Content-Type: application/json
Authorization: Bearer ${TOKEN}
CrPassToken: ${PASS_TOKEN}

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
