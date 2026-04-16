#!/usr/bin/env python3

weight = float(input("Weight (kg): "))
height = float(input("Height (m) : "))

# --- Calculate ---
bmi = weight / (height ** 2)  # standard BMI formula: kg / m²

# --- Classify ---
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25.0:
    category = "Normal"
elif bmi < 30.0:
    category = "Overweight"
else:
    category = "Obese"

# --- Output ---
print(f"BMI      : {bmi:.1f}")
print(f"Category : {category}")
