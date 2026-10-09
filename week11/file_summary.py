#!/usr/bin/env python3
"""
Scan directory and classify files by extension with counts.

Usage:
1. Run: python3 file_summary.py
2. Enter a directory path.
3. The script prints counts for files directly inside that directory, grouped by extension.
"""
import os

# Returns file extension (e.g., ".txt", ".py").
def get_extension(filename):
    _, ext = os.path.splitext(filename)
    # Give extensionless files their own group rather than using an empty key.
    return ext.lower() if ext else "no_extension"

# Scans directory for files and counts by extension.
def classify_files(path):
    extensions = {}
    
    for name in os.listdir(path):
        item_path = os.path.join(path, name)
        
        if os.path.isfile(item_path):
            ext = get_extension(name)
            # Increment this extension's count, starting at one for its first file.
            extensions[ext] = extensions.get(ext, 0) + 1
    
    return extensions

# Prints file counts for each extension.
def print_summary(extensions):
    if not extensions:
        print("No files found.")
        return
    
    print()
    for ext in sorted(extensions.keys()):
        count = extensions[ext]
        print(f"{ext:<15} {count:>5} files")

# Runs the script.
def main():
    path = input("Directory path: ").strip()
    
    if not os.path.isdir(path):
        print("Not a valid directory.")
        return
    
    extensions = classify_files(path)
    print_summary(extensions)

if __name__ == "__main__":
    main()
