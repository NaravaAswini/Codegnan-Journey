
"""
Data Analysis
------------------
-->This is process of inspecting, cleaning, transforming, and modeling data to discover useful insights...

Types of DA
-----------------
1. Descriptive Analysis
----------------------------
Summarizing Data

2. Diagnostic Analysis
----------------------------
Understanding Causes

3. Predictive Analysis
---------------------------
Forecasting guture outcomes

4. Prescriptive Analysis
------------------------------
Suggesting actins based on data

Why DA
-------
-->To improve decision making
-->Detects trends and patterns


Numpy(Numerical python)
----------------------------
-->This python library for numerical computing. it provides support for multi-dimensional arrays, and linear algebra operaitons
making it essential for data analysis...


Using numpy in DA
------------------
--> Improved performance
--> Simplifies complex operations
--> Easy data munipulation.....


import sys
print(sys.executable)
print(sys.version)

import numpy as np
a = np.array([1, 2, 3])
b = a.copy()

b[0] = 99

print(a)  # [1 2 3]
print(b)  # [99  2  3]



import numpy as np

ar = np.array([10, 20, 30, 40])
print(ar[2])

ar1=np.array([[2,3,4],[5,4,3]])
a=ar1.reshape(3,2)
print(a)


import numpy as np
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])
C = np.dot(A, B)
print(C)



import numpy as np
arr=np.array([10,20,30])
nrm_copy=arr.view()
arr[0]=100
print(arr)
print(nrm_copy)

copy_deep=arr.copy()
arr[1]=200
print(copy_deep)
print(arr)


Pandas
-----------
-->The pandas is a powerful data manipulation and analysis library...
-->Where it provides data structure like series and dataframe for efficient data handling...

import pandas as pd
any=pd.Series([299,123,345,343,], index=['birds','animals','insects','snakes'])
print(any)


methods series
-----------------
mean()
sum()
max()
min()
apply()
map()


dataframe
-------------
"""
import pandas as pd

data = {
    'product': ['earbuds', 'smartphones', 'laptop', 'watch'],
    'brand': ['noise', 'oneplus', 'hp', 'jocker width'],
    'price': [1500, 30000, 60000, 3000],
    'stock': [20, 30, 40, 10]
}

df = pd.DataFrame(data)
print(df)
