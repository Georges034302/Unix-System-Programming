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

    for part in raw_text.split(","):  # Split input by comma delimiter
        part = part.strip()  # Remove leading/trailing whitespace
        if part:  # Only process non-empty strings
            values.append(float(part))  # Convert string to float number

    return values

# Writes float values to a binary file.
def write_floats_binary(filename, values):
    with open(filename, "wb") as file:  # "wb" = write in binary mode
        for value in values:
            # struct.pack("d", value) converts float to 8-byte binary representation
            # "d" format = double-precision float (64-bit IEEE 754 standard)
            file.write(struct.pack("d", value))

# Reads all float values from a binary file.
def read_floats_binary(filename):
    values = []

    with open(filename, "rb") as file:  # "rb" = read in binary mode
        while True:
            chunk = file.read(8)  # Read exactly 8 bytes (one float)
            if not chunk:  # If nothing read, we've reached end of file
                break
            # struct.unpack("d", chunk) returns a tuple; [0] extracts the first (only) element
            values.append(struct.unpack("d", chunk)[0])

    return values

# Runs the script.
def main():
    raw_text = input("Enter float values separated by commas: ").strip()  # Get input and trim whitespace
    values = parse_floats(raw_text)  # Parse comma-separated string into list of floats

    filename = "floats.bin"
    write_floats_binary(filename, values)  # Serialize floats to binary file
    loaded_values = read_floats_binary(filename)  # Deserialize binary file back to floats

    print(f"Saved {len(values)} values to {filename}")
    print("Read back values:")
    for value in loaded_values:  # Verify round-trip: written values match loaded values
        print(value)

if __name__ == "__main__":
    main()
