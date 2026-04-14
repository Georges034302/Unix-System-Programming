#!/usr/bin/env python3

text = input("Text: ")

upper_text    = text.upper()           # convert all characters to uppercase
lower_text    = text.lower()           # convert all characters to lowercase
reversed_text = text[::-1]             # reverse the string using slice [::-1]
no_spaces     = text.replace(" ", "")  # remove every space
word_count    = len(text.split())      # split into words, count them

# split() returns a list; index [0] gets the first element
first_word = text.split()[0] if text.split() else ""

print(f"Original   : {text}")
print(f"Upper      : {upper_text}")
print(f"Lower      : {lower_text}")
print(f"Reversed   : {reversed_text}")
print(f"No spaces  : {no_spaces}")
print(f"Word count : {word_count}")
print(f"First word : {first_word}")
