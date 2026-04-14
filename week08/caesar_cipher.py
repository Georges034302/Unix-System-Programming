#!/usr/bin/env python3

text  = input("Text : ")          # original message to encrypt
shift = int(input("Shift: ")) % 26  # how many letters to shift; % 26 keeps it in 0-25

result = ""  # build the encrypted string one character at a time

for ch in text:                    # process each character in the input
    if ch.isupper():               # uppercase letter: work within A-Z
        result += chr((ord(ch) - ord("A") + shift) % 26 + ord("A"))
        # ord(ch) - ord("A")  -> 0-25 position in alphabet (e.g. "C" -> 2)
        # + shift              -> apply the shift
        # % 26                 -> wrap around if it goes past Z
        # + ord("A")           -> convert back to ASCII code
        # chr(...)             -> convert ASCII code to character
    elif ch.islower():             # lowercase letter: same logic within a-z
        result += chr((ord(ch) - ord("a") + shift) % 26 + ord("a"))
    else:
        result += ch               # spaces, digits, punctuation pass through unchanged

print(f"Result: {result}")         # display the encrypted text
