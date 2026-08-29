# ============================================================
#                    CONTEXT MANAGERS
# ============================================================

# A Context Manager is an object that manages a resource
# automatically.
#
# The main purpose is:
#
#     Automatically acquire a resource
#     and clean it up when we are finished.
#
# Common resources:
#
# - Files
# - Database connections
# - Network connections
# - Locks
# - Transactions
#
#
# The most common syntax is:
#
#     with resource:
#         code
#
#
# Example:
#
#     with open("data.txt", "r") as file:
#         data = file.read()
#
#
# The "with" statement is using a Context Manager.


# ============================================================
# 1. THE PROBLEM WITHOUT A CONTEXT MANAGER
# ============================================================

# We can open a file normally:

file = open("data.txt", "r")

data = file.read()

file.close()


# The problem:
#
# We have to remember to call:
#
#     file.close()
#
#
# What if an error happens before file.close()?


# Example:

file = open("data.txt", "r")

data = file.read()

x = 10 / 0

file.close()


# The program crashes at:
#
#     x = 10 / 0
#
# So this line is never reached:
#
#     file.close()
#
#
# This can leave the resource open.
#
# Therefore, manually managing resources can be risky.


# ============================================================
# 2. WITH STATEMENT SOLVES THIS
# ============================================================

with open("data.txt", "r") as file:
    data = file.read()


# Python automatically handles the cleanup.
#
# The file will be closed when the "with" block finishes.
#
# Even if an error occurs inside the block,
# Python still performs the cleanup.


# ============================================================
# 3. BASIC FLOW OF A CONTEXT MANAGER
# ============================================================

# Think of it like this:
#
#
#     Enter the context
#            ↓
#     Acquire resource
#            ↓
#     Run our code
#            ↓
#     Exit the context
#            ↓
#     Clean up resource
#
#
# Example:
#
#     with open("data.txt") as file:
#         data = file.read()
#
#
# Roughly:
#
#     Enter
#       ↓
#     Open file
#       ↓
#     Read file
#       ↓
#     Exit
#       ↓
#     Close file


# ============================================================
# 4. REAL-LIFE EXAMPLE
# ============================================================

# Imagine borrowing a book from a library.
#
#
# WITHOUT context manager:
#
#     Borrow book
#          ↓
#     Read book
#          ↓
#     Remember to return book
#
#
# You must remember the cleanup.
#
#
# WITH context manager:
#
#     Enter library
#          ↓
#     Borrow book
#          ↓
#     Read book
#          ↓
#     Leave library
#          ↓
#     Book is automatically returned
#
#
# This is the basic idea of a Context Manager.


# ============================================================
# 5. WITH STATEMENT - PARTS
# ============================================================

with open("data.txt", "r") as file:
    data = file.read()


# Here:
#
#     open("data.txt", "r")
#
# creates/manages the resource.
#
#
#     as file
#
# stores the resource in the variable "file".
#
#
# The indented code:
#
#     data = file.read()
#
# runs inside the context.


# ============================================================
# 6. __enter__() AND __exit__()
# ============================================================

# A Context Manager normally provides two special methods:
#
#     __enter__()
#     __exit__()
#
#
# Think of them as:
#
#     __enter__() → Enter the context / setup
#
#     __exit__()  → Leave the context / cleanup
#
#
# Roughly:
#
#
#     with something:
#         do_something()
#
#
# becomes conceptually:
#
#
#     something.__enter__()
#             ↓
#     do_something()
#             ↓
#     something.__exit__()
#
#
# Python handles these calls for us.


# ============================================================
# 7. OUR OWN CONTEXT MANAGER
# ============================================================

class MyContext:
    def __enter__(self):
        print("Entering")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting")

with MyContext():
    print("Inside")

# Output:
#
#     Entering
#     Inside
#     Exiting
#
# Flow:
#
#     MyContext()
#          ↓
#     __enter__()
#          ↓
#     Inside
#          ↓
#     __exit__()


# ============================================================
# 8. WHY DOES __exit__ HAVE 3 PARAMETERS?
# ============================================================

# The __exit__ method normally looks like:
#
#     def __exit__(self, exc_type, exc_value, traceback):
#
#
# These parameters give information about an exception
# if one occurs inside the "with" block.
#
#
# exc_type:
#     Type/class of the exception
#
# exc_value:
#     Actual exception object/value
#
# traceback:
#     Information about where the error occurred
#
#
# If there is NO exception:
#
#     exc_type   = None
#     exc_value  = None
#     traceback  = None
#
#
# So:
#
#     __exit__() can know whether an error happened.


# ============================================================
# 9. CONTEXT MANAGER WITH AN ERROR
# ============================================================

class MyContext:

    def __enter__(self):
        print("Entering")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting")

        print("Exception type:", exc_type)
        print("Exception value:", exc_value)


with MyContext():
    print("Inside")

    x = 10 / 0


# Output will be similar to:
#
#     Entering
#     Inside
#     Exiting
#     Exception type: <class 'ZeroDivisionError'>
#     Exception value: division by zero
#
#
# Notice:
#
# Even though an error occurred,
# __exit__() was still called.
#
# This is one of the most important purposes of
# Context Managers.


# ============================================================
# 10. __exit__ CAN SUPPRESS AN EXCEPTION
# ============================================================

class MyContext:

    def __enter__(self):
        print("Entering")

    def __exit__(self, exc_type, exc_value, traceback):

        print("Exiting")

        return True


with MyContext():

    print("Inside")

    x = 10 / 0


# Normally:
#
#     10 / 0
#
# would produce:
#
#     ZeroDivisionError
#
#
# But __exit__ returns True.
#
# Returning True tells Python:
#
#     "I handled the exception.
#      Don't raise it again."
#
#
# Therefore, the exception is suppressed.


# ============================================================
# 11. __exit__ RETURNING FALSE / NONE
# ============================================================

class MyContext:

    def __enter__(self):
        print("Entering")

    def __exit__(self, exc_type, exc_value, traceback):

        print("Exiting")

        return False


with MyContext():

    x = 10 / 0


# Returning False means:
#
#     "I did NOT handle the exception."
#
# Python will raise the exception normally.
#
#
# In practice, __exit__ often does not explicitly return
# anything.
#
# None behaves like False here.


# ============================================================
# 12. __enter__ CAN RETURN A VALUE
# ============================================================

# The value returned by __enter__() is assigned to the
# variable after "as".


class MyContext:

    def __enter__(self):
        print("Entering")

        return "Hello from context"

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting")


with MyContext() as value:

    print(value)


# Output:
#
#     Entering
#     Hello from context
#     Exiting
#
#
# This means:
#
#     __enter__()
#          ↓
#     returns "Hello from context"
#          ↓
#     value = "Hello from context"


# ============================================================
# 13. CONTEXT MANAGER WITH A RESOURCE
# ============================================================

class Database:

    def __enter__(self):

        print("Connecting to database")

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing database connection")

    def query(self):
        print("Running query")


with Database() as db:

    db.query()


# Output:
#
#     Connecting to database
#     Running query
#     Closing database connection
#
#
# This is a simplified example of how a resource can be
# automatically opened and closed.


# ============================================================
# 14. FILES ARE A REAL CONTEXT MANAGER
# ============================================================

with open("data.txt", "r") as file:

    data = file.read()

    print(data)


# After leaving the "with" block:
#
#     file.close()
#
# is automatically handled by the file's context manager.


# You can check:

with open("data.txt", "r") as file:

    print(file.closed)
    # False
    #
    # File is still open inside the context.


print(file.closed)
# True
#
# File has been closed after leaving the context.


# ============================================================
# 15. WHY CONTEXT MANAGERS ARE USEFUL
# ============================================================

# Context Managers are useful because they make sure that
# resources are cleaned up properly.
#
#
# WITHOUT:
#
#     resource = acquire()
#
#     do_work()
#
#     resource.close()
#
#
# WITH:
#
#     with resource:
#         do_work()
#
#
# The second approach is safer and cleaner.


# ============================================================
# 16. COMMON USE CASES
# ============================================================

# FILES
#
#     with open("data.txt") as file:
#         data = file.read()
#
#
# DATABASE CONNECTIONS
#
#     with database_connection() as connection:
#         connection.execute(...)
#
#
# LOCKS
#
#     with lock:
#         # protected code
#
#
# NETWORK CONNECTIONS
#
#     with connection:
#         # network operations
#
#
# TRANSACTIONS
#
#     with transaction:
#         # database operations


# ============================================================
# 17. contextlib - EASIER WAY
# ============================================================

# Python also provides the "contextlib" module.
#
# One useful tool is:
#
#     @contextmanager
#
#
# It allows us to create a context manager using a generator.


from contextlib import contextmanager

@contextmanager
def my_context():

    print("Entering")

    yield

    print("Exiting")

with my_context():
    print("Inside")


# Output:
#
#     Entering
#     Inside
#     Exiting
#
#
# The "yield" separates:
#
#     Before yield → entering/setup
#
#     After yield  → exiting/cleanup


# ============================================================
# 18. contextmanager WITH A VALUE
# ============================================================

@contextmanager
def message_context():

    print("Entering")

    yield "Hello"

    print("Exiting")


with message_context() as message:

    print(message)


# Output:
#
#     Entering
#     Hello
#     Exiting


# ============================================================
# 19. contextmanager WITH try/finally
# ============================================================

# For cleanup, try/finally is commonly used with
# @contextmanager.


@contextmanager
def my_resource():
    print("Resource acquired")
    try:
        yield
    finally:
        print("Resource cleaned up")

with my_resource():
    print("Using resource")


# Output:
#
#     Resource acquired
#     Using resource
#     Resource cleaned up
#
#
# The "finally" section runs even if an exception occurs.


# ============================================================
# 20. CONTEXT MANAGER WITH AN ERROR
# ============================================================

@contextmanager
def my_resource():

    print("Resource acquired")

    try:

        yield

    finally:

        print("Resource cleaned up")


with my_resource():

    print("Doing work")

    x = 10 / 0


# Even though an exception happens:
#
#     Resource cleaned up
#
# still runs because it is inside finally.


# ============================================================
# 21. SIMPLE COMPARISON
# ============================================================

# NORMAL RESOURCE MANAGEMENT:
#
#     resource = open_resource()
#
#     try:
#         use_resource()
#
#     finally:
#         close_resource()
#
#
# CONTEXT MANAGER:
#
#     with resource:
#         use_resource()
#
#
# Context Managers make resource management cleaner.


# ============================================================
# 22. IMPORTANT KEYWORDS / METHODS
# ============================================================

# with
#     Starts a context manager block.
#
#
# __enter__()
#     Runs when entering the context.
#
#
# __exit__()
#     Runs when leaving the context.
#
#
# as
#     Stores the value returned by __enter__().
#
#
# @contextmanager
#     Decorator from contextlib for creating context managers.
#
#
# yield
#     Separates setup from the code inside the context.
#
#
# finally
#     Used to guarantee cleanup.


# ============================================================
# 23. FINAL CHEAT SHEET
# ============================================================

# CONTEXT MANAGER
#
#     A mechanism for automatically managing resources.
#
#
# MAIN SYNTAX:
#
#     with resource as variable:
#         code
#
#
# BASIC FLOW:
#
#     with
#       ↓
#     __enter__()
#       ↓
#     code inside block
#       ↓
#     __exit__()
#       ↓
#     cleanup
#
#
# __enter__()
#     Setup / acquire resource
#
#
# __exit__()
#     Cleanup / release resource
#
#
# __exit__(exc_type, exc_value, traceback)
#     Can inspect exceptions.
#
#
# __exit__ returning True
#     Suppresses the exception.
#
#
# __exit__ returning False/None
#     Exception continues normally.
#
#
# __enter__ return value
#     Goes into the variable after "as".
#
#
# Example:
#
#     with MyContext() as value:
#         print(value)
#
#
# means conceptually:
#
#     value = MyContext().__enter__()
#
#     try:
#         print(value)
#
#     finally:
#         __exit__()
#
#
# ============================================================
# MOST IMPORTANT EXAMPLE
# ============================================================

class MyContext:

    def __enter__(self):

        print("Entering context")

        return self

    def __exit__(self, exc_type, exc_value, traceback):

        print("Leaving context")


with MyContext() as obj:

    print("Inside context")


# Output:
#
#     Entering context
#     Inside context
#     Leaving context
#
#
# REMEMBER:
#
#     Context Manager
#          ↓
#     Automatically manages resources
#
#     __enter__()
#          ↓
#     Setup / acquire
#
#     __exit__()
#          ↓
#     Cleanup / release
#
#     with
#          ↓
#     Makes this process automatic and readable.