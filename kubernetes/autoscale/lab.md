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

### Step 3: Set autoscale
```commandline
kubectl autoscale deployment php-apache --cpu-percent=50 --min=1 --max=15 -n autoscale-test
```
