#!/usr/bin/env python3
"""
Cyber security toolkit with Caesar cipher and hash/password utilities.
Usage: python3 cyber_security_toolkit.py
"""

import hashlib

def encrypt(text, shift):
    result = []
    for char in text:
        # Rotate lowercase letters within a-z using modulo wraparound.
        if "a" <= char <= "z":
            result.append(chr((ord(char) - ord("a") + shift) % 26 + ord("a")))
        # Rotate uppercase letters within A-Z using the same shift.
        elif "A" <= char <= "Z":
            result.append(chr((ord(char) - ord("A") + shift) % 26 + ord("A")))
        else:
            # Keep digits, spaces, and symbols unchanged.
            result.append(char)
    return "".join(result)

def decrypt(text, shift):
    return encrypt(text, -shift)

def make_hash(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def hash_checker(text, expected_hash):
    return make_hash(text) == expected_hash

def password_checker(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)
    # Score counts how many character categories are present.
    score = sum((has_upper, has_lower, has_digit, has_symbol))

    if len(password) < 8 or score <= 2:
        return "weak"

    if score == 3:
        return "medium"

    return "strong"

def main():
    last_hash = None

    while True:
        print("\n1 Encrypt")
        print("2 Decrypt")
        print("3 Hash")
        print("4 Hash Checker (Use Last Hash)")
        print("5 Password Checker")
        print("6 Exit")

        choice = input("Choice: ")

        match choice:
            case "1":
                text = input("Text: ")
                shift = int(input("Shift: "))
                print(encrypt(text, shift))
            case "2":
                text = input("Text: ")
                shift = int(input("Shift: "))
                print(decrypt(text, shift))
            case "3":
                text = input("Text: ")
                last_hash = make_hash(text)
                print(last_hash)
            case "4":
                if last_hash is None:
                    print("No hash stored. Use option 3 first.")
                    continue
                text_to_check = input("Text to check: ")
                print("Match" if hash_checker(text_to_check, last_hash) else "No match")
            case "5":
                print(password_checker(input("Password: ")))
            case "6":
                # Exit only when the user explicitly chooses option 6.
                return
            case _:
                print("Invalid choice.")

if __name__ == "__main__":
    main()
