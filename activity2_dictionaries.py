"""
Activity 2 - Task 4: Dictionary Operations
Stores student information and demonstrates adding, updating,
retrieving, and deleting key-value pairs.
"""

student = {
    "StudentID": "20230001",
    "Name": "Juan Dela Cruz",
    "Course": "BSCpE"
}
print("Original dictionary :", student)

# 1. Add a new key-value pair
student["YearLevel"] = 3
print("After adding        :", student)

# 2. Update existing data
student["Course"] = "BS Computer Engineering"
print("After updating      :", student)

# 3. Retrieve information
print("Retrieve Name       :", student["Name"])
print("Retrieve with get() :", student.get("Email", "No email on record"))

# 4. Delete an item
removed = student.pop("YearLevel")
print("Deleted YearLevel   :", removed)
print("Final dictionary    :", student)

print("\nAll records:")
for key, value in student.items():
    print(f"  {key}: {value}")
