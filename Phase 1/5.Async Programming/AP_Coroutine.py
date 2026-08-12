import asyncio

async def task():
    print("Hello")

asyncio.run(task()) # this is right way of calling async fun
task() # but this create coroutine object

#try to print it
x=task()
print(x)

# op:
# shows something like this:
# <coroutine object task at 0x00000159145ECAC0>
# it doesnot execute print("Hello"), It creates a coroutine that is waiting to be executed by the event loop.

# How do we actually run it?
# asyncio.run()
# eg:
import asyncio

async def task():
    print("Hello")

asyncio.run(task())

# Another way: await:
# Inside another async function:
import asyncio

async def task():
    print("Hello")

async def main():
    await task() #This tells the event loop to execute the coroutine and wait for its result.

asyncio.run(main())

import asyncio

async def maintask():
    return 10

async def main():
    data=await maintask() #This tells the event loop to execute the coroutine and wait for its result.
    print(data)

asyncio.run(main())

# Coroutine + Async Wait
import asyncio

async def coas():
    print("Task Start")
    await asyncio.sleep(2)
    print("Task End")
    return 100

async def main():
    result=await coas() #This tells the event loop to execute the coroutine and wait for its result.
    print("Result:",result)

asyncio.run(main())

