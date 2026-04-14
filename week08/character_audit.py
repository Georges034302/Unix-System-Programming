#!/usr/bin/env python3

text = input("Text: ")

# --- Count ---
letters = digits = spaces = punctuation = uppercase = lowercase = 0

for ch in text:
    if ch.isalpha():               letters    += 1  # a-z or A-Z
    if ch.isdigit():               digits     += 1  # 0-9
    if ch == " ":                  spaces     += 1  # space character
    if not ch.isalnum() and ch != " ": punctuation += 1  # not letter, digit, or space
    if ch.isupper():               uppercase  += 1  # A-Z
    if ch.islower():               lowercase  += 1  # a-z

# --- Output ---
print(f"Letters     : {letters}")
print(f"Digits      : {digits}")
print(f"Spaces      : {spaces}")
print(f"Punctuation : {punctuation}")
print(f"Uppercase   : {uppercase}")
print(f"Lowercase   : {lowercase}")
