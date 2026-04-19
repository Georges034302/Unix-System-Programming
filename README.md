
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
<summary><strong>Week 05 — Regular Expressions, grep, sed, and Bash Functions</strong></summary>

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
- Introduction to Bash functions
- Function syntax, parameters, and return values
- Using functions for modular scripting

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
- Function definition and execution
- Positional parameters (`$1`, `$2`, `$@`, `$#`)
- Exit status and return values (`$?`, `return`)

### Data files used

- `demo.txt`

</details>

---

<details>
<summary><strong>Week 06 — Unix Filesystem Internals</strong></summary>

### Topics covered

- Filesystem internal structure
- Partition layout (boot block, superblock, inode table, data blocks)
- Inodes and file metadata
- Block addressing (direct and indirect pointers)
- File size calculation using block pointers
- Directories and path resolution
- Hard links and link counts
- Symbolic (soft) links and differences from hard links

### Commands introduced

- `ls -i`
- `stat`
- `ln`

### Concepts

- Filesystem layout and components
- Inode structure and metadata
- Filename vs inode mapping
- Direct, single, double, and triple indirect pointers
- Directory as filename-to-inode mapping
- Path resolution process
- Hard links vs symbolic links
- Link counts and file deletion behavior

### Data files used

- `demo.txt`

</details>

---

<details>
<summary><strong>Week 07 — Introduction to Python for Unix Systems Programming</strong></summary>

### Topics covered

- Python as a Unix scripting language
- Running Python scripts in Unix environments
- Shebang and execution permissions
- Python script structure and execution flow
- Variables and Python object model
- Primitive data types and expressions
- Mutable vs immutable objects
- Arithmetic, assignment, comparison, and logical operators
- Membership and identity operators
- Strings and string manipulation
- String slicing, indexing, and methods
- String formatting (`print`, `format`, f-strings, printf-style)
- Control flow using `if`, `elif`, and `else`
- Nested conditional logic
- Switch-style control using `match`
- Indentation and block structure in Python
- Passing arguments to scripts using `sys.argv`
- Reading user input using `input()`

### Concepts

- Python as a complement to Bash scripting
- Sequential execution model
- Variable binding and object references
- Expression evaluation and operator precedence
- String immutability and transformation
- Structured decision logic
- Command-line arguments vs interactive input
- Script portability using shebang

</details>

---

<details>
<summary><strong>Week 08 — Loops and Regular Expressions in Python</strong></summary>

### Topics covered

- Iteration over sequences using `for`
- Sentinel-controlled loops using `while`
- Counting and accumulation patterns
- Processing continuous input streams
- Reading multiple lines of input
- Introduction to regular expressions (regex)
- Pattern matching concepts
- The `re` module in Python
- Regex metacharacters and quantifiers
- Anchors, grouping, and alternation
- Special sequences (`\d`, `\w`, `\s`)
- Greedy vs non-greedy matching
- Word boundaries and operator precedence
- Core regex functions:
  - `re.search`
  - `re.findall`
  - `re.split`
  - `re.sub`
  - `re.match`
- Working with match objects
- Line-based processing from STDIN

### Concepts

- Iterative processing of text and data
- Loop control and termination conditions
- Accumulators and counters
- Stream processing model (input → process → output)
- Pattern-based text matching
- Extracting structured data from text
- Transforming and sanitising text
- Using regex for validation and parsing
- Building reusable text-processing scripts

</details>

---

# Requirements

To run the examples you need:

- Linux / macOS terminal or WSL
- Bash shell
- Basic Unix utilities installed (standard on Unix systems)

---

#### 👤 <sub><em>Author: *Georges Bou Ghantous*</em></sub>
