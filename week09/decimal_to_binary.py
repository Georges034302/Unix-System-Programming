#!/usr/bin/env python3
"""
Convert a decimal number (0–255) to 8-bit binary.

Concepts:
- input validation
- repeated division by 2
- storing digits in a list
- printing in reverse order
- fixed 8-bit output
"""

# read input
n = int(input("Enter a decimal number (0–255): "))

# validate range
if n < 0 or n > 255:
    print("Error: value must be between 0 and 255")
    raise SystemExit(1)

original = n

# store binary digits (in reverse order)
bits = []

# build binary digits
while n > 0:
    bits.append(n % 2)   # store remainder (0 or 1)
    n = n // 2

# ensure 8 digits by adding zeros
while len(bits) < 8:
    bits.append(0)

# print digits in correct order
print("8-bit Binary:", end=" ")

# loop from last index (7) down to 0 to print the list in reverse order
for i in range(7, -1, -1):
    print(bits[i], end="")

print()
print("Stored digits:", bits)
print(f"{original} converted to 8-bit binary above")
