#!/usr/bin/env python3
"""
Replace chosen whole words in a sentence.

Usage:
    python3 word_replacer.py
    Enter the sentence, then enter words to replace one at a time.
    Enter STOP when prompted for a word to finish.
"""

import re

text   = input("Text: ")  # Read the sentence to edit.
target = input("Word to replace (or STOP): ")  # Read a word, or STOP to finish.

total = 0  # Count replacements across all entered words.

while target != "STOP":
    # \b requires the match to start and end at a word boundary.
    # re.escape makes the entered word literal, even if it contains regex symbols.
    pattern = r"\b" + re.escape(target) + r"\b"
    text, count = re.subn(pattern, "***", text, flags=re.IGNORECASE)  # Replace whole-word matches, ignoring case.
    total += count  # Add this word's replacements to the running total.
    print(f"  '{target}' replaced {count} time(s)")  # Report replacements for this word.
    target = input("Word to replace (or STOP): ")  # Ask for another word or stop.

print(f"\nUpdated text : {text}")  # Show the edited sentence.
print(f"Total        : {total}")  # Show the total replacements made.
