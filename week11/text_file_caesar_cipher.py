#!/usr/bin/env python3
"""
Encrypt text file content with a Caesar cipher.

Usage:
1. Run: python3 text_file_caesar_cipher.py
2. Enter input text filename and shift value.
3. The script saves encrypted.txt.
"""

ENCRYPTED_OUTPUT = "encrypted.txt"

# Shifts one character by the selected amount.
def shift_character(char, shift):
    if char.islower():
        start = ord("a")
        return chr((ord(char) - start + shift) % 26 + start)

    if char.isupper():
        start = ord("A")
        return chr((ord(char) - start + shift) % 26 + start)

    # Keep digits, spaces, and punctuation unchanged.
    return char

# Applies Caesar shift to a full text string.
def transform_text(text, shift):
    # Mod 26 keeps the shift inside the alphabet range.
    shift = shift % 26
    result = []

    for char in text:
        result.append(shift_character(char, shift))

    return "".join(result)

# Reads text from a file.
def read_text(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()

# Writes text to a file.
def write_text(filename, text):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)

# Reads a valid integer shift from user input.
def read_shift_value():
    while True:
        raw_value = input("Shift value (example: 3): ").strip()
        try:
            return int(raw_value)
        except ValueError:
            print("Please enter a valid integer shift (example: 3).")

# Runs the script.
def main():
    input_file = input("Input text filename: ").strip()
    shift = read_shift_value()

    original_text = read_text(input_file)
    encrypted_text = transform_text(original_text, shift)

    write_text(ENCRYPTED_OUTPUT, encrypted_text)

    print(f"Saved encrypted text to {ENCRYPTED_OUTPUT}")

if __name__ == "__main__":
    main()
