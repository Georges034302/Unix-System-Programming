#!/usr/bin/env python3
"""
Show the most frequent non-space character for each input line.
Usage: cat input.txt | python3 character_frequency_per_line.py
"""

import sys

def char_frequency(line):
    counts = {}
    for char in line:
        if char == " ":
            continue
        counts[char] = counts.get(char, 0) + 1
    return counts

def most_frequent(counts):
    return max(counts.items(), key=lambda item: item[1])

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
