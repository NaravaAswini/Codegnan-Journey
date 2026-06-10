class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    stu_count = 0

    def __init__(self, name, age, edu_bg, gender,
                 dept, student_id, year):

        super().__init__(name, age)

        self.edu_bg = edu_bg
        self.gender = gender
        self.dept = dept
        self.student_id = student_id
        self.year = year

        Student.stu_count += 1

    def display(self):
        print("\n----- STUDENT DETAILS -----")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Education Background:", self.edu_bg)
        print("Gender:", self.gender)
        print("Department:", self.dept)
        print("Student ID:", self.student_id)
00000000000
+print("Year:", self.year)


class Faculty(Person):
    fac_count = 0

    def __init__(self, name, age, experience, department):

        super().__init__(name, age)

        self.experience = experience
        self.department = department

        Faculty.fac_count += 1

    def display(self):
        print("\n----- FACULTY DETAILS -----")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Experience:", self.experience, "Years")
        print("Department:", self.department)


class Watchman(Person):
    watch_count = 0

    def __init__(self, name, age, shift):

        super().__init__(name, age)

        self.shift = shift

        Watchman.watch_count += 1

    def display(self):
        print("\n----- WATCHMAN DETAILS -----")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Shift:", self.shift)


class CleaningStaff(Person):
    clean_count = 0

    def __init__(self, name, age, area_assigned):

        super().__init__(name, age)

        self.area_assigned = area_assigned

        CleaningStaff.clean_count += 1

    def display(self):
        print("\n----- CLEANING STAFF DETAILS -----")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Assigned Area:", self.area_assigned)


class BusDriver(Person):
    driver_count = 0

    def __init__(self, name, age, bus_no):

        super().__init__(name, age)

        self.bus_no = bus_no

        BusDriver.driver_count += 1

    def display(self):
        print("\n----- BUS DRIVER DETAILS -----")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Bus Number:", self.bus_no)


s1 = Student(
    "Sahithi",
    20,
    "Intermediate",
    "Female",
    "CSE",
    "S101",
    3
)

f1 = Faculty(
    "Gowtham",
    35,
    10,
    "Computer Science"
)


w1 = Watchman(
    "Raju",
    45,
    "Morning Shift"
)

w2 = Watchman(
    "Kumar",
    50,
    "Night Shift"
)


c1 = CleaningStaff(
    "Lakshmi",
    40,
    "Block A"
)

c2 = CleaningStaff(
    "Sita",
    35,
    "Block B"
)

c3 = CleaningStaff(
    "Anitha",
    38,
    "Library"
)

c4 = CleaningStaff(
    "Radha",
    42,
    "Canteen"
)


b1 = BusDriver(
    "Ramesh",
    38,
    "AP39AB1234"
)


b2 = BusDriver(
    "Mahesh",
    41,
    "AP39EF9012"
)



s1.display()

f1.display()

w1.display()
w2.display()

c1.display()
c2.display()
c3.display()
c4.display()

b1.display()
b2.display()


print("\n========== UNIVERSITY SUMMARY ==========")
print("Total Students       :", Student.stu_count)
print("Total Faculty        :", Faculty.fac_count)
print("Total Watchmen       :", Watchman.watch_count)
print("Total Cleaning Staff :", CleaningStaff.clean_count)
print("Total Bus Drivers    :", BusDriver.driver_count)
