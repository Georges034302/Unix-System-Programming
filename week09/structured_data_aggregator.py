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

# Maps each category to its running total value.
totals = {}

with open(sys.argv[1], encoding="utf-8") as fin:
    for line in fin:
        line = line.rstrip("\n")  # strip newline but keep leading spaces

        # Skip blank lines between records.
        if not line:
            continue

        # Split on comma to get category and numeric value.
        category, value_text = line.split(",")
        value = int(value_text)  # convert text to integer before accumulating

        # Accumulate value into existing category or initialise it.
        if category in totals:
            totals[category] += value
        else:
            totals[category] = value

print("Aggregated totals:")
for category in totals:
    print(f"  {category:12} -> {totals[category]}")
