#!/usr/bin/env python3
"""
Analyze a password for length, character classes, and strength.

Usage:
    python3 password_analyzer.py
    Enter a password when prompted.
    A password is checked for at least 8 characters, an uppercase letter,
    a lowercase letter, a digit, and a special character.
"""

import re

password = input("Password: ")  # Read the password to check.

length_ok = len(password) >= 8  # Check for at least 8 characters.
has_upper = re.search(r"[A-Z]", password)  # Check for an uppercase letter.
has_lower = re.search(r"[a-z]", password)  # Check for a lowercase letter.
has_digit = re.search(r"\d", password)  # Check for a digit.
has_special = re.search(r"[^A-Za-z0-9]", password)  # Check for a special character.

score = 0  # Count how many password rules are satisfied.
if length_ok:
    score += 1  # Add a point for meeting the length rule.
if has_upper:
    score += 1  # Add a point for having an uppercase letter.
if has_lower:
    score += 1  # Add a point for having a lowercase letter.
if has_digit:
    score += 1  # Add a point for having a digit.
if has_special:
    score += 1  # Add a point for having a special character.

if score == 5:
    strength = "Strong"  # All five rules are satisfied.
elif score >= 3:
    strength = "Medium"  # Three or four rules are satisfied.
else:
    strength = "Weak"  # Fewer than three rules are satisfied.

print(f"Strength : {strength}")  # Display the strength rating.
print(f"Score    : {score}/5")  # Display how many rules passed.
