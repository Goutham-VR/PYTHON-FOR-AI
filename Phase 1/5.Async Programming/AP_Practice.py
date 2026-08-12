import time

# def task1():
#     print('start')
#     time.sleep(5)
#     print("end")

# task1()

# import asyncio

# async def test():
#     print("Start")
#     await asyncio.sleep(2)
#     print("End")

# asyncio.run(test())

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