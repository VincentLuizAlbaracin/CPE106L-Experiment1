"""
Activity 2 - Task 3: Tuple Operations
A tuple stores fixed data that should not change - here, a list of courses.
"""

courses = ("CPE106L", "CPE107", "MATH146", "ENG101", "PE3")

print("--- Tuple Operations ---")
print("Tuple            :", courses)
print("Length of tuple  :", len(courses))
print("First element    :", courses[0])
print("Last element     :", courses[-1])
print("Slice [1:4]      :", courses[1:4])

# Tuples are immutable: trying to change an element raises an error.
try:
    courses[0] = "CPE999"
except TypeError as error:
    print("Attempt to modify:", error)
