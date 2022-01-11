<!-- Space: RD -->
<!-- Title: How to backup kubernetes cluster? -->

# How to backup kubernetes cluster?
### What is Velero?
Velero is a convenient backup tool for Kubernetes clusters that compresses and backs up Kubernetes objects to object storage. It also takes snapshots of your cluster’s Persistent Volumes using your cloud provider’s block storage snapshot features, and can then restore your cluster’s objects and Persistent Volumes to a previous state  
Velero has support for private as well as public cloud systems such as EKS , AKS , GKE
### What is Velero server?
A Velero installation consists of a number of Kubernetes objects that all work together to create, schedule, and manage backups.

### Install the Velero CLI:
Consider having minio installed:
1. Download the supported version of the signed Velero binary for vSphere with Tanzu from the VMware product downloads page.
2. gunzip velero-linux-vX.X.X_vmware.1.gz
3. chmod +x velero-linux-vX.X.X_vmware.1
4. cp velero-linux-vX.X.X_vmware.1 /usr/local/bin/velero
5. velero version

### Installing and configuring Velero:
1. Download the supported Velero installation package from the following VMware download site: https://github.com/vmware-tanzu/velero/releases
```
curl -fsSL -o velero-version-linux-amd64.tar.gz https://github.com/vmware-tanzu/velero/releases/download/version/velero-version-linux-amd64.tar.gz
```
2. Extract: `tar -xvf velero-version-linux-amd64.tar.gz`
3. Change to the directory where the extracted .tar file is located and run the following command:
```commandline
./velero install \
        --use-volume-snapshots=false \
        --no-default-backup-location \
        --no-secret \
        --plugins velero/velero-plugin-for-aws:v1.1.0 -n spp-velero
```
When the installation finishes, a message similar to the following message is displayed:
```text
No secret file was specified, no Secret created.
No bucket and provider were specified, no default backup storage location created.
Velero is installed! ⛵ Use 'kubectl logs deployment/velero -n spp-velero' to view the status.
```

### How to back up manually?
#### What Data should be in the Backup?
There are two data items to be backed up:
- The root certificate files /etc/kubernetes/pki/ca.crt and /etc/kubernetes/pki/ca.key.
- The etcd data.  
Backing up the root certificate is a one-time operation that you do manually after creating the master with kubeadm init. The rest of this post deals with how to back up the etcd data.
- Install etcdctl using: ` sudo apt-get install -y etcd-client`

#### Tips about an ETCD backup:
- Back up your cluster’s etcd data regularly and store in a secure location ideally outside the cluster
- Do not take an etcd backup before the first certificate rotation completes, which occurs 24 hours after installation, otherwise the backup will contain expired certificates.
- It is also recommended to take etcd backups during non-peak usage hours, as it is a blocking action
- Back up your cluster’s etcd data by performing a single invocation of the backup script on a control plane host (also known as the master host). Do not take a backup for each control plane host.

#### Refrences:
- [How To Back Up and Restore a Kubernetes Cluster on DigitalOcean Using Velero
?](https://www.digitalocean.com/community/tutorials/how-to-back-up-and-restore-a-kubernetes-cluster-on-digitalocean-using-velero)
- [Backup,Restore & Migrate Kubernetes cluster with Velero](https://medium.com/@maheshd7878/restore-backup-migrate-kubernetes-cluster-with-velero-434fa151f1e8)
- [6 Backup Features You Need for Kubernetes](https://www.trilio.io/resources/tvk-vs-velero/)
- [Install and Configure Standalone Velero and Restic on a Tanzu Kubernetes Cluster
](https://docs.vmware.com/en/VMware-vSphere/7.0/vmware-vsphere-with-tanzu/GUID-A24A6B91-0CDF-4D02-AD08-7BA5EAC25A42.html)
- [Installing and configuring Velero](https://www.ibm.com/docs/en/spp/10.1.7?topic=support-installing-configuring-velero)
- [Backup and Restore a Kubernetes Master with Kubeadm](https://labs.consol.de/kubernetes/2018/05/25/kubeadm-backup.html)
- [Backing up etcd](https://docs.openshift.com/container-platform/4.7/backup_and_restore/control_plane_backup_and_restore/backing-up-etcd.html)
- [Restoring to a previous cluster state](https://docs.openshift.com/container-platform/4.7/backup_and_restore/control_plane_backup_and_restore/disaster_recovery/scenario-2-restoring-cluster-state.html#dr-restoring-cluster-state)