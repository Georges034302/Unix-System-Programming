#!/usr/bin/env python3

import re

text = input("Text: ")

# --- Extract ---
# \d{2}/\d{2}/\d{4} matches dates in dd/mm/yyyy format
# \b ensures we match whole tokens, not partial ones
pattern = r"\b\d{2}/\d{2}/\d{4}\b"

# --- Output ---
print(f"Dates found : {len(re.findall(pattern, text))}")

for match in re.finditer(pattern, text):  # finditer gives match objects with position info
    print(f"  {match.group()} at position {match.start()}")
