createAccountWithPhone
===========

#### Create an account using a phone instead.

```http
POST /accounts/v2

# Request Headers
Content-Type: application/json
Authorization: Basic ${KEY}

# Request Body
{
  "phone_number": "${phone_number}",
  "verification_code": "${verification_code}",
  "preferred_content_audio_language": "${preferred_content_audio_language}",
  "preferred_content_subtitle_language": "${preferred_content_subtitle_language}",
  "preferred_communication_language": "${preferred_communication_language}"

}
```