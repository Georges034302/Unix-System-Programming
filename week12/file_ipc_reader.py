#!/usr/bin/env python3
"""
Read a message from a shared text file for file-based IPC.

Usage:
1. Run writer first: python3 file_ipc_writer.py
2. Then run this script: python3 file_ipc_reader.py
"""

SHARED_FILE = "shared_message.txt"


# Load message from shared file.
def read_message(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read().strip()


# Run reader workflow.
def main():
    message = read_message(SHARED_FILE)
    print(f"Reader loaded: {message}")


if __name__ == "__main__":
    main()
