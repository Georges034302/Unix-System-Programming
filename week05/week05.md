# Week 5 — Regular Expressions, grep, and sed

## Table of Contents
1. [Regular Expressions Basics](#1-regular-expressions-basics)  
2. [Regex Operators and Quantifiers](#2-regex-operators-and-quantifiers)  
3. [Character Classes and Matching](#3-character-classes-and-matching)  
4. [Anchors and Position Matching](#4-anchors-and-position-matching)  
5. [Grouping and Alternation](#5-grouping-and-alternation)  
6. [The grep Command](#6-the-grep-command)  
7. [grep with Regular Expressions](#7-grep-with-regular-expressions)  
8. [grep Options and Output Control](#8-grep-options-and-output-control)  
9. [The sed Stream Editor](#9-the-sed-stream-editor)
10. [Bash Functions](#10-bash-functions)  


Dataset used in examples:

- `demo.txt`

---

# 1. Regular Expressions Basics

## Definition

A **regular expression (regex)** is a pattern used to **match text strings**.

Regular expressions allow you to:

- search text
- filter text
- validate formats
- perform replacements

Regex is widely used in:

- Unix commands (`grep`, `sed`, `awk`)
- programming languages
- editors
- search tools

Example regex:

```bash
p[aui]nt
```

Matches:

```
pant
pint
punt
```

---

# 2. Regex Operators and Quantifiers

These operators control **how many times a pattern can appear**.

| Operator | Meaning |
|---|---|
| `*` | zero or more occurrences |
| `+` | one or more occurrences |
| `?` | zero or one occurrence |
| `{n}` | exactly n times |
| `{n,m}` | between n and m times |

## Examples

```bash
grep -E 'e+' demo.txt
# match lines containing one or more "e"
```

```bash
grep -E '[0-9]{2}' demo.txt
# match lines containing exactly two consecutive digits
```

```bash
grep -E '[0-9]{2,4}' demo.txt
# match lines containing between 2 and 4 digits
```

```bash
grep -E 'o?' demo.txt
# match lines containing optional "o"
```

---

# 3. Character Classes and Matching

Character classes define **sets of characters to match**.

| Pattern | Meaning |
|---|---|
| `.` | any single character |
| `[abc]` | a, b, or c |
| `[a-z]` | lowercase letters |
| `[A-Z]` | uppercase letters |
| `[0-9]` | digits |
| `[^A-Z]` | not uppercase |

## Examples

```bash
grep '[A-Z]' demo.txt
# match lines containing uppercase letters
```

```bash
grep '[0-9]' demo.txt
# match lines containing digits
```

```bash
grep '[A-Z][a-z]' demo.txt
# match uppercase followed by lowercase letter
```

```bash
grep '[^a-zA-Z]' demo.txt
# match lines containing characters that are not letters
```

---

# 4. Anchors and Position Matching

Anchors match **positions in the line**, not characters.

| Anchor | Meaning |
|---|---|
| `^` | start of line |
| `$` | end of line |

## Examples

```bash
grep '^#' demo.txt
# match lines starting with "#"
```

```bash
grep '\$$' demo.txt
# match lines ending with "$"
```

```bash
grep '^What' demo.txt
# match lines beginning with the word "What"
```

```bash
grep '^$' demo.txt
# match blank lines
```

```bash
grep -v '^$' demo.txt
# print only non-empty lines
```

---

# 5. Grouping and Alternation

Grouping allows **multiple patterns** to be treated as one.

| Operator | Meaning |
|---|---|
| `( )` | grouping |
| `|` | OR operator |

## Examples

```bash
grep -E 'grep|sed' demo.txt
# match lines containing either "grep" or "sed"
```

```bash
grep -E '(grep|sed)' demo.txt
# same as above but explicitly grouped
```

```bash
grep -E '[A-Z].*[0-9]' demo.txt
# match lines containing uppercase letters followed later by digits
```

```bash
grep -E '[0-9]{4}' demo.txt
# match four-digit numbers
```

---

# 6. The grep Command

## Definition

`grep` searches files for lines matching a **pattern or regular expression**.

## Usage

```bash
grep PATTERN file
```

## Examples

```bash
grep unix demo.txt
# print lines containing the word "unix"
```

```bash
grep grep demo.txt
# print lines mentioning the word "grep"
```

```bash
grep sed demo.txt
# print lines mentioning the word "sed"
```

```bash
grep '#' demo.txt
# print lines containing the "#" character
```

---

# 7. grep with Regular Expressions

Regular expressions allow **advanced pattern matching**.

Always **quote regex patterns** so the shell does not expand them.

## Examples

```bash
grep -E '[0-9]{3}' demo.txt
# match lines containing three consecutive digits
```

```bash
grep -E '^#' demo.txt
# match comment lines beginning with "#"
```

```bash
grep -E 'grep|sed' demo.txt
# match lines containing either grep or sed
```

```bash
grep -E '[A-Z].*[0-9]' demo.txt
# uppercase letter followed later by a digit
```

---

# 8. grep Options and Output Control

Common grep options:

| Option | Meaning |
|---|---|
| `-i` | ignore case |
| `-n` | show line numbers |
| `-c` | count matches |
| `-v` | invert match |
| `-F` | fixed string search |
| `-E` | extended regex |

## Examples

```bash
grep -i unix demo.txt
# case-insensitive search for "unix"
```

```bash
grep -n grep demo.txt
# print matching lines with line numbers
```

```bash
grep -c grep demo.txt
# count number of matching lines
```

```bash
grep -v '#' demo.txt
# show lines that do not contain "#"
```

```bash
grep -F 'GREP & SED' demo.txt
# fixed string search without regex interpretation
```

---

# 9. The sed Stream Editor

## Definition

`sed` is a **stream editor** used to perform text transformations.

It reads input line-by-line, applies commands, and outputs the result.

Typical uses:

- substitution (search/replace)
- deleting lines
- inserting lines
- printing selected lines

---

## 9.1 Print and Selection

```bash
sed '=' demo.txt
# print line numbers
```

```bash
sed -n '1,5p' demo.txt
# print lines 1 to 5
```

```bash
sed -n '$p' demo.txt
# print the last line
```

```bash
sed -n '/grep/Ip' demo.txt
# print lines containing "grep" ignoring case
```

---

## 9.2 Substitution

```bash
sed 's/unix/linux/' demo.txt
# replace the first occurrence of "unix" with "linux"
```

```bash
sed 's/unix/linux/g' demo.txt
# replace all occurrences of "unix"
```

```bash
sed 's/[0-9]/X/g' demo.txt
# replace digits with X
```

```bash
sed -E 's/([A-Za-z]+):[ ]*(.+)/\1 => \2/' demo.txt
# demonstrate capture groups and backreferences
```

---

## 9.3 Delete Lines

```bash
sed '5,10d' demo.txt
# delete lines 5 to 10
```

```bash
sed '/grep/d' demo.txt
# delete lines containing "grep"
```

```bash
sed '/grep/!d' demo.txt
# keep only lines containing "grep"
```

---

## 9.4 Insert and Modify Lines

```bash
sed '3i\>>> INSERTED LINE' demo.txt
# insert a line before line 3
```

```bash
sed '3c\Replaced Line' demo.txt
# replace line 3 with new text
```

---

## 9.5 In-place Editing

```bash
sed -i 's/unix/linux/g' demo.txt
# edit the file directly and replace all occurrences
```

```bash
sed -i.bak 's/unix/linux/g' demo.txt
# edit file but keep a backup copy
```

---

# 10. Bash Functions

## Definition

A **function** in Bash is a reusable block of code that performs a specific task.

Functions help to:

- reduce repetition  
- organise scripts  
- improve readability  
- enable modular scripting  

---

## 10.1 Basic Syntax

```bash
function_name() {
    commands
}
```

or

```bash
function function_name {
    commands
}
```

---

## 10.2 Simple Function Example

```bash
greet() {
    echo "Hello, Unix!"
}

greet
```

---

## 10.3 Functions with Parameters

Functions can accept arguments.

```bash
greet() {
    echo "Hello, $1"
}

greet Georges
```

---

## 10.4 Using Multiple Parameters

```bash
add() {
    result=$(($1 + $2))
    echo $result
}

add 5 3
```

---

## 10.5 Return Values

Bash functions return an exit status (0–255).

```bash
check_number() {
    if [ $1 -gt 10 ]; then
        return 0
    else
        return 1
    fi
}

check_number 15
echo $?
```

---

## 10.6 Practical Example

```bash
search_file() {
    grep -i "$1" "$2"
}

search_file unix demo.txt
```
---

## 10.7 Advanced Function Examples

### Example 1 — File Validation and Search

```bash
# This function safely searches for a pattern in a file.
# It validates:
# 1. Correct number of arguments
# 2. File existence
# Then performs a case-insensitive search with line numbers.

search_safe() {
    if [ $# -ne 2 ]; then
        echo "Usage: search_safe <pattern> <file>"
        return 1
    fi

    if [ ! -f "$2" ]; then
        echo "Error: File not found"
        return 2
    fi

    grep -in "$1" "$2"
}

search_safe unix demo.txt
```

---

### Example 2 — Logging Wrapper Function

```bash
# This function executes any command passed as arguments.
# It logs:
# - the command being executed
# - success or failure status
# Useful for debugging and automation scripts.

log_and_run() {
    echo "[INFO] Running: $@"
    "$@"
    status=$?

    if [ $status -eq 0 ]; then
        echo "[SUCCESS]"
    else
        echo "[ERROR] Exit code: $status"
    fi

    return $status
}

log_and_run ls -l
log_and_run grep unix demo.txt
```

---

### Example 3 — File Processing Pipeline

```bash
# This function processes a file by:
# 1. Checking if the file exists
# 2. Converting all text to uppercase
# 3. Sorting the content
# 4. Removing duplicate lines
# Demonstrates combining multiple Unix tools in a pipeline.

process_file() {
    if [ ! -f "$1" ]; then
        echo "File not found"
        return 1
    fi

    cat "$1" | tr 'a-z' 'A-Z' | sort | uniq
}

process_file demo.txt
```
---

## 10.8 Key Notes

- `$1`, `$2`, ... represent positional arguments passed to the function  
- `$#` represents the total number of arguments  
- `$@` represents all arguments as separate values (preserves spacing)  
- `$*` represents all arguments as a single string  
- `$?` stores the exit status of the last executed command (0 = success)  
- `return` sets the function exit status (0–255)  
- Use `"$@"` when forwarding arguments to preserve correctness  
- Always quote variables (`"$1"`, `"$@"`) to avoid word splitting issues  
- Functions improve modularity, readability, and reuse in scripts  

---

**End of Week 5**
