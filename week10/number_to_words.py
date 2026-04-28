#!/usr/bin/env python3
"""
Transform numbers to English words in a text file.
Usage: python3 number_to_words.py input.txt
Output: output.txt with numbers 0-999 converted to words, others unchanged.
"""
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

# Converts numbers 0-99 to English words.
def two_digit_words(n):
    if n < 10:
        return ONES[n]
    if n in TEENS:
        return TEENS[n]
    if n % 10 == 0:
        return TENS[n]
    return f"{TENS[(n // 10) * 10]} {ONES[n % 10]}"

# Converts numbers 0-999 to English words.
def number_to_words(n):
    if n < 100:
        return two_digit_words(n)
    hundreds = n // 100
    remainder = n % 100
    if remainder == 0:
        return f"{ONES[hundreds]} hundred"
    return f"{ONES[hundreds]} hundred and {two_digit_words(remainder)}"

# Transforms tokens in a line: numbers 0-999 to words, others unchanged.
def transform_line(line):
    transformed_tokens = []
    for token in line.split():
        if token.isdigit():
            number = int(token)
            if number <= 999:
                transformed_tokens.append(number_to_words(number))
            else:
                transformed_tokens.append(token)
        else:
            transformed_tokens.append(token)
    return " ".join(transformed_tokens)


# Transforms numbers 0-999 to words in a file, writes to output.txt.
def transform_file(filename):
    output_filename = "output.txt"
    
    with open(filename, "r") as f_in:
        with open(output_filename, "w") as f_out:
            for line in f_in:
                transformed = transform_line(line)
                f_out.write(transformed + "\n")


# Main entry point.
def main():
    filename = sys.argv[1]
    transform_file(filename)

if __name__ == "__main__":
    main()
