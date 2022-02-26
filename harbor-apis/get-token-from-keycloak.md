<!-- Space: RD -->
<!-- Title: How to get token from Keycloak -->
# How to get token from Keycloak
Create a `ClusterIssuer` for staging:
```
curl --location --request POST 'https://accounts.greenrnd.com/auth/realms/master/protocol/openid-connect/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_id=admin-cli' \
--data-urlencode 'username=admin' \
--data-urlencode 'password=hashem@123' \
--data-urlencode 'grant_type=password'
```

#### Refrences:
- [KeycloakRestAPI](https://documenter.getpostman.com/view/7294517/SzmfZHnd)

