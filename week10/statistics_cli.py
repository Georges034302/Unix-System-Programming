#!/usr/bin/env python3
"""
Generate random numbers and compute statistics.
Usage: python3 statistics_cli.py [-t] [-m] [-s] [-n]
Flags: -t (total), -m (mean), -s (standard deviation), -n (min/max)
Prompts for first, last, size then displays population and requested statistics.
"""
import random
import statistics
import sys

# Generates size unique random integers in range [first, last].
def random_list(first, last, size):
    if first > last:
        raise ValueError("first must be <= last")
    if size < 1:
        raise ValueError("size must be >= 1")
    if size > last - first + 1:
        raise ValueError("size is larger than the available range")
    # random.sample returns unique values.
    return random.sample(range(first, last + 1), size)

# Displays statistics based on flags: -t (total), -m (mean), -s (stdev), -n (min/max).
def show_stats(nums, flags):
    if "-t" in flags:
        print("Total =", sum(nums))
    if "-m" in flags:
        print(f"Mean  = {statistics.mean(nums):.2f}")
    if "-s" in flags:
        if len(nums) > 1:
            print(f"STDV  = {statistics.stdev(nums):.2f}")
        else:
            print("STDV  = N/A")
    if "-n" in flags:
        print("Min   =", min(nums))
        print("Max   =", max(nums))

# Reads first, last, size from stdin.
def read_population_input():
    return int(input("first: ")), int(input("last:  ")), int(input("size:  "))

# Reads input, generates population, shows results with flags from argv.
def main():
    flags = sys.argv[1:]
    first, last, size = read_population_input()
    nums = random_list(first, last, size)
    print("\nPopulation:", nums, "\n")
    show_stats(nums, flags)

if __name__ == "__main__":
    main()