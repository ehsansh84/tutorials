# Senior Python developer interview questions
### Q01-How To Avoid Nested Loops?
The following program uses nested loops, which may be not readable enough. How will you optimise it?
```python
list_a = [1, 2020, 70]
list_b = [2, 4, 7, 2000]
list_c = [3, 70, 7]

for a in list_a:
    for b in list_b:
        for c in list_c:
            if a + b + c == 2077:
                print(a, b, c)
# 70 2000 7
```
Answer:
It’s possible to optimise this using the `product` function.
```python
from itertools import product

list_a = [1, 2020, 70]
list_b = [2, 4, 7, 2000]
list_c = [3, 70, 7]

for a, b, c in product(list_a, list_b, list_c):
    if a + b + c == 2077:
        print(a, b, c)
# 70 2000 7
```



### References:
- [Senior Python Developer interview questions and answers](https://resources.workable.com/senior-python-developer-interview-questions)
- [10 Python Interview Questions for Senior Developers](https://medium.com/techtofreedom/10-python-interview-questions-for-senior-developers-4fefe773719a)
- []()
- []()