#!/usr/bin/env python3
"""
Demonstrate safe division with input validation.

Usage:
    python3 input_validation_assertion.py

What it does:
    1. Lets you choose input mode: int or float.
    2. Prompts for two values: a and b.
    3. Validates empty input, type format, range, sign, and zero denominator.
    4. Prints the division result (a / b).
"""

MIN_VALUE = -1_000_000
MAX_VALUE = 1_000_000
ALLOW_NEGATIVE = False

# Returns a / b.
def div(a, b):
    return a / b


# Validates that input is not empty after trimming whitespace.
def validate_not_empty(raw_value, field_name):
    # Whitespace normalization is done with strip() before any parsing.
    value = raw_value.strip()
    if value == "":
        raise ValueError(f"{field_name} cannot be empty")
    return value


# Validates value is within the configured inclusive numeric bounds.
def validate_range(value, field_name):
    if not MIN_VALUE <= value <= MAX_VALUE:
        raise ValueError(
            f"{field_name} must be between {MIN_VALUE} and {MAX_VALUE}"
        )


# Validates sign policy based on ALLOW_NEGATIVE.
def validate_sign(value, field_name):
    if not ALLOW_NEGATIVE and value < 0:
        raise ValueError(f"{field_name} must be non-negative")


# Parses input according to selected mode (int or float).
def validate_type_and_parse(value, mode, field_name):
    # Type mode validation: int mode parses as int, float mode parses as float.
    try:
        if mode == "int":
            return int(value)
        return float(value)
    except ValueError as error:
        if mode == "int":
            raise ValueError(f"{field_name} must be a valid integer") from error
        raise ValueError(f"{field_name} must be a valid float") from error


# Validates denominator is not zero.
def validate_b_not_zero(value):
    # Guard against division by zero before dividing.
    if value == 0:
        raise ValueError("Division by zero: b cannot be zero")


# Reads and validates the numeric input mode.
def get_mode():
    # Normalize case and spacing so users can type variants like " INT ".
    mode = input("Mode (int/float): ").strip().lower()
    if mode not in {"int", "float"}:
        raise ValueError("Mode must be 'int' or 'float'")
    return mode


# Collects and validates both operands, then returns parsed values.
def get_user_input(mode):
    # Prompt and validate in one place so main() stays clean.
    raw_a = validate_not_empty(input("a = "), "a")
    raw_b = validate_not_empty(input("b = "), "b")

    # Parse values after emptiness checks.
    a = validate_type_and_parse(raw_a, mode, "a")
    b = validate_type_and_parse(raw_b, mode, "b")

    # Apply business rules before computation.
    validate_range(a, "a")
    validate_range(b, "b")
    validate_sign(a, "a")
    validate_sign(b, "b")
    validate_b_not_zero(b)
    return a, b


# Orchestrates mode selection, input validation, and safe division output.
def main():
    try:
        mode = get_mode()
        a, b = get_user_input(mode)
        print("Result:", div(a, b))
    except ValueError as error:
        print("Error:", error)

if __name__ == "__main__":
    main()
