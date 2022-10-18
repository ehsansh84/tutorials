<!-- Space: RD -->
<!-- Title: How to install and configure Posgresql with 3 read replicas? -->
# Run Posgres database using 3 read replicas
Original helm repository: https://github.com/bitnami/charts/tree/master/bitnami/postgresql

In case you want to run a few sql commands on db init, you can create this config map:
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: postrges-initdb-config
  namespace: postgres
data:
  initdb.sql: |
    CREATE DATABASE database1;
    CREATE DATABASE database2;
```
Contents of `values.yaml`:
```yaml
replication: # In this case our database should have 3 read replicas
  enabled: true
  readReplicas: 3
primary:
  tolerations:
    - key: database
      operator: Exists
persistence: 
  storageClass: "openebs-lvmpv"

readReplicas:
  tolerations:
    - key: database
      operator: Exists

initdbScriptsConfigMap: postrges-initdb-config # Only if you've created above config map
```
### Finally run:
```
kubectl create namespace postgres
helm repo add bitnami https://charts.bitnami.com/bitnami
helm install -n postgres postgres bitnami/postgresql -f postgres.yaml
```

