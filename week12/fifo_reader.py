#!/usr/bin/env python3
"""
Read one message from a named pipe (FIFO).

Usage:
1. In terminal 1 run: python3 fifo_reader.py
2. In terminal 2 run: python3 fifo_writer.py
"""

import os

FIFO_NAME = "week12_fifo"


# Create FIFO if it does not already exist.
def ensure_fifo_exists(path):
    if not os.path.exists(path):
        os.mkfifo(path)


# Read one message from FIFO.
def read_from_fifo(path):
    with open(path, "r", encoding="utf-8") as fifo_file:
        return fifo_file.read().strip()


# Run reader workflow.
def main():
    ensure_fifo_exists(FIFO_NAME)
    print(f"Reader waiting on FIFO: {FIFO_NAME}")
    message = read_from_fifo(FIFO_NAME)
    print(f"Reader received: {message}")


if __name__ == "__main__":
    main()
