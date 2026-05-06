#!/usr/bin/env python3
"""
Read a text file from a command-line argument into a clean list of lines.
Demonstrates: file input, stripping newlines, appending to a list.

Usage:
    python3 list_from_file_reader.py input.txt
"""

import sys

# Require exactly one argument: the path to the input file.
if len(sys.argv) != 2:
    print("Usage: python3 list_from_file_reader.py <input_file>")
    raise SystemExit(1)

# Accumulate cleaned lines from the file into this list.
clean_lines = []

with open(sys.argv[1], encoding="utf-8") as fin:
    for line in fin:
        # Strip only the trailing newline, preserving leading spaces.
        clean_lines.append(line.rstrip("\n"))

# Print each cleaned line with indentation for readability.
print("Cleaned lines:")
for line in clean_lines:
    print(f"  {line}")

# Report total number of lines read from the file.
print(f"\nLine count: {len(clean_lines)}")
