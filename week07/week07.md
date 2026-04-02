# Week 7 — Introduction to Python for Unix Systems Programming

## Table of Contents
1. [Introduction to Python in Unix Systems](#1-introduction-to-python-in-unix-systems)  
   1.1 [Why Python in Systems Programming](#11-why-python-in-systems-programming)  
   1.2 [Python vs Shell: Roles and Boundaries](#12-python-vs-shell-roles-and-boundaries)  

2. [Getting Started with Python](#2-getting-started-with-python)  
   2.1 [Running Python Scripts](#21-running-python-scripts)  
   2.2 [Shebang and Execution Permissions](#22-shebang-and-execution-permissions)  
   2.3 [Script Structure and Execution Flow](#23-script-structure-and-execution-flow)  

3. [Core Python Syntax](#3-core-python-syntax)  
   3.1 [Printing and Basic Output](#31-printing-and-basic-output)  
   3.2 [Variables and Object Model](#32-variables-and-object-model)  
   3.3 [Strings and Basic Operations](#33-strings-and-basic-operations)  

4. [Data Types and Expressions](#4-data-types-and-expressions)  
   4.1 [Primitive Types](#41-primitive-types)  
   4.2 [Mutable vs Immutable Objects](#42-mutable-vs-immutable-objects)  
   4.3 [Operators and Expressions](#43-operators-and-expressions)  
   4.4 [Identity vs Equality (`is` vs `==`)](#44-identity-vs-equality-is-vs-)  

5. [Control Flow and Logic](#5-control-flow-and-logic)  
   5.1 [Conditional Statements](#51-conditional-statements)  
   5.2 [Indentation and Block Structure](#52-indentation-and-block-structure)  

6. [Interfacing with the System](#6-interfacing-with-the-system)  
   6.1 [Command-Line Arguments (`sys.argv`)](#61-command-line-arguments-sysargv)  
   6.2 [Passing Arguments to Python Scripts](#62-passing-arguments-to-python-scripts)  
   6.3 [Basic Script Interaction Patterns](#63-basic-script-interaction-patterns)  

7. [Python vs Bash: Practical Mapping](#7-python-vs-bash-practical-mapping)  

8. [Choosing the Right Tool](#8-choosing-the-right-tool)  
   8.1 [When to Use Bash](#81-when-to-use-bash)  
   8.2 [When to Use Python](#82-when-to-use-python)  
   8.3 [Combining Bash and Python Effectively](#83-combining-bash-and-python-effectively)  

---

# 1. Introduction to Python in Unix Systems

Python complements shell scripting by enabling structured logic and complex data manipulation.

## 1.1 Why Python in Systems Programming

- Shell is limited for complex logic  
- Python enables:
  - data processing
  - structured programs
  - maintainability  

## 1.2 Python vs Shell: Roles and Boundaries

```text
Shell → orchestration (commands, pipelines)
Python → logic and data processing
```

---

# 2. Getting Started with Python

## 2.1 Running Python Scripts

```bash
python script.py
```

## 2.2 Shebang and Execution Permissions

```python
#!/usr/bin/env python3
print("Hello")
```

```bash
chmod +x script.py
./script.py
```

## 2.3 Script Structure and Execution Flow

```text
top → bottom execution
control structures modify flow
```

---

# 3. Core Python Syntax

## 3.1 Printing and Basic Output

```python
# print a simple string
print("Hello World")

# print multiple values
print("Hello", "Unix", "Systems")
```

## 3.2 Variables and Object Model

```python
# assign a variable
name = "Sydney"

# variables store references
print("Hello " + name)
```

## 3.3 Strings and Basic Operations

```python
# string concatenation
a = "Unix"
b = "Programming"
print(a + " " + b)

# repetition
print(a * 3)
```

---

# 4. Data Types and Expressions

## 4.1 Primitive Types

```python
x = 10        # int
y = 3.14      # float
z = "text"    # string
```

## 4.2 Mutable vs Immutable Objects

```python
# immutable example
a = "hello"
a = "world"  # new object created

# mutable example
lst = [1,2]
lst.append(3)  # same object updated
```

## 4.3 Operators and Expressions

### Arithmetic Operators

```python
# arithmetic operations
a = 10
b = 3

print(a + b)   # addition
print(a - b)   # subtraction
print(a * b)   # multiplication
print(a / b)   # division
print(a // b)  # floor division
print(a % b)   # modulus
print(a ** b)  # exponent
```

### Assignment Operators

```python
# compound assignment
x = 5
x += 3
x *= 2
print(x)
```

### Comparison Operators

```python
# comparisons
x = 10
y = 20

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
```

### Logical Operators

```python
# logical operations
x = True
y = False

print(x and y)
print(x or y)
print(not x)
```

### Membership Operators

```python
# membership
lst = [1,2,3]

print(2 in lst)
print(5 not in lst)
```

## 4.4 Identity vs Equality (`is` vs `==`)

```python
# equality vs identity
a = [1,2]
b = [1,2]
c = a

print(a == b)  # True (same value)
print(a is b)  # False (different objects)
print(a is c)  # True (same object)
```

---

# 5. Control Flow and Logic

## 5.1 Conditional Statements

```python
# simple condition
x = 10

if x > 5:
    print("Greater than 5")
```

## 5.2 Indentation and Block Structure

```python
# indentation defines block
x = 10

if x > 5:
    print("A")
    print("B")
```

---

# 6. Interfacing with the System

## 6.1 Command-Line Arguments (`sys.argv`)

```python
# print first argument
import sys

print(sys.argv[1])
```

## 6.2 Passing Arguments to Python Scripts

```bash
# pass arguments
python script.py hello world
```

## 6.3 Basic Script Interaction Patterns

```python
# script using arguments and logic
import sys

# check argument count
if len(sys.argv) < 2:
    print("Usage: script.py <number>")
    exit()

# convert argument to integer
num = int(sys.argv[1])

# check even or odd
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

---

# 7. Python vs Bash: Practical Mapping

```text
Python                Bash
---------------------------------------
print("hello")        echo hello
var = "x"             VAR=x
if x > 5:             if [ $x -gt 5 ]
sys.argv[1]           $1
```

---

# 8. Choosing the Right Tool

## 8.1 When to Use Bash

- simple automation
- command chaining

## 8.2 When to Use Python

- complex logic
- data manipulation

## 8.3 Combining Bash and Python Effectively

```text
Shell → run commands
Python → process results
```

---

**End of Week 7**
