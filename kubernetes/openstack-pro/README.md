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

### References:
- [Deploying External OpenStack Cloud Provider with Kubeadm](https://kubernetes.io/blog/2020/02/07/deploying-external-openstack-cloud-provider-with-kubeadm/)
- []()
- []()
