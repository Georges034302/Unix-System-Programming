#!/usr/bin/env python3
"""
File operations: show content, count words, find numbers, replace regex pattern.
Usage:
    python3 file_operations.py -s <file>  - Show the full content of the file.
    python3 file_operations.py -c <file>  - Count words in the file.
    python3 file_operations.py -n <file>  - List integer numbers found in the file.
    python3 file_operations.py -r <file> <pattern> <replacement>  - Replace regex matches and print the updated text to stdout.
"""
import sys
import re

USAGE = (
    "Usage:\n"
    "  python3 file_operations.py -s <file>  \t\t\t\t- Show the full content of the file.\n"
    "  python3 file_operations.py -c <file>  \t\t\t\t- Count words in the file.\n"
    "  python3 file_operations.py -n <file>  \t\t\t\t- List integer numbers found in the file.\n"
    "  python3 file_operations.py -r <file> <pattern> <replacement>  \t- Replace regex matches and print the updated text to stdout."
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
        # Treat each whitespace-separated token as a candidate number.
        # lstrip("-") allows negative integers such as -42.
        return [token for line in file for token in line.split() if token.lstrip("-").isdigit()]

# Applies regex pattern substitution and prints result to stdout.
def replace_pattern(filename, pattern, replacement):
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    updated = re.sub(pattern, replacement, content)
    print(updated, end="")

def main():
    # Skip script name and parse only user-provided arguments.
    args = sys.argv[1:]
    if not args:
        print(USAGE)
        return

    op = args[0]
    # Handle single-file operations with exactly one filename argument.
    if op in {"-s", "-c", "-n"} and len(args) == 2:
        filename = args[1]
        if op == "-s":
            show_content(filename)
        elif op == "-c":
            print("Word count =", word_count(filename))
        else:
            print("Numbers found:", find_numbers(filename))
        return

    # Regex replace requires: -r <file> <pattern> <replacement>.
    if op == "-r" and len(args) == 4:
        replace_pattern(args[1], args[2], args[3])
        return

    print(USAGE)

if __name__ == "__main__":
    main()
