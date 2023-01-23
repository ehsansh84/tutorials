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



### Q02: Uses of Eval Functions
Can you implement a function in one line of Python code, which will receive two numbers a and b and a string op.
The op stands for an arithmetic operator, such as `+`, `-`, `*` and `/`. Your function needs to return the
calculated result of a op b.

Answer:
```python
def cal(a, b, op): return eval(f’{a} {op} {b}’)
```

### Q03: What is the use of the map function in Python?
The map() function helps execute a function for all items in the iterated object (list, dictionary, set, or tuple).
It has two arguments:
- Function specifies a function that will be executed on each object.
- Iterable specifies a data collection or a sequence to which a function will be applied.

### References:
- [Senior Python Developer interview questions and answers](https://resources.workable.com/senior-python-developer-interview-questions)
- [10 Python Interview Questions for Senior Developers](https://medium.com/techtofreedom/10-python-interview-questions-for-senior-developers-4fefe773719a)
- [25 Python Developer Interview Questions to Ask Junior, Middle, and Senior Programmers](https://bridgeteams.com/blog/25-python-developer-interview-questions-to-ask-junior-middle-and-senior-programmers/)
- [Senior Python Developer Interview Questions](https://breezy.hr/resources/interview-questions/senior-python-developer)