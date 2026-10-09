#!/usr/bin/env python3
"""
Count and inspect properties of an entered sentence.

Usage:
    python3 text_stats.py
    Enter a sentence when prompted.
"""

text = input("Sentence: ")  # Read the sentence to analyze.

# --- Basic counts ---
length     = len(text)  # Count all characters.
word_count = len(text.split())  # Count whitespace-separated words.
space_count = text.count(" ")  # Count space characters.

# --- Reversal ---
reversed_text = text[::-1]  # Reverse the original sentence.

# --- Palindrome check ---
clean         = text.replace(" ", "").lower()  # remove spaces, lowercase
reversed_clean = clean[::-1]                   # reverse the cleaned text
is_palindrome  = clean == reversed_clean       # same forwards and backwards?

# --- Content check ---
letters_only = text.replace(" ", "").isalpha()  # Check that only letters and spaces are present.

# --- Output ---
print(f"Length       : {length}")
print(f"Words        : {word_count}")
print(f"Spaces       : {space_count}")
print(f"Reversed     : {reversed_text}")
print(f"Palindrome   : {'Yes' if is_palindrome else 'No'}")
print(f"Letters only : {'Yes' if letters_only else 'No'}")
