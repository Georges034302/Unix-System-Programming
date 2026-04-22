#!/usr/bin/env python3
"""
Analyse a list of file sizes and produce a summary report.
Demonstrates: lists, iteration, aggregation, indexing, formatting.
"""

file_sizes = [1200, 850, 3000, 450, 2200, 980]

total_size = 0
largest = file_sizes[0]
smallest = file_sizes[0]

for size in file_sizes:
    total_size += size
    if size > largest:
        largest = size
    if size < smallest:
        smallest = size

average_size = total_size / len(file_sizes)

print("File sizes      :", file_sizes)
print(f"Count           : {len(file_sizes)}")
print(f"Total size      : {total_size} bytes")
print(f"Average size    : {average_size:.2f} bytes")
print(f"Largest file    : {largest} bytes")
print(f"Smallest file   : {smallest} bytes")
