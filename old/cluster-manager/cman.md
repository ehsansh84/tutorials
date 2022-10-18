<!-- Space: RD -->
<!-- Title: Installation of cluster manager project -->
# Installation of cluster manager project
### Step one: Git clone
```
git clone https://git.greenrnd.com/infrastructure/cluster-manager.git
```
There is a `helm` directory,just run:
```
create namespace cman # if not exists
helm install -n cman cman .
```
This is customized values, you can leave it as it is:
```yaml
metadata:
  namespace: cman
backend:
  name: cman
  image: harbor.greenrnd.com/k8s/cman
  tag: latest
  service:
    port: 8282
    type: ClusterIP
database:
  image: "mongo:latest"
  name: mongodb
  user: admin
  pass: Mongo@123
  port: 27017
  pvc:
    name: mongo-pvc
storage:
  storageclassname: rook-cephfs
  storagesize: 1Gi
image:
  tag: dev-dc902ff6
```
Our datacenters:
- Tabriz: almost out of capacity and a slow network
- Afranet: Will be used as the development platform and better network

We prefer to use Traefik as ingress controller and IngressRoute instead of Ingress  
