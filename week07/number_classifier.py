#!/usr/bin/env python3

n = int(input("Number: "))

# --- Sign ---
if n > 0:
    sign = "Positive"
elif n < 0:
    sign = "Negative"
else:
    sign = "Zero"

# --- Parity ---
# % returns the remainder; if remainder after dividing by 2 is 0, the number is even
parity = "Even" if n % 2 == 0 else "Odd"

# --- Divisibility ---
div3  = "Yes" if n % 3  == 0 else "No"
div5  = "Yes" if n % 5  == 0 else "No"
div10 = "Yes" if n % 10 == 0 else "No"

# --- Size ---
# abs() handles negatives so -500 is classified the same as 500
abs_n = abs(n)
if abs_n < 10:
    size = "Single digit"
elif abs_n < 100:
    size = "Double digit"
elif abs_n < 1000:
    size = "Triple digit"
else:
    size = "Large"

# --- Output ---
print(f"Sign      : {sign}")
print(f"Parity    : {parity}")
print(f"Div by 3  : {div3}")
print(f"Div by 5  : {div5}")
print(f"Div by 10 : {div10}")
print(f"Size      : {size}")
