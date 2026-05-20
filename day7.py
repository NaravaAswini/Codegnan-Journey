"""2000
Condition statements
-----------------------
if
nested if
elif

if statement:
---------------
to check weather the statement is ture or not

else
--------
else in the if statement, incase the condition becomes false then it will enter into the flow-back(else), it will execute whatever inside it  statement 

example
---------

n=int(input("enter number:"))
if n%2!=0:
    print(f"{n} is a odd number")
else:
    print(f"{n}is a even number")


n=int(input("enter age:"))
if n>=18:
    print("elgible")
else:
    print(f"we will wait for {18-n} more years")


a=int(input("enter a:"))
b=int(input("enter b:"))
if a>b:
    print(a," is big")
else:
    print(b, "is small")


year=int(input("enter year:"))
if(year%4==0 and year%100!=0) or (year%400==0):
    print(f"{year} is leap year")
else:
    print(f"{year} not leap year")


n=int(input("enter a number:"))
if n>=0:
    print(f"{n} is positive")
else:
    print(f"{n} is negitive")


"""
signal = input("enter red\n or green\n: ")

if signal == "red":
    print(f"{signal} stop")

else:
    print(f"{signal} go")
