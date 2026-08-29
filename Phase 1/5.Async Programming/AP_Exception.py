# Normal Python exception handling
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

print("Program continues")

# output:
# Cannot divide by zero
# Program continues

# Without try/except:
# x = 10 / 0
# print("Program continues")
# ZeroDivisionError
# Program continues does not execute.

#async program
import asyncio

async def task():
    print("Start")
    await asyncio.sleep(1)
    x = 10 / 0
    print("End")

async def main():
    await task()

asyncio.run(main())
# Start
#   ↓
# wait 1 second
#   ↓
# 10 / 0 💥 got error in this case
#   ↓
# Exception
#   ↓
# main() stops

# output:
# Start
# ZeroDivisionError

# End doesn't print.

#another eg
async def task():
    print("Start")
    await asyncio.sleep(1)
    x = 10 / 0
    print("End")

async def taskw():
    print("Start")
    await asyncio.sleep(1)
    x = 10 / 0
    print("End")

async def main():
    result = await asyncio.gather(task(), taskw()) #gather used so all task run but task return error
    print("result", result)

asyncio.run(main())
#gather used so all task run but task return error, never stop in task
# gather() does not mean:"If one task fails, stop all other tasks."



# Adding Try/Except in Async
import asyncio

async def task():
    print("Start")

    try:
        await asyncio.sleep(1)
        x = 10 / 0
        print("End")

    except ZeroDivisionError:
        print("Error handled")

async def main():
    await task()

asyncio.run(main())

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

async def main8():
    t5 = asyncio.create_task(task15())
    t6 = asyncio.create_task(task16())

    await t5
    await t6

    print("t5",t5)
    print("t6",t6)

asyncio.run(main8())

# Exception with task and return values
import asyncio

async def task17():
    print('Start Task 17')
    try:
        await asyncio.sleep(4)
        x=10/0
        print("End task 17")
    except ZeroDivisionError:
        print("Error Handled")

async def task18():
    print('Start Task 18')
    try:
        await asyncio.sleep(1)
        x=10/0
        print("End task 18")
    except ZeroDivisionError:
        print("Error Handled")

async def task19():
    print('Start Task 19')
    try:
        await asyncio.sleep(1)
        data="Hello World"
        x=10/0
        print("End task 19")
        return data #returning data
    except ZeroDivisionError:
        print("Error Handled")
        return data #returning data

async def main9():
    t8 = asyncio.create_task(task17())
    t9 = asyncio.create_task(task18())
    t10 = asyncio.create_task(task19())

    await t8
    await t9
    t10data = await t10 #store returned data to variable

    print("t8",t8)
    print("t9",t9)
    print("t10",t10data)

asyncio.run(main9())

# Why is async exception handling important?
# Imagine you have three API calls:
# Task A → API call
# Task B → API call
# Task C → API call

# A → ✅
# B → ❌
# C → ✅

# Suppose B fails:
# If you don't handle the exception properly, it can affect how your await/gather() flow completes.
# for eg:
import asyncio

async def task1():
    await asyncio.sleep(1)
    return "A"

async def task2():
    await asyncio.sleep(1)
    raise ValueError("Task 2 failed")

async def task3():
    await asyncio.sleep(1)
    return "C"

async def main():
    result = await asyncio.gather(
        task1(),
        task2(),
        task3()
    )

    print(result)

asyncio.run(main())

# output
# Task 1 → A
# Task 2 → ERROR ❌
# Task 3 → C

#         ↓
#     gather()
#         ↓
#     exception

# Handling the exception outside gather()
import asyncio

async def task1():
    print("Start Task1")
    await asyncio.sleep(1)
    print("End Task1")
    return "A"

async def task2():
    print("Start Task2")
    await asyncio.sleep(1)
    raise ValueError("Task 2 failed")

async def task3():
    print("Start Task3")
    await asyncio.sleep(1)
    print("Start Task1")
    return "C"

async def main():
    try:
        result = await asyncio.gather(
            task1(), 
            task2(),
            task3()
        )

        print(result)

    except ValueError as e:
        print("Error:", e)

asyncio.run(main())
# output:
# Start Task1
# Start Task2
# Start Task3
# End Task1
# Start Task1
# Error: Task 2 failed

# here task1,task2,task3 all executed
# but task2 failed but and not stop in task2 it coninues to rest

#another example:
import asyncio

async def task1():
    print("Start Task1")
    await asyncio.sleep(1)
    print("End Task1")
    return "A"

async def task2():
    print("Start Task2")
    await asyncio.sleep(1)
    raise ValueError("Task 2 failed") # value error

async def task3():
    print("Start Task3")
    await asyncio.sleep(1)
    raise ValueError("Task 2 failed") # value error


async def main():
    try:
        result = await asyncio.gather(
            task1(), 
            task2(),
            task3()
        )

        print(result)

    except ValueError as e:
        print("Error:", e)

asyncio.run(main())
# output:
# Start Task1
# Start Task2
# Start Task3
# End Task1
# Start Task1
# Error: Task 2 failed

# same output like previous one
# So is C actually executed? Yes.
# C starts: and continues to:await asyncio.sleep(4) then raise ValueError("Task C Failed")
# why no output for c? The problem is that your main() doesn't collect C's exception.

# If you want to see both B and C failures, use: return_exceptions=True
# Eg:
# result = await asyncio.gather(
#     task1(),
#     task2(),
#     task3(),
#     return_exceptions=True
# )
# print(result)

# EG:
import asyncio

async def taska():
    print("Start Task A")
    await asyncio.sleep(4)
    print("End Task A")
    return "A completed"


async def taskb():
    print("Start Task B")
    await asyncio.sleep(4)
    raise ValueError("B failed")


async def taskc():
    print("Start Task C")
    await asyncio.sleep(4)
    raise ValueError("C failed")


async def main():

    result = await asyncio.gather(
        taska(),
        taskb(),
        taskc(),
        return_exceptions=True
    )

    print(result)


asyncio.run(main())

# With gather(return_exceptions=True)
# Task A → result
# Task B → exception
# Task C → exception
#        ↓
# gather()
#        ↓
# all results returned