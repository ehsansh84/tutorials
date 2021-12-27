<!-- Space: RD -->
<!-- Title: How to create an ArgoCD pipeline? -->
# Title: How to create an ArgoCD pipeline?
### Step 1: Create a project
- Goto `Settings/Projects/New Project`
- Name the project and open the project
- Edit `SOURCE REPOSITORIES` and put your repository url here
- Edit `DESTINATIONS` and: Server: * Name: * Namespace: your_namespace
- Edit `CLUSTER RESOURCE ALLOW LIST` and: Kind: * Group: *

### Step 2: Create a repository
- Goto `Settings/Repositories/Connect Repo using HTTPS`
- Set: `Type` to git or helm
- Set: `Project` to your project name
- Set: `Repository URL` to your reporsitory url
- Set: Username and Password for your git repo

### Step 3: Create an application
- Click on 3 dots on your repository you've built on second step and select `Create application`
- Set `Application Name` to your desired name
- Choose your project
- Set `Sync Policy` to automatic
- Check `Auto Create Namespace`
- Choose `Repository URL`
- Choose `Path`
- Choose `Cluster URL`
- Set `Namespace`
- Choose `Values Files` and change any values if needed
- Click Create and It's Done
