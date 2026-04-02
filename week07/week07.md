# Week 7 — Introduction to Python for Unix Systems Programming

## Table of Contents
1. [Python in Unix Systems](#1-python-in-unix-systems)  
   1.1 [Python as a Unix Scripting Language](#11-python-as-a-unix-scripting-language)  
   1.2 [Why Python in Systems Programming](#12-why-python-in-systems-programming)  
   1.3 [Running Python Scripts](#13-running-python-scripts)  
   1.4 [Shebang and Execution Permissions](#14-shebang-and-execution-permissions)  
   1.5 [Script Structure and Execution Flow](#15-script-structure-and-execution-flow)  

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
   4.1 [Strings](#41-strings)  
   4.2 [Basic String Operations](#42-basic-string-operations)  
   4.3 [String Functions and Methods](#43-string-functions-and-methods)  
   4.4 [String Formatting](#44-string-formatting)  
   4.5 [Printf-Style Formatting with `%s`, `%d`, and `%f`](#45-printf-style-formatting-with-s-d-and-f)  

5. [Control Flow and Logic](#5-control-flow-and-logic)  
   5.1 [The `if` Statement](#51-the-if-statement)  
   5.2 [If-Else](#52-if-else)  
   5.3 [Cascaded If-Elif-Else](#53-cascaded-if-elif-else)  
   5.4 [Nested If](#54-nested-if)  
   5.5 [Switch-Style Control with `match`](#55-switch-style-control-with-match)  
   5.6 [Indentation and Block Structure](#56-indentation-and-block-structure)  

6. [Interfacing with the System](#6-interfacing-with-the-system)  
   6.1 [Passing Arguments and Reading User Input](#61-passing-arguments-and-reading-user-input)  
   6.2 [Passing Arguments to Python Scripts](#62-passing-arguments-to-python-scripts)  
   6.3 [Reading User Input](#63-reading-user-input)  

---

# 1. Python in Unix Systems

## Definition

Python is a high-level, general-purpose programming language widely used in Unix and Linux environments for scripting, automation, data handling, and system-oriented tasks.

In Unix systems programming, Python is often introduced after shell scripting because it gives you a practical step forward from Bash. Shell scripting is excellent for invoking commands and connecting utilities together. Python becomes useful when the task requires more structure, more readable logic, stronger data handling, or more maintainable code.

Python does not replace the shell. Instead, it complements it.

## 1.1 Python as a Unix Scripting Language

In a Unix environment, a script is simply a text file containing instructions that the system can execute through an interpreter. In the case of Bash, the interpreter is the shell. In the case of Python, the interpreter is the Python runtime.

Conceptually:

```text
script file
   ↓
interpreter
   ↓
execution of instructions
```

Python is especially attractive in Unix systems because it offers:

- readable syntax
- portability across operating systems
- strong support for files, directories, and text processing
- better support for structured logic than shell scripts
- a large standard library

This makes Python suitable for tasks such as:

- validating input
- processing text files
- handling command-line arguments
- automating repetitive tasks
- building small utilities for system administration

## 1.2 Why Python in Systems Programming

Shell scripts are powerful for command orchestration:

```text
command → pipe → command → redirect output
```

That model is efficient when the task is mostly based on existing Unix tools such as `grep`, `sort`, `awk`, `sed`, `cut`, and `find`.

However, shell scripting becomes harder to manage when you need to:

- store and manipulate structured data
- perform non-trivial calculations
- apply more complex decision logic
- validate different forms of input
- write code that remains readable as it grows

Python helps because it gives you:

- variables with clear assignment rules
- numeric and text processing
- reusable logic
- safer and more readable condition handling
- more maintainable scripts

A useful boundary is:

```text
Shell  → command orchestration and quick automation
Python → data processing, logic, and structured scripting
```

In practice, many real Unix workflows use both.

## 1.3 Running Python Scripts

A Python script can be executed in more than one way.

### Running a script through the interpreter

```bash
python3 script.py
```

This explicitly tells the system to use the Python interpreter to execute `script.py`.

### Running a script directly

```bash
./script.py
```

This only works if:

- the script has executable permission
- the script begins with a valid shebang line

### Example

```python
# this is a minimal Python script
print("Hello from Python")
```

Save it as `hello.py`, then run:

```bash
python3 hello.py
```

Expected output:

```text
Hello from Python
```

## 1.4 Shebang and Execution Permissions

A shebang is the first line of a script and tells Unix which interpreter should be used when the script is executed directly.

Example:

```python
#!/usr/bin/env python3

# print a message to the terminal
print("Python script executed directly")
```

Make the script executable:

```bash
chmod +x hello.py
```

Now you can run it as:

```bash
./hello.py
```

### Why `/usr/bin/env python3` is useful

Using:

```python
#!/usr/bin/env python3
```

is often preferred because it asks the environment to locate `python3` in the current `PATH`. This is generally more portable than hardcoding a specific interpreter path.

## 1.5 Script Structure and Execution Flow

A Python script normally executes from top to bottom.

Basic model:

```text
line 1
   ↓
line 2
   ↓
line 3
   ↓
...
```

That default sequence changes only when control structures are used, such as:

- `if`
- `elif`
- `else`
- loops
- functions
- `match`

### Example

```python
# line 1: assign a value
x = 10

# line 2: print the current value
print(x)

# line 3: update the value
x = x + 5

# line 4: print the updated value
print(x)
```

Expected output:

```text
10
15
```

This illustrates sequential execution: each line runs in order.

---

# 2. Core Python Foundations

## Definition

Core Python foundations refer to the basic language elements that every Python program uses, including output, variables, object references, primitive data types, expressions, and the distinction between mutable and immutable objects.

## 2.1 Basic Output

The `print()` function writes output to standard output, which usually means the terminal.

### Example 1: print a single string

```python
# print a simple greeting
print("Hello, world")
```

### Example 2: print multiple values

```python
# print several values in a single call
# print() automatically separates them with spaces
print("Unix", "Systems", "Programming")
```

Expected output:

```text
Unix Systems Programming
```

### Example 3: print numbers and strings together

```python
# print a label and a number
# print() converts the integer to text for display
print("Week number:", 7)
```

### Example 4: print with expressions

```python
# evaluate the expression first, then print the result
print(10 + 5 * 2)
```

Expected output:

```text
20
```

This is an important point: Python evaluates the expression before printing.

## 2.2 Variables and Object Model

A variable in Python is a name bound to an object.

This is a very important idea. Python variables do not behave like fixed memory boxes in the traditional beginner model. Instead, a variable is better understood as a reference to an object.

Conceptually:

```text
variable name
   ↓
object in memory
```

### Example 1: assigning a string

```python
# create a string object and bind the name city to it
city = "Sydney"

# print the value referenced by city
print(city)
```

### Example 2: rebinding a variable

```python
# city initially refers to one string object
city = "Sydney"

# city is rebound to a different string object
city = "Melbourne"

# the name now refers to the new object
print(city)
```

### Example 3: two names referring to the same object

```python
# x refers to an integer object
x = 10

# y is assigned the same reference
y = x

# both names currently refer to the same integer object
print(x)
print(y)
```

### Example 4: rebinding after an update

```python
# x and y both start by referring to the same integer object
x = 10
y = x

# integers are immutable, so this creates a new integer object for x
x = x + 5

# x now refers to 15, while y still refers to 10
print("x =", x)
print("y =", y)
```

Expected output:

```text
x = 15
y = 10
```

This demonstrates that assignment in Python binds a name to an object, and rebinding can make two names diverge.

## 2.3 Primitive Data Types and Expressions

Primitive data types are the basic built-in types commonly used in simple Python programs.

For this level, the most important are:

- integers (`int`)
- floating-point numbers (`float`)
- strings (`str`)
- booleans (`bool`)

### Integers

Integers represent whole numbers.

```python
# assign an integer
count = 25

# print the integer
print(count)
```

### Floating-point numbers

Floats represent real numbers with decimal points.

```python
# assign a floating-point value
temperature = 23.5

# print the float
print(temperature)
```

### Strings

Strings represent text.

```python
# assign a string
subject = "Unix Systems Programming"

# print the string
print(subject)
```

### Booleans

Booleans represent truth values.

```python
# assign boolean values
is_open = True
is_closed = False

# print boolean values
print(is_open)
print(is_closed)
```

### Expressions

An expression is a combination of values, variables, and operators that Python evaluates to produce a result.

### Example 1: arithmetic expression

```python
# evaluate multiplication before addition
result = 10 + 5 * 2

# print the final value
print(result)
```

### Example 2: using variables in an expression

```python
# assign numeric variables
a = 8
b = 3

# evaluate an expression using variables
result = a * b + 4

# print the computed result
print(result)
```

### Example 3: combining strings in an expression

```python
# combine two strings with concatenation
first = "Unix"
second = "Programming"

# create a new string expression
course = first + " " + second

# print the combined result
print(course)
```

### Example 4: expression with parentheses

```python
# parentheses change the order of evaluation
value = (10 + 5) * 2

# print the result
print(value)
```

Expected output:

```text
30
```

Without parentheses, the result would be different.

## 2.4 Mutable and Immutable Objects

This is one of the most important conceptual topics in Python.

### Definition

An immutable object cannot be changed after it is created.  
A mutable object can be changed in place after creation.

For this week, strings are the clearest way to understand immutability.

### Strings are immutable

Once a string object exists, Python does not modify its internal content. Any apparent "change" actually creates a new string.

### Example 1: string reassignment

```python
# create an initial string object
text = "hello"

# rebind text to a new string object
text = "world"

# print the new reference
print(text)
```

This is not modifying the original string. It is assigning a different string object to the same variable name.

### Example 2: concatenation creates a new string

```python
# create a string
word = "Unix"

# store another name referring to the same original string
alias = word

# concatenation does not modify the original string in place
# it creates a new string object and rebinds word
word = word + " Systems"

# word now refers to the new string
print("word =", word)

# alias still refers to the original string
print("alias =", alias)
```

Expected output:

```text
word = Unix Systems
alias = Unix
```

### Example 3: replacing text in a string

```python
# create a string
title = "Unix Programming"

# replace() returns a new string object
new_title = title.replace("Unix", "Python")

# original string remains unchanged
print("original =", title)
print("new      =", new_title)
```

### Example 4: case conversion creates a new string

```python
# create a string
name = "georges"

# upper() returns a new string
upper_name = name.upper()

# compare original and transformed values
print("original =", name)
print("upper    =", upper_name)
```

### Why this matters

If strings were mutable, changing one name could silently affect other references. Immutability prevents that and makes string behavior more predictable.

### Brief contrast with mutable objects

Lists are mutable.

```python
# create a list
numbers = [1, 2]

# create another name for the same list
alias = numbers

# append modifies the same list object in place
numbers.append(3)

# both names now show the updated list
print("numbers =", numbers)
print("alias   =", alias)
```

Expected output:

```text
numbers = [1, 2, 3]
alias   = [1, 2, 3]
```

This contrast helps explain why immutable strings behave differently from mutable lists.

---

# 3. Operators and Expressions

## Definition

Operators are symbols or keywords that perform operations on values or variables. Expressions are combinations of operands and operators that Python evaluates to produce a result.

## 3.1 Arithmetic Operators

Arithmetic operators are used for mathematical computation.

Main arithmetic operators:

- `+` addition
- `-` subtraction
- `*` multiplication
- `/` division
- `//` floor division
- `%` remainder (modulus)
- `**` exponentiation

### Example 1: basic arithmetic

```python
# assign two integers
a = 7
b = 2

# perform arithmetic operations and print each result
print("a + b =", a + b)   # addition
print("a - b =", a - b)   # subtraction
print("a * b =", a * b)   # multiplication
print("a / b =", a / b)   # exact division as float
print("a // b =", a // b) # floor division
print("a % b =", a % b)   # remainder
print("a ** b =", a ** b) # exponentiation
```

### Example 2: floor division vs normal division

```python
# compare division styles
x = 9
y = 4

# / produces a float
print(x / y)

# // discards the fractional part
print(x // y)
```

### Example 3: modulus for even/odd detection

```python
# test whether a number is even using modulus
number = 14

# if remainder after division by 2 is zero, the number is even
print(number % 2)
```

If the result is `0`, the number is even.

### Example 4: operator precedence

```python
# multiplication happens before addition
result1 = 10 + 5 * 2

# parentheses force addition first
result2 = (10 + 5) * 2

# print both for comparison
print("without parentheses =", result1)
print("with parentheses    =", result2)
```

## 3.2 Assignment Operators

Assignment operators bind values to variables and also support updating variables concisely.

Main assignment forms:

- `=` basic assignment
- `+=`
- `-=`
- `*=`
- `/=`
- `//=`
- `%=`
- `**=`

### Example 1: basic assignment

```python
# assign an initial value
x = 10

# print current value
print(x)
```

### Example 2: addition assignment

```python
# start with an integer
x = 10

# equivalent to x = x + 5
x += 5

# print updated value
print(x)
```

### Example 3: multiple compound assignments

```python
# initialise a value
score = 20

# add 5
score += 5

# multiply by 2
score *= 2

# subtract 10
score -= 10

# print final result
print(score)
```

### Example 4: exponent assignment

```python
# assign an initial base value
value = 3

# raise value to the power of 2 and reassign
value **= 2

# print squared result
print(value)
```

## 3.3 Comparison Operators

Comparison operators compare two values and produce a boolean result: `True` or `False`.

Main comparison operators:

- `==` equal to
- `!=` not equal to
- `<` less than
- `>` greater than
- `<=` less than or equal to
- `>=` greater than or equal to

### Example 1: direct comparison

```python
# assign two values
x = 5
y = 10

# compare and print boolean results
print(x == y)  # equal?
print(x != y)  # not equal?
print(x < y)   # less than?
print(x > y)   # greater than?
print(x <= y)  # less than or equal?
print(x >= y)  # greater than or equal?
```

### Example 2: comparison inside an expression

```python
# compare computed values
a = 3
b = 4

# evaluate whether the square of b is greater than a sum
print((b ** 2) > (a + 5))
```

### Example 3: string comparison

```python
# compare strings lexicographically
print("apple" == "apple")
print("apple" != "Apple")
```

Comparison operators are heavily used in conditional statements.

## 3.4 Logical Operators

Logical operators combine or invert boolean expressions.

Main logical operators:

- `and`
- `or`
- `not`

### Example 1: simple booleans

```python
# define boolean values
a = True
b = False

# test logical combinations
print(a and b)  # True only if both are True
print(a or b)   # True if at least one is True
print(not a)    # invert truth value
```

### Example 2: logical conditions with comparisons

```python
# assign a number
x = 15

# check whether x is inside a range
print(x > 10 and x < 20)

# check whether x is outside a range
print(x < 10 or x > 20)
```

### Example 3: combining validation rules

```python
# sample input values
username = "student"
age = 21

# access is allowed only if both conditions are satisfied
print(username == "student" and age >= 18)
```

## 3.5 Membership Operators

Membership operators test whether a value appears in a sequence or container.

Main membership operators:

- `in`
- `not in`

### Example 1: membership in a list

```python
# create a list of values
numbers = [10, 20, 30, 40]

# test whether specific values exist
print(20 in numbers)
print(50 in numbers)
print(50 not in numbers)
```

### Example 2: membership in a string

```python
# create a string
course = "Unix Systems Programming"

# test whether a substring appears in the string
print("Unix" in course)
print("Python" in course)
```

### Example 3: practical validation example

```python
# store allowed responses
allowed = ["yes", "no", "maybe"]

# candidate input
response = "yes"

# test whether the response is valid
print(response in allowed)
```

## 3.6 Identity vs Equality

This topic is conceptually important and often misunderstood.

### Equality: `==`

`==` checks whether two objects have the same value.

### Identity: `is`

`is` checks whether two names refer to the very same object in memory.

Conceptually:

```text
==  → same value?
is  → same object?
```

### Example 1: equal values, different objects

```python
# create two separate lists with the same contents
a = [1, 2]
b = [1, 2]

# value equality is True because contents match
print(a == b)

# identity is False because these are different list objects
print(a is b)
```

### Example 2: same object through aliasing

```python
# create one list
a = [1, 2]

# c refers to the same list object
c = a

# both value equality and identity are True
print(a == c)
print(a is c)
```

### Example 3: practical interpretation

```python
# create strings
x = "Unix"
y = "Unix"

# value equality checks whether the contents are the same
print(x == y)

# identity asks whether they are the same object
print(x is y)
```

For strings and small integers, identity results can sometimes seem surprising because Python may reuse objects internally. That is why `==` should be used for value comparison, while `is` should be reserved for identity testing.

---

# 4. Strings and String Formatting

## Definition

A string is an ordered sequence of characters used to represent text in Python.

Strings are one of the most important data types in Unix-oriented scripting because scripts frequently process:

- filenames
- paths
- command-line input
- text files
- messages
- logs

## 4.1 Strings

A string can be written with single quotes or double quotes.

### Example 1: single and double quotes

```python
# define strings using single and double quotes
a = 'Unix'
b = "Python"

# print both values
print(a)
print(b)
```

### Example 2: storing a sentence

```python
# assign a longer text string
message = "Welcome to Unix Systems Programming"

# print the full sentence
print(message)
```

### Example 3: indexing characters

```python
# create a string
word = "Python"

# print specific characters by index
print(word[0])  # first character
print(word[1])  # second character
print(word[-1]) # last character
```

### Example 4: slicing a string

```python
# create a string
word = "Programming"

# slice from index 0 up to but not including 6
print(word[0:6])

# slice from index 3 to the end
print(word[3:])

# slice from the start up to index 4
print(word[:4])
```

## 4.2 Basic String Operations

Basic string operations allow you to combine, repeat, inspect, and test strings.

### Concatenation

```python
# join two strings with +
first = "Unix"
second = "Programming"

# insert a space manually between words
result = first + " " + second

# print concatenated result
print(result)
```

### Repetition

```python
# repeat a string multiple times
text = "Hi "

# multiply string by integer
print(text * 3)
```

### Length

```python
# len() returns number of characters
course = "Unix"

# print length
print(len(course))
```

### Membership test with strings

```python
# check whether a substring exists
title = "Unix Systems Programming"

print("Systems" in title)
print("Java" in title)
```

## 4.3 String Functions and Methods

Python provides many useful string methods. Since strings are immutable, these methods return new strings rather than changing the original one in place.

### Case conversion

```python
# create a string
name = "Georges"

# convert to upper and lower case
print(name.upper())
print(name.lower())
```

### Removing surrounding whitespace

```python
# create a string with leading and trailing spaces
text = "   hello world   "

# strip removes spaces at both ends
print(text.strip())
```

### Replacing text

```python
# create a string
message = "Unix Systems Programming"

# replace one substring with another
new_message = message.replace("Unix", "Python")

# print both values to show original is unchanged
print(message)
print(new_message)
```

### Splitting a string

```python
# create a sentence
line = "red,green,blue"

# split around commas into a list
parts = line.split(",")

# print resulting list
print(parts)
```

### Checking prefixes and suffixes

```python
# create a filename
filename = "notes.txt"

# test prefix and suffix
print(filename.startswith("notes"))
print(filename.endswith(".txt"))
```

## 4.4 String Formatting

String formatting is the process of building readable text from variables and expressions.

This is essential in scripts because programs often need to display:

- labels and values
- status messages
- computed results
- user guidance
- formatted output

### Basic print output

```python
# print a label and a variable using multiple arguments
name = "Georges"

# print() inserts a space between arguments
print("Hello", name)
```

### Multiple strings and values

```python
# define several values
course = "USP"
week = 7

# print them together
print("Course:", course, "Week:", week)
```

### Concatenation-based formatting

```python
# concatenate strings manually
city = "Sydney"

# convert or combine text manually
print("City: " + city)
```

This works, but becomes less convenient with many variables.

### Using `format()`

```python
# define values to insert into a template
name = "Georges"
topic = "Python"

# use placeholders replaced by format()
print("Hello {}, welcome to {}.".format(name, topic))
```

### Positional formatting with `format()`

```python
# insert values into specified positions
first = "Unix"
second = "Python"

# use index positions inside braces
print("{1} comes after {0} in this week's lesson.".format(first, second))
```

### Numeric formatting with `format()`

```python
# define a floating-point value
pi = 3.14159265

# format to two decimal places
print("Pi to two decimal places: {:.2f}".format(pi))
```

### Using f-strings

F-strings are usually the clearest and most modern formatting style.

```python
# define variables
name = "Georges"
week = 7

# embed variables directly inside the string
print(f"Hello {name}, welcome to Week {week}.")
```

### F-strings with expressions

```python
# define values
a = 10
b = 5

# include an expression directly inside the f-string
print(f"The sum of {a} and {b} is {a + b}.")
```

### F-strings with formatting control

```python
# define a float
value = 12.34567

# format to two decimal places inside an f-string
print(f"Formatted value: {value:.2f}")
```

## 4.5 Printf-Style Formatting with `%s`, `%d`, and `%f`

Before `format()` and f-strings became common, Python widely used printf-style formatting based on the `%` operator.

This style is still worth understanding because you may see it in older scripts and legacy code.

Common placeholders include:

- `%s` for strings
- `%d` for integers
- `%f` for floating-point numbers

### Example 1: formatting a string with `%s`

```python
# define a string value
name = "Georges"

# insert the string using %s
print("Hello %s" % name)
```

### Example 2: formatting an integer with `%d`

```python
# define an integer value
week = 7

# insert the integer using %d
print("This is week %d" % week)
```

### Example 3: formatting a float with `%f`

```python
# define a floating-point value
pi = 3.14159265

# insert the float using %f
print("Pi is %f" % pi)
```

### Example 4: controlling decimal places with `%f`

```python
# define a floating-point number
value = 12.34567

# format with two decimal places
print("Value = %.2f" % value)
```

### Example 5: formatting multiple values together

```python
# define values of different types
name = "Georges"
age = 45
score = 92.5

# format string, integer, and float in one output line
print("Name: %s, Age: %d, Score: %.1f" % (name, age, score))
```

### Practical note

Printf-style formatting still works, but in modern Python:

- f-strings are usually the clearest option
- `format()` is also common
- `%` formatting is mainly encountered in older code bases

---

# 5. Control Flow and Logic

## Definition

Control flow determines which statements run, in what order, and under what conditions.

In Python, control flow is strongly based on indentation. Blocks are not marked by braces; they are marked by aligned indentation levels.

## 5.1 The `if` Statement

The `if` statement executes a block only when its condition evaluates to `True`.

General form:

```python
if condition:
    statements
```

### Example 1: simple numeric condition

```python
# assign a number
x = 12

# execute block only if condition is true
if x > 10:
    print("x is greater than 10")
```

### Example 2: testing string equality

```python
# assign a mood value
mood = "good"

# compare the string and act conditionally
if mood == "good":
    print("I am happy")
```

## 5.2 If-Else

The `if-else` structure chooses between two alternative paths.

General form:

```python
if condition:
    statements_if_true
else:
    statements_if_false
```

### Example 1: even or odd

```python
# assign a number
number = 9

# test whether the remainder after division by 2 is zero
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### Example 2: access decision

```python
# assign user role
role = "student"

# choose one of two outcomes
if role == "student":
    print("Access granted")
else:
    print("Access denied")
```

## 5.3 Cascaded If-Elif-Else

Use `elif` when there are more than two mutually exclusive choices.

General form:

```python
if condition1:
    ...
elif condition2:
    ...
elif condition3:
    ...
else:
    ...
```

### Example 1: classify a number

```python
# assign a value
x = 0

# test multiple mutually exclusive cases
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
```

### Example 2: grading logic

```python
# assign a mark
mark = 78

# classify into grade bands
if mark >= 85:
    print("High Distinction")
elif mark >= 75:
    print("Distinction")
elif mark >= 65:
    print("Credit")
elif mark >= 50:
    print("Pass")
else:
    print("Fail")
```

This is a good example of cascaded decision logic in academic grading.

## 5.4 Nested If

A nested `if` is an `if` statement placed inside another conditional block.

Use nested logic when one decision should only be considered after another has already succeeded.

### Example 1: range checking

```python
# assign a number
x = 15

# outer condition checks lower bound
if x > 10:
    # inner condition checks upper bound only if outer test passed
    if x < 20:
        print("x is between 10 and 20")
```

### Example 2: login-style logic

```python
# assign status values
username = "student"
password_ok = True

# first verify username
if username == "student":
    # only if username is correct, verify password status
    if password_ok:
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Unknown user")
```

Nested logic should be used carefully. If it becomes too deep, readability suffers.

## 5.5 Switch-Style Control with `match`

Python 3.10 introduced `match`, which provides a switch-style control structure.

This is useful when one value is compared against several fixed cases.

### Example 1: basic match

```python
# assign a menu option
option = 2

# compare option against several alternatives
match option:
    case 1:
        print("Add record")
    case 2:
        print("Delete record")
    case 3:
        print("Update record")
    case _:
        print("Invalid option")
```

The underscore `_` acts as the default case.

### Example 2: matching strings

```python
# assign a command name
command = "start"

# dispatch based on command value
match command:
    case "start":
        print("System starting")
    case "stop":
        print("System stopping")
    case "restart":
        print("System restarting")
    case _:
        print("Unknown command")
```

## 5.6 Indentation and Block Structure

Indentation is not just a formatting preference in Python. It is part of the syntax.

A block begins after a colon `:` and is defined by consistent indentation.

### Correct example

```python
# correct indentation
x = 10

if x > 5:
    print("Inside the block")
    print("Still inside the block")

print("Outside the block")
```

### Meaning of the structure

```text
if x > 5:
    indented lines belong to the if block

non-indented line:
    execution continues outside the block
```

### Why indentation matters

Poor indentation can change logic or produce syntax errors. In Python, indentation directly defines structure, so it must always be consistent and deliberate.

---

# 6. Interfacing with the System

## Definition

Interfacing with the system means allowing a Python script to receive data from its execution environment rather than hardcoding all values inside the program.

In introductory Unix scripting, the two most common interaction mechanisms are:

- passing arguments to the script at execution time
- reading user input interactively while the script is running

Both approaches allow the same script to behave differently depending on what the user provides.

Conceptually:

```text
user input to program
   ├── command-line arguments
   └── interactive keyboard input
```

## 6.1 Passing Arguments and Reading User Input

Python programs can obtain external input in two common ways.

### 1. Command-line arguments

These are values written after the script name when the script is launched.

Example:

```bash
python3 script.py hello 25
```

In this case:

- `script.py` is the script name
- `hello` is the first user-supplied argument
- `25` is the second user-supplied argument

Python stores command-line arguments in `sys.argv`.

### 2. Interactive user input

This is input entered after the script starts running.

Example:

```python
# ask the user to type a value during execution
name = input("Enter your name: ")
print(name)
```

### Practical distinction

```text
command-line argument → provided before execution
input()               → provided during execution
```

A good general rule is:

- use command-line arguments when the script is designed to be run from the terminal with parameters
- use `input()` when the script should prompt and interact with the user step by step

## 6.2 Passing Arguments to Python Scripts

Python stores command-line arguments in the list `sys.argv`, provided by the `sys` module.

Important indexing rule:

- `sys.argv[0]` is the script name
- `sys.argv[1]` is the first user argument
- `sys.argv[2]` is the second user argument
- and so on

### Example 1: print the whole argument list

```python
# import sys to access command-line arguments
import sys

# print the entire argv list
print(sys.argv)
```

If run as:

```bash
python3 demo.py hello 123
```

Typical output:

```text
['demo.py', 'hello', '123']
```

### Example 2: print the script name

```python
# import sys for argv access
import sys

# sys.argv[0] stores the script name
print(sys.argv[0])
```

If run as:

```bash
python3 demo.py abc
```

Typical output:

```text
demo.py
```

### Example 3: print the first user argument

```python
# import sys so the script can read arguments
import sys

# print the first user-supplied argument
print(sys.argv[1])
```

If run as:

```bash
python3 demo.py Sydney
```

Output:

```text
Sydney
```

### Example 4: print multiple arguments

```python
# import sys to access argv
import sys

# print the first two user arguments
print("First argument :", sys.argv[1])
print("Second argument:", sys.argv[2])
```

If run as:

```bash
python3 demo.py red blue
```

Output:

```text
First argument : red
Second argument: blue
```

### Example 5: safe argument count checking

```python
# import sys for argv access
import sys

# check that at least one user argument was supplied
if len(sys.argv) < 2:
    print("Usage: python3 script.py <name>")
    exit()

# read the first argument safely
name = sys.argv[1]

# print a greeting
print(f"Hello {name}")
```

This pattern is important because directly accessing `sys.argv[1]` without validating length may cause an index error.

### Example 6: adding two integers from the command line

```python
# import sys to access command-line arguments
import sys

# validate that two numeric arguments are supplied
if len(sys.argv) < 3:
    print("Usage: python3 add.py <num1> <num2>")
    exit()

# convert argument strings into integers
a = int(sys.argv[1])
b = int(sys.argv[2])

# compute and print the sum
print(f"The sum of {a} and {b} is {a + b}")
```

Run as:

```bash
python3 add.py 12 30
```

### Example 7: classifying a numeric argument

```python
# import sys for argument handling
import sys

# check that one numeric argument exists
if len(sys.argv) < 2:
    print("Usage: python3 classify.py <number>")
    exit()

# convert the first argument from string to integer
number = int(sys.argv[1])

# classify using conditional logic
if number > 0:
    print("Positive")
elif number == 0:
    print("Zero")
else:
    print("Negative")
```

### Example 8: mood checker with sys.argv

```python
# import sys to read the command-line value
import sys

# verify that one mood argument was supplied
if len(sys.argv) < 2:
    print("Usage: python3 mood.py <good|bad>")
    exit()

# read the mood argument
mood = sys.argv[1]

# produce output based on the provided argument
if mood == "good":
    print("I am happy")
else:
    print("Please leave me alone!")
```

### Example 9: running executable scripts directly with arguments

If the script has a shebang line and executable permission, it can also be run as:

```bash
./script.py hello 25
```

The arguments are still received through `sys.argv` in exactly the same way.

## 6.3 Reading User Input

Interactive input allows the script to pause and wait for the user to type a value.

Python uses the `input()` function for this purpose.

### Important rule about `input()`

`input()` always returns a string.

That means:

- text input can be used directly as a string
- numeric input must usually be converted using `int()` or `float()`

### Example 1: reading a name

```python
# ask the user to enter a name
name = input("Enter your name: ")

# print the entered value
print(f"Hello {name}")
```

### Example 2: showing that input is returned as text

```python
# read a value from the keyboard
value = input("Enter something: ")

# print the value and its type
print(value)
print(type(value))
```

Even if the user types `25`, the returned value is still a string.

### Example 3: reading and converting an integer

```python
# prompt the user for a number
value = input("Enter a number: ")

# convert the returned string to an integer
number = int(value)

# perform a calculation with the integer
print(f"Double of {number} is {number * 2}")
```

### Example 4: reading and converting in one line

```python
# read input and convert to integer immediately
age = int(input("Enter your age: "))

# print the converted value
print(f"You entered age {age}")
```

### Example 5: combining input() with conditional logic

```python
# read age from the user and convert to integer
age = int(input("Enter your age: "))

# classify the input using if-else
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
```

### Example 6: reading two inputs and computing a result

```python
# read two numbers from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# calculate and print the sum
print(f"The sum is {a + b}")
```

### Example 7: reading text and validating allowed values

```python
# read a command string from the user
command = input("Enter command (start/stop): ")

# validate the typed command
if command == "start":
    print("System starting")
elif command == "stop":
    print("System stopping")
else:
    print("Unknown command")
```

### Example 8: combining string input with formatting

```python
# read first and last name separately
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

# combine values into a formatted output string
print(f"Full name: {first_name} {last_name}")
```

### Example 9: argument input vs interactive input

Compare these two approaches:

```python
# command-line argument version
import sys
print(sys.argv[1])
```

```python
# interactive input version
value = input("Enter a value: ")
print(value)
```

The first expects the value when the script is launched.  
The second waits and asks for the value during execution.

---

**End of Week 7**
