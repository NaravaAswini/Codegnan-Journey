"""
Inheritance
-------------
-->This allows one class to aquire the properties and methods of another class..
types
-------
single Inheritance
------------------------
-->A class inherts from a single parent class....
ex
---
class father:
    def Land(self):
        print("I am father have 5A")
class Aswini(father):                                       
    def my(self):
        print("i hve 2 A")
fam=Aswini()
fam.Land()

Multiple Inheritance
---------------------------
-->Child class inherts from more than one parent class....
eg
----
class father:
    def Land(self):
        print("I am father have 5A")
class mother:
        def gold(self):
            print("my mother have 1kg gold")
class Aswini(mother, father):
    def my(self):
        print("i hve 2 A")
fam=Aswini()
fam.Land()
fam.gold()

Multi-level Inheritance
--------------------------
-->A class inherts from a parent class and another class inherts from that child class
eg:
----
class gfather:
    def Land(self):
        print("I am father have 5A")
class father(gfather):
    def gold(self):
            print("my mother have 1kg gold")
class son(father):
    def ntg(self):
        print("i do not have")
a=son()
a.Land()
a.gold()
a.ntg()

Hierarchical Inheritance
----------------------------                                                                                                                                                                  
--->Multiple child classes inherts from a single parent....
eg
-----

class father:
    def Land(self):
        print("I am father have 5A")
class aswini(father):
    def gold(self):
            print("my mother have 1kg gold")
class gowtham(father):
    def ntg(self):
        print("i do not have")
a=aswini()
a.Land()
b=gowtham()
b.Land()

Hybride Inheritance
-----------------------
-->This is the combination of two or more types of inheritance

class GrandFather:
    def land(self):
        print("5 Acres Land")
class Father(GrandFather):
    def house(self):
        print("House")
class Mother:
    def gold(self):
        print("1 Kg Gold")
class Son(Father, Mother):
    def bike(self):
        print("Bike")
s = Son()

s.land()
s.house()
s.gold()
s.bike()

Super method
-----------------
-->Super() is used to access methods and consturctor of the parent class from the child class.

eg
------
class parent:
    def dis(self):
        print('method parent')
class child(parent):
    def dis(self):
        super().dis()
        print('method child')
a=child()
a.dis()


"""
 
class parent:
    def __init__(self,name):
        self.name=name
class stu_(person):
    def __init__(self, name, roll):
        super().__init__(name):
            self.roll=roll
    def show(self):
        print(f"name: {self.name}")
        print(f"Roll No: {self.roll}")

a=stu_('teja', 102)
a.show()
