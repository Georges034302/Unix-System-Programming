#!/usr/bin/env python3
"""
Encrypt a user-selected file with a Caesar key.
Usage:
    python3 caesar_file_encryptor.py
    Choose k to enter the key.
    Choose r to enter the input filename.
    Choose e, then enter the output filename to save the encrypted file.
    Choose x to exit.
    Choose k and r before e.
"""

# Shift one English letter, leaving nonletters unchanged.
def shift_character(char, key):
    if "a" <= char <= "z":
        return chr((ord(char) - ord("a") + key) % 26 + ord("a"))
    if "A" <= char <= "Z":
        return chr((ord(char) - ord("A") + key) % 26 + ord("A"))
    return char


# Encrypt text by shifting each character with the Caesar key.
def encrypt_text(text, key):
    encrypted_characters = []
    for char in text:
        encrypted_characters.append(shift_character(char, key))
    return "".join(encrypted_characters)


# Read and return all text from the named input file.
def read_input_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


# Write encrypted text to the named output file.
def write_output_file(filename, text):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)


# Prompt for and return the user's integer Caesar key.
def get_key():
    return int(input("Enter Caesar key: "))


# Show the menu and run the selected key and file encryption actions.
def main():
    key = None
    input_text = None

    while True:
        print("\nk - read key")
        print("r - read input file")
        print("e - encrypt file")
        print("x - exit")
        option = input("Option: ").strip().lower()

        match option:
            case "k":
                key = get_key()
            case "r":
                input_filename = input("Input filename: ").strip()
                input_text = read_input_file(input_filename)
                print(f"Read input from {input_filename}")
            case "e":
                output_filename = input("Output filename: ").strip()
                encrypted_text = encrypt_text(input_text, key)
                write_output_file(output_filename, encrypted_text)
                print(f"Encrypted text saved to {output_filename}")
            case "x":
                return
            case _:
                print("Invalid option.")

if __name__ == "__main__":
    main()
