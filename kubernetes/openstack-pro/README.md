# How to activate openstack storage provisioner on kubernetes?
### Step 1 - Create `kubeadm-config.yml`:
```yaml
apiVersion: kubeadm.k8s.io/v1beta1
kind: InitConfiguration
nodeRegistration:
  kubeletExtraArgs:
    cloud-provider: "external"
---
apiVersion: kubeadm.k8s.io/v1beta2
kind: ClusterConfiguration
kubernetesVersion: "v1.23.3"
apiServer:
  extraArgs:
    enable-admission-plugins: NodeRestriction
    runtime-config: "storage.k8s.io/v1=true"
controllerManager:
  extraArgs:
    external-cloud-volume-plugin: openstack
  extraVolumes:
  - name: "cloud-config"
    hostPath: "/etc/kubernetes/cloud-config"
    mountPath: "/etc/kubernetes/cloud-config"
    readOnly: true
    pathType: File
networking:
  serviceSubnet: "10.96.0.0/12"
  podSubnet: "10.224.0.0/16"
  dnsDomain: "cluster.local"
```
Of course there may be other values you may want to set like image repository and so on.
### Step 2 - Create `/etc/kubernetes/cloud-config`:
You may need some information about openstack that you can acquire from openstack UI (OpenStack RC file).  
You can get rid of load balancer section if there isn't any.
```
[Global]
region=RegionOne
username=username
password=password
auth-url=https://openstack.cloud:5000/v3
tenant-id=14ba698c0aec4fd6b7dc8c310f664009
domain-id=default
ca-file=/etc/kubernetes/ca.pem

[LoadBalancer]
subnet-id=b4a9a292-ea48-4125-9fb2-8be2628cb7a1
floating-network-id=bc8a590a-5d65-4525-98f3-f7ef29c727d5

[BlockStorage]
bs-version=v2

[Networking]
public-network-name=public
ipv6-support-disabled=false
```
### Step 3 - Initiate control-plane:
```commandline
kubeadm init --config=kubeadm-config.yml
```
At this stage, the control-plane node is created but not ready.(Of course for my experience it was Ready!) 
All the nodes have the taint `node.cloudprovider.kubernetes.io/uninitialized=true:NoSchedule` and are waiting to be 
initialized by the cloud-controller-manager.  
You can check it:
```commandline
$ kubectl describe no master1
Name:               master1
Roles:              master
......
Taints:             node-role.kubernetes.io/master:NoSchedule
                    node.cloudprovider.kubernetes.io/uninitialized=true:NoSchedule
                    node.kubernetes.io/not-ready:NoSchedule
......
```





### Step 4 - Create a secret with the cloud-config for the openstack cloud provider:
```commandline
kubectl create secret -n kube-system generic cloud-config --from-literal=cloud.conf="$(cat /etc/kubernetes/cloud-config)" --dry-run -o yaml > cloud-config-secret.yaml
kubectl apply -f cloud-config-secret.yaml 
```
### Step 5 - Get the CA certificate for OpenStack API endpoints and put that into `/etc/kubernetes/ca.pem`

### Step 6: Create RBAC resources:
```commandline
kubectl apply -f https://github.com/kubernetes/cloud-provider-openstack/raw/release-1.15/cluster/addons/rbac/cloud-controller-manager-roles.yaml
kubectl apply -f https://github.com/kubernetes/cloud-provider-openstack/raw/release-1.15/cluster/addons/rbac/cloud-controller-manager-role-bindings.yaml
```

### Step 7:
We'll run the OpenStack cloud controller manager as a DaemonSet rather than a pod. The manager will only run on the
control-plane node, so if there are multiple control-plane nodes, multiple pods will be run for high availability.
Create `openstack-cloud-controller-manager-ds.yaml` containing the following manifests, then apply it.

### Step 8:
```yaml
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: cloud-controller-manager
  namespace: kube-system
---
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: openstack-cloud-controller-manager
  namespace: kube-system
  labels:
    k8s-app: openstack-cloud-controller-manager
spec:
  selector:
    matchLabels:
      k8s-app: openstack-cloud-controller-manager
  updateStrategy:
    type: RollingUpdate
  template:
    metadata:
      labels:
        k8s-app: openstack-cloud-controller-manager
    spec:
      nodeSelector:
        node-role.kubernetes.io/master: ""
      securityContext:
        runAsUser: 1001
      tolerations:
      - key: node.cloudprovider.kubernetes.io/uninitialized
        value: "true"
        effect: NoSchedule
      - key: node-role.kubernetes.io/master
        effect: NoSchedule
      - effect: NoSchedule
        key: node.kubernetes.io/not-ready
      serviceAccountName: cloud-controller-manager
      containers:
        - name: openstack-cloud-controller-manager
          image: docker.io/k8scloudprovider/openstack-cloud-controller-manager:v1.15.0
          args:
            - /bin/openstack-cloud-controller-manager
            - --v=1
            - --cloud-config=$(CLOUD_CONFIG)
            - --cloud-provider=openstack
            - --use-service-account-credentials=true
            - --address=127.0.0.1
          volumeMounts:
            - mountPath: /etc/kubernetes/pki
              name: k8s-certs
              readOnly: true
            - mountPath: /etc/ssl/certs
              name: ca-certs
              readOnly: true
            - mountPath: /etc/config
              name: cloud-config-volume
              readOnly: true
            - mountPath: /usr/libexec/kubernetes/kubelet-plugins/volume/exec
              name: flexvolume-dir
            - mountPath: /etc/kubernetes
              name: ca-cert
              readOnly: true
          resources:
            requests:
              cpu: 200m
          env:
            - name: CLOUD_CONFIG
              value: /etc/config/cloud.conf
      hostNetwork: true
      volumes:
      - hostPath:
          path: /usr/libexec/kubernetes/kubelet-plugins/volume/exec
          type: DirectoryOrCreate
        name: flexvolume-dir
      - hostPath:
          path: /etc/kubernetes/pki
          type: DirectoryOrCreate
        name: k8s-certs
      - hostPath:
          path: /etc/ssl/certs
          type: DirectoryOrCreate
        name: ca-certs
      - name: cloud-config-volume
        secret:
          secretName: cloud-config
      - name: ca-cert
        secret:
          secretName: openstack-ca-cert
```
When the controller manager is running, it will query OpenStack to get information about the nodes and remove the taint.
In the node info you'll see the VM's UUID in OpenStack.
```commandline
$ kubectl describe no master1
Name:               master1
Roles:              master
......
Taints:             node-role.kubernetes.io/master:NoSchedule
                    node.kubernetes.io/not-ready:NoSchedule
......
sage:docker: network plugin is not ready: cni config uninitialized
......
PodCIDR:                     10.224.0.0/24
ProviderID:                  openstack:///548e3c46-2477-4ce2-968b-3de1314560a5
```
### Step 8: Install your favourite CNI and the control-plane node will become ready.
For me it is weave. I already configured in `net.yaml`. so:
```commandline
kubectl apply -f net.yaml
```

### Step 9: Now setup workers:
Get a token from master
```commandline
kubeadm token create --print-join-command
```

### Step 10: Create `kubeadm-config.yml` for worker nodes with the above token and ca cert hash.
```yaml
apiVersion: kubeadm.k8s.io/v1beta2
discovery:
  bootstrapToken:
    apiServerEndpoint: 192.168.1.7:6443
    token: 0c0z4p.dnafh6vnmouus569
    caCertHashes: ["sha256:fcb3e956a6880c05fc9d09714424b827f57a6fdc8afc44497180905946527adf"]
kind: JoinConfiguration
nodeRegistration:
  kubeletExtraArgs:
    cloud-provider: "external"
```
apiServerEndpoint is the control-plane node, token and caCertHashes can be taken from the join command printed in the
output of 'kubeadm token create' command.
Run this command on workers to join:
```commandline
kubeadm join  --config kubeadm-config.yml 
```


### References:
- [Deploying External OpenStack Cloud Provider with Kubeadm](https://kubernetes.io/blog/2020/02/07/deploying-external-openstack-cloud-provider-with-kubeadm/)
- []()
- []()
