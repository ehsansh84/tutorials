<!-- Space: RD -->
<!-- Title: How to install older versions of kubernetes? -->
# How to install older versions of kubernetes?

```bash
sudo apt-get update && sudo apt-get install -y apt-transport-https curl
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
cat <<EOF | sudo tee /etc/apt/sources.list.d/kubernetes.list
deb https://apt.kubernetes.io/ kubernetes-xenial main
EOF
apt update
```
There is the most important thing I got a problem :). Get available package versions
```bash
apt list -a kubeadm
```
From the output select which you want to install
```bash
# apt list -a kubeadm
Listing... Done
kubeadm/kubernetes-xenial 1.20.0-00 amd64 [upgradable from: 1.18.13-00]
kubeadm/kubernetes-xenial 1.19.5-00 amd64
kubeadm/kubernetes-xenial 1.19.4-00 amd64
kubeadm/kubernetes-xenial 1.19.3-00 amd64
kubeadm/kubernetes-xenial 1.19.2-00 amd64
kubeadm/kubernetes-xenial 1.19.1-00 amd64
kubeadm/kubernetes-xenial 1.19.0-00 amd64
kubeadm/kubernetes-xenial,now 1.18.13-00 amd64 [installed,upgradable to: 1.20.0-00]
kubeadm/kubernetes-xenial 1.18.12-00 amd64
kubeadm/kubernetes-xenial 1.18.10-00 amd64
```
And now simply specify this version for packages
```bash
apt install -y kubeadm=1.18.13-00 kubelet=1.18.13-00 kubectl=1.18.13-00
```
#### Refrences:
- [How to install specific version of Kubernetes?](https://stackoverflow.com/questions/49721708/how-to-install-specific-version-of-kubernetes)
