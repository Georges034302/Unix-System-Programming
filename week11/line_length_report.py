#!/usr/bin/env python3
"""
Print each line with its length, then show shortest and longest line.

Usage:
1. Run: python3 line_length_report.py
2. Enter a text filename when prompted.
3. The script prints line lengths and a shortest/longest summary.
"""

# Reads all lines from a text file.
def read_lines(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.readlines()

# Strips newline from a line.
def clean_line(line):
    return line.rstrip("\n")

# Finds shortest line by comparing lengths.
def find_shortest_line(lines):
    return min(lines, key=lambda line: len(clean_line(line)))

# Finds longest line by comparing lengths.
def find_longest_line(lines):
    return max(lines, key=lambda line: len(clean_line(line)))

# Finds blank lines in text.
def find_blank_lines(lines):
    blank_numbers = [i + 1 for i, line in enumerate(lines) if clean_line(line).strip() == ""]
    return blank_numbers

# Prints the summary report.
def print_summary(lines, blank_numbers):
    shortest = clean_line(find_shortest_line(lines))
    longest = clean_line(find_longest_line(lines))
    
    print()
    print(f"Shortest line length: {len(shortest)}")
    print(f"Shortest line text: {shortest}")
    print(f"Longest line length: {len(longest)}")
    print(f"Longest line text: {longest}")
    
    if blank_numbers:
        print(f"Blank lines: {len(blank_numbers)} at lines {blank_numbers}")
    else:
        print("None")

# Runs the script.
def main():
    filename = input("Input text filename: ").strip()
    lines = read_lines(filename)
    blank_numbers = find_blank_lines(lines)
    print_summary(lines, blank_numbers)

if __name__ == "__main__":
    main()
