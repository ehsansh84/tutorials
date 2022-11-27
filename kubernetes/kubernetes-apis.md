# How to call kubernetes APIs
### Get token like this:
```commandline
export TOKENNAME=$(kubectl -n kube-system get serviceaccount/default -o jsonpath='{.secrets[0].name}')
export TOKEN=$(kubectl -n kube-system get secret $TOKENNAME -o jsonpath='{.data.token}' | base64 --decode)
```
### References:
- [A Beginner’s Guide to Kubernetes Python Client](https://www.velotio.com/engineering-blog/kubernetes-python-client)
- [How To Call Kubernetes API using Simple HTTP Client](https://iximiuz.com/en/posts/kubernetes-api-call-simple-http-client/)
- [Obtaining the Service Account Token](https://kb.selectel.com/docs/cloud/managed-kubernetes/instructions/service-account-token/)