# Async Programming 

# Now we start Async Programming from zero.

# The first thing to understand is:

# Async programming allows a program to work on other tasks while one task is waiting.

# This is especially useful for:

# API calls
# Database operations
# Network requests
# File/network I/O
# Web applications
# AI APIs

# It is not primarily about making CPU-heavy ML training faster. For heavy CPU/GPU work, multiprocessing, threads, or GPU parallelism may be more appropriate.

import time

def task1():
    print("Task 1 started")
    time.sleep(3)
    print("Task 1 finished")

def task2():
    print("Task 2 started")
    print("Task 2 finished")

task1()
task2()

# Task 1 started
#      ↓
# WAIT 3 seconds ⏳ During those 3 seconds, Python is basically waiting.
#      ↓
# Task 1 finished
#      ↓
# Task 2 started
#      ↓
# Task 2 finished

# Async Idea:

# With async programming, we can say:

# "While Task 1 is waiting, work on Task 2."
# Task 1 starts
#      ↓
# Task 1 waits ⏳
#      ↓
#        Task 2 starts
#           ↓
#        Task 2 finishes
#           ↓
# Task 1 finishes

# The async Keyword
# An asynchronous function is defined using:
# async def

# eg:
async def task():
    print("Hello")

task()
# But there is something important:
# You cannot normally call it like a regular function and expect it to execute immediately.
# This creates a coroutine object.


# await
# Inside an async function, we can use:
# eg:
import asyncio

async def task():
    print("Start")
    await asyncio.sleep(2)
    print("End")

# here await asyncio.sleep(2) means approximately:
# "I'm waiting for 2 seconds. While I'm waiting, the event loop can work on another async task."

# Python provides the asyncio library for asynchronous programming.
import asyncio

# simple program
import asyncio

async def task():
    print("Hello")

asyncio.run(task())


#program
import asyncio

async def test():
    print("Start")
    await asyncio.sleep(2)
    print("End")

asyncio.run(test())
# her ewe cannot see result beacouse there is no concurrent tasks


#Multi tasking
import asyncio

async def task1():
    print("Task1 start")
    await asyncio.sleep(4)
    print("Task1 End")

async def task2():
    print ("Task 2 Start")
    await asyncio.sleep(1)
    print ("Task 2 End")

async def task3():
    print ("Task 3 Start")
    await asyncio.sleep(10)
    print ("Task 3 End")

async def main():
    await asyncio.gather(task1(),task2(),task3())

asyncio.run(main())

#op
# Task1 start
# Task 2 Start
# Task 3 Start
# Task 2 End
# Task1 End
# Task 3 End