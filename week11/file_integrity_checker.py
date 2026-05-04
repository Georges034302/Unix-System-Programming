#!/usr/bin/env python3
"""
Create file hashes (SHA-256) and save them to a manifest file.

Usage:
1. Run: python3 file_integrity_checker.py
2. Enter a directory path.
3. Script creates (or overwrites) hash_manifest.json.
"""
import hashlib
import json
import os

MANIFEST_FILE = "hash_manifest.json"

# Computes SHA-256 hash for one file.
def hash_file(filename):
    hasher = hashlib.sha256()

    with open(filename, "rb") as file:
        while True:
            chunk = file.read(4096)
            if not chunk:
                break
            hasher.update(chunk)

    return hasher.hexdigest()

# Builds a hash dictionary for files in one directory level.
def build_hash_map(path, ignore_files=None):
    if ignore_files is None:
        ignore_files = set()

    hash_map = {}

    for name in os.listdir(path):
        # Skip helper files such as the manifest itself.
        if name in ignore_files:
            continue

        full_path = os.path.join(path, name)
        if os.path.isfile(full_path):
            hash_map[name] = hash_file(full_path)

    return hash_map

# Saves hash data to a JSON manifest file.
def save_manifest(filename, hash_map):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(hash_map, file, indent=2)

# Runs the script.
def main():
    path = input("Directory path: ").strip()

    # Stop early if the given directory path is not valid.
    if not os.path.isdir(path):
        print("Error: directory path is not valid.")
        return

    # Save the manifest inside the selected directory.
    manifest_path = os.path.join(path, MANIFEST_FILE)
    current_hashes = build_hash_map(path, {MANIFEST_FILE})
    save_manifest(manifest_path, current_hashes)
    print(f"Manifest saved (overwritten) at {manifest_path}")

if __name__ == "__main__":
    main()
