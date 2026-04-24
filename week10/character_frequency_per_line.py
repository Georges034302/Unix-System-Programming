#!/usr/bin/env python3
import sys

def char_frequency(line):
    counts = {}

    for char in line:
        if char == " ":
            continue

        counts[char] = counts.get(char, 0) + 1

    return counts

def most_frequent(counts):
    best_char = None
    best_count = 0

    for char in counts:
        if counts[char] > best_count:
            best_char = char
            best_count = counts[char]

    return best_char, best_count

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
