#!/usr/bin/env python3

line_count  = 0
total_chars = 0
longest     = ""
shortest    = ""

line = input("Line (or END): ")

while line != "END":
    line_count  += 1
    total_chars += len(line)

    if line_count == 1:                  # first line sets the baseline
        longest = shortest = line
    else:
        if len(line) > len(longest):     longest  = line
        if len(line) < len(shortest):    shortest = line

    line = input("Line (or END): ")

# --- Summary ---
print(f"\nLines   : {line_count}")
print(f"Chars   : {total_chars}")

if line_count > 0:
    print(f"Longest : {longest}")
    print(f"Shortest: {shortest}")
else:
    print("No lines entered")
