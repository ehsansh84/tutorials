<!-- Space: RD -->
<!-- Title: Kubernetes Role Based Access Control (RBAC) -->
# Kubernetes Role Based Access Control (RBAC)
#### Dictionary:
- What is a role?  A group of api groups, resources and verbs that defines what to do with what resources?
  - api groups: Networking, Apps, ...
  - Resources: Pods, Deployments, ReplicaSets, ...
  - Verbs: get, list, watch, update, ...
- Role: Applies only to a namespace
- ClusterRole: Applies to whole cluster


## Step-by-step guide:
### Step 1: Create a kubeconfig for the user

I want to create a user called Ehsan. First create a private key:
```
openssl genrsa -out ehsan.key 2048
```
Then We want to create a certificate sign ing request:
```
openssl req -new -key ehsan.key -out ehsan.csr -subj "/CN=ehsan/O=MyProject"
```
Now we need to have kubernetes certification authority files. default path: `/etc/kubernetes/pki` and files are `ca.crt, ca.key`  
Finally certificated will be created:
```
openssl x509 -req -in ehsan.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out ehsan.crt -days 365
```
### Step 2: Create a kubeconfig for the user
```
kubectl --kubeconfig ehsan.kubeconfig config set-cluster kubernetes --server https://SERVER_IP:6443 --certificate-authority=ca.crt
kubectl --kubeconfig ehsan.kubeconfig config set-credentials ehsan --client-certificate ehsan.crt --client-key ehsan.key
kubectl --kubeconfig ehsan.kubeconfig config set-context ehsan-kubernetes --cluster kubernetes --namespace cman --user ehsan
```
You can use `--embed certs=true` to embed certs in kubeconfig like this:
```
kubectl --kubeconfig ehsan.kubeconfig config set-cluster kubernetes --server https://SERVER_IP:6443 --certificate-authority=ca.crt --embed certs=true
kubectl --kubeconfig ehsan.kubeconfig config set-credentials ehsan --client-certificate ehsan.crt --client-key ehsan.key --embed certs=true
```

In ehsan.kubeconfig set `current-context` values to `ehsan-kubernetes`
If try a send a request using this kubeconfig an error will be raise like this:
`Error from server (Forbidden): pods is forbidden: User "ehsan" cannot list resource "pods" in API group "" in the namespace "cman"`
### Step 3: 
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: myns
  name: ehsan-role
rules:
- apiGroups: [""] # "" indicates the core API group
  resources: ["pods"]
  verbs: ["get", "watch", "list"]
- apiGroups: [""] # "" indicates the core API group
  resources: ["pods/exec"]
  verbs: ["create"]
```
### Step 4:
```
kind: RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: ehsan-rolebinding
  namespace: myns
subjects:
- kind: User
  name: ehsan
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: ehsan-role
  apiGroup: rbac.authorization.k8s.io 
```

To put it together simply run this bash:
```shell
NAMESPACE=namespace
USER=user
SERVER_IP=server_ip
openssl genrsa -out $USER.key 2048
openssl req -new -key $USER.key -out $USER.csr -subj "/CN=$USER/O=$NAMESPACE"
scp ubuntu@$SERVER_IP:/etc/kubernetes/pki/ca.{crt,key} .
openssl x509 -req -in $USER.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out $USER.crt -days 365
kubectl --kubeconfig $USER.kubeconfig config set-cluster kubernetes --server https://$SERVER_IP:6443 --certificate-authority=ca.crt
kubectl --kubeconfig $USER.kubeconfig config set-credentials $USER --client-certificate $USER.crt --client-key $USER.key
kubectl --kubeconfig $USER.kubeconfig config set-context $USER-kubernetes --cluster kubernetes --namespace $NAMESPACE --user $USER
```



#### Refrences:
- [Configuring permissions in Kubernetes with RBAC](https://medium.com/containerum/configuring-permissions-in-kubernetes-with-rbac-a456a9717d5d)
