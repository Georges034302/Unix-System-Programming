# Week 10 — Functions in Python for Unix Systems Programming

## Table of Contents
1. [Functions in Python](#1-functions-in-python)  
   1.1 [Definition of Functions](#11-definition-of-functions)  
   1.2 [Creating and Calling Functions](#12-creating-and-calling-functions)  
   1.3 [Parameters vs Arguments](#13-parameters-vs-arguments)  

2. [Function Parameters and Arguments](#2-function-parameters-and-arguments)  
   2.1 [Positional Arguments](#21-positional-arguments)  
   2.2 [Keyword Arguments](#22-keyword-arguments)  
   2.3 [Default Parameter Values](#23-default-parameter-values)  
   2.4 [Usage Scenarios](#24-usage-scenarios)  
   2.5 [Example 1 — Basic Parameter Usage](#25-example-1--basic-parameter-usage)  
   2.6 [Example 2 — Flexible Function Calls](#26-example-2---flexible-function-calls)  

3. [Return Values](#3-return-values)  
   3.1 [Single Return Value](#31-single-return-value)  
   3.2 [Multiple Return Values](#32-multiple-return-values)  
   3.3 [Usage Scenarios](#33-usage-scenarios)  
   3.4 [Example 1 — Returning a Single Value](#34-example-1--returning-a-single-value)  
   3.5 [Example 2 — Returning Multiple Values](#35-example-2---returning-multiple-values)  

4. [Memory and Argument Passing](#4-memory-and-argument-passing)  
   4.1 [Variable Memory Model](#41-variable-memory-model)  
   4.2 [Immutable vs Mutable Objects](#42-immutable-vs-mutable-objects)  
   4.3 [Passing Immutable Objects](#43-passing-immutable-objects)  
   4.4 [Passing Mutable Objects](#44-passing-mutable-objects)  
   4.5 [Usage Scenarios](#45-usage-scenarios)  
   4.6 [Example 1 — Immutable Argument Behaviour](#46-example-1--immutable-argument-behaviour)  
   4.7 [Example 2 — Mutable Argument Behaviour](#47-example-2---mutable-argument-behaviour)  

5. [Working with Data Structures in Functions](#5-working-with-data-structures-in-functions)  
   5.1 [Lists as Arguments](#51-lists-as-arguments)  
   5.2 [Dictionaries as Arguments](#52-dictionaries-as-arguments)  
   5.3 [Updating Data Structures in Functions](#53-updating-data-structures-in-functions)  
   5.4 [Usage Scenarios](#54-usage-scenarios)  
   5.5 [Example 1 — List Processing Function](#55-example-1--list-processing-function)  
   5.6 [Example 2 — Dictionary Update Function](#56-example-2---dictionary-update-function)  

6. [Variable-Length Arguments](#6-variable-length-arguments)  
   6.1 [*args (Variable Positional Arguments)](#61-args-variable-positional-arguments)  
   6.2 [**kwargs (Variable Keyword Arguments)](#62-kwargs-variable-keyword-arguments)  
   6.3 [Practical Use Cases](#63-practical-use-cases)  
   6.4 [Example 1 — Using *args](#64-example-1--using-args)  
   6.5 [Example 2 — Using **kwargs](#65-example-2---using-kwargs)  

7. [Functions in Practice](#7-functions-in-practice)  
   7.1 [Modular Program Design](#71-modular-program-design)  
   7.2 [Reusing Functions](#72-reusing-functions)  
   7.3 [Using Standard Library Functions](#73-using-standard-library-functions)  
   7.4 [Functions with Files](#74-functions-with-files)  
   7.5 [Example 1 — File Reading Function](#75-example-1--file-reading-function)  
   7.6 [Example 2 — File Processing and Reporting](#76-example-2---file-processing-and-reporting)  


---

# 1. Functions in Python

## 1.1 Introduction to Functions
**Definition:** Functions encapsulate reusable logic to improve modularity and readability.

**Syntax:**
```python
def function_name(parameters):
    return value
```

**Example 1:**
```python
def hello(name):
    print("Hello", name)

hello("Sydney")
```

**Example 2:**
```python
def add(a, b):
    return a + b

print(add(5, 3))
```

## 1.2 Creating and Calling Functions
**Definition:** Functions are defined using `def` and executed via calls.

**Example 1:**
```python
def square(x):
    return x * x

print(square(4))
```

**Example 2:**
```python
def greet():
    print("Welcome")

greet()
```

## 1.3 Parameters vs Arguments
**Definition:** Parameters are variables in definition; arguments are values passed.

**Example 1:**
```python
def show(x):
    print(x)

show(10)
```

**Example 2:**
```python
def multiply(a, b):
    print(a * b)

multiply(2, 3)
```

# 2. Function Parameters and Arguments

## 2.1 Positional Arguments
**Example 1:**
```python
def sub(a, b):
    print(a - b)

sub(5, 2)
```

**Example 2:**
```python
sub(2, 5)
```

## 2.2 Keyword Arguments
**Example 1:**
```python
def volume(h, w, d):
    print(h * w * d)

volume(h=2, w=3, d=4)
```

**Example 2:**
```python
volume(d=4, h=2, w=3)
```

## 2.3 Default Parameter Values
**Example 1:**
```python
def volume(h=10, w=10, d=10):
    print(h * w * d)

volume()
```

**Example 2:**
```python
volume(20)
```

# 3. Return Values

## 3.1 Single Return Value
**Example 1:**
```python
def square(x):
    return x**2

print(square(3))
```

**Example 2:**
```python
y = square(5)
print(y)
```

## 3.2 Multiple Return Values
**Example 1:**
```python
def calc(a, b):
    return a+b, a-b

x, y = calc(5, 3)
print(x, y)
```

**Example 2:**
```python
def circle(r):
    return 2*3.14*r, 3.14*r*r

c, a = circle(2)
```

# 4. Memory and Argument Passing

## 4.1 Variable Memory Model
**Example 1:**
```python
x = 10
y = x
```

**Example 2:**
```python
x = 20
```

## 4.2 Immutable vs Mutable Objects
**Example 1:**
```python
x = 10
x = 20
```

**Example 2:**
```python
l = [1,2]
l[0] = 5
```

## 4.3 Passing Immutable Objects
**Example 1:**
```python
def f(x):
    x = 100

a = 10
f(a)
print(a)
```

**Example 2:**
```python
def g(n):
    n += 1
```

## 4.4 Passing Mutable Objects
**Example 1:**
```python
def modify(l):
    l[0] = 100

a = [1,2]
modify(a)
print(a)
```

**Example 2:**
```python
def add_item(l):
    l.append(5)
```

# 5. Working with Data Structures

## 5.1 Lists as Arguments
**Example 1:**
```python
def sum_list(l):
    return sum(l)
```

**Example 2:**
```python
print(sum_list([1,2,3]))
```

## 5.2 Dictionaries as Arguments
**Example 1:**
```python
def print_dict(d):
    for k in d:
        print(k, d[k])
```

**Example 2:**
```python
print_dict({"a":1})
```

## 5.3 Updating Data Structures
**Example 1:**
```python
def update(d,k,v):
    d[k] = v
```

**Example 2:**
```python
users = {}
update(users,"x",10)
```

# 6. Variable-Length Arguments

## 6.1 *args
**Example 1:**
```python
def f(*args):
    print(args)
```

**Example 2:**
```python
f(1,2,3)
```

## 6.2 **kwargs
**Example 1:**
```python
def f(**kwargs):
    print(kwargs)
```

**Example 2:**
```python
f(a=1,b=2)
```

## 6.3 Practical Use Cases
**Example 1:**
```python
def max_val(*args):
    return max(args)
```

**Example 2:**
```python
print(max_val(1,2,3))
```

# 7. Functions in Practice

## 7.1 Modular Design
**Example 1:**
```python
def process():
    pass
```

**Example 2:**
```python
def main():
    process()
```

## 7.2 Reuse Functions
**Example 1:**
```python
def add(a,b):
    return a+b
```

**Example 2:**
```python
print(add(1,2))
```

## 7.3 Standard Library
**Example 1:**
```python
import math
print(math.sqrt(4))
```

**Example 2:**
```python
print(len("abc"))
```

## 7.4 Functions with Files
**Definition:** Functions can encapsulate file operations for reuse.

**Example 1:**
```python
def read_file(path):
    with open(path) as f:
        return f.read()
```

**Example 2:**
```python
def write_file(path, text):
    with open(path, 'a') as f:
        f.write(text + "\n")
```

