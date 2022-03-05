<!-- Space: RD -->
<!-- Title: How to create robot accounts using harbor APIs? -->
# How to create robot accounts using harbor APIs?
First you should know about list of `resources` and `actions` related.
### List of resources:
- "*"
- "configuration"
- "helm-chart"
- "helm-chart-version"
- "helm-chart-version-label"
- "label"
- "log"
- "ldap-user"
- "member"
- "metadata"
- "quota"
- "repository"
- "tag-retention"
- "immutable-tag"
- "robot"
- "notification-policy"
- "scan"
- "scanner"
- "artifact"
- "tag"
- "artifact-addition"
- "artifact-label"
- "preheat-policy"
- "preheat-instance"
- ""
- "audit-log"
- "catalog"
- "project"
- "user"
- "user-group"
- "registry"
- "replication"
- "distribution"
- "garbage-collection"
- "replication-adapter"
- "replication-policy"
- "scan-all"
- "system-volumes"

### List of actions:
- "*"
- "pull" => pull repository tag
- "push" => push repository tag
- "create"
- "read"
- "update"
- "delete"
- "list"
- "operate"
- "scanner-pull" => for robot account created by scanner to pull image, bypass the policy check
- "stop" => for stop scan/scan-all execution

#### Refrences:
- [Harbor source: const.go](https://github.com/goharbor/harbor/blob/5cd5bcaee44e9f57c96ac8327009bcffb95ac7a5/src/common/rbac/const.go)

