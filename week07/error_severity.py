#!/usr/bin/env python3

# Read error details from the user
title = input("Error title: ")
severity = int(input("Severity (1-5): "))  # convert string input to integer

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
