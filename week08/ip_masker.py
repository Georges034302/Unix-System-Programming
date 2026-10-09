#!/usr/bin/env python3
"""
Replace an entered IP address with a fixed mask.

Usage:
    python3 ip_masker.py
    Enter an IP address when prompted; the script prints the masked address.
"""

import re

ip_address = input("IP address: ").strip()  # Read the address and remove surrounding spaces.

# \d matches a digit.
# + means one or more of the previous item.
# \. matches a literal dot.
# The pattern matches four groups of digits separated by dots.
pattern = r"\d+\.\d+\.\d+\.\d+"

masked_ip = re.sub(pattern, "255.225.255.255", ip_address)  # Replace a matching address with the mask.

print(f"Masked IP: {masked_ip}")  # Display the result.
