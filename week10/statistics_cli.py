#!/usr/bin/env python3
"""
Generate random numbers and compute statistics.
Usage:
    python3 statistics_cli.py [-t] [-m] [-s] [-n]
    Enter the first value, last value, and sample size when prompted.
    Use -t for total, -m for mean, -s for standard deviation, and -n for min/max.
    The -s flag requires a sample size of at least 2.
"""
import random
import statistics
import sys

# Generates size unique random integers in range [first, last].
def random_list(first, last, size):
    return random.sample(range(first, last + 1), size)

# Displays statistics based on flags: -t (total), -m (mean), -s (stdev), -n (min/max).
def show_stats(nums, flags):
    if "-t" in flags:
        print("Total =", sum(nums))
    if "-m" in flags:
        print(f"Mean  = {statistics.mean(nums):.2f}")
    if "-s" in flags:
        print(f"STDV  = {statistics.stdev(nums):.2f}")
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