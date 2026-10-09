#!/usr/bin/env python3
"""
Send one message from child process to parent using Pipe.

Usage:
1. Run: python3 process_pipe_demo.py
2. Child sends a message and parent prints it.
"""

from multiprocessing import Process, Pipe


# Child process sends one message through the pipe.
def child_send_message(child_connection):
    child_connection.send("Hello from child process")
    # Close this endpoint when the child has finished sending.
    child_connection.close()


# Create pipe, start child, receive message in parent.
def run_pipe_demo():
    # Pipe returns the parent and child endpoints of a duplex connection.
    parent_connection, child_connection = Pipe()

    process = Process(target=child_send_message, args=(child_connection,))
    process.start()

    # recv() waits until the child sends a value through its endpoint.
    message = parent_connection.recv()
    print(f"Parent received: {message}")

    process.join()


# Run the script.
def main():
    run_pipe_demo()


if __name__ == "__main__":
    main()
