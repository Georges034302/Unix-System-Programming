#!/usr/bin/env python3

# Validates that input text represents an integer value.
def validate_input(value):
    text = value.strip()

    if text.startswith("-"):
        text = text[1:]

    if text == "" or not text.isdigit():
        raise ValueError("Value is not a valid integer")

# Validates that divisor b is not zero.
def validate_b_not_zero(value):
    if value == 0:
        raise ValueError("b must not be zero")

# Reads inputs, validates them, then prints the division result.
def main():
    a = input("a: ")
    b = input("b: ")

    validate_input(a)
    validate_input(b)

    a = int(a)
    b = int(b)

    validate_b_not_zero(b)

    print("Division =", a / b)

if __name__ == "__main__":
    main()
