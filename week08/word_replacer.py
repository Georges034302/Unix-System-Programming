#!/usr/bin/env python3

import re

text   = input("Text: ")
target = input("Word to replace (or STOP): ")

total = 0

while target != "STOP":
    # \b matches word boundaries so only whole words are replaced
    # re.escape treats the target as a literal string (not a regex pattern)
    # re.subn returns the updated text and the number of replacements made
    pattern = r"\b" + re.escape(target) + r"\b"
    text, count = re.subn(pattern, "***", text, flags=re.IGNORECASE)
    total += count
    print(f"  '{target}' replaced {count} time(s)")
    target = input("Word to replace (or STOP): ")

# --- Result ---
print(f"\nUpdated text : {text}")
print(f"Total        : {total}")
