#!/usr/bin/env python3

# Read service name and integer status code from the user
service = input("Service name: ")
status_code = int(input("Status code: "))  # convert string input to integer

# match compares status_code against each case value
# only the matching case block executes — similar to switch in other languages
match status_code:
    case 200:
        meaning = "Running"
        note = "Service is healthy"
    case 301:
        meaning = "Restarting"
        note = "Service is being restarted"
    case 404:
        meaning = "Missing"
        note = "Service is not available"
    case 500:
        meaning = "Failed"
        note = "Service encountered an internal error"
    case _:
        # _ is the wildcard — matches any value not listed above
        meaning = "Unknown"
        note = "Unrecognised status code"

print("\n--- Service Status ---")
print(f"Service      : {service}")
print(f"Status code  : {status_code}")
print(f"Meaning      : {meaning}")
print(f"Note         : {note}")
