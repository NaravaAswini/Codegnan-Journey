#matploitb:-this is a lib in py for data visualization allowing user to create a variety  places
'''grid
title
legend
'''
#bar graph
'''
import matplotlib.pyplot as plt
sales = ["A","B","C"]
values = [25,40,56]
plt.bar(sales,values,color = "red",edgecolor = "black")
plt.xlabel("car models")
plt.ylabel("values")
plt.title("BMW sales")
plt.show()
'''

#line plot graph
"""
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [10,70,30,40,50]
plt.plot(x,y)
plt.title("line plot")
plt.xlabel("x values")
plt.ylabel("y values")
plt.show()

import matplotlib.pyplot as plt
subjects=['python','java','js']
students=[35,7,15]
plt.pie(students,labels=subjects)
plt.title('students in courses')
plt.show()


import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[10,15,18,20,13]
plt.scatter(x,y)
plt.xlabel('x values')
plt.ylabel('y values')
plt.show()

import matplotlib.pyplot as plt
y=[10,23,33,12,11]
x=[1,2,3,4,5]
plt.hist(y)
plt.title('Histogram plot')
plt.xlabel('x values')
plt.ylabel('y values')
plt.show()
"""

import matplotlib.pyplot as plt

years = [2020, 2021, 2022, 2023, 2024]
sales = [50000, 65000, 80000, 95000, 120000]

plt.plot(years, sales, marker='o')
plt.title("Sales Per Year")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.grid(True)

plt.show()
