<!-- Space: RD -->
<!-- Title: What is Falco project? -->
# What is Falco project?
Falco detects threats at runtime by observing the behavior of your applications and containers.  
Falco is the first runtime security project to join CNCF as an incubation-level project. Falco acts as a security camera detecting unexpected behavior, intrusions, and data theft in real time.
- `Strengthen container security:` The flexible rules engine allows you to describe any type of host or container behavior or activity.
- `Reduce risk via immediate alerts:` You can immediately respond to policy violation alerts and integrate Falco within your response workflows.
- `Leverage most current detection rules:` Falco out-of-the box rules alert on malicious activity and CVE exploits.
### What does Falco do?
Falco uses system calls to secure and monitor a system, by:
- Parsing the Linux system calls from the kernel at runtime
- Asserting the stream against a powerful rules engine
- Alerting when a rule is violated
### What does Falco check for?
Falco ships with a default set of rules that check the kernel for unusual behavior such as:
- Privilege escalation using privileged containers
- Namespace changes using tools like setns
- Read/Writes to well-known directories such as /etc, /usr/bin, /usr/sbin, etc
- Creating symlinks
- Ownership and Mode changes
- Unexpected network connections or socket mutations
- Spawned processes using execve
- Executing shell binaries such as sh, bash, csh, zsh, etc
- Executing SSH binaries such as ssh, scp, sftp, etc
- Mutating Linux coreutils executables
- Mutating login binaries
- Mutating shadowutil or passwd executables such as shadowconfig, pwck, chpasswd, getpasswd, change, useradd, etc, and others.
### What are the Components of Falco?
Falco is composed of three main components:
- Userspace program - is the CLI tool falco that you can use to interact with Falco. The userspace program handles signals, parses information from a Falco driver, and sends alerts.
- Configuration - defines how Falco is run, what rules to assert, and how to perform alerts. For more information, see Configuration.
- Driver - is a software that adheres to the Falco driver specification and sends a stream of system call information. You cannot run Falco without installing a driver. Currently, Falco supports the following drivers:
  - (Default) Kernel module built on libscap and libsinsp C++ libraries
  - BPF probe built from the same modules
  - Userspace instrumentation
- Plugins - allow users to extend the functionality of falco libraries/falco executable by adding new event sources and new fields that can extract information from events. For more information, see Plugins.


#### Refrences:
- [The Falco Project](https://falco.org/)
- []()
- []()
