#!/usr/bin/env python3
import sys

# Builds a dictionary mapping each token to its frequency.
# Here, a token is a full whitespace-separated string (not a substring).
def build_frequency_map(items):
    freq = {}

    for item in items:
        # Count each token occurrence.
        freq[item] = freq.get(item, 0) + 1

    return freq

# Prints token frequencies in sorted key order.
def show_frequency_map(freq):
    for key in sorted(freq):
        print(f"{key} -> {freq[key]}")

# Reads tokens from stdin, builds a frequency map, and prints results.
def main():
    tokens = []

    for line in sys.stdin:
        # split() creates full tokens by spaces/tabs/newlines.
        tokens.extend(line.split())

    show_frequency_map(build_frequency_map(tokens))

if __name__ == "__main__":
    main()
