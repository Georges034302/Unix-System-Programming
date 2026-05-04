#!/usr/bin/env python3
"""
Display directory structure in a tree view.

Usage:
1. Run: python3 directory_viewer.py
2. Enter a directory path.
3. The script prints the directory tree with indentation.
"""
import os

# Returns "└── " if last, else "├── ".
def get_connector(is_last):
    return "└── " if is_last else "├── "

# Returns "    " if last, else "│   ".
def get_extension(is_last):
    return "    " if is_last else "│   "

# Returns sorted list of items in a directory.
def list_items(path):
    return sorted(os.listdir(path))

# Returns True if path is a directory.
def is_directory(path):
    return os.path.isdir(path)

# Prints a single node with connector and name.
def print_node(prefix, connector, name):
    print(f"{prefix}{connector}{name}")

# Prints all items in a directory (recurse for subdirs).
def print_items(path, prefix):
    items = list_items(path)
    for index, item in enumerate(items):
        item_path = os.path.join(path, item)
        is_last = (index == len(items) - 1)
        connector = get_connector(is_last)
        
        if is_directory(item_path):
            print_node(prefix, connector, f"{item}/")
            next_prefix = prefix + get_extension(is_last)
            print_items(item_path, next_prefix)
        else:
            print_node(prefix, connector, item)

# Displays directory tree starting from root.
def show_tree(path):
    print(f"{path}/")
    print_items(path, "")

# Runs the script.
def main():
    path = input("Directory path to view: ").strip()
    
    if not is_directory(path):
        print("Not a valid directory.")
        return
    
    print()
    show_tree(path)

if __name__ == "__main__":
    main()
