"""time_=input("enter 24 hour time:")
part=time_.split(":")
hour=int(part[0])
min_=int(part[1])
print(f"{time_} converted into normal clock {hour-12}:{min_}  pm")

List
------
--->List is collection of different data type
--->[] and separated by ,

example
---------
any=[1, "aswini", [1,2]]
print(any)

"""

#any=[1,"python",[1,2],[34,"ths is python 3rd class",78],"pyhton is a language",89],34,[3,4]
"""for i in any:
    if "p" in str(i)
        print("p")
        break"""
"""any=[1,"python",[1,2],[34,"ths is python 3rd class",78],
     "pyhton is a language",89,34,[3,4]]

print(any[5])



""{Append
---------
--> thismethod is used to add new item into list, and it will in the last index position

syntax--> variable_name.append(item)"""


"""item=[23,33,44]

item.append(44)

print(item)


Immutable
-------------
-->Could not able to  modify on that particular variable

example
--------
int, str

mutable
---------
--> Can able to modify on that particular variable
example
----------
list

s="python is prg"
print(s.replace("python", "java"))
print(s)


Extend
---------

-->this method is used to add new itterable into list, and it will in the last index position, each value or substring is each index in the list

example
--------
syntax-->variable_name.extend (itterables)

s=[2,3,4,5]
s.extend("aswini")
print(s)


append() Method (Push)
----------------------------
Description
--------------

append() is used to add an element at the end of the list.

Syntax:
--------

list_name.append(value)
The original list gets modified.
It does not return a new list.
Example
numbers = [1, 2, 3]

numbers.append(4)

print(numbers)
Output
[1, 2, 3, 4]

Explanation:
--------------

4 is added at the end of the list.
pop() Method

Description
---------------

pop() is used to remove the last element from the list.

Syntax:
----------

list_name.pop()
Removes the last item.
Returns the removed value.

Example
-----------
numbers = [1, 2, 3, 4]

numbers.pop()

print(numbers)

Output
----------
[1, 2, 3]

Explanation:

4 is removed from the list.
pop(index) Example

You can also remove an element using its index.

numbers = [10, 20, 30, 40]

numbers.pop(1)

print(numbers)
Output
-------
[10, 30, 40]

Explanation:
-------------

Index 1 contains 20
So 20 is removed.
Push and Pop Example (Stack)
stack = []

# Push elements
stack.append(10)
stack.append(20)
stack.append(30)

print(stack)

# Pop element
removed = stack.pop()

print(removed)
print(stack)
Output
[10, 20, 30]
30
[10, 20]
