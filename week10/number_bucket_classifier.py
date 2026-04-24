#!/usr/bin/env python3
import sys

def bucket_label(value, width):
    start = (value // width) * width
    end = start + width - 1
    return f"{start}-{end}"

def classify_numbers(numbers, width):
    buckets = {}

    for number in numbers:
        label = bucket_label(number, width)
        buckets[label] = buckets.get(label, 0) + 1

    return buckets

def read_numbers():
    numbers = []

    for line in sys.stdin:
        for token in line.split():
            numbers.append(int(token))

    return numbers

def main():
    width = 10

    if len(sys.argv) > 1:
        width = int(sys.argv[1])

    buckets = classify_numbers(read_numbers(), width)

    for label in sorted(buckets, key=lambda x: int(x.split("-")[0])):
        print(f"{label} -> {buckets[label]}")

if __name__ == "__main__":
    main()
