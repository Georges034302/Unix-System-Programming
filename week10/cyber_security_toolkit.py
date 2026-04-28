#!/usr/bin/env python3
import hashlib  # Used to create SHA256 hashes for text comparison.

# Encrypts text using a Caesar shift.
def encrypt(text, shift):
    result = []

    for char in text:
        if "a" <= char <= "z":
            # Wrap around alphabet using modulo arithmetic.
            result.append(chr((ord(char) - ord("a") + shift) % 26 + ord("a")))
        elif "A" <= char <= "Z":
            result.append(chr((ord(char) - ord("A") + shift) % 26 + ord("A")))
        else:
            # Keep punctuation, spaces, and numbers unchanged.
            result.append(char)

    return "".join(result)

# Decrypts Caesar-shifted text by applying the negative shift.
def decrypt(text, shift):
    # Caesar decryption is the same operation with opposite shift.
    return encrypt(text, -shift)

# Returns the SHA256 hash (hex string) of the input text.
def make_hash(text):
    # Encode text to bytes before hashing.
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

# Checks whether text matches a given SHA256 hash.
def hash_checker(text, expected_hash):
    return make_hash(text) == expected_hash

# Rates password strength using length and character variety.
def password_checker(password):
    # Check whether each character category appears at least once.
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)

    # Score is the number of categories present (0 to 4).
    score = sum([has_upper, has_lower, has_digit, has_symbol])

    if len(password) < 8 or score <= 2:
        return "weak"

    if score == 3:
        return "medium"

    return "strong"

# Shows one menu, runs one selected tool action, then exits.
def main():
    print("\n1 Encrypt")
    print("2 Decrypt")
    print("3 Hash")
    print("4 Hash Checker")
    print("5 Password Checker")
    print("6 Exit")

    choice = input("Choice: ")

    if choice == "1":
        text = input("Text: ")
        shift = int(input("Shift: "))
        print(encrypt(text, shift))

    elif choice == "2":
        text = input("Text: ")
        shift = int(input("Shift: "))
        print(decrypt(text, shift))

    elif choice == "3":
        print(make_hash(input("Text: ")))

    elif choice == "4":
        text = input("Text: ")
        expected = input("Hash: ")
        print("Match" if hash_checker(text, expected) else "No match")

    elif choice == "5":
        print(password_checker(input("Password: ")))

    elif choice == "6":
        return

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
