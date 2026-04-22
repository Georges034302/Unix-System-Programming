#!/usr/bin/env python3
"""
Look up and update user roles in a dictionary.
Demonstrates: dictionaries, access by key, update, iteration.
"""

user_roles = {
    "george": "lecturer",
    "admin": "administrator",
    "guest": "viewer",
    "analyst": "staff",
}

print("Original roles:")
for username in user_roles:
    print(f"  {username:10} -> {user_roles[username]}")

lookup_user = "admin"
print(f"\nRole for {lookup_user}: {user_roles[lookup_user]}")

user_roles["guest"] = "student"

print("\nUpdated roles:")
for username in user_roles:
    print(f"  {username:10} -> {user_roles[username]}")
