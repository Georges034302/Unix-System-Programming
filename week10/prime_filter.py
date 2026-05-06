#!/usr/bin/env python3
"""
Generate random numbers and filter primes.
Usage: python3 prime_filter.py
Prompts for start, end, and size to generate random numbers and display primes.
"""
import random

# Generates size unique random integers in range [start, end].
def random_list(size, start, end):
    if start > end:
        raise ValueError("start must be <= end")
    if size > end - start + 1:
        raise ValueError("size is larger than the available range")
    return random.sample(range(start, end + 1), size)

# Returns True if n is a prime number, False otherwise.
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2
    return True

# Filters and returns only prime numbers from a list.
def prime_list(numbers):
    return [number for number in numbers if is_prime(number)]

# Prompts user for start, end, size and generates random numbers.
def get_user_input():
    start = int(input("start: ").strip())
    end = int(input("end: ").strip())
    size = int(input("size: ").strip())
    return start, end, size

# Prompts for input, generates random numbers, and displays primes.
def main():
    start, end, size = get_user_input()
    numbers = random_list(size, start, end)
    primes = prime_list(numbers)
    print("Numbers:", numbers)
    print("Primes :", primes)

if __name__ == "__main__":
    main()
