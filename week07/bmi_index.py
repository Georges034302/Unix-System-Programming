#!/usr/bin/env python3
"""
Calculate and classify body mass index (BMI).

Usage:
    python3 bmi_index.py
    Enter weight in kilograms and height in metres when prompted.
"""

weight = float(input("Weight (kg): "))  # Convert the entered weight to a number.
height = float(input("Height (m) : "))  # Convert the entered height to a number.

# --- Calculate ---
bmi = weight / (height ** 2)  # standard BMI formula: kg / m²

# --- Classify ---
if bmi < 18.5:
    category = "Underweight"  # BMI below 18.5.
elif bmi < 25.0:
    category = "Normal"  # BMI from 18.5 up to 25.
elif bmi < 30.0:
    category = "Overweight"  # BMI from 25 up to 30.
else:
    category = "Obese"  # BMI of 30 or higher.

# --- Output ---
print(f"BMI      : {bmi:.1f}")
print(f"Category : {category}")
