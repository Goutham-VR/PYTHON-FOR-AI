# Async Context Managers

# You know the normal context manager:
# with something:
#     ...

# For asynchronous resources, we use:
# async with something:
#     ...

# 1. Why async with?
# For example, imagine opening an async database connection:
# Request connection
#       ↓
# WAIT ⏳
#       ↓
# Connection available
#       ↓
# Use connection
#       ↓
# Close connection

# 2. Normal vs Async Context Manager

# Normal
# with resource:
#     print("Using resource")

# Uses:
    # __enter__()
    # __exit__()

# Async
# async with resource:
    #     print("Using resource")

# Uses:
    # __aenter__()
    # __aexit__()

# Notice the a:

    # __enter__   → normal
    # __aenter__  → async

    # __exit__    → normal
    # __aexit__   → async

# Eg
import asyncio
class MyAsyncContext:
    async def __aenter__(self):
        print("Entering")

    async def __aexit__(self, exc_type, exc, tb):
        print("End")

async def main():
    async with MyAsyncContext():
        print("Inside")

asyncio.run(main())

#dataase example
class Database:
    async def __aenter__(self):
        print("Connecting...")
        # await database connection
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        print("Closing connection...")
        # await database close

async def main():
    async with Database() as db:
        print("Run query")

asyncio.run(main())

