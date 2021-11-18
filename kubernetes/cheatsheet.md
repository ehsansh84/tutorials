<!-- Space: RD -->
<!-- Title: Kubernetes Cheatsheet -->
# Kubernetes Cheatsheet
#### Port forwarding to access pod locally:
```
kubectl port-forward POD_NAME LOCAL_PORT:POD_PORT
```
#### Label nodes:
```
kubectl label node NODE_NAME node-role.kubernetes.io/label=
```
#### Remove Label from nodes:
```
kubectl label node NODE_NAME node-role.kubernetes.io/label-
```
#### Exec into a multi container pod:
```
kubectl exec -it POD_NAME -c CONTAINER_NAME --  bash
```
#### Create a tls secret:
```
kubectl create secret tls SECRET_NAME --cert=path/to/cert/file --key=path/to/key/file 
```
#### Read last 10 logs:
```
kubectl logs --tail=20 POD_NAME
```
#### See kubernetes config:
```
kubectl config view
```
