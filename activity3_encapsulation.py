"""
Activity 3 - Task 3: Encapsulation
Attributes are made private (prefixed with __) so they cannot be
changed directly from outside the class. Access goes through
getter and setter methods, which can validate the data.
"""


class Student:
    """A Student class with private attributes."""

    def __init__(self, student_id, name, course):
        self.__student_id = student_id    # private
        self.__name = name                # private
        self.__course = course            # private

    # ----- Getters -----
    def get_student_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def get_course(self):
        return self.__course

    # ----- Setters (with validation) -----
    def set_name(self, name):
        if name.strip() == "":
            print("Error: Name cannot be empty.")
        else:
            self.__name = name

    def set_course(self, course):
        if course.strip() == "":
            print("Error: Course cannot be empty.")
        else:
            self.__course = course


# --- Test encapsulation ---
student = Student("20230001", "Juan Dela Cruz", "BSCpE")

print("=== Using Getters ===")
print("Student ID:", student.get_student_id())
print("Name      :", student.get_name())
print("Course    :", student.get_course())

print("\n=== Using Setters ===")
student.set_name("Maria Santos")
print("New name  :", student.get_name())
student.set_name("")          # rejected by validation
print("Name after invalid update:", student.get_name())

print("\n=== Trying to access a private attribute directly ===")
try:
    print(student.__name)
except AttributeError as error:
    print("AttributeError:", error)
