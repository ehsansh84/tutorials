# Kubernetes auto scaler
### What is Cluster Autoscaler?
Cluster Autoscaler is a standalone program that adjusts the size of a Kubernetes cluster to meet the current needs.
### When does Cluster Autoscaler change the size of a cluster?

Cluster Autoscaler increases the size of the cluster when:
- there are pods that failed to schedule on any of the current nodes due to insufficient resources.
- adding a node similar to the nodes currently present in the cluster would help.

> Cluster Autoscaler decreases the size of the cluster when some nodes are consistently unneeded for a significant amount of time. A node is unneeded when it has low utilization and all of its important pods can be moved elsewhere.

### What are the key best practices for running Cluster Autoscaler?
- Do not modify the nodes belonging to autoscaled node groups directly. All nodes within the same node group should have the same capacity, labels and system pods running on them.
- Specify requests for your pods.
- Use PodDisruptionBudgets to prevent pods from being deleted too abruptly (if needed).
- Check if your cloud provider's quota is big enough before specifying min/max settings for your node pools.
- Do not run any additional node group autoscalers (especially those from your cloud provider).


### Install `metrics-server` like this:
Check if metrics-server installed:
```commandline
kubectl get po -n kube-system | grep metric
```
Install if necessary:
```commandline
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```
> The Cluster Autoscaler doesn't look at memory or CPU available when it triggers the autoscaling.  
Instead, the Cluster Autoscaler reacts to events and checks for any unschedulable Pods every 10 seconds.
### How Auto scaler selects node type?
If you have a cluster with several node types (often also referred to as node groups or node pools), the Cluster Autoscaler will pick one of them using the following strategies:

- Random — picks a node type at random. This is the default strategy.
- Most pods — selects the node group that would schedule the most pods.
- Least waste — selects the node group with the least idle CPU after scale-up.
- Price — select the node group that will cost the least (only works for GCP at the moment).
- Priority — selects the node group with the highest priority (and you manually assign priorities).
### Time to create a new pod on a new node depends on:
- Horizontal Pod Autoscaler reaction time.
- Cluster Autoscaler reaction time.
- Node provisioning time.
- Pod creation time.
> By default, pods' CPU and memory usage is scraped by kubelet every 10 seconds.
### Once one or more Pods are detected, it will run an algorithm to decide:
- How many nodes are necessary to deploy all pending Pods.
- What type of node group should be created.

### Total timing for trigger the autoscaling when there is no space in the current cluster is:
- The Horizontal Pod Autoscaler might take up to 1m30s to increase the number of replicas.
- The Cluster Autoscaler should take less than 30 seconds for a cluster with less than 100 nodes and less than a minute for a cluster with more than 100 nodes.
- The cloud provider might take 3 to 5 minutes to create the computer resource.
- The container runtime could take up to 30 seconds to download the container image.
At worse, it takes about 7 minutes.

> You can cache docker images using a cache tools like [kube-fledged](https://github.com/senthilrch/kube-fledged) to reduce download time. 
### References: 
- [Frequently Asked Questions](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#what-is-cluster-autoscaler)
- [Horizontal Pod Autoscaling](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)
- [How to Test Autoscaling in Kubernetes](https://speedscale.com/how-to-test-kubernetes-autoscaling/)
- [Kubernetes Metrics Server](https://kubernetes-sigs.github.io/metrics-server/)
- [How the Cluster Autoscaler works in Kubernetes](https://learnk8s.io/kubernetes-autoscaling-strategies#how-the-cluster-autoscaler-works-in-kubernetes)
- [kube-fledged](https://github.com/senthilrch/kube-fledged)
- []()
- []()
