#!/usr/bin/env python3
"""
Find repeated consecutive words in a sentence.

Usage:
    python3 repeated_word.py
    Enter a sentence when prompted; the script reports repeated words.
"""

import re

text = input("Sentence: ")  # Read the sentence to check.

# r keeps backslashes for the regex engine.
# \b matches a word boundary.
# (\w+) captures one or more word characters as group 1.
# \s+ matches one or more whitespace characters between the words.
# \1 matches the same word captured in group 1.
pattern = r"\b(\w+)\s+\1\b"
matches = re.findall(pattern, text, flags=re.IGNORECASE)  # Find repeated words, ignoring letter case.

if matches:
    print(f"Repeated words: {len(matches)}")  # Show how many repetitions were found.
    for word in matches:
        print(f"  - {word}")  # Show each repeated word.
else:
    print("No repeated words found")  # Report when there are no matches.
