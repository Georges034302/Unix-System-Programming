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

3. [Return Values](#3-return-values)  
   3.1 [Single Return Value](#31-single-return-value)  
   3.2 [Multiple Return Values](#32-multiple-return-values)  

4. [Memory and Argument Passing](#4-memory-and-argument-passing)  
   4.1 [Variable Memory Model](#41-variable-memory-model)  
   4.2 [Immutable vs Mutable Objects](#42-immutable-vs-mutable-objects)  
   4.3 [Passing Immutable Objects](#43-passing-immutable-objects)  
   4.4 [Passing Mutable Objects](#44-passing-mutable-objects)  

5. [Working with Data Structures in Functions](#5-working-with-data-structures-in-functions)  
   5.1 [Lists as Arguments](#51-lists-as-arguments)  
   5.2 [Dictionaries as Arguments](#52-dictionaries-as-arguments)  
   5.3 [Updating Data Structures in Functions](#53-updating-data-structures-in-functions)  

6. [Variable-Length Arguments](#6-variable-length-arguments)  
   6.1 [*args (Variable Positional Arguments)](#61-args-variable-positional-arguments)  
   6.2 [**kwargs (Variable Keyword Arguments)](#62-kwargs-variable-keyword-arguments)  

7. [Functions in Practice](#7-functions-in-practice)  
   7.1 [Modular Program Design](#71-modular-program-design)  
   7.2 [Reusing Functions](#72-reusing-functions)  
   7.3 [Using Standard Library Functions](#73-using-standard-library-functions)  
   7.4 [Functions with Files](#74-functions-with-files)  

---

# 1. Functions in Python

## 1.1 Definition of Functions
**Definition:** A function is a reusable block of code that performs a specific task.

**Purpose:**  
- Avoid repetition  
- Improve modularity  
- Improve readability  

**Syntax:**
```python
def name(parameters):
    return value
```

**Example 1:**
```python
def greet(name):
    print("Hello", name)

greet("Sydney")
```

**Example 2:**
```python
def add(a, b):
    return a + b

print(add(5, 3))
```

## 1.2 Creating and Calling Functions
**Definition:** Functions are created using `def` and executed via calls.

**Purpose:** Encapsulate logic and reuse.

**Syntax:**
```python
def f():
    pass
f()
```

**Example 1:**
```python
def hello():
    print("Hi")

hello()
```

**Example 2:**
```python
def square(x):
    return x*x

print(square(4))
```

## 1.3 Parameters vs Arguments
**Definition:** Parameters are placeholders; arguments are values passed.

**Purpose:** Allow flexibility.

**Syntax:**
```python
def f(p): pass
f(value)
```

**Example 1:**
```python
def show(x):
    print(x)

show(10)
```

**Example 2:**
```python
def mul(a,b):
    return a*b

print(mul(2,3))
```

# 2. Function Parameters and Arguments

## 2.1 Positional Arguments
**Definition:** Arguments passed by order.

**Purpose:** Simple and fast.

**Syntax:**
```python
f(a,b)
```

**Example 1:**
```python
def sub(a,b):
    return a-b

print(sub(5,2))
```

**Example 2:**
```python
print(sub(2,5))
```

## 2.2 Keyword Arguments
**Definition:** Arguments passed by name.

**Purpose:** Flexibility.

**Syntax:**
```python
f(a=1,b=2)
```

**Example 1:**
```python
def volume(h,w,d):
    return h*w*d

print(volume(h=2,w=3,d=4))
```

**Example 2:**
```python
print(volume(d=4,h=2,w=3))
```

## 2.3 Default Parameter Values
**Definition:** Parameters have default values.

**Purpose:** Optional arguments.

**Syntax:**
```python
def f(a=10):
    pass
```

**Example 1:**
```python
def inc(x=1):
    return x+1

print(inc())
```

**Example 2:**
```python
print(inc(5))
```

# 3. Return Values

## 3.1 Single Return Value
**Definition:** Return one value.

**Purpose:** Send result back.

**Example 1:**
```python
def sq(x):
    return x*x

print(sq(3))
```

**Example 2:**
```python
y = sq(4)
print(y)
```

## 3.2 Multiple Return Values
**Definition:** Return multiple values.

**Purpose:** Return structured results.

**Example 1:**
```python
def stats(l):
    return min(l), max(l)

print(stats([1,5,3]))
```

**Example 2:**
```python
a,b = stats([10,20])
print(a,b)
```

# 4. Memory and Argument Passing

## 4.1 Variable Memory Model
**Definition:** Variables store references.

**Purpose:** Efficient memory use.

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
**Definition:** Immutable cannot change, mutable can.

**Example 1:**
```python
x = 10
x = 20
```

**Example 2:**
```python
l=[1,2]
l[0]=5
```

## 4.3 Passing Immutable Objects
**Example 1:**
```python
def f(x):
    x=100

a=10
f(a)
print(a)
```

**Example 2:**
```python
def g(n):
    n+=1
```

## 4.4 Passing Mutable Objects
**Example 1:**
```python
def mod(l):
    l[0]=99

a=[1,2]
mod(a)
print(a)
```

**Example 2:**
```python
def add(l):
    l.append(5)
```

# 5. Working with Data Structures in Functions

## 5.1 Lists as Arguments
**Example 1:**
```python
def avg(l):
    return sum(l)/len(l)
```

**Example 2:**
```python
print(avg([1,2,3]))
```

## 5.2 Dictionaries as Arguments
**Example 1:**
```python
def show(d):
    for k in d:
        print(k,d[k])
```

**Example 2:**
```python
show({"a":1})
```

## 5.3 Updating Data Structures in Functions
**Example 1:**
```python
def update(d,k,v):
    d[k]=v
```

**Example 2:**
```python
d={}
update(d,"x",10)
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

# 7. Functions in Practice

## 7.1 Modular Program Design
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

## 7.2 Reusing Functions
**Example 1:**
```python
def add(a,b):
    return a+b
```

**Example 2:**
```python
print(add(1,2))
```

## 7.3 Using Standard Library Functions
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
**Definition:** Encapsulate file operations.

**Purpose:** Reusable file processing.

**Example 1:**
```python
def read_file(path):
    with open(path) as f:
        return f.read()
```

**Example 2:**
```python
def count_lines(path):
    with open(path) as f:
        return len(f.readlines())
```
