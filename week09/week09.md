# Week 09 — Python Data Structures

## Table of Contents
1. [Python Data Structures](#1-python-data-structures)  
   1.1 [Definition of Data Structures](#11-definition-of-data-structures)  
   1.2 [Built-in Data Types](#12-built-in-data-types)  
   1.3 [Mutable vs Immutable Types](#13-mutable-vs-immutable-types)  
   1.4 [When and Why Data Structures Are Used](#14-when-and-why-data-structures-are-used)  

2. [Lists](#2-lists)  
   2.1 [Definition of Lists](#21-definition-of-lists)  
   2.2 [Creating Lists](#22-creating-lists)  
   2.3 [Accessing and Modifying Elements](#23-accessing-and-modifying-elements)  
   2.4 [List Indexing and Slicing](#24-list-indexing-and-slicing)  
   2.5 [Iterating Through Lists](#25-iterating-through-lists)  
   2.6 [List Operations and Methods](#26-list-operations-and-methods)  
   2.7 [Usage Scenarios](#27-usage-scenarios)  
   2.8 [Example 1 — Basic List Usage](#28-example-1--basic-list-usage)  
   2.9 [Example 2 —  List Processing](#29-example-2---list-processing)  

3. [Sets](#3-sets)  
   3.1 [Definition of Sets](#31-definition-of-sets)  
   3.2 [Creating Sets](#32-creating-sets)  
   3.3 [Set Operations (Union, Intersection, Difference)](#33-set-operations-union-intersection-difference)  
   3.4 [Membership Testing](#34-membership-testing)  
   3.5 [Usage Scenarios](#35-usage-scenarios)  
   3.6 [Example 1 — Basic Set Usage](#36-example-1--basic-set-usage)  
   3.7 [Example 2 —  Set Operations](#37-example-2---set-operations)  

4. [Tuples](#4-tuples)  
   4.1 [Definition of Tuples](#41-definition-of-tuples)  
   4.2 [Creating Tuples](#42-creating-tuples)  
   4.3 [Accessing Elements](#43-accessing-elements)  
   4.4 [Immutability and Its Benefits](#44-immutability-and-its-benefits)  
   4.5 [Usage Scenarios](#45-usage-scenarios)  
   4.6 [Example 1 — Basic Tuple Usage](#46-example-1--basic-tuple-usage)  
   4.7 [Example 2 —  Tuple Processing](#47-example-2---tuple-processing)  

5. [Dictionaries](#5-dictionaries)  
   5.1 [Definition of Dictionaries](#51-definition-of-dictionaries)  
   5.2 [Creating Dictionaries](#52-creating-dictionaries)  
   5.3 [Accessing and Updating Values](#53-accessing-and-updating-values)  
   5.4 [Adding and Removing Elements](#54-adding-and-removing-elements)  
   5.5 [Iterating Through Dictionaries](#55-iterating-through-dictionaries)  
   5.6 [Dictionary Operations and Methods](#56-dictionary-operations-and-methods)  
   5.7 [Usage Scenarios](#57-usage-scenarios)  
   5.8 [Example 1 — Basic Dictionary Usage](#58-example-1--basic-dictionary-usage)  
   5.9 [Example 2 —  Dictionary Processing](#59-example-2---dictionary-processing)  

6. [Advanced Data Structures](#6-advanced-data-structures)  
   6.1 [Nested Lists](#61-nested-lists)  
   6.2 [Lists of Dictionaries](#62-lists-of-dictionaries)  
   6.3 [Dictionaries of Lists](#63-dictionaries-of-lists)  
   6.4 [Dictionaries of Dictionaries](#64-dictionaries-of-dictionaries)  
   6.5 [Complex Data Modelling](#65-complex-data-modelling)  
   6.6 [Example 1 — Nested Data Processing](#66-example-1--nested-data-processing)  
   6.7 [Example 2 — Multi-level Data Aggregation](#67-example-2--multi-level-data-aggregation)  

7. [Practical Application](#7-practical-application)  
   7.1 [Processing Structured Input Data](#71-processing-structured-input-data)  
   7.2 [Splitting Input Records](#72-splitting-input-records)  
   7.3 [Aggregating Data](#73-aggregating-data)  
   7.4 [Data Transformation and Reporting](#74-data-transformation-and-reporting)  
   7.5 [Example 1 — Basic Data Processing](#75-example-1--basic-data-processing)  
   7.6 [Example 2 — Printer Job Analysis (Dictionary of Lists)](#76-example-2--printer-job-analysis-dictionary-of-lists) \
   7.7 [Example 3 — Reading and Splitting File Input (from Argument)](#77-example-3--reading-and-splitting-file-input-from-argument)  
   7.8 [Example 4 — Full File-Based Aggregation (Printer Analysis)](#78-example-4--full-file-based-aggregation-printer-analysis)

---

# 1. Python Data Structures

## 1.1 Definition of Data Structures

A data structure is a way of storing and organising multiple values so that they can be accessed, updated, and processed efficiently.

In Python, data structures are used whenever one variable is not enough to represent the required information. Instead of storing separate values in many independent variables, Python allows you to group related values together into a single object.

Conceptually:

```text
single value        → one variable
multiple values     → data structure
structured data     → richer data structure
```

For example:

- a list can store many values in sequence
- a set can store unique values
- a tuple can store a fixed group of related values
- a dictionary can store key-value pairs

Data structures are fundamental in systems programming because many practical tasks involve collections of values such as:

- filenames in a directory
- process IDs
- configuration settings
- user records
- lines read from input
- counters and summaries

## 1.2 Built-in Data Types

Python provides several built-in data types. Some hold a single value, while others can hold many values.

Common built-in types include:

- `int` → integer numbers
- `float` → floating-point numbers
- `str` → text strings
- `bool` → boolean values
- `list` → ordered, mutable sequence
- `tuple` → ordered, immutable sequence
- `set` → unordered collection of unique values
- `dict` → mapping of keys to values

A useful classification is:

```text
Simple scalar types     → int, float, bool, str
Collection types        → list, tuple, set, dict
```

In this lecture, the main focus is on:

- lists
- sets
- tuples
- dictionaries

These are the most relevant built-in data structures for introductory Python data processing.

## 1.3 Mutable vs Immutable Types

A mutable object can be changed after it is created.  
An immutable object cannot be changed after it is created.

This distinction is very important because it affects how updates work.

Examples:

- `list` is mutable
- `set` is mutable
- `dict` is mutable
- `tuple` is immutable
- `str` is immutable

Conceptually:

```text
Mutable     → modify in place
Immutable   → create a new object instead
```

### Example

```python
# strings are immutable
s = "Unix"

# this creates a new string object rather than modifying the old one
s = s + " Systems"

print(s)

# lists are mutable
items = [1, 2, 3]

# this changes the existing list object
items.append(4)

print(items)
```

The distinction matters because mutable structures are convenient for dynamic processing, while immutable structures are safer when values should not change.

## 1.4 When and Why Data Structures Are Used

Data structures are used whenever a program must handle more than one value in a meaningful way.

Examples:

- list of marks for a student
- set of unique error codes
- tuple storing `(username, uid, shell)`
- dictionary mapping service names to status codes

A good general guide is:

- use a **list** when order matters and updates are common
- use a **set** when uniqueness matters
- use a **tuple** when values belong together and should remain fixed
- use a **dictionary** when values must be accessed by a key rather than by position

In systems programming, this makes code easier to read, easier to extend, and more aligned with real input data.

---

# 2. Lists

## 2.1 Definition of Lists

A list is an ordered, mutable collection of values.

A list stores its elements in sequence order, and each element can be accessed by its index. Lists are one of the most widely used Python data structures because they are flexible and easy to update.

A list may contain:

- values of the same type
- values of mixed types
- even other data structures

Conceptually:

```text
index:   0    1    2    3
list : [val, val, val, val]
```

## 2.2 Creating Lists

Lists are created using square brackets.

### Example

```python
# create a list with several values
numbers = [10, 20, 30]

# create a list with mixed types
mixed = [7, 11.2, "text", True]

# create an empty list
empty_list = []

print(numbers)
print(mixed)
print(empty_list)
```

This shows three common ways to create lists:

- a numeric list
- a mixed list
- an empty list to be filled later

## 2.3 Accessing and Modifying Elements

List elements are accessed using indexes. Python lists are zero-based, so the first element is at index `0`.

### Example

```python
# create a list
cities = ["Sydney", "Melbourne", "Brisbane"]

# read an element using its index
print(cities[0])   # first element
print(cities[2])   # third element

# lists are mutable, so elements can be modified
cities[1] = "Perth"

print(cities)
```

Because lists are mutable, they are useful when values need to be updated during program execution.

## 2.4 List Indexing and Slicing

Lists support several useful index notations.

Important forms include:

- `my_list[0]` → first element
- `my_list[-1]` → last element
- `my_list[1:4]` → elements from index 1 to 3
- `my_list[:3]` → first three elements
- `my_list[2:]` → from index 2 to the end
- `my_list[::2]` → every second element

### Example

```python
# define a list of values
values = [10, 20, 30, 40, 50, 60]

print(values[-1])    # last element
print(values[1:4])   # slice from index 1 to 3
print(values[:3])    # first three elements
print(values[2:])    # from index 2 onwards
print(values[::2])   # step through the list with step 2
```

Slicing is powerful because it lets you work with parts of a list without needing separate loops.

## 2.5 Iterating Through Lists

Lists are often processed element by element.

There are two common ways to iterate through a list.

### Method 1: iterate directly through values

```python
# list of subject names
subjects = ["USP", "Networks", "Databases"]

# print each subject directly
for item in subjects:
    print(item)
```

### Method 2: iterate through indexes

```python
# same list
subjects = ["USP", "Networks", "Databases"]

# print each subject using its index
for i in range(len(subjects)):
    print(i, subjects[i])
```

The second form is more flexible because it also provides the position of each value.

## 2.6 List Operations and Methods

Lists support many useful built-in operations.

Common operations include:

- `append()` → add at the end
- `insert()` → insert at a chosen position
- `del` → delete an element
- `reverse()` → reverse the list in place
- `sort()` → sort the list in place
- `+` → concatenate lists
- `in` → test membership
- `len()` → return list length

### Example

```python
# start with a simple list
names = ["Tom", "Ann"]

# append adds a new element to the end
names.append("John")

# insert adds a new element at a chosen position
names.insert(1, "Mary")

# delete the element at index 0
del names[0]

print(names)

# reverse the current order
names.reverse()
print(names)

# sort alphabetically
names.sort()
print(names)

# membership test
print("Ann" in names)

# length
print(len(names))
```

## 2.7 Usage Scenarios

Lists are useful when:

- order matters
- items may repeat
- values must be added, removed, or updated
- the program processes sequences

Typical systems-oriented examples include:

- list of usernames
- list of filenames
- list of service names
- list of marks
- list of command-line arguments

A very important real Python list is `sys.argv`, which stores command-line arguments.

## 2.8 Example 1 — Basic List Usage

```python
#!/usr/bin/env python3

# create a list of log severity values
levels = ["INFO", "WARNING", "ERROR"]

# print the full list
print(levels)

# access the first and last elements
print("First level:", levels[0])
print("Last level :", levels[-1])

# modify an element because lists are mutable
levels[1] = "WARN"

# add a new level at the end
levels.append("CRITICAL")

# show final result
print("Updated list:", levels)
```

This example demonstrates the key basic list actions:

- creation
- reading
- modifying
- appending

## 2.9 Example 2 —  List Processing

```python
#!/usr/bin/env python3

# list of file sizes in bytes
sizes = [1200, 850, 3000, 450, 2200]

# prepare summary variables
total = 0
largest = sizes[0]
smallest = sizes[0]

# process the list one item at a time
for size in sizes:
    total += size  # accumulate the total size

    # update the largest value if needed
    if size > largest:
        largest = size

    # update the smallest value if needed
    if size < smallest:
        smallest = size

# compute the average using the list length
average = total / len(sizes)

print("Sizes   :", sizes)
print("Total   :", total)
print("Largest :", largest)
print("Smallest:", smallest)
print("Average :", average)
```

This example shows why lists are useful in data processing: they allow repeated values to be stored and analysed with a loop.

---

# 3. Sets

## 3.1 Definition of Sets

A set is an unordered collection of unique values.

Unlike a list, a set does not keep duplicates.  
This makes sets useful when the goal is to store distinct items only.

Conceptually:

```text
Input values with duplicates  → set removes repeated values
```

For example, the set created from:

```text
1, 2, 2, 3, 3, 3
```

contains only:

```text
1, 2, 3
```

## 3.2 Creating Sets

Sets are created using curly braces or by converting another collection using `set()`.

### Example

```python
# create a set directly
codes = {"A", "B", "C"}

# duplicates are automatically removed
numbers = {1, 2, 2, 3, 3, 4}

# create a set from a list
items = set(["red", "green", "red", "blue"])

print(codes)
print(numbers)
print(items)
```

Notice that duplicates disappear automatically.

## 3.3 Set Operations (Union, Intersection, Difference)

Sets support mathematical-style operations.

Main operations:

- union `|` → values in either set
- intersection `&` → values in both sets
- difference `-` → values in first set but not in second

### Example

```python
# create two sets
group_a = {"Tom", "Ann", "John"}
group_b = {"Ann", "Mary", "John"}

# union combines all unique values
print(group_a | group_b)

# intersection keeps only common values
print(group_a & group_b)

# difference keeps values only in group_a
print(group_a - group_b)
```

These operations are especially useful when comparing collections.

## 3.4 Membership Testing

A set is very useful when you need to test whether a value exists in a collection.

### Example

```python
# allowed commands
allowed = {"start", "stop", "restart"}

# test if a command exists in the set
print("start" in allowed)
print("reload" in allowed)
```

Because sets are built for uniqueness and membership checks, they are often used in validation tasks.

## 3.5 Usage Scenarios

Sets are useful when:

- duplicates should be removed
- quick membership tests are needed
- intersections and differences matter

Typical examples:

- unique usernames
- unique error codes
- allowed commands
- set of installed packages
- comparison between two groups of values

## 3.6 Example 1 — Basic Set Usage

```python
#!/usr/bin/env python3

# list of repeated service names
services = ["nginx", "ssh", "nginx", "cron", "ssh"]

# convert list to set to remove duplicates
unique_services = set(services)

print("Original list :", services)
print("Unique values :", unique_services)

# test membership
print("ssh exists?   :", "ssh" in unique_services)
print("mysql exists? :", "mysql" in unique_services)
```

This demonstrates the most common basic use of sets: duplicate removal and membership testing.

## 3.7 Example 2 —  Set Operations

```python
#!/usr/bin/env python3

# packages installed on two different systems
host1 = {"python", "vim", "git", "curl"}
host2 = {"python", "git", "htop", "wget"}

# packages seen on either system
all_packages = host1 | host2

# packages common to both systems
shared_packages = host1 & host2

# packages only on host1
host1_only = host1 - host2

print("All packages   :", all_packages)
print("Shared packages:", shared_packages)
print("Host1 only     :", host1_only)
```

This example shows why sets are useful for system comparison tasks.

---

# 4. Tuples

## 4.1 Definition of Tuples

A tuple is an ordered, immutable collection of values.

A tuple is similar to a list, but once created, its contents cannot be changed.

Conceptually:

```text
List   → ordered, mutable
Tuple  → ordered, immutable
```

Because tuples are immutable, they are safer when a group of related values should stay fixed.

## 4.2 Creating Tuples

Tuples are created using parentheses.

### Example

```python
# create a tuple with three values
record = ("alice", 1042, "running")

print(record)
```

Tuples may also hold mixed types, just like lists.

## 4.3 Accessing Elements

Tuple elements are accessed by index in the same way as list elements.

### Example

```python
# tuple storing a username, UID, and shell
user_info = ("tom", 501, "/bin/bash")

print(user_info[0])   # first element
print(user_info[1])   # second element
print(user_info[-1])  # last element
```

Although tuple elements can be read easily, they cannot be modified.

## 4.4 Immutability and Its Benefits

Tuple immutability means the tuple cannot be changed after creation.

### Example

```python
# create a tuple
coords = (10, 20)

# this would fail because tuples are immutable
# coords[0] = 99
```

The benefit of immutability is that tuples can safely represent fixed records such as:

- coordinates
- user records
- command results
- grouped return values from functions

When a structure should not be accidentally modified, a tuple is often a better choice than a list.

## 4.5 Usage Scenarios

Tuples are useful when:

- values belong together as one record
- values should remain fixed
- the data should be protected from accidental updates

Examples:

- `(username, uid, shell)`
- `(x, y)` coordinates
- `(course_code, course_name)`
- `(printer_name, total_jobs)`

## 4.6 Example 1 — Basic Tuple Usage

```python
#!/usr/bin/env python3

# tuple representing a simple process record
process = ("python3", 2481, "running")

# access values by position
print("Command:", process[0])
print("PID    :", process[1])
print("State  :", process[2])
```

This shows the tuple as a compact record structure.

## 4.7 Example 2 —  Tuple Processing

```python
#!/usr/bin/env python3

# tuple storing a course code, title, and credit points
subject = ("32547", "Unix Systems Programming", 6)

# tuple unpacking assigns each element to a variable
code, title, credit_points = subject

print("Code         :", code)
print("Title        :", title)
print("Credit points:", credit_points)

# tuples can also be used as fixed return-style records
report = ("PASS", 78)

status, mark = report

print("Status:", status)
print("Mark  :", mark)
```

This example shows how tuples are useful for grouped records and tuple unpacking.

---

# 5. Dictionaries

## 5.1 Definition of Dictionaries

A dictionary is a collection of key-value pairs.

Instead of using numeric indexes like a list, a dictionary uses keys to access values.

Conceptually:

```text
list        → position selects value
dictionary  → key selects value
```

For example:

```text
"Name"  → "Alice"
"Mark"  → 88
```

Dictionaries are one of the most important Python data structures because they model structured data very naturally.

## 5.2 Creating Dictionaries

Dictionaries are created using curly braces with key-value pairs.

### Example

```python
# create a dictionary with three entries
student = {
    "Name": "John Carrisi",
    "Subject": "32547",
    "Mark": 100
}

print(student)
```

Keys are usually strings, and values can be of many types.

## 5.3 Accessing and Updating Values

Dictionary values are accessed using their key.

### Example

```python
# define a student dictionary
student = {
    "Name": "Alice",
    "Mark": 92
}

# read a value using its key
print(student["Mark"])

# update a value
student["Mark"] -= 10

print(student)
```

This makes dictionaries very convenient when the data has named fields.

## 5.4 Adding and Removing Elements

New key-value pairs can be added by assigning to a new key.  
Existing elements can be removed with `del`.

### Example

```python
# create a dictionary
service = {"Name": "nginx", "Status": "running"}

# add a new key-value pair
service["Port"] = 80

# remove an existing key
del service["Status"]

print(service)
```

Because dictionaries are mutable, they are very flexible during program execution.

## 5.5 Iterating Through Dictionaries

Dictionaries can be iterated in different ways.

### Example 1: iterate through keys

```python
# dictionary of marks
marks = {"Tom": 80, "Ann": 95, "John": 72}

# iterating directly gives keys
for name in marks:
    print(name)
```

### Example 2: iterate through keys and values

```python
# same dictionary
marks = {"Tom": 80, "Ann": 95, "John": 72}

for name in marks:
    print(name, marks[name])
```

This is the most common introductory style for printing dictionary content.

## 5.6 Dictionary Operations and Methods

Common dictionary operations include:

- assignment to add or update
- `del` to remove
- `in` to test key existence
- `len()` for size

### Example

```python
# create a dictionary
config = {
    "host": "localhost",
    "port": 8080
}

# check if a key exists
print("host" in config)
print("user" in config)

# number of entries
print(len(config))

# update an existing key
config["port"] = 9090

# add a new key
config["mode"] = "dev"

print(config)
```

## 5.7 Usage Scenarios

Dictionaries are useful when:

- values have names rather than positions
- fast lookup by key is needed
- the data represents records or structured properties

Examples:

- student record
- service configuration
- printer statistics
- user profile
- filename-to-size mapping

## 5.8 Example 1 — Basic Dictionary Usage

```python
#!/usr/bin/env python3

# dictionary storing service details
service = {
    "name": "nginx",
    "status": "running",
    "port": 80
}

# access individual values using keys
print("Service:", service["name"])
print("Status :", service["status"])
print("Port   :", service["port"])

# update an existing value
service["status"] = "restarting"

print("Updated dictionary:", service)
```

This demonstrates the most important basic dictionary operations:

- creation
- access by key
- update by key

## 5.9 Example 2 —  Dictionary Processing

```python
#!/usr/bin/env python3

# dictionary of student marks
marks = {
    "Tom": 80,
    "Ann": 95,
    "John": 72
}

# prepare counters
total = 0
highest_name = ""
highest_mark = -1

# iterate through all keys in the dictionary
for name in marks:
    mark = marks[name]  # get the mark for the current student
    total += mark       # update running total

    # update highest mark information if needed
    if mark > highest_mark:
        highest_mark = mark
        highest_name = name

# average mark is total divided by dictionary size
average = total / len(marks)

print("Marks        :", marks)
print("Average mark :", average)
print("Top student  :", highest_name)
print("Top mark     :", highest_mark)
```

This example shows how dictionaries are used in aggregation tasks.

---

# 6. Advanced Data Structures

## 6.1 Nested Lists

A nested list is a list whose elements are themselves lists.

This is useful when the program must represent rows, groups, or structured collections.

### Example

```python
# nested list representing rows and columns
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

# access nested values
print(matrix[0])      # first row
print(matrix[1][2])   # third value of second row
```

Nested lists are often used for:

- tables
- grids
- grouped records

## 6.2 Lists of Dictionaries

A list of dictionaries is useful when there are multiple records with the same fields.

### Example

```python
# each dictionary represents one student record
students = [
    {"name": "Tom", "mark": 80},
    {"name": "Ann", "mark": 95},
    {"name": "John", "mark": 72}
]

# access the second student's name
print(students[1]["name"])
```

This structure is common in structured data processing because it resembles rows in a table.

## 6.3 Dictionaries of Lists

A dictionary of lists is useful when each key maps to multiple related values.

### Example

```python
# each printer maps to [job_count, total_size]
printers = {
    "Printer_A": [3, 1200],
    "Printer_B": [1, 400]
}

print(printers["Printer_A"][0])  # job count
print(printers["Printer_A"][1])  # total size
```

This structure is especially useful for aggregation.

## 6.4 Dictionaries of Dictionaries

A dictionary of dictionaries is useful when each key maps to a complete sub-record.

### Example

```python
# nested dictionary of service details
services = {
    "nginx": {"status": "running", "port": 80},
    "ssh": {"status": "running", "port": 22}
}

print(services["nginx"]["status"])
print(services["ssh"]["port"])
```

This is a very natural structure for grouped configuration or status information.

## 6.5 Complex Data Modelling

Complex data modelling means combining data structures so that the program can represent realistic data more naturally.

Typical combinations include:

- list of lists
- list of dictionaries
- dictionary of lists
- dictionary of dictionaries

The main design question is:

```text
What must be selected by position?
What must be selected by key?
What should be grouped together?
```

This helps determine which structure is the best fit.

## 6.6 Example 1 — Nested Data Processing

```python
#!/usr/bin/env python3

# list of dictionaries representing student records
students = [
    {"name": "Tom", "marks": [70, 80, 75]},
    {"name": "Ann", "marks": [90, 95, 88]},
    {"name": "John", "marks": [60, 72, 68]}
]

# process each student record
for student in students:
    name = student["name"]      # extract the student name
    marks = student["marks"]    # extract the student's mark list

    # compute total mark for this student
    total = 0
    for mark in marks:
        total += mark

    average = total / len(marks)

    print(name, "->", average)
```

This example combines:

- a list for multiple students
- a dictionary for named fields
- a nested list for repeated marks

## 6.7 Example 2 — Multi-level Data Aggregation

```python
#!/usr/bin/env python3

# dictionary of dictionaries storing printer statistics
printers = {
    "Printer_A": {"jobs": 2, "size": 450},
    "Printer_B": {"jobs": 3, "size": 900}
}

# update a printer record with another job
printer_name = "Printer_A"
job_size = 200

# increment the job counter
printers[printer_name]["jobs"] += 1

# add the job size to the running total
printers[printer_name]["size"] += job_size

# print the updated structure
for printer in printers:
    print(printer, printers[printer])
```

This example shows how a nested structure supports clear named aggregation.

---

# 7. Practical Application

## 7.1 Processing Structured Input Data

Real programs often receive structured input rather than single isolated values.

Examples include:

- `printer_name,job_size`
- `username,uid,shell`
- `service,status,port`

The input must usually be:

1. read
2. split into fields
3. converted where necessary
4. stored in an appropriate data structure
5. processed and reported

This is where data structures become practically useful.

## 7.2 Splitting Input Records

A structured line is often split into fields before processing.

### Example

```python
import re

# one structured input line
line = "anon_pro100,235444"

# split at the comma
fields = re.split(",", line)

print(fields)
```

After splitting, each field can be assigned meaning:

- `fields[0]` → printer name
- `fields[1]` → job size

## 7.3 Aggregating Data

Aggregation means combining multiple input records into a summary.

Typical aggregated values include:

- total count
- total size
- average
- largest value
- grouped summaries by key

A dictionary is especially useful for this because each unique key can store its own cumulative result.

## 7.4 Data Transformation and Reporting

After reading and aggregating the data, the program usually transforms it into a readable report.

This may include:

- converting strings to integers
- computing totals
- computing counts
- printing grouped results

A good data structure allows this to be done clearly and efficiently.

## 7.5 Example 1 — Basic Data Processing

```python
#!/usr/bin/env python3

import re

# structured line with two fields
line = "printer1,200"

# remove any trailing newline if the line came from input
line = line.rstrip("\n")

# split the line into fields using the comma separator
fields = re.split(",", line)

# extract and convert the values
printer_name = fields[0]
job_size = int(fields[1])

print("Printer:", printer_name)
print("Job size:", job_size)
```

This is the simplest form of structured data processing: read, split, convert, and print.

## 7.6 Example 2 — Printer Job Analysis (Dictionary of Lists)

```python
#!/usr/bin/env python3

import re

# sample structured input lines
lines = [
    "anon_pro100,235444",
    "Secure Print B&W,85410",
    "anon_pro100,2549",
    "Secure Print Colour,1000000",
    "anon_pro100,3235444",
    "anon_pro100,191919",
    "Secure Print B&W,14591"
]

# create an empty dictionary
# each key will be a printer name
# each value will be a list: [job_count, total_job_size]
printers = {}

# process each input line
for line in lines:
    # remove the final newline if present
    line = line.rstrip("\n")

    # split the structured record into fields
    fields = re.split(",", line)

    # extract the printer name and convert the size to int
    printer_name = fields[0]
    job_size = int(fields[1])

    # if the printer already exists, update its aggregated values
    if printer_name in printers:
        printers[printer_name][0] += 1      # increment job count
        printers[printer_name][1] += job_size  # add to total size
    else:
        # otherwise create a new entry with initial values
        printers[printer_name] = [1, job_size]

# print the final aggregated report
for printer in printers:
    print(printer, printers[printer])
```

This example is important because it demonstrates:

- structured input processing
- splitting records
- type conversion
- dictionary-based aggregation
- dictionary of lists as a practical data structure

## 7.7 Example 3 — Reading and Splitting File Input (from Argument)

### Explanation

In Python, command-line arguments are accessed using the `sys.argv` list.

- `sys.argv[0]` → script name  
- `sys.argv[1]` → first argument, which is typically the input file  

When the script is executed as:

    python3 script.py data.txt

the file `data.txt` becomes available inside the program as `sys.argv[1]`.

Python opens the file using:

    fin = open(sys.argv[1])

This allows the program to read the file contents.

When iterating over the file:

    for line in fin:

Python reads the file **line by line**, which is efficient and avoids loading the entire file into memory.

Each line ends with a newline character (`\n`), which is usually removed before processing:

    line = line.rstrip('\n')

Once cleaned, the line can be split into structured fields.

---

### Example — Reading and Splitting File Input
```python
    #!/usr/bin/env python3

    import sys
    import re

    # create an empty dictionary (not used yet, but prepares structure)
    printers = {}

    # open file passed as argument
    fin = open(sys.argv[1])

    # read file line by line
    for line in fin:
        # remove trailing newline
        line = line.rstrip('\n')

        # split line into fields using comma
        fields = re.split(',', line)

        # print extracted fields
        print(fields)

    # close file after reading
    fin.close()
```
### What this demonstrates

- Reading a file passed as a command-line argument  
- Processing input line by line  
- Cleaning input data (`rstrip`)  
- Splitting structured records into fields  
- Preparing data for further processing (aggregation, analysis)

## 7.8 Example 4 — Full File-Based Aggregation (Printer Analysis)

### Explanation

In Python, command-line arguments are accessed using the `sys.argv` list.

- `sys.argv[0]` → script name  
- `sys.argv[1]` → first argument, which in this case is the input file name  

If the script is run as:

    python3 script.py spool.csv

then `spool.csv` becomes available inside the program as `sys.argv[1]`.

Python opens that file using:

    fin = open(sys.argv[1])

This opens the file in read mode by default.

When Python processes a file using:

    for line in fin:

it reads the file **line by line**, which is efficient and practical for structured input files.

Each line usually ends with a newline character (`\n`), so it is common to remove it before processing:

    line = line.rstrip('\n')

After that, the line can be split into fields, converted where needed, and aggregated into a data structure.

### Example — Printer Job Aggregation from File
```python
    #!/usr/bin/env python3

    import sys
    import re

    # dictionary to store aggregated results
    # key   -> printer name
    # value -> [job_count, total_size]
    printers = {}

    # open the file passed as the first command-line argument
    fin = open(sys.argv[1])

    # process each line in the file
    for line in fin:
        # remove trailing newline
        line = line.rstrip('\n')

        # split the structured record into fields
        fields = re.split(',', line)

        # extract printer name and convert job size to integer
        printer_name = fields[0]
        job_size = int(fields[1])

        # update aggregation
        if printer_name in printers:
            printers[printer_name][0] += 1         # increment job count
            printers[printer_name][1] += job_size  # add to total size
        else:
            printers[printer_name] = [1, job_size] # initialise entry

    # close the file after processing
    fin.close()

    # print final aggregated report
    print("\n--- Printer Job Report ---")

    for printer in printers:
        jobs = printers[printer][0]
        size = printers[printer][1]

        print(f"{printer} -> jobs: {jobs}, total size: {size}")
```
### What this demonstrates

- Reading a file from a command-line argument  
- Processing structured input line by line  
- Splitting each record into fields  
- Converting string data into numeric values  
- Aggregating data using a dictionary  
- Producing a structured summary report
---

**End of Week 09**

