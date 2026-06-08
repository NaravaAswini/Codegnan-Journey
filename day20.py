class Person:
    def __init__(self, name, age, edu_bg, gender, dept):
        self.name = name
        self.age = age
        self.edu_bg = edu_bg
        self.gender = gender
        self.dept = dept


class Student(Person):
    stu_count = 0

    def __init__(self, name, age, student_id, course, year,
        edu_bg, gender, dept):

        super().__init__(name, age, edu_bg, gender, dept)

        self.student_id = student_id
        self.course = course
        self.year = year

        Student.stu_count += 1

    def display(self):
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Student ID : {self.student_id}")
        print(f"Course     : {self.course}")
        print(f"Year       : {self.year}")
        print(f"Gender     : {self.gender}")
        print(f"Department : {self.dept}")
        print(f"Education  : {self.edu_bg}")


class Faculty(Person):
    fac_count = 0

    def __init__(self, name, age, faculty_id, subject,
                 edu_bg, gender, dept):

        super().__init__(name, age, edu_bg, gender, dept)

        self.faculty_id = faculty_id
        self.subject = subject

        Faculty.fac_count += 1

    def display(self):
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Faculty ID : {self.faculty_id}")

        
        print(f"Subject    : {self.subject}")
        print(f"Gender     : {self.gender}")
        print(f"Department : {self.dept}")
        print(f"Education  : {self.edu_bg}")

s1 = Student("Sahithi", 20, "S101", "CSE", 3,
             "Intermediate", "Female", "Computer Science")

f1 = Faculty("gowtham", 30, "F101", "Python",
             "M.Tech", "Male", "Computer Science")

s1.display()
print("-" * 30)
f1.display()

print("\nTotal Students:", Student.stu_count)
print("Total Faculty :", Faculty.fac_count)

    
    
