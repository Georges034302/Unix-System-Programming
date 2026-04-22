#!/usr/bin/env python3
"""
Model student records using a list of dictionaries containing mark lists.
Demonstrates: multi-level data model, nested access, aggregation.
"""

students = [
    {"name": "Tom", "marks": [70, 80, 75]},
    {"name": "Ann", "marks": [90, 95, 88]},
    {"name": "John", "marks": [60, 72, 68]},
]

print("Student averages:")
for student in students:
    total = 0
    for mark in student["marks"]:
        total += mark
    average = total / len(student["marks"])
    print(f"  {student['name']:5} -> average: {average:.2f}")
