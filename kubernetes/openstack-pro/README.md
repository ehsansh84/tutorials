# How to activate openstack storage provisioner on kubernetes?
### Step 1 - Create `/etc/kubernetes/cloud.conf` in all nodes:
```
[Global]
auth-url=https://cloud.xxx.com:50000
username=USERNAME
password=PASSWORD
region=RegionOne
tenant-name=TENANT_NAME
domain-id=default
# this is for using a self-signed cert if your using a CA then comment this line
# and point to the CA certificate using the "ca-file" arg
tls-Insecure=true 

[BlockStorage]
bs-version=v2

[Networking]
public-network-name=NETWORK_NAME
ipv6-support-disabled=false
```
You may need to resolve `https://cloud.xxx.com` in all your nodes, so it is better to configure core dns to handle it. 
Edit `ConfigMaps/coredns` in `kube-system` namespace and add this config to the end:
```
hosts custom.hosts cloud.xxxx.com {
      xxx.xxx.xxx.xxx cloud.xxx.com
      fallthrough
}
```
### Step 2 - Install cinder-csi-plugin:
Configure values file as you wish. Actually I did nothing but changing docker images to my local repo and removing ca parts because I didn't have a ca-file.
```commandline
helm repo add cpo https://kubernetes.github.io/cloud-provider-openstack
helm repo update
helm install cinder-csi cpo/openstack-cinder-csi
```
It will create two storageClasses: `csi-cinder-sc-delete` and `csi-cinder-sc-retain`  
Happy provisioning!
### References:
- [Deploying External OpenStack Cloud Provider with Kubeadm](https://kubernetes.io/blog/2020/02/07/deploying-external-openstack-cloud-provider-with-kubeadm/)
- [Github cloud-provider-openstack](https://github.com/kubernetes/cloud-provider-openstack)
- [How to change host name resolve like host file in coredns](https://stackoverflow.com/questions/65283827/how-to-change-host-name-resolve-like-host-file-in-coredns)
- []()
