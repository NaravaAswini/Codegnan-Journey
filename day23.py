"""
File handling
-----------------
-->File handler is an object of file to maintain several function of file like, creating, reading, updating and deleting the file.....

open a file
---------------
1. open()
2. with open()

open('filename', 'mode') as name
name.close()
Modes
-------------
'r'-->is used to reading the file, error if file does not exist....
'a'-->is used to add the txt into file, if file at last index, if file does not exist...
'w'-->is used to add the txt into file but it will override of all txt inside file. if the does not exist it will create with that name...
'x'-->used to create the file
'r'-->mode to create...

so=open('demo.txt', 'w')
print(so.write('nxt will be java'))
so.close()


s=open('s.txt','r')
print(s.read())
s.close()

with open('s.txt', 'w')as so:
          print(so.write('java'))

methods
-------------
write()
read()
---------
-->This method can read entire file chunk where we can specify the side

readline()
------------
-->can read only one line at a time in a file....

readlines()
--------
-->it will read entire file and gives in a list where each line is each index in the list

with open('a.txt', 'r') as any:
    print(any.readlines(2))
any.close()

"""
import os
os.remove('aa.txt')
