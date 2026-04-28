# Week 10 — Functions in Python

## Table of Contents
1. [Functions in Python](#1-functions-in-python)
    - [1.1 Definition of Functions](#11-definition-of-functions)
    - [1.2 Creating and Calling Functions](#12-creating-and-calling-functions)
    - [1.3 Parameters vs Arguments](#13-parameters-vs-arguments)

2. [Function Parameters and Arguments](#2-function-parameters-and-arguments)
    - [2.1 Positional Arguments](#21-positional-arguments)
    - [2.2 Keyword Arguments](#22-keyword-arguments)
    - [2.3 Default Parameter Values](#23-default-parameter-values)

3. [Return Values](#3-return-values)
    - [3.1 Single Return Value](#31-single-return-value)
    - [3.2 Multiple Return Values](#32-multiple-return-values)

4. [Memory and Argument Passing](#4-memory-and-argument-passing)
    - [4.1 Variable Memory Model](#41-variable-memory-model)
    - [4.2 Immutable vs Mutable Objects](#42-immutable-vs-mutable-objects)
    - [4.3 Passing Immutable Objects](#43-passing-immutable-objects)
    - [4.4 Passing Mutable Objects](#44-passing-mutable-objects)

5. [Working with Data Structures in Functions](#5-working-with-data-structures-in-functions)
    - [5.1 Lists as Arguments](#51-lists-as-arguments)
    - [5.2 Dictionaries as Arguments](#52-dictionaries-as-arguments)
    - [5.3 Updating Data Structures in Functions](#53-updating-data-structures-in-functions)

6. [Variable-Length Arguments](#6-variable-length-arguments)
    - [6.1 *args](#61-args)
    - [6.2 **kwargs](#62-kwargs)

7. [Functions in Practice](#7-functions-in-practice)
    - [7.1 Modular Program Design](#71-modular-program-design)
    - [7.2 Reusing Functions](#72-reusing-functions)
    - [7.3 Using Standard Library Functions](#73-using-standard-library-functions)
    - [7.4 Functions with Files](#74-functions-with-files)

8. [Practical Applications and Use Cases](#8-practical-applications-and-use-cases)
    - [8.1 Command-Line Data Processing Pipeline](#81-command-line-data-processing-pipeline)
    - [8.2 Configuration Validation and Reporting](#82-configuration-validation-and-reporting)

---

# 1. Functions in Python

Functions are the core mechanism for organizing behaviour in Python. A function packages a task into a named, reusable unit so that the same logic does not need to be rewritten throughout a program.

Good functions help a program become:

- easier to read
- easier to test
- easier to debug
- easier to reuse
- easier to extend later

In practice, functions are the tool that lets a programmer turn a long script into a structured design.

## 1.1 Definition of Functions

A function is a named block of code that performs a specific task.

The important idea is abstraction: a function hides internal steps behind a meaningful name. The caller does not need to repeatedly describe how something is done. The caller only needs to know what the function expects and what it produces.

Conceptually:

```text
input values -> function logic -> result
```

### Example 1 — Intermediate

```python
def normalize_username(username):
    cleaned = username.strip().lower()
    return cleaned.replace(" ", "_")

print(normalize_username("  Alice Smith  "))
```

This function defines one focused operation: normalize a username for later use.

### Example 2 — Complex

```python
def summarize_service_status(records):
    summary = {"running": 0, "stopped": 0, "failed": 0}

    for name, state in records:
        if state in summary:
            summary[state] += 1
        else:
            summary["failed"] += 1

    return summary

services = [
    ("nginx", "running"),
    ("redis", "stopped"),
    ("db", "running"),
    ("backup", "broken"),
]

print(summarize_service_status(services))
```

This function is more advanced because it performs aggregation, classification, and reporting inside one reusable unit.

## 1.2 Creating and Calling Functions

A function is created with the `def` keyword. Its header declares the function name and its parameters. Its body contains the logic that runs when the function is called.

Defining a function does not execute it. The code inside the function runs only when the function call happens.

### Example 1 — Intermediate

```python
def calculate_disk_usage(blocks, block_size):
    return blocks * block_size

total_bytes = calculate_disk_usage(240, 4096)
print(total_bytes)
```

The program first defines the function and only later uses it to compute a result.

### Example 2 — Complex

```python
def parse_record(line):
    user, uid, shell = line.strip().split(":")
    return {"user": user, "uid": int(uid), "shell": shell}

def show_record(record):
    print(f"{record['user']} -> uid={record['uid']} shell={record['shell']}")

line = "guest:1002:/bin/bash"
record = parse_record(line)
show_record(record)
```

This design separates data conversion from output formatting, which is a common and useful pattern.

## 1.3 Parameters vs Arguments

A parameter is a variable declared by the function definition.
An argument is the real value supplied when the function is called.

This distinction matters because parameters describe a general interface, while arguments provide specific runtime data.

### Example 1 — Intermediate

```python
def repeat_text(text, count):
    return text * count

print(repeat_text("ab", 3))
```

Here, `text` and `count` are parameters. The values `"ab"` and `3` are the arguments.

### Example 2 — Complex

```python
def within_range(value, lower, upper):
    return lower <= value <= upper

numbers = [4, 11, 17, 29, 32]
filtered = []

for number in numbers:
    if within_range(number, 10, 30):
        filtered.append(number)

print(filtered)
```

The same function can be reused with many different arguments while keeping one stable definition.

---

# 2. Function Parameters and Arguments

Parameter design affects how clear and safe a function call is. Two functions can compute the same result, but the one with better parameter design is easier to use correctly.

## 2.1 Positional Arguments

With positional arguments, values are matched to parameters according to order. This is simple and compact, but the caller must remember the correct parameter sequence.

### Example 1 — Intermediate

```python
def build_path(directory, filename, extension):
    return f"{directory}/{filename}.{extension}"

print(build_path("logs", "system", "txt"))
```

The order works well because the arguments follow the natural layout of a path.

### Example 2 — Complex

```python
def compute_window(series, start, length):
    return series[start:start + length]

data = [12, 18, 21, 30, 27, 19, 16, 11]
window = compute_window(data, 2, 4)
print(window)
```

Here, choosing the right order is important because all arguments are valid types, so mistakes may not immediately cause errors.

## 2.2 Keyword Arguments

With keyword arguments, values are supplied by parameter name. This improves readability and is useful when several parameters have similar meanings or similar data types.

### Example 1 — Intermediate

```python
def create_user(name, role, active):
    return {"name": name, "role": role, "active": active}

user = create_user(role="operator", name="Nadia", active=True)
print(user)
```

The meaning of each value is immediately visible in the call.

### Example 2 — Complex

```python
def connect_service(host, port, timeout, retries):
    return f"Connecting to {host}:{port} timeout={timeout} retries={retries}"

message = connect_service(
    host="127.0.0.1",
    port=8080,
    retries=3,
    timeout=5,
)
print(message)
```

Keyword arguments reduce confusion when a function accepts several configuration values.

## 2.3 Default Parameter Values

Default parameters provide a fallback value when the caller does not supply an argument. This makes common calls simpler while preserving flexibility.

### Example 1 — Intermediate

```python
def read_chunk(size=1024):
    return f"Reading {size} bytes"

print(read_chunk())
print(read_chunk(4096))
```

A default value supports a standard case without blocking customization.

### Example 2 — Complex

```python
def export_report(data, format_name="txt", include_header=True):
    lines = []

    if include_header:
        lines.append("REPORT")

    for item in data:
        lines.append(str(item))

    return {"format": format_name, "content": lines}

print(export_report(["ok", "warning"]))
print(export_report(["ok", "warning"], format_name="json", include_header=False))
```

This pattern is common in reporting and export tools where a few sensible defaults handle most calls.

---

# 3. Return Values

A function becomes much more powerful when it returns data. Returned values can be stored, checked, transformed, or passed into other functions.

## 3.1 Single Return Value

Most functions return one result. That result may be a simple scalar or a larger structure.

### Example 1 — Intermediate

```python
def count_vowels(text):
    total = 0

    for char in text.lower():
        if char in "aeiou":
            total += 1

    return total

print(count_vowels("Documentation"))
```

The caller decides how to use the returned count.

### Example 2 — Complex

```python
def highest_scoring_player(players):
    best_name = None
    best_score = -1

    for name, score in players.items():
        if score > best_score:
            best_name = name
            best_score = score

    return {"name": best_name, "score": best_score}

print(highest_scoring_player({"Ali": 88, "Mina": 93, "Ravi": 91}))
```

This still returns one value, but that value is a structured object containing multiple pieces of information.

## 3.2 Multiple Return Values

Python can return multiple values by packaging them into a tuple. This is useful when one analysis naturally produces several related outputs.

### Example 1 — Intermediate

```python
def divide_and_remainder(a, b):
    return a // b, a % b

quotient, remainder = divide_and_remainder(17, 5)
print(quotient, remainder)
```

### Example 2 — Complex

```python
def analyze_marks(marks):
    total = sum(marks)
    average = total / len(marks)
    passed = [mark for mark in marks if mark >= 50]
    failed = [mark for mark in marks if mark < 50]
    return total, average, passed, failed

total, average, passed, failed = analyze_marks([72, 44, 91, 53, 38])
print(total)
print(average)
print(passed)
print(failed)
```

This is appropriate when all returned values belong to one combined analysis.

---

# 4. Memory and Argument Passing

Understanding how Python handles objects is essential for understanding function behaviour. Many bugs come from misunderstanding what gets changed and what does not.

## 4.1 Variable Memory Model

Python variables store references to objects. Multiple names can refer to the same object, especially when the object is mutable.

### Example 1 — Intermediate

```python
values = [10, 20, 30]
alias = values
alias.append(40)

print(values)
print(alias)
```

Both variables point to the same list object.

### Example 2 — Complex

```python
def attach_tag(record, tag):
    record["tags"].append(tag)

user = {"name": "Lena", "tags": ["student"]}
copy_ref = user

attach_tag(copy_ref, "active")
print(user)
print(copy_ref)
```

The update is visible through both names because they reference the same dictionary.

## 4.2 Immutable vs Mutable Objects

Immutable objects cannot be changed in place. Mutable objects can.

This distinction explains why some changes stay local while others affect shared state.

### Example 1 — Intermediate

```python
name = "unix"
updated = name.upper()

print(name)
print(updated)
```

The original string stays unchanged because strings are immutable.

### Example 2 — Complex

```python
config = {"ports": [22, 80]}
config["ports"].append(443)

print(config)
```

The dictionary and nested list are mutable, so the structure is modified in place.

## 4.3 Passing Immutable Objects

When an immutable object is passed to a function, rebinding the parameter creates a new value for the local name instead of modifying the caller's original object.

### Example 1 — Intermediate

```python
def bump(value):
    value = value + 5
    return value

count = 10
new_count = bump(count)
print(count)
print(new_count)
```

### Example 2 — Complex

```python
def mask_username(username):
    username = username[:2] + "***"
    return username

original = "administrator"
masked = mask_username(original)
print(original)
print(masked)
```

The function returns a new value rather than mutating the original immutable object.

## 4.4 Passing Mutable Objects

When a mutable object is passed to a function, in-place updates affect the original object seen by the caller.

### Example 1 — Intermediate

```python
def add_log_entry(logs, message):
    logs.append(message)

entries = []
add_log_entry(entries, "system started")
print(entries)
```

### Example 2 — Complex

```python
def update_inventory(stock, item, amount):
    if item not in stock:
        stock[item] = 0
    stock[item] += amount

inventory = {"usb": 5, "ssd": 2}
update_inventory(inventory, "usb", 3)
update_inventory(inventory, "hdmi", 7)
print(inventory)
```

This is a deliberate side effect: the function exists to update a shared structure.

---

# 5. Working with Data Structures in Functions

Functions become far more practical when they operate on collections such as lists and dictionaries.

## 5.1 Lists as Arguments

Lists are useful when a function processes ordered data, windows of values, or repeated entries.

### Example 1 — Intermediate

```python
def count_even_numbers(values):
    total = 0

    for value in values:
        if value % 2 == 0:
            total += 1

    return total

print(count_even_numbers([3, 4, 8, 11, 14]))
```

### Example 2 — Complex

```python
def sliding_averages(values, window_size):
    averages = []

    for start in range(len(values) - window_size + 1):
        window = values[start:start + window_size]
        averages.append(sum(window) / window_size)

    return averages

print(sliding_averages([10, 20, 30, 40, 50], 3))
```

This style appears in monitoring systems, analytics, and time-series calculations.

## 5.2 Dictionaries as Arguments

Dictionaries are useful when data should be accessed by key rather than by position.

### Example 1 — Intermediate

```python
def format_service(service):
    return f"{service['name']} -> {service['status']}"

print(format_service({"name": "nginx", "status": "running"}))
```

### Example 2 — Complex

```python
def average_department_scores(records):
    result = {}

    for department, scores in records.items():
        result[department] = sum(scores) / len(scores)

    return result

data = {
    "networks": [78, 82, 91],
    "security": [88, 90, 84],
    "systems": [70, 76, 80],
}

print(average_department_scores(data))
```

This is common in structured data processing where categories, labels, and fields matter.

## 5.3 Updating Data Structures in Functions

Some functions are designed to mutate a data structure directly instead of returning a new one.

These functions should be named clearly so their side effects are obvious.

### Example 1 — Intermediate

```python
def mark_absent(attendance, student):
    attendance[student] = "absent"

attendance = {"Amir": "present"}
mark_absent(attendance, "Amir")
print(attendance)
```

### Example 2 — Complex

```python
def register_event(metrics, category, value):
    if category not in metrics:
        metrics[category] = []

    metrics[category].append(value)

system_metrics = {}
register_event(system_metrics, "cpu", 47)
register_event(system_metrics, "cpu", 63)
register_event(system_metrics, "memory", 71)
print(system_metrics)
```

This pattern is widely used in aggregation, logging, and incremental processing.

---

# 6. Variable-Length Arguments

In some situations, the exact number or names of arguments cannot be known in advance. Python supports this with `*args` and `**kwargs`.

## 6.1 *args

`*args` collects extra positional arguments into a tuple.

### Example 1 — Intermediate

```python
def multiply_all(*args):
    result = 1

    for value in args:
        result *= value

    return result

print(multiply_all(2, 3, 4))
```

### Example 2 — Complex

```python
def merge_ranges(*ranges):
    merged = []

    for start, end in ranges:
        for value in range(start, end + 1):
            if value not in merged:
                merged.append(value)

    return merged

print(merge_ranges((1, 3), (5, 7), (3, 5)))
```

The function can accept any number of input ranges without changing its definition.

## 6.2 **kwargs

`**kwargs` collects extra keyword arguments into a dictionary.

### Example 1 — Intermediate

```python
def build_profile(**kwargs):
    return kwargs

print(build_profile(name="Dina", role="admin", active=True))
```

### Example 2 — Complex

```python
def render_query(table, **filters):
    clauses = []

    for key, value in filters.items():
        clauses.append(f"{key}='{value}'")

    where_clause = " AND ".join(clauses)
    return f"SELECT * FROM {table} WHERE {where_clause};"

print(render_query("users", role="operator", active="yes", region="eu"))
```

This is useful for optional named settings that vary from call to call.

---

# 7. Functions in Practice

The real value of functions appears when several of them work together to form a complete workflow.

## 7.1 Modular Program Design

Modular design means breaking one larger task into smaller functions where each function has one clear job.

### Example 1 — Intermediate

```python
def read_score():
    return int(input("Score: "))

def classify_score(score):
    return "pass" if score >= 50 else "fail"

def show_score_result(result):
    print(result)
```

Each function has a narrow role: input, processing, and output.

### Example 2 — Complex

```python
def parse_numbers(line):
    return [int(token) for token in line.split()]

def filter_primes(values):
    primes = []

    for value in values:
        if value < 2:
            continue

        is_prime = True
        divisor = 2

        while divisor * divisor <= value:
            if value % divisor == 0:
                is_prime = False
                break
            divisor += 1

        if is_prime:
            primes.append(value)

    return primes

def show_numbers(values):
    print("Primes:", values)

numbers = parse_numbers("10 11 12 13 14 15 16 17")
show_numbers(filter_primes(numbers))
```

This is much easier to understand than one large script block doing everything at once.

## 7.2 Reusing Functions

Reusable functions allow one correct implementation to be used in many parts of a program.

### Example 1 — Intermediate

```python
def is_uppercase_word(word):
    return word.isalpha() and word.isupper()

print(is_uppercase_word("CPU"))
print(is_uppercase_word("Cpu"))
```

### Example 2 — Complex

```python
def normalize_email(email):
    return email.strip().lower()

raw_emails = [" Admin@Site.com ", "USER@site.com", "guest@site.com "]
cleaned = []

for email in raw_emails:
    cleaned.append(normalize_email(email))

print(cleaned)
```

The same helper could also be reused in validation, duplicate detection, and storage operations.

## 7.3 Using Standard Library Functions

Python's standard library provides reliable tools that should be reused whenever they fit the problem.

### Example 1 — Intermediate

```python
import math

def hypotenuse(a, b):
    return math.sqrt(a * a + b * b)

print(hypotenuse(5, 12))
```

### Example 2 — Complex

```python
from collections import Counter

def top_three_words(text):
    counts = Counter(text.lower().split())
    return counts.most_common(3)

print(top_three_words("error warning info error error warning ok info error"))
```

Using the standard library usually leads to code that is clearer and more reliable.

## 7.4 Functions with Files

File-processing programs become easier to reason about when reading, parsing, computation, and reporting are split into separate functions.

### Example 1 — Intermediate

```python
def read_lines(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.readlines()

def count_non_empty_lines(lines):
    total = 0

    for line in lines:
        if line.strip():
            total += 1

    return total
```

### Example 2 — Complex

```python
def parse_sales_lines(lines):
    records = []

    for line in lines:
        product, qty, price = line.strip().split(",")
        records.append({"product": product, "qty": int(qty), "price": float(price)})

    return records

def total_revenue(records):
    revenue = 0

    for record in records:
        revenue += record["qty"] * record["price"]

    return revenue

sample_lines = [
    "usb,3,19.5",
    "ssd,2,79.9",
    "cable,5,4.2",
]

records = parse_sales_lines(sample_lines)
print(total_revenue(records))
```

This pattern is the basis of many report generators and data-analysis scripts.

---

# 8. Practical Applications and Use Cases

Functions matter most when they work together in realistic workflows. This section shows how multiple focused functions form larger solutions.

## 8.1 Command-Line Data Processing Pipeline

A pipeline breaks work into stages such as tokenizing, filtering, and summarizing.

### Example 1 — Intermediate

```python
def tokenize(line):
    return line.lower().split()

def filter_long_words(words, minimum_length):
    return [word for word in words if len(word) >= minimum_length]

def summarize(words):
    return {"count": len(words), "words": words}

words = tokenize("Systems programming teaches reusable design")
long_words = filter_long_words(words, 7)
print(summarize(long_words))
```

### Example 2 — Complex

```python
def parse_log_lines(lines):
    entries = []

    for line in lines:
        level, service, message = line.strip().split("|", 2)
        entries.append({"level": level, "service": service, "message": message})

    return entries

def filter_errors(entries):
    return [entry for entry in entries if entry["level"] == "ERROR"]

def count_by_service(entries):
    counts = {}

    for entry in entries:
        service = entry["service"]
        counts[service] = counts.get(service, 0) + 1

    return counts

log_lines = [
    "INFO|auth|login succeeded",
    "ERROR|db|connection timeout",
    "ERROR|db|replica unavailable",
    "ERROR|auth|token expired",
]

entries = parse_log_lines(log_lines)
errors = filter_errors(entries)
print(count_by_service(errors))
```

This demonstrates how functions form a readable analysis pipeline.

## 8.2 Configuration Validation and Reporting

Another common use case is validating structured records and building a report from the results.

### Example 1 — Intermediate

```python
def validate_port(port):
    return 1 <= port <= 65535

def check_service_config(name, port):
    status = "valid" if validate_port(port) else "invalid"
    return {"service": name, "port": port, "status": status}

print(check_service_config("web", 8080))
print(check_service_config("db", 70000))
```

### Example 2 — Complex

```python
def validate_record(record):
    errors = []

    if not record.get("host"):
        errors.append("missing host")

    port = record.get("port")
    if not isinstance(port, int) or not (1 <= port <= 65535):
        errors.append("invalid port")

    if record.get("protocol") not in {"http", "https", "ssh"}:
        errors.append("invalid protocol")

    return errors

def build_validation_report(records):
    report = []

    for record in records:
        report.append({
            "name": record.get("name", "unknown"),
            "errors": validate_record(record),
        })

    return report

configs = [
    {"name": "frontend", "host": "site.local", "port": 443, "protocol": "https"},
    {"name": "admin", "host": "", "port": 22, "protocol": "ssh"},
    {"name": "legacy", "host": "legacy.local", "port": 90000, "protocol": "ftp"},
]

print(build_validation_report(configs))
```

This structure is common in deployment tools, validation scripts, and systems administration utilities.

---

# Summary

Week 10 is about using functions to turn scripts into well-structured programs.

The central lessons are:

- define focused functions with clear responsibilities
- design parameters so calls are readable and safe
- return values so functions can be combined into larger workflows
- understand mutability so side effects are predictable
- use functions to process lists, dictionaries, files, and structured records
- apply functions to realistic pipelines such as parsing, validation, aggregation, and reporting

These ideas are foundational for writing maintainable Python code in the rest of the course.

---

**End of Week 10**
