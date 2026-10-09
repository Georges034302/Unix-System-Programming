#!/usr/bin/env python3
"""
List files in a directory with their sizes and total size.

Usage:
1. Run: python3 directory_size_report.py
2. Enter a directory path.
3. The script prints each file directly inside that directory and the total size.
"""
import os

# Returns file names and sizes for one directory level.
def collect_file_sizes(path):
    results = []

    for name in os.listdir(path):
        full_path = os.path.join(path, name)
        # Ignore subdirectories; this report only counts files at the given path.
        if os.path.isfile(full_path):
            size = os.path.getsize(full_path)
            results.append((name, size))

    return results

# Prints a simple size report.
def print_size_report(file_data):
    total_size = 0

    for name, size in file_data:
        print(f"{name}: {size} bytes")
        # Add each displayed file's size to the overall total.
        total_size += size

    print(f"Total size: {total_size} bytes")

# Runs the script.
def main():
    path = input("Directory path: ").strip()
    file_data = collect_file_sizes(path)
    print_size_report(file_data)

if __name__ == "__main__":
    main()
