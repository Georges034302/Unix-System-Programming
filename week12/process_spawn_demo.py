#!/usr/bin/env python3
"""
Create one child process using multiprocessing.Process.

Usage:
1. Run: python3 process_spawn_demo.py
2. Script starts a child process and waits for it to finish.
"""

from multiprocessing import Process
import os


# Work performed by the child process.
def child_task():
    print(f"Child process PID: {os.getpid()}")
    print("Child process: doing work")


# Start child process and wait for completion.
def run_process_demo():
    process = Process(target=child_task)
    process.start()
    process.join()

    print(f"Parent process PID: {os.getpid()}")
    print(f"Child process finished with PID: {process.pid}")


# Run the script.
def main():
    run_process_demo()


if __name__ == "__main__":
    main()
