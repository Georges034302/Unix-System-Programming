#!/usr/bin/env python3
"""
Extract lines containing a keyword and save them to a new file.

Usage:
1. Run: python3 keyword_line_extractor.py
2. Enter input filename and keyword.
3. The script always saves matching lines to matches.txt.
"""
OUTPUT_FILE = "matches.txt"

# Returns only lines that contain the keyword.
def filter_matching_lines(lines, keyword):
    matches = []

    for line in lines:
        # Case-insensitive plain text matching.
        if keyword.lower() in line.lower():
            matches.append(line)

    return matches

# Writes selected lines to an output file.
def write_lines(filename, lines):
    with open(filename, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line)

# Reads saved matches and prints them.
def show_saved_matches(filename):
    print("\nMatched lines:")

    with open(filename, "r", encoding="utf-8") as file:
        saved_lines = file.readlines()

    for line in saved_lines:
        print(line.rstrip("\n"))

# Runs the script.
def main():
    input_file = input("Input text filename: ").strip()
    keyword = input("Keyword: ").strip()

    with open(input_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    matches = filter_matching_lines(lines, keyword)
    write_lines(OUTPUT_FILE, matches)

    print(f"Saved {len(matches)} matching lines to {OUTPUT_FILE}")
    show_saved_matches(OUTPUT_FILE)

if __name__ == "__main__":
    main()
