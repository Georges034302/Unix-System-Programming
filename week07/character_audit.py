#!/usr/bin/env python3
"""
Count character categories in a line of text.

Usage:
    python3 character_audit.py
    Enter text when prompted; the script prints its character counts.
"""

text = input("Text: ")  # Read the line whose characters will be counted.

# --- Count ---
letters = digits = spaces = punctuation = uppercase = lowercase = 0

for ch in text:
    if ch.isalpha():               letters    += 1  # Count letters.
    if ch.isdigit():               digits     += 1  # Count digits.
    if ch == " ":                  spaces     += 1  # Count space characters.
    if not ch.isalnum() and ch != " ": punctuation += 1  # Count non-letter, non-digit characters except spaces.
    if ch.isupper():               uppercase  += 1  # Count uppercase letters.
    if ch.islower():               lowercase  += 1  # Count lowercase letters.

# --- Output ---
print(f"Letters     : {letters}")
print(f"Digits      : {digits}")
print(f"Spaces      : {spaces}")
print(f"Punctuation : {punctuation}")
print(f"Uppercase   : {uppercase}")
print(f"Lowercase   : {lowercase}")
