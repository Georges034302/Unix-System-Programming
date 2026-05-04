#!/usr/bin/env python3
"""
Demonstrate ps listing and safe signal termination using SIGTERM.

Usage:
1. Run: python3 process_management_demo.py
2. Script starts a sleep process, shows it in ps, then terminates it.
"""

import signal
import subprocess


# Start a simple long-running process for demo.
def start_demo_process():
    return subprocess.Popen(["sleep", "60"])


# Show one process entry from ps output.
def show_process_info(pid):
    result = subprocess.run(
        ["ps", "-p", str(pid), "-o", "pid,ppid,stat,cmd"],
        check=True,
        capture_output=True,
        text=True,
    )
    print(result.stdout.strip())


# Stop process gracefully with SIGTERM.
def stop_process(process):
    process.send_signal(signal.SIGTERM)
    process.wait()


# Run demo workflow.
def main():
    process = start_demo_process()
    print(f"Started demo process PID: {process.pid}")

    print("Process snapshot from ps:")
    show_process_info(process.pid)

    stop_process(process)
    print("Process terminated with SIGTERM")


if __name__ == "__main__":
    main()
