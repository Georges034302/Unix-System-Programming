#!/usr/bin/env python3
# Count unique printers from printer_jobs.txt

file_path = input("Enter the file path: ").strip()

try:
    with open(file_path, 'r') as file:
        printers = set()   # stores unique printer names only

        for line in file:
            line = line.strip()

            # skip empty lines
            if not line:
                continue

            # split structured record: Printer,Size,User
            fields = line.split(',')

            # ensure the record has at least 3 fields
            if len(fields) >= 3:
                printer_name = fields[0].strip()
                printers.add(printer_name)

    print("\n--- Printer Summary ---")
    print("Unique printers:", sorted(printers))
    print(f"Number of printers = {len(printers)}")

except FileNotFoundError:
    print("❌ The file was not found. Please check the file path.")
