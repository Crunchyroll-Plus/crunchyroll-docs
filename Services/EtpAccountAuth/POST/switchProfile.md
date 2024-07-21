switchProfile
===========

#### Switch profiles.

```http
POST /auth/v1/token

# Request Headers
Authorization: Basic eHVuaWh2ZWRidDNtYmlzdWhldnQ6MWtJUzVkeVR2akUwX3JxYUEzWWVBaDBiVVhVbXhXMTE=
ETP-Anonymous-ID: ${ETP_ID}

# Request Body

"grant_type=refresh_token_profile_id&refresh_token=${refresh_token}&profile_id=${profile_id}&scope=offline_access"
```
