#!/usr/bin/env python3
import sys

def build_frequency_map(items):
    freq = {}

    for item in items:
        freq[item] = freq.get(item, 0) + 1

    return freq

def show_frequency_map(freq):
    for key in sorted(freq):
        print(f"{key} -> {freq[key]}")

def main():
    tokens = []

    for line in sys.stdin:
        tokens.extend(line.split())

    show_frequency_map(build_frequency_map(tokens))

if __name__ == "__main__":
    main()
