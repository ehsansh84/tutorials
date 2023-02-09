# How to optimize your code using profile?
#### Step1: install library:
```commandline
pip install line_profiler
```
#### Step2: add `@profile` on top of your function
```python
@profile
def sum(a, b):
    return a + b
```
#### Step3: run script using this command:
```commandline
kernprof -lv profile.py
```
See the result:
```commandline
Wrote profile results to profile.py.lprof
Timer unit: 1e-06 s

Total time: 7.51e-07 s
File: profile.py
Function: sum at line 2

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     2                                           @profile
     3                                           def sum(a, b):
     4         1          0.8      0.8    100.0      return a + b


```

# References:
- [Github pyutils/line_profiler ](https://realpython.com/lessons/print-and-breakpoint/)
- []()