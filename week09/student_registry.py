#!/usr/bin/env python3

"""
Register n students with:
- random 3-digit ID
- name and age

Structure:
ID -> {name, age}

Concepts:
- dictionary of dictionaries
- random unique IDs
- input validation (basic)
- clean data modelling
"""

import random as ran
import pprint as pp

n = int(input("Number of students (n): "))

# Sample n unique IDs from the range 100-999 to avoid duplicates.
ids = ran.sample(range(100, 1000), n)

# Outer dictionary keyed by student ID.
students = {}

for ID in ids:
    print(f"\nStudent ID: {ID}")

    name = input("Name: ")

    # ensure age is stored as integer
    age = int(input("Age: "))

    # Store student fields as an inner dictionary under their ID.
    students[ID] = {
        "name": name,
        "age": age
    }

# pprint formats nested structures clearly with indentation.
print("\n--- Student Database ---")
pp.pprint(students, indent=2, width=40)
