#!/usr/bin/env python3
"""
Read structured records from a file and aggregate totals by category.

Expected input format:
    category,value

Usage:
    python3 structured_data_aggregator.py input.csv
"""

import sys

if len(sys.argv) != 2:
    print("Usage: python3 structured_data_aggregator.py <input_file>")
    raise SystemExit(1)

totals = {}

with open(sys.argv[1], encoding="utf-8") as fin:
    for line in fin:
        line = line.rstrip("\n")

        if not line:
            continue

        category, value_text = line.split(",")
        value = int(value_text)

        if category in totals:
            totals[category] += value
        else:
            totals[category] = value

print("Aggregated totals:")
for category in totals:
    print(f"  {category:12} -> {totals[category]}")
