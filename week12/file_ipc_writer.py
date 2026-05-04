#!/usr/bin/env python3
"""
Write a message into a shared text file for file-based IPC.

Usage:
1. Run this writer first: python3 file_ipc_writer.py
2. Run reader next: python3 file_ipc_reader.py
"""

SHARED_FILE = "shared_message.txt"


# Save message to shared file.
def write_message(path, message):
    with open(path, "w", encoding="utf-8") as file:
        file.write(message + "\n")


# Run writer workflow.
def main():
    message = "Hello from file IPC writer"
    write_message(SHARED_FILE, message)
    print(f"Writer saved message in {SHARED_FILE}")


if __name__ == "__main__":
    main()
