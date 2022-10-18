<!-- Space: RD -->
<!-- Title: PodMan vs Docker -->

### What is docker?
Docker is the standard container management technology. It has so much weight in the industry that when most people think of containers, they think of Docker.
### What is Podman?
Podman is an open-source, Linux-native tool designed to develop, manage, and run containers and pods under the Open Container Initiative (OCI) standards. Presented as a user-friendly container orchestrator developed by Red Hat.

Command sets:
- Podman - pods and container image manger
- Buildah - a container builder
- Skopeo - a container image inspection manager
- runc - container runner and feature builder to podman and buildah
- crun - optional runtime that allows greater flexibility, control, and security for rootless containers

These tools can also work with any OCI-compatible container engine, like Docker, making it easy to transition to Podman or use it with an existing Docker installation. And can Kubernetes use Podman? Yes it can. In fact, Kubernetes and Podman are similar in some ways.

Podman is daemon-less. Podman is a unique take on the container engine, as it doesn’t actually depend on a daemon, but instead launches containers and pods as child processes.

### Podman vs Docker: Differences:
#### Architecture
Docker uses a daemon, an ongoing program running in the background, to create images and run containers. Podman has a daemon-less architecture which means it can run containers under the user starting the container. Docker has a client-server logic mediated by a daemon; Podman does not need the mediator.
#### Root privileges
Podman, since it doesn't have a daemon to manage its activity, also dispenses root privileges for its containers. Docker recently added rootless mode to its daemon configuration, but Podman used this approach first and promoted it as a fundamental feature. And this is because of the next point.
#### Security
Is Podman safer than Docker? Podman allows for non-root privileges for containers.Rootless containers are considered safer than containers with root privileges. In Docker, daemons have root privileges, making them the preferred gateway for attackers. Containers in Podman do not have root access by default, adding a natural barrier between root and rootless levels, improving security. Still, Podman can run both root and rootless containers.
#### Systemd
Without a daemon, Podman needs another tool to manage services and support running containers in the background. Systemd creates control units for existing containers or to generate new ones. Systemd can also be integrated with Podman allowing it to run containers with systemd enabled by default, without any modification.

By using systemd, vendors can install, run, and manage their applications as containers since most are now exclusively packaged and delivered this way.
#### Building images

As a self-sufficient tool, Docker can build container images on its own. Podman requires the assistance of another tool called Buildah, which expresses its specialized nature: it is made for running but not building containers on its own.
Docker Swarm

Podman does not support Docker Swarm, which may rule it out of the options for projects using this feature since using Docker Swarm commands will generate an error. Podman has recently added support for Docker Compose to make it Swarm compliant, overcoming this limitation. Docker, naturally, works well with Swarm.
All in one vs modular

And maybe this is the crucial difference in both technologies: Docker is a monolithic, powerful, independent tool with all the benefits and drawbacks implied, handling all of the containerization tasks throughout their entire cycle. Podman has a modular approach, relying on specialized tools for specific duties.
Podman vs Docker: Can they work together?

Sold as the best and easiest to apply alternative to Docker - users can just alias Docker to Podman (alias docker=podman) without any problems, as shown in this presentation - Podman is a more than capable tool for containerization tasks.

Is Podman a replacement for Docker?
Podman can be a primary containerization technology option if you are starting a project from scratch. If the project is ongoing and already using Docker, it depends on the specifics, but it might not be worth the effort. As a Linux native application, it demands Linux skills from the developers involved.

Developers can combine both tools by relying on Docker in the development stage and later push the project to Podman in runtime environments, benefitting from the added security it provides. And since they're both OCI-compliant, compatibility shouldn't be a problem.

Can Docker and Podman coexist? Yes, and quite well. Many developers have been using Docker and Podman in tandem to create safer, more efficient, agile frameworks. They have a lot in common, making the transition from Docker to Podman or their combination quite seamless.

You can use Podman firsthand by downloading and installing it on your Linux machine or, if Linux is not available, you can try it online.

#### Refrences:
- [Podman vs Docker: What are the differences?](https://www.imaginarycloud.com/blog/podman-vs-docker/)
