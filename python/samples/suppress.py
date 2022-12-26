from contextlib import suppress
x = 0
try:
    a = 10 / x
except:
    print('An error happened')

try:
    a = 10 / x
except:
    pass

with suppress(ZeroDivisionError):
    a = 10 / x



