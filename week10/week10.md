# Week 10 — Functions in Python

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
   6.1 [args](#61-args)  
   6.2 [kwargs](#62-kwargs)  

7. [Functions in Practice](#7-functions-in-practice)  
   7.1 [Modular Program Design](#71-modular-program-design)  
   7.2 [Reusing Functions](#72-reusing-functions)  
   7.3 [Using Standard Library Functions](#73-using-standard-library-functions)  
   7.4 [Functions with Files](#74-functions-with-files)  

---

# 1. Functions in Python

## 1.1 Definition of Functions

A function is a reusable execution block that encapsulates logic and allows structured program design. 
Conceptually, functions isolate computation, enable abstraction, and support composition of complex workflows.

### Usage
- Used to structure large programs
- Enables reuse of logic
- Supports pipeline design (input → process → output)
- Helps debugging and testing

### Example 1
```python
#!/usr/bin/env python3
import sys

def read_lines():
    return sys.stdin.readlines()  # read all stdin lines

def count_errors(lines):
    count = 0
    for line in lines:
        if "ERROR" in line:  # detect error
            count += 1
    return count

data = read_lines()
print("Total Errors:", count_errors(data))
```

### Example 2
```python
#!/usr/bin/env python3
import os

def collect_files(path):
    files = []
    for root, _, fs in os.walk(path):  # traverse directories
        for f in fs:
            files.append(os.path.join(root, f))
    return files

def total_size(files):
    size = 0
    for f in files:
        try:
            size += os.path.getsize(f)  # accumulate size
        except:
            pass
    return size

files = collect_files(".")
print("Total size:", total_size(files))
```

## 1.2 Creating and Calling Functions

A function is a reusable execution block that encapsulates logic and allows structured program design. 
Conceptually, functions isolate computation, enable abstraction, and support composition of complex workflows.

### Usage
- Used to structure large programs
- Enables reuse of logic
- Supports pipeline design (input → process → output)
- Helps debugging and testing

### Example 1
```python
#!/usr/bin/env python3
import sys

def read_lines():
    return sys.stdin.readlines()  # read all stdin lines

def count_errors(lines):
    count = 0
    for line in lines:
        if "ERROR" in line:  # detect error
            count += 1
    return count

data = read_lines()
print("Total Errors:", count_errors(data))
```

### Example 2
```python
#!/usr/bin/env python3
import os

def collect_files(path):
    files = []
    for root, _, fs in os.walk(path):  # traverse directories
        for f in fs:
            files.append(os.path.join(root, f))
    return files

def total_size(files):
    size = 0
    for f in files:
        try:
            size += os.path.getsize(f)  # accumulate size
        except:
            pass
    return size

files = collect_files(".")
print("Total size:", total_size(files))
```

## 1.3 Parameters vs Arguments

A function is a reusable execution block that encapsulates logic and allows structured program design. 
Conceptually, functions isolate computation, enable abstraction, and support composition of complex workflows.

### Usage
- Used to structure large programs
- Enables reuse of logic
- Supports pipeline design (input → process → output)
- Helps debugging and testing

### Example 1
```python
#!/usr/bin/env python3
import sys

def read_lines():
    return sys.stdin.readlines()  # read all stdin lines

def count_errors(lines):
    count = 0
    for line in lines:
        if "ERROR" in line:  # detect error
            count += 1
    return count

data = read_lines()
print("Total Errors:", count_errors(data))
```

### Example 2
```python
#!/usr/bin/env python3
import os

def collect_files(path):
    files = []
    for root, _, fs in os.walk(path):  # traverse directories
        for f in fs:
            files.append(os.path.join(root, f))
    return files

def total_size(files):
    size = 0
    for f in files:
        try:
            size += os.path.getsize(f)  # accumulate size
        except:
            pass
    return size

files = collect_files(".")
print("Total size:", total_size(files))
```

# 2. Function Parameters and Arguments

## 2.1 Positional Arguments

A function is a reusable execution block that encapsulates logic and allows structured program design. 
Conceptually, functions isolate computation, enable abstraction, and support composition of complex workflows.

### Usage
- Used to structure large programs
- Enables reuse of logic
- Supports pipeline design (input → process → output)
- Helps debugging and testing

### Example 1
```python
#!/usr/bin/env python3
import sys

def read_lines():
    return sys.stdin.readlines()  # read all stdin lines

def count_errors(lines):
    count = 0
    for line in lines:
        if "ERROR" in line:  # detect error
            count += 1
    return count

data = read_lines()
print("Total Errors:", count_errors(data))
```

### Example 2
```python
#!/usr/bin/env python3
import os

def collect_files(path):
    files = []
    for root, _, fs in os.walk(path):  # traverse directories
        for f in fs:
            files.append(os.path.join(root, f))
    return files

def total_size(files):
    size = 0
    for f in files:
        try:
            size += os.path.getsize(f)  # accumulate size
        except:
            pass
    return size

files = collect_files(".")
print("Total size:", total_size(files))
```

## 2.2 Keyword Arguments

A function is a reusable execution block that encapsulates logic and allows structured program design. 
Conceptually, functions isolate computation, enable abstraction, and support composition of complex workflows.

### Usage
- Used to structure large programs
- Enables reuse of logic
- Supports pipeline design (input → process → output)
- Helps debugging and testing

### Example 1
```python
#!/usr/bin/env python3
import sys

def read_lines():
    return sys.stdin.readlines()  # read all stdin lines

def count_errors(lines):
    count = 0
    for line in lines:
        if "ERROR" in line:  # detect error
            count += 1
    return count

data = read_lines()
print("Total Errors:", count_errors(data))
```

### Example 2
```python
#!/usr/bin/env python3
import os

def collect_files(path):
    files = []
    for root, _, fs in os.walk(path):  # traverse directories
        for f in fs:
            files.append(os.path.join(root, f))
    return files

def total_size(files):
    size = 0
    for f in files:
        try:
            size += os.path.getsize(f)  # accumulate size
        except:
            pass
    return size

files = collect_files(".")
print("Total size:", total_size(files))
```

## 2.3 Default Parameter Values

A function is a reusable execution block that encapsulates logic and allows structured program design. 
Conceptually, functions isolate computation, enable abstraction, and support composition of complex workflows.

### Usage
- Used to structure large programs
- Enables reuse of logic
- Supports pipeline design (input → process → output)
- Helps debugging and testing

### Example 1
```python
#!/usr/bin/env python3
import sys

def read_lines():
    return sys.stdin.readlines()  # read all stdin lines

def count_errors(lines):
    count = 0
    for line in lines:
        if "ERROR" in line:  # detect error
            count += 1
    return count

data = read_lines()
print("Total Errors:", count_errors(data))
```

### Example 2
```python
#!/usr/bin/env python3
import os

def collect_files(path):
    files = []
    for root, _, fs in os.walk(path):  # traverse directories
        for f in fs:
            files.append(os.path.join(root, f))
    return files

def total_size(files):
    size = 0
    for f in files:
        try:
            size += os.path.getsize(f)  # accumulate size
        except:
            pass
    return size

files = collect_files(".")
print("Total size:", total_size(files))
```

# 3. Return Values

## 3.1 Single Return Value

A function is a reusable execution block that encapsulates logic and allows structured program design. 
Conceptually, functions isolate computation, enable abstraction, and support composition of complex workflows.

### Usage
- Used to structure large programs
- Enables reuse of logic
- Supports pipeline design (input → process → output)
- Helps debugging and testing

### Example 1
```python
#!/usr/bin/env python3
import sys

def read_lines():
    return sys.stdin.readlines()  # read all stdin lines

def count_errors(lines):
    count = 0
    for line in lines:
        if "ERROR" in line:  # detect error
            count += 1
    return count

data = read_lines()
print("Total Errors:", count_errors(data))
```

### Example 2
```python
#!/usr/bin/env python3
import os

def collect_files(path):
    files = []
    for root, _, fs in os.walk(path):  # traverse directories
        for f in fs:
            files.append(os.path.join(root, f))
    return files

def total_size(files):
    size = 0
    for f in files:
        try:
            size += os.path.getsize(f)  # accumulate size
        except:
            pass
    return size

files = collect_files(".")
print("Total size:", total_size(files))
```

## 3.2 Multiple Return Values

A function is a reusable execution block that encapsulates logic and allows structured program design. 
Conceptually, functions isolate computation, enable abstraction, and support composition of complex workflows.

### Usage
- Used to structure large programs
- Enables reuse of logic
- Supports pipeline design (input → process → output)
- Helps debugging and testing

### Example 1
```python
#!/usr/bin/env python3
import sys

def read_lines():
    return sys.stdin.readlines()  # read all stdin lines

def count_errors(lines):
    count = 0
    for line in lines:
        if "ERROR" in line:  # detect error
            count += 1
    return count

data = read_lines()
print("Total Errors:", count_errors(data))
```

### Example 2
```python
#!/usr/bin/env python3
import os

def collect_files(path):
    files = []
    for root, _, fs in os.walk(path):  # traverse directories
        for f in fs:
            files.append(os.path.join(root, f))
    return files

def total_size(files):
    size = 0
    for f in files:
        try:
            size += os.path.getsize(f)  # accumulate size
        except:
            pass
    return size

files = collect_files(".")
print("Total size:", total_size(files))
```

# 4. Memory and Argument Passing

## 4.1 Variable Memory Model

A function is a reusable execution block that encapsulates logic and allows structured program design. 
Conceptually, functions isolate computation, enable abstraction, and support composition of complex workflows.

### Usage
- Used to structure large programs
- Enables reuse of logic
- Supports pipeline design (input → process → output)
- Helps debugging and testing

### Example 1
```python
#!/usr/bin/env python3
import sys

def read_lines():
    return sys.stdin.readlines()  # read all stdin lines

def count_errors(lines):
    count = 0
    for line in lines:
        if "ERROR" in line:  # detect error
            count += 1
    return count

data = read_lines()
print("Total Errors:", count_errors(data))
```

### Example 2
```python
#!/usr/bin/env python3
import os

def collect_files(path):
    files = []
    for root, _, fs in os.walk(path):  # traverse directories
        for f in fs:
            files.append(os.path.join(root, f))
    return files

def total_size(files):
    size = 0
    for f in files:
        try:
            size += os.path.getsize(f)  # accumulate size
        except:
            pass
    return size

files = collect_files(".")
print("Total size:", total_size(files))
```

## 4.2 Immutable vs Mutable Objects

A function is a reusable execution block that encapsulates logic and allows structured program design. 
Conceptually, functions isolate computation, enable abstraction, and support composition of complex workflows.

### Usage
- Used to structure large programs
- Enables reuse of logic
- Supports pipeline design (input → process → output)
- Helps debugging and testing

### Example 1
```python
#!/usr/bin/env python3
import sys

def read_lines():
    return sys.stdin.readlines()  # read all stdin lines

def count_errors(lines):
    count = 0
    for line in lines:
        if "ERROR" in line:  # detect error
            count += 1
    return count

data = read_lines()
print("Total Errors:", count_errors(data))
```

### Example 2
```python
#!/usr/bin/env python3
import os

def collect_files(path):
    files = []
    for root, _, fs in os.walk(path):  # traverse directories
        for f in fs:
            files.append(os.path.join(root, f))
    return files

def total_size(files):
    size = 0
    for f in files:
        try:
            size += os.path.getsize(f)  # accumulate size
        except:
            pass
    return size

files = collect_files(".")
print("Total size:", total_size(files))
```

## 4.3 Passing Immutable Objects

A function is a reusable execution block that encapsulates logic and allows structured program design. 
Conceptually, functions isolate computation, enable abstraction, and support composition of complex workflows.

### Usage
- Used to structure large programs
- Enables reuse of logic
- Supports pipeline design (input → process → output)
- Helps debugging and testing

### Example 1
```python
#!/usr/bin/env python3
import sys

def read_lines():
    return sys.stdin.readlines()  # read all stdin lines

def count_errors(lines):
    count = 0
    for line in lines:
        if "ERROR" in line:  # detect error
            count += 1
    return count

data = read_lines()
print("Total Errors:", count_errors(data))
```

### Example 2
```python
#!/usr/bin/env python3
import os

def collect_files(path):
    files = []
    for root, _, fs in os.walk(path):  # traverse directories
        for f in fs:
            files.append(os.path.join(root, f))
    return files

def total_size(files):
    size = 0
    for f in files:
        try:
            size += os.path.getsize(f)  # accumulate size
        except:
            pass
    return size

files = collect_files(".")
print("Total size:", total_size(files))
```

## 4.4 Passing Mutable Objects

A function is a reusable execution block that encapsulates logic and allows structured program design. 
Conceptually, functions isolate computation, enable abstraction, and support composition of complex workflows.

### Usage
- Used to structure large programs
- Enables reuse of logic
- Supports pipeline design (input → process → output)
- Helps debugging and testing

### Example 1
```python
#!/usr/bin/env python3
import sys

def read_lines():
    return sys.stdin.readlines()  # read all stdin lines

def count_errors(lines):
    count = 0
    for line in lines:
        if "ERROR" in line:  # detect error
            count += 1
    return count

data = read_lines()
print("Total Errors:", count_errors(data))
```

### Example 2
```python
#!/usr/bin/env python3
import os

def collect_files(path):
    files = []
    for root, _, fs in os.walk(path):  # traverse directories
        for f in fs:
            files.append(os.path.join(root, f))
    return files

def total_size(files):
    size = 0
    for f in files:
        try:
            size += os.path.getsize(f)  # accumulate size
        except:
            pass
    return size

files = collect_files(".")
print("Total size:", total_size(files))
```

# 5. Working with Data Structures in Functions

## 5.1 Lists as Arguments

A function is a reusable execution block that encapsulates logic and allows structured program design. 
Conceptually, functions isolate computation, enable abstraction, and support composition of complex workflows.

### Usage
- Used to structure large programs
- Enables reuse of logic
- Supports pipeline design (input → process → output)
- Helps debugging and testing

### Example 1
```python
#!/usr/bin/env python3
import sys

def read_lines():
    return sys.stdin.readlines()  # read all stdin lines

def count_errors(lines):
    count = 0
    for line in lines:
        if "ERROR" in line:  # detect error
            count += 1
    return count

data = read_lines()
print("Total Errors:", count_errors(data))
```

### Example 2
```python
#!/usr/bin/env python3
import os

def collect_files(path):
    files = []
    for root, _, fs in os.walk(path):  # traverse directories
        for f in fs:
            files.append(os.path.join(root, f))
    return files

def total_size(files):
    size = 0
    for f in files:
        try:
            size += os.path.getsize(f)  # accumulate size
        except:
            pass
    return size

files = collect_files(".")
print("Total size:", total_size(files))
```

## 5.2 Dictionaries as Arguments

A function is a reusable execution block that encapsulates logic and allows structured program design. 
Conceptually, functions isolate computation, enable abstraction, and support composition of complex workflows.

### Usage
- Used to structure large programs
- Enables reuse of logic
- Supports pipeline design (input → process → output)
- Helps debugging and testing

### Example 1
```python
#!/usr/bin/env python3
import sys

def read_lines():
    return sys.stdin.readlines()  # read all stdin lines

def count_errors(lines):
    count = 0
    for line in lines:
        if "ERROR" in line:  # detect error
            count += 1
    return count

data = read_lines()
print("Total Errors:", count_errors(data))
```

### Example 2
```python
#!/usr/bin/env python3
import os

def collect_files(path):
    files = []
    for root, _, fs in os.walk(path):  # traverse directories
        for f in fs:
            files.append(os.path.join(root, f))
    return files

def total_size(files):
    size = 0
    for f in files:
        try:
            size += os.path.getsize(f)  # accumulate size
        except:
            pass
    return size

files = collect_files(".")
print("Total size:", total_size(files))
```

## 5.3 Updating Data Structures in Functions

A function is a reusable execution block that encapsulates logic and allows structured program design. 
Conceptually, functions isolate computation, enable abstraction, and support composition of complex workflows.

### Usage
- Used to structure large programs
- Enables reuse of logic
- Supports pipeline design (input → process → output)
- Helps debugging and testing

### Example 1
```python
#!/usr/bin/env python3
import sys

def read_lines():
    return sys.stdin.readlines()  # read all stdin lines

def count_errors(lines):
    count = 0
    for line in lines:
        if "ERROR" in line:  # detect error
            count += 1
    return count

data = read_lines()
print("Total Errors:", count_errors(data))
```

### Example 2
```python
#!/usr/bin/env python3
import os

def collect_files(path):
    files = []
    for root, _, fs in os.walk(path):  # traverse directories
        for f in fs:
            files.append(os.path.join(root, f))
    return files

def total_size(files):
    size = 0
    for f in files:
        try:
            size += os.path.getsize(f)  # accumulate size
        except:
            pass
    return size

files = collect_files(".")
print("Total size:", total_size(files))
```

# 6. Variable-Length Arguments

## 6.1 *args

A function is a reusable execution block that encapsulates logic and allows structured program design. 
Conceptually, functions isolate computation, enable abstraction, and support composition of complex workflows.

### Usage
- Used to structure large programs
- Enables reuse of logic
- Supports pipeline design (input → process → output)
- Helps debugging and testing

### Example 1
```python
#!/usr/bin/env python3
import sys

def read_lines():
    return sys.stdin.readlines()  # read all stdin lines

def count_errors(lines):
    count = 0
    for line in lines:
        if "ERROR" in line:  # detect error
            count += 1
    return count

data = read_lines()
print("Total Errors:", count_errors(data))
```

### Example 2
```python
#!/usr/bin/env python3
import os

def collect_files(path):
    files = []
    for root, _, fs in os.walk(path):  # traverse directories
        for f in fs:
            files.append(os.path.join(root, f))
    return files

def total_size(files):
    size = 0
    for f in files:
        try:
            size += os.path.getsize(f)  # accumulate size
        except:
            pass
    return size

files = collect_files(".")
print("Total size:", total_size(files))
```

## 6.2 **kwargs

A function is a reusable execution block that encapsulates logic and allows structured program design. 
Conceptually, functions isolate computation, enable abstraction, and support composition of complex workflows.

### Usage
- Used to structure large programs
- Enables reuse of logic
- Supports pipeline design (input → process → output)
- Helps debugging and testing

### Example 1
```python
#!/usr/bin/env python3
import sys

def read_lines():
    return sys.stdin.readlines()  # read all stdin lines

def count_errors(lines):
    count = 0
    for line in lines:
        if "ERROR" in line:  # detect error
            count += 1
    return count

data = read_lines()
print("Total Errors:", count_errors(data))
```

### Example 2
```python
#!/usr/bin/env python3
import os

def collect_files(path):
    files = []
    for root, _, fs in os.walk(path):  # traverse directories
        for f in fs:
            files.append(os.path.join(root, f))
    return files

def total_size(files):
    size = 0
    for f in files:
        try:
            size += os.path.getsize(f)  # accumulate size
        except:
            pass
    return size

files = collect_files(".")
print("Total size:", total_size(files))
```

# 7. Functions in Practice

## 7.1 Modular Program Design

A function is a reusable execution block that encapsulates logic and allows structured program design. 
Conceptually, functions isolate computation, enable abstraction, and support composition of complex workflows.

### Usage
- Used to structure large programs
- Enables reuse of logic
- Supports pipeline design (input → process → output)
- Helps debugging and testing

### Example 1
```python
#!/usr/bin/env python3
import sys

def read_lines():
    return sys.stdin.readlines()  # read all stdin lines

def count_errors(lines):
    count = 0
    for line in lines:
        if "ERROR" in line:  # detect error
            count += 1
    return count

data = read_lines()
print("Total Errors:", count_errors(data))
```

### Example 2
```python
#!/usr/bin/env python3
import os

def collect_files(path):
    files = []
    for root, _, fs in os.walk(path):  # traverse directories
        for f in fs:
            files.append(os.path.join(root, f))
    return files

def total_size(files):
    size = 0
    for f in files:
        try:
            size += os.path.getsize(f)  # accumulate size
        except:
            pass
    return size

files = collect_files(".")
print("Total size:", total_size(files))
```

## 7.2 Reusing Functions

A function is a reusable execution block that encapsulates logic and allows structured program design. 
Conceptually, functions isolate computation, enable abstraction, and support composition of complex workflows.

### Usage
- Used to structure large programs
- Enables reuse of logic
- Supports pipeline design (input → process → output)
- Helps debugging and testing

### Example 1
```python
#!/usr/bin/env python3
import sys

def read_lines():
    return sys.stdin.readlines()  # read all stdin lines

def count_errors(lines):
    count = 0
    for line in lines:
        if "ERROR" in line:  # detect error
            count += 1
    return count

data = read_lines()
print("Total Errors:", count_errors(data))
```

### Example 2
```python
#!/usr/bin/env python3
import os

def collect_files(path):
    files = []
    for root, _, fs in os.walk(path):  # traverse directories
        for f in fs:
            files.append(os.path.join(root, f))
    return files

def total_size(files):
    size = 0
    for f in files:
        try:
            size += os.path.getsize(f)  # accumulate size
        except:
            pass
    return size

files = collect_files(".")
print("Total size:", total_size(files))
```

## 7.3 Using Standard Library Functions

A function is a reusable execution block that encapsulates logic and allows structured program design. 
Conceptually, functions isolate computation, enable abstraction, and support composition of complex workflows.

### Usage
- Used to structure large programs
- Enables reuse of logic
- Supports pipeline design (input → process → output)
- Helps debugging and testing

### Example 1
```python
#!/usr/bin/env python3
import sys

def read_lines():
    return sys.stdin.readlines()  # read all stdin lines

def count_errors(lines):
    count = 0
    for line in lines:
        if "ERROR" in line:  # detect error
            count += 1
    return count

data = read_lines()
print("Total Errors:", count_errors(data))
```

### Example 2
```python
#!/usr/bin/env python3
import os

def collect_files(path):
    files = []
    for root, _, fs in os.walk(path):  # traverse directories
        for f in fs:
            files.append(os.path.join(root, f))
    return files

def total_size(files):
    size = 0
    for f in files:
        try:
            size += os.path.getsize(f)  # accumulate size
        except:
            pass
    return size

files = collect_files(".")
print("Total size:", total_size(files))
```

## 7.4 Functions with Files

A function is a reusable execution block that encapsulates logic and allows structured program design. 
Conceptually, functions isolate computation, enable abstraction, and support composition of complex workflows.

### Usage
- Used to structure large programs
- Enables reuse of logic
- Supports pipeline design (input → process → output)
- Helps debugging and testing

### Example 1
```python
#!/usr/bin/env python3
import sys

def read_lines():
    return sys.stdin.readlines()  # read all stdin lines

def count_errors(lines):
    count = 0
    for line in lines:
        if "ERROR" in line:  # detect error
            count += 1
    return count

data = read_lines()
print("Total Errors:", count_errors(data))
```

### Example 2
```python
#!/usr/bin/env python3
import os

def collect_files(path):
    files = []
    for root, _, fs in os.walk(path):  # traverse directories
        for f in fs:
            files.append(os.path.join(root, f))
    return files

def total_size(files):
    size = 0
    for f in files:
        try:
            size += os.path.getsize(f)  # accumulate size
        except:
            pass
    return size

files = collect_files(".")
print("Total size:", total_size(files))
```
---

**End of Week 10**
