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

#### Refrences:
- [Install static binaries](https://docs.docker.com/engine/install/binaries/#install-daemon-and-client-binaries-on-linux)
