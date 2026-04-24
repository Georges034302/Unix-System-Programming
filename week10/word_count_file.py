#!/usr/bin/env python3
import sys

def append_file(filename):
    print(f"Appending to {filename}. Type q to stop.")

    with open(filename, "a", encoding="utf-8") as file:
        while True:
            line = input()

            if line.lower() == "q":
                break

            file.write(line + "\n")

def show_content(filename):
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")

def word_count(filename):
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    return len(text.split())

def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python fileops.py -a <file>")
        print("  python fileops.py -s <file>")
        print("  python fileops.py -c <file>")
        sys.exit(1)

    op = sys.argv[1]
    filename = sys.argv[2]

    match op:
        case "-a":
            append_file(filename)
        case "-s":
            show_content(filename)
        case "-c":
            print("Word count =", word_count(filename))
        case _:
            print("Invalid option.")

if __name__ == "__main__":
    main()
