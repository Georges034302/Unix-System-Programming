# Week 12 — Processes, IPC, and Sockets in Unix and Python

## Table of Contents
1. [Processes in Unix](#1-processes-in-unix)
    - [1.1 Program vs Process](#11-program-vs-process)
    - [1.2 Main Components of a Process](#12-main-components-of-a-process)
    - [1.3 Processes vs Threads](#13-processes-vs-threads)

2. [Process Management Commands](#2-process-management-commands)
    - [2.1 Listing Processes with ps](#21-listing-processes-with-ps)
    - [2.2 Terminating Processes with kill](#22-terminating-processes-with-kill)
    - [2.3 Useful Monitoring Patterns](#23-useful-monitoring-patterns)

3. [Creating Processes in Unix](#3-creating-processes-in-unix)
    - [3.1 The fork Model](#31-the-fork-model)
    - [3.2 Parent and Child Execution](#32-parent-and-child-execution)
    - [3.3 Python fork Example](#33-python-fork-example)

4. [Interprocess Communication (IPC) Overview](#4-interprocess-communication-ipc-overview)
    - [4.1 Why IPC Is Needed](#41-why-ipc-is-needed)
    - [4.2 Main IPC Styles](#42-main-ipc-styles)
    - [4.3 Choosing an IPC Mechanism](#43-choosing-an-ipc-mechanism)

5. [Files, Pipes, and FIFOs](#5-files-pipes-and-fifos)
    - [5.1 Files as IPC](#51-files-as-ipc)
    - [5.2 Pipes in Unix and Python](#52-pipes-in-unix-and-python)
    - [5.3 FIFOs (Named Pipes)](#53-fifos-named-pipes)

6. [Sockets and Network Communication](#6-sockets-and-network-communication)
    - [6.1 What a Socket Is](#61-what-a-socket-is)
    - [6.2 TCP vs UDP](#62-tcp-vs-udp)
    - [6.3 Core Socket Methods in Python](#63-core-socket-methods-in-python)

7. [Other IPC Mechanisms](#7-other-ipc-mechanisms)
    - [7.1 Signals](#71-signals)
    - [7.2 Semaphores](#72-semaphores)
    - [7.3 Shared Memory and Queues](#73-shared-memory-and-queues)

8. [Practical Python Examples](#8-practical-python-examples)
    - [8.1 Parent-Child with fork](#81-parent-child-with-fork)
    - [8.2 One-Way Pipe Example](#82-one-way-pipe-example)
    - [8.3 Minimal TCP Server and Client](#83-minimal-tcp-server-and-client)

9. [Summary and Best Practices](#9-summary-and-best-practices)
    - [9.1 Key Takeaways](#91-key-takeaways)
    - [9.2 Common Mistakes](#92-common-mistakes)
    - [9.3 Recommended Practice Tasks](#93-recommended-practice-tasks)

---

# 1. Processes in Unix

A process is a running instance of a program. A program is a file on disk (passive), while a process is an active execution context in memory.

In systems programming, this distinction matters because you are usually controlling running behavior, not just static files.

## 1.1 Program vs Process

A program becomes a process when the operating system loads it, allocates memory, sets CPU context, and starts execution.

### Example 1

```bash
ls
```

This runs `ls` as a short-lived process. It starts, lists entries, and exits.

### Example 2

```bash
python3 hello.py
```

This starts one Python interpreter process that loads and executes `hello.py`.

## 1.2 Main Components of a Process

A process usually includes:

- Code segment: instructions (typically read-only)
- Data segment: global/static runtime data
- Stack segment: function calls and local variables
- CPU registers: process execution state, including program counter

Important behavior:

- Different processes from the same program can share code pages
- Their writable data is separated by default

## 1.3 Processes vs Threads

Processes provide stronger isolation. Threads are lighter but share memory within one process.

Threads can be faster for communication, but shared memory means race conditions are easier to create.

---

# 2. Process Management Commands

Unix provides command-line tools to inspect process state and send control signals.

## 2.1 Listing Processes with ps

`ps` gives a snapshot of process information.

### Example 1

```bash
ps -ef
```

Shows all processes with extra details such as PID, PPID, start time, and command.

### Example 2

```bash
ps -u "$USER"
```

Filters processes to the current user.

## 2.2 Terminating Processes with kill

`kill` sends a signal to a process ID. It does not always mean force-kill.

### Example 1

```bash
kill -s SIGTERM 12345
```

Requests graceful termination. This is usually the first signal to try.

### Example 2

```bash
kill -9 12345
```

Sends `SIGKILL`, which stops immediately and cannot be handled by the target process.

## 2.3 Useful Monitoring Patterns

You can monitor your terminal's processes with pipelines.

```bash
ps -e | grep pts/0
```

This helps identify processes attached to a specific pseudo-terminal.

---

# 3. Creating Processes in Unix

Unix process creation is based on `fork()`, and often followed by `exec()` to run a different program.

## 3.1 The fork Model

`fork()` duplicates the current process.

- Parent receives child PID (non-zero)
- Child receives `0`
- Both continue from the next instruction

## 3.2 Parent and Child Execution

After `fork()`, parent and child execute the same code path unless conditional logic separates behavior.

Because execution continues from the same point, branching on `pid` is mandatory for clear behavior.

## 3.3 Python fork Example

### Example 1

```python
#!/usr/bin/env python3
import os
import time

print("[START] Initial process PID:", os.getpid())

# fork duplicates the current process.
pid = os.fork()

if pid == 0:
    # Child branch: pid is 0 here.
    print("[CHILD] My PID:", os.getpid())
    print("[CHILD] My parent PID:", os.getppid())
    time.sleep(1)  # Keep child alive briefly for `ps` observation.
else:
    # Parent branch: pid is child PID here.
    print("[PARENT] My PID:", os.getpid())
    print("[PARENT] Child PID:", pid)
    time.sleep(1)  # Keep parent alive briefly for `ps` observation.
```

This example highlights the two return values from `fork()` and why branch checks are required.

---

# 4. Interprocess Communication (IPC) Overview

Multiple processes often need to coordinate work, exchange data, or signal events. IPC provides these mechanisms.

## 4.1 Why IPC Is Needed

IPC is needed when tasks are split for modularity, performance, or reliability. Examples include:

- Producer-consumer pipelines
- Parent-worker models
- Client-server applications

## 4.2 Main IPC Styles

Common IPC mechanisms in Unix:

- Files
- Pipes and FIFOs
- Sockets
- Signals
- Semaphores
- Shared memory
- Message queues

## 4.3 Choosing an IPC Mechanism

Simple decision guide:

- Files: easiest, persistent, slower
- Pipes/FIFOs: stream data, local processes
- Sockets: local or remote communication
- Shared memory: fastest data exchange, more synchronization required
- Queues: object/message passing with cleaner producer-consumer design

---

# 5. Files, Pipes, and FIFOs

## 5.1 Files as IPC

One process writes to disk, another process reads later. This is robust and simple but not real-time by default.

### Example 1

```python
#!/usr/bin/env python3

# Writer process: save status to a shared file.
with open("status.txt", "w", encoding="utf-8") as file:
    file.write("READY")  # Data becomes available for other processes.
```

### Example 2

```python
#!/usr/bin/env python3

# Reader process: load status from the same file.
with open("status.txt", "r", encoding="utf-8") as file:
    status = file.read().strip()  # strip removes trailing newline/spaces.

print("Status from writer:", status)
```

## 5.2 Pipes in Unix and Python

A pipe is a one-way in-memory byte stream.

- Reader blocks if no data
- Writer blocks if buffer full

### Example 1

```bash
ls -Rl | more
```

`ls -Rl` writes to stdout, `more` reads from stdin through a pipe.

### Example 2

```python
#!/usr/bin/env python3
import os

# Create pipe before fork so both parent and child inherit it.
read_fd, write_fd = os.pipe()
pid = os.fork()

if pid > 0:
    # Parent writes data.
    os.close(read_fd)  # Close unused read end for safety.
    with os.fdopen(write_fd, "w") as writer:
        writer.write("USP 32547")  # Send text to child.
    print("[PARENT] Sent message to child")
else:
    # Child reads data.
    os.close(write_fd)  # Close unused write end for safety.
    with os.fdopen(read_fd, "r") as reader:
        message = reader.read()  # Blocks until parent writes/closes.
    print("[CHILD] Received:", message)
```

## 5.3 FIFOs (Named Pipes)

FIFOs are pipes with a filesystem name, allowing unrelated processes to communicate if they know the path.

### Example 1

```bash
mkfifo fifo
ls -l fifo
```

The first permission character `p` indicates a FIFO special file.

### Example 2

```python
#!/usr/bin/env python3

# FIFO reader: run this in one terminal.
with open("fifo", "r", encoding="utf-8") as fifo_file:
    data = fifo_file.read()  # Waits until writer sends data.

print("FIFO received:", data)
```

In another terminal, write with `echo "hello" > fifo`.

---

# 6. Sockets and Network Communication

Sockets are communication endpoints used for local and network IPC.

## 6.1 What a Socket Is

A socket endpoint combines address family, protocol, and an address like host:port.

Example: `127.0.0.1:5000` means local host (IPv4) on port 5000.

## 6.2 TCP vs UDP

TCP (stream):

- Connection-oriented
- Reliable and ordered
- Suitable for file transfer, APIs, web traffic

UDP (datagram):

- Connectionless
- No guaranteed delivery/order
- Suitable for low-latency telemetry or media where drops are acceptable

## 6.3 Core Socket Methods in Python

TCP server flow:

1. Create socket
2. Bind host and port
3. Listen for clients
4. Accept one connection
5. Receive and send data
6. Close sockets

TCP client flow:

1. Create socket
2. Connect to server
3. Send and receive data
4. Close socket

For UDP, use `socket.SOCK_DGRAM`, `sendto()`, and `recvfrom()`.

---

# 7. Other IPC Mechanisms

## 7.1 Signals

Signals are asynchronous notifications to processes.

Common signals:

- `SIGINT`: interrupt (Ctrl+C)
- `SIGTERM`: graceful termination request
- `SIGKILL`: immediate forced termination

### Example 1

```python
#!/usr/bin/env python3
import os
import signal

target_pid = 12345

# Ask process to terminate gracefully.
os.kill(target_pid, signal.SIGTERM)
```

## 7.2 Semaphores

Semaphores limit concurrent access to shared resources.

Use semaphores to avoid race conditions when N workers share one resource.

### Example 1

```python
import threading

# Allow up to 2 threads in critical section at once.
sem = threading.Semaphore(2)

def worker(name):
    with sem:  # Automatically acquire/release semaphore.
        print(name, "entered protected section")
```

## 7.3 Shared Memory and Queues

`multiprocessing.shared_memory` provides fast shared blocks.

`multiprocessing.Queue` provides safer message passing with Python objects.

### Example 1

```python
from multiprocessing import Queue

q = Queue()
q.put({"task": "parse", "id": 7})  # Send dictionary object.
item = q.get()  # Receive object in another process.
print(item)
```

---

# 8. Practical Python Examples

## 8.1 Parent-Child with fork

```python
#!/usr/bin/env python3
import os
import time

pid = os.fork()  # Duplicate process.

if pid == 0:
    # Child process branch.
    print("[CHILD] PID:", os.getpid(), "PPID:", os.getppid())
    time.sleep(2)  # Keep alive briefly for process inspection.
else:
    # Parent process branch.
    print("[PARENT] PID:", os.getpid(), "Child PID:", pid)
    time.sleep(2)
```

## 8.2 One-Way Pipe Example

```python
#!/usr/bin/env python3
import os

# Create one-direction channel.
r, w = os.pipe()
pid = os.fork()

if pid > 0:
    # Parent writes bytes to pipe.
    os.close(r)  # Close read end not used by parent.
    os.write(w, b"hello from parent")  # Send message bytes.
    os.close(w)
else:
    # Child reads bytes from pipe.
    os.close(w)  # Close write end not used by child.
    message = os.read(r, 1024)
    print("[CHILD]", message.decode("utf-8"))  # Decode bytes to text.
    os.close(r)
```

## 8.3 Minimal TCP Server and Client

### Server

```python
#!/usr/bin/env python3
import socket

HOST = "127.0.0.1"
PORT = 5000

# Create TCP socket.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))  # Reserve host+port for this server.
server.listen(1)  # Queue up to 1 pending connection.

conn, addr = server.accept()  # Block until one client connects.
print("Connected by", addr)

conn.sendall(b"Hello client")  # Send bytes to connected client.
conn.close()  # Close per-client socket.
server.close()  # Close listening socket.
```

### Client

```python
#!/usr/bin/env python3
import socket

HOST = "127.0.0.1"
PORT = 5000

# Create TCP socket and connect to server.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

data = client.recv(1024)  # Read up to 1024 bytes from server.
print(data.decode("utf-8"))

client.close()
```

---

# 9. Summary and Best Practices

## 9.1 Key Takeaways

- A process is an active runtime instance of a program
- `fork()` creates a parent-child execution split
- IPC is essential for coordinating independent processes
- Pipes/FIFOs are good local stream channels
- Sockets are the standard mechanism for network communication

## 9.2 Common Mistakes

- Forgetting to close unused pipe ends after `fork()`
- Using `SIGKILL` as first choice instead of `SIGTERM`
- Assuming UDP guarantees ordering/delivery
- Mixing text and bytes incorrectly in pipe/socket code
- Hardcoding ports already in use without handling bind errors

## 9.3 Recommended Practice Tasks

1. Write a script that forks and prints parent PID, child PID, and PPID.
2. Implement a one-way pipe where parent sends three messages and child prints each.
3. Create a FIFO-based sender and receiver script using `mkfifo`.
4. Build a TCP echo server and test with two client requests.
5. Compare TCP and UDP by sending 100 short messages and observing behavior.

---

**End of Week 12**