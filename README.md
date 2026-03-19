
# Unix System Programming (Bash & Python)

Unix Systems Programming lecture materials and demos.

This repository contains **lecture notes, examples, and scripts** used in the subject **32547 – Unix Systems Programming**.

The material introduces Unix fundamentals, command-line tools, file systems, and Bash scripting.

---

# Lecture Structure

<details>
<summary><strong>Week 01 — Introduction to Unix Systems Programming</strong></summary>

### Topics covered

- Overview of Unix Systems Programming
- Operating system fundamentals
- Unix architecture (Kernel, Shell, CLI vs GUI)
- Linux and Unix environments
- Basic command-line navigation

### Commands introduced

- `man`
- `pwd`
- `mkdir`
- `cd`
- `rmdir`

</details>

---

<details>
<summary><strong>Week 02 — Filesystem and File Control</strong></summary>

### Topics covered

- Unix filesystem structure
- Absolute vs relative paths
- File permissions model
- Ownership and groups
- Managing files and directories

### Commands introduced

- `touch`
- `ls`
- `cp`
- `mv`
- `find`
- `rm`
- `tar`
- `gzip`

### Concepts

- File permissions
- Ownership
- Globbing patterns

</details>

---

<details>
<summary><strong>Week 03 — Text Processing and Bash Scripting</strong></summary>

### Topics covered

- Processing text files with Unix tools
- Viewing and inspecting files
- Combining commands in Bash
- Shell variables and environment variables
- Conditional statements
- Writing simple Bash scripts

### Commands introduced

- `cat`
- `less`
- `more`
- `head`
- `tail`
- `sort`
- `wc`
- `echo`
- `read`

### Concepts

- Command chaining
- Command substitution
- Shell aliases
- PATH environment variable
- Bash scripting basics

### Scripts included

- `preview_cities.sh`
- `check_capital.sh`
- `slice_cities.sh`

</details>

---

<details>
<summary><strong>Week 04 — Piping, Redirection, and Shell Control Structures</strong></summary>

### Topics covered

- Unix pipelines and command chaining
- Standard streams (stdin, stdout, stderr)
- Input and output redirection
- Error redirection and null device usage
- Special shell parameters
- Unix text processing filters
- Looping constructs and interactive menus in Bash

### Commands introduced

- `cut`
- `awk`
- `uniq`
- `join`
- `split`
- `paste`
- `tr`
- `pr`
- `diff`

### Concepts

- Pipelines and process chaining
- File descriptors (0, 1, 2)
- Text processing filters
- Structured shell loops (`for`, `while`)
- Interactive shell menus using `select` and `case`

### Data files used

- `animals.txt`
- `list.txt`

</details>

---

<details>
<summary><strong>Week 05 — Regular Expressions, grep, and sed</strong></summary>

### Topics covered

- Regular expressions (regex)
- Pattern matching and text filtering
- Regex operators and quantifiers
- Character classes and anchors
- Grouping and alternation
- Searching with `grep`
- Extended regex with `grep -E`
- grep options for output control
- Stream editing with `sed`
- Substitution, deletion, and in-place editing

### Commands introduced

- `grep`
- `sed`

### Concepts

- Regex patterns
- Quantifiers (`*`, `+`, `?`, `{n}`, `{n,m}`)
- Character classes (`[a-z]`, `[0-9]`, `.`)
- Anchors (`^`, `$`)
- Grouping and alternation (`()`, `|`)
- Stream editing

### Data files used

- `demo.txt`

</details>

---

# Requirements

To run the examples you need:

- Linux / macOS terminal or WSL
- Bash shell
- Basic Unix utilities installed (standard on Unix systems)

---

#### 👤 <sub><em>Author: *Georges Bou Ghantous*</em></sub>
