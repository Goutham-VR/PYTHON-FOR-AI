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

# import asyncio

# async def task1():
#     print("Task1 start")
#     await asyncio.sleep(4)
#     print("Task1 End")

# async def task2():
#     print ("Task 2 Start")
#     await asyncio.sleep(1)
#     print ("Task 2 End")

# async def task3():
#     print ("Task 3 Start")
#     await asyncio.sleep(10)
#     print ("Task 3 End")

# async def main():
#     await asyncio.gather(task1(),task2(),task3())

# asyncio.run(main())

import asyncio

async def task4():
    print("start something")
    await asyncio.sleep(3)
    print("end something")

async def task5():
    print("start something task 5")
    await asyncio.sleep(2)
    print("end something task 5")

async def main1():
    await asyncio.gather(task4(),task5())

asyncio.run(main1())



import asyncio
async def task6():
    return 100

async def main2():
    data=await task6()
    print(data)

asyncio.run(main2())

# coroutine + async wait
import asyncio
async def task7():
    print("Task 7 start")
    await asyncio.sleep(3)
    print('Task 7 End')
    return 400

async def main3():
    res=await task7()
    print("Result:",res)

asyncio.run(main3())

# coroutine + async wait with 2 task
import asyncio
async def task8():
    print("Task 8 start")
    await asyncio.sleep(3)
    print('Task 8 End')
    return 800

async def task9():
    print("Task 9 start")
    await asyncio.sleep(1)
    print('Task 9 End')
    return 900

async def main4():
    res1=await task8()
    res2=await task9() 
    print("Result1:",res1)
    print("Result2:",res2)

asyncio.run(main4())
#Drawback: here wait for Task 8 before starting Task 9.
#Solution: use create_task().
# eg:
import asyncio
async def task10():
    print("Task 10 start")
    await asyncio.sleep(3)
    print('Task 10 End')
    return 1000

async def task11():
    print("Task 11 start")
    await asyncio.sleep(1)
    print('Task 11 End')
    return 1100

async def main5():
    t1=asyncio.create_task(task10())
    t2=asyncio.create_task(task11())

    await t1
    await t2
    print("Result T1:",t1)
    print("Result T2:",t2)

asyncio.run(main5())

# Adding Try/Except in Async
import asyncio

async def task12():
    print('Start Task 12')
    try:
        await asyncio.sleep(3)
        x=10/0
        print("End task 12")
    except ZeroDivisionError:
        print("Error Handled")

async def main6():
    await task12()

asyncio.run(main6())

# Exception with gather
import asyncio

async def task13():
    print('Start Task 13')
    try:
        await asyncio.sleep(4)
        x=10/0
        print("End task 13")
    except ZeroDivisionError:
        print("Error Handled")

async def task14():
    print('Start Task 14')
    try:
        await asyncio.sleep(1)
        x=10/0
        print("End task 14")
    except ZeroDivisionError:
        print("Error Handled")

async def main7():
    await asyncio.gather(task13(),task14())
    
asyncio.run(main7())

# Exception with task
import asyncio

async def task15():
    print('Start Task 15')
    try:
        await asyncio.sleep(4)
        x=10/0
        print("End task 15")
    except ZeroDivisionError:
        print("Error Handled")

async def task16():
    print('Start Task 16')
    try:
        await asyncio.sleep(1)
        x=10/0
        print("End task 16")
    except ZeroDivisionError:
        print("Error Handled")

async def task17():
    print('Start Task 17')
    try:
        await asyncio.sleep(1)
        data="Hello World"
        x=10/0
        print("End task 17")
        return data
    except ZeroDivisionError:
        print("Error Handled")
        return data

async def main8():
    t5 = asyncio.create_task(task15())
    t6 = asyncio.create_task(task16())
    t7 = asyncio.create_task(task17())

    await t5
    await t6
    t7data=await t7

    print("t5",t5)
    print("t6",t6)
    print("t7",t7data)

asyncio.run(main8())

import asyncio
async def taska():
    print("Start Task A")
    await asyncio.sleep(4)
    print("End Task A")

async def taskb():
    print("Start Task B")
    await asyncio.sleep(4)
    raise ValueError("Task B Failed")

async def taskc():
    print("Start Task C")
    await asyncio.sleep(4)
    raise ValueError("Task C Failed")

async def main():
    try:
        result=await asyncio.gather(taska(),taskb(),taskc())
        print(result)
    except ValueError as e:
        print("Error:",e)

asyncio.run(main())

#context manager and async programming
import asyncio

class asynccontextmanager:
    async def __aenter__(self):
        print("Enter")
    async def __aexit__(self, exc_type, exc, tb):
        print("End")

async def main():
    async with asynccontextmanager():
        print('hai')

asyncio.run(main())

class asynccontextmanager2:
    async def __aenter__(self):
        print("Enter")

    async def __aexit__(self, exc_type, exc, tb):
        print("Exit")

async def main():
    async with asynccontextmanager2():
        print("Hello World")

asyncio.run(main())

import asyncio
class asynccontextmanager3:
    async def __aenter__(self):
        print("Starting")

    async def __aexit__(self, exc_type, exc, tb):
        print("Exiting")
        print("Exception Type:",exc_type)
        print("Exception Value:",exc)

async def main():
    async with asynccontextmanager3():
        # x=10
        x=10/0
        print('Result:',x)

asyncio.run(main())

import asyncio
class asynccontext:
    async def __aenter__(self):
        print("Enter")

    async def __aexit__(self, exc_type, exc, tb):
        if exc_type:
            print("Exception Type:",exc_type)
        if exc:
            print("Exception Value:",exc)

async def main():
    async with asynccontext():
        print("hai")

asyncio.run(main())

#itrator
import asyncio
class Number:
    def __aiter__(self):
        self.number=3
        return self
    async def __anext__(self):
        if self.number>3:
            raise StopAsyncIteration
        value=self.number
        self.number+=1

        await asyncio.sleep(1)
        return value

async def main():
    async for number in Number():
        print(number)

asyncio.run(main())