#!/usr/bin/env python3
import hashlib

def encrypt(text, shift):
    result = []

    for char in text:
        if "a" <= char <= "z":
            result.append(chr((ord(char) - ord("a") + shift) % 26 + ord("a")))
        elif "A" <= char <= "Z":
            result.append(chr((ord(char) - ord("A") + shift) % 26 + ord("A")))
        else:
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

    score = sum([has_upper, has_lower, has_digit, has_symbol])

    if len(password) < 8 or score <= 2:
        return "weak"

    if score == 3:
        return "medium"

    return "strong"

def main():
    while True:
        print("\n1 Encrypt")
        print("2 Decrypt")
        print("3 Hash")
        print("4 Hash Checker")
        print("5 Password Checker")
        print("6 Exit")

        choice = input("Choice: ")

        match choice:
            case "1":
                print(encrypt(input("Text: "), int(input("Shift: "))))
            case "2":
                print(decrypt(input("Text: "), int(input("Shift: "))))
            case "3":
                print(make_hash(input("Text: ")))
            case "4":
                text = input("Text: ")
                expected = input("Hash: ")
                print("Match" if hash_checker(text, expected) else "No match")
            case "5":
                print(password_checker(input("Password: ")))
            case "6":
                break
            case _:
                print("Invalid choice.")

if __name__ == "__main__":
    main()
