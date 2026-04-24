#!/usr/bin/env python3
import random

def random_list(size, start, end):
    if start > end:
        raise ValueError("start must be <= end")

    if size > end - start + 1:
        raise ValueError("size is larger than the available range")

    return random.sample(range(start, end + 1), size)

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

def prime_list(numbers):
    primes = []

    for number in numbers:
        if is_prime(number):
            primes.append(number)

    return primes

def main():
    try:
        start = int(input("start: "))
        end = int(input("end: "))
        size = int(input("size: "))

        numbers = random_list(size, start, end)
        primes = prime_list(numbers)

        print("Numbers:", numbers)
        print("Primes :", primes)

    except ValueError as error:
        print("Error:", error)

if __name__ == "__main__":
    main()
