#!/usr/bin/env python3

import re

record = input("Record: ")  # example: user=alice pid=2048 status=running

# --- Parse ---
# three capturing groups: (\w+) word, (\d+) digits, (\w+) word
pattern = r"^user=(\w+)\s+pid=(\d+)\s+status=(\w+)$"
match = re.match(pattern, record)

# --- Output ---
if match:
    print(f"User   : {match.group(1)}")
    print(f"PID    : {match.group(2)}")
    print(f"Status : {match.group(3)}")
else:
    print("Invalid format")
    print("Expected: user=<name> pid=<number> status=<value>")
