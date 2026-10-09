#!/usr/bin/env python3
"""
Check whether one entered email matches a pattern.

Usage:
    python3 email_validator.py
    Enter an email address when prompted.
"""

import re

# r keeps backslashes in the pattern for the regex engine.
# ^ matches the start of the email; $ matches its end.
# [...] matches one character from the listed letters, digits, or symbols.
# A-Z and a-z mean letter ranges; 0-9 means digits.
# + means one or more characters from the preceding character set.
# @ and . match those literal characters; \. makes the dot literal.
# {2,} means at least two letters for the ending.
# The hyphen at the end of [...] is treated as a literal hyphen.
pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

email = input("Email: ")

if re.match(pattern, email):
    print("Email matches the pattern.")
else:
    print("Email does not match the pattern.")
