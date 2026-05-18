"""
Sets
---------
A set is a collection of uniqe and unoredered elements
--> Duplicate values are not allowed
-->Items are not stored in index order
--> Represented in {}
Union
--------
--> It will give all values from 2 or more sets together in once without duplication.
-->syntax: Variable_name.union() (another variable)
any={1,2,2,3,4,3}
a = {68, 64}
print(any)
print(any|a)
c=any.union(a)
print(c)

Intersection
--------------
--> to get the common elements from both sets
-->syntax: Variable_name.union() or (another variable)
any={1,2,2,68,3,4,3}
a = {68,3,4,64}
print(any)
print(any & a) # and do not give the ascending order
print(any.intersection(a))

Difference
------------
-->To get the different values or elements from the set
syntax-->variable_name.
any={1,2,2,68,3,4,3}
a = {68,3,4,64,6}
print(any)
print(any - a) # and do not give the ascending order
print(any.difference(a))

add()
--------
-->to add new element into set
syntax-->variable_name.add(element)

any={1,2,2,68,3,4,3}
any.add(66)
print(any)

update()
---------
to add multiple elements into set
syntax:variable_name.update([elemetns])

"""

any={1,2,2,68,3,4,3}
print(max(any))
print(min(any))
any.remove(2) #if any element want to remove in set but it is not in the set then the error is key error.
print(sum(any))
print(any)
any.discard(9)# useed to remove element from the set 
print(any)
print(len(any))
