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
1. Login into Harbor as administrator
2. Set `Administration\Configuration\Authentication\Auth Mode` to `OIDC`
  if the option is disabled, You have to delete all accounts except admin.
3. Set these values:
    - OIDC Provider Name: `keycloak.domain.com`
    - OIDC Endpoint: KEYCLOAK_URL/auth/realms/master (or other realm)
    - OIDC Client ID: `harbor`
    - OIDC Client Secret: Acquire from Step 1 number 5
    - Group Claim Name: If you want to assign a group to you can use this
    - OIDC Scope: `openid`
    - If you want to automatically get username from token:
      - Set `Automatic onboarding` to `Checked`
      - Set `Username Claim` to `preferred_username`

### Step3: Create a project and assign a group in Harbor
- Create a project if needed
- Open project and go to `Members`
- Create a `Group`

### Step4: 
- Go to `Clients\your_client\Roles`
- `Add Role` for your group
- Go to `Clients\your_client\Mappers\Create`
- Set `Mapper Type` to `User Clients Role`
- Set `Token Claim Name` to name you specified in Step 2.3 Group Claim Name
- Set 'Client ID' to `harbor` as you specified in Step2.3 OIDC Client ID
- Go to `Users/Role Mappings`
- Set `Clients Roles` to your_client
- Assign roles from Available roles 
#### Refrences:
- [Harbor Keycloak Auth](https://blog.lazybit.ch/harbor-keycloak-auth/)
