#!/usr/bin/env python3
"""
Read a text file from a command-line argument into a clean list of lines.
Demonstrates: file input, stripping newlines, appending to a list.

Usage:
    python3 list_from_file_reader.py input.txt
"""

import sys

if len(sys.argv) != 2:
    print("Usage: python3 list_from_file_reader.py <input_file>")
    raise SystemExit(1)

clean_lines = []

with open(sys.argv[1], encoding="utf-8") as fin:
    for line in fin:
        clean_lines.append(line.rstrip("\n"))

print("Cleaned lines:")
for line in clean_lines:
    print(f"  {line}")

print(f"\nLine count: {len(clean_lines)}")
