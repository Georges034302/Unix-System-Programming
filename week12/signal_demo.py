#!/usr/bin/env python3
"""
Handle SIGINT and SIGTERM signals in a running process.

Usage:
1. Run: python3 signal_demo.py
2. Press Ctrl+C or use: kill -TERM <pid>
"""

import os
import signal
import time


# Handle incoming signal and exit cleanly.
def handle_signal(signum, _frame):
    print(f"Signal received: {signum}. Exiting cleanly.")
    raise SystemExit(0)


# Register signal handlers.
def register_handlers():
    signal.signal(signal.SIGINT, handle_signal)
    signal.signal(signal.SIGTERM, handle_signal)


# Run loop waiting for signals.
def run_wait_loop():
    print(f"Signal demo running. PID={os.getpid()}")
    print("Press Ctrl+C or send SIGTERM to stop.")
    while True:
        time.sleep(1)


# Run script workflow.
def main():
    register_handlers()
    run_wait_loop()


if __name__ == "__main__":
    main()
