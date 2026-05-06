#!/usr/bin/env python3
"""
Count unique printers from a structured jobs file.

Usage:
    python3 unique_printer_counter.py
    When prompted, enter the path to the jobs file (e.g. printer_jobs.txt).

Expected file format (comma-separated):
    PrinterName,JobSize,Username

Example:
    Printer_A,120,alice
    Printer_B,350,bob
    Printer_A,80,carol
"""

file_path = input("Enter the file path: ").strip()

try:
    with open(file_path, 'r') as file:
        printers = set()        # stores unique printer names only
        job_counts = {}         # maps each printer name to its total job count

        for line in file:
            line = line.strip()  # remove leading/trailing whitespace per line

            # skip empty lines
            if not line:
                continue

            # split structured record: Printer,Size,User
            fields = line.split(',')

            # ensure the record has at least 3 fields before accessing index 0
            if len(fields) >= 3:
                printer_name = fields[0].strip()  # trim spaces around printer name
                printers.add(printer_name)         # set ignores duplicate entries
                job_counts[printer_name] = job_counts.get(printer_name, 0) + 1  # increment job count

    print("\n--- Printer Summary ---")
    print(f"Number of printers = {len(printers)}")
    print("\nJobs per printer:")
    for printer in sorted(job_counts):
        print(f"  {printer:12} -> {job_counts[printer]} job(s)")

except FileNotFoundError:
    print("❌ The file was not found. Please check the file path.")
