#!/usr/bin/env python3
"""
Generate random numbers and group them into bucket ranges.
Usage: python3 number_bucket_classifier.py
"""

import random

# Reads and validates the count of random numbers to generate.
def read_count(prompt):
    response = input(prompt).strip()
    # Accept only positive whole-number input for sample size.
    if not response.isdigit() or int(response) <= 0:
        raise ValueError("Please enter a positive integer")
    return int(response)


# Generates n random integers in the inclusive range [min_val, max_val].
def generate_random_numbers(n, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(n)]


# Returns the bucket label string for a value and bucket width.
def bucket_label(value, width):
    # Compute inclusive bucket bounds (e.g., 27 with width 10 -> 20-29).
    start = (value // width) * width
    end = start + width - 1
    return f"{start}-{end}"


# Groups numbers into labeled buckets and returns the mapping.
def classify_numbers(numbers, width):
    buckets = {}
    for number in numbers:
        label = bucket_label(number, width)
        # Initialize bucket list on first use, then append current value.
        if label not in buckets:
            buckets[label] = []
        buckets[label].append(number)
    return buckets


# Extracts numeric bucket start for proper label sorting.
def bucket_start(label):
    # Extract left bound for numeric sorting of labels like "10-19".
    return int(label.split("-")[0])


# Runs the CLI flow: input, generation, classification, and display.
def main():
    n = read_count("How many random numbers? ")
    # Fixed bucket width keeps distribution output consistent.
    width = 10
    numbers = generate_random_numbers(n, 1, 99)
    buckets = classify_numbers(numbers, width)
    print(f"\nGenerated {n} random numbers in range [1, 99]")
    print(f"Numbers: {numbers}")
    print("\nBucket Distribution:\n")
    print("Bucket       Count    Contents")
    print("-" * 50)
    # Sort by bucket start so rows appear in ascending range order.
    for label in sorted(buckets, key=bucket_start):
        count = len(buckets[label])
        content = buckets[label]
        print(f"{label:<12} {count:<8} {content}")


if __name__ == "__main__":
    main()
