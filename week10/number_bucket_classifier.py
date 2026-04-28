#!/usr/bin/env python3
import random

# Read a positive integer from stdin.
def read_count(prompt):
    response = input(prompt).strip()
    if not response.isdigit() or int(response) <= 0:
        raise ValueError("Please enter a positive integer")
    return int(response)


# Generate n random integers in the range [min_val, max_val].
def generate_random_numbers(n, min_val, max_val):
    numbers = []
    for i in range(n):
        numbers.append(random.randint(min_val, max_val))
    return numbers


# Builds one bucket label for a number using the given bucket width.
def bucket_label(value, width):
    start = (value // width) * width
    end = start + width - 1
    return f"{start}-{end}"


# Groups numbers into buckets and stores each number with its bucket label.
def classify_numbers(numbers, width):
    buckets = {}
    for number in numbers:
        label = bucket_label(number, width)
        if label not in buckets:
            buckets[label] = []
        buckets[label].append(number)
    return buckets


# Extracts the bucket start value from a label like "20-29".
def bucket_start(label):
    return int(label.split("-")[0])


# Reads n, generates random numbers, classifies them, and prints bucket distribution.
def main():
    n = read_count("How many random numbers? ")
    width = 10
    numbers = generate_random_numbers(n, 1, 99)
    buckets = classify_numbers(numbers, width)
    print(f"\nGenerated {n} random numbers in range [1, 99]")
    print(f"Numbers: {numbers}")
    print("\nBucket Distribution:\n")
    print("Bucket       Count    Contents")
    print("-" * 50)
    for label in sorted(buckets, key=bucket_start):
        count = len(buckets[label])
        content = buckets[label]
        print(f"{label:<12} {count:<8} {content}")


if __name__ == "__main__":
    main()
