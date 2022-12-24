# What is PEP8?
PEP: Python Enterprise Proposal.  
It's a kind of standard to improve Python code quality and make your code more readable and created by Guido van Rossum in 2001.   
PEP 8 helps developers to write beautiful code.
#TODO: still working on it.

### What is `# noqa` in python comments?
Adding `# noqa` to a line indicates that the linter (a program that automatically checks code quality) should not check
this line. Any warnings that code may have generated will be ignored.
for example consider this code:
```python
import os
print("hello world!")
```
As you didn't use `os` library, `import os` command is useless and code quality checker softwares usually warn about that.
In case you don't want to get a warning for this purpose you can use `# noqa` this way:
```python
import os # noqa
print("hello world!")
```

# References:
- [PEP 8 in Python | what is the purpose of PEP 8 in Python?](https://www.javatpoint.com/pep-8-in-python)
- [What does '# noqa' mean in Python comments?](https://stackoverflow.com/questions/45346575/what-does-noqa-mean-in-python-comments)
- []()
- []()