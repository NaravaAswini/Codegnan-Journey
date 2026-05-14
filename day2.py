"""
Types of Operators in Python
--------------------------------

Assignment
Comparision
Logical
Membership
Indentity
Bitwise


1. Arithmetic Operators
---------------------------

Used for mathematical calculations.

Operator	Meaning 	Example
+	   Addition	        10 + 5
-	   Subtraction	        10 - 5
*	   Multiplication	10 * 5
/	   Division	        10 / 5
//	   Floor Division       10 // 3
%	   Modulus (Remainder)	10 % 3
**	   Power	        2 ** 3

Example
a = 10
b = 3

print(a + b)
print(a % b)
print(a // b)
Output
13
1
3

2. Assignment Operators
------------------------

Used to assign values.

Operator	Example
=	        x = 5
+=	        x += 2
-=	        x -= 2
*=	        x *= 2

3. Comparison Operators
--------------------------

Used to compare values.

Operator	Meaning
==	        Equal
!=	        Not Equal
>	        Greater than
<	        Less than
>=	        Greater or Equal
<=	        Less or Equal
is              Comparing Id's

Note: What is the difference between is and  ==?
Ans: Is an operator looks for object is same or not
Ans: == operator looks for both values equal or not

Example
print(10 > 5)

Output:

True

4. Logical Operators
--------------------------

Used with conditions.

Operator	Meaning
and	        Both conditions true
or	        Any one true
not	        Reverse result

5. Membership Operators
------------------------------

Check whether value exists.

Operator	Example
in	        "a" in "apple"
not in	        "z" not in "apple"

6. Identity Operators
----------------------------

Check whether two variables refer to same object.

Operator	Meaning
is	        Same object
is not	        Different object

Types of Bitwise Operators
Operator	Name
&	AND
`	`
^	XOR
~	NOT
<<	Left Shift
>>	Right Shift


Datatypes in Python
---------------------------

A datatype defines the type of value stored in a variable.
Python uses datatypes to understand:

what kind of data is stored
what operations can be performed on it
how memory should be allocated

Integer Datatype (int) in Python
-----------------------------------------

An integer is a datatype used to store whole numbers without decimal values.

Integers can be:

positive numbers
negative numbers
zero

Python automatically identifies whole numbers as int.

Example
--------
age = 21

print(age)
print(type(age))
Output
21
<class 'int'>

String Datatype (str) in Python
----------------------------------------

A string is a datatype used to store:

text
words
characters

Strings must be written inside quotes:

" "
or ' '

Python treats anything inside quotes as a string.

Example
--------
name = "Aswini"

print(name)
print(type(name))
Output
Aswini
<class 'str'>

any="hello world"
print(any.replace("hello", "hi"))

split() Method in Python
----------------------------------
The split() method is used to break a string into smaller parts.

It separates the string wherever it finds a space (by default) and converts it into a list.

Example
--------
text = "car-bike-bus"

print(text.split("-"))
Output
['car', 'bike', 'bus']

len() Method in Python
---------------------------

The len() function is used to find the total number of characters/items.

Example
--------
text = "Python"

print(len(text))
Explanation

String:

"Python"

Characters are:

P
y
t
h
o
n

Total characters = 6

Slicing in Python
----------------------------------

Slicing is used to extract a part of a string.

Syntax:
-------

string[start : end]
start → starting index
end → stopping index
end value is not included
Example
-------
text = "Python"

print(text[0:4])
Explanation

String:

P  y  t  h  o  n
0  1  2  3  4  5

Slice:

text[0:4]

Starts from index 0
and stops before index 4.

So characters are:

P
y
t
h
Output
Pyth

text = "Python"

print(text[4])

output
------
o

count() Method in Python
-------------------------
The count() method is used to count how many times a character or word appears in a string.
Example
--------
text = "hello"

print(text.count("l"))
Explanation
-----------

String:

hello

Character "l" appears 2 times.

Output
2

join() Method in Python
------------------------------
The join() method is used to combine list items into a single string.

Example
--------
text = ["Python", "Java", "C"]

print("-".join(text))
Explanation
--------------

List items are joined using -.

So:

Python
Java
C

become one string.

Output
Python-Java-C

strip() Method in Python
-------------------------------

The strip() method is used to remove extra spaces from the beginning and ending of a string.
Example
text = "  Python  "

print(text.strip())

Explanation
-----------------

Original string contains spaces before and after "Python".

strip() removes those extra outer spaces.

Output
--------
Python

"""


