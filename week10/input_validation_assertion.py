#!/usr/bin/env python3
"""
Validate two integer inputs and print a division result.
Usage: python3 input_validation_assertion.py
"""

def validate_input(value):
    try:
        return int(value.strip())
    except ValueError as error:
        raise ValueError("Value is not a valid integer") from error

def validate_b_not_zero(value):
    if value == 0:
        raise ValueError("b must not be zero")

def main():
    a = validate_input(input("a: "))
    b = validate_input(input("b: "))

    validate_b_not_zero(b)

    print("Division =", a / b)

if __name__ == "__main__":
    main()
