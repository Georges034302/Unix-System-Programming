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

# generate unique 3-digit IDs
ids = ran.sample(range(100, 1000), n)

students = {}

for ID in ids:
    print(f"\nStudent ID: {ID}")

    name = input("Name: ")

    # ensure age is stored as integer
    age = int(input("Age: "))

    # directly assign dictionary (cleaner)
    students[ID] = {
        "name": name,
        "age": age
    }

# print formatted output
print("\n--- Student Database ---")
pp.pprint(students, indent=2, width=40)
