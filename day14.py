"""
list comprehension
---------------------
-->The list comprehension offers a shortest syntax when we want to create a new list from on existing list.

syntax:
----------
variable_name=[expression loop condition
old=[1,2,3,4]
new=[so for  so in old if so%2==0]
print(new)


old = [22,33,23,34,12,13]
new = [so if so % 2 != 0 else "even" for so in old]
print(new)


generators
---------------
-->Generators in python  are a special type of itterable, allowing users to iterate over data effeciently without storing everything in memory
-->They generate values lazily using yield keyword


def simple():
    print("start")
    yield 1
    yield 2
    yield 3
    print("end")
s=simple()
print(next(s))
print(next(s))
print(next(s))
print(next(s))

why to use gen
------------------
-->Generators do not store the entire dataset in memory, they generate values on the fly.
-->Avoiding unnecessary storage of data speed up execution

how it works
----------------
--> It looks like normal function but uses the yield keyword instead of return
-->when the function is called, it does not execute immediately. instead, it return a generator object which can be iterated using loop or the next() function


def any(n):
    for i in range(n):
        yield i*i
a=any(5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))


def any(n):
    for i in range(n):
        print(i*i)
any(5)

"""

def sq(n):
    res=[]
    for i in range(n):
        res.append(i*i)
    return res
print(sq(5))
        

    
