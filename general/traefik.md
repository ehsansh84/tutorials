# Run Traefik ingress controller
Original helm repository: https://github.com/traefik/traefik-helm-chart/tree/master/traefik

Contents of `values.yaml`:
```yaml
service:
  type: NodePort
ports:
  web:
    nodePort: 32080
  websecure:
    nodePort: 32443
logs:
    level: INFO
env:
  - name: TZ
    value: Asia/Tehran
image:
  pullPolicy: IfNotPresent
```
### Finally run:
```
$ helm repo add traefik https://helm.traefik.io/traefik 
$ helm install traefik traefik/traefik -f values.yaml
```
