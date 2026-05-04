#!/usr/bin/env python3
"""
Create a child process using os.fork and show parent/child PIDs.

Usage:
1. Run: python3 fork_process_demo.py
2. Observe output from both parent and child process.
"""

import os
import time


# Print process identity information.
def print_process_info(role):
    print(f"[{role}] PID={os.getpid()} PPID={os.getppid()}")


# Run a simple fork demonstration.
def run_fork_demo():
    print_process_info("START")

    child_pid = os.fork()

    if child_pid == 0:
        # Child branch: fork returns 0 in the child process.
        print_process_info("CHILD")
        time.sleep(1)
    else:
        # Parent branch: fork returns child's PID in parent process.
        print(f"[PARENT] Child PID is {child_pid}")
        print_process_info("PARENT")
        os.waitpid(child_pid, 0)
        print("[PARENT] Child has finished")


# Run the script.
def main():
    run_fork_demo()


if __name__ == "__main__":
    main()
