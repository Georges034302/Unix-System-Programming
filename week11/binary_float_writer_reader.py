#!/usr/bin/env python3
"""
Write float values to a binary file, then read them back.

Usage:
1. Run: python3 binary_float_writer_reader.py
2. Enter float values separated by commas (example: 1.2, 3.5, 7).
3. The script saves floats.bin and prints loaded values.
"""
import struct

# Parses comma-separated numbers from user input.
def parse_floats(raw_text):
    values = []

    for part in raw_text.split(","):
        part = part.strip()
        if part:
            values.append(float(part))

    return values

# Writes float values to a binary file.
def write_floats_binary(filename, values):
    with open(filename, "wb") as file:
        for value in values:
            # Format "d" stores one double-precision float (8 bytes).
            file.write(struct.pack("d", value))

# Reads all float values from a binary file.
def read_floats_binary(filename):
    values = []

    with open(filename, "rb") as file:
        while True:
            chunk = file.read(8)
            if not chunk:
                break
            values.append(struct.unpack("d", chunk)[0])

    return values

# Runs the script.
def main():
    raw_text = input("Enter float values separated by commas: ").strip()
    values = parse_floats(raw_text)

    filename = "floats.bin"
    write_floats_binary(filename, values)
    loaded_values = read_floats_binary(filename)

    print(f"Saved {len(values)} values to {filename}")
    print("Read back values:")
    for value in loaded_values:
        print(value)

if __name__ == "__main__":
    main()
