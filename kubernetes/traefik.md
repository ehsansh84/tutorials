<!-- Space: RD -->
<!-- Title: How to install and config Traefik? -->
# How to install and config Traefik?
Create values.yaml like this:
```yaml
---
ports:
  web:
    port: 80
  websecure:
    port: 443

ingressRoute:
  dashboard:
    enabled: false # We will use a custom inrgessRoute with basic auth instead of the default one

# The following lines are needed if you have an error like: error while building entryPoint web: error preparing server: error opening listener: listen tcp :80: bind: permission denied
# It just means that Traefik is unable to listen to connections on the host because of a lack of permissions.
# Hence the need for aditionnal permissions.
securityContext:
  capabilities:
    drop: [ALL]
    add: [NET_BIND_SERVICE]
  readOnlyRootFilesystem: true
  runAsGroup: 0
  runAsNonRoot: false
  runAsUser: 0
```
Now we can install Traefik in our cluster with Helm using the values file:
```
helm repo add traefik https://helm.traefik.io/traefik
helm repo update
helm install --namespace=traefik --create-namespace traefik traefik/traefik -f values.yaml
```
Create a file called `ingressroute.yaml` with the following content:
```yaml
---
apiVersion: traefik.containo.us/v1alpha1
kind: IngressRoute
metadata:
  name: traefik-dashboard
  namespace: traefik
spec:
  entryPoints:
    - web
    - websecure
  routes:
    - match: Host(`traefik.domain.com`) # Hostname to match
      kind: Rule
      services: # Service to redirect requests to
        - name: api@internal # Special service created by Traefik pod
          kind: TraefikService
```
Now you can see dashboard in your browser.
### Secure access to Traefik using basic auth
Set up a basic auth middleware to block access to the dashboard without the correct credentials in `auth.yaml`:
```yaml
---
apiVersion: traefik.containo.us/v1alpha1
kind: Middleware
metadata:
  name: auth
  namespace: traefik
spec:
  basicAuth:
    namespace: traefik
    secret: traefik-auth

---
apiVersion: v1
kind: Secret
metadata:
  name: traefik-auth
  namespace: traefik
data:
  users: |1
   YWRtaW46YWRtaW5AMTIzCg== # username: admin password admin@123
```
Provide user data this way: if needed `apt install apache2-utils`
```
htpasswd -c auth admin
```
Enter password and then `cat auth | base64`

You also need to update the ingressRoute to use this middleware:
```yaml
---
apiVersion: traefik.containo.us/v1alpha1
kind: IngressRoute
metadata:
  name: traefik-dashboard
  namespace: traefik
spec:
  entryPoints:
    - web
    - websecure
  routes:
    - match: Host(`traefik.domain.com`)
      kind: Rule
      services:
        - name: api@internal
          kind: TraefikService
      # Enable auth middleware
      middlewares:
        - name: auth
```
Finally, apply your manifests: 
```
kubectl apply -f auth.yaml
kubectl apply -f ingressroute.yaml
```

#### Refrences:
- [How to configure Traefik on Kubernetes with Cert-manager?](https://www.padok.fr/en/blog/traefik-kubernetes-certmanager)
- [Basic Authentication](https://github.com/kubernetes/ingress-nginx/blob/main/docs/examples/auth/basic/README.md)


