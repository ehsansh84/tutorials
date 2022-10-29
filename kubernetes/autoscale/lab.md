# Lab for Autoscale
### Step 1: Create namespace
```commandline
kubectl create namespace autoscale-test
```
### Step 2: Deploy php-apache
```commandline
kubectl create -f deploy.yml
```
Before 2nd step you must ensure that metrics server is installed and active in your cluster.
```commandline
kubectl get po -n kube-system | grep metric
```
Then you need to install a tool to produce stress on your pod:
```commandline
sh -c "$(curl -Lfs https://downloads.speedscale.com/speedctl/install)"
```