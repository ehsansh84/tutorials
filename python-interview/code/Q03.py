def str_len(n):
    return len(n)


x = map(str_len, ('apple', 'banana', 'cherry'))
print(list(x))


def sum(a, b):
    return a + b


x = map(sum, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
print(list(x))


def full_name(info):
    return f'{info["name"]} {info["family"]}'


x = map(full_name, [{'name': 'ehsan', 'family': 'shirzadi'},
                    {'name': 'faraneh', 'family': 'erfani'},
                    {'name': 'ali', 'family': 'rezaei'}, ])
print(list(x))
