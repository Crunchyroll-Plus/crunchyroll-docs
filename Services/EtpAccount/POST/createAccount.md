createAccount
===========

#### Create an account.

```http
POST /accounts/v2

# Request Headers
Content-Type: application/json
Authorization: Bearer ${TOKEN}

# Request Body
{
  "email": "${email}",
  "password": "${password}",
  "preferred_content_audio_language": "${preferred_content_audio_language}",
  "preferred_content_subtitle_language": "${preferred_content_subtitle_language}",
  "preferred_communication_language": "${preferred_communication_language}"
}
```
