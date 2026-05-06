#!/usr/bin/env python3
"""
Represent a process as a fixed record using a tuple.
Demonstrates: tuples, indexing, unpacking, immutability by design.
"""

# Tuple represents a fixed process snapshot: (command, pid, status).
process = ("python3", 2481, "running")

# Unpack tuple fields into named variables for readability.
command, pid, status = process

print("Process record  :", process)
print("Command         :", command)
print("PID             :", pid)
print("Status          :", status)

# Tuples are immutable, so create a new one to represent a state change.
updated_process = (command, pid, "sleeping")
print("Updated record  :", updated_process)
