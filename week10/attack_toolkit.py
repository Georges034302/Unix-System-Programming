#!/usr/bin/env python3
import hashlib  # Used to create SHA256 hashes for dictionary-attack comparison.

# Decrypts a Caesar-cipher text using one specific shift.
def decrypt_caesar(text, shift):
    letters = []

    for char in text:
        if "a" <= char <= "z":
            # Move lowercase letters backward by shift, wrapping around a-z.
            moved = chr((ord(char) - ord("a") - shift) % 26 + ord("a"))
        elif "A" <= char <= "Z":
            # Move uppercase letters backward by shift, wrapping around A-Z.
            moved = chr((ord(char) - ord("A") - shift) % 26 + ord("A"))
        else:
            # Keep spaces and punctuation unchanged.
            moved = char

        letters.append(moved)

    return "".join(letters)


# Prints all 26 Caesar-shift decryption attempts.
def show_all_caesar_shifts(text):
    # Try every shift from 0 to 25.
    for shift in range(26):
        print("Shift", shift, ":", decrypt_caesar(text, shift))


# Finds and returns the word whose SHA256 hash matches the target.
def find_word_by_hash(target_hash, words):
    for word in words:
        candidate = word.strip()
        current_hash = hashlib.sha256(candidate.encode("utf-8")).hexdigest()

        if current_hash == target_hash:
            return candidate

    return None


# Reads candidate words from input until '*' is entered.
def read_words_until_star():
    words = []
    print("Enter words. Type * to finish.")

    while True:
        word = input()
        if word == "*":
            return words
        words.append(word)

# Shows one menu, runs one selected action, then exits.
def main():
    print("\n1 Show Caesar shifts")
    print("2 Find word from hash")
    print("3 Exit")

    choice = input("Choice: ")

    if choice == "1":
        text = input("Cipher text: ")
        show_all_caesar_shifts(text)

    elif choice == "2":
        target_hash = input("Target hash: ")
        words = read_words_until_star()
        result = find_word_by_hash(target_hash, words)
        print("Found:" if result else "Not found", result or "")

    elif choice == "3":
        return

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
