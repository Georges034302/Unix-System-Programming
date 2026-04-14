#!/usr/bin/env python3

import re

text = input("Sentence: ")

# --- Detect repeated consecutive words ---
# (\w+) captures a word, \s+ matches spaces, \1 matches the same word again
pattern = r"\b(\w+)\s+\1\b"
matches = re.findall(pattern, text, flags=re.IGNORECASE)  # findall returns all captured groups

# --- Output ---
if matches:
    print(f"Repeated words: {len(matches)}")
    for word in matches:
        print(f"  - {word}")
else:
    print("No repeated words found")
