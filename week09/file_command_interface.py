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

FILENAME = "data.txt"

op = input("Command (r/w/x): ")

while op != 'x':

    match op:

        case 'r':
            # check if file exists by attempting safe open mode
            h = open(FILENAME, 'a+')   # create file if not exists
            h.seek(0)                 # move pointer to beginning
            content = h.read()
            h.close()

            print("\n--- File Content ---")
            print(content)

        case 'w':
            s = input("Enter text: ")
            h = open(FILENAME, 'a')
            h.write(s + '\n')
            h.close()
            print("Line added.")

        case _:
            print("Unknown command!")

    op = input("\nCommand (r/w/x): ")

print("Exiting program.")
