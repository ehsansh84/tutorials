# How to activate openstack storage provisioner (Manila) on kubernetes?

### Step 1 - Create values file `openstack-ccm.yaml`:
```yaml
cloudConfig:
    global:
        auth-url: https://OPENSTACK_URL:5000/v3
        username: USERNAME
        password: PASSWORD
        tls-insecure: true
        domain-name: Default
        region: RegionOne
        tenant-id: fef63215927e433a83a0c431e373e65d
image:
        repository: docker.iranserver.com:15000/provider-os/openstack-cloud-controller-manager
        tag: "v1.27.1"
```
### Step 2 - Install cinder-csi-plugin:
Run this:
```commandline
helm repo add cpo https://kubernetes.github.io/cloud-provider-openstack
helm repo update
helm install openstack-ccm cpo/openstack-cloud-controller-manager --values openstack-ccm.yaml
```

### Step 3 -  Install Manila CSI chart
Create values file `manila-values.yaml`:
```yaml
csimanila:
  image:
    repository: docker.iranserver.com:15000/provider-os/manila-csi-plugin
    pullPolicy: IfNotPresent
    tag:  # defaults to .Chart.AppVersion

# DeamonSet deployment
nodeplugin:
  name: nodeplugin
  registrar:
    image:
      repository: docker.iranserver.com:15000/sig-storage/csi-node-driver-registrar
      tag: v2.4.0
      pullPolicy: IfNotPresent

controllerplugin:
  name: controllerplugin
  provisioner:
    image:
      repository: docker.iranserver.com:15000/sig-storage/csi-provisioner
      tag: v3.0.0
      pullPolicy: IfNotPresent
    resources: {}
  snapshotter:
    image:
      repository: docker.iranserver.com:15000/sig-storage/csi-snapshotter
      tag: v5.0.1
      pullPolicy: IfNotPresent
  resizer:
    image:
      repository: docker.iranserver.com:15000/sig-storage/csi-resizer
      tag: v1.3.0
      pullPolicy: IfNotPresent
    resources: {}
logVerbosityLevel: 2
```

```commandline
helm install manila-csi cpo/openstack-manila-csi -f manila-values.yaml
```
Or Install Cinder CSI chart:
```commandline
helm install cinder-csi cpo/openstack-cinder-csi
```


### References:
- [openstack-cloud-controller-manager github](https://github.com/kubernetes/cloud-provider-openstack/tree/master/charts/openstack-cloud-controller-manager)
- [Cloud Provider OpenStack Helm Chart Repository](https://kubernetes.github.io/cloud-provider-openstack/)
