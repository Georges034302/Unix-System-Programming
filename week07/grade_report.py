#!/usr/bin/env python3
"""
Assign a grade and pass/fail result to a student.

Usage:
    python3 grade_report.py
    Enter a student name and mark from 0 to 100.
"""

# Read the student name and their numeric mark
name = input("Student name: ")  # Read the student's name.
mark = int(input("Mark (0-100): "))  # Convert the entered mark to an integer.

# Cascaded if-elif-else classifies the mark into a grade band
# Conditions are tested from highest to lowest — only one branch executes
if mark >= 85:
    grade = "HD"  # Highest grade band.
    label = "High Distinction"
elif mark >= 75:
    grade = "D"
    label = "Distinction"
elif mark >= 65:
    grade = "C"
    label = "Credit"
elif mark >= 50:
    grade = "P"  # Lowest passing grade band.
    label = "Pass"
else:
    # else handles any mark below 50
    grade = "Z"
    label = "Fail"

# Derive pass/fail status directly from the grade
# Z is the only failing grade, so any other grade means the student passed
if grade == "Z":
    status = "Failed"
else:
    status = "Passed"

print(f"Student : {name}")
print(f"Mark    : {mark}")
print(f"Grade   : {grade}")
print(f"Result  : {label}")
print(f"Status  : {status}")
