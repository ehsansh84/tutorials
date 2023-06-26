# How to use Python caching?

### Use `lru_cache` like this:
```python
from functools import lru_cache
from time import sleep


@lru_cache(maxsize=None)  # No limit on cache size
def expensive_function(n):
    result = 0
    for i in range(n):
        result += i
        sleep(1)
    return result


print(expensive_function(5))
print(expensive_function(5))
```

In this function it takes 5 seconds for the first run, but it returns immediately for the second run.

# References:
- []()
- []()
- []()
