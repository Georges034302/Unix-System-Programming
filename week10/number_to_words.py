#!/usr/bin/env python3
import sys

ONES = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

TEENS = {
    10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
    15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"
}

TENS = {
    20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
    60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"
}

def two_digit_words(n):
    if n < 10:
        return ONES[n]

    if n in TEENS:
        return TEENS[n]

    if n % 10 == 0:
        return TENS[n]

    return f"{TENS[(n // 10) * 10]} {ONES[n % 10]}"

def number_to_words(n):
    if not 0 <= n <= 999:
        raise ValueError("Number must be between 0 and 999")

    if n < 100:
        return two_digit_words(n)

    hundreds = n // 100
    remainder = n % 100

    if remainder == 0:
        return f"{ONES[hundreds]} hundred"

    return f"{ONES[hundreds]} hundred {two_digit_words(remainder)}"

def main():
    for line in sys.stdin:
        for token in line.split():
            number = int(token)
            print(f"{number} -> {number_to_words(number)}")

if __name__ == "__main__":
    main()
