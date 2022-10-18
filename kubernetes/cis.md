<!-- Space: RD -->
<!-- Title: What is CIS and Kube-Bench?-->
# What is CIS?
- CIS security is a community driven and non-profit organization that aims at improving security around the internet. It is the one that creates and updates CIS controls and CIS benchmarks.  
- The Center for Internet Security, Inc. (CIS®) makes the connected world a safer place for people, businesses, and governments through our core competencies of collaboration and innovation.  
- The CIS Mission is to make the connected world a safer place by developing, validating, and promoting timely best practice solutions that help people, businesses, and governments protect themselves against pervasive cyber threats.  
### What Are CIS Benchmarks?
CIS benchmarks are best practices around your IT system. Kubernetes CIS benchmarks are industry-accepted system hardening procedures. CIS Kubernetes benchmarks are reviewed by Kubernetes community as well as security experts.
### How You Can Benchmark Your Cluster Against CIS Benchmarks?
There are two ways in which you can benchmark your cluster against CIS benchmarks
- Kube-bench CLI
- Kubernetes Jobs & CronJobs
### Installing Kube-Bench
Install using:
```commandline
curl -LO https://github.com/aquasecurity/kube-bench/releases/download/v0.6.8/kube-bench_0.6.8_linux_amd64.tar.gz
```
After this, you have to create one directory where the default config files of kube-bench will reside.
```commandline
sudo mkdir -p /etc/kube-bench
```
Now after this you need to untar the kube-bench files in this above directory.
```commandline
sudo tar -xvf kube-bench_0.6.8_linux_amd64.tar.gz -C /etc/kube-bench
```
Last thing that you need to do is to move the kube-bench binary to `/usr/local/bin`
```commandline
sudo mv /etc/kube-bench/kube-bench /usr/local/bin
```
You have successfully installed and configured kube-bench, and we are ready to move ahead. To verify the installation, use the command `kube-bench version`

#### Refrences:
- [Kube-Bench](https://earthly.dev/blog/kube-bench/)
- [About CIS](https://www.cisecurity.org/about-us)
- []()
- []()
- []()


