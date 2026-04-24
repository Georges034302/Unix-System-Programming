#!/usr/bin/env python3
import hashlib

def brute_force_caesar(cipher_text):
    results = []

    for shift in range(26):
        candidate = []

        for char in cipher_text:
            if "a" <= char <= "z":
                candidate.append(chr((ord(char) - ord("a") - shift) % 26 + ord("a")))
            elif "A" <= char <= "Z":
                candidate.append(chr((ord(char) - ord("A") - shift) % 26 + ord("A")))
            else:
                candidate.append(char)

        results.append((shift, "".join(candidate)))

    return results

def dictionary_attack(target_hash, words):
    for word in words:
        candidate = word.strip()
        digest = hashlib.sha256(candidate.encode("utf-8")).hexdigest()

        if digest == target_hash:
            return candidate

    return None

def main():
    while True:
        print("\n1 Brute Force Caesar")
        print("2 Dictionary Attack")
        print("3 Exit")

        choice = input("Choice: ")

        match choice:
            case "1":
                text = input("Cipher text: ")

                for shift, candidate in brute_force_caesar(text):
                    print(f"{shift:2d}: {candidate}")

            case "2":
                target = input("Target hash: ")
                words = []

                print("Enter words. Use * to stop.")
                while True:
                    word = input()

                    if word == "*":
                        break

                    words.append(word)

                result = dictionary_attack(target, words)
                print("Found:" if result else "Not found", result or "")

            case "3":
                break

            case _:
                print("Invalid choice.")

if __name__ == "__main__":
    main()
