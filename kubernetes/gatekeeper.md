<!-- Space: RD -->
<!-- Title: What is gatekeeper -->
# What is gatekeeper?
Gatekeeper helps reduce the dependency between DevOps admins and the developers themselves. Enforcement of your organization's policies can be automated, which frees DevOps engineers from worrying about developers making mistakes.  
OPA Gatekeeper, a subproject of Open Policy Agent, is specifically designed to implement OPA into a Kubernetes cluster.
### Why use OPA Gatekeeper?
OPA Gatekeeper provides you with two critical abilities:
- Control what the end user can do on the cluster
- Enforce company policies in the cluster

### How to use OPA:
- Integrate with OPA: If your services are written in Go, you can embed OPA as a package within your project. Otherwise, you can deploy OPA as a host-level daemon.
- Write and store your policies: To define your policies in OPA, you need to write them in Rego and send them to OPA. This way, whenever you use OPA for policy enforcement, OPA will query the input against these policies.
- Request policy evaluation: When your application needs to make a policy decision, it will send an API query request using JSON, containing all the required data via HTTP.
### When a request comes into the Kubernetes API, it passes through a series of steps before it's executed.
- The request is authenticated and authorized.
- The request is processed by a list of special Kubernetes webhooks collections called admission controllers that can mutate, modify, and validate the objects in the request.
- The request is persisted into etcd to be executed.
### How to use OPA:
- Integrate with OPA: If your services are written in Go, you can embed OPA as a package within your project. Otherwise, you can deploy OPA as a host-level daemon.
- Write and store your policies: To define your policies in OPA, you need to write them in Rego and send them to OPA. This way, whenever you use OPA for policy enforcement, OPA will query the input against these policies.
- Request policy evaluation: When your application needs to make a policy decision, it will send an API query request using JSON, containing all the required data via HTTP.

# Kubernetes admission webhooks
When a request comes into the Kubernetes API, it passes through a series of steps before it's executed.
- The request is authenticated and authorized.
- The request is processed by a list of special Kubernetes webhooks collections called admission controllers that can mutate, modify, and validate the objects in the request.
- The request is persisted into etcd to be executed.  

Admission controllers are middle wares that manage deployments requesting too many resources, enforce pod security policies, and even block vulnerable images from being deployed.
There are two types of admission controllers:
- MutatingAdmissionWebhook => Enforce custom defaults
- ValidatingAdmissionWebhook =< ٍEnforce custom policies

...

### How is Gatekeeper different from OPA?
Gatekeeper introduces the following functionality:



#### Refrences:
- [Why use OPA Gatekeeper?](https://opensource.com/article/21/12/kubernetes-gatekeeper)
- [How is Gatekeeper different from OPA?](https://open-policy-agent.github.io/gatekeeper/website/docs/)
