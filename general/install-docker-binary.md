<!-- Space: RD -->
<!-- Title: How to install Docker engine from binary? -->
# How to install Docker engine from binary?

1. Download the static binary archive from https://download.docker.com/linux/static/stable/
2. Extract the archive:
```commandline
tar xzvf /path/to/<FILE>.tar.gz
```
3. Optional: Move the binaries to a directory on your executable path, such as `/usr/bin/`
```commandline
sudo cp docker/* /usr/bin/
```
4. Start the Docker daemon:
```commandline
sudo dockerd &
```
- If you need to start the daemon with additional options, modify the above command accordingly or create and edit the file `/etc/docker/daemon.json` to add the custom configuration options.
5. Verify that Docker is installed correctly by running the hello-world image.
```commandline
sudo docker run hello-world
```

### Sertup docker service:
Put these files inside `/etc/systemd/system`:
`docker.service`:
```commandline
[Unit]
Description=Docker Application Container Engine
Documentation=https://docs.docker.com
After=network-online.target docker.socket firewalld.service containerd.service time-set.target
Wants=network-online.target containerd.service
Requires=docker.socket

[Service]
Type=notify
# the default is not to use systemd for cgroups because the delegate issues still
# exists and systemd currently does not support the cgroup feature set required
# for containers run by docker
ExecStart=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
ExecReload=/bin/kill -s HUP $MAINPID
TimeoutStartSec=0
RestartSec=2
Restart=always

# Note that StartLimit* options were moved from "Service" to "Unit" in systemd 229.
# Both the old, and new location are accepted by systemd 229 and up, so using the old location
# to make them work for either version of systemd.
StartLimitBurst=3

# Note that StartLimitInterval was renamed to StartLimitIntervalSec in systemd 230.
# Both the old, and new name are accepted by systemd 230 and up, so using the old name to make
# this option work for either version of systemd.
StartLimitInterval=60s

# Having non-zero Limit*s causes performance problems due to accounting overhead
# in the kernel. We recommend using cgroups to do container-local accounting.
LimitNOFILE=infinity
LimitNPROC=infinity
LimitCORE=infinity

# Comment TasksMax if your systemd version does not support it.
# Only systemd 226 and above support this option.
TasksMax=infinity

# set delegate yes so that systemd does not reset the cgroups of docker containers
Delegate=yes

# kill only the docker process, not all processes in the cgroup
KillMode=process
OOMScoreAdjust=-500

[Install]
WantedBy=multi-user.target
```
`docker.socket`:
```commandline
[Unit]
Description=Docker Socket for the API

[Socket]
# If /var/run is not implemented as a symlink to /run, you may need to
# specify ListenStream=/var/run/docker.sock instead.
ListenStream=/run/docker.sock
SocketMode=0660
SocketUser=root
SocketGroup=docker

[Install]
WantedBy=sockets.target
```


#### Refrences:
- [Install static binaries](https://docs.docker.com/engine/install/binaries/#install-daemon-and-client-binaries-on-linux)
- [How to configure systemctl service for docker installed from binaries?](https://stackoverflow.com/questions/68829478/how-to-configure-systemctl-service-for-docker-installed-from-binaries)
