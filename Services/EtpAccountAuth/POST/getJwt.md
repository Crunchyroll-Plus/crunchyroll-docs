getJwt
===========

#### Get a user JWT.

```http
POST /auth/v1/token

# Request Headers
Authorization: Basic ${KEY}
ETP-Anonymous-ID: ${ETP_ID}

# Request Body

## Keep in mind these are all of the available parameters, you don't have to use them all.

"grant_type=${password,phone,refresh_token,etp_rt_cookie}&device_id=${device_id}&device_name=${device_name}&device_type=${device_type}&refresh_token=${refresh_token}&scope=${offline_access,refresh_token}& username=${username}&password=${password}&phone_number=${phone_number}&verification_code=${verification_code}"
```
