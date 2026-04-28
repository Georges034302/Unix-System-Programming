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
    numbers = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            for token in line.split():
                if token.lstrip("-").isdigit():
                    numbers.append(token)
    return numbers

# Applies regex pattern substitution and prints result to stdout.
def replace_pattern(filename, pattern, replacement):
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    updated = re.sub(pattern, replacement, content)
    print(updated, end="")

# Dispatches operation to the correct handler function.
def handle_operation(op, args):
    filename = args[2]
    match op:
        case "-s":
            show_content(filename)
        case "-c":
            print("Word count =", word_count(filename))
        case "-n":
            numbers = find_numbers(filename)
            print("Numbers found:", numbers)
        case "-r":
            if len(args) < 5:
                print("Usage: python3 file_operations.py -r <file> <pattern> <replacement>")
                return
            replace_pattern(filename, args[3], args[4])
        case _:
            print(f"Invalid option: {op}")

# Parses arguments and delegates to handle_operation.
def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python3 file_operations.py -s <file>")
        print("  python3 file_operations.py -c <file>")
        print("  python3 file_operations.py -n <file>")
        print("  python3 file_operations.py -r <file> <pattern> <replacement>")
        return
    handle_operation(sys.argv[1], sys.argv)
if __name__ == "__main__":
    main()
