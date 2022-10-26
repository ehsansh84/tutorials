# Kubernetes auto scaler
### What is Cluster Autoscaler?
Cluster Autoscaler is a standalone program that adjusts the size of a Kubernetes cluster to meet the current needs.
### When does Cluster Autoscaler change the size of a cluster?

Cluster Autoscaler increases the size of the cluster when:
- there are pods that failed to schedule on any of the current nodes due to insufficient resources.
- adding a node similar to the nodes currently present in the cluster would help.

### Cluster Autoscaler decreases the size of the cluster when some nodes are consistently unneeded for a significant amount of time. A node is unneeded when it has low utilization and all of its important pods can be moved elsewhere.

### What are the key best practices for running Cluster Autoscaler?
- Do not modify the nodes belonging to autoscaled node groups directly. All nodes within the same node group should have the same capacity, labels and system pods running on them.
- Specify requests for your pods.
- Use PodDisruptionBudgets to prevent pods from being deleted too abruptly (if needed).
- Check if your cloud provider's quota is big enough before specifying min/max settings for your node pools.
- Do not run any additional node group autoscalers (especially those from your cloud provider).

### Install `metrics-server` like this:
```commandline
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

### 
### References: 
- [Frequently Asked Questions](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#what-is-cluster-autoscaler)
- [Horizontal Pod Autoscaling](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)
- [How to Test Autoscaling in Kubernetes](https://speedscale.com/how-to-test-kubernetes-autoscaling/)
- [Kubernetes Metrics Server](https://kubernetes-sigs.github.io/metrics-server/)
- []()
- []()
- []()
- []()
