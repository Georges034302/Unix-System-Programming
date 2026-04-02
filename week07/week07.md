# Week 7 — Introduction to Python for Unix Systems Programming

## Table of Contents
1. [Python in Unix Systems](#1-python-in-unix-systems)  
2. [Core Python Foundations](#2-core-python-foundations)  
   2.1 [Basic Output](#21-basic-output)  
   2.2 [Variables and Object Model](#22-variables-and-object-model)  
   2.3 [Primitive Data Types and Expressions](#23-primitive-data-types-and-expressions)  
   2.4 [Mutable and Immutable Objects](#24-mutable-and-immutable-objects)  
3. [Operators and Expressions](#3-operators-and-expressions)  
   3.1 [Arithmetic Operators](#31-arithmetic-operators)  
   3.2 [Assignment Operators](#32-assignment-operators)  
   3.3 [Comparison Operators](#33-comparison-operators)  
   3.4 [Logical Operators](#34-logical-operators)  
   3.5 [Membership Operators](#35-membership-operators)  
   3.6 [Identity vs Equality](#36-identity-vs-equality)  
4. [Strings and String Formatting](#4-strings-and-string-formatting)  
5. [Control Flow and Logic](#5-control-flow-and-logic)  
6. [Interfacing with the System](#6-interfacing-with-the-system)  

---

# 1. Python in Unix Systems

Python complements shell scripting by enabling structured logic, better abstraction, and scalable scripting.

```text
Shell → orchestration (commands, pipes)
Python → logic and data processing
```

---

# 2. Core Python Foundations

## 2.1 Basic Output

```python
# print a simple message
print("Hello World")

# print multiple values (auto spacing)
print("Unix", "Systems", "Programming")
```

## 2.2 Variables and Object Model

```python
# variables store references to objects
x = 10
y = x  # y points to same object

# modifying x creates a new object (integers are immutable)
x = x + 5

print(x)  # 15
print(y)  # 10
```

## 2.3 Primitive Data Types and Expressions

```python
# integer
a = 10

# float
b = 3.14

# string
c = "text"

# expression evaluation
result = a + 5 * 2
print(result)  # precedence applies
```

## 2.4 Mutable and Immutable Objects

```python
# immutable example (string)
s = "hello"
s2 = s

# modifying creates new object
s = s + " world"

print(s)   # new object
print(s2)  # unchanged

# mutable example (list)
lst = [1, 2]
lst2 = lst

lst.append(3)

print(lst)   # modified
print(lst2)  # same object affected
```

---

# 3. Operators and Expressions

## 3.1 Arithmetic Operators

```python
# arithmetic operations
a = 7
b = 2

print(a + b)   # addition
print(a - b)   # subtraction
print(a * b)   # multiplication
print(a / b)   # division
print(a // b)  # floor division
print(a % b)   # modulus
print(a ** b)  # exponentiation
```

## 3.2 Assignment Operators

```python
# compound assignment
x = 10

x += 5   # add and assign
x *= 2   # multiply and assign

print(x)
```

## 3.3 Comparison Operators

```python
# comparison operations
x = 5
y = 10

print(x == y)  # equality
print(x != y)  # not equal
print(x < y)
print(x > y)
print(x <= y)
print(x >= y)
```

## 3.4 Logical Operators

```python
# logical evaluation
a = True
b = False

print(a and b)  # both must be True
print(a or b)   # one must be True
print(not a)    # negation
```

## 3.5 Membership Operators

```python
# check if element exists
lst = [1, 2, 3]

print(2 in lst)      # True
print(5 not in lst)  # True
```

## 3.6 Identity vs Equality

```python
# identity vs equality
a = [1, 2]
b = [1, 2]
c = a

print(a == b)  # same values
print(a is b)  # different objects
print(a is c)  # same object
```

---

# 4. Strings and String Formatting

```python
# basic string
s = "Unix"

# concatenation
print(s + " Programming")

# repetition
print(s * 2)

# string methods
print(s.lower())
print(s.upper())
print(s.replace("Unix", "Python"))

# formatting using f-string
name = "Georges"
print(f"Hello {name}")

# format function
print("Hello {}".format(name))
```

---

# 5. Control Flow and Logic

## If Statement Variants

```python
# if-else
x = 10
if x > 5:
    print("Greater")
else:
    print("Smaller")

# cascaded if-else
x = 0
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")

# nested if
x = 10
if x > 5:
    if x < 20:
        print("Between 5 and 20")

# match (Python 3.10+)
value = 2
match value:
    case 1:
        print("One")
    case 2:
        print("Two")
    case _:
        print("Other")
```

---

# 6. Interfacing with the System

## 6.1 Command-Line Arguments

```python
# access command-line arguments
import sys

print(sys.argv)
```

## 6.2 Passing Arguments

```bash
python script.py 10 20
```

## 6.3 Script Example

```python
# process arguments
import sys

if len(sys.argv) < 3:
    print("Usage: script.py <a> <b>")
    exit()

a = int(sys.argv[1])
b = int(sys.argv[2])

print("Sum =", a + b)
```

---

**End of Week 7**
