#!/usr/bin/env python3
import random
import statistics
import sys

def random_list(first, last, size):
    if first > last:
        raise ValueError("first must be <= last")

    if size < 1:
        raise ValueError("size must be >= 1")

    if size > last - first + 1:
        raise ValueError("size is larger than the available range")

    return random.sample(range(first, last + 1), size)

def show_stats(nums, flags):
    print("List:", nums)

    if "-t" in flags:
        print("Total =", sum(nums))

    if "-m" in flags:
        print(f"Mean = {statistics.mean(nums):.2f}")

    if "-s" in flags:
        if len(nums) > 1:
            print(f"STDV = {statistics.stdev(nums):.2f}")
        else:
            print("STDV = N/A")

    if "-n" in flags:
        print("Min =", min(nums))
        print("Max =", max(nums))

def main():
    if len(sys.argv) < 4:
        print("Usage: python stats.py <first> <last> <size> [-t] [-m] [-s] [-n]")
        sys.exit(1)

    try:
        first = int(sys.argv[1])
        last = int(sys.argv[2])
        size = int(sys.argv[3])
        flags = sys.argv[4:]

        nums = random_list(first, last, size)
        show_stats(nums, flags)

    except ValueError as error:
        print("Error:", error)
        sys.exit(1)

if __name__ == "__main__":
    main()
