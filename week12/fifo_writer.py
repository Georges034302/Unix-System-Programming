#!/usr/bin/env python3
"""
Write one message to a named pipe (FIFO).

Usage:
1. Start reader first: python3 fifo_reader.py
2. Then run writer: python3 fifo_writer.py
"""

import os

FIFO_NAME = "week12_fifo"


# Create FIFO if it does not already exist.
def ensure_fifo_exists(path):
    if not os.path.exists(path):
        os.mkfifo(path)


# Write one message into FIFO.
def write_to_fifo(path, message):
    with open(path, "w", encoding="utf-8") as fifo_file:
        fifo_file.write(message)


# Run writer workflow.
def main():
    ensure_fifo_exists(FIFO_NAME)
    message = "Hello from FIFO writer"
    write_to_fifo(FIFO_NAME, message)
    print("Writer sent message")


if __name__ == "__main__":
    main()
