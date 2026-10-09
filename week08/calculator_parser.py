#!/usr/bin/env python3
"""
Parse and evaluate a basic arithmetic expression.

Usage:
    python3 calculator_parser.py
    Enter an expression with two integers (which may be negative) and one of +, -, *, or /.
"""

import re
import sys

# r keeps backslashes for the regex:
# \d is a digit
# \s is whitespace
# + means one or more digits
# * means zero or more spaces.
# ? makes the minus sign optional for each number.
# Parentheses capture each number and the operator.
pattern = r"(-?\d+)\s*([+*/-])\s*(-?\d+)"

expression = input("Expression: ").strip()  # Read the calculation and remove outer spaces.
match = re.fullmatch(pattern, expression)   # Require the pattern to match the whole input.

if not match:
    print("Invalid expression")             # Explain that the input did not match the pattern.
    sys.exit(1)                             # Stop because there are no valid values to calculate.

left, op, right = match.groups()            # Get the three captured parts from the match.
left, right = int(left), int(right)         # Convert the number strings to integers.

if op == "+":
    result = left + right  # Add the operands.
elif op == "-":
    result = left - right  # Subtract the right operand from the left.
elif op == "*":
    result = left * right  # Multiply the operands.
elif op == "/":
    if right == 0:
        print("Error: division by zero")    # Division by zero is undefined.
        sys.exit(1)                         # Stop before attempting the division.
    result = left / right                   # Divide the left operand by the right.

print(f"Left operand : {left}")             # Show the first number.
print(f"Operator     : {op}")               # Show the selected operation.
print(f"Right operand: {right}")            # Show the second number.
print(f"Result       : {result}")           # Show the calculated answer.
