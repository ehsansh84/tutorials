<!-- Space: RD -->
<!-- Title: How to connect Harbor to Keycloak -->
# How to connect Harbor to Keycloak

HARBOR_URL: harbor.domain.com  
KEYCLOAK_URL: kc.domain.com

### Step1: Keycloak settings:
1. Login to keycloak
2. Create a realm if needed
3.  Create a client if needed
4. Goto `Clients\your-client-settings`
  - Set `Access type` to `confidential`
  - Set `Valid Redirect URIs` to `HARBOR_URL`
5. After saving changes you can go to `Credentials` tab next to the Settings tab and copy `Secret` for Harbor settings

### Step2: Change auth in Harbor
- Login into Harbor as administrator
- Set `Administration\Configuration\Authentication\Auth Mode` to `OIDC`
  if the option is disabled, You have to delete all accounts except admin.
- Set these values:
  - OIDC Provider Name: `keycloak.domain.com`
  - OIDC Endpoint: KEYCLOAK_URL/auth/realms/master (or other realm)
  - OIDC Client ID: `harbor`
  - OIDC Client Secret: Acquire from Step 1 number 5
  - Group Claim Name: If you want to assign a group to you can use this
  - OIDC Scope: `openid`
  - If you want to automatically get username from token:
    - Set `Automatic onboarding` to `Checked`
    - Set `Username Claim` to `preferred_username`





#### Refrences:
- [Harbor Keycloak Auth](https://blog.lazybit.ch/harbor-keycloak-auth/)
