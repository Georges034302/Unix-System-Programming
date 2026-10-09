#!/usr/bin/env python3
"""
Replace whitespace between list items with commas.

Usage:
    python3 csv_maker.py
    Enter a line of items separated by spaces.
"""

import re

items = input("Enter list items: ").strip()  # Read one line and remove outer spaces.
# \s matches whitespace, such as a space or tab.
# + means one or more, so consecutive whitespace is matched together.
pattern = r"\s+"  # Match one or more whitespace characters.
comma_separated = re.sub(pattern, ",", items)  # Replace whitespace separators with commas.

print(comma_separated)  # Display the comma-separated list.
