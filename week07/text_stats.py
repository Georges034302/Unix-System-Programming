#!/usr/bin/env python3

text = input("Sentence: ")

# --- Basic counts ---
length     = len(text)
word_count = len(text.split())
space_count = text.count(" ")

# --- Reversal ---
reversed_text = text[::-1]

# --- Palindrome check ---
clean         = text.replace(" ", "").lower()  # remove spaces, lowercase
reversed_clean = clean[::-1]                   # reverse the cleaned text
is_palindrome  = clean == reversed_clean       # same forwards and backwards?

# --- Content check ---
letters_only = text.replace(" ", "").isalpha()  # True if no digits or symbols

# --- Output ---
print(f"Length       : {length}")
print(f"Words        : {word_count}")
print(f"Spaces       : {space_count}")
print(f"Reversed     : {reversed_text}")
print(f"Palindrome   : {'Yes' if is_palindrome else 'No'}")
print(f"Letters only : {'Yes' if letters_only else 'No'}")
