signInWithFun
===========

#### Sign in with funimation.

```http
POST /auth/v1/login/funimation

# Request Headers
Authorization: Basic ${KEY}
ETP-Anonymous-ID: ${ETP_ID}

# Request Body

## Keep in mind these are all of the available parameters, you don't have to use them all.

grant_type=${password,phone,refresh_token}&device_id=${device_id}&device_name=${device_name}&device_type=${device_type}&scope=${offline_access}&username=${username}&password=${password}&client_id=pak8lt8altqda-3gfabp&client_secret=y5SIwpxhjUy3EpYsfuaj13LbHbc7bFgQ
```