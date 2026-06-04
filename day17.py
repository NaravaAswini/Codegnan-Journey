"""
OOPS
-----
1. Class
2. Object

1.Class
--------
-->A class is a blue-print or template used to create object

object
----------
-->an object is an instance of a class
eg:
----
class stu_:
    name="teja"
s1=stu_()
print(s1.name)


class stu:
    def edu(self):
        print("I am studying")
    def sports(self):
        print("cricket")
s=stu()

Attributes
------------
-->Attribute  arethe variables that belongs to a class or an object

eg
----
class stu:
    name='teja'
    age=33
s=stu()
print(s.name)
print(s.age)

class PFS_DA:
    def python(self):
        PFS_DA='Batch_03'
        print("Hello")

    def Flask(self):
        PFS='Batch_03'

all_=PFS_DA()
all_.python()
all_.Flask()

Constructor
------------
-->__init__ is a special method that is automatically called when an object

class ATM:
    def __init__(self, balance,name):
        self.balance=balance
        self.name=name
    def bal_check(self):
        print(f"{self.name} total balance is {self.balance}")
    def name(self):
        print(self.name)
card=ATM(balance=3000,name='aswini')
card.bal_check()
card.name()

Access specifiers
-------------------
public
---------
-->This can be accessed from anywhere in the program 
protect
-----------
-->This is represented using a single underscore(_)
private
---------
-->This is represented using a double underscore(__)


class stu:
    __name='teja'
s=stu()
print(s._stu__name)

Ensapsulation
--------------
-->Is the process of binding  data and methods together
"""
class bank:
    def __init__(self, balance):
        self.__balance=balance
    def dep_(self, amount):
        self.__balance+=amount
    def get_bala(self):
        return self.__balance
acc=bank(2000)
acc.dep_(3000)
print(acc.get_bala())
        


