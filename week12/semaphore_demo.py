#!/usr/bin/env python3
"""
Control concurrent thread access using Semaphore.

Usage:
1. Run: python3 semaphore_demo.py
2. Observe only two workers inside critical section at once.
"""

import threading
import time


# Worker enters critical section using semaphore.
def worker(name, semaphore):
    print(f"{name} waiting")
    with semaphore:
        print(f"{name} entered critical section")
        time.sleep(1)
        print(f"{name} leaving critical section")


# Start multiple workers with a semaphore limit.
def run_semaphore_demo():
    semaphore = threading.Semaphore(2)
    threads = []

    for number in range(1, 6):
        thread = threading.Thread(target=worker, args=(f"Worker-{number}", semaphore))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


# Run script workflow.
def main():
    run_semaphore_demo()


if __name__ == "__main__":
    main()
