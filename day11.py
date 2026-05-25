"""
assert
-----------
this is debugging statement used to test whether a condition is True
if False it throws the error is Assertion Error
n=11
assert n>55
print("True")


Functions
-----------
A function is block of code which only execute when it is called
--> you can pass data,known as parameters into a function
-->To avoid repeated lines in code

def function_name(parameters):
    ---------------
    ---------------
function_name(arguments)


n=4
def even(n):
    if n%2==0:
        print("Yes")
    else:
        print("No")
even(n)
even(99)

ways to pass arguments
-----------------------
-->required arguments
-------------------------
-->a function must be called with the same number of arguments
def even(n):
    if n%2==0:
        print(f"{n} even")
    else:
        print(f"{n} odd")
even(100,33)c


default arguments
------------------
-->by default, values is defined at parameters even tho it will take from the arguments

def even(name="aswini",age=23, sal=40):
    print(name)
    print(age)
    print(sal)
even("narava",22,30)

keyword length arguments
----------------------------
-->We can send arguments with key=value syntax. By this, the order of arguments doesn't matter

def even(age, sal, name):
    print(name)
    print(age)
    print(sal)
even(name="aswini", age=22, sal=40)

Variable length argument
----------------------------
-->Adding a star(*)  before the parameter name in the function, receive a tuple of arguments and can accss items with indexes

def even(*name):
    print(name[1])
even("aswini","narava",82)


name="t"
 def even(a):
     print(a)
even(name)
"""

for num in range(2, 101):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)
    
