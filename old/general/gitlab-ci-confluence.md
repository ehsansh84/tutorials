<!-- Space: RD -->
<!-- Title: How to send you markdown documents to confluence directly from Gitlab -->
# How to send you markdown documents to confluence directly from Gitlab
Consider your documentation must be in Markdown format.
Put these two line on top of your each files:
```
<!-- Space: Your spaceID which is RD for R & D department  -->
<!-- Title: Your desired title in confluence -->
```
Then you must provide 3 secrets in your gitlab project from: `Settings>CI/CD>Variables>Expand>Add variable`
```
CONFLUENCE_USER = your_confluence_username
CONFLUENCE_PASSWORD = your_confluence_password
CONFLUENCE_URL = https://doc.greenweb.ir
```
Add `.gitlab-ci.yml` to root of your project containing:
```yaml
stages:
  - sync
test:
  stage: sync
  image: shirzadi/md2conf
  script: |
      for file in $(git show $CI_COMMIT_SHA --name-status | grep "^[AM]\s.*md" | awk '{print $2}'); do
        echo "> Sync $file";
        mark -u $CONFLUENCE_USER -p $CONFLUENCE_PASSWORD -b $CONFLUENCE_URL -f $file || exit 1;
        echo;
      done
```
Finally enable runner for your project from `Settings>CI/CD>Runners>Expand>Enable runner for this project`  
That's It! Now commit and see your documents in confluence!
