#!/usr/bin/env python3
"""
File operations: show content, count words, find numbers, replace regex pattern.
Usage:
  python3 file_operations.py -s <file>              (show file content)
  python3 file_operations.py -c <file>              (count words)
  python3 file_operations.py -n <file>              (find all numbers)
  python3 file_operations.py -r <file> <pattern> <replacement>  (regex replace, stdout only)
"""
import sys
import re

USAGE = (
    "Usage:\n"
    "  python3 file_operations.py -s <file>\n"
    "  python3 file_operations.py -c <file>\n"
    "  python3 file_operations.py -n <file>\n"
    "  python3 file_operations.py -r <file> <pattern> <replacement>"
)

# Prints the full content of a file to stdout.
def show_content(filename):
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")

# Returns the total number of words in a file.
def word_count(filename):
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()
    return len(text.split())

# Finds and returns all numeric tokens in a file.
def find_numbers(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return [token for line in file for token in line.split() if token.lstrip("-").isdigit()]

# Applies regex pattern substitution and prints result to stdout.
def replace_pattern(filename, pattern, replacement):
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    updated = re.sub(pattern, replacement, content)
    print(updated, end="")

def main():
    args = sys.argv[1:]
    if not args:
        print(USAGE)
        return

    op = args[0]
    if op in {"-s", "-c", "-n"} and len(args) == 2:
        filename = args[1]
        if op == "-s":
            show_content(filename)
        elif op == "-c":
            print("Word count =", word_count(filename))
        else:
            print("Numbers found:", find_numbers(filename))
        return

    if op == "-r" and len(args) == 4:
        replace_pattern(args[1], args[2], args[3])
        return

    print(USAGE)

if __name__ == "__main__":
    main()
