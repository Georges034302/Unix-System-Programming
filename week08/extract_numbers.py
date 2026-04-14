#!/usr/bin/env python3

import re

text = input("Log text: ")

# --- Extract ---
numbers = re.findall(r"\d+", text)  # \d+ matches one or more consecutive digits

# --- Output ---
print(f"All numbers : {numbers}")
print(f"Count       : {len(numbers)}")
print(f"First       : {numbers[0] if numbers else '[none]'}")
