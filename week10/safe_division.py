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
    a_str = input("a = ").strip()
    b_str = input("b = ").strip()
    
    if not a_str.lstrip("-").isdigit() or not b_str.lstrip("-").isdigit():
        raise ValueError("Enter integers only")
    
    a = int(a_str)
    b = int(b_str)
    
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
