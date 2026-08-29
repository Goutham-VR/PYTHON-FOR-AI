# ============================================================
# TYPE HINTS IN PYTHON
# PART 8: CALLABLE TYPE HINTS
# ============================================================


# ============================================================
# 1. WHAT IS CALLABLE?
# ============================================================

# In Python, functions are objects.
#
# This means we can:
#
#     - store a function in a variable
#     - pass a function to another function
#     - return a function from a function
#
#
# Example:

def add(a, b):
    return a + b


# We can store the function in a variable:

x = add


# Now:
#
# x refers to the add function.


print(x(10, 20))


# Output:
#
# 30


# ============================================================
# 2. FUNCTION AS AN ARGUMENT
# ============================================================

def add(a, b):
    return a + b


def execute(func):
    return func(10, 20)


result = execute(add)

print(result)


# Output:
#
# 30


# Here:
#
# add
#     ↓
# passed as an argument
#     ↓
# execute()
#     ↓
# func
#     ↓
# calls add()


# ============================================================
# 3. BASIC CALLABLE TYPE HINT
# ============================================================

from typing import Callable


def execute(func: Callable):
    return func()


# Callable means:
#
# func is expected to be something
# that can be called.
#
#
# A function is callable.


# Example:

def say_hello():
    print("Hello")


execute(say_hello)


# Output:
#
# Hello


# ============================================================
# 4. WHAT DOES "CALLABLE" MEAN?
# ============================================================

# Something is callable if we can use:
#
# ()
#
# with it.


def hello():
    print("Hello")


hello()


# hello is callable.


# Functions are callable.


# There are also other callable objects
# in Python, but functions are the most common
# example when learning Callable.


# ============================================================
# 5. MORE SPECIFIC CALLABLE
# ============================================================

# We can describe:
#
#     parameter types
#     return type
#
# using Callable.


Callable[[int, int], int]


# Read this as:
#
# Callable[
#     [parameter types],
#     return type
# ]
#
#
# Therefore:
#
# Callable[[int, int], int]
#
# means:
#
# function accepts:
#
#     int
#     int
#
# and returns:
#
#     int


# ============================================================
# 6. EXAMPLE WITH ADD
# ============================================================

def add(a: int, b: int) -> int:
    return a + b


# The function:
#
# accepts:
#
#     int
#     int
#
# returns:
#
#     int


# Therefore its function type is:

Callable[[int, int], int]


# ============================================================
# 7. USING CALLABLE AS A PARAMETER
# ============================================================

def execute(
    func: Callable[[int, int], int]
) -> None:

    print(func(10, 20))


# The parameter:
#
# func
#
# must be a callable that:
#
#     accepts int
#     accepts int
#     returns int


execute(add)


# Output:
#
# 30


# ============================================================
# 8. UNDERSTANDING THE STRUCTURE
# ============================================================

func: Callable[[int, int], int]


# Break it down:
#
#
# Callable
#     ↓
#     This is a callable function/object.
#
#
# [int, int]
#     ↓
#     It accepts two parameters.
#
#
# int
#     ↓
#     It returns an integer.
#
#
# Therefore:
#
# Callable[[int, int], int]
#
# =
#
# Function
#     ↓
# 2 parameters
#     ↓
# int, int
#     ↓
# returns int


# ============================================================
# 9. CALLABLE WITH ONE PARAMETER
# ============================================================

Callable[[str], int]


# Means:
#
# function accepts:
#
#     1 parameter
#
# parameter type:
#
#     str
#
# return type:
#
#     int


# Example:

def get_length(text: str) -> int:
    return len(text)


# This matches:

Callable[[str], int]


# Because:
#
# Input:
#     str
#
# Output:
#     int


# ============================================================
# 10. USING THE FUNCTION
# ============================================================

def execute(func: Callable[[str], int]) -> None:
    result = func("Hello")
    print(result)


execute(get_length)


# Output:
#
# 5


# Why?
#
# "Hello"
#     ↓
# str
#     ↓
# get_length()
#     ↓
# 5
#     ↓
# int


# ============================================================
# 11. CALLABLE WITH NO PARAMETERS
# ============================================================

Callable[[], str]


# This means:
#
# function accepts:
#
#     no parameters
#
# and returns:
#
#     str


# Example:

def get_name() -> str:
    return "Alice"


# This matches:

Callable[[], str]


# ============================================================
# 12. FUNCTION ACCEPTING A FUNCTION
# ============================================================

def execute(func: Callable[[], str]) -> str:
    return func()


def get_name() -> str:
    return "Alice"


result = execute(get_name)

print(result)


# Output:
#
# Alice


# Breakdown:
#
# get_name
#     ↓
# accepts no parameters
#     ↓
# returns str
#
#
# Therefore:
#
# Callable[[], str]


# ============================================================
# 13. CALLABLE WITH THREE PARAMETERS
# ============================================================

Callable[[int, int, int], int]


# Means:
#
# function accepts:
#
#     parameter 1 -> int
#     parameter 2 -> int
#     parameter 3 -> int
#
# returns:
#
#     int


# Example:

def add_three(a: int, b: int, c: int) -> int:
    return a + b + c


# add_three matches:
#
# Callable[[int, int, int], int]


# ============================================================
# 14. CALLABLE WITH DIFFERENT PARAMETER TYPES
# ============================================================

Callable[[str, int], bool]


# Means:
#
# parameter 1 -> str
# parameter 2 -> int
# return      -> bool


# Example:

def check_name(name: str, age: int) -> bool:
    return age >= 18


# This matches:

Callable[[str, int], bool]


# ============================================================
# 15. CALLABLE WITH LIST PARAMETER
# ============================================================

Callable[[list[int]], int]


# Means:
#
# function accepts:
#
#     list[int]
#
# and returns:
#
#     int


# Example:

def calculate_total(numbers: list[int]) -> int:
    return sum(numbers)


# This matches:
#
# Callable[[list[int]], int]


# ============================================================
# 16. CALLABLE WITH OPTIONAL RETURN
# ============================================================

Callable[[int], str | None]


# Means:
#
# function accepts:
#
#     int
#
# and returns:
#
#     str
# OR
#     None


# Example:

def find_student(id: int) -> str | None:

    if id == 1:
        return "Alice"

    return None


# This matches:
#
# Callable[[int], str | None]


# ============================================================
# 17. CALLABLE WITH UNION PARAMETERS
# ============================================================

Callable[[int | str], str]


# Means:
#
# function accepts one parameter.
#
# The parameter can be:
#
#     int
# OR
#     str
#
# The function returns:
#
#     str


# Example:

def convert(value: int | str) -> str:
    return str(value)


# This matches:
#
# Callable[[int | str], str]


# ============================================================
# 18. CALLABLE AND DECORATORS
# ============================================================

# This is where Callable becomes
# especially useful.
#
# A decorator receives a function
# and usually returns a function.


def decorator(func: Callable) -> Callable:

    def wrapper():
        print("Before function")
        func()
        print("After function")

    return wrapper


# Here:
#
# func -> Callable
#
# and:
#
# wrapper -> function
#
# decorator() returns a Callable.


# ============================================================
# 19. MORE SPECIFIC DECORATOR
# ============================================================

def decorator(
    func: Callable[[int], int]
) -> Callable[[int], int]:

    def wrapper(value: int) -> int:
        print("Before function")

        result = func(value)

        print("After function")

        return result

    return wrapper


# Here the decorator expects:
#
# Callable[[int], int]
#
# and returns:
#
# Callable[[int], int]
#
#
# Meaning:
#
# Input function:
#
#     int -> int
#
# Output function:
#
#     int -> int


# ============================================================
# 20. USING THE DECORATOR
# ============================================================

def double(value: int) -> int:
    return value * 2


double = decorator(double)


print(double(10))


# Output:
#
# Before function
# After function
# 20


# This demonstrates why Callable
# is useful when working with decorators.


# ============================================================
# 21. FUNCTION RETURNING A FUNCTION
# ============================================================

def create_multiplier(
    number: int
) -> Callable[[int], int]:

    def multiply(value: int) -> int:
        return value * number

    return multiply


# The return type:
#
# Callable[[int], int]
#
# means:
#
# the function returns another function
# that:
#
# accepts an int
# and returns an int.


double = create_multiplier(2)


print(double(10))


# Output:
#
# 20


# ============================================================
# 22. CALLABLE VS NORMAL FUNCTION TYPE HINT
# ============================================================

def execute(func: Callable):
    func()


# Callable means:
#
# func is expected to be callable.
#
#
# This is useful when we don't need
# to specify the exact parameters
# and return type.


# But if we know them:

def execute(
    func: Callable[[int, int], int]
):
    print(func(10, 20))


# This provides much more information
# to the type checker.


# ============================================================
# 23. QUICK REFERENCE
# ============================================================

# Any callable:

Callable


# No parameters, returns string:

Callable[[], str]


# One string parameter, returns integer:

Callable[[str], int]


# One integer parameter, returns string:

Callable[[int], str]


# Two integer parameters, returns integer:

Callable[[int, int], int]


# Three integer parameters, returns integer:

Callable[[int, int, int], int]


# Integer OR string parameter, returns string:

Callable[[int | str], str]


# Integer parameter, returns string OR None:

Callable[[int], str | None]


# List of integers parameter, returns integer:

Callable[[list[int]], int]


# ============================================================
# 24. QUICK SUMMARY
# ============================================================

# Basic:

Callable


# Means:
#
# some callable object/function.


# More specific:

Callable[[int, int], int]


# Means:
#
# accepts:
#     int
#     int
#
# returns:
#     int


# One parameter:

Callable[[str], int]


# Means:
#
# accepts:
#     str
#
# returns:
#     int


# No parameters:

Callable[[], str]


# Means:
#
# accepts:
#     nothing
#
# returns:
#     str


# ============================================================
# KEY IDEA
# ============================================================
#
# Callable is used when a function itself
# is being passed around as data.
#
#
# Example:
#
# def execute(func: Callable):
#     func()
#
#
# More specifically:
#
# Callable[[int, int], int]
#
# means:
#
#     Function
#         ↓
#     parameter 1 -> int
#     parameter 2 -> int
#         ↓
#     returns int
#
#
# Another example:
#
# Callable[[str], int]
#
# means:
#
#     Function
#         ↓
#     one parameter -> str
#         ↓
#     returns int
#
#
# Callable is especially important for:
#
#     - Functions as arguments
#     - Higher-order functions
#     - Decorators
#     - Callbacks
#     - Function factories
#
#
# Remember:
#
# Callable[
#     [parameter types],
#     return type
# ]
#
# ============================================================