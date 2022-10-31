# How to do a load test using wrk?
### Step 1: ّInstall wrk:
#### Method 1:
```
sudo apt install wrk
```
#### Method 2: from source
```
git clone https://github.com/wg/wrk.git
cd wrk
make
./wrk -v
```
In case you do not have necessary tools, you may need to install:
```
apt install make
apt install unzip
apt install gcc
```

### Now demos:
#### Demo 1:
By default 2 threads and 10 connections
```
wrk http://SERVER_IP:PORT
```
### Demo 2:
Using 100 threads and 100 connections
```
wrk -t100 -c100 http://SERVER_IP:PORT
```

### References:
- [wrk - modern HTTP benchmarking tool](https://www.youtube.com/watch?v=idJIVvSDPrk)
