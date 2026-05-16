"""Concatination
-----------------
-->The (+) for int and can add, but for the other data types it will act as concatinating the data type

a=90
b=8
print(a+b)
any_="python "
so="is a language"
print(any_+so)
an=[1,2]
am=[3,4]
print(an+am)


Tuple
-------
-->Collection of different datatypes seperated by commas, represented in () and immutable

some=(1, "python", [1,2], [4,6])
print(some)

methods
----------
count
--------
-->This used to count the particular item in the tuple
Index()
--------
-->Used to find out the index position of the item, and only gives the first occurance

print(some.index("python"))
print(some.count("python"))

Dictionary
-------------
-->Dict
--> Dict is a key:value pair, key and value is dseparated by : and pair is separated by 


asw={"name":"aswini", "age":23, 2:4, (33,44):[3,5]}
print(asw)

values()
---------
-->Used ot get all values from the dict
syntax--> dict.vlaues()

aas={"name":"aswini",
    "age":23,
    "num":8106059184}
print(aas.keys())
print(aas.items())
print(aas["age"])

Update()
------------
-->Used to add a new key : value pair into dict
syntax--> dict.update({key:value})

aas={"name":"aswini",
    "age":23,
    "num":8106059184}
aas.update({"age": 24})
print(aas)
aas.update({"age":25})
print(aas)

Clear()
------------
-->Used to remove all the items in the dict


"""
aas={"name":"aswini",
    "age":23,
    "num":8106059184}
aas.clear()
print(aas)







    
