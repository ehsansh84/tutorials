# Hello Go!
Step 1: 
```commandline
sudo apt install golang
```
Step 2: Confirm the installation by checking for the go version
```commandline
go version
```
Step 3:
```commandline
go get github.com/golang/example/hello
```
In this step you may encounter an error like:
```commandline
go: go.mod file not found in current directory or any parent directory.
        'go get' is no longer supported outside a module.
        To build and install a command, use 'go install' with a version,
        like 'go install example.com/cmd@latest'
        For more information, see https://golang.org/doc/go-get-install-deprecation
        or run 'go help get' or 'go help install'.
```
In this case solve it by using this command:
```commandline
go env -w GO111MODULE=off
```
Step 4: Run your hello world project:
```commandline
~/go/bin/hello
```
Output should be:
> Hello, Go examples!

### References: 
- [How To Install Go on Ubuntu 20.04 Focal Fossa Linux](https://linuxconfig.org/how-to-install-go-on-ubuntu-20-04-focal-fossa-linux)
- [Error message "go: go.mod file not found in current directory or any parent directory; see 'go help modules'"](https://stackoverflow.com/questions/66894200/error-message-go-go-mod-file-not-found-in-current-directory-or-any-parent-dire)
