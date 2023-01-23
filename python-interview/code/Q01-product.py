list_a = [1, 2020, 70]
list_b = [2, 4, 7, 2000]
list_c = [3, 70, 7]


def using_loops():
    for a in list_a:
        for b in list_b:
            for c in list_c:
                if a + b + c == 2077:
                    print(a, b, c)


def using_product():
    from itertools import product
    for a, b, c in product(list_a, list_b, list_c):
        if a + b + c == 2077:
            print(a, b, c)


using_loops()
using_product()
