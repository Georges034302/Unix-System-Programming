#!/usr/bin/env python3
"""
Count vowel frequencies in text strings and save results.
Usage: python3 vowel_frequency.py
Reads strings, counts a/e/i/o/u frequencies, saves to txt/csv/json (enter '*' to exit).
"""
import csv
import json

# Counts occurrences of a single character in text.
def frequency(char, text):
    return text.count(char)

# Returns a dictionary of vowel frequencies for text.
def frequencies(text):
    data = {}
    for char in "aeiou":
        data[char] = frequency(char, text)
    return data

# Prints vowel frequencies to stdout.
def print_frequencies(data):
    for key in data:
        print(f"{key} --> {data[key]}")

# Writes vowel frequency records to a text file.
def save_to_txt(records, filename="vowels.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        for index, data in enumerate(records, start=1):
            file.write(f"Entry {index}\n")
            for key in data:
                file.write(f"{key} --> {data[key]}\n")
            file.write("\n")

# Prompts for strings, collects vowel frequencies, saves to files until '*' entered.
def main():
    records = []
    text = input("string: ")
    while text != "*":
        data = frequencies(text.lower())
        records.append(data)
        print_frequencies(data)
        text = input("string: ")
    save_to_txt(records)
    print("Saved to vowels.txt, vowels.csv, and vowels.json")

if __name__ == "__main__":
    main()
