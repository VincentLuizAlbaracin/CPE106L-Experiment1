"""
Activity 3 - Task 4: Inheritance and Polymorphism

Hierarchy:
    Person
    ├── Student
    └── Instructor

Student and Instructor inherit the name and contact attributes and
methods from Person. Each one overrides display_info() and role(),
so the same method call behaves differently depending on the object
(polymorphism).
"""


class Person:
    """Base (parent) class for all people in the system."""

    def __init__(self, name, email):
        self._name = name
        self._email = email

    def get_name(self):
        return self._name

    def get_email(self):
        return self._email

    def role(self):
        return "Person"

    def display_info(self):
        print(f"Name  : {self._name}")
        print(f"Email : {self._email}")


class Student(Person):
    """Student inherits from Person and adds an ID, course, and grades."""

    def __init__(self, name, email, student_id, course):
        super().__init__(name, email)     # reuse Person's constructor
        self._student_id = student_id
        self._course = course
        self._grades = []

    def add_grade(self, grade):
        self._grades.append(grade)

    def get_average(self):
        if not self._grades:
            return 0
        return sum(self._grades) / len(self._grades)

    def role(self):                       # overrides Person.role()
        return "Student"

    def display_info(self):               # overrides Person.display_info()
        super().display_info()            # reuse the parent's output
        print(f"Student ID : {self._student_id}")
        print(f"Course     : {self._course}")
        print(f"Average    : {self.get_average():.2f}")


class Instructor(Person):
    """Instructor inherits from Person and adds an employee ID and department."""

    def __init__(self, name, email, employee_id, department):
        super().__init__(name, email)
        self._employee_id = employee_id
        self._department = department

    def role(self):
        return "Instructor"

    def display_info(self):
        super().display_info()
        print(f"Employee ID : {self._employee_id}")
        print(f"Department  : {self._department}")


# --- Inheritance demo ---
print("=== Inheritance ===")
student = Student("Juan Dela Cruz", "juan@mymail.mapua.edu.ph", "20230001", "BSCpE")
student.add_grade(90)
student.add_grade(85)
student.add_grade(88)

instructor = Instructor("Engr. Ana Reyes", "areyes@mapua.edu.ph", "EMP-1024", "Computer Engineering")

# get_name() is defined only in Person, but Student and Instructor can use it.
print("Student name (inherited method)   :", student.get_name())
print("Instructor name (inherited method):", instructor.get_name())
print("Is Student a Person?   ", isinstance(student, Person))
print("Is Instructor a Person?", isinstance(instructor, Person))

# --- Polymorphism demo ---
print("\n=== Polymorphism ===")
people = [Person("Pedro Penduko", "pedro@example.com"), student, instructor]

for person in people:
    print(f"\n[{person.role()}]")
    person.display_info()        # same call, different behavior per class
