"""
Activity 2 - Task 1: String Manipulation
Accepts a user's full name and displays it in uppercase and lowercase,
counts its characters, and shows the user's initials.
"""

full_name = input("Enter your full name: ").strip()

print("\n--- String Operations ---")
print("Uppercase        :", full_name.upper())
print("Lowercase        :", full_name.lower())
print("Total characters :", len(full_name))
print("Characters (no spaces):", len(full_name.replace(" ", "")))

# Initials: first letter of each word, e.g. "Juan Dela Cruz" -> "J.D.C."
words = full_name.split()
initials = ".".join(word[0].upper() for word in words) + "."
print("Initials         :", initials)
