#!/usr/bin/env python3

import re

text = input("Text: ")

# --- Mask sensitive values ---
# each re.sub replaces all matches of a pattern with a placeholder

text = re.sub(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", "[EMAIL-HIDDEN]", text)  # email addresses
text = re.sub(r"\b\d{1,3}(?:\.\d{1,3}){3}\b", "[IP-HIDDEN]", text)                        # IPv4 addresses
text = re.sub(r"\b\d{4,}\b", "[ID-HIDDEN]", text)                                          # numeric IDs (4+ digits)

# --- Output ---
print(f"Masked : {text}")
