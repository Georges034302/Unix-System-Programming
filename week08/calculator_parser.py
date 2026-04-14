#!/usr/bin/env python3

import re
import sys

expr = input("Expression: ")

# --- Parse ---
# pattern captures: left number, operator, right number
# -?\d+ allows optional negative sign before digits
pattern = r"^\s*(-?\d+)\s*([+\-*/])\s*(-?\d+)\s*$"
match = re.match(pattern, expr)

if not match:
    print("Invalid expression")
    sys.exit(1)

left  = int(match.group(1))  # first number
op    = match.group(2)        # operator
right = int(match.group(3))  # second number

# --- Calculate ---
if op == "+":
    result = left + right
elif op == "-":
    result = left - right
elif op == "*":
    result = left * right
elif op == "/":
    if right == 0:
        print("Error: division by zero")
        sys.exit(1)
    result = left / right

# --- Output ---
print(f"Left operand : {left}")
print(f"Operator     : {op}")
print(f"Right operand: {right}")
print(f"Result       : {result}")
