#!/usr/bin/env python3
"""
Exchange a Python object using multiprocessing.Queue.

Usage:
1. Run: python3 process_queue_demo.py
2. Child puts a dictionary into queue, parent receives it.
"""

from multiprocessing import Process, Queue


# Child sends one dictionary object to queue.
def child_put_message(queue):
    payload = {"source": "child", "message": "Hello via queue", "id": 1}
    queue.put(payload)


# Parent receives one object from queue.
def parent_get_message(queue):
    return queue.get()


# Run queue IPC workflow.
def run_queue_demo():
    queue = Queue()

    process = Process(target=child_put_message, args=(queue,))
    process.start()

    message = parent_get_message(queue)
    print(f"Parent received: {message}")

    process.join()


# Run script workflow.
def main():
    run_queue_demo()


if __name__ == "__main__":
    main()
