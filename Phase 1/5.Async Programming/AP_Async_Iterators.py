# You already know normal:

# for item in data:
#     print(item)

# Now we'll learn:

# async for item in data:
#     print(item)

# This is useful when data arrives asynchronously, such as streaming data from an API or database.

# Normal forloop
numbers = [10, 20, 30]

for number in numbers:
    print(number)

# ============================================================
# ASYNC FOR
# ============================================================

# Imagine data arrives one item at a time from a network:
#
# Request
#    ↓
# wait
#    ↓
# 10 arrives
#    ↓
# wait
#    ↓
# 20 arrives
#    ↓
# wait
#    ↓
# 30 arrives
#
# We don't want to block the whole program while waiting
# for each item.
#
# So we can use:
#
# async for item in data:
#     print(item)


# ============================================================
# CREATING AN ASYNC ITERATOR
# ============================================================

# An async iterator uses two special methods:
#
# __aiter__()  → tells Python which object is the iterator
# __anext__()  → produces the next value asynchronously


import asyncio


class Numbers:

    # --------------------------------------------------------
    # __aiter__()
    # --------------------------------------------------------
    # This is a NORMAL method, not async.
    #
    # Its job is simply to return the async iterator object.
    #
    # Here, "self" itself is the iterator.
    #
    # We also initialize our state here.
    # --------------------------------------------------------

    def __aiter__(self):
        self.number = 1

        # Return the iterator.
        # In this example, the Numbers object itself
        # is the async iterator.
        return self


    # --------------------------------------------------------
    # __anext__()
    # --------------------------------------------------------
    # This is an ASYNC method.
    #
    # Its job is to provide the NEXT value.
    #
    # Because getting the next value might involve waiting
    # for something (network, database, file, etc.),
    # this method can use "await".
    # --------------------------------------------------------

    async def __anext__(self):

        # If there are no more values,
        # tell async for that iteration is finished.
        #
        # IMPORTANT:
        # Async iterators use StopAsyncIteration,
        # not StopIteration.
        if self.number > 3:
            raise StopAsyncIteration


        # Save the current number.
        value = self.number


        # Move to the next number.
        #
        # First call:
        #   number = 1 → then becomes 2
        #
        # Second call:
        #   number = 2 → then becomes 3
        #
        # Third call:
        #   number = 3 → then becomes 4
        self.number += 1


        # Simulate waiting for data to arrive.
        #
        # In a real application, this could be:
        #
        #   await network_request()
        #   await database_query()
        #   await read_from_stream()
        #
        # asyncio.sleep() does NOT block the whole event loop.
        await asyncio.sleep(1)


        # Give the value back to async for.
        return value



# ============================================================
# MAIN
# ============================================================

async def main():

    # async for works with an ASYNC ITERABLE.
    #
    # Python will internally use:
    #
    #   __aiter__()
    #   __anext__()
    #
    # repeatedly.
    async for number in Numbers():

        # Print each value when it arrives.
        print(number)


# Start the async program.
asyncio.run(main())