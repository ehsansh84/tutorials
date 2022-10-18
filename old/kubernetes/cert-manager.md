<!-- Space: RD -->
<!-- Title: How to work with cert manager to issue certificates -->
# How to work with cert manager to issue certificates?
Create a `ClusterIssuer` for staging:
```yaml
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-staging
spec:
  acme:
    email: your@email.com
    server: https://acme-staging-v02.api.letsencrypt.org/directory
    privateKeySecretRef:
      # Secret resource used to store the account's private key.
      name: your-own-very-secretive-key
    solvers:
      - http01:
          ingress:
            class: traefik-cert-manager
```

###Issuer
An Issuer or ClusterIssuer identifies which Certificate Authority cert-manager will use to issue a certificate. Issuer is a namespaced resource allowing you to use different CAs in each namespace, a ClusterIssuer is used to issue certificates in any namespace. Configuration depends on which ACME challenge you are using.

#### Refrences:
- [How to easily(ish!) get SSL/TLS configured for your web hosting needs using Traefik and cert-manager on Kubernetes](https://medium.com/@alexgued3s/how-to-easily-ish-471307f276a9)
- [Using cert-manager](https://www.getambassador.io/docs/emissary/latest/howtos/cert-manager/)


