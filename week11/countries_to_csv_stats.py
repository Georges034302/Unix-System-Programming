#!/usr/bin/env python3
"""
Read countries from countries.txt and write a simple CSV stats report.

Usage:
1. Put country names in countries.txt (one country per line).
2. Run: python3 countries_to_csv_stats.py
3. The script creates countries_stats.csv and prints its rows.
"""
import csv

# Reads country names from a text file.
def read_countries(filename):
    countries = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            name = line.strip()
            if name:
                countries.append(name)

    return countries

# Writes country stats to a CSV file.
def write_country_stats_csv(countries, filename):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["country", "name_length", "first_letter"])

        for country in countries:
            writer.writerow([
                country,
                len(country),
                country[0].upper(),
            ])

# Reads CSV file with csv module and prints it in STDOUT.
def read_from_csv(filename):
    print("\nCountries stats table:")

    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        rows = list(reader)
    # Fixed-width f-string columns keep output aligned in most terminals.
    print(f"{rows[0][0]:<42} {rows[0][1]:>12} {rows[0][2]:>12}")
    print(f"{'-' * 42} {'-' * 12} {'-' * 12}")

    for row in rows[1:]:
        print(f"{row[0]:<42} {row[1]:>12} {row[2]:>12}")

# Runs the script.
def main():
    input_file = "countries.txt"
    output_file = "countries_stats.csv"

    countries = read_countries(input_file)
    write_country_stats_csv(countries, output_file)
    read_from_csv(output_file)

    print(f"Read {len(countries)} countries from {input_file}")
    print(f"Saved stats to {output_file}")

if __name__ == "__main__":
    main()
