#!/usr/bin/env python3

# Simple Interest  : earned only on the original principal  →  SI = P × r × t
# Compound Interest: earned on principal + previously earned interest → CI = P(1+r)^t - P
#   used in savings accounts, investments, and loans — interest builds on itself over time,
#   meaning money grows faster the longer it is left; also why debt grows quickly if unpaid.
# Compound always >= simple; the gap grows larger over time

principal = float(input("Principal ($)  : "))
rate      = float(input("Annual rate (%) : ")) / 100  # convert % to decimal
years     = float(input("Years           : "))

# --- Calculate ---
simple   = principal * rate * years                   # SI  = P × r × t
compound = principal * (1 + rate) ** years - principal  # CI = P(1 + r)^t - P

total_simple   = principal + simple    # total amount after simple interest
total_compound = principal + compound  # total amount after compound interest

difference = total_compound - total_simple  # compound always >= simple

# --- Classify ---
if difference < 10:
    verdict = "nearly the same"
elif difference < 500:
    verdict = "moderately more with compound"
else:
    verdict = "significantly more with compound"

# --- Output ---
print(f"\nSimple interest   : ${simple:.2f}  (total: ${total_simple:.2f})")
print(f"Compound interest : ${compound:.2f}  (total: ${total_compound:.2f})")
print(f"Difference        : ${difference:.2f} — {verdict}")
