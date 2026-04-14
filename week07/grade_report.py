#!/usr/bin/env python3

# Read the student name and their numeric mark
name = input("Student name: ")
mark = int(input("Mark (0-100): "))  # convert string input to integer

# Cascaded if-elif-else classifies the mark into a grade band
# Conditions are tested from highest to lowest — only one branch executes
if mark >= 85:
    grade = "HD"
    label = "High Distinction"
elif mark >= 75:
    grade = "D"
    label = "Distinction"
elif mark >= 65:
    grade = "C"
    label = "Credit"
elif mark >= 50:
    grade = "P"
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
