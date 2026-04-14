#!/usr/bin/env python3

import re

password = input("Password: ")

# --- Check each property ---
# re.search returns a match object on success, or None on failure
length_ok   = len(password) >= 8
has_upper   = re.search(r"[A-Z]", password) is not None       # at least one uppercase
has_lower   = re.search(r"[a-z]", password) is not None       # at least one lowercase
has_digit   = re.search(r"\d", password) is not None          # at least one digit
has_special = re.search(r"[^A-Za-z0-9]", password) is not None  # at least one special char

# --- Score ---
# each True adds 1 (True == 1 in Python)
score = length_ok + has_upper + has_lower + has_digit + has_special

if score == 5:    strength = "Strong"
elif score >= 3:  strength = "Medium"
else:             strength = "Weak"

# --- Output ---
print(f"Strength : {strength}")
print(f"Score    : {score}/5")

if not length_ok:   print("Issue: at least 8 characters required")
if not has_upper:   print("Issue: add an uppercase letter")
if not has_lower:   print("Issue: add a lowercase letter")
if not has_digit:   print("Issue: add a digit")
if not has_special: print("Issue: add a special character")
