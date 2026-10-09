#!/usr/bin/env python3
"""
Extract and report digit sequences from a line of text.

Usage:
    python3 extract_numbers.py
    Enter text when prompted; all numbers, their count, and the first are printed.
"""

import re

text = input("Log text: ")

# --- Extract ---
numbers = re.findall(r"\d+", text)  # \d+ matches one or more consecutive digits

# --- Output ---
print(f"All numbers : {numbers}")
print(f"Count       : {len(numbers)}")
print(f"First       : {numbers[0] if numbers else '[none]'}")
