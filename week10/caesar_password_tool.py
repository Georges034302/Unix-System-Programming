#!/usr/bin/env python3
"""
Create a short Caesar-encrypted password challenge and brute-force it.
Usage:
1. Run: python3 caesar_password_tool.py
2. Choose option 1 to generate a short encrypted password and save the original in secrets.txt.
3. Choose option 2 to list all possible Caesar decryptions and compare them with secrets.txt.
"""

import random
import string

MIN_PASSWORD_LENGTH = 3
MAX_PASSWORD_LENGTH = 6
MAX_SHIFT = 25
SECRETS_FILE = "secrets.txt"


# Shift one letter by the given Caesar key.
def shift_character(char, shift):
    if "a" <= char <= "z":
        # Wrap lowercase letters back into the a-z range.
        return chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
    if "A" <= char <= "Z":
        # Wrap uppercase letters back into the A-Z range.
        return chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
    return char


# Apply one Caesar shift to every character in the text.
def transform_caesar(text, shift):
    return "".join(shift_character(char, shift) for char in text)


# Encrypt text with the selected Caesar key.
def encrypt_caesar(text, shift):
    return transform_caesar(text, shift)


# Decrypt text by applying the opposite Caesar key.
def decrypt_caesar(text, shift):
    return transform_caesar(text, -shift)


# Generate a letters-only password for the demo.
def generate_password(length):
    alphabet = string.ascii_letters
    return "".join(random.choice(alphabet) for _ in range(length))


# Generate a private key between 0 and 25.
def generate_private_key():
    return random.randint(0, MAX_SHIFT)


# Save the current original password so the user can verify decryption.
def save_secret(password):
    with open(SECRETS_FILE, "w", encoding="utf-8") as file:
        file.write(password + "\n")


# Print every possible decryption when the key is unknown.
def show_all_caesar_shifts(text, expected_password=None):
    # Caesar cipher has only 26 possible keys, so brute force is simple here.
    for shift in range(26):
        decrypted_text = decrypt_caesar(text, shift)
        match_label = ""
        if expected_password == decrypted_text:
            match_label = "  <== match"
        print(f"Shift {shift:02d}: {decrypted_text}{match_label}")


# Create one encrypted password challenge.
def handle_generate_password():
    # Keep the password short so the output stays easy to read.
    password_length = random.randint(MIN_PASSWORD_LENGTH, MAX_PASSWORD_LENGTH)
    private_key = generate_private_key()
    password = generate_password(password_length)
    encrypted_password = encrypt_caesar(password, private_key)
    save_secret(password)

    print("Encrypted password:", encrypted_password)
    print("Password length   :", password_length)
    print("Private key       : hidden")
    print(f"Original password saved to {SECRETS_FILE}")
    print("Use option 2 to brute-force the password.")
    return password, encrypted_password


# Read an encrypted password and show all brute-force attempts.
def handle_decipher_password(expected_password=None, expected_encrypted_password=None):
    if expected_encrypted_password:
        prompt = "Encrypted password (press Enter to use current challenge): "
    else:
        prompt = "Encrypted password: "

    encrypted_password = input(prompt).strip()
    if not encrypted_password:
        if expected_encrypted_password:
            encrypted_password = expected_encrypted_password
            print("Using current challenge:", encrypted_password)
        else:
            print("Please enter an encrypted password.")
            return

    # The user does not know the key, so the script tries all possible shifts.
    print("Trying all possible private keys:")
    if encrypted_password == expected_encrypted_password:
        show_all_caesar_shifts(encrypted_password, expected_password)
    else:
        show_all_caesar_shifts(encrypted_password)


# Show the menu and run the selected option.
def main():
    current_password = None
    current_encrypted_password = None

    while True:
        print("\n1 Generate encrypted password")
        print("2 Brute-force decrypt password")
        print("3 Exit")

        choice = input("Choice: ").strip()

        match choice:
            case "1":
                current_password, current_encrypted_password = handle_generate_password()
            case "2":
                handle_decipher_password(current_password, current_encrypted_password)
            case "3":
                return
            case _:
                print("Invalid choice.")

if __name__ == "__main__":
    main()
