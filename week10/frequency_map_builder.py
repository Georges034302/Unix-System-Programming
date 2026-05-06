#!/usr/bin/env python3
"""
Build and print token frequency maps from standard input.
Usage: cat input.txt | python3 frequency_map_builder.py
"""

import sys

def build_frequency_map(items):
    freq = {}
    for item in items:
        # Increment count for each token, starting at 0 when first seen.
        freq[item] = freq.get(item, 0) + 1
    return freq

def show_frequency_map(freq):
    # Sort keys for stable, predictable output order.
    for key in sorted(freq):
        print(f"{key} -> {freq[key]}")

def main():
    tokens = []
    for line in sys.stdin:
        # Split each input line on whitespace and append tokens.
        tokens.extend(line.split())
    show_frequency_map(build_frequency_map(tokens))

if __name__ == "__main__":
    main()
