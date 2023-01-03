### Working with `pytest`
- All tests must start with `test_`.
- assert decides if test can pass or not.
- Any uncaught exception raised within a test will cause the test to fail. 
```python
# 01_test_one.py
def test_passing():
    assert (1, 2, 3) == (1, 2, 3)
```
To run this test, install `pytest`:
```commandline
pip install pytest
```
Now you can run the test above using:
```commandline
pytest 01_test_one.py
```
And the result is like:
```
collected 1 item                                                                                                                                                                                                                       

01_test_one.py .  
```
A green dot after `01_test_one.py` means that the test is passed.
You can have more verbose result using `-v`:
```commandline
pytest 01_test_one.py -v
```
And the result is like:
```
==================== test session starts ====================
collected 1 item                                                                                                                                                                                                                       

01_test_one.py::test_passing PASSED                                                                                                                                                                                              [100%]
==================== 1 passed in 0.01s ====================
```
Now a failing test:
```python
# 02_test_two.py
def test_failing():
    assert (1, 2, 3) == (1, 2, 4)
```
Run:
```commandline
pytest 02_test_two.py
```
And the result is like:
```
==================== test session starts ====================
collected 1 item                                                                                                                                                                                                                       

02_test_two.py F                                                                                                                                                                                                                 [100%]

========================= FAILURES ==========================
----------------------- test_passing ------------------------

    def test_passing():
>       assert (1, 2, 3) == (1, 2, 4)
E       assert (1, 2, 3) == (1, 2, 4)
E         At index 2 diff: 3 != 4
E         Use -v to get more diff

02_test_two.py:2: AssertionError
==================== short test summary info ====================
FAILED 02_test_two.py::test_passing - assert (1, 2, 3) == (1, 2, 4)
======================== 1 failed in 0.02s ======================
```
And also you can see the result more verbose:
```commandline
pytest 02_test_two.py -v
```
And the result is like:
```
================================ test session starts ===========================
collected 1 item                                                                                                                                                                                                                       

02_test_two.py::test_passing FAILED                                                                                                                                                                                              [100%]

===================================== FAILURES =================================
----------------------------------- test_passing -------------------------------

    def test_passing():
>       assert (1, 2, 3) == (1, 2, 4)
E       assert (1, 2, 3) == (1, 2, 4)
E         At index 2 diff: 3 != 4
E         Full diff:
E         - (1, 2, 4)
E         ?        ^
E         + (1, 2, 3)
E         ?        ^

02_test_two.py:2: AssertionError
=============================== short test summary info ========================
FAILED 02_test_two.py::test_passing - assert (1, 2, 3) == (1, 2, 4)
================================= 1 failed in 0.02s ============================
```
Ofcourse you may not want to see a lot of details, so you can turn of tracebacks:
```python
pytest 02_test_two.py --tb=no
```
And you have a simple report:
```
============================ test session starts =================================
platform linux -- Python 3.10.6, pytest-7.2.0, pluggy-1.0.0
rootdir: /home/ehsan/dev/tutorials/pytest/tests
plugins: anyio-3.6.2
collected 1 item                                                                                                                                                                                                                       

02_test_two.py F                                                                                                                                                                                                                 [100%]

========================== short test summary info ===============================
FAILED 02_test_two.py::test_passing - assert (1, 2, 3) == (1, 2, 4)
=========================== 1 failed in 0.01s ====================================
```
How to run both tests?
```python
pytest 01_test_one.py 02_test_two.py --tb=no
```
You can see the results for both test files:
```
=============================== test session starts ==============================
platform linux -- Python 3.10.6, pytest-7.2.0, pluggy-1.0.0
rootdir: /home/ehsan/dev/tutorials/pytest/tests
plugins: anyio-3.6.2
collected 2 items                                                                                                                                                                                                                      

01_test_one.py .                                                                                                                                                                                                                 [ 50%]
02_test_two.py F                                                                                                                                                                                                                 [100%]

============================ short test summary info =============================
FAILED 02_test_two.py::test_passing - assert (1, 2, 3) == (1, 2, 4)
========================== 1 failed, 1 passed in 0.01s ===========================
```
If you want to run all tests inside a directory you can use a * instead of all names:
```python
pytest * --tb=no
```


### References:
- [Rapidleech Github](https://github.com/redwangtc/Rapidleech)
- []()
- 