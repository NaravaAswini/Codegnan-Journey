"""Error Handling
------------------
try block
------------
-->The try  block, test a block of code for error

except
---------
--> the except block let hand if code contain errors


try:
    print(10/0)
except:
    print("zero division error")

try:
    num = int(input("num: "))
    result = 10 / num
    print(result)
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Division by zero is not allowed")

    try:
    print(a)
    print(9 + "a")
except NameError:
    print("This handles NameError")
except TypeError:
    print("This handles TypeError")



else block
-----------
-->This will be executed, if the try block has no error in the code....

try:
    a = 10
    b = 2
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("No error occurred")

finally block:
-------------------
The finally block is used to execute code regardless of whether an exception occurs or not.
It is commonly used for cleanup tasks, such as closing files, releasing resources, or printing a final message.
try:
    

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Result:", result)
finally:
    print("Program execution completed")
"""

