#!/usr/bin/env python3
import sys

# Counts how many times each non-space character appears in one line.
def char_frequency(line):
    counts = {}

    for char in line:
        if char == " ":
            # Treat spaces as separators, not counted characters.
            continue

        counts[char] = counts.get(char, 0) + 1

    return counts

# Finds the character with the highest frequency from a count dictionary.
def most_frequent(counts):
    best_char = None
    best_count = 0

    for char in counts:
        if counts[char] > best_count:
            best_char = char
            best_count = counts[char]

    return best_char, best_count

# Reads input lines and prints the most frequent character per line.
def main():
    for line in sys.stdin:
        line = line.rstrip("\n")
        counts = char_frequency(line)

        if not counts:
            print("No characters found.")
            continue

        char, count = most_frequent(counts)
        print(f"{repr(char)} -> {count}")

if __name__ == "__main__":
    main()
