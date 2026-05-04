#!/usr/bin/env python3
"""
Register students from stdin, generate marks and Australian grades,
save to JSON, then read and display the content.

Usage:
1. Run: python3 student_profile_pretty_print.py
2. Enter output JSON filename (or press Enter for students.json).
3. Enter number of students and student names.
4. Script generates random marks, maps grades (HD/D/C/P/Z), saves JSON, and prints profiles.
"""
import json
import random
from pprint import pprint

PROFILE_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
DIGITS = "0123456789"

# Generates a unique random code from a character set.
def generate_unique_code(existing_values, alphabet, size=6):
    while True:
        code = "".join(random.choice(alphabet) for _ in range(size))
        if code not in existing_values:
            return code

# Maps exam marks to letter grades.
def mark_to_grade(mark):
    # Australian style grades: HD, D, C, P, Z.
    if mark >= 85:
        return "HD"
    if mark >= 75:
        return "D"
    if mark >= 65:
        return "C"
    if mark >= 50:
        return "P"
    return "Z"

# Creates one student profile dictionary.
def build_student_profile(name, student_id):
    # Generate mark during registration so JSON is complete in one save.
    exam_mark = random.randint(1, 100)
    return {
        "name": name,
        "student_id": student_id,
        "exam_mark": exam_mark,
        "grade": mark_to_grade(exam_mark),
    }

# Collects n student names and builds a dictionary of dictionaries.
def register_students(count):
    students = {}
    existing_ids = set()

    for index in range(1, count + 1):
        name = input(f"Student {index} name: ").strip()
        profile_key = generate_unique_code(students.keys(), PROFILE_ALPHABET, 6)
        student_id = generate_unique_code(existing_ids, DIGITS, 6)
        existing_ids.add(student_id)
        students[profile_key] = build_student_profile(name, student_id)

    return students

# Saves student dictionary data to JSON.
def save_students(filename, students):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=2)

# Loads student dictionary data from JSON.
def load_students(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

# Reads a positive integer from user input.
def read_positive_count(prompt):
    while True:
        raw_value = input(prompt).strip()
        if raw_value.isdigit() and int(raw_value) > 0:
            return int(raw_value)
        print("Please enter a positive integer (example: 3).")

# Runs the script.
def main():
    filename = input("Output JSON filename [students.json]: ").strip()
    if not filename:
        filename = "students.json"

    count = read_positive_count("How many students to register? ")

    students = register_students(count)
    save_students(filename, students)

    # Read from JSON so output proves data was saved correctly.
    loaded_students = load_students(filename)
    print("\nStudent Profiles (Marks + Grades)")
    # Default pprint formatting is enough for clean output.
    pprint(loaded_students)
    print(f"Saved data to {filename}")

if __name__ == "__main__":
    main()
