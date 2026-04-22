#!/usr/bin/env python3
"""
Store marks in a nested list and calculate row totals.
Demonstrates: nested lists, nested indexing, nested iteration.
"""

marks = [
    [70, 80, 75],
    [90, 95, 88],
    [60, 72, 68],
]

print("Student mark rows:")
for row in marks:
    print(" ", row)

print("\nRow totals:")
for index in range(len(marks)):
    total = 0
    for mark in marks[index]:
        total += mark
    print(f"  Student {index + 1}: total = {total}")
