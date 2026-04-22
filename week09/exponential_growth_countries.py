#!/usr/bin/env python3

"""
Read country population data from a file and compute
exponential growth / decay after t years.

Compute exponential growth using:
    A = P * e^(r * t)

Expected file format (countries.txt):
Country,Population,Rate

Example:
Australia,26000000,0.012
USA,331000000,0.007
"""

import sys
import math

# ensure file argument exists
if len(sys.argv) != 2:
    print("Usage: python3 exponential_growth_countries.py <countries_file>")
    raise SystemExit(1)

file_path = sys.argv[1]

# read time in years from STDIN
t = float(input("Time in years = "))

print("\n--- Exponential Growth Report ---")

# open file passed as argument
with open(file_path, 'r') as fin:
    for line in fin:
        line = line.strip()

        # skip empty lines
        if not line:
            continue

        # split record into fields
        fields = line.split(',')

        # extract values
        country = fields[0].strip()
        P = float(fields[1])   # initial population
        r = float(fields[2])   # growth/decay rate

        # apply exponential growth / decay formula
        A = P * math.exp(r * t)

        # print result
        print(f"{country:12} -> initial: {P:,.0f}, final: {A:,.0f}")
