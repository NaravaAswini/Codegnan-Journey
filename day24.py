#regular expression or (RegEx)
'''
RegEX is a sequence of characters that form a searching pattern
this can be used to check the string contains a specified search pattern
python has a built in package called "re" which can be used to work with RegEX
'''

#functions in re
'''
Findall
Search()
fullmatch
'''

'''text = "Python is a high-level programming language renowned for its clean, highly readable syntax"
import re
print(re.findall("a", text))
'''

#Meta Charc
'''
[] - a-z,A-Z,0-9 and any specified squence...
. (dot) - here each dot is one char
^ -->This look for the , string is starting with specified squence of not....
$ -->This look for the, string is ending iwth specified squence or not.
* --> Zero or more
? --> Zero or one
+ --> one or more


'''
#[]
#alphabets
'''
import re
text = "Python is a high-level programming23 language98 renowned fo8r its clean, highly readable syntax"
print(re.findall("[a-zA-Z]", text))
'''

#numbers
'''
import re
text = "Python is a high-level programming23 language98 renowned fo8r its clean, highly readable syntax"
print(re.findall("[0-9]", text))
'''

#it find single letters of a l s
'''
import re
text = "Python is a high-level programming23 language98 renowned fo8r its clean, highly readable syntax"
print(re.findall("[als]", text))
'''

# Dot(.):
import re
text = "Python is a high-level programming23 language98 renowned fo8r its clean, highly readable syntax"
print(re.findall("re......", text))

import re
text = "Python is a high-level programming23 language98 renowned fo8r its clean, highly readable syntax"
print(re.findall('p.*i', text))
print(re.findall('\S', text))

"""
Specia sequence
-------------------
\s-->no space
\S-->only space
\D-->
"""

# Dot(.):
'''
import re
text = "Python is a high-level programming23 language98 renowned fo8r its clean, highly readable syntax"
print(re.findall("re......", text))
'''

#Cap(^):
'''
import re
text = "Python is a high-level programming23 language98 renowned fo8r its clean, highly readable syntax"
print(re.findall("^Python is", text))
print(re.findall("^is", text))
'''

#dollar($)
'''
import re
text = "Python is a high-level programming23 language98 renowned fo8r its clean, highly readable syntax"
print(re.findall("syntax$", text))
print(re.findall("is$", text))
'''

#star*
'''
import re
text = "Python is a high-level programming23 language98 renowned fo8r its clean, highly readable syntax"
print(re.findall("P.*ython", text))
print(re.findall("P.*e", text))
'''

#?
'''import re
text = "Python is a high-level programming23 language98 renowned fo8r its clean, highly readable syntax"
print(re.findall("P.?ython", text))'''

#+
'''import re
text = "Python is a high-level programming23 language98 renowned fo8r its clean, highly readable syntax"
print(re.findall("P.+ython", text))'''

#{}
'''
import re
text = "Python is a high-level programming23 language98 renowned fo8r its clean, highly readable syntax"
print(re.findall("P.{10}", text))
'''

#/S and /s
'''
import re
text = "Python is a high-level programming23 language98 renowned fo8r its clean, highly readable syntax"
print(re.findall("\S", text))
print(re.findall("\s", text))'''

#/D and /d
'''
import re
text = "Python is a high-level programming23 language98 renowned fo8r its clean, highly readable syntax"
print(re.findall("\D", text))
print(re.findall("\d", text))'''

#/W and /w
'''import re
text = "Python is a high-level programming23 language98 renowned fo8r its clean, highly readable syntax"
print(re.findall("\W", text))
print(re.findall("\w", text))'''


import re

m = input("Enter number: ")

how = re.fullmatch('[6-9][0-9]{9}', m)

if how:
    print(f"{m} is a valid Indian mobile number")
else:
    print(f"{m} is not a valid Indian mobile number")

