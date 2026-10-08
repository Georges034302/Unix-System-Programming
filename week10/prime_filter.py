#!/usr/bin/env python3
"""
Generate random numbers and filter primes.
Usage: python3 prime_filter.py
Prompts for start, end, and size to generate random numbers and display primes.
"""
import random

# Returns True if n is a prime number, False otherwise.
def is_prime(n):
    if n < 2:
        return False
    for e in range(2, n):
        if n % e == 0:
            return False
    return True

# Prompts for input, generates random numbers, and displays primes.
def main():
    start = int(input("start: "))
    end = int(input("end: "))
    size = int(input("size: "))
    numbers = random.sample(range(start, end + 1), size)
    primes = [number for number in numbers if is_prime(number)]
    print("Numbers:", numbers)
    print("Primes :", primes)

if __name__ == "__main__":
    main()
