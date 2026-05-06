#!/usr/bin/env python3
"""
Simple file command interface.

Commands:
r → read file content
w → write new line to file
x → exit program

Concepts:
- loops
- match-case
- file handling
- simple validation
"""

# Fixed filename used for all read/write operations.
FILENAME = "data.txt"

op = input("Command (r/w/x): ")

# Loop until user chooses exit command.
while op != 'x':

    match op:

        case 'r':
            # Open in append+read mode to create the file if it doesn't exist.
            h = open(FILENAME, 'a+')   # create file if not exists
            h.seek(0)                  # rewind pointer to beginning before reading
            content = h.read()
            h.close()

            print("\n--- File Content ---")
            print(content)

        case 'w':
            s = input("Enter text: ")
            # Open in append mode to add a new line without overwriting.
            h = open(FILENAME, 'a')
            h.write(s + '\n')  # write text followed by a newline
            h.close()
            print("Line added.")

        case _:
            print("Unknown command!")

    op = input("\nCommand (r/w/x): ")

print("Exiting program.")
