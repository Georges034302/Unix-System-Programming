#!/usr/bin/env python3
"""
Store marks in a nested list and calculate row totals.
Demonstrates: nested lists, nested indexing, nested iteration.
"""

# Each inner list holds one student's marks for multiple subjects.
marks = [
    [70, 80, 75],
    [90, 95, 88],
    [60, 72, 68],
]

# Print each row as-is to show the raw nested structure.
print("Student mark rows:")
for row in marks:
    print(" ", row)

# Use index-based iteration to show student number alongside total.
print("\nRow totals:")
for index in range(len(marks)):
    total = 0
    # Sum all marks in this student's row.
    for mark in marks[index]:
        total += mark
    print(f"  Student {index + 1}: total = {total}")
