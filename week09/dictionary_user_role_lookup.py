#!/usr/bin/env python3
"""
Look up and update user roles in a dictionary.
Demonstrates: dictionaries, access by key, update, iteration.
"""

# Each key is a username, each value is the role assigned to that user.
user_roles = {
    "george": "lecturer",
    "admin": "administrator",
    "guest": "viewer",
    "analyst": "staff",
}

# Print each username alongside its current role.
print("Original roles:")
for username in user_roles:
    print(f"  {username:10} -> {user_roles[username]}")

# Direct key access to retrieve a specific user's role.
lookup_user = "admin"
print(f"\nRole for {lookup_user}: {user_roles[lookup_user]}")

# Overwrite an existing role by reassigning its key.
user_roles["guest"] = "student"

# Print all roles again to reflect the update.
print("\nUpdated roles:")
for username in user_roles:
    print(f"  {username:10} -> {user_roles[username]}")
