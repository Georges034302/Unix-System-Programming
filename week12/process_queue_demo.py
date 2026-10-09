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
    # Queue safely transports picklable Python objects between processes.
    queue.put(payload)


# Parent receives one object from queue.
def parent_get_message(queue):
    # get() blocks until an object is available from the child.
    return queue.get()


# Run queue IPC workflow.
def run_queue_demo():
    queue = Queue()

    process = Process(target=child_put_message, args=(queue,))
    process.start()

    message = parent_get_message(queue)
    print(f"Parent received: {message}")

    # Wait for the producer process to finish after receiving its payload.
    process.join()


# Run script workflow.
def main():
    run_queue_demo()


if __name__ == "__main__":
    main()
