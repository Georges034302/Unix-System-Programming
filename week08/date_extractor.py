#!/usr/bin/env python3
"""
Find dates in dd/mm/yyyy format in a line of text.

Usage:
    python3 date_extractor.py
    Enter text when prompted; matching dates and their positions are printed.
"""

import re

text = input("Text: ")  # Read the text to search.

# \b matches a word boundary.
# \d matches one digit.
# {2} repeats the previous pattern exactly two times.
# {4} repeats the previous pattern exactly four times.
# / matches a literal slash.
pattern = r"\b\d{2}/\d{2}/\d{4}\b"

dates = list(re.finditer(pattern, text))    # Find each date and its position.

print(f"Dates found : {len(dates)}")        # Show how many dates were found.
for match in dates:
    print(f"  {match.group()} at position {match.start()}")  # Show the date and its starting position.
