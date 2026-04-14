#!/usr/bin/env python3

correct_user = "student"  # expected username
correct_pass = "unix123"  # expected password

username = input("Username: ")
password = input("Password: ")

# and requires both conditions to be True
if username == correct_user and password == correct_pass:
    print("Login successful")
elif username == correct_user:   # right user, wrong password
    print("Incorrect password")
elif password == correct_pass:   # right password, wrong user
    print("Incorrect username")
else:                            # both wrong
    print("Invalid username and password")
