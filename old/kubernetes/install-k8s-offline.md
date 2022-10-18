<!-- Space: RD -->
<!-- Title: How to install kubernetes from binary? -->
# How to install kubernetes from binary?
### Step1: Download binary package
There is a binary package containing all necessary files. Download and uncompress

### Step2: Install docker:
```commandline
mkdir /etc/docker
groupadd docker
mv containerd.service /lib/systemd/system
mv daemon.json /etc/docker
mv docker/* /usr/bin
mv docker.* /lib/systemd/system
systemctl daemon-reload
systemctl enable docker.service
systemctl enable containerd.service
systemctl daemon-reload
```
### Step2: Install kubernetes binaries:
```commandline
mv kubelet.service /lib/systemd/system
chmod +x kube*
mv kube* /usr/bin
ln -s /etc/systemd/system/multi-user.target.wants/kubelet.service /lib/systemd/system/kubelet.service
mkdir /etc/systemd/system/kubelet.service.d/
mv 10-kubeadm.conf /etc/systemd/system/kubelet.service.d/
systemctl enable kubelet.service
```
### Step3: init
```commandline
apt install -y conntrack
kibeadm init --config-config.yaml
```



#### Refrences:
- []()