<!-- Space: RD -->
<!-- Title: How to install and configure Harbor on an existing Postgres? -->
# Run Harbor on an existing postgresql

Original helm repository: https://github.com/goharbor/harbor-helm
To run harbor you must create 3 databases:
- registry
- notary_server
- notary_signer
The command for creating in Postgres is:
```
CREATE DATABASE registry;
CREATE DATABASE notary_server;
CREATE DATABASE notary_signer;
```
### Setting external database configurations:
```yaml
database: # Making database external
  type: external
external:
   host: "postgres-postgresql"
   port: "5432"
   username: "postgres"
   password: "^Avnsdhj6534"
   coreDatabase: "registry"
   notaryServerDatabase: "notary_server"
   notarySignerDatabase: "notary_signer"
```
### Finally run:
```
kubectl create namespace harbor
helm repo add harbor https://helm.goharbor.io
helm install -n harbor harbor harbor/harbor -f harbor.yaml
```

