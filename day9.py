"""
for loop
------------

n=int(input("enter:"))
for i in range(1,11):
    print(f"{n} * {i} = {i*n}")


palindrome
-----------

so=input()
emp=""
for i in so:
    emp=i+emp
if emp==so:
    print("pal")
else:
    print("not")


armstrong
-----------

n=int(input("enter:"))
am=0
le=len(str(n))
for i in range(str(n)):
    am+=int(n)**le
if am==n:
    print("yes")
else:
    print("no")

perfect
---------

n=int(input("enter:"))
temp=0
for i in range(1,n):
    if n%i==0:
        temp=temp+i
if temp==n:
    print("yes")
else:
    print("no")


prime
--------

n=int(input("enter num:"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count=count+1
if count==2:
    print("prime")
else:
    print("not")

shapes
--------

for i in range(1,6):
    ch = 97
    for j in range(i):
        print(chr(ch), end="  ")
        ch = ch + 1
    print()


a=5
cou=0
for i in range(1,a):
    for j in range(1, i+1):
        count+=1
        print(j, end=" ")
    print()



n = 0
for i in range(1,9):
    for j in range(i):
        print(n, end=" ")
        n = n + 1

    print()




a=4
count=0
for i in range(a,0,-1):
    for j in range(i):
        count+=1
        print(d, end=" ")
    print()
    """

for i in range(1,6):
    print(" "*(5-i), end="")
    for j in range(i):
        print("*", end=" ")
    print()

        
