switchProfile
===========

#### Switch profiles.

```http
POST /auth/v1/token

# Request Headers
Authorization: Basic bm9haWhkZXZtXzZpeWcwYThsMHE6
ETP-Anonymous-ID: ${ETP_ID}

# Request Body

"grant_type=refresh_token_profile_id&refresh_token=${refresh_token}&scope=offline_access"
```
