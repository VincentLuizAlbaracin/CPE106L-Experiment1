"""
Activity 2 - Task 2: List Operations
Accepts five grades, stores them in a list, and displays the average,
highest, lowest, and the grades sorted in ascending order.
"""

grades = []
for i in range(1, 6):
    grade = float(input(f"Enter grade {i}: "))
    grades.append(grade)

average = sum(grades) / len(grades)

print("\n--- List Operations ---")
print("Grades entered   :", grades)
print(f"Average grade    : {average:.2f}")
print("Highest grade    :", max(grades))
print("Lowest grade     :", min(grades))
print("Sorted (ascending):", sorted(grades))
