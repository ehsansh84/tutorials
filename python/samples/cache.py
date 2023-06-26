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
