#!/usr/bin/env python3
import csv
import json

def frequency(char, text):
    return text.count(char)

def frequencies(text):
    data = {}

    for char in "aeiou":
        data[char] = frequency(char, text)

    return data

def print_frequencies(data):
    for key in data:
        print(f"{key} --> {data[key]}")

def save_to_txt(records, filename="vowels.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        for index, data in enumerate(records, start=1):
            file.write(f"Entry {index}\n")

            for key in data:
                file.write(f"{key} --> {data[key]}\n")

            file.write("\n")

def save_to_csv(records, filename="vowels.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Entry", "Vowel", "Frequency"])

        for index, data in enumerate(records, start=1):
            for key in data:
                writer.writerow([index, key, data[key]])

def save_to_json(records, filename="vowels.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=2)

def main():
    records = []
    text = input("string: ")

    while text != "*":
        data = frequencies(text.lower())
        records.append(data)
        print_frequencies(data)
        text = input("string: ")

    save_to_txt(records)
    save_to_csv(records)
    save_to_json(records)

    print("Saved to vowels.txt, vowels.csv, and vowels.json")

if __name__ == "__main__":
    main()
