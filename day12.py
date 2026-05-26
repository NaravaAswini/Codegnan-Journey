
"""
built-in functions:
----------------------
print()
input()
len()
type()
max()
min()

a=[1,3,4,2,5]
a.sort()
print(a)
print(a)

Recursice functions
--------------------
-->recursive function that calls itself to solve program by breaking  it into small or simple sub-problems 

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))

armstrong using function
--------------------------
def armstrong(n):
    temp=n
    sum=0
    while n>0:
        digit=n%10
        sum=sum+digit**3
        n=n//10
    if temp==sum:
        print("yes")
    else:
        print("no")
n=int(input("enter num:"))
armstrong(n)


def perfect(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    if sum==n:
        print("yes")
    else:
        print("no")
n=int(input("enter num:"))
perfect(n)
"""

def prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count=count+1
    if count==2:
        print("yes")
    else:
        print("no")
n=int(input("enter:"))
prime(n)
            
            
            
