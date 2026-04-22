#!/usr/bin/env python3
"""
Aggregate printer jobs using a dictionary of lists.
Demonstrates: dictionary of lists, grouped counters, grouped totals.
"""

jobs = [
    ("Printer_A", 120),
    ("Printer_B", 350),
    ("Printer_A", 80),
    ("Printer_C", 500),
    ("Printer_B", 90),
]

printers = {}

for printer_name, job_size in jobs:
    if printer_name in printers:
        printers[printer_name][0] += 1
        printers[printer_name][1] += job_size
    else:
        printers[printer_name] = [1, job_size]

print("Printer summary:")
for printer_name in printers:
    job_count, total_size = printers[printer_name]
    print(f"  {printer_name:10} -> jobs: {job_count}, total size: {total_size}")
