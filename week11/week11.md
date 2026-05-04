# Week 11 — Files and Filesystem Access in Python

## Table of Contents
1. [Files and Filesystem Access in Python](#1-files-and-filesystem-access-in-python)
    - [1.1 Why Files Matter](#11-why-files-matter)
    - [1.2 File Objects and Opening Files](#12-file-objects-and-opening-files)
    - [1.3 File Modes](#13-file-modes)

2. [Reading Text Files](#2-reading-text-files)
    - [2.1 Reading a File Line by Line](#21-reading-a-file-line-by-line)
    - [2.2 Reading an Entire File at Once](#22-reading-an-entire-file-at-once)
    - [2.3 Working with Newlines and Text Content](#23-working-with-newlines-and-text-content)

3. [Writing Text Files](#3-writing-text-files)
    - [3.1 Writing and Overwriting Files](#31-writing-and-overwriting-files)
    - [3.2 Appending and Creating Files](#32-appending-and-creating-files)
    - [3.3 Converting Data Before Writing](#33-converting-data-before-writing)

4. [Binary Data in Python](#4-binary-data-in-python)
    - [4.1 Text Files vs Binary Files](#41-text-files-vs-binary-files)
    - [4.2 bytes and bytearray](#42-bytes-and-bytearray)
    - [4.3 Encoding and Decoding Data](#43-encoding-and-decoding-data)

5. [Structured Binary Files](#5-structured-binary-files)
    - [5.1 Writing Binary Data with struct.pack](#51-writing-binary-data-with-structpack)
    - [5.2 Reading Binary Data with struct.unpack](#52-reading-binary-data-with-structunpack)
    - [5.3 Fixed-Length Records](#53-fixed-length-records)

6. [File Positioning and Random Access](#6-file-positioning-and-random-access)
    - [6.1 The seek Function](#61-the-seek-function)
    - [6.2 Offsets and Record Sizes](#62-offsets-and-record-sizes)
    - [6.3 Accessing Specific Records](#63-accessing-specific-records)

7. [Managing File Access Errors](#7-managing-file-access-errors)
    - [7.1 Using try and except](#71-using-try-and-except)
    - [7.2 Testing Before Access](#72-testing-before-access)
    - [7.3 Common File Access Checks](#73-common-file-access-checks)

8. [Working with Directories](#8-working-with-directories)
    - [8.1 Listing Directory Contents](#81-listing-directory-contents)
    - [8.2 Changing the Current Directory](#82-changing-the-current-directory)
    - [8.3 Exploring Directory Trees](#83-exploring-directory-trees)

9. [Practical Applications and Use Cases](#9-practical-applications-and-use-cases)
    - [9.1 Safe Text File Processing](#91-safe-text-file-processing)
    - [9.2 CSV File Processing](#92-csv-file-processing)
    - [9.3 JSON File Processing](#93-json-file-processing)
    - [9.4 Binary Record Storage and Retrieval](#94-binary-record-storage-and-retrieval)
    - [9.5 Recursive Directory Traversal](#95-recursive-directory-traversal)

---

# 1. Files and Filesystem Access in Python

Programs often need data that continue to exist after the program ends. This persistent data is usually stored in files inside the filesystem.

Python can read files, write files, and inspect directories. These operations are essential in systems programming because logs, configuration files, reports, and binary records are all stored on disk.

In practice, working with files means moving data between Python objects in memory and named paths in the filesystem. A program opens a path, gets a file object, performs operations through that object, and then closes it when the work is finished.

## 1.1 Why Files Matter

Files allow programs to store information between executions.

Without files, every result would disappear as soon as the program stops. With files, a script can save data, reload it later, and share it with other programs.

### Example 1

```python
# Read a saved username from a small text file.
def load_username(filename):
    with open(filename, "r", encoding="utf-8") as file:
        # strip removes the trailing newline from the stored name.
        return file.readline().strip()

print(load_username("user.txt"))
```

This example shows that a program can recover previously stored information from disk.

### Example 2

```python
# Save one status message so it can be checked later.
def save_status(filename, message):
    with open(filename, "w", encoding="utf-8") as file:
        # write stores the exact string in the file.
        file.write(message)

save_status("status.txt", "service started")
```

This function shows the opposite direction: the program creates persistent output instead of only printing to the screen.

## 1.2 File Objects and Opening Files

Before Python can use a file, it must open that file. The `open()` function creates a file object, and that object gives the program methods for reading or writing.

The file path may be absolute or relative. Once the file object exists, the program can interact with the file through that object. The file object also remembers important state such as the access mode and the current read/write position.

### Example 1

```python
# Open a file for reading and print the first line.
def show_first_line(path):
    file = open(path, "r", encoding="utf-8")
    # readline reads one line from the current file position.
    line = file.readline()
    file.close()
    return line.strip()

print(show_first_line("notes.txt"))
```

This example uses `open()` directly and closes the file manually after reading.

### Example 2

```python
# Open a file with a context manager for safer cleanup.
def count_characters(path):
    with open(path, "r", encoding="utf-8") as file:
        # read returns the full text content as one string.
        content = file.read()
    return len(content)

print(count_characters("notes.txt"))
```

The `with` statement is useful because the file is closed automatically when the block finishes.

## 1.3 File Modes

The mode passed to `open()` tells Python how the file will be used.

The most common text-file modes are shown below. Modes with `+` allow both reading and writing.

| Mode | Description |
| --- | --- |
| `"r"` | Open an existing file for reading only. Fails if the file does not exist. |
| `"r+"` | Open an existing file for both reading and writing. Fails if the file does not exist. |
| `"w"` | Open a file for writing only. Creates the file if needed and overwrites existing content. |
| `"w+"` | Open a file for both reading and writing. Creates the file if needed and overwrites existing content. |
| `"a"` | Open a file for appending only. Creates the file if needed and writes at the end. |
| `"a+"` | Open a file for both reading and appending. Creates the file if needed and writes at the end. |

Other useful mode flags include `"x"` for exclusive file creation, `"b"` for binary mode, and `"t"` for text mode. Text mode is the default.

The choice of mode affects both safety and behaviour. For example, `"w"` and `"w+"` can destroy old content immediately, while `"a"` and `"a+"` preserve old content and place new writes at the end of the file.

### Example 1

```python
# Overwrite a file with fresh report text.
def write_report(path, text):
    with open(path, "w", encoding="utf-8") as file:
        # Mode "w" clears previous content before writing.
        file.write(text)

write_report("report.txt", "Daily summary\n")
```

Mode `"w"` is useful when the program should replace old content completely.

### Example 2

```python
# Append one extra log line without removing old ones.
def append_log(path, message):
    with open(path, "a", encoding="utf-8") as file:
        # Add a newline so each message stays on its own line.
        file.write(message + "\n")

append_log("system.log", "backup finished")
```

Mode `"a"` is suitable when the file should grow over time, such as a log file.

---

# 2. Reading Text Files

Text files are the most common kind of file used in beginner programs. Python makes them easy to process either line by line or all at once.

The main design choice is whether the program should stream the file gradually or load it completely into memory. Small files are often convenient to read all at once, while larger files are usually better processed one line at a time.

## 2.1 Reading a File Line by Line

Reading line by line is efficient and easy to understand. It is especially useful when the file may contain many lines.

### Example 1

```python
# Print each line after removing the final newline character.
def show_clean_lines(path):
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            # rstrip removes the trailing newline from each line.
            print(line.rstrip())

show_clean_lines("food.txt")
```

This follows the common pattern of iterating through a file object directly.

### Example 2

```python
# Count how many non-empty lines appear in a file.
def count_non_empty_lines(path):
    total = 0

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            # strip removes spaces and newline before the emptiness check.
            if line.strip():
                total += 1

    return total

print(count_non_empty_lines("food.txt"))
```

This style is common in log processing and simple file analysis tasks.

## 2.2 Reading an Entire File at Once

Python can also read all file contents in one operation with `read()`. This is convenient when the file is small enough to fit comfortably in memory.

### Example 1

```python
# Read the full file into one string and return it.
def load_text(path):
    with open(path, "r", encoding="utf-8") as file:
        # read consumes the whole remaining file.
        return file.read()

text = load_text("food.txt")
print(text)
```

This is compact and useful for smaller files or when the whole text is needed at once.

### Example 2

```python
# Show the raw text representation and its total length.
def inspect_text(path):
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()

    print(repr(content))
    print(len(content))

inspect_text("food.txt")
```

Using `repr()` makes newline characters visible, which helps explain exactly what was read.

## 2.3 Working with Newlines and Text Content

When text is read from a file, each line usually ends with a newline character. Programs often need to remove or preserve that newline depending on the task.

This is why printing file lines directly can sometimes produce unexpected blank lines: the line already contains `\n`, and `print()` adds another newline of its own.

### Example 1

```python
# Return lines without their trailing newline characters.
def get_clean_lines(path):
    cleaned = []

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            # rstrip keeps the content but removes the line ending.
            cleaned.append(line.rstrip())

    return cleaned

print(get_clean_lines("food.txt"))
```

This is useful when the lines will be compared, stored in a list, or shown without extra blank lines.

### Example 2

```python
# Split full text into lines after reading the complete file.
def load_lines(path):
    with open(path, "r", encoding="utf-8") as file:
        text = file.read()

    # splitlines handles different line-ending styles safely.
    return text.splitlines()

print(load_lines("food.txt"))
```

This approach is helpful when one operation needs the whole file first and later wants line-based processing.

---

# 3. Writing Text Files

Writing files allows a program to save results, logs, reports, and transformed content for future use.

## 3.1 Writing and Overwriting Files

Opening a file with mode `"w"` creates a writable file and clears previous contents if the file already exists.

### Example 1

```python
# Write a list of names into a file, one per line.
def write_names(path, names):
    with open(path, "w", encoding="utf-8") as file:
        for name in names:
            # Add newline so each item appears on a separate line.
            file.write(name + "\n")

write_names("names.txt", ["Ali", "Mina", "Ravi"])
```

This example builds a fresh text file from a Python list.

### Example 2

```python
# Replace simple HTML paragraph tags while copying a file.
import re

def convert_paragraphs(source_path, target_path):
    with open(source_path, "r", encoding="utf-8") as fin:
        with open(target_path, "w", encoding="utf-8") as fout:
            for line in fin:
                # Replace opening paragraph tags with line breaks.
                line = re.sub("<p>", "<br>", line)
                # Remove closing paragraph tags completely.
                line = re.sub("</p>", "", line)
                fout.write(line)

convert_paragraphs("input.html", "output.html")
```

This shows a practical transformation pipeline where a file is read, modified, and written out again.

## 3.2 Appending and Creating Files

Appending adds data to the end of an existing file. Creating with `"x"` is stricter because it fails if the file already exists.

### Example 1

```python
# Append one event to a log file.
def record_event(path, event):
    with open(path, "a", encoding="utf-8") as file:
        # Each event is stored on its own line.
        file.write(event + "\n")

record_event("events.log", "user login")
```

Appending is the normal choice for logs, journals, and growing histories.

### Example 2

```python
# Create a file only if it does not already exist.
def create_config_stub(path):
    with open(path, "x", encoding="utf-8") as file:
        # Store minimal starter content for the new file.
        file.write("host=localhost\nport=8080\n")

create_config_stub("service.conf")
```

Mode `"x"` is useful when overwriting an existing file would be a mistake.

## 3.3 Converting Data Before Writing

Text files store strings, so non-string values must usually be converted before writing.

### Example 1

```python
# Write numeric output after converting it to text.
def save_number(path, number):
    with open(path, "w", encoding="utf-8") as file:
        # str converts the number into writable text form.
        file.write(str(number))

save_number("number.txt", 273.91)
```

This is necessary because `write()` expects a string in text mode.

### Example 2

```python
# Save a mixed list by converting the whole object to a string.
def save_list(path, values):
    with open(path, "w", encoding="utf-8") as file:
        # The list is rendered as text before writing.
        file.write(str(values))

save_list("items.txt", [123, "abc", True])
```

The data are stored as text, which is easy to inspect even if it is not a strict data-exchange format.

---

# 4. Binary Data in Python

Not all files are text files. Many programs need binary data, where values are stored in the machine-oriented format used by the computer.

Binary files are especially useful when exact size matters. Unlike text, binary storage can keep numbers and fixed-width records in predictable byte layouts that are easy for programs to read back efficiently.

## 4.1 Text Files vs Binary Files

A text file stores readable characters, while a binary file stores raw bytes. Binary files are useful for compact storage, fixed-size records, and non-text data.

### Example 1

```python
# Write text digits to a text file.
def save_text_number(path, value):
    with open(path, "w", encoding="utf-8") as file:
        # The number is stored as visible characters.
        file.write(str(value))

save_text_number("value.txt", 1.235)
```

In a text file, the number appears as characters that a human can read directly.

### Example 2

```python
# Write one floating-point value as raw binary bytes.
import struct

def save_binary_number(path, value):
    with open(path, "wb") as file:
        # Format "d" stores one double-precision float.
        file.write(struct.pack("d", value))

save_binary_number("value.bin", 1.235)
```

This binary file is not human-readable, but it stores the value in a compact machine format.

## 4.2 bytes and bytearray

Python provides two main binary sequence types: `bytes`, which is immutable, and `bytearray`, which is mutable.

### Example 1

```python
# Create immutable bytes from a text string.
def make_bytes(text):
    # utf-8 converts the string to a byte sequence.
    return bytes(text, "utf-8")

print(make_bytes("unix"))
```

`bytes` is useful when the binary data should not be changed after creation.

### Example 2

```python
# Change one byte inside a mutable bytearray.
def update_first_byte(text):
    data = bytearray(text, "utf-8")
    # Replace the first byte with uppercase A.
    data[0] = ord("A")
    return data

print(update_first_byte("admin"))
```

This example demonstrates that `bytearray` can be modified in place.

## 4.3 Encoding and Decoding Data

Strings must be encoded to bytes before they are written to a binary file. Later, bytes can be decoded back into strings.

Encoding answers the question, "How should these characters be represented as bytes?" Decoding answers the reverse question, "How should these bytes be interpreted as characters?"

### Example 1

```python
# Encode a username before storing it as binary data.
def encode_username(username):
    # encode returns bytes in the requested character encoding.
    return username.encode("utf-8")

print(encode_username("nadia"))
```

Encoding translates text into the byte representation required by binary files.

### Example 2

```python
# Decode bytes back into a normal Python string.
def decode_username(data):
    # decode reverses the earlier text-to-bytes conversion.
    return data.decode("utf-8")

print(decode_username(b"nadia"))
```

Decoding is essential when binary data must become readable text again.

---

# 5. Structured Binary Files

Binary files become especially useful when a program stores repeated records with fixed sizes. Python's `struct` module helps pack values into binary form and unpack them later.

The format string is the contract between writing and reading. If the write format and read format do not match, the unpacked data will be incorrect or the read will fail.

## 5.1 Writing Binary Data with struct.pack

`struct.pack()` converts Python values into a sequence of bytes according to a format string.

### Example 1

```python
# Write one floating-point value to a binary file.
import struct

def write_score(path, score):
    with open(path, "wb") as file:
        # "d" means one double-precision floating-point number.
        file.write(struct.pack("d", score))

write_score("test.bin", 273.91)
```

This is the simplest structured binary write: one value, one format code.

### Example 2

```python
# Pack a username and balance into one binary record.
import struct

def write_account(path, username, balance):
    with open(path, "wb") as file:
        # "8sd" means 8-byte string followed by one double.
        packed = struct.pack("8sd", username.encode("utf-8"), balance)
        file.write(packed)

write_account("account.bin", "massimo", 1020.678)
```

Here the format string controls the exact byte layout of the stored record.

## 5.2 Reading Binary Data with struct.unpack

`struct.unpack()` reverses the packing process. It reads raw bytes and interprets them according to the same format string.

### Example 1

```python
# Read one binary floating-point value back from disk.
import struct

def read_score(path):
    with open(path, "rb") as file:
        # Read exactly 8 bytes for one double.
        data = file.read(8)
    return struct.unpack("d", data)[0]

print(read_score("test.bin"))
```

The format used for reading must match the format used for writing.

### Example 2

```python
# Read a fixed account record and decode the username field.
import struct

def read_account(path):
    with open(path, "rb") as file:
        data = file.read(16)

    username_bytes, balance = struct.unpack("8sd", data)
    # rstrip removes padding zero bytes from the fixed-width string.
    username = username_bytes.rstrip(b"\x00").decode("utf-8")
    return {"username": username, "balance": balance}

print(read_account("account.bin"))
```

This example shows how fixed-width strings often need cleanup after unpacking.

## 5.3 Fixed-Length Records

Fixed-length records give every stored item the same size. This makes random access much easier because the position of each record can be calculated directly.

### Example 1

```python
# Write one student record using fixed-width fields.
import struct

def write_student(path, login, first_name, last_name, score):
    with open(path, "wb") as file:
        record = struct.pack(
            "8s20s20sd",
            # Fixed-width string fields are encoded before packing.
            login.encode("utf-8"),
            first_name.encode("utf-8"),
            last_name.encode("utf-8"),
            score,
        )
        file.write(record)

write_student("students.bin", "john2012", "John", "Miller", 88.5)
```

The record size is fixed because each field has a fixed binary width.

### Example 2

```python
# Compute the size of one record from its format string.
import struct

def record_size():
    # calcsize returns the number of bytes required by the format.
    return struct.calcsize("8s20s20sd")

print(record_size())
```

Knowing the exact record size is essential for direct access later in the file.

---

# 6. File Positioning and Random Access

Sequential reading starts from the beginning and moves forward. Random access is different: the program jumps directly to a chosen location in the file.

This byte-level positioning matters most in binary files because each record can be placed at a known offset. Once the record size is known, the program can jump straight to the required data instead of scanning everything before it.

## 6.1 The seek Function

The `seek()` method changes the current file position. This allows a program to skip over data and read from an exact byte offset.

### Example 1

```python
# Skip the first 8 bytes, then read the next 8 bytes.
def read_second_number(path):
    with open(path, "rb") as file:
        # Move past the first stored double (8 bytes).
        file.seek(8, 0)
        return file.read(8)

print(read_second_number("numbers.bin"))
```

The second argument `0` means the offset is measured from the start of the file.

### Example 2

```python
# Ask seek for the final position after moving forward.
def move_and_report(path, offset):
    with open(path, "rb") as file:
        # seek returns the new byte position after moving.
        position = file.seek(offset, 0)
    return position

print(move_and_report("test.bin", 16))
```

This is useful when the program must confirm where it is inside the file.

## 6.2 Offsets and Record Sizes

When records all have the same length, the location of record `n` can be computed as:

```text
offset = n * record_size
```

This makes direct access predictable and efficient.

### Example 1

```python
# Calculate the byte offset of a chosen record index.
def record_offset(index, size):
    # Multiply the record number by the size of each record.
    return index * size

print(record_offset(6, 56))
```

If each record is 56 bytes, record index 6 starts 336 bytes from the beginning.

### Example 2

```python
# Jump to the start of one fixed-length record.
def go_to_record(file, index, size):
    # index * size gives the starting byte of the chosen record.
    file.seek(index * size, 0)

with open("test.bin", "rb") as file:
    go_to_record(file, 1, 56)
    print(file.tell())
```

This pattern is the basis of indexed access in simple binary storage systems.

## 6.3 Accessing Specific Records

Once the offset is known, a program can jump directly to a chosen record and read only that record.

### Example 1

```python
# Read one account record by its index in a binary file.
import struct

def read_record_at(path, index):
    size = struct.calcsize("8s20s20sd")

    with open(path, "rb") as file:
        # Move directly to the selected record.
        file.seek(index * size, 0)
        data = file.read(size)

    return struct.unpack("8s20s20sd", data)

print(read_record_at("test.bin", 1))
```

This avoids reading all earlier records when only one record is needed.

### Example 2

```python
# Read the second stored user and decode only selected fields.
import struct

def read_user_name_and_value(path):
    size = struct.calcsize("8s20s20sd")

    with open(path, "rb") as file:
        # The second record starts after one full record.
        file.seek(size, 0)
        login, first_name, last_name, value = struct.unpack(
            "8s20s20sd",
            file.read(size),
        )

    return {
        "login": login.rstrip(b"\x00").decode("utf-8"),
        "value": value,
    }

print(read_user_name_and_value("test.bin"))
```

This is a direct adaptation of the fixed-record idea from the lecture notes.

---

# 7. Managing File Access Errors

File operations can fail for many reasons. A file may not exist, the program may not have permission to access it, or the path may refer to the wrong type of object.

In practice, programs usually handle this in one of two ways: attempt the operation and catch the failure, or check the path first and continue only when it looks safe to do so.

## 7.1 Using try and except

One common method is to try the operation and handle the error if it happens.

### Example 1

```python
# Attempt to open a file and show a simple error message if it fails.
def safe_open_read(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except OSError as error:
        return f"Error opening file: {error}"

print(safe_open_read("inexistent_file"))
```

This approach is practical because it handles the failure exactly where it occurs.

### Example 2

```python
# Read lines or return an empty list when the file cannot be opened.
def safe_load_lines(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.readlines()
    except OSError:
        # Empty result is used here as a fallback value.
        return []

print(safe_load_lines("missing.txt"))
```

The caller can continue running even when the file is unavailable.

## 7.2 Testing Before Access

Another method is to check the path before trying the operation. The `os.path` and `os.access` functions are useful for these checks.

### Example 1

```python
# Open a file only if it exists and is readable.
import os

def read_if_possible(path):
    if os.path.exists(path) and os.access(path, os.R_OK):
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    return "Error: file reading not possible"

print(read_if_possible("notes.txt"))
```

This avoids a failed open when the path is clearly not suitable.

### Example 2

```python
# Check that a path points to a normal file before using it.
import os

def is_readable_file(path):
    # isfile rejects directories and special paths.
    return os.path.isfile(path) and os.access(path, os.R_OK)

print(is_readable_file("notes.txt"))
```

This check is useful when the program must distinguish files from directories.

## 7.3 Common File Access Checks

Common checks include whether a path exists, whether it is a file or directory, and whether the process has the right permissions.

### Example 1

```python
# Summarize several basic checks for one path.
import os

def inspect_path(path):
    return {
        "exists": os.path.exists(path),
        "is_file": os.path.isfile(path),
        "is_dir": os.path.isdir(path),
        "readable": os.access(path, os.R_OK),
    }

print(inspect_path("notes.txt"))
```

This produces a compact report about what the program can expect from the path.

### Example 2

```python
# Choose a message based on the path type.
import os

def describe_path(path):
    if not os.path.exists(path):
        return "path does not exist"
    if os.path.isdir(path):
        return "path is a directory"
    if os.path.isfile(path):
        return "path is a file"
    return "path exists but is not a normal file"

print(describe_path("notes.txt"))
```

This type of classification often appears before file-processing logic begins.

---

# 8. Working with Directories

Files live inside directories, so many systems programs must inspect directory contents, move between directories, or traverse a whole directory tree.

Directory functions usually work with names and paths rather than file contents. This makes them useful for inventory tasks such as listing, counting, searching, and recursive traversal.

## 8.1 Listing Directory Contents

Python provides `os.listdir()` to retrieve the entries inside a directory.

### Example 1

```python
# Return all directory entries as a list.
import os

def list_entries(path):
    # listdir returns names, not full paths.
    return os.listdir(path)

print(list_entries("."))
```

This is the simplest way to inspect what a directory contains.

### Example 2

```python
# Print one entry per line for easier viewing.
import os

def show_entries(path):
    entries = os.listdir(path)

    for entry in entries:
        # Printing one item at a time gives a simple ls-style view.
        print(entry)

show_entries(".")
```

Printing entries one by one is often easier to read than printing the full list at once.

## 8.2 Changing the Current Directory

The current working directory affects how relative paths are interpreted. Python can change it with `os.chdir()`.

### Example 1

```python
# Move into another directory, then report the new location.
import os

def change_and_report(path):
    os.chdir(path)
    # getcwd returns the absolute current working directory.
    return os.getcwd()

print(change_and_report("."))
```

This shows that changing directory affects later relative file operations.

### Example 2

```python
# Temporarily change directory to inspect a different location.
import os

def count_entries_in(path):
    original = os.getcwd()
    os.chdir(path)
    # Count entries relative to the new current directory.
    total = len(os.listdir("."))
    # Restore the original directory before leaving the function.
    os.chdir(original)
    return total

print(count_entries_in("."))
```

This keeps the directory change local to one function by restoring the original location afterward.

## 8.3 Exploring Directory Trees

A directory tree contains directories inside directories. Programs can explore the tree either with helpers such as `os.walk()` or with manual recursion.

### Example 1

```python
# Use os.walk to visit each directory in a tree.
import os

def show_tree(root_path):
    for current_path, directories, filenames in os.walk(root_path):
        # os.walk returns the current path plus child directories/files.
        print("Directory:", current_path)
        print("Subdirectories:", directories)
        print("Files:", filenames)

show_tree(".")
```

`os.walk()` is a convenient standard-library solution for full tree traversal.

### Example 2

```python
# Recursively visit subdirectories in a manual depth-first traversal.
import os

def visitdir(path):
    print("Directory:", path)
    entries = os.listdir(path)
    print("Content:", entries)

    for item in entries:
        full_path = path + "/" + item
        if os.path.isdir(full_path):
            visitdir(full_path)

visitdir(".")
```

This manual recursive version makes the tree traversal logic visible step by step.

---

# 9. Practical Applications and Use Cases

The most useful programs combine several file and directory operations into a complete workflow.

This is where separate ideas such as opening files, checking paths, encoding data, and traversing directories become part of one larger program design.

## 9.1 Safe Text File Processing

A realistic file-processing script should check that input is available, read it safely, and then produce a useful result.

### Example 1

```python
# Load a text file and report how many lines it contains.
import os

def count_lines_safely(path):
    if not os.path.isfile(path) or not os.access(path, os.R_OK):
        return "Cannot read file"

    with open(path, "r", encoding="utf-8") as file:
        # readlines returns a list containing all text lines.
        lines = file.readlines()

    return len(lines)

print(count_lines_safely("food.txt"))
```

This combines path checking with normal text-file processing.

### Example 2

```python
# Filter non-empty lines and save them to a new file.
def copy_non_empty_lines(source_path, target_path):
    with open(source_path, "r", encoding="utf-8") as fin:
        with open(target_path, "w", encoding="utf-8") as fout:
            for line in fin:
                # Only meaningful text lines are copied.
                if line.strip():
                    fout.write(line)

copy_non_empty_lines("input.txt", "cleaned.txt")
```

This is a practical example of safe reading plus selective writing.

## 9.2 CSV File Processing

CSV files are common in reporting, data exchange, and spreadsheet-style storage. Python can process them with the standard library or with external libraries such as `pandas`.

The standard `csv` module is a good fit when the goal is to show how rows, columns, headers, and output files work explicitly. `pandas` is more compact when the data should be treated like a table and transformed column by column.

### Example 1

```python
# Read a CSV file and write a filtered CSV file without pandas.
import csv

def filter_passing_scores(source_path, target_path):
    with open(source_path, "r", encoding="utf-8", newline="") as fin:
        # DictReader uses the first CSV row as field names.
        reader = csv.DictReader(fin)
        rows = []

        for row in reader:
            # Keep only students whose score is 50 or above.
            if int(row["score"]) >= 50:
                rows.append(row)

    with open(target_path, "w", encoding="utf-8", newline="") as fout:
        # newline="" avoids extra blank lines on some systems.
        writer = csv.DictWriter(fout, fieldnames=["name", "score"])
        # Write the column names before the filtered data rows.
        writer.writeheader()
        writer.writerows(rows)

filter_passing_scores("scores.csv", "passed_scores.csv")
```

This version uses the standard `csv` module and keeps the workflow explicit step by step.

### Example 2

```python
# Read and write CSV data with pandas.
import pandas as pd

def summarize_scores(source_path, target_path):
    # read_csv loads the file into a table-like DataFrame object.
    table = pd.read_csv(source_path)
    # Create a new boolean column from the numeric score column.
    table["passed"] = table["score"] >= 50
    # index=False keeps pandas from writing row numbers as a column.
    table.to_csv(target_path, index=False)

summarize_scores("scores.csv", "scores_with_status.csv")
```

`pandas` is more compact for table-shaped data, although it must be installed separately.

## 9.3 JSON File Processing

JSON is widely used for configuration files, APIs, and structured data exchange. Python's standard `json` module makes it easy to write and read JSON data.

JSON maps naturally to Python dictionaries, lists, strings, numbers, booleans, and `None`. That makes it a practical format for saving structured settings in a human-readable way.

### Example 1

```python
# Write a configuration dictionary to a JSON file.
import json

def save_config(path, config):
    with open(path, "w", encoding="utf-8") as file:
        # indent makes the output easier for humans to read.
        # dump writes JSON text directly into the open file.
        json.dump(config, file, indent=4)

save_config(
    "service.json",
    {"host": "localhost", "port": 8080, "active": True},
)
```

This example serializes a Python dictionary into a common structured text format.

### Example 2

```python
# Read JSON data back into normal Python objects.
import json

def load_config(path):
    with open(path, "r", encoding="utf-8") as file:
        # load converts JSON text into Python data structures.
        return json.load(file)

print(load_config("service.json"))
```

JSON reading is useful when programs need to restore structured settings or saved records.

## 9.4 Binary Record Storage and Retrieval

Binary storage is useful when repeated records need compact layout and direct access by position.

This is one of the clearest cases where file modes, encoding, `struct`, and `seek()` all work together in one design.

### Example 1

```python
# Store two account records with identical binary structure.
import struct

def save_accounts(path, accounts):
    with open(path, "wb") as file:
        for login, first_name, last_name, value in accounts:
            record = struct.pack(
                "8s20s20sd",
                # Every text field is converted to bytes before packing.
                login.encode("utf-8"),
                first_name.encode("utf-8"),
                last_name.encode("utf-8"),
                value,
            )
            file.write(record)

save_accounts(
    "accounts.bin",
    [
        ("massimo", "Massimo", "Piccardi", 1020.678),
        ("john2012", "John", "Miller", -74.0),
    ],
)
```

Each record uses the same format, so every write has the same length.

### Example 2

```python
# Read the second account directly by jumping to its offset.
import struct

def read_second_account(path):
    size = struct.calcsize("8s20s20sd")

    with open(path, "rb") as file:
        # Skip exactly one record to reach the second one.
        file.seek(size, 0)
        login, first_name, last_name, value = struct.unpack(
            "8s20s20sd",
            file.read(size),
        )

    return {
        # Fixed-width strings may include zero-byte padding at the end.
        "login": login.rstrip(b"\x00").decode("utf-8"),
        "value": value,
    }

print(read_second_account("accounts.bin"))
```

This is the main advantage of fixed-length records: fast direct retrieval.

## 9.5 Recursive Directory Traversal

Directory traversal is a common systems task for inspection, reporting, and automation.

The main idea is repetition over nested directories: inspect the current directory, then apply the same logic to each child directory that appears inside it.

### Example 1

```python
# Count how many files appear in a directory tree.
import os

def count_files(root_path):
    total = 0

    for current_path, directories, filenames in os.walk(root_path):
        # Add the number of plain files found in this directory.
        total += len(filenames)

    return total

print(count_files("."))
```

This example uses `os.walk()` to summarize the whole tree.

### Example 2

```python
# Recursively print every directory found below a root path.
import os

def print_directories(path):
    print(path)

    for item in os.listdir(path):
        full_path = path + "/" + item
        # Recurse only into child directories, not regular files.
        if os.path.isdir(full_path):
            print_directories(full_path)

print_directories(".")
```

This version emphasizes recursion and the structure of the directory tree itself.

---

**End of Week 11**