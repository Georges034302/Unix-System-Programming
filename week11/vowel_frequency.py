#!/usr/bin/env python3
"""
Read text records from txt/csv/json files, count vowel frequencies, and save results.

Usage:
1. Run: python3 vowel_frequency.py
2. Enter input filename (.txt, .csv, or .json).
3. The script saves vowels.txt, vowels.csv, and vowels.json.
"""
import csv
import json
from pathlib import Path

# Counts occurrences of a single character in text.
def frequency(char, text):
    return text.count(char)

# Returns a dictionary of vowel frequencies for text.
def frequencies(text):
    data = {}
    for char in "aeiou":
        data[char] = frequency(char, text)
    return data

# Builds one analysis record from a text string.
def build_record(text):
    cleaned_text = text.strip()
    record = {"text": cleaned_text}
    record.update(frequencies(cleaned_text.lower()))
    return record

# Prints vowel frequencies to stdout.
def print_frequencies(data):
    print(f"text: {data['text']}")
    for key in "aeiou":
        print(f"{key} --> {data[key]}")

# Reads text records from a plain text file.
def load_from_txt(filename):
    texts = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            # Ignore completely blank lines in the text input file.
            if line.strip():
                texts.append(line.rstrip("\n"))

    return texts

# Reads text records from a CSV file.
def load_from_csv(filename):
    texts = []

    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            # Use the "text" column when available.
            if "text" in row and row["text"].strip():
                texts.append(row["text"].strip())

    return texts

# Reads text records from a JSON file.
def load_from_json(filename):
    texts = []

    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        # Accept either plain strings or dictionaries with a text field.
        if isinstance(item, str) and item.strip():
            texts.append(item.strip())
        elif isinstance(item, dict) and "text" in item and str(item["text"]).strip():
            texts.append(str(item["text"]).strip())

    return texts

# Loads input text records according to the file extension.
def load_texts(filename):
    extension = Path(filename).suffix.lower()

    if extension == ".txt":
        return load_from_txt(filename)
    if extension == ".csv":
        return load_from_csv(filename)
    if extension == ".json":
        return load_from_json(filename)

    raise ValueError("Unsupported input file type")

# Writes vowel frequency records to a text file.
def save_to_txt(records, filename="vowels.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        for index, data in enumerate(records, start=1):
            file.write(f"Entry {index}\n")
            file.write(f"text: {data['text']}\n")
            for key in "aeiou":
                file.write(f"{key} --> {data[key]}\n")
            file.write("\n")

# Writes vowel frequency records to a CSV file.
def save_to_csv(records, filename="vowels.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Entry", "Text", "a", "e", "i", "o", "u"])
        for index, data in enumerate(records, start=1):
            writer.writerow([
                index,
                data["text"],
                data["a"],
                data["e"],
                data["i"],
                data["o"],
                data["u"],
            ])

# Writes vowel frequency records to a JSON file.
def save_to_json(records, filename="vowels.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=2)

# Saves all output formats.
def save_results(records):
    save_to_txt(records)
    save_to_csv(records)
    save_to_json(records)

# Reads an input file, analyzes each text record, and saves the results.
def main():
    input_filename = input("Input file (.txt, .csv, .json): ").strip()
    texts = load_texts(input_filename)
    records = []

    for text in texts:
        data = build_record(text)
        print_frequencies(data)
        print()
        records.append(data)

    save_results(records)

    print("Saved to vowels.txt, vowels.csv, and vowels.json")

if __name__ == "__main__":
    main()
