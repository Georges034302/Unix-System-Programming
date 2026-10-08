#!/usr/bin/env python3
"""
Run a login lockout demo and print timestamped attempt logs.
Usage:
    python3 login_lockout.py
    Create a demo username and password, then enter login attempts.
    The demo allows up to 3 attempts and prints the log as JSON.
"""

import json
from datetime import datetime

MAX_LOGIN_ATTEMPTS = 3


def create_login_log(login_logs, username, status):
    timestamp = datetime.now().isoformat(timespec="seconds")
    updated_logs = login_logs.copy()
    attempt_number = len(updated_logs) + 1
    updated_logs[f"login_attempt_{attempt_number}"] = {
        "user": username,
        "timestamp": timestamp,
        "status": status,
    }
    return updated_logs


def login_lockout(username, password):
    login_logs = {}

    for attempt_number in range(1, MAX_LOGIN_ATTEMPTS + 1):
        entered_username = input("Username: ")
        entered_password = input("Password: ")
        login_succeeded = entered_username == username and entered_password == password
        status = "success" if login_succeeded else "failed"
        login_logs = create_login_log(login_logs, entered_username, status)

        if login_succeeded:
            print("Login successful.")
            return login_logs

        remaining = MAX_LOGIN_ATTEMPTS - attempt_number
        if remaining > 0:
            print(f"Invalid login. Attempts remaining: {remaining}")

    print("Account locked after too many failed attempts.")
    return login_logs

def main():
    username = input("Create demo username: ")
    password = input("Create demo password: ")
    login_logs = login_lockout(username, password)
    print("Login logs:")
    print(json.dumps(login_logs, indent=4))

if __name__ == "__main__":
    main()
