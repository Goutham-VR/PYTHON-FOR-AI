# GATHER
# gather() — "Run these together and give me the results"
# usecase:await asyncio.gather(task1(), task2())
# think:"Run these coroutines concurrently, and wait until all of them finish."

# eg:
import asyncio

async def task1():
    await asyncio.sleep(2)
    return "A"

async def task2():
    await asyncio.sleep(1)
    return "B"

async def main():
    results = await asyncio.gather(task1(), task2())
    print(results)

asyncio.run(main())

# op:
# ['A', 'B'] 
# Even though Task 2 finishes first, gather() returns the results in the order you provided them:

# CREATE_TASK
# create_task() — "Schedule this task"
t1 = asyncio.create_task(task1())
t2 = asyncio.create_task(task2())

# Now you have task objects:
# t1 → Task 1
# t2 → Task 2

# You can do other work:
print("Something else")
# and later:
result1 = await t1
result2 = await t2