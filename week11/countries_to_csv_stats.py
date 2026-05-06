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

    with open(filename, "r", encoding="utf-8") as file:  # UTF-8 encoding for international characters
        for line in file:
            name = line.strip()  # Remove newline (\n) and whitespace from both ends
            if name:  # Skip empty lines
                countries.append(name)  # Add non-empty country name to list

    return countries

# Writes country stats to a CSV file.
def write_country_stats_csv(countries, filename):
    with open(filename, "w", newline="", encoding="utf-8") as file:  # newline="" prevents extra blank lines on Windows
        writer = csv.writer(file)  # Create CSV writer object for proper formatting
        writer.writerow(["country", "name_length", "first_letter"])  # Write header row

        for country in countries:
            writer.writerow([
                country,  # Country name
                len(country),  # Calculate name length (number of characters)
                country[0].upper(),  # Extract first character and convert to uppercase
            ])

# Reads CSV file with csv module and prints it in STDOUT.
def read_from_csv(filename):
    print("\nCountries stats table:")

    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)  # Parse CSV file into rows
        rows = list(reader)  # Convert reader to list to allow indexing
    # Format: :<42 = left-aligned in 42 chars; :>12 = right-aligned in 12 chars
    print(f"{rows[0][0]:<42} {rows[0][1]:>12} {rows[0][2]:>12}")  # Print header row with formatting
    print(f"{'-' * 42} {'-' * 12} {'-' * 12}")  # Print separator line with dashes

    for row in rows[1:]:  # Iterate over data rows (skip header at index 0)
        print(f"{row[0]:<42} {row[1]:>12} {row[2]:>12}")  # Print each country's stats with aligned columns

# Runs the script.
def main():
    input_file = "countries.txt"
    output_file = "countries_stats.csv"

    countries = read_countries(input_file)  # Load country names from text file
    write_country_stats_csv(countries, output_file)  # Analyze and save to CSV with stats
    read_from_csv(output_file)  # Read back and display formatted table

    print(f"Read {len(countries)} countries from {input_file}")
    print(f"Saved stats to {output_file}")

if __name__ == "__main__":
    main()
