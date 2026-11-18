"""
Activity 3 - Task 2: Student Class
A Student class with an ID, name, and course, plus methods
to display information and update records.
"""


class Student:
    """Represents a student with an ID, name, and course."""

    def __init__(self, student_id, name, course):
        """Constructor: runs automatically when a Student object is created."""
        self.student_id = student_id
        self.name = name
        self.course = course

    def display_info(self):
        """Displays the student's information."""
        print(f"Student ID : {self.student_id}")
        print(f"Name       : {self.name}")
        print(f"Course     : {self.course}")

    def update_record(self, name=None, course=None):
        """Updates the student's name and/or course."""
        if name:
            self.name = name
        if course:
            self.course = course
        print("Record updated.")


# --- Test the class ---
student1 = Student("20230001", "Juan Dela Cruz", "BSCpE")

print("=== Original Record ===")
student1.display_info()

print("\n=== Updating Record ===")
student1.update_record(course="BS Computer Engineering")
student1.display_info()
