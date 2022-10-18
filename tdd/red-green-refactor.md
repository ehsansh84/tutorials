# A step-by-step example for Red-Green-Refactor
ُ#TODO: Raw text
As you already know test driven development is the process of testing for the outcome before writing the implementation logic. This is a counter intuitive way to develop because the way that coding is typically done is in the following format: 

`Design -> Implement -> Test` 

However, with TDD the process is as follows:

`Test -> Design -> Implement`

This backwards thinking has been promoted by respected agile practitioners because it's very possible to make the wrong assumption when you’re writing the business logic first. 

Therefore, the first step in test driven development is to write a test that fails. When the test is in the failed state it's called `RED`.

Next, the programmer must write just enough functionality so that the test now passes. Once the test passes this is called `GREEN`. 

The next stage is to `REFACTOR` which is when the code is continuously cleaned up. Duplicate code is removed, variables are given more meaningful names, and complexity is removed while still keeping the functionality of the code the same. 

Now that we had a brief review of TDD let’s work through an example. Let’s say that we want to create a python script that simulates basic financial applications. 

The functionality that we want the script to have is as follows:

- cash flow: Income - Expenses 
- Net worth: Assets - debts
- Net income: Revenue - expenses 
- Simple interest: I = p x r x  (p is principal, r is interest rate, and t is how long the money is borrowed in years)
- Gains (or losses): (Market price - purchase price) / purchase price 

Let's take the TDD approach to building this script for these formulas. According to TDD the first step is RED, so we must first get the test to fail. 

I created a file called test_finances.py and then added the following code to it:
```python
import unittest
class TestFinances(unittest.TestCase):
   def test_cash_flow(self):
       self.assertTrue(self.cf(10000, 5500), 4500)

if __name__ == '__main__':
   unittest.TestCase()
```
When ran, the output states the following:
```
Ran 1 test in 0.004s
```

FAILED (errors=1)

We're in the red and rightfully so. We never created a class that had the cf method which is short for cash flow. Therefore, the next step is to get to GREEN by creating a class with the method cf and writing the absolute minimum code to get it to pass. 

The file we created is finance_formulas.py as listed below:
```python
class Finance:
   """
   This is a class which implements several
   finance formulas using the TDD
   approach:
   """
   def cf(self, income, expenses):
       if income < 0:
           return
       return income - expenses
```
Now, let's go back and re-run our test in test_finances.py. 

When ran here’s the output:
```
Ran 1 test in 0.005s
OK
```

YAY! Our test now passes so we’re in the `GREEN`. 

However, we’re roughly 66.6% of the way done because we now must refactor. 	

We can go back to finance_formulas.py and rename the method from cf to something more meaningful like cash_flow. 

And guess what’s cool about doing TDD? The RED-GREEN-REFACTOR mantra serves as a safety belt because if you mess something up during refactoring then your unit test will fail giving you a better indication on what went wrong. 

The accompanying lab for this section will give you more practice with applying the TDD approach by filing out the rest of the tests and adding their corresponding functionality. 