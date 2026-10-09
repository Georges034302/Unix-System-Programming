#!/usr/bin/env python3
"""
Read one message from a named pipe (FIFO).

Usage:
1. In terminal 1 run: python3 fifo_reader.py
2. In terminal 2 run: python3 fifo_writer.py
3. The reader waits until the writer opens the FIFO and sends a message.
"""

import os

FIFO_NAME = "week12_fifo"


# Create FIFO if it does not already exist.
def ensure_fifo_exists(path):
    # Both programs use the same named pipe as their communication endpoint.
    if not os.path.exists(path):
        os.mkfifo(path)


# Read one message from FIFO.
def read_from_fifo(path):
    # Opening a FIFO for reading blocks until a writer connects.
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
