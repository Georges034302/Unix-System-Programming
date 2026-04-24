#!/usr/bin/env python3

def validate_input(value):
    assert str(value).lstrip("-").isdigit(), "Value is not a number"

def validate_b_not_zero(value):
    assert value != 0, "b is ZERO"

def main():
    try:
        a = input("a: ")
        b = input("b: ")

        validate_input(a)
        validate_input(b)

        a = int(a)
        b = int(b)

        validate_b_not_zero(b)

        print("Division =", a / b)

    except AssertionError as error:
        print("Validation error:", error)

if __name__ == "__main__":
    main()
