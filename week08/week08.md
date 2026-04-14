# Week 8 — Regular Expressions in Python for Unix Systems Programming

## Table of Contents
1. [Regular Expressions in Python](#1-regular-expressions-in-python)  
   1.1 [Introduction to Regex](#11-introduction-to-regex)  
   1.2 [The `re` Module](#12-the-re-module)  
   1.3 [Reading from Standard Input (STDIN)](#13-reading-from-standard-input-stdin)  
   1.4 [Removing Trailing Newline](#14-removing-trailing-newline)  
   1.5 [Basic Regex Matching](#15-basic-regex-matching)  

2. [Pattern Matching Fundamentals](#2-pattern-matching-fundamentals)  
   2.1 [How Regex Matching Works](#21-how-regex-matching-works)  
   2.2 [Match Objects](#22-match-objects)  
   2.3 [Building a Regex Tester](#23-building-a-regex-tester)  

3. [Regex Metacharacters](#3-regex-metacharacters)  
   3.1 [Core Metacharacters](#31-core-metacharacters)  
   3.2 [Quantifiers](#32-quantifiers)  
   3.3 [Anchors](#33-anchors)  
   3.4 [Examples](#34-examples)  

4. [Advanced Regex Concepts](#4-advanced-regex-concepts)  
   4.1 [Greedy Behaviour](#41-greedy-behaviour)  
   4.2 [Grouping and Alternation](#42-grouping-and-alternation)  
   4.3 [Special Sequences](#43-special-sequences)  
   4.4 [Word Boundaries](#44-word-boundaries)  
   4.5 [Operator Precedence](#45-operator-precedence)  

5. [Python `re` Functions](#5-python-re-functions)  
   5.1 [`re.search`](#51-research)  
   5.2 [`re.findall`](#52-refindall)  
   5.3 [`re.split`](#53-resplit)  
   5.4 [`re.sub`](#54-resub)  
   5.5 [`re.match`](#55-rematch)  

6. [Working with Matches](#6-working-with-matches)  
   6.1 [Using `findall`](#61-using-findall)  
   6.2 [Using `split`](#62-using-split)  
   6.3 [Using `sub`](#63-using-sub)  
   6.4 [Matching Empty Strings](#64-matching-empty-strings)  

7. [Practical System Applications](#7-practical-system-applications)  
   7.1 [Processing Log Files](#71-processing-log-files)  
   7.2 [Extracting Patterns](#72-extracting-patterns)  
   7.3 [STDIN Redirection](#73-stdin-redirection)  

---

# 1. Regular Expressions in Python

## Definition

A regular expression, usually shortened to regex, is a pattern used to describe and match text.

In Unix systems programming, regex is important because many system tasks involve text rather than graphical data. You often work with:

- command output
- configuration files
- log files
- filenames
- user input
- process reports

A regex allows you to describe what kind of text you want to detect rather than checking every character manually.

Instead of writing many individual comparisons, you write one pattern and let the regex engine test the text for you.

Conceptually:

```text
input text
   ↓
regex pattern
   ↓
regex engine checks the text
   ↓
match found / no match
   ↓
print, extract, split, or replace
```

This makes regex especially useful for filtering lines, extracting structured text, validating formats, and automating repetitive text-processing tasks.

## 1.1 Introduction to Regex

A regex is not a complete program. It is a compact language for describing patterns in text.

For example:

- `cat` matches the literal text `cat`
- `\d` matches a digit
- `\w+` matches one or more word characters
- `^error` matches text that begins with `error`

A useful mental model is:

```text
plain text search      → looks for an exact fixed string
regular expression     → looks for a pattern
```

So if you search for:

```text
error
```

you are asking:

```text
"Does this exact text appear?"
```

But if you search for:

```text
error \d+
```

you are asking:

```text
"Is there the word error followed by one or more digits?"
```

That is the key power of regex: it describes structure, not just literal text.

### Example 1: simple literal search

```python
# import the regex module
import re

# define an input string
line = "disk error occurred during backup"

# search for the literal word 'error' anywhere in the line
if re.search("error", line):
    print("Match found")
```

In this example, the regex is simply `error`, which contains no special regex operators.  
The engine scans the line from left to right until it finds that exact sequence of characters.

### Example 2: match a number pattern

```python
# import regex support
import re

# define a string containing a code
message = "Process finished with exit code 127"

# \d+ means one or more digits
if re.search(r"\d+", message):
    print("A numeric value exists in the message")
```

Here the pattern is no longer a fixed literal string.  
`\d+` means:

- `\d` → any digit from 0 to 9
- `+` → one or more of the previous item

So this matches `127`.

## 1.2 The `re` Module

Python provides regex support through the standard library module `re`.

You usually start with:

```python
import re
```

The `re` module contains the main regex tools you will use in Unix scripting, such as:

- `re.search()` → find the first match anywhere in the string
- `re.findall()` → return all matching parts
- `re.split()` → split a string using a regex pattern
- `re.sub()` → replace matching text
- `re.match()` → match only at the beginning of a string

A simple architecture is:

```text
Python script
   ↓
re module
   ↓
regex function
   ↓
string input
   ↓
match result / transformed output
```

A very important practical point is the use of raw strings.

Python strings use backslash `\` for escape sequences such as `\n` or `\t`.  
Regex also uses backslash for special patterns such as `\d`, `\w`, and `\b`.

To avoid confusion, regex patterns are often written as raw strings:

```python
r"\d+"
```

instead of:

```python
"\\d+"
```

Both can work, but raw strings are clearer and safer.

### Example 1: importing and using `re`

```python
# import the regular expression module
import re

# define a sample string
text = "user42 logged in"

# search for one or more digits
match = re.search(r"\d+", text)

# if a match exists, print the matched substring
if match:
    print(match.group())
```

This prints `42` because `\d+` matches the consecutive digits in the string.

### Example 2: why raw strings help

```python
# import regex support
import re

# define a path-like string
text = "report_2026.txt"

# use a raw string so backslash sequences remain easy to read
# \d+ means one or more digits
match = re.search(r"\d+", text)

if match:
    print(match.group())
```

The raw string avoids double escaping and makes the regex easier to understand.

## 1.3 Reading from Standard Input (STDIN)

In Unix systems programming, scripts often do not read from a hardcoded filename.  
Instead, they read from standard input, usually called STDIN.

This lets the script participate naturally in Unix workflows such as:

- pipe-based processing
- input redirection
- command chaining

Conceptually:

```text
file / command output / keyboard input
                 ↓
               STDIN
                 ↓
            Python script
                 ↓
             regex logic
                 ↓
               output
```

This is important because Unix tools are designed to work together.  
A regex-based Python script becomes much more useful when it can accept input from another command or from a redirected file.

### Example 1: print every line from STDIN

```python
#!/usr/bin/env python3

# import sys so we can access sys.stdin
import sys

# iterate over every line arriving through standard input
for line in sys.stdin:
    # print the line exactly as received
    print(line)
```

This script reads one line at a time from STDIN.  
If the input comes from a file or another command, the script still works the same way.

### Example 2: prepare for line-based processing

```python
#!/usr/bin/env python3

# import sys for stdin access
import sys

# read each line from standard input
for line in sys.stdin:
    # remove surrounding whitespace only for display clarity
    cleaned = line.strip()

    # display the processed line
    print(f"Read line: {cleaned}")
```

This demonstrates the usual pattern in Unix-style Python scripts:

1. read one line
2. clean it
3. apply regex or other logic
4. output the result

## 1.4 Removing Trailing Newline

When a line is read from STDIN, it usually includes the newline character `\n` at the end.

That means if you print the line directly, the line already contains a newline, and `print()` adds another line ending for display purposes. This can cause awkward spacing or unexpected formatting.

A standard solution is:

```python
line = line.rstrip('\n')
```

This removes only the trailing newline from the right side of the string.

It is preferred over removing all whitespace in many system scripts because you often want to preserve spaces and tabs that may be meaningful.

Conceptually:

```text
line read from STDIN   → "error found\n"
rstrip('\n')           → "error found"
```

### Example 1: removing only the newline

```python
#!/usr/bin/env python3

# import sys for stdin access
import sys

# read each incoming line
for line in sys.stdin:
    # remove only the final newline character
    line = line.rstrip('\n')

    # print the cleaned line
    print(line)
```

This is the most common pattern before applying regex processing.

### Example 2: why `rstrip('\n')` is precise

```python
# create a line that ends with a newline
line = "system warning\n"

# remove only the newline at the end
cleaned = line.rstrip('\n')

# show both values explicitly
print(repr(line))
print(repr(cleaned))
```

Using `repr()` reveals the hidden newline clearly.

## 1.5 Basic Regex Matching

The most common first regex task is checking whether a line contains a particular pattern.

This is usually done with `re.search()`.

A basic Unix processing model is:

```text
read line
   ↓
remove newline
   ↓
apply regex
   ↓
if matched, print or process
```

### Example 1: print lines containing a word

```python
#!/usr/bin/env python3

# import sys for stdin and re for regex matching
import sys
import re

# read each input line
for line in sys.stdin:
    # remove trailing newline before further processing
    line = line.rstrip('\n')

    # search for the literal word 'error' anywhere in the line
    if re.search(r"error", line):
        # print only lines that contain the word
        print(line)
```

This is similar to a simplified `grep` written in Python.

### Example 2: match warning or error

```python
#!/usr/bin/env python3

# import required modules
import sys
import re

# process input line by line
for line in sys.stdin:
    # remove the line ending
    line = line.rstrip('\n')

    # (error|warning) means match either 'error' or 'warning'
    if re.search(r"error|warning", line):
        print(line)
```

This shows the move from exact text search to pattern-based search.  
The regex is now capable of matching more than one possible form.

---

# 2. Pattern Matching Fundamentals

## Definition

Pattern matching means testing whether text satisfies the structure described by a regular expression.

This is more than simply checking whether two strings are equal.  
Regex matching allows the pattern to move across the string, testing character positions until it either succeeds or fails.

In practice, the regex engine performs a controlled scan through the text.

## 2.1 How Regex Matching Works

When a regex is applied to a string, the engine tries to match the pattern starting from the earliest possible position. If a match fails, it shifts forward and tries again.

Conceptually:

```text
string position 0 → try match
fail
string position 1 → try match
fail
string position 2 → try match
success
```

Suppose the pattern is:

```text
mamma
```

and the string is:

```text
mamammamma
```

The engine effectively does this:

```text
mamammamma
mamma      no match at first position
 mamma     no match at next position
  mamma    match
```

It keeps sliding across the string until the pattern fits.

### Example 1: matching from left to right

```python
# import regex support
import re

# define a sample input
text = "xxerroryy"

# search for the literal word 'error'
match = re.search(r"error", text)

# if a match is found, display the exact substring
if match:
    print(match.group())
```

The engine does not require `error` to start at the beginning.  
It scans until it reaches the first `e` that begins a successful match.

### Example 2: partial match within larger text

```python
# import regex support
import re

# define text containing a process ID
text = "PID=3489 completed successfully"

# \d+ means one or more digits
match = re.search(r"\d+", text)

# print the first numeric sequence
if match:
    print(match.group())
```

The engine ignores earlier characters until it reaches the first place where one or more digits can be matched.

## 2.2 Match Objects

When `re.search()` succeeds, it does not return the matched text directly.  
It returns a match object.

A match object stores information about the successful match, including:

- the matched text
- the starting position
- the ending position
- captured groups, if any

The most common method is:

```python
match.group()
```

which returns the text that matched.

### Example 1: retrieving the matched substring

```python
# import regex support
import re

# define a line containing a username
line = "logged in as admin42"

# search for a word followed by digits
match = re.search(r"\w+\d+", line)

# if a match exists, print the matching text
if match:
    print(match.group())
```

This prints `admin42`.

### Example 2: using start and end positions

```python
# import regex support
import re

# define a text sample
text = "task 314 failed"

# search for the digits
match = re.search(r"\d+", text)

# print information about the match
if match:
    print("Matched text :", match.group())
    print("Start index  :", match.start())
    print("End index    :", match.end())
```

This is useful when you want not only the text itself, but also its location inside the string.

## 2.3 Building a Regex Tester

A regex tester is a simple script that lets the user type a pattern and then try it against several lines of input.

This is a very good teaching tool because it separates:

- the pattern
- the input text
- the observed match

Architecture:

```text
user enters regex
        ↓
program stores regex
        ↓
user supplies text lines
        ↓
re.search tests each line
        ↓
display matched part
```

### Example: interactive regex tester

```python
#!/usr/bin/env python3

# import required modules
import sys
import re

# ask the user to type a regex pattern
regex = input("Enter a regular expression: ")

# show the stored pattern so the user can verify it
print("Regex:", regex)
print("Enter some lines:")

# process all subsequent input lines from stdin
for line in sys.stdin:
    # remove the trailing newline for clean output
    line = line.rstrip('\n')

    # test the current line against the entered regex
    match = re.search(regex, line)

    # if a match exists, print both the line and the matched part
    if match:
        print("Line        :", line)
        print("Matched part:", match.group())
```

This script is useful because it reveals the difference between:

- the full input line
- the matched section only

That distinction is central to understanding regex.

---

# 3. Regex Metacharacters

## Definition

Metacharacters are characters that have a special meaning in regex syntax.

Unlike ordinary literal characters, metacharacters do not simply match themselves.  
They tell the regex engine how matching should behave.

For example:

- `.` means any character
- `*` means repeat zero or more times
- `^` means beginning of line

Without metacharacters, regex would behave like ordinary text search.  
Metacharacters are what make regex expressive.

## 3.1 Core Metacharacters

Some of the most important regex metacharacters are:

- `.` → matches any single character except newline
- `*` → matches zero or more of the previous item
- `+` → matches one or more of the previous item
- `?` → matches zero or one of the previous item
- `{m,n}` → matches between `m` and `n` repetitions
- `^` → anchors the match at the beginning of the line
- `$` → anchors the match at the end of the line

These can be grouped conceptually as:

```text
character matcher     → .
repeat operators      → *  +  ?  {m,n}
position anchors      → ^  $
```

### Example 1: dot matches any single character

```python
# import regex support
import re

# define a short text
text = "hat"

# h.t means:
# h followed by any single character followed by t
match = re.search(r"h.t", text)

if match:
    print(match.group())
```

This matches `hat`, but the same pattern would also match `hit` or `hot`.

### Example 2: plus requires at least one repetition

```python
# import regex support
import re

# define sample text
text = "helloooo"

# o+ means one or more 'o' characters
match = re.search(r"o+", text)

if match:
    print(match.group())
```

This returns the longest consecutive run of `o` characters that fits the pattern.

## 3.2 Quantifiers

Quantifiers specify how many times the previous character, group, or class may occur.

The main quantifiers are:

- `*` → zero or more
- `+` → one or more
- `?` → zero or one
- `{m,n}` → at least `m`, at most `n`

These are essential because real-world text is often variable in length.

Conceptually:

```text
a*       → "", "a", "aa", "aaa", ...
a+       → "a", "aa", "aaa", ...
a?       → "" or "a"
a{2,4}   → "aa", "aaa", or "aaaa"
```

### Example 1: zero or more

```python
# import regex support
import re

# define a text string
text = "hell"

# o* means zero or more 'o' characters
# since zero is allowed, the regex can still succeed
match = re.search(r"o*", text)

if match:
    print(repr(match.group()))
```

This example is important because `*` can match an empty string.

### Example 2: bounded repetition

```python
# import regex support
import re

# define a text sample
text = "ID: 2026"

# \d{4} means exactly four digits
match = re.search(r"\d{4}", text)

if match:
    print(match.group())
```

This is useful when a format expects a fixed number of digits, such as a year or code.

## 3.3 Anchors

Anchors do not match ordinary characters.  
They match positions.

The main anchors are:

- `^` → beginning of string or line
- `$` → end of string or line

This is useful when you need to control where the match occurs.

Without anchors:

```text
error
```

matches anywhere in the line.

With anchors:

```text
^error
```

matches only if the line begins with `error`.

### Example 1: beginning-of-line match

```python
# import regex support
import re

# define a line of text
line = "ERROR: failed to connect"

# ^ERROR means the string must begin with ERROR
match = re.search(r"^ERROR", line)

if match:
    print("Line starts with ERROR")
```

### Example 2: end-of-line match

```python
# import regex support
import re

# define a filename
filename = "report.txt"

# \.txt$ means the string must end with '.txt'
match = re.search(r"\.txt$", filename)

if match:
    print("This is a text file")
```

The dot is escaped because an unescaped dot means “any character” in regex.

## 3.4 Examples

This section combines metacharacters in practical patterns.

### Example 1: optional plural

```python
# import regex support
import re

# define several test strings
tests = ["apple", "apples", "pineapple"]

# apples? means:
# 'apple' followed by optional 's'
for text in tests:
    match = re.search(r"apples?", text)
    if match:
        print(f"{text} -> {match.group()}")
```

This matches `apple` and `apples`.

### Example 2: match text that begins with hello and ends with digits

```python
# import regex support
import re

# define a sample string
text = "hello_user_2026"

# ^hello means start with hello
# .* means any characters after that
# \d+$ means end with one or more digits
match = re.search(r"^hello.*\d+$", text)

if match:
    print(match.group())
```

This kind of combined pattern is common in filenames, process labels, and logs.

---

# 4. Advanced Regex Concepts

## Definition

Advanced regex concepts explain how multiple regex operators interact and how the engine decides what to match when more than one possibility exists.

These concepts matter because a regex may be syntactically valid but still behave differently from what you expected.

## 4.1 Greedy Behaviour

By default, many regex quantifiers are greedy.  
This means they try to match as much text as possible while still allowing the overall pattern to succeed.

Greedy quantifiers include:

- `*`
- `+`
- `?`
- `{m,n}`

A good mental model is:

```text
greedy regex → "take the largest match possible"
```

### Example 1: greedy matching with tags

```python
# import regex support
import re

# define a string containing two tags
text = "<tag>data</tag>"

# .* is greedy, so it tries to consume as much as possible
match = re.search(r"<.*>", text)

if match:
    print(match.group())
```

This matches the entire string:

```text
<tag>data</tag>
```

because `.*` expands as far as it can before the final `>`.

### Example 2: non-greedy matching

```python
# import regex support
import re

# define the same text
text = "<tag>data</tag>"

# .*? is non-greedy, so it stops at the earliest valid point
match = re.search(r"<.*?>", text)

if match:
    print(match.group())
```

This matches only:

```text
<tag>
```

Adding `?` after a quantifier changes it from greedy to non-greedy.

## 4.2 Grouping and Alternation

Parentheses `()` group parts of a regex together.  
The vertical bar `|` means alternation, which is similar to logical OR.

These operators are useful when a pattern has repeated structure or multiple possible forms.

Conceptually:

```text
(cat|dog)     → either cat or dog
(ab)+         → one or more repetitions of ab
```

### Example 1: alternation

```python
# import regex support
import re

# define a test line
text = "the dog ran away"

# cat|dog means match either 'cat' or 'dog'
match = re.search(r"cat|dog", text)

if match:
    print(match.group())
```

### Example 2: grouped repetition

```python
# import regex support
import re

# define text with repeated pattern
text = "ababab"

# (ab)+ means one or more repetitions of the whole group 'ab'
match = re.search(r"(ab)+", text)

if match:
    print(match.group())
```

Without parentheses, the regex would not treat `ab` as a single repeated unit.

## 4.3 Special Sequences

Special sequences are compact regex shortcuts introduced with a backslash.

Important examples include:

- `\d` → a digit `[0-9]`
- `\D` → a non-digit
- `\w` → a word character `[a-zA-Z0-9_]`
- `\W` → a non-word character
- `\s` → whitespace such as space, tab, newline
- `\S` → a non-whitespace character

These are extremely useful in system scripts because they avoid verbose character lists.

### Example 1: extracting a process number

```python
# import regex support
import re

# define a sample line
line = "Process ID: 9281"

# \d+ means one or more digits
match = re.search(r"\d+", line)

if match:
    print(match.group())
```

### Example 2: matching a username-like token

```python
# import regex support
import re

# define a string containing a user identifier
text = "current user = admin_42"

# \w+ means one or more word characters
match = re.search(r"\w+", text)

if match:
    print(match.group())
```

This returns the first word-like sequence.

## 4.4 Word Boundaries

A word boundary is a position between a word character and a non-word character, or between a word character and the start or end of the string.

The regex token is:

```text
\b
```

This is useful when you want to match a whole word rather than a substring inside another word.

Conceptually:

```text
cat\b   → cat at the end of a word
\bcat   → cat at the beginning of a word
\bcat\b → cat as a whole word
```

### Example 1: whole-word match

```python
# import regex support
import re

# define a sentence
text = "the cat sat on the mat"

# \bcat\b means match cat as a complete word
match = re.search(r"\bcat\b", text)

if match:
    print(match.group())
```

### Example 2: prevent matching inside a larger word

```python
# import regex support
import re

# define a string where 'cat' appears inside a larger word
text = "concatenate"

# \bcat\b will fail because cat is not a full word here
match = re.search(r"\bcat\b", text)

print(match)
```

This returns `None`.

## 4.5 Operator Precedence

When a regex contains several operators, Python must decide which parts are applied first.

A simplified precedence order is:

1. parentheses `()`
2. quantifiers `* + ? {m,n}`
3. sequences and anchors
4. alternation `|`

This matters because the same characters arranged differently can produce a different pattern.

Conceptually:

```text
ab|cd      → either "ab" or "cd"
a(b|c)d    → "abd" or "acd"
```

### Example 1: alternation without grouping

```python
# import regex support
import re

# define text
text = "cd"

# ab|cd means either the sequence 'ab' or the sequence 'cd'
match = re.search(r"ab|cd", text)

if match:
    print(match.group())
```

### Example 2: grouping changes meaning

```python
# import regex support
import re

# define text
text = "acd"

# a(b|c)d means:
# start with 'a'
# then either 'b' or 'c'
# then end with 'd'
match = re.search(r"a(b|c)d", text)

if match:
    print(match.group())
```

Understanding precedence helps you write patterns that behave exactly as intended.

---

# 5. Python `re` Functions

## Definition

The `re` module provides several functions for different regex tasks.

Some functions search for a match.  
Others return all matches, split text, or replace matching parts.

Choosing the right function depends on your goal:

```text
Need first match only?     → re.search
Need all matches?          → re.findall
Need to split text?        → re.split
Need to replace text?      → re.sub
Need match at start only?  → re.match
```

## 5.1 `re.search`

`re.search(pattern, string)` scans the entire string and returns the first match object if a match exists.

This is usually the most practical regex function for Unix scripting because many tasks are of the form:

```text
"Does this line contain a pattern?"
```

### Example 1: search anywhere in the line

```python
# import regex support
import re

# define a system message
line = "backup completed with warning code 7"

# search for the word warning anywhere in the line
match = re.search(r"warning", line)

if match:
    print(match.group())
```

### Example 2: find the first numeric sequence

```python
# import regex support
import re

# define text containing several tokens
text = "job id=2048 status=done"

# \d+ finds the first sequence of one or more digits
match = re.search(r"\d+", text)

if match:
    print(match.group())
```

## 5.2 `re.findall`

`re.findall(pattern, string)` returns a list of all matched substrings.

This is useful when the goal is not just to know whether a pattern exists, but to collect every occurrence.

### Example 1: extract all digits

```python
# import regex support
import re

# define a sample string
text = "a1 b22 c333"

# \d+ finds each full numeric sequence
matches = re.findall(r"\d+", text)

print(matches)
```

This returns:

```text
['1', '22', '333']
```

### Example 2: extract all words beginning with log

```python
# import regex support
import re

# define text with several tokens
text = "log log1 login logger"

# log\w* means:
# start with 'log'
# then match zero or more word characters
matches = re.findall(r"log\w*", text)

print(matches)
```

This is useful for extracting related patterns from command output.

## 5.3 `re.split`

`re.split(pattern, string)` divides a string wherever the pattern matches.

This is useful when a string uses separators that may vary or have a structure more complex than a single fixed character.

### Example 1: split on commas

```python
# import regex support
import re

# define a comma-separated string
text = "red,green,blue"

# split wherever a comma appears
parts = re.split(r",", text)

print(parts)
```

### Example 2: split on colon or semicolon

```python
# import regex support
import re

# define text with mixed separators
text = "alpha:beta;gamma"

# [:;] means either ':' or ';'
parts = re.split(r"[:;]", text)

print(parts)
```

This is more flexible than ordinary string splitting when multiple separator types may occur.

## 5.4 `re.sub`

`re.sub(pattern, replacement, string)` replaces every match of the pattern with the replacement text.

This is very useful for cleaning text, masking values, or normalising formats.

### Example 1: replace digits

```python
# import regex support
import re

# define a string containing digits
text = "user42 logged in at 09:15"

# replace every digit with X
result = re.sub(r"\d", "X", text)

print(result)
```

### Example 2: mask an ID number

```python
# import regex support
import re

# define sample text
text = "Employee ID: 58291"

# replace the numeric part with a placeholder
result = re.sub(r"\d+", "[HIDDEN]", text)

print(result)
```

This is useful when logs or reports need sanitisation.

## 5.5 `re.match`

`re.match(pattern, string)` checks only at the beginning of the string.

This is different from `re.search()`, which scans through the full string.

A useful rule is:

```text
re.match  → beginning only
re.search → anywhere in the string
```

### Example 1: match only at the start

```python
# import regex support
import re

# define a line that starts with ERROR
line = "ERROR code 503"

# re.match succeeds because ERROR is at the start
match = re.match(r"ERROR", line)

if match:
    print(match.group())
```

### Example 2: compare with a non-starting occurrence

```python
# import regex support
import re

# define a line where ERROR appears later
line = "System raised ERROR code 503"

# re.match fails because the string does not start with ERROR
match = re.match(r"ERROR", line)

print(match)
```

This returns `None`.

---

# 6. Working with Matches

## Definition

Once you know the main `re` functions, the next step is learning how they behave in realistic cases.

This includes:

- collecting multiple matches
- splitting using a pattern
- replacing matching parts
- understanding patterns that can match empty strings

These details matter because regex results are sometimes less obvious than beginners expect.

## 6.1 Using `findall`

`findall` is especially useful when a line contains several items of the same type and you want to capture all of them at once.

### Example 1: collect all numbers from a line

```python
# import regex support
import re

# define a line with multiple numbers
line = "ports 22, 80, and 443 are open"

# \d+ captures each full number
numbers = re.findall(r"\d+", line)

print(numbers)
```

This returns a list of strings, not integers.

### Example 2: extract all filenames ending in .log

```python
# import regex support
import re

# define sample text
text = "today.log error.log report.txt archive.log"

# \w+\.log matches word-like names ending with .log
matches = re.findall(r"\w+\.log", text)

print(matches)
```

This kind of extraction is common in log and file analysis.

## 6.2 Using `split`

`split` is useful when a regex describes the separators better than a simple literal string.

### Example 1: split on one or more spaces

```python
# import regex support
import re

# define text with uneven spacing
text = "alpha   beta    gamma"

# \s+ means one or more whitespace characters
parts = re.split(r"\s+", text)

print(parts)
```

This handles variable spacing much better than splitting on one literal space.

### Example 2: split a system path-like record

```python
# import regex support
import re

# define a mixed-separator record
text = "user:group|shell"

# split on either ':' or '|'
parts = re.split(r"[:|]", text)

print(parts)
```

This lets a single regex handle more than one separator.

## 6.3 Using `sub`

`sub` is central to text cleanup and transformation.

### Example 1: normalise whitespace

```python
# import regex support
import re

# define text with repeated spaces and tabs
text = "alpha\t\tbeta    gamma"

# replace one or more whitespace characters with a single space
cleaned = re.sub(r"\s+", " ", text)

print(cleaned)
```

This is very common when cleaning command output before further processing.

### Example 2: hide IP address numbers

```python
# import regex support
import re

# define a line containing an IP-like value
text = "Connection from 192.168.1.14 accepted"

# replace every digit sequence with ***
masked = re.sub(r"\d+", "***", text)

print(masked)
```

This shows how `sub` can be used for anonymisation.

## 6.4 Matching Empty Strings

Some regex patterns are allowed to match zero characters.  
This is one of the most confusing early regex concepts.

Examples include:

- `a*`
- `a?`

Why? Because:

- `*` means zero or more
- `?` means zero or one

So a match can succeed even when the character is absent.

Conceptually:

```text
pattern: a*
string : bb

possible matches:
- empty string before first b
- empty string before second b
- empty string at end
```

The regex engine must still move forward after a zero-length match, otherwise it would match the same empty position forever.

### Example 1: replacing with `a*`

```python
# import regex support
import re

# define text with no 'a' at all
text = "bb"

# a* can match empty strings, not just visible 'a' characters
result = re.sub(r"a*", "X", text)

print(result)
```

This surprises many learners because the pattern matches at several zero-length positions.

### Example 2: seeing the empty-string behaviour more clearly

```python
# import regex support
import re

# define a short string
text = "aaab"

# a* matches:
# 1. the whole run 'aaa'
# 2. an empty position before 'b'
# 3. an empty position at the end
result = re.sub(r"a*", "Z", text)

print(result)
```

This topic matters because quantifiers do not always consume visible characters.

---

# 7. Practical System Applications

## Definition

Regex becomes especially valuable in Unix systems programming when it is applied to real command-line tasks.

Typical use cases include:

- selecting lines from log files
- extracting fields from command output
- validating file names or IDs
- cleaning and transforming text streams

In these situations, regex is not used in isolation.  
It sits inside a broader Unix pipeline.

## 7.1 Processing Log Files

System logs often contain many lines, but only some of them are relevant.

Regex helps you filter lines based on structure rather than reading the file manually.

Architecture:

```text
log file
   ↓
STDIN or file redirection
   ↓
Python script
   ↓
regex filter
   ↓
matching lines only
```

### Example 1: print only ERROR lines

```python
#!/usr/bin/env python3

# import sys for stdin and re for regex matching
import sys
import re

# process each incoming log line
for line in sys.stdin:
    # remove the trailing newline for cleaner output
    line = line.rstrip('\n')

    # look for the whole word ERROR
    if re.search(r"\bERROR\b", line):
        print(line)
```

This is a realistic line filter for system logs.

### Example 2: print lines with either WARNING or ERROR

```python
#!/usr/bin/env python3

# import required modules
import sys
import re

# read log lines one by one
for line in sys.stdin:
    # strip only the final newline
    line = line.rstrip('\n')

    # match either WARNING or ERROR as whole words
    if re.search(r"\b(WARNING|ERROR)\b", line):
        print(line)
```

This is equivalent to building a more expressive log filter than a simple fixed-text search.

## 7.2 Extracting Patterns

Sometimes you do not want the entire line.  
You want only the specific pattern inside the line.

This is where match objects and `group()` are especially useful.

### Example 1: extract TASK labels from a log

```python
#!/usr/bin/env python3

# import required modules
import sys
import re

# define a regex that matches:
# TASK [anything inside square brackets]
regex = r"TASK \[.*\]"

# read input lines from stdin
for line in sys.stdin:
    # remove the trailing newline
    line = line.rstrip('\n')

    # search for the task pattern
    match = re.search(regex, line)

    # if the pattern exists, print only the matched part
    if match:
        print(match.group())
```

This extracts only the useful structured part.

### Example 2: extract all numeric IDs from a line

```python
# import regex support
import re

# define a line with multiple IDs
line = "users: 104, 208, 512"

# find every number in the line
ids = re.findall(r"\d+", line)

print(ids)
```

This is common when parsing reports, command output, or access records.

## 7.3 STDIN Redirection

A good Unix-style script should not depend on hardcoded file paths.  
Instead, it should accept input from STDIN so it can be reused easily.

You can provide input through redirection:

```bash
python3 script.py < logfile.txt
```

or through a pipe:

```bash
cat logfile.txt | python3 script.py
```

Architecture:

```text
source file or command output
            ↓
     shell redirection / pipe
            ↓
           STDIN
            ↓
       Python regex script
            ↓
      filtered or extracted output
```

### Example 1: complete STDIN-driven regex filter

```python
#!/usr/bin/env python3

# import required modules
import sys
import re

# define the pattern once so it is easy to change later
regex = r"\bFAIL(ed)?\b"

# read text line by line from stdin
for line in sys.stdin:
    # remove only the trailing newline
    line = line.rstrip('\n')

    # print lines whose content matches FAIL or FAILED
    if re.search(regex, line):
        print(line)
```

This design is flexible because the script can be connected to many different sources.

### Example 2: STDIN-driven extractor

```python
#!/usr/bin/env python3

# import required modules
import sys
import re

# pattern for one or more digits
regex = r"\d+"

# read every input line
for line in sys.stdin:
    # clean the line ending
    line = line.rstrip('\n')

    # extract all digit groups from the line
    matches = re.findall(regex, line)

    # print the line only if at least one number was found
    if matches:
        print(matches)
```

This shows a very typical Unix workflow:

- input comes from the shell
- regex performs the selection or extraction
- the script prints structured results

---

**End of Week 8**
