#!/usr/bin/env python3
"""
Represent a process as a fixed record using a tuple.
Demonstrates: tuples, indexing, unpacking, immutability by design.
"""

process = ("python3", 2481, "running")

command, pid, status = process

print("Process record  :", process)
print("Command         :", command)
print("PID             :", pid)
print("Status          :", status)

updated_process = (command, pid, "sleeping")
print("Updated record  :", updated_process)
