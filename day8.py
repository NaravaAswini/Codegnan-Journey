"""
marks=int(input("enter marks:"))
if marks>=90:
    print("A+")
if marks<=:90
    print("A+")
if marks>=70:
    print("A")
if marks>=60:
    print("B+")
if marks>=50:
    print("B")
if marks>=40:


    print("C+")
if marks>=35:
    print("A+")
else:
    print("Fail")

a=int(input("enter a number:"))
b=int(input("enter b number:"))
c=int(input("enter c number:"))
if a>=b and a>=c:
    print(a,"a is big")
elif b>=a and b>=c:
    print(b,"b is big")
else:
    print(c,"c is big")



Nested if
-----------


sbi={"pin":1234}
pin=input("enter pin:")
if len(pin)==4:
    if pin == sbi['pin']:
        print("welcome to sbi")
    else:
        print("not valid")
else:
    print("enter valid pin")

for statetment
----------------
--> used to itterate over a squence


any="python"
so=[1,2,3,4]
for i in any:
    print(i)

range()
-------
--> range is a in-built function used to generate numbers in  squence manner

-->syntax: range(start,end,step)

else in for
--------------
once the itteration completed this else will be executed 


for i in range(20, 40):
    print(i)

break
----------
-->break is used to exit from the loop based on the condition

for j in range(1,10):
    print(j)
else:
    print("code is ended")


for i in range(1, 10):
    if i==5:
        break
    print(i)

continue
----------
-->used to skip that current itteration based on the condition

for i in range(1,10):
    if i==3:
        continue
    print(i)

pass
---------
-->pass is a placeholder

for i in range(1,10):
    if i==3:

      pass

"""

i=1
while i<=5:
    i=i+1
    print(i)
    

    




