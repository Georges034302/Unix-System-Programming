#!/usr/bin/env python3
"""
Share text between processes using multiprocessing.shared_memory.

Usage:
1. Run: python3 shared_memory_demo.py
2. Parent creates shared memory, child reads from it.
3. Parent releases its handle and unlinks the shared-memory block after the child exits.
"""

from multiprocessing import Process
from multiprocessing import shared_memory


# Child attaches to shared memory and reads bytes.
def child_read(shared_name, byte_count):
    # Attach by name; read only the bytes containing the encoded message.
    shm = shared_memory.SharedMemory(name=shared_name)
    raw = bytes(shm.buf[:byte_count])
    message = raw.decode("utf-8")
    print(f"Child read from shared memory: {message}")
    shm.close()


# Create shared memory, write message, run child reader.
def run_shared_memory_demo():
    message = "Hello from shared memory"
    message_bytes = message.encode("utf-8")

    # Allocate exactly enough shared storage for the UTF-8 encoded message.
    shm = shared_memory.SharedMemory(create=True, size=len(message_bytes))
    shm.buf[: len(message_bytes)] = message_bytes

    process = Process(target=child_read, args=(shm.name, len(message_bytes)))
    process.start()
    process.join()

    # Close this process's handle, then unlink the shared block from the system.
    shm.close()
    shm.unlink()


# Run script workflow.
def main():
    run_shared_memory_demo()


if __name__ == "__main__":
    main()
