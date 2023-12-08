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
  "age_consent": "${true|false}"
}
```
