# Some advanced Python tips

### `surpass` an error?
Probably you know how to handle exceptions in python like this:
```python
x = 0
try:
    a = 10 / x 
except:
    # some code here
```
Sometimes you don't need to tell python what to do in case of an error, you just want program works and not terminate.
In this case you can put a 'pass' in except part or use suppress like this:
```python
x = 0
from contextlib import suppress
with suppress(ZeroDivisionError):
    a = 10 / x
```
You can see the examples in `suppress.py`
***



# References:
- [Suppress Exceptions in Python](https://www.pythonforbeginners.com/basics/suppress-exceptions-in-python)
- []()
- []()
