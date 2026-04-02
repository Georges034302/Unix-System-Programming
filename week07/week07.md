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

Python extends Unix scripting by providing structured programming, better abstraction, and stronger data handling capabilities.

## 1.1 Why Python in Systems Programming

Shell scripting is effective for:
- command orchestration
- pipelines
- simple automation

However, it becomes limited when:
- logic becomes nested
- data structures are required
- scripts scale in size

Python addresses these limitations by:
- enabling structured logic
- supporting complex data types
- improving readability and maintainability

## 1.2 Python vs Shell: Roles and Boundaries

```text
Shell → system interaction (commands, pipes, automation)
Python → computation, logic, data processing
```

---

# 2. Getting Started with Python

## 2.1 Running Python Scripts

```bash
# run script using interpreter
python script.py
```

## 2.2 Shebang and Execution Permissions

```python
# shebang tells OS which interpreter to use
#!/usr/bin/env python3

print("Hello")
```

```bash
# make script executable
chmod +x script.py

# execute directly
./script.py
```

## 2.3 Script Structure and Execution Flow

```text
Python executes sequentially:
line 1 → line 2 → line 3

Control flow modifies execution:
if / loops / functions
```

---

# 3. Core Python Syntax

## 3.1 Printing and Basic Output

```python
# print string
print("Hello World")

# print multiple values (auto space separated)
print("Unix", "Systems", "Programming")
```

## 3.2 Variables and Object Model

```python
# assign variable
x = 10

# assign another reference to same object
y = x

# modifying x creates new object (immutable type)
x = x + 5

print(x, y)
# y remains original reference
```

## 3.3 Strings and Basic Operations

```python
# concatenation
a = "Unix"
b = "Programming"
print(a + " " + b)

# repetition
print(a * 3)

# indexing
print(a[0])  # first character

# slicing
print(a[0:3])  # substring
```

---

# 4. Data Types and Expressions

## 4.1 Primitive Types

```python
# numeric types
a = 10
b = 3.14

# string
c = "text"
```

## 4.2 Mutable vs Immutable Objects

```python
# immutable example
x = "hello"
x = x + " world"  # new object created

# mutable example
lst = [1, 2]
lst.append(3)  # modifies existing object
```

## 4.3 Operators and Expressions

### Arithmetic Operators

```python
# demonstrate arithmetic
a = 7
b = 2

print(a + b)   # addition → 9
print(a - b)   # subtraction → 5
print(a * b)   # multiplication → 14
print(a / b)   # division → 3.5
print(a // b)  # floor division → 3
print(a % b)   # remainder → 1
print(a ** b)  # exponent → 49
```

### Assignment Operators

```python
# compound assignments
x = 10
x += 5   # x = x + 5
x *= 2   # x = x * 2
print(x)
```

### Comparison Operators

```python
# comparisons return boolean
x = 5
y = 10

print(x == y)  # False
print(x != y)  # True
print(x < y)   # True
print(x > y)   # False
```

### Logical Operators

```python
# logical evaluation
a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False
```

### Membership Operators

```python
# check membership in list
lst = [1, 2, 3]

print(2 in lst)     # True
print(5 not in lst) # True
```

## 4.4 Identity vs Equality (`is` vs `==`)

```python
# demonstrate identity vs equality
a = [1, 2]
b = [1, 2]
c = a

print(a == b)  # True (values equal)
print(a is b)  # False (different objects)
print(a is c)  # True (same object)
```

---

# 5. Control Flow and Logic

## 5.1 Conditional Statements

```python
# simple condition
x = 15

if x > 10:
    print("x is greater than 10")
```

## 5.2 Indentation and Block Structure

```python
# indentation defines scope
x = 5

if x > 0:
    print("Positive")
    print("Still inside block")

print("Outside block")
```

---

# 6. Interfacing with the System

## 6.1 Command-Line Arguments (`sys.argv`)

```python
# print all arguments
import sys

print(sys.argv)  # list of arguments
```

## 6.2 Passing Arguments to Python Scripts

```bash
# run script with arguments
python script.py 10 20
```

## 6.3 Basic Script Interaction Patterns

```python
# program that processes arguments safely
import sys

# ensure correct usage
if len(sys.argv) < 3:
    print("Usage: script.py <num1> <num2>")
    exit()

# parse inputs
a = int(sys.argv[1])
b = int(sys.argv[2])

# perform operation
result = a + b

print("Sum =", result)
```

---

# 7. Python vs Bash: Practical Mapping

```text
Python                Bash
---------------------------------------
print("hello")        echo hello
x = 10                X=10
if x > 5:             if [ $x -gt 5 ]
sys.argv[1]           $1
```

---

# 8. Choosing the Right Tool

## 8.1 When to Use Bash

- file operations
- command chaining
- automation scripts

## 8.2 When to Use Python

- data processing
- complex logic
- reusable scripts

## 8.3 Combining Bash and Python Effectively

```text
Shell script:
- invokes system tools

Python:
- processes outputs and logic
```

---

**End of Week 7**
