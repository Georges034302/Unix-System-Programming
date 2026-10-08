#!/usr/bin/env python3
"""
Generate random numbers and group them into bucket ranges.
Usage: python3 number_bucket_classifier.py
"""

import random

# Group numbers into ranges of ten.
def classify_numbers(numbers):
    buckets = {}
    for number in numbers:
        start = (number // 10) * 10
        label = f"{start}-{start + 9}"
        if label not in buckets:
            buckets[label] = []
        buckets[label].append(number)
    return buckets


# Get the count, generate numbers, and display their bucket distribution.
def main():
    n = int(input("How many random numbers? "))

    numbers = [random.randint(1, 99) for _ in range(n)]
    buckets = classify_numbers(numbers)
    
    print(f"\nGenerated {n} random numbers in range [1, 99]")
    print(f"Numbers: {numbers}")
    print("\nBucket Distribution:\n")
    print("Bucket       Count    Contents")
    print("-" * 50)

    for label in sorted(buckets):
        count = len(buckets[label])
        print(f"{label:<12} {count:<8} {buckets[label]}")


if __name__ == "__main__":
    main()
