"""
Polymorphism
-----------------
-->this means 'many forms'.. it allows the same function, method,or operatorto behave differently depending on the object...

1.Method Overloading
-----------------------
class cal:
    def add(self,a,b,c=0):
        return a+b+c
a=cal()
print(a.add(22,33))
print(a.add(11,22,33))

2.Method Overriding
---------------------
-->This occurs when a child class provides its own implementation fo a method already defined in the parent class...

class animal:
    def sound(self):
        print("Animal makes sound")
class dog(animal):
    def sound(self):
        print("Barks")
a=dog()
a.sound()

3. Operator Overloading
--------------------------
-->This allows operators such as +, -,* etc,, to perform different actions for user-defined objects

Note
-----
--> The operator inside the method will overload a special method or operator given in the call....

class stu_:
    def __init__(self, marks):
        self.marks=marks
    def __add__(self, other):
        return self.marks+other.marks
a=stu_(3)
b=stu_(33)
print(a+b)

Data Abstraction
-------------------
-->This is the process of hiding onternal implementation details and dhowing only essential features to the user
-->It foucs on what an object does rather than does it....


"""
from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def perimeters(self):
        pass
class Rec(shape):
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def area(self):
        return self.a*self.b
    def perimeters(self):
        return 2*(self.a * self.b)
a=Rec(10,5)
print(a.area())

