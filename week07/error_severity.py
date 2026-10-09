#!/usr/bin/env python3
"""
Label an error severity and suggest an action.

Usage:
    python3 error_severity.py
    Enter an error title and a severity from 1 to 5.
"""

# Read error details from the user
title = input("Error title: ")  # Read a short description of the error.
severity = int(input("Severity (1-5): "))  # Convert the entered severity to an integer.

# Cascaded if-elif-else maps each severity level to a label and recommended action
# Each elif is only reached if all previous conditions were False
if severity == 1:
    label = "INFO"
    action = "Ignore for now"
elif severity == 2:
    label = "LOW"
    action = "Monitor the situation"
elif severity == 3:
    label = "WARNING"
    action = "Investigate soon"
elif severity == 4:
    label = "ERROR"
    action = "Investigate immediately"
elif severity == 5:
    label = "CRITICAL"
    action = "Escalate now"
else:
    # else catches any value outside 1-5
    label = "UNKNOWN"
    action = "Invalid severity value"

print("\n--- Severity Report ---")
print(f"Title    : {title}")
print(f"Severity : {severity}")
print(f"Label    : {label}")
print(f"Action   : {action}")
