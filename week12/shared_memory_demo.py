#!/usr/bin/env python3
"""
Share text between processes using multiprocessing.shared_memory.

Usage:
1. Run: python3 shared_memory_demo.py
2. Parent creates shared memory, child reads from it.
"""

from multiprocessing import Process
from multiprocessing import shared_memory


# Child attaches to shared memory and reads bytes.
def child_read(shared_name, byte_count):
    shm = shared_memory.SharedMemory(name=shared_name)
    raw = bytes(shm.buf[:byte_count])
    message = raw.decode("utf-8")
    print(f"Child read from shared memory: {message}")
    shm.close()


# Create shared memory, write message, run child reader.
def run_shared_memory_demo():
    message = "Hello from shared memory"
    message_bytes = message.encode("utf-8")

    shm = shared_memory.SharedMemory(create=True, size=len(message_bytes))
    shm.buf[: len(message_bytes)] = message_bytes

    process = Process(target=child_read, args=(shm.name, len(message_bytes)))
    process.start()
    process.join()

    shm.close()
    shm.unlink()


# Run script workflow.
def main():
    run_shared_memory_demo()


if __name__ == "__main__":
    main()
