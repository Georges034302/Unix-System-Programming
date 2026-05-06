#!/usr/bin/env python3
"""
Demonstrate safe division with validation.
Usage: python3 safe_division.py
Prompts for two integers and performs division with prevention validation.
"""

# Divides a by b.
def div(a, b):
    return a / b

# Prompts for two integers with validation.
def get_user_input():
    try:
        a = int(input("a = ").strip())
        b = int(input("b = ").strip())
    except ValueError as error:
        raise ValueError("Enter integers only") from error

    if b == 0:
        raise ValueError("Division by zero: b cannot be zero")

    return a, b

# Prompts for input, validates, and performs division.
def main():
    a, b = get_user_input()
    result = div(a, b)
    print("Result:", result)

if __name__ == "__main__":
    main()
