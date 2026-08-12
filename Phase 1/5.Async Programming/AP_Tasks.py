# asyncio.create_task(). This is an important step because it explains how async tasks actually run concurrently.
# await task() - means:Start the coroutine and wait for it to finish.
# But sometimes we don't want to wait immediately.
# We want to tell the event loop: "Start this task. I'll do something else while it's running."
# That's what create_task() helps us do.

# Without create_task()

import asyncio
async def task1():
    print("Task 1 start")
    await asyncio.sleep(2)
    print("Task 1 end")
async def task2():
    print("Task 2 start")
    await asyncio.sleep(1)
    print("Task 2 end")
async def main():
    await task1()
    await task2()
asyncio.run(main())

# Task 1 start
#       ↓
# WAIT 2 sec
#       ↓
# Task 1 end
#       ↓
# Task 2 start
#       ↓
# WAIT 1 sec
#       ↓
# Task 2 end

# Total ≈ 3 seconds.

# Because we explicitly wait for Task 1 before starting Task 2.

# With create_task()
import asyncio
async def task1():
    print("Task 1 start")
    await asyncio.sleep(2)
    print("Task 1 end")
async def task2():
    print("Task 2 start")
    await asyncio.sleep(1)
    print("Task 2 end")
async def main():
    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())

    await t1
    await t2
asyncio.run(main())
# now
    #       Event Loop
    #           ↓
    #    ┌──────┴──────┐
    #    ↓             ↓
    #   t1             t2
    #    ↓             ↓
    # waiting 2s    waiting 1s
    #    ↓             ↓
    #    │          finishes
    #    ↓
    # finishes

# when using gather there is no need for create_task but 
# to control individual task we must use create_task()
# eg:

# t1 = asyncio.create_task(task1())
# t2 = asyncio.create_task(task2())
# print("Tasks started!")
# await t1
# await t2

# here we can control task using t1 and t2 variables

# create_task() vs await
# This distinction is VERY important.

# await task1()
# Think: "Run task1 and wait for it."

# t1 = asyncio.create_task(task1())
# Think: "Schedule task1. I'll continue doing other things."

# Then later: await t1
# means:"Now wait for task1 to finish and give me its result."

# eg:
import asyncio

async def task1():
    print("A")
    await asyncio.sleep(2)
    print("B")

async def task2():
    print("C")
    await asyncio.sleep(1)
    print("D")

async def main():

    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())

    print("E")

    await t1
    await t2

asyncio.run(main())