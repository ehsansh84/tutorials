# Create your own hello world
Step 1: put this code in `hello-world.go`:
```commandline
package main

import "fmt"

func main() {
    fmt.Println("hello world")
}
```
Step 2: Run
```commandline
$ go run hello-world.go
hello world
```
If you want to build binary do this:
```commandline
$ go build hello-world.go
$ ls
hello-world    hello-world.go
$ ./hello-world
hello world
```

### References: 
- [Go by Example: Hello World](https://gobyexample.com/hello-world)
