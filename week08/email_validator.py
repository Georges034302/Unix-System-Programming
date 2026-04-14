#!/usr/bin/env python3

import re

# local@domain.ext — letters/digits/symbols before @, domain, then 2+ letter extension
pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

valid_count = invalid_count = 0

email = input("Email (or STOP): ")

while email != "STOP":
    if re.match(pattern, email):  # re.match checks from the start of the string
        print(f"{email} -> valid")
        valid_count += 1
    else:
        print(f"{email} -> invalid")
        invalid_count += 1
    email = input("Email (or STOP): ")

# --- Summary ---
print(f"\nValid   : {valid_count}")
print(f"Invalid : {invalid_count}")
