#!/usr/bin/env python3
"""
Remove duplicate usernames and perform membership checks.
Demonstrates: sets, uniqueness, membership testing.
"""

# Raw list preserving all login events including duplicates.
login_attempts = [
    "george", "admin", "guest", "george", "admin", "analyst", "guest"
]

# Convert to set to automatically discard duplicate usernames.
unique_users = set(login_attempts)

print("Login attempts  :", login_attempts)
print("Unique users    :", unique_users)
print(f"User count      : {len(unique_users)}")
print(f"Contains admin? : {'admin' in unique_users}")  # O(1) membership check
print(f"Contains root?  : {'root' in unique_users}")   # O(1) membership check
