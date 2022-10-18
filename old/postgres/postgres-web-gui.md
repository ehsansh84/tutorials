<!-- Space: RD -->
<!-- Title: How to install a web gui for Postgres -->
# How to install a web gui for Postgres
You can easily manage Postgres through a webgui:
```yaml
apiVersion: v1
kind: Pod
metadata:
  labels:
    run: pgweb
  name: pgweb
spec:
  containers:
    - image: sosedoff/pgweb
      name: pgweb
      ports:
        - containerPort: 8081
---
apiVersion: v1
kind: Service
metadata:
  labels:
    run: pgweb
  name: pgweb-svc
spec:
  ports:
    - port: 8081
      targetPort: 8081
      protocol: TCP
  type: NodePort
  selector:
    run: pgweb
```

#### Refrences:
- [Secure Access to PostgreSQL with Pgweb](https://www.suse.com/c/rancher_blog/secure-access-to-postgresql-with-pgweb/)

