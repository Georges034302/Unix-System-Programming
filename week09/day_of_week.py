#!/usr/bin/env python3
"""
Determine the day of the week using:
1. total days from start of year
2. simple offset calculation

Usage:
    python3 day_of_week.py
    Enter a day and month when prompted. The example assumes a non-leap year
    with January 1 on Monday.

Concepts:
- lists
- loops
- accumulation
- modulo (%)
"""

# days in each month (non-leap year)
days = [31,28,31,30,31,30,31,31,30,31,30,31]

# read input
day = int(input("Day   = "))
month = int(input("Month = "))

# compute total days from Jan 1
i = 0
total = 0

while i < month - 1:
    total += days[i]
    i += 1

total += day

# assume Jan 1 is Monday (for teaching simplicity)
day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# determine day of week
index = (total - 1) % 7

print(f"Total days = {total}")
print(f"Day of week = {day_names[index]}")
