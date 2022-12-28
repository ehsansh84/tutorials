print('===== Part 1: unpacking a dictionary')
a = {'name': 'ehsan', 'age': 38}
print(a)
print({**a, 'family': 'shirzadi'})

print('===== Part 2: unpacking a list')
a = [1, 2, 3]
print(a)
print([*a, 4, 5])


print('===== Part 3: unpacking function params')


def test(**kwargs):
    print(kwargs)
    print({**kwargs})


test(name='ehsan')
test(name='ehsan', family='shirzadi')
